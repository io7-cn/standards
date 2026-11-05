# 09. 版本与发布规范

[规范目录](../README.md) · [English](../../en/04-delivery/release-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 公共软件包、应用、服务与独立发布组件。指定发布负责人协调兼容性、[制品](../../glossary.md#artifact)发布与恢复。

## 规范

- **REL-01 MUST（必须）** 定义各产品对外兼容范围与版本真源。带版本的[公开契约](../../glossary.md#contract)使用 [SemVer 2.0.0](../../glossary.md#semver)：兼容修复升补丁号，兼容功能及公开 [API](../../glossary.md#api) [弃用](../../glossary.md#deprecation)升次版本号，1.0 后的[破坏性变更](../../glossary.md#breaking-change)升主版本号。记录 `0.y.z` 的兼容承诺；[预发布](../../glossary.md#release-candidate)使用 `1.5.0-rc.1` 等标识。内部[持续交付](../../glossary.md#ci-cd)服务可用已记录的 [SHA](../../glossary.md#sha)／[digest](../../glossary.md#digest) 标识发布，对外契约仍单独编号。
- **REL-02 MUST（必须）** 同步受影响的清单、[锁文件](../../glossary.md#dependency-lock)及文档中的版本。对验证过的受保护历史使用受保护、签名且带附注的 Git Tag，如 `v1.4.0`、`v1.5.0-rc.1` 和 `v1.4.1`。多组件仓库可定义带组件命名空间的 Tag，例如 `sdk/v1.4.0`。不得移动已发布 Tag 或覆盖同版本[制品](../../glossary.md#artifact)；更正时发布新版本。
- **REL-03 MUST（必须）** 维护面向用户的 [Changelog](../../glossary.md#release-notes-and-changelog) 或等效有序发布历史。[发布说明](../../glossary.md#release-notes-and-changelog)包含版本／日期、主要变更、修复、可披露的安全影响、破坏性或[弃用](../../glossary.md#deprecation)行为、配置／[数据迁移](../../glossary.md#migration)、已知问题及升级／恢复步骤。关联[工作项](../../glossary.md#issue)、[源码 SHA](../../glossary.md#sha)、[不可变制品](../../glossary.md#artifact)、[流水线](../../glossary.md#pipeline)和验证记录。
- **REL-04 MUST（必须）** 验证与已部署客户端、配置及 [Schema](../../glossary.md#schema) 的兼容性。混合版本[上线](../../glossary.md#rollout)时记录兼容矩阵和顺序。生产变更前明确[回滚](../../glossary.md#rollback)阈值、负责人、已知可用版本及数据恢复方案；破坏性或不可逆步骤须演练。
- **REL-05 MUST（必须）** 仅通过[授权](../../glossary.md#authentication-and-authorization) [CI](../../glossary.md#ci-cd) 发布已验证输入并按[环境晋级](cicd-standards.md)。[热修复](../../glossary.md#hotfix)遵守相同的不可变发布规则，可加急审查并按需[移植](../../glossary.md#backport-and-forward-port)；不得原地重发以修复坏版本。

## 流程：准备、发布与恢复

1. 确定受影响组件，更新版本并填写[发布记录](../templates/release/Release.md)。审查[发布说明](../../glossary.md#release-notes-and-changelog)、依赖兼容性、迁移、配置、[弃用](../../glossary.md#deprecation)和恢复。
2. 验证候选版本，仅从[授权](../../glossary.md#authentication-and-authorization)引用发布一次。用[制品](../../glossary.md#artifact) [digest](../../glossary.md#digest)／[校验和](../../glossary.md#digest)标识[晋级](../../glossary.md#promotion)对象，确认安装说明可用，[冒烟](../../glossary.md#smoke-test)后记录实际生产状态。
3. 未达到阈值时停止[晋级](../../glossary.md#promotion)，按计划恢复兼容旧版或[向前修复](../../glossary.md#roll-forward)。使[期望状态](../../glossary.md#desired-state)与实际一致，验证真实流量及数据，记录决策；平台允许时标注问题版本或撤回。不得盲目逆向执行[数据迁移](../../glossary.md#migration)。

**验收证据：** 经批准的发布记录、[受保护引用](../../glossary.md#ref)及适用的签名 Tag、[发布说明](../../glossary.md#release-notes-and-changelog)、源码／[流水线](../../glossary.md#pipeline)／[制品](../../glossary.md#artifact)身份、[冒烟](../../glossary.md#smoke-test)与恢复结果。另见 [API 与数据](../02-development/api-data-standards.md)及[弃用流程](../05-maintenance/maintenance-standards.md)。
