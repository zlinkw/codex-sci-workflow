# Method writing

Entry guard: apply the active [SKILL.md](../SKILL.md) kernel and its real top/local-comment gate first. If the kernel is absent, read it once; this backlink does not rerun routing. Other links activate only for an actual task condition, never recursive preload.

## Method structure rules

- Organize the Method around three core modules by default. Allow a different number only when the real method structure requires it; never invent, merge, or split mechanisms merely to reach three modules.
- Give each module three to four core display equations by default. Preserve technical accuracy when the genuine formulation requires an exception.
- Count key transformations, modeling relations, and module objectives as core equations. Do not count pure notation definitions, dimension declarations, or repeated expansions.
- Count one outer `equation` environment as one equation. An `aligned` block nested inside it still counts as one equation regardless of its number of lines.
- State each module's input, processing, and output. Verify that adjacent modules use compatible symbols, meanings, indices, and dimensions.

### Design rationale and content-driven organization

Explain a consequential design choice through the real task condition or relevant limitation, the selected operation and its concrete effect. Use **真实问题及后果 → 针对性设计 → 对应操作及公式 → 实际作用与验证** as an argument check, not a sentence template. Preserve a meaningful problem-to-solution connection, including a justified To address construction, instead of replacing the motivation with a component list. Where the passage explains the design's benefit, identify which dependence, ambiguity or unconstrained variation the operation changes and what that enables for the task. Merely saying that objects are connected, integrated or used downstream leaves this inference unstated. Explain the actual objective or constraint without inventing a stronger mechanism, and distinguish its intended effect from an experimentally demonstrated benefit. Go beyond dataflow where the choice needs explanation, without requiring every operation to prove a simpler alternative inadequate. Compare alternatives when the actual question or evidence warrants comparison, using their real formulations and supported differences. Do not invent an alternative's failure or claim that the chosen architecture is the only valid solution.

Organize the actual content using the following flexible Chinese blueprint. Functions may share a paragraph; do not force a fixed paragraph count, a separate motivation paragraph, or a summary after every module.

| 位置 | 内容与段内逻辑 | 向后承接 |
|---|---|---|
| 任务定义 | 必要的数据、监督条件与目标，以及真正影响设计的限制 | 明确后续可使用的信息与约束 |
| 方法总览 | 总体处理思路 → 关键设计的作用分工 → 共同形成的训练或推理过程 | 交代整体关系，具体选择理由在对应操作处解释；不复述整段引言 |
| 模块首段 | 当前对象的具体性质或缺陷 → 对应操作 → 必要公式 | 同时交代做什么和为什么这样处理 |
| 模块后续段 | 展开关键计算，在实质选择处解释参数、权重、粒度、约束或聚合方式 | 接续真实结果、作用范围或剩余限制，不重复宣称提高性能 |
| 优化与推理 | 模块结果如何进入目标函数、参数如何更新、测试时保留哪些部分 | 将机制落实为可执行过程，闭合监督与推理路径 |

Connect modules and overview details according to their real relationship:

- **Dependency:** continue with the object actually produced upstream and the computation applied to it. Check any intermediate prediction or transformation; never invent a direct tensor handoff.
- **Complementarity:** identify the distinct property not constrained by the preceding operation and explain the additional constraint. Do not imply the earlier module created a problem that already existed.
- **Parallelism:** organize different constraints around their shared target without inventing a sequential pipeline.
- **Joint coupling:** explain the actual shared parameters, joint objective or gradient path through which components interact; generic claims of synergy are insufficient.

Apply the existing implicit-flow rules: put the explicit relation in the local Chinese paragraph-plan comment, while prose carries it through substantive content and only necessary short cues. Preserve the valid upstream output, the reason it is needed downstream and the next operation's role when revising a transition. Tighten redundant lead-ins without deleting the information that carries the module dependency or turning the transition into a bare list of operations. Do not invent a remaining problem at every boundary or force every paragraph to criticize an alternative. Routine standard operations need no separate defense.

At consequential design choices, check five things within the requested scope:

1. Which actual task condition or modeling requirement makes this choice relevant?
2. Which exact equation term, operation or training step provides the required effect, and how?
3. Why does the selected statistic, weighting, representation granularity or aggregation suit that requirement? Explain meaningful choices, not every implementation detail.
4. Is the rationale a mathematical property, cited finding, observation, design hypothesis or experimentally supported conclusion? Preserve those distinctions. Mark missing project evidence as `needs experiment` or `unsupported`; do not present an anticipated failure as an observed result.
5. Does the argument establish the need for a capability or genuinely distinguish the chosen implementation from alternatives? A task requirement alone does not establish that an alternative is incapable of meeting it. Compare the actual formulations, conditions and evidence before making a stronger claim.

**Length guidance, not reference measurements or venue limits:** task definition plus overview usually needs about **100–160 English words**, less for a simple setting. Integrate a consequential local rationale into **1–2 technically informative sentences** when sufficient. A paragraph often needs **3–5 sentences** around one substantive issue; these are optional ranges, not quotas. Determine total Method length from the real mechanisms and reproducibility needs; **do not impose a 1300–1800-word default** or pad to any target. Preserve the existing module/equation defaults above without inventing mechanisms or formulas to meet them. Verified venue requirements and the author's confirmed project blueprint take priority.

For this author's concise method explanations, retain relevant hyperparameters already covered by the paper's ablation or sensitivity analysis and their established settings. Do not remove these settings merely to shorten a clarification, or add unstudied auxiliary schedule constants and implementation parameters to that explanation. Keep necessary reproducibility configuration in its appropriate location. Verify the existing setting and analysis before describing it, and do not turn a reported setting into a newly verified experimental or optimality claim.

Source provenance for this section is consolidated in [reference-templates.md](source-notes.md#source-notes-and-verification-status). These examples do not override the confirmed project logic or actual venue requirements.

Read [mathematical-notation.md](mathematical-notation.md) when editing equations, symbols or interfaces; a purely verbal module overview need not load notation mechanics.
