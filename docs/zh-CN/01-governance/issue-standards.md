# 06. 需求与任务规范

[规范目录](../README.md) · [English](../../en/01-governance/issue-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 产品需求、缺陷、故障、工程维护与调研。产品或技术负责人负责[分诊](../../glossary.md#triage)和排序，执行人推进工作，验收人确认结果。

## 规范

- **ISS-01 MUST（必须）** 计划工作先建[工作项](../../glossary.md#issue)再实施；紧急工作应及时建立或关联故障记录。类型包括功能、缺陷、维护、调研、安全及故障。敏感证据放在受限记录，公开记录仅引用脱敏信息。
- **ISS-02 MUST（必须）** 记录问题、受影响用户或系统、预期结果、范围内外事项、可衡量的[验收标准](../../glossary.md#acceptance-criteria)、责任人、[优先级](../../glossary.md#priority)与依赖。缺陷还需记录受影响版本／环境、复现步骤、预期与实际行为、影响及脱敏证据。影响验收的非功能要求应写明。
- **ISS-03 SHOULD（推荐）** 澄清范围后评估工作量，记录主要假设、估算区间及不确定性。按可独立验证的结果拆分，分别指定负责人和[验收条件](../../glossary.md#acceptance-criteria)。未知事项设为有时限的[调研任务](../../glossary.md#spike)，产出决策或证据。
- **ISS-04 MUST（必须）** 跟踪状态，保持阻塞、依赖和负责人信息最新。默认流程：待[分诊](../../glossary.md#triage) → 就绪 → 进行中 → 审查中 → 已验收 → 完成。用阻塞标签记录原因和下一步；重复、拒绝或延期关闭时记录理由。可用跟踪系统的状态、标签或看板列实现。
- **ISS-05 MUST（必须）** 关联[工作项](../../glossary.md#issue) → 可行时关联分支 → [变更请求](../../glossary.md#change-request) → [流水线](../../glossary.md#pipeline) → 适用的发布或部署。仅部分交付的[变更请求](../../glossary.md#change-request)使用普通引用；附验收证据且达到约定交付条件后才能关闭。合并自动关闭与生产验收冲突时，使用普通引用并在部署验证后关闭。

## 默认[优先级](../../glossary.md#priority)

| [优先级](../../glossary.md#priority) | 含义与下一步 |
| --- | --- |
| [P0](../../glossary.md#priority) | 正在发生的严重中断、损失或安全暴露。立即启动故障[分诊](../../glossary.md#triage)。 |
| [P1](../../glossary.md#priority) | 影响重大或阻断关键交付。指定负责人，在当前周期安排。 |
| [P2](../../glossary.md#priority) | 常规交付。进入待办排序。 |
| [P3](../../glossary.md#priority) | 小改进或低影响事项。批量处理或说明延期原因。 |

[优先级](../../glossary.md#priority)表示紧迫性；[严重度](../../glossary.md#priority)表示实际影响，应分别记录。这里的标签与规范接入[优先级](../../glossary.md#priority)无关。

## 流程：就绪与完成

用[需求](../templates/issue/Feature.md)或[缺陷](../templates/issue/Bug.md)模板[分诊](../../glossary.md#triage)。范围、验收、负责人及依赖明确后进入就绪。完成前核对预期结果与测试／演示证据，确认约定的交付状态，关联剩余任务并记录验收人。架构决策按[维护规范](../05-maintenance/maintenance-standards.md)补充 [ADR](../../glossary.md#adr)。

**验收证据：** [工作项](../../glossary.md#issue)历史、[验收条件](../../glossary.md#acceptance-criteria)与结果、关联[变更请求](../../glossary.md#change-request)、验证和交付链接。
