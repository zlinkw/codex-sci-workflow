# codex-sci-workflow

面向 Codex 的九项科研技能，覆盖读论文、Obsidian 批量筛读与收藏、文献检索、实验规划、结果分析、论文写作、审稿和参考文献管理。用最匹配的技能处理当前问题，需要跨阶段协作时再使用总流程技能。

这些技能来自个人科研工作流，保留了具体写作偏好和审核约定。它们不是 OpenAI 官方技能包，也不保证论文接收或实验结论正确。项目指令和作者的明确要求优先。

## 包含的技能

| 技能 | 用途 | 调用示例 |
|---|---|---|
| [sci-research-workflow](skills/sci-research-workflow/SKILL.md) | 协调跨阶段科研任务和证据流转 | `$sci-research-workflow` 统筹从实验到论文的工作 |
| [sci-paper-reading](skills/sci-paper-reading/SKILL.md) | 精读论文、学习新课题、分析创新点 | `$sci-paper-reading` 精读这篇论文 |
| [sci-obsidian-reading](skills/sci-obsidian-reading/SKILL.md) | 在 Obsidian 中批量图文速览、两轮选择、收藏、关联和引用导出 | `$sci-obsidian-reading` 按我的阅读偏好推荐 10 篇论文 |
| [sci-literature-review](skills/sci-literature-review/SKILL.md) | 检索文献、核查原始来源、综合相关研究 | `$sci-literature-review` 查找相关原始研究 |
| [sci-experiment-planning](skills/sci-experiment-planning/SKILL.md) | 规划复现、基线、消融和实验配置 | `$sci-experiment-planning` 设计消融实验 |
| [sci-results-analysis](skills/sci-results-analysis/SKILL.md) | 分析日志、指标、统计和失败案例 | `$sci-results-analysis` 检查已有实验结果 |
| [sci-paper-writing](skills/sci-paper-writing/SKILL.md) | LaTeX 写作、回复信及修订审核 | `$sci-paper-writing` 修改论文并回复相关审稿意见 |
| [sci-paper-review](skills/sci-paper-review/SKILL.md) | 自审论文，检查论证、实验和一致性 | `$sci-paper-review` 检查主张与证据是否一致 |
| [sci-bibliography](skills/sci-bibliography/SKILL.md) | 核对 BibTeX、引文和参考文献格式 | `$sci-bibliography` 核查参考文献 |

自然语言请求也可以触发匹配的技能。仓库不包含架构绘图技能、SimpleExperiment/SimpleSFTP 技能、服务器工具或其他通用开发技能。

## 安装

### 方法一：复制一条命令，安装全部九项

需要 Git 和 Python。下列命令先将仓库下载到当前目录，再将九项技能复制到用户目录 `~/.agents/skills/`。不安装依赖、不执行实验、不修改已有论文或编辑器配置。

Windows PowerShell 7：

```powershell
git clone https://github.com/zlinkw/codex-sci-workflow.git && python codex-sci-workflow/install.py
```

macOS / Linux：

```bash
git clone https://github.com/zlinkw/codex-sci-workflow.git && python3 codex-sci-workflow/install.py
```

如果仓库已下载，直接执行其 `install.py`，不必重复 clone。安装器会先检查全部目标，遇到同名技能目录就停止，不覆盖已有内容。需要更新时先自行比较现有版本，或选择另一个明确的安装位置。

仅安装部分技能：

```bash
python3 codex-sci-workflow/install.py --skill sci-paper-reading sci-literature-review
```

安装到当前项目的技能目录：

```bash
python3 codex-sci-workflow/install.py --dest .agents/skills
```

Windows 将上述 `python3` 换成 `python`。部分技能相互引用，推荐安装全部九项。只装部分时，相关跨阶段功能还需要对应技能。

### 方法二：交给 Codex 的内置安装器

在 Codex 中发送：

```text
$skill-installer 请从 GitHub 仓库 zlinkw/codex-sci-workflow 安装 skills/ 下的全部九项技能，不覆盖我已有的同名技能。
```

### 方法三：手动复制

下载仓库，将 `skills/` 下需要的整个技能文件夹复制到 `~/.agents/skills/`，不要只复制 `SKILL.md`，配套的 references、scripts、assets 和 agents 目录也要保留。

Codex 通常会自动发现新增技能。如果未显示，重启 Codex。安装位置与发现方式见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## Obsidian 论文阅读

`sci-paper-reading` 负责理解论文，`sci-obsidian-reading` 负责批次、图文笔记和两轮选择，不维护第二套论文库。AI 使用 Codex，不要求 Zotero、其他 AI、向量数据库或全库索引。

默认流程：每批 10 篇图文速览 → 选择感兴趣的编号 → 详细阅读重新编号 → 再次明确确认收藏。每篇只保留一份权威笔记，候选不会因为展开或保存而自动成为正式收藏。

速览从第一轮就提供完整原文框架图、期刊或会议及年份，并尽可能展示实验原图。框架图默认作封面。优先阅读方法流程和实质思想，默认排除仅以注意力路径、卷积组合等常规结构变化为主要贡献的论文。

当前个人工作流的来源限制为中科院大类或任一小类一区期刊、CCF A 类会议，以及 MICCAI、BIBM。每篇需要核实所用版次与来源。具体约定以用户库内的 `阅读偏好.md` 为准，明确修改须由用户提出，不把 JCR Q1 混作中科院一区。

仅安装阅读相关技能：

```bash
python3 codex-sci-workflow/install.py --skill sci-obsidian-reading sci-paper-reading sci-literature-review sci-bibliography
```

首次使用时提供自己的 Obsidian 库目录。公开版本的 `references/local-vault.md` 不预设作者电脑路径。技能附带论文和批次模板、Bases 视图及阅读 CSS，不包含私人笔记、PDF、插件二进制或整套 Obsidian 库。

需要配置应用时，按相应指南使用 BibLib 与 PDF++，可选 Style Settings、Image Lens、Hover Editor 和 Better Export PDF。默认全宽单栏、框架图在说明上方，图片支持单击放大，保留用户库内后续偏好。当前批次视图读取 `当前批次.md` 的 `active_batch`，历史资料与正式收藏保留全库范围。安装技能不会自动安装插件。原图优先复用已有提图工具，必要时可使用已安装 PDF 工具提取真实原图，不重绘科研图。

## 工作原则与写作偏好

- 实验结论需要项目运行记录、结果表或 claims 证据支持，不能编造结果、引用或实现细节。有效但不理想的结果不得按性能排除，失败、重试与统计单位须可追溯。
- 优先修改已有内容，非必要不增加篇幅。复用原稿术语，不为回复审稿人另造名称。
- 有准确的过程、模块或模型主语时优先使用，但不全面禁止第一人称。
- 每条回复首句感谢，以实际修改后的内容为依据，统筹处理完整审稿问题及关联修改。
- 回复信是否附修后原文，写作前先与作者约定。需要时在最终统一标红阶段集中插入。
- 原稿基准固定后，最终修订稿的新增和替换内容统一标红。批注插件负责审核与接收，不逐次写颜色。

具体规则以各技能文件为准。技能安装不会自动修改项目 AGENTS.md，也不会自动初始化 Git、创建远端或授权运行实验。

## 按需使用的工具

| 使用场景 | 需要的工具或条件 |
|---|---|
| 读写与人工审稿 | 能访问项目文件的 Codex。检索来源需要可用的搜索或浏览工具 |
| Obsidian 图文阅读与收藏 | 用户指定的 Obsidian 库。配置时按阅读指南安装相应插件，纯论文理解不依赖 Obsidian |
| LaTeX 编译及最终 PDF | 本机 LaTeX 工具链，例如 TeX Live/TinyTeX 和 latexmk |
| 配套 Python 审核工具 | Python 3.12+。依具体命令的帮助和引用文档运行 |
| 原文件审核卡片及完整审核 PDF | 与文档协议匹配的 TeXScholar 本地扩展及相关 LaTeX 工具。安装技能本身不会安装或启用扩展 |
| 正式实验与远程传输 | 已核实的项目脚本、CLI、调度器、SSH/tmux、SFTP/scp/rsync 或 API。遵循通用执行与证据规范，不要求指定插件。SimpleExperiment/SimpleSFTP 仅为可选工具，不包含在本仓库 |
| Git 成果备份 | Git、有效的远端和项目授权。Git 不是普通写作的前提 |

`sci-paper-writing/assets/vscode-local-latex/` 和旧打包脚本是技能随附的历史审核组件源码，保留依赖完整性，不代表当前 TeXScholar 发行版。安装器只复制技能，不构建或安装 VSIX。进阶操作需要先核对实际工具版本和能力。

## 来源与发布范围

参考来源保存在技能的 `references/source-notes.md` 等文件中，第三方资源保留链接与原有署名。历史审核组件的 MIT 许可保留在其目录内。仓库没有为全部来源统一重新授权，具体组件沿用其已有许可。

本仓库仅发布这九项技能及必要配套文件，不包含论文项目、实验数据、服务器配置、凭据、运行时审核状态、缓存或清理归档。本机特有的维护路径仅在发布副本中改成通用说明，原本机技能不受影响。
