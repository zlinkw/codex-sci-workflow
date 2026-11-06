# 安装与配置

只在实际配置或修复时加载。先检查当前应用、库和版本，保留用户已有配置。选择官方免费稳定版，程序与库按用户指定盘符安装，不购买 Sync/Publish、不建立账户、不初始化或发布 Git 仓库。

最小插件为 BibLib 与 PDF++。从 Obsidian 社区清单所指向的作者仓库发行安装，检查 manifest 的 id、版本、最低应用版本及实际加载状态。下载文件不等于插件成功加载。不要启用 Zotero Connector、外部 AI、OCR、索引或未要求的同步。

可选阅读增强包括 Style Settings、Image Lens、Hover Editor、Better Export PDF，以及 MCL Multi Column / Wide Views CSS。只有用户要求配置时才安装，不继承发布者过去的安装授权，也不要求每个新库全部启用。保留原主题，图片不反色、不裁切。Hover Editor 默认阅读模式且不抢焦点，图片查看交给 Image Lens，避免重复接管图片点击。PDF 导出带书签和页码，不添加重复文件标题。屏幕保留双栏，打印时将嵌套 callout 改为单栏，防止 PDF 的说明段落被挤成多条窄列。

论文模板的 `cssclasses` 使用 `paper-reading` 和 `wide-page`，批次使用 `paper-batch` 和 `wide-page`。图文并排使用标准嵌套 callout 加 MCL 样式，空间不足时自动纵排。批次仍嵌入原笔记，不为分栏复制正文。缺失 MCL 时仍保留可读的 callout 文字与原图链接。

本技能自带的 [paper-library.css](../assets/paper-library.css) 提供阅读宽度、行距、图片适屏和 PDF 单栏打印样式。用户授权配置时将其复制到所选库的 `.obsidian/snippets/` 并启用。MCL 样式从其作者仓库另行获取，不随技能复制第三方插件或完整私人论文库。

如需创建显示检查页或操作流程示意，必须标为说明材料，不是科研论文、原文框架图或实验结果，不放入真实论文列表，也不冒充论文封面。阅读包输出到 `导出/`，正式 BibTeX 仍在 `引用导出/`。

BibLib 识别标签设为 `paper/retained`，笔记目录设为 `论文`，附件设为 `附件`，书目输出设为 `引用导出`，禁止编辑时自动再生笔记正文和引用键。候选由 Codex 按模板写入，不走 BibLib 的直接手动收藏入口。

Bases 提供速览卡片、待展开、详细阅读、待收藏、正式收藏、全部论文和待核实视图。封面字段为 `cover`，`imageFit: contain`。模板不放进论文目录，不把空模板计为论文。批次页嵌入实际论文速览和详细段落。

初始库不放演示论文，不假装已经完成第一轮检索。使用说明清楚写明两次选择与当前提图适配尚未接入。只验证配置语法、插件加载、视图解析与授权内必要界面，不为了交付跑真实论文检索或迁移旧 Zotero 库。

有可用的官方 Obsidian CLI 时优先用它进行有界检查，引用实际安装版帮助，不凭记忆操作。文件是主数据，CLI 不是必须的常驻服务。检查截图不占用用户桌面，不自动删除未经批准的文件。

当前权威入口：
- https://obsidian.md/download
- https://obsidian.md/pricing
- https://obsidian.md/help/bases/syntax
- https://obsidian.md/help/bases/views/cards
- https://obsidian.md/help/cli
- https://callumalpass.github.io/obsidian-biblib/settings/
- https://github.com/RyotaUshio/obsidian-pdf-plus
