# 01. 项目与仓库规范

[规范目录](../README.md) · [English](../../en/01-governance/repository-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 所有源码、文档和基础设施仓库。仓库[维护者](../../glossary.md#ownership)负责入门体验、所有权与基础配置。

## 规范

- **REP-01 MUST（必须）** 指定负责团队和备用联系人。新仓库使用简短、描述性的全小写连字符名称，例如 `order-api` 或 `order-deploy-manifests`。保留既有名称；改名时须处理重定向、[CI](../../glossary.md#ci-cd)、包引用和集成。
- **REP-02 SHOULD（推荐）** 当组件频繁联动且权限与工具一致时采用[单仓库](../../glossary.md#repository-layout)；当所有权、权限或发布节奏不同时采用[多仓库](../../glossary.md#repository-layout)。记录选择理由；[单仓库](../../glossary.md#repository-layout)还要记录组件边界、构建目标、所有者和独立发布规则。
- **REP-03 MUST（必须）** 在根 [README](../../glossary.md#readme) 提供用途、所有者与支持方式、前置条件和工具链、安装与配置、运行／构建／测试命令、架构及发布入口，以及贡献与许可／使用条款。声明经批准的许可证或内部使用条款；未经[授权](../../glossary.md#authentication-and-authorization)不得套用开源许可证。提供 `AGENTS.md`、贡献入口及安全问题报告渠道。
- **REP-04 MUST（必须）** 将格式设置、忽略规则、可复现构建输入及适用的 [CI](../../glossary.md#ci-cd) 和[变更请求](../../glossary.md#change-request)模板纳入版本管理。按需提供 `.editorconfig`、`.gitattributes`、`.gitignore`、工具链声明和依赖[锁文件](../../glossary.md#dependency-lock)。顶层不以点开头的目录留给仓库核心内容，例如 `src/`、`tests/` 和 `docs/`。持续维护的便捷脚本及仅供 CI 使用的辅助文件放入 `.scripts/` 或 `.ci/` 等以点开头的目录。移动辅助文件时同步更新调用方、流水线路径和文档。为供使用方消费而提交的生成源码须记录再生成方法。临时任务脚本与一次性数据遵循 [MNT-09](../05-maintenance/maintenance-standards.md#验收记录不进入源码仓库)，目录以点开头不代表可以将其纳入版本管理。
- **REP-05 MUST（必须）** 记录每项环境变量或配置的类型、是否必填、安全默认值、优先级、示例和保密级别。Git 只保存安全默认值和占位示例，密钥从外部注入。缺少必填配置时应启动失败。配置变更同步更新受影响的应用设置、绑定、容器、[部署声明](../../glossary.md#manifest)、测试与文档。
- **REP-06 MUST（必须）** 排除本地覆盖配置、[凭据](../../glossary.md#secret)、数据库、日志、缓存及构建／测试产物。发布包与镜像存入[制品库](../../glossary.md#registry)，构建报告存入 [CI](../../glossary.md#ci-cd)；忽略规则对已跟踪文件无效。
- **REP-07 MUST（必须）** 通过 .standards/ 下的 [Git 子模块](../../glossary.md#git-submodule)接入共享规范，由父仓库记录经审查的完整提交。根 AGENTS.md 直接链接到 .standards/docs/en/README.md，项目文档提供两种语言的入口。干净检出及 [CI](../../glossary.md#ci-cd) 初始化所记录的提交。固定提交的升级通过正常变更审查，不在验证或发布时跟随可变分支或执行远程更新。参见[接入与更新](../adopting-standards.md)。

## 流程：初始化或接入

1. 确定布局，用[仓库模板](../templates/repository/README-template.md)编写 [README](../../glossary.md#readme)。必要时在组件最近的目录放置 `AGENTS.md`。
2. 启用[分支保护](../02-development/git-branching.md)，指定审查人，接入适用的[质量门禁](../03-quality/testing-standards.md)。按所用平台的规则安装[工作项](../../glossary.md#issue)与[变更请求](../../glossary.md#change-request)模板，参阅[接入示例](platform-examples.md)。
3. 请贡献者从干净检出按 [README](../../glossary.md#readme) 执行，记录成功的构建／检查结果，并确认密钥和产物未被跟踪。

**验收证据：** [README](../../glossary.md#readme)、所有权入口、干净检出命令、[CI](../../glossary.md#ci-cd) 状态与入库配置。组件责任划分与配置联动的示例见[参考实践](../reference-patterns.md)。
