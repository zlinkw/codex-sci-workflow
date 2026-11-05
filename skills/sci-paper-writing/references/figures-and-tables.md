# Figure and table writing

Entry guard: apply the active [SKILL.md](../SKILL.md) kernel and its real top/local-comment gate first. If the kernel is absent, read it once; this backlink does not rerun routing. Other links activate only for an actual task condition, never recursive preload.

Read for title, caption, legend or note work. Shared evidence, scope and comment ownership remain in [SKILL.md](../SKILL.md#global-agreement-precedence-and-consistency). Use the current actual display; this guide does not itself authorize drawing or compilation.

## Figure rules

Apply this section to figure/table titles, captions, legends and notes. The default division is **短题交代对象与比较问题；图注说明读图方式及必要条件；表注解释读表规则；正文分析观察的意义、原因、例外和边界**. A reader with the display and its caption/notes should understand the relevant information without searching the main text for essential definitions. Repeat needed terms, units and conditions; do not reproduce the Method or Results analysis merely to make a caption self-contained. For motivation-figure planning, also use the specialized introduction reference, without duplicating its scientific argument here.

### Titles and caption sentence logic

The figure title is normally the caption's opening phrase or sentence; avoid duplicating it as a large title inside the image. A table title identifies the comparison, task/dataset and consequential conditions. Prefer specific content over generic titles such as “experimental results” or evaluative labels such as “superior performance.” A bounded finding may appear in a title when supported, but is not compulsory for every display.

| 用途 | 中文短题逻辑 |
|---|---|
| 动机 | ［具体问题］及［针对性处理思路］ |
| 方法 | ［方法名/关键机制］的整体流程 |
| 定性比较 | ［任务与条件］下［不同方法］的预测比较 |
| 消融 | ［关键设计］对［具体能力/指标］的影响 |
| 敏感性 | ［指标或行为］随［参数/条件］的变化 |
| 失败案例 | ［明确条件］下的失败案例及具体表现 |

Use **［展示对象与问题］→［面板或行列对应关系］→［必要条件及编码］→［可选的一句有边界的直接观察］** as a flexible Chinese caption blueprint. The first sentence identifies the task, objects and comparison/relationship. Explain panels in their actual `(a), (b), ...` or row/column order, then include only the conditions and decoding information needed to interpret them. Merge functions naturally; impose neither a fixed sentence count nor an obligatory concluding effectiveness claim. Explain what is visible rather than adding generic bridge sentences. Keep method/module names and symbols consistent with the manuscript.

- **Method diagrams:** identify inputs, consequential operations, outputs and real relationships; define solid/dashed arrows, shared parameters and training/inference-only branches where used. A conceptual process is not evidence of a performance gain; omit a full equation/implementation recap.
- **Qualitative results:** identify task/modality/adaptation direction, method order, row/column correspondence, reference annotation, zoomed regions and meaningful arrows/overlays. Restrict a visible observation to the shown cases or regions; do not generalize from selected images to population-level superiority. Supply anatomical orientation, physical scale or display-window information where necessary and actually known, never invented.
- **Quantitative curves and ablations:** define axes/units, comparison groups, aggregation, replicate unit/count and uncertainty as applicable. Name the actual meaning of shading/error bars, such as SD, SE or CI; “variation range” alone is inadequate. Describe a supported trend or exception briefly without reporting every point.
- **Motivation schematics:** label conceptual distributions or predictions as schematic, not measured t-SNE, verified failures or experimental outcomes. Preserve the specialized motivation/challenge-panel logic in the introduction reference.
- **Feature projections:** identify the projection method and color/shape meanings needed for interpretation. A two-dimensional embedding alone does not establish alignment, discrimination or a causal mechanism.

Keep a consistent visual vocabulary across the paper: use one stable meaning for each scientifically meaningful color, marker, line style, arrow, size or highlight. Distinguish failure marks from processing paths; a red dashed line must not ambiguously mean both boundary and selected anomaly. Legends, axes and colorbars must carry their necessary labels rather than outsourcing all decoding to the caption. Definitions already clear in the legend need not be copied word for word. Use redundant non-color cues and check readability at the actual rendered size when rendering is authorized; a color name or “best viewed in color” is not a substitute for interpretable encoding.

### Table titles and notes

Use **［比较内容］＋［任务/数据集］＋［决定比较含义的条件］** for a table title, and **［数值及统计口径］→［特殊行列/缩写］→［强调与符号规则］→［来源及必要例外］** for notes. Put metric names, units and directions in column headers where practical, such as `Dice (%) ↑` or `HD95 (mm) ↓`; keep supplementary decoding below the table under the actual template. Do not move a Results discussion into the table title or notes.

- Define the actual estimator and aggregation unit: a mean over classes, patients, folds or seeds has a different interpretation. State whether `±` is SD or another quantity and what repeats vary; do not relabel patient variation as independent-run variability. Specify weighting/averaging when consequential to the comparison.
- Define abbreviations, marks, checkmarks and special rows/columns. Explain the ranking scope for bold/underline and handle ties consistently. **Numerical rank is not statistical significance.** If significance symbols appear, identify the actual test, comparison, threshold and relevant multiplicity treatment; never infer a test or add stars without verified analysis.
- Separate original-paper reported values from local reproductions and distinguish supervised reference bounds or incompatible source/target access conditions. Do not hide consequential setting differences inside one unqualified ranking. Reuse the existing comparison/evidence rules rather than asserting fairness from a tidy table.
- Distinguish unavailable, unreported, inapplicable and zero values; define the missing-data notation actually used and never fill a gap with zero. Preserve appropriate numerical precision and ensure percentages and units match the source data.

### Findings, prose division and consistency

A caption may include one concise direct observation if it helps locate the evidence, for example **“在所示病例的标记区域，［具体错误］较少”**, only when visible. The body then explains the informative contrast, agreement with other evidence, innovation addressed, and limitations. Do not repeat the same group of values in caption, table and prose, add a generic effectiveness ending to every display, emphasize only favorable trends, or delete essential definitions merely to avoid overlap.

Before delivering a caption/note edit, check it against the actual current display, not its filename or an old description: panel labels/order, rows/columns, method/structure colors, markers, units, adaptation direction, reference annotation, crop/zoom correspondence, statistical meaning and source version. Reconcile numbers, qualifiers and scientific claims with the relevant source evidence and manuscript/reply under the existing consistency rules. Rank, significance and mechanism evidence remain distinct. If the display cannot be inspected or the data/analysis is unavailable, identify the exact gap rather than claim visual/statistical verification. Editing captions does not authorize changing data, drawing an image, running experiments or compiling.

### Flexible length guidance and examples

These are personal suggested **English-word** ranges, not measured TMI/MedIA norms, journal hard limits or quotas. Count readable caption text including its opening title, excluding automatic numbering, TeX markup and comments; count table title and notes separately. Journal requirements and actual completeness take priority; do not pad short content or remove essential qualifiers to hit a range. Chinese blueprints follow their own content needs, not these figures relabeled as character counts.

| 部分 | 通常建议 |
|---|---|
| 图题/表题短语 | 6–15 words |
| 简单单面板图注 | 30–60 words |
| 动机图注 | 60–110 words，沿用原默认，独立于引言正文预算 |
| 方法框架图注 | 70–130 words |
| 多面板定性比较图注 | 60–110 words |
| 定量曲线/消融图注 | 50–100 words |
| 表注合计 | 30–80 words，复杂统计或设置可适当增加 |

Adaptable Chinese examples, not statements about an existing figure or completed experiment:

- **Method:** “［关键机制］的流程。［输入］经［操作及真实关系］得到［输出］。实线表示［实际含义］，虚线表示［实际含义］；推理阶段保留［真实分支］。” Include only encodings that exist in the image.
- **Qualitative:** “［实际任务与条件］下的［比较对象］。各列依次为［实际列顺序］，各行对应［真实样本及其关系］。［标记］指示［实际可见区域或现象］。［仅在支持时加入所示样本的具体观察］。” Define meaningful visual encodings in the actual legend/caption.
- **Quantitative:** “［参数］变化下的［任务指标］。横轴为［参数与单位］，纵轴为［指标与单位］。各点表示［真实重复单位及次数］上的均值，阴影表示［实际不确定性定义］，其余条件为［实际控制条件］。［必要时一句趋势或例外］。”
- **Table:** title “［实际研究条件］下［比较对象或因素］的［评价内容］”; notes “数值为［真实次数/单位］的［实际汇总量及不确定性］。［指标及单位/方向］；［强调方式］标出［明确比较组及规则］。［符号］表示［真实来源/特殊设置］。” Use only estimators, comparisons and marks present in the actual study.

### Local source comments and venue formatting

Use the local display-plan field immediately before the outer LaTeX figure/table source. Record only its purpose, panel/row/column correspondence, encoding/statistics, actual observation and boundary, prose division and source gap as relevant. Follow the canonical comment ownership rules; moving an authorized display moves its plan.

Follow the verified journal template for numbering, casing, punctuation and title/caption/note placement; do not manually apply bibliography-title casing rules to displays. Preserve stable labels and references, with TeX labels after their caption. Cite the relevant panel where the body needs it and follow the existing reused/adapted-material attribution and permissions requirements. Rendered placement is unknown until an authorized compile is inspected. The author's existing figure layout below remains unchanged by caption work.

Source provenance for figure/table guidance is consolidated in [reference-templates.md](source-notes.md#source-notes-and-verification-status).

### Existing figure layout

- Default to a full-width two-column figure with `figure*`, top placement `[t!]`, and `width=\textwidth`.
- Use the following structure:

```latex
\begin{figure*}[t!]
\centering
\includegraphics[width=\textwidth]{<figure-file>}
\caption{<caption>}
\label{<label>}
\end{figure*}%
```

- Keep `width=\textwidth` by default. Do not choose or adjust a narrower width unless the user explicitly requests it; width tuning belongs to the user.


