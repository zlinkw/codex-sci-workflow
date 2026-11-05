# Project comment templates

Entry guard: apply the active [SKILL.md](../SKILL.md) kernel and its real top/local-comment gate first. If the kernel is absent, read it once; this backlink does not rerun routing. Other links activate only for an actual task condition, never recursive preload.

## Embedded TeX setup

The following blocks are the canonical setup content, embedded directly in this skill-internal module. No standalone TeX template needs to be imported, copied into the skill folder, or bundled separately when sharing the skill. Read the actual main/header and target-local comments before selecting any template. Initialize only the block needed by an authorized writing edit; preserve existing author rules, packages, and compatible macros. Never initialize during read-only review or before confirming a new-paper logic plan.

### Main manuscript header comments

Place an appropriate project-specific version of this comment block at the real main manuscript's top when absent. Child sections inherit it; a separately compiled response letter can point to the verified main manuscript in a short comment rather than duplicate every rule.

```latex
% CODEX-RULES-BEGIN
% 本块由作者维护，适用于主稿、输入的各节、附录和关联回复信。
% 每轮开始先读本块、顶端写作蓝图/审稿状态及待改段落前的局部蓝图，确认真实文件、逻辑、篇幅和未决事项。
% 内容优先级：遵守全局指令及科学/证据边界；实际期刊要求与作者决定有实质冲突时具体说明。作者当前决定更新旧项目偏好，项目确认方案优先于通用默认。
% 写作方式：需要且获准修改正文时先改手稿，再依据实际版本写回复；非必要不增加篇幅，优先改写、合并或替换现有内容，确有必要的信息缺口才最小增补；纯回复澄清或有依据不改时不硬改正文。只改指定部分及必要关联位置。
% 一致性：沿用顶部全文论证与关键术语约定；相同或相似方法、操作与对象尽可能复用原文词汇和描述方式，保留真实区别，不为回应审稿人自行造词、另起名称或缩写；科学条件、定义、结果或主张变化时检查受影响的章节/图表及回复，纯措辞修改不强制全篇审计。
% 未经批准不得全篇改符号、换概念、扩大结论、补造实验或宣称未完成的修改。
% 实现与询问：直接描述具体方法、设置和操作，不写 In the available implementation、In our implementation 等空泛限定；核对相关材料后仍不清楚的必要细节向作者提问，不猜测，也不因自身信息不足就缩减必要回答或虚构方法局限；真实科学限制与实验取证要求保留。
% 修订方式：新改动以独立候选和固定基线进行编号审核，作者明确接收前不替换正式正文；正文用 1、2、3，回复信用 a、b、c（z 后为 aa）。仅作者要求或期刊明确要求时启用彩色修订；现有未决宏不得自动移除或当作接收。
% 编号规则：各自连续编号，不按轮重置，不复用已发编号；返修保留编号。数字指正文，字母指回复信。
% 接收与返修：按编号逐条接收、拒绝或返修；保存、编译、暂存、提交、格式化、推送均不等于接收。仅恢复指定且核实匹配的修改，保护手改、其他未决项及原有暂存；冲突先保留并核对。
% 回复摘录约定：开始撰写回复信前先与作者确认是否附修后原文，并将“是、否或待确认”记录在回复信顶部现有规则或画像注释内。已有确认不重复询问。若为是，逐条先完成实质答复，原文摘录等全部相关修改和审核完成后，与最终统一标红一起集中插入并核对文字、符号、颜色和定位。若为否，不插摘录，仍保留完整解释与真实定位。
% 回复信：保留审稿意见原文，每条首句必须简短感谢，然后直接答复、给出必要依据并说明真实修改或有依据不改及定位。先核对实际修改后的内容再写回复，不凭计划或假设描述。原则上每次统筹解决一个完整审稿问题的全部子项、必要手稿修改和相关意见一致性，并完成对应回复，不以单处修改代替整条完成。位置审核编号保持独立，待审候选与已接收修改分开说明。
% 审稿状态：先解析并保留唯一状态块的实际归属及指针；新增回复信不另建状态或重置编号。版本基线、计数、意见及依赖只在该块维护；AI 交接与运行记录也放入该完整注释块，不写进正文、回复或作者审核候选。作者接收、问题解决与证据状态分开，依赖变化标为待重新核对。
% 轮次审核：在状态注释保留本轮确切编号；每轮用编号、位置、修改目的和待作者判断事项给出简短导航。
% 界面审核：在真实原文件展开候选卡片；每处一键接收并替换该处原文，不手动复制。未接收的原文保持不变，不满意保留原编号批注返修。精确原文选区批注关联不可变版本，保存在唯一状态块。
% 批注处理：每轮写论文、改稿、写回复信及上下文恢复时，自动读取唯一状态块、作者决定、相关开放批注及待重新核对的依赖；同轮未变化时复用，不因进入其他模块重复读取。核对所选原文/候选的真实版本及局部计划，无需专用口令或重输编号；范围外事项保持待处理。
% 批注返修：保存批注不等于已改写，也不自动启动 AI；下次普通写作请求会按范围处理。实际返修保留编号和原文，仅标明已实际回应的请求，新候选仍待审，不自动接收。
% 定位：未核实最终编译 PDF 时只用章节、标签和文件位置，不编造页码或行号。
% 操作：真实本地文件为准，仅本地编辑、编译与预览。Ctrl+S 保存编译，Ctrl+Alt+J/右键跳到 PDF，PDF 双击回源码；不锁定 main.tex。
% 环境与版本：简记已核实引擎/TeX Live 年份和构建目录；Git 仅作可选备份，不阻断写作审核。配置备份时记录获准私有仓库和真实同步状态，不填凭据或提交流水。
% 文件：不添加 Markdown 管理文件、整篇可编辑副本或重复状态表；活跃审核对象在 .codex-review/objects，与 Git 无关。普通推送只含成功成果，不含私有审核历史和批注；需要时才单独归档当前活跃审核状态，恢复到独立目录，不默认永久保留已完结候选。
% 源码：新写或实质改写的普通正文一句一行，段内不空行，段间留空行；正确处理缩写、小数、引用与数学，不批量重排现稿。手动格式化只整理缩进，不依赖 Git；作者明确本批审完后，自动按真实目的提交已接收成果并推送已核实私有 GitHub；成功后精简已完结状态，并自动删除已核实无引用的审核对象缓存，不归档、不逐批再问；未接收候选、批注、必要基线与依赖保留。
% 修订稿标红：保留并核实本轮修订所用固定原稿基准；全部相关修改及作者审核完成后，最终交付前统一对比，新增与替换的内容在交付 LaTeX 和正常编译 PDF 中标红，并核对回复信说明和定位；未改内容保留原色。插件仅负责批注与接收，不逐次写颜色；审核预览的旧红新蓝不能代替最终标红。源稿基准不明时先询问，不猜测。
% 投稿：仅明确要求时执行预检和派生导出；未决修改/过期回复/证据缺口不自动清除，内部注释仅从导出副本去除，真实源码与审核状态保留，不自动上传。
% 审核分工：原文件卡片审措辞与论证；右侧单份完整论文审核 PDF 仅将修改句原句上、候选下排列，不改句只出现一次，仅变化词原文红色删除线、新文蓝色。正常 PDF 查实际排版；全部开放批注可一键加入 Codex 输入区，不自动发送。
% 语言：讨论默认中文，稿件与回复默认沿用已有语言和期刊模板；论文不鼓励不必要的第一人称，有明确且准确的过程、模块、模型等名词主语时优先复用；第一人称更清楚自然时可以保留，不机械改成被动句或将研究者行为误写成模型行为；回复信保留自然作者口吻，审稿原文引述不改。
% 标点：论文与回复信的自写叙述禁用英文分号和中文分号，改用独立句或合适连词并保持原意。审稿原文引述、文献原标题、代码及 LaTeX 语法、数学中具有必要含义的符号不做机械替换。
% 参考模板：作者提供的参考论文/回复信用于仿写结构、语气与格式；具体文件及用途在本块注明。
% 参考文献：按实际引擎与目标期刊处理；此处仅记期刊、文献库/样式、权威来源与核验日期及未确认项，具体引文支持关系记在引用段落前。
% 蓝图位置：全文论证、关键术语/符号、总篇幅及标题/摘要/风格放顶部唯一画像块；具体正文逻辑放相关段落前，回复按条放首段前，图表放外层源码前，只填必要字段、原位更新。
% 蓝图依据：先引导作者选最满意的文献或段落并读原文；区分参考实际篇幅、建议范围与期刊硬限制，不把示例句数或页数当通用规定。
% 仿写边界：章节、段落、句子的论证功能及实验组织可以借鉴；研究事实、数值和结论必须来自当前项目。
% 逻辑：同时检查句内、句间、段间、章节间的承接、前提、因果、对比、证据与结论边界，禁止刻板套写。
% 段间过渡：注释明确前提、关系与交接；正文优先以概念接力、内容对比和问题回应自然衔接，仅在必要处保留简短提示，不重复概括或套用过渡句。
% 引言起始段：一般是先有问题，再自然而然地导出背景；背景服务于凸显问题，不为介绍而介绍。每句作用与句序依参考及本研究定制。
% 逻辑确认：写全新论文或作者要求确认文章逻辑时，先读参考及现有内容，提出针对性问题并讨论组织方案；确认后再成文。
% 引言约定：通常分类讨论 2～3 类研究、提炼 2～3 个本文核心挑战；挑战须有对应方案、创新与验证，数量不强求与模块一一相等；贡献使用 \item[\textbullet]。
% 文献综述分工：有独立 Related Work 时，引言仅保留路线提示及必要挑战论证，详细机制与最近邻比较放 Related Work；无独立章节则沿用整合写法，不重复增设。
% 方法约定：任务条件/具体缺陷 → 所需性质 → 实际操作及公式；说明省略关键设计后会留下什么问题，区分假设与证据，不夸大为唯一方案。
% 公式段落：公式以句号结束时，在外层 \end{equation} 与后续正文之间留一个真正空行以开始新段；以逗号结束时不得留空行，后文接续同一句和同一段。
% 方法承接：按真实依赖、互补、并行或联合关系组织；逻辑记在局部注释，正文用技术内容自然衔接，不强造剩余问题或填充动机/小结。
% 实验约定：创新点对应预期、对照、实际证据与边界；图表须能追溯项目 runs/results.csv/claims 记录，缺口标 unsupported/needs experiment，不凭正文或回复相互证明。
% 讨论与结论：讨论解释贡献、意义与真实适用边界，不重复报数或推演无依据的严重缺陷；结论只收束已支持的研究答案，不扩大主张或掩盖影响主要结论的已知问题。
% 本块只存稳定约定；发现矛盾先指出，不擅自改写作者规则。
% CODEX-RULES-END
```

### Review-state header comments

For an authorized reviewer-response or tracked-revision task, first resolve and preserve the single existing owner. For first initialization only, prefer the existing response letter top, otherwise the manuscript top, before `\documentclass`. A later reply file does not create a second block or reset history; an authorized relocation follows review-round.md and preserves all records/pointers. Keep this block separate from stable `CODEX-RULES`; other roots use only a `% CODEX-REVIEW-STATE-FILE: <verified relative path>` pointer. Populate actual associations and issue records only, never invented comments, evidence, decisions or example statuses. See [review-round.md](review-round.md) for merging, reconciliation and update rules.

```latex
% CODEX-REVIEW-STATE-BEGIN
% 本块是审稿意见与修订进度的唯一状态表；每轮及上下文恢复后先读，并与真实源码核对。
% 交接摘要：仅按实际需要记录当前任务范围、已执行事项、下一步及阻塞，原位更新，不追加聊天流水或重复机械决定表。
% 记录边界：AI 交接和运行状态只放在本块内，每个物理行均为 LaTeX 注释；它们不生成修订编号、候选或作者批注，也不代表接收或科学问题解决。
% 文件关系：按已核实的相对路径填写主稿与回复信；其他根文件只保留指向本块的注释。
% 版本：审稿基线=真实投稿版本及已核实来源（未知/不适用如实标明）；轮前基线=固定本地不可变对象，不依赖 Git/HEAD；已接收投影与当前候选分别记录；作者额外手改不能默认为已接收。
% 当前轮：任务与范围按实际填写；正文编号=无；回复编号=无。分配编号后更新为本轮确切集合。
% CODEX-REVIEW-NEXT manuscript=1 response=a
% 上行为新项目初始化示例；已有计数沿用实际值。旧计数在稳定规则块时，仅在获准写作轮迁至本块，保留已发编号，不重置或建立第二份。
% 干净源码审核：source_review.py 在本块维护唯一 CODEX-REVIEW-DATA JSON 行，包含轮前/已接收对象、确切编号集合、逐项作者决定、候选代次与显式依赖；不要手填虚构对象或复制第二份状态。
% 原文/候选及上下文锚点保存在 .codex-review/objects 的不可变本地对象中；JSON 只存身份与状态，不将行号当唯一定位。机械决定以该 JSON 为准，下面的意见记录引用编号并补问题/证据/语义依赖，不重复维护决定表。
% 中断时保留本块 transaction 意图，先核对真实文件再显式 recover；匹配失败或手改重叠时停止覆盖，不能整文件恢复。彩色旧模式尚未迁移时按其原有记录保全。
% 字段：意见来源/子问题 | 正文数字编号及定位 | 回复字母编号及定位 | 作者决定引用上述 JSON 编号记录（未迁移旧模式仍原位维护） | 问题处理状态 | 证据状态及来源/缺口 | 依赖与核对状态；同一记录原位维护。
% 必要时另记：科学严重程度、编辑明确要求、工作成本与依赖；审稿要求不等于作者承诺，作者计划不等于已完成。
% 实际意见在下方逐项填写；未开始时留空，不将说明或示例当作已完成记录。
% 作者决定：待审/接收/拒绝/返修；问题状态：待处理/部分回应/已答复待核对/已解决/有依据不改；证据状态：已核验/待核验/待实验/不适用。
% 接收文字不等于问题解决；所有子问题有充分回应、依据有效且对应当前版本后，才能标已解决；仍依赖未接收的正文/回复时保留已答复待核对。
% 依赖变化：正文/结果/主张被改写、拒绝或撤回时，关联回复、摘录与定位标待重新核对；即使无开放批注，下轮也按实际版本重核。通过后仅更新本记录的核对结果/版本及必要 freshness 字段，不改变作者决定，不自动接收其他改动；范围不允许修复时保留缺口。
% 同一意见原位更新；保留未决依赖与作者决定，不追加聊天流水或在两文件复制状态表。
% 完整审稿原文保留在回复正文；本块仅存简短映射，页码行号只在最终 PDF 核实后填写。
% CODEX-REVIEW-STATE-END
```

#### Machine handoff and status records

This is the shared contract for AI-generated bookkeeping, not scientific prose or author instructions.

- Put task handoff, progress/resume position, next actions, blockers and runtime summaries inside the **existing single owner's** `% CODEX-REVIEW-STATE-BEGIN` / `% CODEX-REVIEW-STATE-END` block. Both markers must be complete standalone lines starting at column 1, with exact spelling. Every nonblank physical line inside is a LaTeX comment; prefix each line of a multiline note with `% `. Do not invent a HANDOFF block, append loose status notes beside the block, duplicate it in the manuscript/reply, or create a tracker file. Other roots retain only the verified owner pointer.
- Keep one short current summary and update it in place. Read actual source/state first; record only work performed, current scope, remaining work and real blockers. Reference the canonical DATA records rather than duplicating decisions, candidate history or counters in prose. Machine bookkeeping is not input to `propose`, `rework` or author feedback: allocate no review ID, require no acceptance and never include it in a manuscript/reply replacement span. A real scientific wording change must still use normal author review, not be hidden as bookkeeping.
- Preserve the existing schema, owner, batch identity, counters, decisions, candidates, notes and dependencies. Mechanical DATA/NEXT fields remain tool-owned: use the existing state writer, shared lock, fresh-version checks and atomic persistence; never hand-edit their JSON or synthesize history. Updating human-readable handoff comments must also serialize with that owner writer and preserve all unrelated bytes. If no safe update path is available, report the limitation in the chat handoff rather than bypassing locks or turning the note into a fake candidate. Missing state is initialized only during genuinely authorized writing setup, not merely to store this maintenance task's progress.
- Stable author requirements remain in CODEX-RULES, confirmed writing blueprints in their profile/local comments, and original reviewer questions plus verified question locators in their normal locations. Do not move these into the machine block just to suppress checking. In particular, a paragraph's logical transition/“交接” describes the paper argument, not an AI session handoff.
- TeXScholar excludes a complete comment-only canonical state block from source-review display anchors and ChkTeX diagnostics; malformed markers or real TeX inside must not suppress normal checking. Follow [review UI](review-ui.md) for presentation behavior. Do not disable project-wide ChkTeX, insert whole-file suppressions, or patch third-party plugins to conceal a misplaced record. This rule update alone does not authorize rewriting an existing paper or cleaning old records.

### Writing-profile comments

At the main manuscript's top, keep one canonical title/keyword/abstract/style block. Reuse the Title, acronym and keyword rules for the naming fields rather than duplicating their defaults here. Use actual source locators, units and measured/proposed ranges when known, otherwise label the field pending rather than inventing a count. Expand each abstract functional block into the actual planned sentences, especially the multi-sentence methods block; neither five nor nine sentences is required. If the abstract is in a child file, name it here and put only a pointer in that file.

```latex
% CODEX-WRITING-PROFILE-BEGIN
% 状态：按实际记录待讨论/已确认；来源及定位：填写已读参考的文件或链接、章节与段落。
% 全文论证：中心问题及任务条件 → 核心挑战 → 对应设计/真实创新 → 可检验预期及实际证据位置 → 结论与边界；只存本项目确认后的紧凑映射，具体研究事实与作者决定不作为其他项目的通用要求，局部推理留原位。
% 术语与符号：关键概念的中英文规范名/缩写 | 定义及作用域 | 首次定义位置 | 允许别称/易混淆概念；必要时记关键符号含义，不抄全部数值或常规索引。
% 总篇幅：目标期刊/文章类型 | 已核实页数/词数及计数范围、来源与日期 | 各节和图表/参考文献的总体分配 | 未知或超限项；结合全篇分配，不叠加各节上限。
% 风格画像：按已读样本概括句子节奏、承接、谨慎措辞、引用方式与章节语气；个人样本与外部参考分开注明。
% 标题定位：按实际记录中心问题、核心创新、对应支持及不能扩大的研究条件；沿用作者已确认定位。
% 标题与缩写：默认“常见英文单词式缩写：具体描述”；简记候选/作者决定、名称语义、自然展开及字母来源，保留必要任务/条件，不堆模块或为凑字母造机制。
% 标题篇幅与核验：记录可读英文词数及计数口径；个人建议与已核实期刊要求分开，简记重名检索范围、来源/日期、近似名称及未决项，不宣称绝对唯一。
% 关键词选择：记录实际候选/作者决定及任务、设定、机制等覆盖理由；去除同义或缩写/全称重复槽位，允许与标题重合，不把投稿分类数量套给正文。
% 摘要文件：填写真实相对路径；中心问题、贡献与证据边界沿用作者已确认方案。
% 摘要主线：任务必要性 → 与引言一致的关键挑战及后果 → 方法总体思路及关键机制 → 实验证据 → 代码（适用时）。
% 挑战：忠实压缩引言的挑战论证，数量按实际需要；不新增引言没有的挑战，不强求两类。
% 方法展开：总体思路 → 机制如何回应挑战 → 按真实依赖/并行/互补关系说明作用；不固定模块或句数，不强加转折句。
% 默认英文摘要篇幅：目标 180～210 词，上限 220 词；期刊有明确要求时优先遵循期刊要求，并记录来源与实际适用限制。
% 计数范围：摘要可读正文，含放在摘要内的代码声明；不计 TeX 注释和排版命令，期刊另有口径时从其规定。
% 篇幅依据：分别填写参考实测篇幅、目标建议范围、期刊已核实硬限制及来源；未知项明确待核实。
% 统计口径：英文用词数，中文用字数并说明是否含标点；总篇幅与逐句分配应协调。
% 摘要逐句蓝图：按实际句数逐行填写“第几句 | 论证功能 | 本研究中文句式/内容槽位 | 前后承接 | 目标词数/字数范围 | 对应证据或缺口”。
% 原则：参考顺序可按本研究逻辑调整；不机械套五句，不为满足篇幅虚构内容；修改蓝图不等于接收正文修订。
% CODEX-WRITING-PROFILE-END
```

The following is a **field catalog, not a block to paste in full**. For a real local plan select the location/status and task, then only the relevant argument/evidence/length fields. Place it immediately before the affected prose paragraph; a response entry can share one plan before its first paragraph; a figure/table plan goes before the outer LaTeX environment, not inside its caption. Keep section allocation only in its first relevant plan and sentence rows only when helpful. Local blueprint status records agreement on organization, not author acceptance of prose; author decisions and issue/dependency freshness remain in the canonical review state. Use existing labels/topics and LaTeX comments, update in place and preserve author edits; follow the always-on kernel's comment-ownership rules.

```latex
% CODEX-PARAGRAPH-PLAN-BEGIN
% 对应位置：填写真实章节/标签与段落主题；状态：按实际填写待讨论/已确认。
% 参考与风格：填写已读参考的准确段落位置及本段可借鉴的写法。
% 段落任务：写清本段回答什么，以及本段实际新增的信息。
% 段间承接：注明前段已确立什么、本段接续什么及真实关系；正文用具体内容体现，勿照抄成解释性过渡句。
% 段末交接：注明留给下一段的具体问题或结论；保留必要前提，避免重复小结与强造因果。
% 研究定位（仅综述段适用）：本段主题 | 分类/比较维度 | 共同点与关键差别 | 本文定位是否需在此出现 | 与引言的内容分工；代表文献及支持定位复用下方引文核验字段，不重复建表。
% 设计依据（仅方法段适用）：按需简记本研究的真实问题及条件、选择依据、对应操作/公式、实际作用及证据类型；需要比较时再记录替代方案的具体差异，不强求每段都有反例。
% 实验论证（仅实验/结果段适用）：本段检验的主张 | 关键对照 | 预期观察（区分事前预期/事后解释） | 实际证据及定位或缺口 | 可得结论与限制；按实际填，不将计划写成结果。
% 讨论解释（仅讨论段适用）：解释的发现 | 证据定位 | 观察/支持的解释/未验证推断 | 新增意义 | 适用边界；局限区分已观察问题与尚未覆盖条件，相邻段落关系沿用承接字段。
% 结论收束（仅结论段适用）：最终主张 | 已有支持及范围 | 不得扩大的条件/认识；与摘要一致但不复用其背景、模块清单和成组数字。
% 回复论证（仅作者回复适用）：完整原意见及全部子问题 | 首句简短感谢 | 直接答复或处理决定 | 解释及证据/缺口 | 经实际改后内容核对的真实改动或合理不改 | 手稿位置/必要摘录 | 未决状态。沿用相邻 CODEX-RESPONSE 的正文编号依赖，不另建映射表，不遗漏关联回复。
% 图表论证（仅图表适用，放对应图表源码前）：用途及问题 | 面板/行列对应 | 编码、单位及统计口径 | 关键观察、支持及边界 | 与正文分工；沿用已有标签、证据/引文核验及篇幅字段，未知信息保留缺口。
% 引文核验（按实际引用逐项简记）：支持的具体主张/文献键 | 引用用途 | 已读来源及章节/段落/图表定位 | 支持范围 | 身份/摘要或全文/支持关系的各自状态与缺口；不重复完整元数据，不将待核实文献写成正式引用。
% 篇幅：区分参考实测与目标建议；需要时仅在本节首个相关块记录全节预算及分配。
% 逐句蓝图：按实际句数逐行填写“第几句 | 功能 | 本研究中文句式/内容槽位 | 承接方式 | 建议词数/字数范围 | 证据或缺口”。
% 作者决定与边界：保留已确认逻辑、未决分支和不能扩大或虚构的内容；同一块原位更新。
% CODEX-PARAGRAPH-PLAN-END
```

These templates are text embedded in this skill package. Inline selected fields into the authorized .tex file; do not add external skill-file inputs or copy this Markdown into a paper project.
