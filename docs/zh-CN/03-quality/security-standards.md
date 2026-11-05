# 10. 安全开发规范

[规范目录](../README.md) · [English](../../en/03-quality/security-standards.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 代码、依赖、[凭据](../../glossary.md#secret)、[CI](../../glossary.md#ci-cd)、运行时与数据处理。安全负责人制定要求并协调受限故障；服务负责人落实修复。

## 规范

- **SEC-01 MUST（必须）** 密钥不得进入 Git、构建参数／镜像层、[制品](../../glossary.md#artifact)、示例[夹具](../../glossary.md#fixture)、[遥测](../../glossary.md#telemetry)或普通日志。使用批准的密钥管理系统；可用时用短期且限域的[工作负载身份](../../glossary.md#workload-identity)。按环境限制访问，审计读取、轮换和撤销。仅启用变量掩码不能让不可信作业安全使用变量。
- **SEC-02 MUST（必须）** 在信任边界[认证](../../glossary.md#authentication-and-authorization)，在服务端逐项验证受保护操作与对象权限。默认拒绝，坚持[最小权限](../../glossary.md#least-privilege)并验证[租户隔离](../../glossary.md#tenant-isolation)。校验输入大小、类型与语义；使用参数化查询、安全输出编码及适用的服务端请求目标白名单。使用 [TLS](../../glossary.md#tls)，保护浏览器会话免受令牌窃取和请求伪造。
- **SEC-03 MUST（必须）** 对相关变更运行密钥检测、[静态分析](../../glossary.md#static-analysis)和[依赖扫描](../../glossary.md#dependency-scanning)；扫描实际发布的[容器镜像](../../glossary.md#container-image)，并复查仍受支持版本的新披露漏洞。发现暴露[凭据](../../glossary.md#secret)时阻断并立即响应。新增适用的严重／高危问题应阻断，除非已批准并记录缓解措施的例外。结合可达性和影响[分诊](../../glossary.md#triage)，单独记录已判定的误报。
- **SEC-04 MUST（必须）** 使用可信环境、批准的来源构建，审查新增和传递依赖，固定工具链／[基础镜像](../../glossary.md#container-image)输入。可部署[制品](../../glossary.md#artifact)应发布与[制品](../../glossary.md#artifact)身份绑定的 [SBOM](../../glossary.md#sbom) 和[来源证明](../../glossary.md#provenance)；[晋级](../../glossary.md#promotion)前验证要求的签名／来源。可行时容器以非 root 且无额外能力运行，例外须[授权](../../glossary.md#authentication-and-authorization)并记录。
- **SEC-05 MUST（必须）** 对敏感数据分级，最小化收集和保留。按政策加密传输和存储，限制日志和备份访问并审计特权操作。非生产环境使用合成或经批准脱敏的数据。新增信任边界、[鉴权](../../glossary.md#authentication-and-authorization)流程及敏感处理须审查滥用场景。
- **SEC-06 MUST（必须）** 提供安全漏洞报告渠道，在协调前限制披露，跟踪[严重度](../../glossary.md#priority)、责任人及修复期限。自确认起默认：正在被利用或[凭据](../../glossary.md#secret)暴露时立即启动故障响应；严重问题 72 小时内修复，高危问题 14 个自然日内修复。无法按期完成时，须记录并落实缓解措施，在到期前取得安全负责人批准的限时例外。

## 流程：疑似[凭据](../../glossary.md#secret)泄漏

1. 限制报告访问，识别[凭据](../../glossary.md#secret)范围但不复制其值。立即撤销或限制其使用并轮换，然后更新受影响使用方，验证旧[凭据](../../glossary.md#secret)已无法使用。
2. 检查审计记录和滥用迹象，保全证据并判断受影响环境及数据。从代码、[制品](../../glossary.md#artifact)、日志及缓存移除暴露内容；仅在需要时协调历史清理。改写历史不能撤销密钥。
3. 验证新[凭据](../../glossary.md#secret)及服务恢复，补充防复发检查，并按[维护规范](../05-maintenance/maintenance-standards.md)记录事件和后续事项。

**验收证据：** 扫描结果、[SBOM](../../glossary.md#sbom)／[来源证明](../../glossary.md#provenance)引用、受限风险决策、轮换／撤销及审计记录。证据不得含明文密钥或未经[授权](../../glossary.md#authentication-and-authorization)的个人数据。
