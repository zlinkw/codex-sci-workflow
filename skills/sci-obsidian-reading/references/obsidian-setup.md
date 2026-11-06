# 安装与配置

只在实际配置或修复时加载。先检查当前应用、库和版本，保留用户已有配置。选择官方免费稳定版，程序与库按用户指定盘符安装，不购买 Sync/Publish、不建立账户、不初始化或发布 Git 仓库。

最小插件为 BibLib 与 PDF++。从 Obsidian 社区清单所指向的作者仓库发行安装，检查 manifest 的 id、版本、最低应用版本及实际加载状态。下载文件不等于插件成功加载。不要启用 Zotero Connector、外部 AI、OCR、索引或未要求的同步。

阅读增强可选 Style Settings、Image Lens、Hover Editor 和 Better Export PDF。只在用户要求配置时安装，保留原主题与已有偏好，不把本机历史授权推广到新库。图片不反色、不裁切。Hover Editor 不接管图片点击，图片放大交给 Image Lens。使用其实际设置实现普通单击预览，包括带链接的图片，并验证缩放与关闭，不假定安装即生效。

屏幕默认接近铺满编辑区，只保留少量边距。正文和图片均采用单栏，完整框架图在说明上方，不限制图片高度。阅读模式和实时预览都需覆盖。论文使用 `paper-reading`，批次使用 `paper-batch`。`wide-page` 与现有 MCL 可以保留兼容，但不再要求安装 MCL 或生成双栏 callout。打印也使用单栏，保留书签/页码，避免重复标题。

[paper-library.css](../assets/paper-library.css) 是默认样式。配置前读取库内 `阅读偏好.md`、实际 `.obsidian` 设置和当前样式，只更新必要项，不盲目覆盖用户后来的配置。默认全宽、无图片高度上限，关闭所选库的“缩减栏宽/Readable line length”限制。核实当前窗口打开的库，父库和嵌套论文库有独立设置，不把修改另一个库当成当前窗口已生效。

操作说明与显示示例不是真实科研论文，不放入真实论文列表，不冒充原文框架图或实验结果。阅读包输出到 `导出/`，正式 BibTeX 在 `引用导出/`。

BibLib 识别标签设为 `paper/retained`，笔记目录设为 `论文`，附件设为 `附件`，书目输出设为 `引用导出`，禁止编辑时自动再生笔记正文和引用键。候选由 Codex 按模板写入，不走 BibLib 的直接手动收藏入口。

Bases 提供速览卡片、待展开、详细阅读、待收藏、正式收藏、全部论文和待核实视图。前四个视图按当前批次指针过滤，后三个保留全库范围，具体契约见 [batch-reading.md](batch-reading.md)。封面字段为 `cover`，`imageFit: contain`。模板不放进论文目录，不把空模板计为论文。批次页嵌入实际论文速览和详细段落。

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
