'use strict';
const test=require('node:test'), assert=require('node:assert/strict');
const {createReview}=require('./review');
const version='a'.repeat(40), newer='b'.repeat(40);
function harness() {
    const handlers=new Map(), values=new Map(), calls=[], errors=[], threads=[], providers=new Map(), editorCalls=[];
    const disposable=()=>({dispose(){}});
    const ctx={repo:require('node:path').resolve('fixture'),owner:'reply.tex',id:'a',version,side:'candidate'};
    class Uri {
        constructor(v){Object.assign(this,v);}
        static from(v){return new Uri(v);}
        static file(file){return new Uri({scheme:'file',fsPath:file,path:file});}
        toString(){return this.scheme+':'+this.path+'?'+this.query;}
    }
    class Range {
        constructor(a,b){this.start=a;this.end=b;this.isEmpty=a.character===b.character;}
    }
    const text='🙂 This is too strong.';
    const resource=Uri.from({scheme:'latex-review',path:'/a/candidate.tex',query:JSON.stringify(ctx)});
    const doc={uri:resource,getText:r=>r?text.slice(r.start.character,r.end.character):text,
        positionAt:character=>({line:0,character}),offsetAt:p=>p.character};
    const editor={document:doc,selection:new Range(doc.positionAt(11),doc.positionAt(text.length))};
    const api={Uri,Range,MarkdownString:class {constructor(){this.value='';}appendText(x){this.value+=x;}},
        CommentMode:{Preview:1},CommentThreadCollapsibleState:{Collapsed:0,Expanded:1},RelativePattern:class{},
        env:{clipboard:{writeText:async()=>{}}},
        commands:{registerCommand:(name,fn)=>{handlers.set(name,fn);return disposable();},executeCommand:async(name,...args)=>{
            editorCalls.push({name,args});
            if(name==='setContext'){values.set(args[0],args[1]);return;}
            return handlers.get(name)?.(...args);
        }},
        workspace:{isTrusted:true,textDocuments:[],getConfiguration:()=>({get:(name,fallback)=>fallback}),getWorkspaceFolder:()=>({}),
            registerTextDocumentContentProvider:(scheme,p)=>{providers.set(scheme,p);return disposable();},openTextDocument:async()=>doc},
        comments:{createCommentController:()=>({createCommentThread:(uri,range,comments)=>{const t={uri,range,comments,dispose(){this.disposed=true;}};threads.push(t);return t;},dispose(){}})},
        window:{activeTextEditor:editor,tabGroups:{activeTabGroup:{activeTab:{input:{modified:resource}}},onDidChangeTabs:()=>disposable()},
            onDidChangeActiveTextEditor:()=>disposable(),registerUriHandler:()=>disposable(),showErrorMessage:x=>errors.push(x),
            showWarningMessage:x=>errors.push(x),showInformationMessage:()=>{}}
    };
    let currentVersion=version;
    const data=()=>({sha256:'owner-sha',version,original:'Original.',candidate:text,source_match:true,
        edit:{file:'reply.tex',versions:[currentVersion],status:'pending',requests:[]}});
    const execute=async(command,args,cwd,input)=>{
        calls.push({command,args,cwd,input});
        if(args.includes('inspect'))return JSON.stringify(data());
        if(args.includes('feedback'))return JSON.stringify({rewritten:false});
        if(args.includes('decide'))return '{}';
        throw new Error('Unexpected backend command');
    };
    const review=createReview(api,{subscriptions:[]},execute);
    return {review,api,ctx,editor,doc,threads,calls,handlers,errors,editorCalls,newVersion:()=>{currentVersion=newer;}};
}

test('selected Unicode text posts exact code-point anchor and requirement through the existing state helper',async()=>{
    const h=harness(), thread=await h.review.annotate();
    await h.review.post({thread,text:'语气弱一点\n保留依据'});
    const call=h.calls.find(x=>x.args.includes('feedback'));
    assert(call); assert(call.args.includes('--apply')); assert(call.args.includes('--expect'));
    assert.equal(call.input.version,version);assert.equal(call.input.side,'candidate');
    assert.equal(call.input.start,10); // UTF-16 offset 11 follows a two-code-unit emoji
    assert.equal(call.input.quote,'too strong.');assert.equal(call.input.text,'语气弱一点\n保留依据');
    assert.equal(thread.disposed,true);
});
test('dirty source buffer and stale displayed version both prevent any decision process',async()=>{
    const h=harness();
    h.api.workspace.textDocuments=[{uri:h.api.Uri.file(require('node:path').join(h.ctx.repo,'reply.tex')),isDirty:true}];
    await assert.rejects(h.review.decide('accept'),/未保存/);
    assert(!h.calls.some(x=>x.args.includes('decide')));
    h.api.workspace.textDocuments=[];h.newVersion();
    await assert.rejects(h.review.decide('reject'),/候选已更新/);
    assert(!h.calls.some(x=>x.args.includes('decide')));
});
test('restricted mode never launches a backend and annotations reject an unrelated editor',async()=>{
    const h=harness();h.api.workspace.isTrusted=false;
    const count=h.calls.length;
    await assert.rejects(h.review.decide('accept'),/受限模式/);
    assert.equal(h.calls.length,count);
    h.api.workspace.isTrusted=true;
    h.api.window.activeTextEditor={document:{uri:h.api.Uri.file('unrelated.tex')}};
    await assert.rejects(h.review.annotate(),/点击原文或候选/);
    assert(!h.calls.some(x=>x.args.includes('feedback')));
});
test('review tab names identify immutable candidates without a stale author-decision label',async()=>{
    const h=harness();await h.review.open(h.ctx);
    const shown=h.editorCalls.find(x=>x.name==='vscode.diff');
    assert(shown);assert.match(shown.args[2],/候选 v1/);
    assert(!/pending|accepted|rejected|rework/.test(shown.args[2]));
});
