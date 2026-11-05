# Introduction writing

Entry guard: apply the active [SKILL.md](../SKILL.md) kernel and its real top/local-comment gate first. If the kernel is absent, read it once; this backlink does not rerun routing. Other links activate only for an actual task condition, never recursive preload.

## Overall structure and length

Use the argument chain **背景使问题成立 → 分类说明已有进展 → 提炼本文要解决的挑战 → 给出对应设计 → 概括创新贡献**. These are functional blocks, not a fixed paragraph count. A motivation figure helps explain the same chain. Adapt to inspected favorite references, real method/evidence and actual journal requirements; preserve the new-paper/overall-logic discussion gate.

For an **integrated layout without a separate Related Work**, retain the usual introduction target of **750–950 English words**, with no universal hard cap. Count the figure caption separately; journal requirements take priority. Suggested allocations are opening 90–130 words, categorized research 260–340 in total, challenges around 120–180, methods overview 160–210 and contributions around 60–90. Allocate within the total instead of taking every upper bound, padding or deleting necessary reasoning to hit a quota. Lengths are project-adaptable guidance, not fixed per-sentence counts or page limits.

For a **separate Related Work**, use the canonical [Related Work module](related-work.md#related-work-rules) only if its detailed division or organization is being changed: shorten the introduction's literature overview to roughly **100–160 English words** of route-level context, move detailed mechanism and nearest-work comparisons to Related Work, and preserve the premises needed for the challenge argument. Do not retain the old 260–340-word review as well or pad other introduction blocks merely to keep the former total. Recalculate the introduction budget from its remaining argument without imposing a replacement total. The two sections may share the same research spine and references for different purposes, but must not repeat the same survey paragraphs or technical detail. Without a separate Related Work, do not add another duplicate review section. These are planning defaults, not permission to restructure a live manuscript outside its authorized scope.

## Opening: choose background from the problem

Plan backward from the precise problem and select only the facts/premises needed to make it intelligible and consequential. Then narrate those facts in a natural order that leads to the problem. Problem-led planning does not require a literal problem/contrast in sentence one. Avoid generic field praise or definitions that could be pasted into any paper and do not help establish the later gap.

Around five sentences is a starting point, with merging/splitting as needed:

| Position | Function | Chinese logic template |
|---|---|---|
| 1 | Specific application objective | [应用或研究过程]依赖[具体能力]，以支持[明确目标]。 |
| 2 | Relevant real-world characteristic | 在这一过程中，[数据、环境、对象或资源]具有[与后续问题有关的特征或约束]。 |
| 3 | Existing capability and its condition | 现有[技术]已经能够[实现什么]，但这一能力通常建立在[相关条件]之上。 |
| 4 | Tension and consequences | 当[现实特征]使该条件难以满足时，[机制层偏差]会导致[具体后果]。 |
| 5 | Define the research need | 因此，需要在[实际约束]下实现[尚未满足的能力]，这构成了[研究任务]的核心需求。 |

Functions need not occupy one sentence each or use those exact expressions. Verify that background supports the problem, the problem warrants the research task, and wording does not imply clinical deployment or another scope beyond the study's evidence.

## Categorized research: usually 2–3 classes

Use a coherent classification criterion such as solution strategy, information used or optimization target. Categories may overlap; explain the basis rather than presenting a false mutually exclusive taxonomy. Do not invent classes to reach a count. In the integrated layout usually discuss each class in one paragraph, expanding only where genuine content requires it. With a separate Related Work, keep a brief route-level overview here and place the detailed functions below in Related Work under its canonical blueprint instead of completing the same comparison twice.

Select the relevant functions for an integrated category paragraph:

1. The common strategy and the problem it addresses.
2. A representative mechanism and its purpose.
3. Meaningful comparisons with other representative approaches, rather than a paper-by-paper name list.
4. What this class has achieved.
5. Its evidence-supported boundary under the conditions relevant to this paper.

Chinese template: **一类方法通过[共同策略]处理[问题]。[代表工作]采用[机制]实现[能力]；其他工作进一步利用[不同策略]改善[具体方面]。这些研究推进了[已有能力]，但在[本文关注的条件]下，[关键因素]仍未得到充分处理，因而留下[相关问题]。**

Use only the paragraph functions needed for the actual argument; the example's contrast ending is optional, not a requirement to attach a defect to every class. Where a passage establishes the research gap, retain a direct, supported account of what existing methods constrain, the conditions under which a limitation remains, and its consequences for the task. Do not flatten that analysis into a neutral list of methods or generic objectives. Class findings can provide premises for the challenge argument. Do not assert that every method in a class shares a failure simply to motivate the proposed model. Keep the explanation of how a real gap creates a challenge in the challenge block, rather than duplicating it in both the introduction survey and Related Work. All literature statements still need appropriate source support and the existing local citation-verification comments; no automatic unrelated bibliography audit.

## Challenges: usually 2–3, tied to the actual innovations

For each important challenge explain **具体缺口 → 形成原因 → 直接后果 → 对研究目标的影响**. Identify the proximate consequence attributable to the described method or constraint, not merely a generic consequence of failing the overall task. Carry that concrete consequence into the challenge and corresponding design, with conditions and evidence appropriate to the claim. A useful starting point is approximately three sentences and 35–55 words per challenge, varying with the reasoning required.

Chinese template: **现有[策略]虽然能够[已有能力]，但未充分处理[关键因素]。由于[具体机制或假设]，[必要操作]难以准确实现。这会产生[直接后果]，进一步限制[本文关注的目标]。**

Organize the challenge analysis around the paper's research goal and innovation, grounded in the real task conditions and inspected evidence. Explicitly connect each relevant limitation and its consequences to the corresponding design, operation and verification. It is useful to work backward from the design to check whether the stated challenge is accurate and the argument closes. The omission of a particular module alone does not establish a deficiency: explain the substantive information or constraint at issue and its task consequence, without inventing failures or redefining the field's task around the solution. Each challenge presented as this paper's core motivation must have an actual response in the method and an identifiable innovation/evidence path. Check **核心挑战 → 对应设计 → 实际创新 → 验证依据** internally and in the relevant Chinese blueprint comments. Categories, challenges, modules and contribution counts need not match one-to-one: several designs may jointly address one challenge. Do not add an unresolved core challenge only for rhetorical drama. Genuine remaining boundaries belong in honest scope/limitations, never a false claim of resolution.

The abstract challenge block must faithfully compress this introduction argument, preserving meaning, scope, mechanism and consequence. It does not need to reproduce every challenge at full detail.

## Method overview: explain the design against the challenges

Use a flexible sequence:

| Position | Purpose |
|---|---|
| Overall proposal | Name the method and state the unifying idea and goal. |
| Design rationale | Explain why that idea responds to the stated problem. |
| Challenge-specific solutions | For each core challenge, identify its mechanism and direct effect. |
| Relationships | Explain real dependencies, parallel roles or complementarity; justify any extra design's distinct role. |
| Closure | State the combined capability within the supported scope. |

For an individual solution, explain **针对什么挑战 → 为什么这样设计 → 关键机制做什么 → 带来什么直接作用**. Use the actual number of sentences needed. A foundation-model name cannot substitute for design rationale. Do not list component names without explaining what their combination accomplishes, or force an invented remaining-problem/shift transition. Keep implementation details and formula-level exposition in the Method unless the introduction needs them to understand the core idea.

## Contributions

Use the author's exact marker:

```latex
\begin{itemize}
\item[\textbullet] 提出什么创新设计，针对什么挑战，形成什么能力。
\item[\textbullet] 引入什么新的机制或策略，解决什么已有缺口。
\item[\textbullet] 概括其他实质贡献或支持核心主张的验证。
\end{itemize}
```

This is a logic template, not mandatory Chinese final prose or a fixed three-item count. Emphasize the new design and its value, tie it to the challenges and method, and avoid copying the method overview verbatim. Retain the existing roughly three-rendered-lines-per-item preference in a two-column layout; rendered compliance is unknown until a requested compile is inspected. Experimental superiority or significance needs evidence; listing a result is not permission to invent it.

## Reference observations

These public examples informed the opening analysis, without making their exact paragraph counts or wording universal: [AlphaFold 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC11168924/) develops a broader modelling question from prior progress; [CellSAM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12695629/) links experimental analysis needs to segmentation and its bottlenecks; [MedSAM](https://pmc.ncbi.nlm.nih.gov/articles/PMC10803759/) connects application/annotation needs with the generalization boundary of specialist models. Author-provided introductions may illustrate research-category, challenge and solution relationships. Their project-specific names and scientific assertions are not transferable defaults or independently verified facts for another manuscript.
