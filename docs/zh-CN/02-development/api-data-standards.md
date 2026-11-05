# 11. [API](../../glossary.md#api) 与数据规范

[规范目录](../README.md) · [English](../../en/02-development/api-data-standards.md) · [P1](../../glossary.md#priority)


**适用范围与责任人：** [REST](../../glossary.md#rest)、[gRPC](../../glossary.md#grpc) 及其他 [RPC](../../glossary.md#rpc) 契约、数据库和[数据迁移](../../glossary.md#migration)。契约所有者协调消费方，数据所有者批准迁移和恢复方案。

## 规范

- **API-01 MUST（必须）** 定义契约真源：[REST](../../glossary.md#rest) 用 [OpenAPI](../../glossary.md#openapi)，[gRPC](../../glossary.md#grpc) 用 [Protobuf](../../glossary.md#protobuf)，其他 [RPC](../../glossary.md#rpc) 用等效 [Schema](../../glossary.md#schema)。与实现、示例同步版本管理，在 [CI](../../glossary.md#ci-cd) 验证客户端生成和兼容性。[REST](../../glossary.md#rest) 优先用资源名词、一致命名和正确 [HTTP](../../glossary.md#http) 语义（如 `GET /v1/orders/{orderId}`）；记录过滤条件、允许排序字段和带稳定排序的[有界分页](../../glossary.md#pagination)。[Protobuf](../../glossary.md#protobuf) 保留已删除字段的编号和名称。
- **API-02 MUST（必须）** 记录校验、[鉴权](../../glossary.md#authentication-and-authorization)、[限流](../../glossary.md#rate-limit)、超时和稳定的机器可读错误。[REST](../../glossary.md#rest) 使用 [RFC 9457 Problem Details](../../glossary.md#rfc) 或已记录的既有错误结构。请求无效用 400，未[认证](../../glossary.md#authentication-and-authorization)或[认证](../../glossary.md#authentication-and-authorization)无效用 401，无权限用 403，资源不存在或有意隐藏用 404，状态冲突用 409，[限流](../../glossary.md#rate-limit)用 429，服务端故障用 5xx。[gRPC](../../glossary.md#grpc) 使用标准状态码和安全错误详情。不得暴露堆栈、密钥或[跨租户](../../glossary.md#tenant-isolation)数据。
- **API-03 MUST（必须）** 兼容性增量应保留对现有受支持客户端的支持。删除、改变语义或默认值、新增必填输入、改变不兼容类型均视为[破坏性变更](../../glossary.md#breaking-change)；通过版本或分阶段迁移处理，通知所有者并走[弃用流程](../05-maintenance/maintenance-standards.md)。协调受影响的 [Schema](../../glossary.md#schema)／包、服务、[UI](../../glossary.md#ui)、[CLI](../../glossary.md#cli)、[SDK](../../glossary.md#sdk)、测试和文档；验证各受影响客户端实际使用的契约版本。
- **API-04 MUST（必须）** 重复副作用有风险的可重试写入须去重。定义[幂等键](../../glossary.md#idempotency)的范围、有效期、请求不匹配时的行为及重放结果，原子处理并发重复请求。客户端只在总时间预算内重试符合条件的操作，并遵循重试提示。
- **DAT-01 MUST（必须）** 使用一致的 [Schema](../../glossary.md#schema) 命名（新 [SQL](../../glossary.md#sql) [Schema](../../glossary.md#schema) 默认 [snake_case](../../glossary.md#naming-case)）、[稳定主键](../../glossary.md#primary-key)及显式空值、约束和[事务边界](../../glossary.md#transaction)。按真实查询设计索引并评估写入开销。持久化时间点使用 [UTC](../../glossary.md#utc)；按需保留业务时区并记录公开时间和 [ID](../../glossary.md#id) 编码。
- **DAT-02 MUST（必须）** 将迁移入库审查，在空库及有代表性的旧库升级场景验证，并检查模型／[Schema](../../glossary.md#schema) 漂移。[EF Core](../../glossary.md#ef-core) 使用批准工具和项目启动路径；审查生成 [SQL](../../glossary.md#sql) 及为保护数据而手工调整的部分。增加必填字段、唯一索引或[外键](../../glossary.md#primary-key)前检查历史行。
- **DAT-03 MUST（必须）** 明确迁移顺序、锁／耗时预算、分批、续跑及安全[回滚](../../glossary.md#rollback)／[向前修复](../../glossary.md#roll-forward)。采用[扩展 →](../../glossary.md#expand-and-contract) 部署兼容读写方 → [回填](../../glossary.md#backfill)与校验 → 旧客户端退出后收紧或清理的顺序。保留身份和数据；首个兼容版本不做破坏性清理。
- **DAT-04 MUST（必须）** 定义备份保留期、[RPO](../../glossary.md#rpo)（可接受的数据损失）和 [RTO](../../glossary.md#rto)（[恢复时间目标](../../glossary.md#rto)）；保护备份，在隔离环境演练恢复。恢复后检查 [Schema](../../glossary.md#schema)、数据行／不变量完整性和关键操作。不可逆变更前确认近期可用恢复点及决策人。

## 共享契约与关系型模型

- **API-05 MUST（必须）** 与消费方协调共享契约变更。先确认请求与响应行为，再验证服务提供方的实际映射，按契约包的发布流程授权发布。将消费方更新到经验证的确切包版本，并针对兼容的提供方测试实际调用、权限和错误行为。关联契约、提供方和消费方的变更。软件包发布与服务部署各自保留验证和交付记录。
- **DAT-05 MUST（必须）** 用映射的集合和关系约束表示关系型数据库的一对多关系。子记录随父记录一起管理时使用拥有型集合。子记录有独立身份或生命周期时使用独立实体关系。受影响的 [EF Core](../../glossary.md#ef-core) 服务构建后，针对所配置的上下文检查是否仍有未生成迁移的模型变更。使用项目工具生成缺失的迁移，并结合有代表性的既有数据审查迁移操作。

项目工具支持时，使用配置好的启动项目和上下文执行 `dotnet ef migrations has-pending-model-changes`，检查模型是否仍有变更需要生成迁移。另行执行升级测试，确认迁移保护了既有数据。参见 [EF Core 迁移工具](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/managing)。

## 流程：安全新增必填列

1. 先增加可空列或提供安全默认值。部署能容忍过渡 [Schema](../../glossary.md#schema) 的读取方，以及能够写入新字段的写入方。
2. 按可续跑批次[回填](../../glossary.md#backfill)并保留 [ID](../../glossary.md#id)；核对行数与不变量，测量锁影响，确认没有无效历史行。
3. 用单独经过验证的变更收紧约束；仅在兼容窗口结束后移除旧数据路径。保留可用恢复点，在破坏性操作前演练恢复或[向前修复](../../glossary.md#roll-forward)。

**验收证据：** [Schema](../../glossary.md#schema) 差异、[契约测试](../../glossary.md#contract-test)与消费方矩阵、生成的迁移／[SQL](../../glossary.md#sql)、升级与恢复结果、生产验证及[发布记录](../04-delivery/release-standards.md)。
