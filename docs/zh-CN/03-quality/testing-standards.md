# 07. 测试与质量规范

[规范目录](../README.md) · [English](../../en/03-quality/testing-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 代码、基础设施及发布验证。组件所有者按风险定义检查，贡献者补足测试，[维护者](../../glossary.md#ownership)强制执行[必过作业](../../glossary.md#gate)。

## 规范

- **TST-01 MUST（必须）** 在最低且可靠的层级验证变更行为，包括有意义的负面和边界场景。缺陷修复补充[回归测试](../../glossary.md#regression-test)；无法稳定自动复现时记录可重复的人工检查及原因。即使总[覆盖率](../../glossary.md#coverage)很高，仍须覆盖关键路径和故障模式。
- **TST-02 MUST（必须）** 隔离自动化测试，使其可重复，按需控制时钟、[夹具](../../glossary.md#fixture)和种子数据。不得依赖生产[凭据](../../glossary.md#secret)、数据或服务。行为依赖真实提供方时，用[集成测试](../../glossary.md#integration-test)验证；仅用 [Mock](../../glossary.md#mock) 或内存库不能证明真实数据库、身份或网络行为。
- **TST-03 MUST（必须）** 适用的格式／[Lint](../../glossary.md#lint)／[静态分析](../../glossary.md#static-analysis)、构建、测试和[安全门禁](security-standards.md)必须阻止失败的变更合并；失败也要发布报告。显式区分可选检查；[必过作业](../../glossary.md#gate)不得被跳过或允许失败。核对路径过滤是否覆盖共享依赖及最新候选。
- **TST-04 SHOULD（推荐）** 跟踪整体[覆盖率](../../glossary.md#coverage)、变更[覆盖率](../../glossary.md#coverage)趋势和关键路径覆盖。设门槛时记录范围、测量方式和合理例外。新增或变动的安全、可靠性警告按缺陷处理；无关历史问题单列基线和清理计划。
- **TST-05 MUST（必须）** 为[不稳定测试](../../glossary.md#flaky-test)记录责任人、复现证据及修复期限。[临时隔离](../../glossary.md#flaky-test)需批准；若影响关键覆盖，须提供替代验证。盲目重试不能作为通过证据。
- **TST-06 MUST（必须）** 说明跑了什么、针对哪一构建和环境、还有什么未验证。纯文档变更执行适用的链接、[Lint](../../glossary.md#lint) 和示例验证；改动命令或行为时运行相应的可执行检查。
- **TST-07 MUST（必须）** 将单个组件的测试放在该组件内。涉及多个组件的行为使用独立的[集成测试](../../glossary.md#integration-test)套件，明确依赖参与的组件或其构建[制品](../../glossary.md#artifact)。验证组件自己的测试可在仅有其声明依赖的环境中运行，无需检出无关组件的源码。

| 层级 | 最低使用场景 |
| --- | --- |
| 单元 | 领域不变量、转换、校验及错误分支 |
| 集成 | 使用有代表性的依赖验证真实持久化／迁移、[鉴权](../../glossary.md#authentication-and-authorization)适配器和外部 [I/O](../../glossary.md#io) |
| 契约 | 检查 [API Schema](../../glossary.md#schema)／[Proto](../../glossary.md#protobuf) 和消费方兼容性；变更时验证序列化器和生成客户端 |
| [端到端](../../glossary.md#e2e)／[冒烟](../../glossary.md#smoke-test) | 针对实际部署[制品](../../glossary.md#artifact)验证关键用户流程与部署后就绪情况 |
| 性能／韧性 | 影响延迟、并发、容量或故障处理的高风险变更；按记录的负载和预算比较 |

## 流程：[质量门禁](../../glossary.md#gate)

选择受影响的测试套件，再执行项目验证入口。对 .NET，按[统一验证顺序](../02-development/coding-standards.md#按技术栈验证)执行项目记录的命令。契约、迁移或性能变更触发时增加对应门禁。发布前核对证据对应的确切[制品](../../glossary.md#artifact)／提交，并在部署后验证关键路径。

**验收证据：** [必过作业](../../glossary.md#gate)结果、测试报告、范围及风险、人工证据或例外链接，以及适用的性能对比。
