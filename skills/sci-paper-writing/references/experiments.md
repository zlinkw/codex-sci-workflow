# Experimental section writing

Entry guard: apply the active [SKILL.md](../SKILL.md) kernel and its real top/local-comment gate first. If the kernel is absent, read it once; this backlink does not rerun routing. Other links activate only for an actual task condition, never recursive preload.

## Experimental section and result analysis rules

Organize around **创新点 → 可检验的预期 → 区分该作用的对照与观察 → 实际证据 → 结论及边界**. A section answers a substantive question rather than narrating the order in which runs were performed. Distinguish overall effectiveness, component contribution, mechanism evidence and conditions of failure. Apply the existing evidence and implicit-flow rules; this writing blueprint neither authorizes running experiments nor requires new experiments merely to fill its structure.

### Innovation-to-evidence correspondence

For each core innovation, identify the expected observable effect, the contrast that distinguishes it from a simpler plausible treatment, relevant intermediate/error evidence, and outcomes that would support, weaken or fail to establish the claim. When explaining a questioned design, keep its specific role at the center: what changes relative to the actual baseline or replacement, how that change addresses the task, and which discriminating evidence supports its value. Report the size of its incremental gain honestly, without ranking methodological contributions solely by gain magnitude or shifting the answer to another component's larger improvement. A procedure recap is not an explanation of value, and a plausible mechanism does not replace evidence of benefit. Necessary evidence boundaries should qualify the supported explanation rather than displace it with repeated concessions or disclaimers. One experiment may inform several innovations, and one innovation may need several pieces of evidence; do not match experiment counts mechanically to module counts. When analyzing completed work, distinguish prior expectations from retrospective interpretation rather than inventing a preregistered hypothesis.

Choose evidence at the granularity of the actual claim. The following are examples, not a mandatory experiment inventory:

| 声称的作用 | 有针对性的观察 | 单独不足以支持的结果 |
|---|---|---|
| 保留类别语义的对齐 | 类别混淆、跨域语义对应及类别条件下的变化 | 只有平均 Dice 或一张特征投影图 |
| 提高伪标签可靠性 | 相同筛选预算下的错误率，以及困难区域覆盖情况 | 仅筛得更少后准确率升高 |
| 改善全局结构合理性 | 与所声称结构性质一致的错误统计及定位案例 | 只有重叠分数改善或轮廓更平滑 |
| 多机制互补 | 有效组合对照、条件增益及不同错误的改善 | 只有逐步加模块的升分曲线 |
| 对先验误差稳健 | 扰动所依赖的信息，观察有效区间和退化位置 | 只有一个默认取值表现最好 |

### Flexible subsection, paragraph and sentence blueprint

Use these six functions as needed; merge or reorder them to fit the actual argument and venue. Mechanism evidence usually belongs next to its relevant ablation rather than in a repetitive standalone section. The ranges below are **suggested English-word budgets**, not measured reference lengths, hard limits or quotas. A confirmed project blueprint and verified venue requirements take priority. Do not impose a universal section total, pad short findings or fabricate missing results.

| 小节功能 | 段落与段内内容逻辑 | 建议篇幅 |
|---|---|---|
| 实验设置 | 数据与划分、比较协议、实现、评价与统计；按下述四个短段组织或合并 | 合计 250～400 词 |
| 与现有方法比较 | 通常 2～3 段：主要发现 → 代表性证据及例外；关键任务/结构/条件差异 → 对应结论；必要的错误定位可视化 → 与定量结果对应 | 合计 200～350 词 |
| 消融与设计验证 | 简明定义基线、变体及不变条件；每个核心问题按“改变什么 → 实际观察 → 任务表现 → 支持范围与未决解释”展开 | 每个核心问题 80～150 词 |
| 稳健性与敏感性 | 改变的依赖及范围 → 趋势或稳定区间 → 明显退化位置 → 使用边界 | 每个问题 60～100 词 |
| 计算代价 | 测量条件 → 主要新增成本 → 对应收益及部署影响 | 60～100 词 |
| 失败与适用边界 | 失败病例/条件 → 可定位错误 → 有证据的原因或明确标注的假设 → 需要收窄的结论；可合并至 Discussion | 80～140 词 |

For experimental settings, adapt these paragraph/sentence roles without turning them into stock sentences:

- **数据段：**任务与域差异 → 患者/扫描数量及划分 → 实际使用的标签、数据与监督权限。只保留影响实验解释的背景。
- **比较协议段：**方法选择依据 → 骨干、预训练、数据与后处理是否一致 → 复现值/引用值及不可比条件。不要将资源或协议差异归因于算法。
- **实现段：**复现所需训练设置 → 重复运行、停止及模型选择方式 → 超参数选择依据。常规信息可进表，勿复述 Method。
- **评价段：**主要指标及关注错误 → 汇总单位 → 不确定性与统计比较方式。指标应覆盖所声称的能力，而非只选有利指标。

For ablations, separate deletion (contribution within the current system), replacement (why this design rather than a simpler/existing choice), and mechanism observations (whether the claimed change accompanies the gain). Explain a module's tested necessity through the capability or performance lost when it is removed or replaced, the matched numerical contrast, and how its operation addresses the corresponding task requirement. Do not substitute an input/output recap for that argument. Distinguish its incremental effect on a basic configuration from its conditional contribution within the complete framework; one small baseline increment does not describe every supported role of the module. Use the appropriate existing controls, keep their training context explicit and preserve meaningful interfaces and dependencies. Not every detail needs all three types of evidence, and no exhaustive combination experiment is implied. Missing evidence remains a gap rather than an invented contrast. A removal result supports necessity within the tested framework and conditions, not universal indispensability. A synergy/complementarity claim needs informative combination contrasts rather than an additive sequence alone; do not demand combinations that are meaningless under the actual dependencies.

### Comparison, uncertainty and boundary checks

- State important matching conditions and deviations, including backbone/pretraining, data/labels, training budget, model selection and postprocessing. Control a plausible competing explanation when the claim depends on it; disclose unavoidable differences. Separate reproduced and literature-reported numbers.
- Distinguish variability across patients, seeds and folds; name the unit and aggregation. Do not treat slices from one patient as independent patients. Use justified statistical analysis for key comparisons, report effect magnitude and uncertainty, and reserve statistical-significance wording for actual statistical evidence. Aggregate literature scores alone cannot support an invented paired test. Non-significance is not equivalence.
- Check repeated-run/case summaries, important hyperparameter sensitivity, failure cases, limitations and efficiency as required by the applicable research rules. Report genuine missing experiments/analyses as gaps in the existing evidence or local paragraph comments, not as completed findings or new project Markdown trackers. Select parameters/checkpoints without test-label tuning.
- Robustness analysis should stress dependencies that matter to the method, such as prior error, pseudo-label noise or target sample size. Explain stable intervals and breakdowns instead of recounting every parameter setting. Distinguish training, adaptation and inference cost, including preprocessing when relevant; report hardware, input and timing scope. Training-only components do not automatically make adaptation inexpensive.

### Finding-led result prose and implicit transitions

Each paragraph develops one finding that answers its scientific question. Every independently stated experimental phenomenon or comparative judgment in result interpretation requires at least one directly corresponding numerical result in the same sentence or its immediately connected explanation. A paragraph containing several phenomena needs evidence for each, not one score at its beginning or end to stand for all. If directions or conditions show different effects, supply a result for each stated effect; an aggregate alone cannot substantiate separate directional claims. A baseline/result pair, an explicit increment, a rate or a relevant statistic can provide the numerical anchor. A table citation or words such as improves, worse or best alone do not meet this minimum. Definitions, descriptions of operations and clearly identified mechanism hypotheses are not additional empirical phenomena; several sentences explaining the same observation may share its clearly linked result. Do not invent a value when evidence is unavailable. Establish the scientific judgment and discriminating comparison before choosing numbers; table order must not dictate the sentence sequence. Use result values or their differences as appropriate, without repeating both for every configuration. Organize the selected results around their task significance, retaining unfavorable findings, mixed directions, uncertainty and exceptions. Leave irrelevant inventory and duplicate values in the table, but do not impose a paragraph-level numerical cap or remove evidence needed for the per-phenomenon minimum. Do not report run chronology or repeat generic claims of effectiveness. Overall scores do not by themselves verify an internal mechanism.

Individually sound result sentences do not by themselves form a coherent analysis. Develop the paragraph's central question through connected comparisons and interpretations: a later sentence should explain, contrast, distinguish, test or qualify the specific finding carried forward, rather than merely report the next configuration. When changing comparison objects or factors, make clear how that comparison follows from the preceding finding and what unresolved distinction it addresses. When introducing a design explanation, connect the established operation to that observation and separate its intended effect from the observed outcome. If adjacent sentences lack a substantive relationship, revise their order, allocation or explanation within scope; adding a connective or inserting a detached method recap does not repair the argument. Preserve the numerical support for each independent empirical judgment, but do not manufacture more judgments to attach numbers to. These are criteria for progression, not a mandatory sentence sequence or a requirement for an extra bridge sentence, and they do not license a causal link or mechanism absent from the evidence.

Anchor visual analysis to an observable error and location, its change across methods and its relation to quantitative results. Explain case selection and include failures; do not infer dataset-wide reliability from selected good examples. A heatmap, projection or training curve alone does not establish a causal mechanism, calibrated confidence or global distribution alignment. Keep observations, interpretations and causal conclusions distinct; narrower findings can require narrower novelty claims. Preserve contrary trends, non-winning structures and uncertainty instead of automatically blaming randomness.

At paragraph boundaries, let the comparison and carried object provide the transition: overall effects motivate a distinguishing ablation, the ablation connects to its mechanism evidence, robustness examines a real dependency, cost establishes the tradeoff, and failures restrict scope. These are possible relationships, not an obligatory sequence or a bridge sentence after every result. Delete a closing sentence that merely repeats “proves effectiveness”; retain it when it defines the supported conclusion or passes a substantive question onward. If a core comparison or interpretation contains an inaccurate analogy, rewrite that analogy at the appropriate scientific level rather than deleting the discussion. Preserve the informative contrast and its bounded implication, keeping the claim's relevant variables, conditions, mechanisms and outcomes consistent with the study being evaluated.

Use the local plan's experimental-argument field for the tested claim, contrast, prior expectation versus actual evidence, and supported conclusion/boundary. Preserve real evidence locators and gaps under the canonical ownership rules.

### Sources informing the experiment blueprint

Source provenance for this section is consolidated in [reference-templates.md](source-notes.md#source-notes-and-verification-status). These examples do not override the confirmed project logic or actual venue requirements.
