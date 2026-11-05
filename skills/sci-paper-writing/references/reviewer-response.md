# Reviewer response writing

Entry guard: apply the active [SKILL.md](../SKILL.md) kernel and its real top/local-comment gate first. If the kernel is absent, read it once; this backlink does not rerun routing. Other links activate only for an actual task condition, never recursive preload.

## Pre-writing excerpt agreement

Before composing the letter or individual replies, read the response file's top comment rules/profile for the author's decision on including revised manuscript excerpts. If no clear decision exists, ask whether to include them and record the answer there before reply drafting. A pending decision is not permission to choose either option. Reuse an existing confirmed choice across review batches without repeated questions. Continue independent inspection and manuscript work while awaiting the answer. Keep this agreement in the actual response file's existing top comments, not a sidecar or second review-state block.

If excerpts are requested, prepare each complete substantive response together with its manuscript revisions, but do not repeatedly insert provisional excerpts. Keep the exact source associations and remaining final-assembly dependency in existing local comments/state. After all relevant revisions and author decisions are finished, perform unified red highlighting against the fixed baseline, insert the agreed final revised passages under the corresponding replies, then verify wording, symbols, colors and final locators against that same manuscript version. Do not announce an excerpt below before it has been inserted. Further source changes require refreshing the affected excerpts. If excerpts are declined, provide full explanations and real locations without copying the manuscript. Either choice preserves mandatory opening thanks, issue coverage, evidence checks and question-level manuscript/reply coordination.

## Manuscript-first response workflow

1. Preserve each reviewer/editor comment verbatim, its reviewer identity and numbering. Use the complete question as the normal work unit, covering all subrequests through coordinated manuscript revisions, relevant cross-reviewer consistency checks and one complete response entry. Do not stop after an isolated wording change or defer the reply merely because review cards are separate. Related comments may share a manuscript fix, but each retains its own complete answer. Respect an explicit author request for a narrower task. Record coverage and links in the existing state. A missing fact or required experiment keeps the question open and is clarified with the author, never guessed or hidden by partial completion.
2. Locate the existing passages that should carry the clarification, their preceding local plans and supporting evidence. Apply the revision length tradeoff below before deciding to add prose. Load the actual target chapter module before drafting its scientific change, adding notation rules only for equation/symbol work. Within the authorized scope, address research positioning, evidence, method explanation and structural changes before language polish, courtesy phrases and layout. Group comments with a shared underlying problem into a coherent manuscript fix, while retaining an adequate answer for each reviewer. Revise the manuscript before drafting a reply about those revisions.
   Reuse the kernel's automatic review gate and the revision module's manuscript/reply synchronization protocol, including stale dependencies without open annotations. A response-only clarification or justified non-change does not require a manufactured manuscript edit.
3. Read the exact revised passages, equations, captions and supporting evidence for the version being answered, then derive the reply from those contents using the mandatory response structure below. Do not substitute an edit plan, old draft, assumed implementation detail or intended result for the actual revised wording. A reply depending on unaccepted candidates must match their current generation and remain a draft, not describe them as accepted source. Distinguish original content from actual additions/corrections and recheck after rework or acceptance.
4. Attach a source comment before each affected response entry, for example `% CODEX-RESPONSE reviewer=R1-Q2 changes=1,3`. `changes` lists manuscript numeric dependencies; response edits carry letter IDs in the canonical state. This marker only locates dependencies: do not mirror author decisions or issue status here. An older local `status=` value is nonauthoritative and cannot override the sole state; reconcile it in scoped authorized writing, without a project-wide comment rewrite during an audit.
   For question lookup, add `% CODEX-QUESTION {"id":"R1-Q2","file":"reviewer-comments.tex","quote":"Exact original reviewer wording."}` in this same local comment area. The example filename is illustrative, never a required project filename or an instruction to create another file. First read the actual original source and use its project-relative path and exact, uniquely matching UTF-8 text. Current direct links support .tex, .txt and existing .md sources; do not invent PDF/Word paragraph anchors or generate a second index merely for navigation. A quote containing newlines uses JSON escapes in the single comment line. The plugin recognizes this marker for question-number hover and exact source navigation. When proposing/reworking a related candidate, pass the same verified objects in optional `questions`; the tool stores these inside the existing sole review state so the card can show all relevant questions. Preserve existing associations on rework unless their source actually changes. Several questions can share one content-based candidate. These are source locators, not a duplicate issue/status table or evidence that the issue is solved. No generated question-map files or Markdown trackers; do not add markers during global tool maintenance or rewrite unrelated old replies.
5. Treat a response depending on pending text as a draft. Report its pending IDs; do not represent it as submission-ready or as an accepted modification. On acceptance, rejection or rework, reconcile the canonical state, local dependencies and proposed reply; a substantive edit to an already accepted reply receives a new letter ID and remains pending until accepted. A shared fix must not cause reviewers' responses to contradict one another or consist only of `see the other response` without the necessary core answer.
6. Once the requested changes are accepted and an actual compiled PDF is available, verify page/line references if the journal requires them. Before then use stable sections and labels, not guessed pagination.
   At final revised-manuscript delivery, apply [unified red highlighting against the fixed original baseline](submission.md#final-revision-highlighting) and, if the top-comment agreement requests excerpts, insert them together from the final marked manuscript. Check each reply's description, excerpt and locator against that same version. Individual plugin acceptance and review-preview colors do not satisfy final manuscript highlighting.

Response letters preserve point-by-point reviewer order even though manuscript prose normally avoids list-like summaries. Follow the actual journal template, official names and reviewer numbering; preserve quoted text. Apply the main style rule's distinction between past-tense literature descriptions and present/current facts or completed-revision wording in author replies.

### Revision length tradeoff

The author's default is **非必要不增加篇幅，优先通过修改现有内容回答审稿人**. Adequate coverage means answering the actual concern with sufficient support, not expanding every possible interpretation.

- First replace unclear or overstated wording, merge overlapping explanations, or sharpen an existing definition, caption, table note or result interpretation. Several related comments can be addressed by the same revised passage; do not append one paragraph per comment or repeat the rationale across sections.
- Translate the concern into the actual missing definition, mechanism, derivation or evidence before drafting. Improve that substantive content rather than echoing the criticism with a negation or inserting defensive disclaimers into the manuscript. If the answer needs unavailable evidence, retain that gap in the existing state instead of manufacturing reassurance.
- Add prose only for a concrete gap that cannot be resolved within the existing content, such as a missing reproducibility detail, necessary qualification or newly required evidence. Put the shortest sufficient addition at its natural location. If the revision needs net growth, briefly identify what information requires it; routine authorized choices need no extra approval. Never replace an experimental evidence gap with a longer argument or claim an unperformed comparison.
- Keep essential method details, evidence and limitations in the manuscript. The reply can explain the handling decision and point to existing or revised support, but must not become the only home for information readers need. Do not repeat the manuscript and then paraphrase the same excerpt in the reply, or expand a complete answer to reach a suggested word range.
- Review the affected passage with its neighbors for repeated information and unnecessary additions. Compare local length when a substantial expansion is proposed or a real limit matters; do not create a word-count report for every edit. Remove only redundant material within scope, preserving distinct reviewer requests, scientific qualifications and necessary new results. No mandatory equal-length replacement or arbitrary word cap.

### Implementation wording and clarification

- Do not write empty framing such as In the available implementation, In our implementation or 在我的实现里. State the operation, setting or specific limitation directly, using the manuscript's existing vocabulary. Meaningful implementation details, such as the software framework or parameter update, remain appropriate; the word implementation itself is not banned.
- Distinguish missing knowledge from an actual method limitation. Inspect the relevant existing material first; if a necessary detail is still unclear, ask the author exactly what needs clarification and continue work that does not depend on it. Do not present a restricted or incomplete answer as finished merely to appear cautious, or turn the assistant's inspection/access limits into claims about the method, code completeness or supported scope.
- Clarification does not authorize guessing or fabricating evidence. Once the detail is established, use it to give the necessary complete answer concisely. State genuine conditions or limitations specifically, and preserve experimental evidence requirements. Do not use longer caveats to hide an unresolved question.

### Terminology continuity

The author's default is **不为回答审稿人自行造词，尽可能复用原文已有词汇和描述方式**. A clearer explanation should refine the existing description rather than introduce another name for the same thing.

- Before revising, check how the relevant object or operation is defined and described in the actual manuscript and its existing terminology profile. Reuse that wording in the revised passage and corresponding replies. Prefer a precise existing phrase over stylistic synonym rotation, a new shorthand or an invented technical label.
- Apply the kernel's scientific-continuity rule to the meaning of ordinary descriptions as well as technical names. For the same concept, keep its established name; for a similar concept, reuse the existing descriptive vocabulary and state the actual difference with ordinary words. Do not collapse distinct concepts, change an object's role or imply a new module or mechanism merely to keep the vocabulary uniform.
- When the original wording is ambiguous or inaccurate, clarify or correct it with established vocabulary. If a necessary distinction has no adequate existing expression, use a standard term or a short plain description and explain the distinction at its natural location. Do not fabricate a named concept, acronym or novelty claim, or perform an unsolicited global renaming. Preserve reviewer quotations verbatim even when they use different terminology.
- Check changed manuscript passages and related replies for competing names or descriptions of the same object. Reconcile only the affected uses, retain approved names and definitions, and reuse the existing profile if a genuine terminology decision needs recording; do not create a separate glossary or terminology report by default.

The manuscript's preference for a clear process, module or model as subject is not a first-person ban and does not require impersonal reply prose: We thank and We have revised remain appropriate. Follow the factual response voice below, without attitude or self-blame statements. Manuscript excerpts retain the actual manuscript wording; reviewer quotations remain verbatim.

### Reply tense by sentence function

| Sentence purpose | Default tense | Typical expression |
|---|---|---|
| Neutral thanks or current factual explanation | Simple present | We thank / The method uses |
| This round's completed addition, revision or clarification | Present perfect | We have revised / We have added |
| A completed revision with the changed object as subject | Present perfect passive | Fig. 1 has been updated |
| Current method, fact, limitation or contents of the revised manuscript | Simple present | The dataset consists of / we provide / the explanation is included |
| An actual future plan | plan to, aim to or will | We plan to / future work will focus on |

Choose tense by the sentence's purpose, not a single past-tense rule for the whole letter. Completed-revision wording must correspond to a real change; it is not evidence that a change happened. A reply relying on unaccepted candidates remains a draft and must retain that review status. Do not copy reference-specific results, facts, promises or grammatical mistakes.

## Response structure, sentence logic and courtesy

### Letter organization

Default to **简短总致谢 → 必要的本轮重要改动概述 → 编辑意见及逐条回复 → 各审稿人原始意见及逐条回复**, subject to the actual decision letter and venue template. The opening usually needs **50-100 English words**, less when sufficient, optionally naming two or three consequential actual changes. Do not appraise the reviewer's judgment, describe unfinished work as completed or restate the abstract. Keep a reviewer's original comment and its response together and preserve the original order/numbering. Shared concerns can use one coherent manuscript fix and cross-references for detailed evidence, but every affected response retains its core answer. Do not import conference-style regrouping or decision-score strategy into a journal revision by default.

### Factual response voice

After brief neutral thanks, state the method, evidence, explanation and actual revision directly. Do not express agreement or disagreement with the reviewer, evaluate whether the reviewer is right, or use admissions, apologies or self-blame. Avoid formulations such as `We agree/disagree`, `We admit`, `We acknowledge our mistake`, `We mistakenly...`, `We were wrong` and `We apologize`. This is a writing preference, not permission to conceal an actual error, adverse evidence or an unresolved issue. Describe a real correction objectively, for example `The denominator has been corrected from <old> to <new> in Eq. <label>.`, rather than narrating fault or attitude. Explain a justified non-change through its factual basis, not a declaration of disagreement. Verbatim reviewer comments and exact quotations retain their original wording.

### Mandatory response structure

Do not use internal editing expressions such as `The proposed sentence` or `the proposed paragraph` in reviewer-facing replies. Describe the substantive clarification or correction and its actual manuscript location directly. Keep pending author decisions and drafting status in the canonical review state, not reviewer-facing prose. This does not prohibit the scientific term `proposed method` or authorize a false claim of completed work.

Every response entry must follow **首句中性致谢 → 直接事实答复或实际处理 → 针对问题的解释与最小充分依据 → 真实修改或有依据不改的说明及定位**. The first sentence briefly thanks the reviewer without praise, agreement or self-blame. For one substantive question, subsequent functions may share sentences without forced headings or padding. For multiple substantive subquestions within one comment, use the numbered format below. A justified non-change explains its basis and points to relevant existing text rather than inventing a revision. Revised-text inclusion follows the pre-writing top-comment agreement. If requested, exact excerpts are inserted at final assembly, not during each question's drafting.

| 位置/功能 | 中文内容逻辑 |
|---|---|
| 首句 | 简短、中性地感谢审稿人，不加赞许、同意、自责或道歉 |
| 随后的实质答复 | 回答实际问题，或明确采用、部分采用、澄清、合理不改的处理决定 |
| 解释依据 | 给与该问题直接相关的条件、机制、比较维度、推导或事实，说明为什么这样处理 |
| 必要证据 | 提供足以判断的实际对照/结果及条件，解释它支持什么、支持到哪里；设计假设不写成已验证机制 |
| 修改说明 | 说明本轮具体新增、纠正、补充或收窄什么，区分原稿已有内容与本轮改动 |
| 定位与摘录 | 给真实章节、标签、图表或公式位置。是否附修后原文遵循顶部约定，需要时在最终统一标红阶段集中插入，不以“详见修订稿”代替实质答复 |

Match the answer to the question: a why-question needs a reason, a whether-question needs an answer and conditions, and an evidence-question needs the relevant evidence. For a questioned contribution or design choice, address the numerical premise where relevant, then center the answer on that design's actual distinction, task-relevant effect and supporting comparison. Apply the experimental-writing module's sentence-to-sentence progression criteria as well as its minimum of one directly corresponding numerical result for each independent empirical phenomenon or comparison, including each separately stated direction or condition. A result at the end of the reply does not support unrelated claims earlier in it. For module necessity, use matched removal or replacement evidence within its actual training context, distinguishing a basic increment from a contribution in the complete framework. Keep the scientific interpretation rather than copying every table row, imposing a numerical cap or substituting a procedure recap for evidence. Address the substantive issue and reported evidence directly, without shifting the answer to another component's larger contribution; equally, do not evade a small gain with a mechanism description or claim universal indispensability from an ablation alone. Keep necessary qualifications proportionate so that they do not replace the substantive answer. Do not force yes/no answers onto open questions. Explain why a change addresses the concern; a statement that text was added is insufficient for a substantive scientific question. Keep explanation and quotation complementary: the reply explains the basis, the excerpt shows the actual wording. Follow the agreed excerpt scope at final assembly, using only the relevant final passage rather than an automatic word/sentence quota. If excerpts are declined, explain the change and give its location without copying text. For a simple correction, one precise change/location sentence may suffice. Page/line checks and pending-edit handling follow the existing workflow above.

### Multiple subquestions and revised-text format

When one reviewer comment contains multiple substantive questions, retain the complete original comment verbatim and answer its subquestions in their original order using `1.`, `2.` and so on. Put a short, faithful subquestion heading on its own line, then the corresponding answer on the next line. Each answer contains its direct explanation, necessary basis and actual change location. Do not invent extra requests, collapse distinct questions into an undifferentiated paragraph, or repeat the opening thanks for every subquestion. Use the current LaTeX template to render the headings and line breaks; keep ordinary author-review units within their existing paragraph/environment boundaries.

When the agreed revised-manuscript excerpts are actually inserted, follow the complete numbered answer with the exact sentence `The revised content is provided below:` and quote the corresponding final revised text with LaTeX opening double backticks and closing double apostrophes. Where several distinct passages are needed, identify their manuscript locations and quote them separately rather than duplicating one passage under several answers. Do not append this lead-in before the excerpt exists, insert empty quotation marks, invent a manuscript change for a response-only clarification, or pass an unaccepted candidate off as final text. The existing author-decision and final-assembly timing remains unchanged.

Structural example only, not text to paste with placeholders:

```text
We thank the reviewer for the comment.

1. <Faithful heading for subquestion 1>
<Direct answer, necessary basis and actual change location.>

2. <Faithful heading for subquestion 2>
<Direct answer, necessary basis and actual change location.>

The revised content is provided below:
``<Exact final revised manuscript passage>''
```

### Concern-specific response paths

| 意见类型 | 中文展开逻辑 |
|---|---|
| 笔误、定义、格式 | 具体纠正结果 → 位置；通常无需单独论证 |
| 不清或误解 | 实际做法及条件 → 易混淆点的解释 → 手稿对应澄清 |
| 设计必要性 | 真实任务需求 → 具体选择及作用机制 → 相应依据/证据 → 修改位置；需要比较时再核对替代方案的实际差异 |
| 创新性 | 最近邻工作的共同基础 → 同一维度的实质差异 → 差异的作用与支持；不靠模块名称或新组合宣称创新 |
| 补实验/公平比较 | 实际完成的对照及条件 → 关键观察 → 有边界的结论 → 新增内容与定位 |
| 事实澄清或有依据不改 | 问题所涉事实与科学依据 → 实际调整、替代处理或不改的依据，不发表同意或不同意的态度 |
| 多个子问题 | 按原问题顺序编号，问题标题单独一行、下一行回答；回答后按约定附真实修后原文，不以一项易处理修改代表全部完成 |

For method comparisons, match actual formulations before asserting incapability; for example, a need for joint structural information alone does not prove all graph methods cannot model it. For evidence requests, include relevant matching conditions and uncertainty, and do not use an overall score gain alone to establish a particular mechanism. Preserve negative/mixed findings and narrow claims where required. Use the factual clarification and experiment-authorization rules below rather than treating every criticism as misunderstanding or responding with unapproved future work.

Illustrative Chinese skeletons, not reports of completed work:

- **必要性：**“感谢审稿人关注这一设计。［真实任务条件］要求［所需性质］。［具体操作］通过［实际计算关系］提供［作用］，其依据为［数学性质、已核实文献或真实实验］。修订稿在［位置］补充［对应解释或证据］。” Add an alternative-method comparison only when warranted and supported. Missing evidence stays a gap, not a fabricated finding.
- **公平比较：**“感谢审稿人指出比较设置的问题。原有比较无法分离［因素 A］与［因素 B］的贡献。在［真实共同设置］下，［已完成对照及核验结果］支持［有边界的判断］。修订稿在［位置］加入［实际结果与设置］。” Use completion wording only after the stated work exists.
- **收窄范围：**“感谢审稿人关注泛化范围。现有实验支持［已测试条件］，尚不能推断［更广条件］。我们将［实际原表述］收窄为［与证据一致的表述］，并在［位置］明确尚未覆盖的条件。” A real known failure and an untested condition remain distinct.

### Gratitude and professional tone

Use **整体简洁致谢，每条首句中性感谢**. The letter opening can thank the editor and reviewers for their time, and a separate reviewer introduction remains optional. Every individual response begins with a concise neutral sentence of thanks before its substantive answer. Do not omit it because the issue is simple or the overall opening already thanks the reviewers. For a multi-question comment, thank once before the numbered answers. Follow the factual response voice rather than praise or mechanical synonym rotation.

| 情境 | 可调整的表达示例 |
|---|---|
| 全信开头 | We thank the editor and reviewers for their time and comments. |
| 每位审稿人开头 | We thank the reviewer for reviewing the manuscript. |
| 公式或定义 | We thank the reviewer for the comment on this definition. |
| 补充说明 | We thank the reviewer for requesting this clarification. |
| 比较建议 | We thank the reviewer for suggesting this comparison. |
| 范围关切 | We thank the reviewer for the question about the scope of this claim. |
| 事实澄清 | We thank the reviewer for the comment. Then state the relevant facts and evidence. |
| 总体评价 | We thank the reviewer for reading the manuscript. |

Select or adapt the exact wording to the actual concern, keeping the opening thanks neutral. Do not add evaluative praise such as `helpful`, `insightful` or `constructive`, declarations of agreement, self-blame or apologies. Describe the actual method, factual correction or supported scope directly. Do not imply an unperformed experiment or close every item with requests for satisfaction or claims that all doubts have been eliminated. Politeness is not evidence and does not guarantee acceptance.

### Flexible length guidance

These are **personal suggested English-word budgets**, not measured reference lengths, journal hard limits or quotas. Count the author's reply prose, including any courtesy, but exclude the quoted reviewer comment and manuscript excerpts. Verified venue requirements and the actual concern's completeness take priority. Chinese drafting uses its real content needs, not the same numbers relabeled as character limits.

| 回复类型 | 通常建议英文词数 |
|---|---|
| 简单纠错/格式 | 15-40 |
| 定义、条件、实现澄清 | 60-120 |
| 方法依据、必要性、创新性 | 100-180 |
| 新实验、统计、公平比较 | 120-220 |
| 有依据的事实澄清或不改 | 100-180 |

Use the numbered subquestion format for multi-question replies rather than treating the upper ranges as universal caps. Do not pad a complete short answer, repeatedly summarize the comment, reproduce the Method or report every table value. Retain the evidence and qualifications needed to judge the answer.

### Local reply plans and efficient consistency checks

Use the embedded local reply field catalog before the response entry's first paragraph, selecting the actual subquestions, answer, basis/evidence gap, real change/non-change, manuscript locator/excerpt and pending status. A multi-paragraph reply may share this plan; add local paragraph details only when useful. The adjacent CODEX-RESPONSE marker lists manuscript numeric-ID dependencies. The main comment-ownership scheme governs placement, in-place recovery and scope.

Split subquestions before drafting, share real fixes without losing each reviewer's answer, and keep explanation and excerpt complementary. Manuscript revision IDs follow original content units, not questions: when several concerns affect the same sentence/display, formulate one coherent manuscript candidate and have the relevant replies depend on that same ID. Each reply explains the aspect relevant to its own comment; do not create competing manuscript edits merely to obtain one ID per question. Apply the version/freshness and issue-closure protocol in review-round.md whenever support changes. A draft that describes a pending candidate must be reconciled with the author's eventual accepted reading before external use.

## Misunderstanding, disagreement and conflicting requests

For a consequential concern needing public response examples, use [review-precedents.md](review-precedents.md) selectively. The accepted ReviewSearch client retrieves anonymized concern queries only; conference precedents guide argument/evidence relationships, not journal format, project facts or predicted editorial outcomes. No RebuttalDraft, automatic experiments or new Markdown response files are implied.

- Diagnose the actual question behind a comment, such as correctness, novelty, comparison fairness, generalization, efficiency or clarity. If multiple readings are plausible, briefly show the likely reading, an alternative, supporting context and uncertainty before recommending costly work. Record a compact unresolved interpretation in the existing state block; do not claim to know the reviewer's private intent or infer editorial outcomes from tone or scores.
- When a reviewer misunderstands an existing point, inspect why the text is easy to misread. Where warranted and authorized, clarify the manuscript's definition, explanation or emphasis as well as the response; do not resolve the issue solely in a private explanation that future readers will never see.
- For a justified non-change, explain the actual scope, applicable assumptions and verifiable evidence, and offer an appropriate alternative when available. `Out of scope` or `cannot do it` alone is inadequate. Do not imply an unperformed experiment or promise unapproved work. If additional experiments are needed, record the gap and use the experiment workflow only under its separate authorization.
- When requests conflict, inspect the editor's decision and applicable journal instructions, identify the precise incompatible demands, and propose one consistent resolution and its rationale. Obtain the author's decision where needed. If a consequential conflict or unclear request remains, prepare a concise clarification for the author to send to the editor; do not contact anyone automatically or separately promise both incompatible changes.

Before requesting new experiments, identify the precise unresolved question, why existing evidence cannot answer it and which result patterns would support, narrow or contradict the claim. Prioritize necessary, interpretable work within actual time/resources, including a useful interpretation if the result is negative. Do not duplicate evidence or propose experiments merely to signal effort. Planning/running experiments uses the corresponding skills and existing API/authorization rules; a writing request alone does not authorize execution.

Before delivering a response draft or claiming an issue resolved, inspect each completion/claim statement such as `we added`, `we revised`, `we evaluated`, `we demonstrated` or `we clarified`. Link it to the actual source change, analysis/result or justified response-only clarification, verify that the evidence supports its strength, and distinguish a reviewer request, an author-approved plan, a proposed edit and completed work. An unfulfilled promise stays visible in the state block and must be corrected or qualified in the response, never treated as fulfilled because a sentence says so.

Follow [review-round.md](review-round.md) for actual tracked source changes, versions, counters and acceptance decisions. Use only the current concern's response/thanks sections when the task is narrowly scoped.

## Source provenance

Read [source-notes.md](source-notes.md#response-writing-provenance) only when tracing guidance or verifying venue requirements.
