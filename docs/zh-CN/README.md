# 软件开发规范

[English](../en/README.md) · [执行矩阵](enforcement.md) · [参考实践](reference-patterns.md) · [平台接入示例](01-governance/platform-examples.md) · [工程术语表](../glossary.md)

[接入固定版本](adopting-standards.md) · [贡献与问题报告](contributing.md)

本简体中文版与英文版对应。规范适用于艾欧柒（杭州）智能科技有限公司所有产品研发序列，包括开源和内部项目的应用、软件库及配套基础设施。按项目涉及的活动和组件应用相应条款，适用范围跨代码托管平台和 [CI/CD](../glossary.md#ci-cd) 系统。C#、[TypeScript](../glossary.md#ts) 和 [CSS](../glossary.md#css) 的专项要求见[代码开发规范](02-development/coding-standards.md#主要技术栈)。

**[变更请求](../glossary.md#change-request)**是用于审查并合并拟议变更的记录，例如 [Pull Request](../glossary.md#change-request) 或 [Merge Request](../glossary.md#change-request)。**[工作项](../glossary.md#issue)**（[Issue](../glossary.md#issue)）可以记录在独立的跟踪系统中。

## 如何应用规范

- **[MUST](../glossary.md#requirement-levels)（必须）**是强制要求；**[SHOULD](../glossary.md#requirement-levels)（推荐）**是建议默认做法，重大偏离应记录理由；**[MAY](../glossary.md#requirement-levels)（可选）**可自行决定。规范定义必须遵守的规则，指南说明默认方案与替代选择，流程描述操作步骤。
- 在仓库 [README](../glossary.md#readme) 或贡献文档记录采用版本、责任人、工具链、分支模型、门禁、发布触发条件和运行细则。项目指令补充实施细节；与 [MUST](../glossary.md#requirement-levels) 冲突需显式例外，其他适用的更严格政策仍有效。
- 申请例外时，在[工作项](../glossary.md#issue)或受限记录填写规则编号、范围、原因、风险、缓解措施、责任人、到期时间和恢复计划。绕过前须经仓库及受影响领域的负责人批准；安全控制需安全负责人参与，生产控制需生产负责人参与。将记录关联到变更。活动故障期间只有预[授权](../glossary.md#authentication-and-authorization)应急流程可以加急；当时记录操作者、操作与理由，最迟下一工作日复审并恢复控制。检查到期例外，用证据关闭。
- 两种语言在同一变更维护，规则编号及强制等级保持一致。理解有歧义时以英文版为准并更正翻译。跨模块变更由规范[维护者](../glossary.md#ownership)和受影响领域的负责人共同审查。
- 工程文档使用[行话](../glossary.md#jargon)、专业术语或缩写时必须解释，本规范仓库的文档也适用。见 [MNT-07](05-maintenance/maintenance-standards.md#解释工程术语)。

C#、TypeScript 与 CSS 使用[统一代码写法与文件组织](02-development/coding-style.md)。

## 专项目录

| 编号 | 规范 | 接入[优先级](../glossary.md#priority) |
| --- | --- | --- |
| 01 | [项目与仓库规范](01-governance/repository-standards.md) | [P0](../glossary.md#priority) |
| 02 | [代码开发规范](02-development/coding-standards.md) | [P0](../glossary.md#priority) |
| 03 | [Git 分支规范](02-development/git-branching.md) | [P0](../glossary.md#priority) |
| 04 | [Git 提交规范](02-development/commit-convention.md) | [P0](../glossary.md#priority) |
| 05 | [代码审查规范](01-governance/review-standards.md) | [P0](../glossary.md#priority) |
| 06 | [需求与任务规范](01-governance/issue-standards.md) | [P0](../glossary.md#priority) |
| 07 | [测试与质量规范](03-quality/testing-standards.md) | [P0](../glossary.md#priority) |
| 08 | [CI/CD、构建与部署规范](04-delivery/cicd-standards.md) | [P0](../glossary.md#priority) |
| 09 | [版本与发布规范](04-delivery/release-standards.md) | [P0](../glossary.md#priority) |
| 10 | [安全开发规范](03-quality/security-standards.md) | [P0](../glossary.md#priority) |
| 11 | [API 与数据规范](02-development/api-data-standards.md) | [P1](../glossary.md#priority) |
| 12 | [文档与维护规范](05-maintenance/maintenance-standards.md) | [P1](../glossary.md#priority) |

[P0](../glossary.md#priority) 是首批基线；[P1](../glossary.md#priority) 可随项目发展分阶段接入。[优先级](../glossary.md#priority)只决定接入顺序；规范接入后，适用的 [MUST](../glossary.md#requirement-levels) 仍须执行。

## 接入顺序

1. **研发协作：** 确定分支模型、强制审查与提交规则，采用[工作项](../glossary.md#issue)与[变更请求](../glossary.md#change-request)模板。选择一项变更验证从[工作项](../glossary.md#issue)到合并的流程。
2. **质量与交付：** 建立 [Lint](../glossary.md#lint)、构建、测试、安全及发布门禁。验证放行与阻断场景，将同一不可变候选[制品](../glossary.md#artifact)完整[晋级](../glossary.md#promotion)一次。
3. **长期治理：** 补充契约兼容、迁移和恢复演练、运维文档、[ADR](../glossary.md#adr)、[故障复盘](../glossary.md#incident-review)和[弃用](../glossary.md#deprecation)跟踪。为剩余缺口指定负责人和期限。

## 模板

复制模板时，按目标位置调整术语链接，或保留术语文字并移除链接标记。

[仓库 README](templates/repository/README-template.md) · [需求](templates/issue/Feature.md) · [缺陷](templates/issue/Bug.md) · [变更请求](templates/change-request/Change.md) · [发布记录](templates/release/Release.md) · [ADR](../glossary.md#adr) [模板](templates/maintenance/ADR.md) · [故障复盘](templates/maintenance/Incident-review.md)
