# 05. [代码审查](../../glossary.md#code-review)规范

[规范目录](../README.md) · [English](../../en/01-governance/review-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 所有进入[保护分支](../../glossary.md#protected-branch)的变更，包括文档、迁移、[CI](../../glossary.md#ci-cd)、[部署声明](../../glossary.md#manifest)及机器人变更。[维护者](../../glossary.md#ownership)配置门禁，作者与审查人对审查记录负责。

## 规范

- **REV-01 MUST（必须）** 创建[变更请求](../../glossary.md#change-request)，提供清晰标题、[工作项](../../glossary.md#issue)链接、变更前后行为、范围、风险、验证证据，以及适用的[上线](../../glossary.md#rollout)与[回滚方案](../../glossary.md#rollback)。视觉变更附脱敏截图，公共 [API](../../glossary.md#api) 变更附代表性请求／响应。未就绪时标记为草稿。
- **REV-02 MUST（必须）** 合并须由至少一名有仓库写权限的人员授权，并由至少一个与该人员不同的独立[合格审核主体](../../glossary.md#qualified-reviewer)批准当前候选版本。涉及[认证／授权](../../glossary.md#authentication-and-authorization)、密钥、[破坏性迁移](../../glossary.md#migration)、关键交付控制或受保护生产基础设施时，须取得至少两个独立的合格审核主体的批准，其中包括相关[领域所有者](../../glossary.md#ownership)。用[所有权规则](../../glossary.md#ownership)分派审查，在平台支持时强制其审批。
- **REV-03 MUST（必须）** 草稿状态、必需检查缺失或失败、冲突未解决、阻塞讨论未关闭、审批已失效时禁止合并。验证最新候选；实质修改后重置或明确重新确认审批，目标分支更新时重跑受影响的检查。并发合并可能让验证失效时，使用合并队列、验证拟议合并结果，或针对当前目标分支重新验证。
- **REV-04 MUST（必须）** 将合并权限限制给指定[维护者](../../glossary.md#ownership)或受控合并服务。尽可能在服务端执行规则。托管平台或套餐不支持某项强制功能时，由有合并权限的指定[维护者](../../glossary.md#ownership)核查并记录等效门禁，或使用受保护的合并服务。清单本身不构成自动门禁。
- **REV-05 SHOULD（推荐）** 让[变更请求](../../glossary.md#change-request)小到可以一次审完。审查正确性、负面路径、[鉴权](../../glossary.md#authentication-and-authorization)与[租户隔离](../../glossary.md#tenant-isolation)、测试、可读性、依赖、兼容性、[可观测性](../../glossary.md#observability)及[回滚](../../glossary.md#rollback)。明确标记阻塞意见并说明影响，区分可选建议。作者处理或讨论后再关闭意见。

## 审批资格与证据

[合格审核主体](../../glossary.md#qualified-reviewer)可以是另一名有写权限的人员、明确获授权在该仓库及变更范围内审批的 [AI Agent](../../glossary.md#ai-agent)，或其他具备同等审批权限的审核身份。所有审批者均须独立于作者及其他参与改动的贡献者。常规变更可以由独立且获授权的 AI 智能体审查并批准，再由一名有写权限的维护者授权合并。

将合并授权和每次审批绑定到所审候选的 [SHA](../../glossary.md#sha)。审批记录应标明审核主体、审批决定和适用的授权依据。自动化审核主体使用独立且可审计的身份，审批权限限定在获授权的范围内。仅有审查评论或 [CI](../../glossary.md#ci-cd) 通过不构成批准。托管平台无法直接计入获授权审核身份的批准时，按 REV-04 落实等效门禁。

## 流程：从提交审查到合并

1. 填写 [变更请求模板](../templates/change-request/Change.md)，运行相关本地检查，邀请受影响模块的审查人。
2. 审查人检查最新差异和证据，必要时重跑高风险场景，再批准所审版本。[紧急修复](../../glossary.md#hotfix)仍走审查；获批偏离按[例外流程](../README.md)留痕。
3. 获[授权](../../glossary.md#authentication-and-authorization)的合并者核对有写权限人员的合并决定、独立审批、讨论、[必过流水线](../../glossary.md#gate)和实际[提交信息](../../glossary.md#commit)，按[分支规范](../02-development/git-branching.md)合并。观察合并后[流水线](../../glossary.md#pipeline)，失败时及时修复或撤销。

**验收证据：** 审查历史、[工作项](../../glossary.md#issue)链接、被检查的 [SHA](../../glossary.md#sha)、成功的[必过作业](../../glossary.md#gate)与最终提交。参阅[执行矩阵](../enforcement.md)。
