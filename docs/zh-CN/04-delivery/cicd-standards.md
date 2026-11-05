# 08. [CI/CD](../../glossary.md#ci-cd)、构建与部署规范

[规范目录](../README.md) · [English](../../en/04-delivery/cicd-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** [流水线](../../glossary.md#pipeline)、[制品](../../glossary.md#artifact)与环境。[CI](../../glossary.md#ci-cd) [维护者](../../glossary.md#ownership)负责流程和 [Runner](../../glossary.md#runner) 信任，发布负责人负责[晋级](../../glossary.md#promotion)，运维负责生产部署和恢复。

## 规范

- **CIC-01 MUST（必须）** 为[变更请求](../../glossary.md#change-request)运行[必过检查](../../glossary.md#gate)，并验证[受保护引用](../../glossary.md#ref)的变更。明确[变更请求](../../glossary.md#change-request)、[默认分支](../../glossary.md#branch)更新、[标签](../../glossary.md#tag)、定时任务和下游流程何时触发 [CI](../../glossary.md#ci-cd)。避免因分支和[变更请求](../../glossary.md#change-request)事件对同一候选重复检查。按需执行校验、测试、构建、扫描、打包、发布、部署及验证。不可信[变更请求](../../glossary.md#change-request)不得访问发布或生产[凭据](../../glossary.md#secret)。
- **CIC-02 MUST（必须）** 固定工具链与依赖；共享[流水线](../../glossary.md#pipeline)模板固定到经过审查的引用。可行时按 [digest](../../glossary.md#digest) 固定生产[基础镜像](../../glossary.md#container-image)和 [CI](../../glossary.md#ci-cd) 镜像，并记录更新方式。从干净检出构建，隔离可信缓存，记录[源码 SHA](../../glossary.md#sha)、[流水线](../../glossary.md#pipeline)、构建输入及产物身份。缓存不等于发布[制品](../../glossary.md#artifact)。
- **CIC-03 MUST（必须）** 将不可变且唯一命名的产物发布到批准的[制品库](../../glossary.md#registry)。可用仓库／产品名加版本或提交作可读[标签](../../glossary.md#tag)；部署容器按 [digest](../../glossary.md#digest)，其他[制品](../../glossary.md#artifact)按不可变版本及[校验和](../../glossary.md#digest)。按[安全规范](../03-quality/security-standards.md)关联扫描、[SBOM](../../glossary.md#sbom) 和[来源证明](../../glossary.md#provenance)。按[制品](../../glossary.md#artifact)类型设置保留期；部署中及[回滚](../../glossary.md#rollback)所需版本和发布证据至少保留至支持／[回滚](../../glossary.md#rollback)窗口结束。
- **CIC-04 MUST（必须）** 同一[制品](../../glossary.md#artifact)从测试、[预生产](../../glossary.md#environment)[晋级](../../glossary.md#promotion)到生产，各环境配置独立注入。签名、平台或打包约束需要生成新产物时，赋予独立身份，重新验证并建立[晋级](../../glossary.md#promotion)证据。
- **CIC-05 MUST（必须）** 保护[部署环境](../../glossary.md#environment)，按环境限制部署角色与[凭据](../../glossary.md#secret)。开发、测试可自动部署；生产须显式审批，或采用已[授权](../../glossary.md#authentication-and-authorization)、具备等效门禁、可审计身份和[回滚](../../glossary.md#rollback)能力的书面自动策略。对同一环境串行变更，拒绝过时[晋级](../../glossary.md#promotion)。
- **CIC-06 MUST（必须）** 以经过审查的[期望状态](../../glossary.md#desired-state)管理部署输入，保持唯一权威部署入口。采用[部署清单](../../glossary.md#manifest)的服务，应用 [CI](../../glossary.md#ci-cd) 仅向部署仓库或服务交付[制品](../../glossary.md#artifact)身份及来源证据，不直接修改生产宿主机。按项目使用批准的 [Kubernetes](../../glossary.md#kubernetes)、[Compose](../../glossary.md#compose) 或等效部署流程，配置资源、就绪／[健康探针](../../glossary.md#health-and-readiness)及发布超时。
- **CIC-07 MUST（必须）** [上线](../../glossary.md#rollout)后验证实际运行的[制品](../../glossary.md#artifact)身份、健康、[冒烟结果](../../glossary.md#smoke-test)及指标。失败时停止[晋级](../../glossary.md#promotion)，使用已知可用[制品](../../glossary.md#artifact)及兼容配置／[Schema](../../glossary.md#schema)，或执行有记录的[向前修复](../../glossary.md#roll-forward)／恢复。记录实际结果，不能只看部署作业状态。

## 默认环境细则

| 环境 | 触发与[制品](../../glossary.md#artifact)身份 | 进入下一步的门禁 |
| --- | --- | --- |
| 开发／[变更请求](../../glossary.md#change-request)预览 | 可自动部署短期候选，[凭据](../../glossary.md#secret)及数据隔离 | 提供[冒烟](../../glossary.md#smoke-test)或评审反馈；[变更请求](../../glossary.md#change-request)关闭后清理预览。 |
| 测试 | [CI](../../glossary.md#ci-cd) 部署不可变发布候选 | 针对该[制品](../../glossary.md#artifact)通过集成与[契约检查](../../glossary.md#contract-test)。 |
| [预生产](../../glossary.md#environment) | [晋级](../../glossary.md#promotion)同一候选，使用类生产配置及代表性数据 | 验证迁移与[回滚](../../glossary.md#rollback)准备及关键流程。 |
| 生产 | 通过[授权](../../glossary.md#authentication-and-authorization)部署入口[晋级](../../glossary.md#promotion)获批候选 | 核对实际 [digest](../../glossary.md#digest) 和健康阈值；失败时暂停或恢复。 |

风险允许时项目可合并环境，但应记录保留哪些门禁与隔离边界。

## 流程：[晋级](../../glossary.md#promotion)与部署

1. 核对受保护候选的[必过作业](../../glossary.md#gate)、[digest](../../glossary.md#digest)／[校验和](../../glossary.md#digest)及[来源证明](../../glossary.md#provenance)。确认环境当前版本、配置及[迁移方案](../02-development/api-data-standards.md)。
2. 更新并审查[部署声明](../../glossary.md#manifest)或已[授权](../../glossary.md#authentication-and-authorization)变更单，按需取得环境审批。按 [digest](../../glossary.md#digest)／[校验和](../../glossary.md#digest)[晋级](../../glossary.md#promotion)，执行发布，等待就绪并跑关键[冒烟](../../glossary.md#smoke-test)路径。
3. 在观察窗口内按预设健康／[回滚](../../glossary.md#rollback)阈值判断。失败时暂停后续[晋级](../../glossary.md#promotion)，按故障流程通知[值班](../../glossary.md#on-call)，恢复兼容的[期望状态](../../glossary.md#desired-state)或[向前修复](../../glossary.md#roll-forward)，再验证并记录结果。

**验收证据：** [流水线](../../glossary.md#pipeline)、[制品](../../glossary.md#artifact)及 [digest](../../glossary.md#digest)、已审查的声明／审批、变更前后期望与实际版本、[冒烟结果](../../glossary.md#smoke-test)及恢复记录。参阅[执行矩阵](../enforcement.md)和[参考实践](../reference-patterns.md)。
