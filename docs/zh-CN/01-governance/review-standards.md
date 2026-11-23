# 05. [代码审查](../../glossary.md#code-review)规范

[规范目录](../README.md) · [English](../../en/01-governance/review-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 所有进入[保护分支](../../glossary.md#protected-branch)的变更，包括文档、迁移、[CI](../../glossary.md#ci-cd)、[部署声明](../../glossary.md#manifest)及机器人变更。[维护者](../../glossary.md#ownership)配置门禁，作者与审查人对审查记录负责。

## 规范

- **REV-01 MUST（必须）** 创建[变更请求](../../glossary.md#change-request)，提供清晰标题、[工作项](../../glossary.md#issue)链接、变更前后行为、范围、风险、验证证据，以及适用的[上线](../../glossary.md#rollout)与[回滚方案](../../glossary.md#rollback)。视觉变更附脱敏截图，公共 [API](../../glossary.md#api) 变更附代表性请求／响应。未就绪时标记为草稿。
- **REV-02 SHOULD（推荐）** 在本地开发时、请求合并前进行独立[代码审查](../../glossary.md#code-review)。熟悉相关领域的同事或本地 [Code Review 子代理](../../glossary.md#code-review-subagent)均可检查当前差异和相关证据。涉及[认证／授权](../../glossary.md#authentication-and-authorization)、密钥、[破坏性迁移](../../glossary.md#migration)、关键交付控制或受保护生产基础设施时，建议征求相关[领域所有者](../../glossary.md#ownership)意见，并深入审查失败与恢复路径。
- **REV-03 MUST（必须）** 草稿状态、必需检查缺失或失败、冲突未解决或阻塞讨论未关闭时禁止合并。验证最新候选，目标分支更新时重跑受影响的检查。并发合并可能让验证失效时，使用[合并队列](../../glossary.md#merge-queue)、验证拟议合并结果，或针对当前目标分支重新验证。
- **REV-04 MUST（必须）** 将合并权限限制给指定[维护者](../../glossary.md#ownership)或受控合并服务，在托管平台落实 REV-03 的检查。代码审查的必需批准数设为 0，关闭最后推送及代码所有者的强制批准门禁。用[所有权规则](../../glossary.md#ownership)分派审查请求。有写权限的维护者结合审查意见和验证结果判断是否就绪并决定合并。平台缺少必需的技术强制功能时，由受控合并服务或指定维护者核验并记录等效检查。
- **REV-05 SHOULD（推荐）** 让[变更请求](../../glossary.md#change-request)小到可以一次审完。审查正确性、负面路径、[鉴权](../../glossary.md#authentication-and-authorization)与[租户隔离](../../glossary.md#tenant-isolation)、测试、可读性、依赖、兼容性、[可观测性](../../glossary.md#observability)及[回滚](../../glossary.md#rollback)。明确标记阻塞意见并说明影响，区分可选建议。作者处理或讨论后再关闭意见。

## 审批资格与证据

[合格审核主体](../../glossary.md#qualified-reviewer)具备评估该变更所需的知识与上下文。同事或本地 [Code Review 子代理](../../glossary.md#code-review-subagent)均可承担这一角色。独立审查应由未编写该变更的审查人或单独调用的智能体完成，并提供当前差异、适用规范和相关测试结果。

审查意见应标明所审 [SHA](../../glossary.md#sha) 或当前工作差异、受影响文件、判断依据和相关验证。实质修改后，建议针对改动补充审查。按照 [MNT-09](../05-maintenance/maintenance-standards.md#验收记录不进入源码仓库)，将有保留价值的意见放在变更请求或获准的外部审查记录中。托管平台的批准计数与审核账号权限，和建议的本地审查实践分别处理。

## 流程：从提交审查到合并

1. 填写 [变更请求模板](../templates/change-request/Change.md)，运行相关本地检查，按 REV-02 建议为受影响模块选择本地审查人或子代理。
2. 审查人检查当前差异和证据并给出意见，作者处理意见并重跑受影响检查。本地审查建议遵循 REV-02。[紧急修复](../../glossary.md#hotfix)对强制控制的获批偏离按[例外流程](../README.md)留痕。
3. 获授权的合并者结合审查意见，核对讨论、[必过流水线](../../glossary.md#gate)和实际[提交信息](../../glossary.md#commit)，按[分支规范](../02-development/git-branching.md)合并。观察合并后[流水线](../../glossary.md#pipeline)，失败时及时修复或撤销。

**验收证据：** 审查历史、[工作项](../../glossary.md#issue)链接、被检查的 [SHA](../../glossary.md#sha)、成功的[必过作业](../../glossary.md#gate)与最终提交。参阅[执行矩阵](../enforcement.md)。
