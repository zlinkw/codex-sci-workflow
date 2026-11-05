'use strict';
// Retired source: no activation from main.js and not shipped; retain until next confirmed cleanup.
// Native read-only diff + comments. The Python helper owns every durable decision.
const cp = require('node:child_process');
const path = require('node:path');
const fs = require('node:fs/promises');
const SCHEME = 'latex-review';
const OPEN = new Set(['pending', 'rework']);

function run(command, args, cwd, input) {
    return new Promise((resolve, reject) => {
        const env = {...process.env, PYTHONUTF8: '1'};
        for (const k of Object.keys(env)) if (/^GIT_/i.test(k)) delete env[k];
        const child = cp.execFile(command, args, {cwd, env, windowsHide: true, timeout: 120000,
            encoding: 'utf8', maxBuffer: 8 * 1024 * 1024}, (error, out, err) => {
            if (error) reject(new Error(err.trim() || out.trim() || error.message));
            else resolve(out);
        });
        child.stdin.end(input === undefined ? undefined : JSON.stringify(input));
    });
}
function parse(uri) {
    if (!uri || uri.scheme !== SCHEME) return undefined;
    const value = JSON.parse(uri.query);
    if (!value || typeof value.repo !== 'string' || !path.isAbsolute(value.repo) ||
        typeof value.owner !== 'string' || path.isAbsolute(value.owner) || value.owner.split(/[\\/]/).includes('..') ||
        !value.owner.endsWith('.tex') || !/^(?:[1-9][0-9]*|[a-z]+)$/.test(value.id) ||
        !/^(?:[a-f0-9]{40}|[a-f0-9]{64})$/.test(value.version) || !['original', 'candidate'].includes(value.side)) {
        throw new Error('审核文档身份无效。');
    }
    return value;
}
function key(c) { return JSON.stringify([c.repo, c.owner, c.id, c.version]); }
function activate(context) { return createReview(require('vscode'), context); }

function createReview(vscode, context, execute = run) {
    const cache = new Map(), threads = new Map();
    let busy = false;
    const controller = vscode.comments.createCommentController('localLatexReview', '论文修改审核');
    controller.options = {prompt: '填写具体返修要求', placeHolder: '例如：语气弱一点，保留前半句；提交后由 Codex 处理。'};
    context.subscriptions.push(controller);
    const uri = c => vscode.Uri.from({scheme: SCHEME, path: `/${c.id}/${c.side}.tex`, query: JSON.stringify(c)});
    const active = () => {
        const editor = vscode.window.activeTextEditor;
        if (editor?.document.uri.scheme === SCHEME) return parse(editor.document.uri);
        const tab = vscode.window.tabGroups?.activeTabGroup.activeTab;
        return parse(tab?.input?.modified);
    };
    function trusted(c) {
        if (!vscode.workspace.isTrusted) throw new Error('当前工作区处于受限模式，审核写入未启用。');
        if (!vscode.workspace.getWorkspaceFolder(vscode.Uri.file(c.repo))) throw new Error('请先在 VS Code 打开该论文仓库根目录。');
    }
    async function backend(c, args, input, expect) {
        trusted(c);
        const cfg = vscode.workspace.getConfiguration('localLatex');
        const argv = ['-X', 'utf8', path.join(__dirname, 'source_review.py'), '--repo', c.repo, '--state', c.owner,
            '--git', cfg.get('gitPath', 'git')];
        if (expect) argv.push('--apply', '--expect', expect);
        return JSON.parse(await execute(cfg.get('pythonPath', 'python'), [...argv, ...args], c.repo, input));
    }
    async function inspect(c, fresh = false) {
        trusted(c);
        if (!fresh && cache.has(key(c))) return cache.get(key(c));
        const data = await backend(c, ['inspect', '--id', c.id, '--version', c.version]);
        cache.set(key(c), data);
        return data;
    }
    function checkBuffers(c, file) {
        const targets = [path.resolve(c.repo, c.owner), path.resolve(c.repo, file)].map(x => x.toLowerCase());
        for (const doc of vscode.workspace.textDocuments) {
            if (doc.uri.scheme === 'file' && targets.includes(path.resolve(doc.uri.fsPath).toLowerCase()) && doc.isDirty) {
                throw new Error('对应源码或审核状态文件有未保存的手改，请先保存并核对；未自动覆盖。');
            }
        }
    }
    async function current(c) {
        const data = await inspect(c, true);
        if (!OPEN.has(data.edit.status)) throw new Error('这一项已有作者决定，请查看下一项。');
        if (data.edit.versions.at(-1) !== c.version) throw new Error('候选已更新，请重开最新差异后再操作。');
        if (!data.source_match) throw new Error('真实源码与候选不再匹配，请先让 Codex 核对手改，未覆盖任何内容。');
        checkBuffers(c, data.edit.file);
        return data;
    }
    async function refreshContext() {
        let c;
        try { c = active(); } catch (_) { /* not a valid review document */ }
        await vscode.commands.executeCommand('setContext', 'localLatex.reviewActive', !!c);
        let enabled = false;
        if (c && vscode.workspace.isTrusted) {
            try {
                const data = await inspect(c);
                enabled = OPEN.has(data.edit.status) && data.edit.versions.at(-1) === c.version && data.source_match;
            } catch (_) { /* disabled; an explicit action will explain the exact error */ }
        }
        await vscode.commands.executeCommand('setContext', 'localLatex.reviewPending', enabled);
    }
    function codePointToUtf16(text, n) { return Array.from(text).slice(0, n).join('').length; }
    async function syncThreads(c, data) {
        const prefix = JSON.stringify([c.repo, c.owner, c.id]);
        for (const [id, entry] of threads) {
            if (entry.scope === prefix) { entry.thread.dispose(); threads.delete(id); }
        }
        for (const note of data.edit.requests || []) {
            const target = {...c, side: note.side, version: note.version};
            const snapshot = note.version === c.version ? data : await inspect(target);
            const text = snapshot[note.side];
            const doc = await vscode.workspace.openTextDocument(uri(target));
            const range = new vscode.Range(doc.positionAt(codePointToUtf16(text, note.start)), doc.positionAt(codePointToUtf16(text, note.end)));
            const markdown = new vscode.MarkdownString();
            markdown.appendText(note.text); // untrusted author text: no commands/HTML
            const thread = controller.createCommentThread(uri(target), range, [{body: markdown,
                mode: vscode.CommentMode.Preview, author: {name: '作者'}, label: note.status === 'open' ? '待 Codex 返修' : note.status}]);
            thread.label = `${c.id} · ${note.side === 'original' ? '原文' : '候选'}批注`;
            thread.contextValue = 'localLatexReview';
            thread.canReply = OPEN.has(data.edit.status) && note.version === data.edit.versions.at(-1);
            thread.collapsibleState = vscode.CommentThreadCollapsibleState.Collapsed;
            threads.set(note.id, {thread, scope: prefix});
        }
    }
    async function open(c) {
        const data = await inspect(c, true);
        const selected = {...c, version: data.edit.versions.at(-1)};
        if (selected.version !== c.version) return open(selected);
        await vscode.commands.executeCommand('vscode.diff', uri({...selected, side: 'original'}), uri({...selected, side: 'candidate'}),
            `${c.id} · ${data.edit.file} · 原文 ↔ 候选 v${data.edit.versions.length}`, {preview: false});
        await syncThreads(selected, data);
        await refreshContext();
    }
    async function discover() {
        const prior = active();
        if (prior) return prior;
        if (!vscode.workspace.isTrusted) throw new Error('请在已有受信任的本地论文工作区使用审核入口。');
        const doc = vscode.window.activeTextEditor?.document;
        const folder = doc?.uri.scheme === 'file' ? vscode.workspace.getWorkspaceFolder(doc.uri) : vscode.workspace.workspaceFolders?.[0];
        if (!folder) throw new Error('请先打开本地论文文件夹。');
        const cfg = vscode.workspace.getConfiguration('localLatex');
        const repo = (await execute(cfg.get('gitPath', 'git'), ['rev-parse', '--show-toplevel'], folder.uri.fsPath)).trim();
        trusted({repo});
        const files = await vscode.workspace.findFiles(new vscode.RelativePattern(repo, '**/*.tex'), '**/{.git,.latex-build,clean_dir,node_modules}/**');
        const owners = [];
        for (const file of files) {
            const text = await fs.readFile(file.fsPath, 'utf8');
            if (text.includes('% CODEX-REVIEW-STATE-BEGIN') && text.includes('% CODEX-REVIEW-DATA ')) owners.push(file.fsPath);
        }
        if (owners.length !== 1) throw new Error(owners.length ? '发现多个审核状态块，请先核对唯一归属。' : '项目尚未登记干净源码审核，请先让 Codex 建立本轮审核基线和编号。');
        return {repo, owner: path.relative(repo, owners[0]).split(path.sep).join('/')};
    }
    async function select(next = false) {
        const c = await discover();
        const state = await backend(c, ['status']);
        const choices = Object.entries(state.edits || {}).filter(([, edit]) => OPEN.has(edit.status)).map(([id, edit]) => ({
            label: `${id} · ${edit.file}`, description: edit.location || edit.status,
            detail: `${edit.source_match ? '' : '源码有冲突；'}${(edit.requests || []).filter(x => x.status === 'open').length} 条待处理批注`,
            ctx: {repo: c.repo, owner: c.owner, id, version: edit.versions.at(-1), side: 'candidate'}}));
        if (!choices.length) return vscode.window.showInformationMessage('没有待审修改。已接收不等于审稿问题已解决。');
        const position = choices.findIndex(x => x.ctx.id === c.id);
        const picked = next ? choices[(position + 1) % choices.length] : await vscode.window.showQuickPick(choices, {placeHolder: '选择一项查看差异；点击接收、拒绝，或选中文字添加返修批注'});
        if (picked) await open(picked.ctx);
    }
    async function decide(action) {
        const c = active();
        if (!c) throw new Error('请先打开“审核待审修改”中的差异。');
        const data = await current(c);
        await backend(c, ['decide', action === 'accept' ? '--accept' : '--reject', c.id, '--version', c.version], undefined, data.sha256);
        cache.delete(key(c));
        const updated = await inspect(c, true);
        await syncThreads(c, updated);
        await refreshContext();
        vscode.window.showInformationMessage(`${c.id} 已${action === 'accept' ? '接收' : '拒绝'}。原有暂存保持不变，提交前请核对；未编译或推送。`);
    }
    async function annotate(whole = false) {
        const c = active();
        if (!c) throw new Error('请先打开编号差异。');
        await current(c);
        let editor = vscode.window.activeTextEditor;
        if (!editor || editor.document.uri.scheme !== SCHEME) throw new Error('请先点击原文或候选中的文字。');
        let range = editor.selection;
        if (whole || range.isEmpty) range = new vscode.Range(editor.document.positionAt(0), editor.document.positionAt(editor.document.getText().length));
        const thread = controller.createCommentThread(editor.document.uri, range, []);
        thread.contextValue = 'localLatexReview';
        thread.label = `${c.id} · 填写返修要求后点击“保存返修批注”`;
        thread.canReply = true;
        thread.collapsibleState = vscode.CommentThreadCollapsibleState.Expanded;
        return thread;
    }
    async function post(reply) {
        if (!reply?.thread || !reply.text?.trim()) throw new Error('请输入具体返修要求。');
        const c = parse(reply.thread.uri);
        if (!c) throw new Error('不是本地论文审核批注。');
        const data = await current(c);
        const doc = await vscode.workspace.openTextDocument(reply.thread.uri);
        const range = reply.thread.range || new vscode.Range(doc.positionAt(0), doc.positionAt(doc.getText().length));
        const start = Array.from(doc.getText().slice(0, doc.offsetAt(range.start))).length;
        const end = Array.from(doc.getText().slice(0, doc.offsetAt(range.end))).length;
        await backend(c, ['feedback'], {id: c.id, version: c.version, side: c.side, start, end,
            quote: doc.getText(range), text: reply.text}, data.sha256);
        reply.thread.dispose(); // display-only draft; durable annotation is in the canonical state
        cache.delete(key(c));
        await syncThreads(c, await inspect(c, true));
        await refreshContext();
        vscode.window.showInformationMessage('返修批注已保存，正文尚未改写。对 Codex 说“处理待返修批注”即可，不用输入编号。');
    }
    async function copyRequests() {
        const c = await discover(), state = await backend(c, ['status']);
        const notes = Object.entries(state.edits || {}).flatMap(([id, edit]) => (edit.requests || []).filter(n => n.status === 'open').map(n => `${id}（${edit.file}）：${n.text}`));
        if (!notes.length) return vscode.window.showInformationMessage('没有待处理的返修批注。');
        await vscode.env.clipboard.writeText(`请读取 ${c.owner} 内唯一 CODEX-REVIEW-STATE，处理以下已保存的返修批注。保留原文和编号，候选修改后仍待审核，不自动接收。\n${notes.join('\n')}`);
        vscode.window.showInformationMessage('返修指令已复制，可粘贴给当前 Codex 会话；未自动发送或调用其他代理。');
    }
    function command(name, handler) {
        context.subscriptions.push(vscode.commands.registerCommand(name, async (...args) => {
            if (busy) return vscode.window.showWarningMessage('当前审核操作尚未结束。');
            busy = true;
            try { return await handler(...args); }
            catch (error) { vscode.window.showErrorMessage(error.message); }
            finally { busy = false; }
        }));
    }
    context.subscriptions.push(vscode.workspace.registerTextDocumentContentProvider(SCHEME, {
        provideTextDocumentContent: async resource => { const c = parse(resource); if (!c) throw new Error('Invalid review URI'); return (await inspect(c))[c.side]; }
    }));
    controller.commentingRangeProvider = {provideCommentingRanges(document) {
        const c = parse(document.uri), data = c && cache.get(key(c));
        return data && OPEN.has(data.edit.status) && data.edit.versions.at(-1) === c.version ?
            [new vscode.Range(document.positionAt(0), document.positionAt(document.getText().length))] : [];
    }};
    command('localLatex.reviewChanges', () => vscode.commands.executeCommand('localLatex.inlineReview'));
    command('localLatex.reviewNext', () => select(true));
    command('localLatex.reviewAccept', () => decide('accept'));
    command('localLatex.reviewReject', () => decide('reject'));
    command('localLatex.reviewRework', () => annotate(true));
    command('localLatex.reviewAnnotate', () => annotate());
    command('localLatex.reviewPostComment', post);
    command('localLatex.reviewCopyRequests', copyRequests);
    // Explicit open only: an external URI can never decide or modify a paper.
    context.subscriptions.push(vscode.window.registerUriHandler({async handleUri(resource) {
        try {
            if (resource.path !== '/review') throw new Error('不支持的审核入口。');
            const q = new URLSearchParams(resource.query);
            const c = {repo: q.get('repo'), owner: q.get('state'), id: q.get('id')};
            trusted(c);
            const state = await backend(c, ['status']);
            const edit = state.edits[c.id];
            if (!edit) throw new Error('没有该审核编号。');
            await vscode.commands.executeCommand('localLatex.inlineReviewAt', {...c, version: edit.versions.at(-1), side: 'candidate'});
        } catch (error) { vscode.window.showErrorMessage(error.message); }
    }}));
    context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor(() => {refreshContext().catch(() => {});}));
    context.subscriptions.push(vscode.window.tabGroups.onDidChangeTabs(() => {refreshContext().catch(() => {});}));
    refreshContext().catch(() => {});
    return {open, inspect, current, post, annotate, decide, controller, refreshContext};
}
module.exports = {activate, createReview, parse, SCHEME};
