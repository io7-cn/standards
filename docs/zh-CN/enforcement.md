# 门禁执行矩阵

[规范目录](README.md) · [English](../en/enforcement.md) · [平台接入示例](01-governance/platform-examples.md)

按下表接入，并在采用规范的仓库记录实际配置。若受套餐或版本限制，按[审查规范](01-governance/review-standards.md)记录等效控制。本地 Hook 不能作为唯一强制手段。

| 规则 | 门禁与责任人 | 验收方式 |
| --- | --- | --- |
| REP-04、COD-01 | [CI](../glossary.md#ci-cd) 使用入库的[格式化器](../glossary.md#formatter)、[Lint](../glossary.md#lint) 和设置；组件所有者负责 | 故意提交格式错误，确认[必过检查](../glossary.md#gate)失败。 |
| GIT-01、GIT-03 | [分支保护](../glossary.md#protected-branch)规则及服务端或必过 [CI](../glossary.md#ci-cd) 分支命名检查；[维护者](../glossary.md#ownership)负责 | 普通开发者无法直接推送或[强推](../glossary.md#force-push)到[保护分支](../glossary.md#protected-branch)；不合规[工作分支](../glossary.md#topic-branch)名被拒绝。 |
| COM-04 | Commitlint 或等效工具检查保留的提交；受控 [squash](../glossary.md#squash) 消息或合并服务；[维护者](../glossary.md#ownership)负责 | 无效最终主题被拒绝，包含手工修改的 [squash](../glossary.md#squash) 消息。 |
| REV-02–04 | 要求[流水线](../glossary.md#pipeline)通过、讨论解决和审批；使用[所有权规则](../glossary.md#ownership)并限制合并权限；[维护者](../glossary.md#ownership)负责 | 自审、[审批失效](../glossary.md#stale-approval)、[流水线](../glossary.md#pipeline)失败／缺失、阻塞讨论未解决都无法合并。 |
| TST-03 | [Lint](../glossary.md#lint)、构建及适用测试设为[必过作业](../glossary.md#gate)，并发布报告；[CI](../glossary.md#ci-cd) 负责人负责 | 测试失败阻止合并，报告仍可见。用共享依赖改动验证路径过滤。 |
| SEC-01、SEC-03–04 | 密钥检测、[SAST](../glossary.md#sast)、依赖／镜像扫描、[SBOM](../glossary.md#sbom) 和来源校验；安全负责人负责 | 合成测试告警能阻断门禁；不可信[变更请求](../glossary.md#change-request) 无法读取受保护密钥。 |
| CIC-03–07 | [制品](../glossary.md#artifact)不可变或按 [digest](../glossary.md#digest) 寻址，受限的环境访问、串行部署及部署后验证；运维负责人负责 | 未[授权](../glossary.md#authentication-and-authorization)部署与过时[晋级](../glossary.md#promotion)均失败；记录实际[制品](../glossary.md#artifact) [digest](../glossary.md#digest) 和[冒烟结果](../glossary.md#smoke-test)。 |
| REL-02、REL-05 | 保护 Tag、校验签名及限权发布作业；发布负责人负责 | 未签名／未[授权](../glossary.md#authentication-and-authorization) Tag 以及冲突的已发布版本无法发布。 |
| [API](../glossary.md#api)-01、DAT-02 | 按需在 [CI](../glossary.md#ci-cd) 运行 [Schema](../glossary.md#schema)／契约差异检查和迁移演练；契约／数据所有者负责 | 不兼容契约或不安全迁移针对代表性客户端或数据时触发失败。 |
| MNT-01 | Markdown／链接检查及 [变更请求](../glossary.md#change-request)的文档字段；文档所有者负责 | 失效相对链接使 [CI](../glossary.md#ci-cd) 失败，所需文档更新纳入审查。 |
| [MNT-07](05-maintenance/maintenance-standards.md#解释工程术语) | 审查人核对术语在当前语境中是否得到解释，并用自动化检查验证术语锚点。 | 审查人可以从术语跳到正确词条，并通过任一语言的释义理解该术语。 |
| [MNT-08](05-maintenance/maintenance-standards.md#分开维护中英文文档) | 检查文档配对和链接，审查 `AGENTS.md` 及受影响文档的两种版本。 | 两种版本互相链接，纯英文的 `AGENTS.md` 直接打开英文文档入口。 |
| [REP-07](01-governance/repository-standards.md) | 检查记录的[子模块](../glossary.md#git-submodule)提交、初始化检出与英文智能体入口；仓库维护者 | 规范检出缺失、有未提交修改或提交不匹配时验证失败；升级须改变父仓库记录的提交并经过审查。 |

## 配置顺序

1. 按需配置[变更请求](../glossary.md#change-request)、[默认分支](../glossary.md#branch)、受保护的发布[标签](../glossary.md#tag)和下游流程的 [CI](../glossary.md#ci-cd) 触发条件。本地与 [CI](../glossary.md#ci-cd) 共用仓库检查入口。验证[必过作业](../glossary.md#gate)缺失时不能合并[变更请求](../glossary.md#change-request)。
2. 配置服务端分支、Tag、审批与环境控制，检查重叠规则，并以普通开发者权限验证。共享 [CI](../glossary.md#ci-cd) 配置和环境权限按高风险变更保护。
3. 在测试仓库或非生产环境使用合成输入验证拒绝场景。记录证据，在平台能力、组策略或 [CI 执行环境](../glossary.md#runner)的访问权限变化后重新核查。
