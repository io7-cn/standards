# 02. 代码开发规范

[规范目录](../README.md) · [English](../../en/02-development/coding-standards.md) · [P0](../../glossary.md#priority) · [统一代码写法与文件组织](coding-style.md)


**适用范围与责任人：** 手写代码、构建输入和共享运行行为。组件所有者维护技术栈细则；贡献者遵守最近一层的格式配置与架构约定。

## 规范

- **COD-01 MUST（必须）** 使用项目配置的[格式化器](../../glossary.md#formatter)、[Lint](../../glossary.md#lint) 和导入排序。遵守[统一代码写法](coding-style.md)，文本使用 [UTF-8](../../glossary.md#utf-8)、[LF](../../glossary.md#lf) 及末尾换行。纯格式变更单独提交。命名采用业务术语，操作用动词、类型用名词短语，布尔值用肯定式名称；大小写遵循语言惯例。
- **COD-02 MUST（必须）** 在信任边界完成校验与[鉴权](../../glossary.md#authentication-and-authorization)，在负责的领域层或等效模块维护业务不变量。分离契约与存储模型。保持函数职责集中，让副作用清晰可见；当独立行为、重复或复杂度妨碍测试和审查时再提取，避免预设未来需求的抽象。
- **COD-03 MUST（必须）** 显式建模缺失值，校验外部输入，区分预期业务错误与基础设施故障。保留有用的错误上下文，在传输边界映射错误。只为恢复、转换或补充上下文捕获异常；传播取消，避免静默回退。
- **COD-04 MUST（必须）** 使用结构化日志，在可用时带[关联 ID](../../glossary.md#correlation-id)。Debug 用于诊断，Information 用于有意义的状态变化，Warning 用于可恢复异常，Error 用于失败操作。避免传播链上重复记错，脱敏敏感字段并限制指标标签基数。
- **COD-05 MUST（必须）** 为 [I/O](../../glossary.md#io) 设置超时与取消，限制并发。仅对可安全重复的暂态失败重试，限制次数并使用[退避与随机抖动](../../glossary.md#backoff-and-jitter)。通过事务、锁或条件更新保护共享状态；有风险时验证重放与竞态。
- **COD-06 SHOULD（推荐）** 注释解释原因、不变量及外部限制；[公共契约](../../glossary.md#contract)应说明错误行为和资源归属。延期工作用 [TODO](../../glossary.md#todo) 标记，例如 `TODO(#123): 原因` 或等效任务链接追踪，清理失效注释。
- **COD-07 MUST（必须）** 说明新增依赖的理由，审查许可证、维护状态、漏洞和传递依赖影响。固定工具链；可部署项目用入库[锁文件](../../glossary.md#dependency-lock)或等效机制锁定解析结果。同步更新清单与[锁文件](../../glossary.md#dependency-lock)，依赖升级应可独立审查。

## 主要技术栈

| 工作类型 | 参考技术栈 |
| --- | --- |
| .NET 服务与软件库 | 使用 C# 和 .NET，适合托管服务时采用 [ASP.NET Core](../../glossary.md#asp-net-core)。已采用 [NOF](../../glossary.md#nof) 的应用沿用其请求处理流程和生成客户端。采用 [EF Core](../../glossary.md#ef-core) 的关系型数据服务，可参考 EF Core 与 [PostgreSQL](../../glossary.md#postgresql) 的组合。 |
| 内部管理界面 | 默认采用 [Blazor](../../glossary.md#blazor)。通常由后端团队在开发服务时一并完成管理页面，沿用项目选定的[组件库](../../glossary.md#component-library)。 |
| 公开产品界面 | 默认采用 [Vue](../../glossary.md#vue)，搭配 [TypeScript](../../glossary.md#ts) 与 [Vite](../../glossary.md#vite)。 |
| 面向 JavaScript 使用者的软件库 | 以 [TypeScript](../../glossary.md#ts) 为源码，使用 [Node.js](../../glossary.md#node-js) 工具链。公开类型接口的软件包同时发布 JavaScript 和匹配的类型声明。 |
| Web 样式 | 使用 [CSS](../../glossary.md#css)，沿用项目主题与组件样式隔离机制。 |

在项目 [README](../../glossary.md#readme) 中记录选定的技术栈、受支持的版本与验证命令。引入新技术栈或大幅更换框架时，评估交付、兼容性和维护需求，并将重大决策记入 [ADR](../../glossary.md#adr)。

### C# 与 .NET

- **COD-08 MUST（必须）** 声明目标框架及支持的 .NET [SDK](../../glossary.md#sdk)。构建依赖特定 SDK 选择时，用 `global.json` 固定。将共享构建设置放入 `Directory.Build.props`，多项目仓库优先使用 `Directory.Packages.props` 集中管理 [NuGet](../../glossary.md#nuget) 包版本。同仓库内使用项目引用，独立构建的仓库之间通过带版本的软件包依赖。
- **COD-09 MUST（必须）** 遵守仓库的 `.editorconfig`，新项目启用[可空引用类型](../../glossary.md#nullable-reference-types)。类型和公开成员用 [PascalCase](../../glossary.md#naming-case)，局部变量和参数用 [camelCase](../../glossary.md#naming-case)。参考格式使用四空格缩进和带花括号的控制块，适用时使用文件范围命名空间。接口允许时，异步方法使用 `Async` 后缀。对可取消的 [I/O](../../glossary.md#io) 传递 `CancellationToken`，并等待异步操作完成。
- **COD-10 MUST（必须）** 保持依赖边界。采用[分层架构](../../glossary.md#layered-architecture)时，Domain 管理业务规则，Application 编排用例。Domain 独立于传输和持久化，传输模型与领域实体分离。由 Host 或 Infrastructure 承担相应的运行时注册与持久化装配。[UI](../../glossary.md#ui) 通过契约或批准的客户端调用。[NOF](../../glossary.md#nof) 项目复用框架注册的处理器、客户端生成及请求上下文。[EF Core](../../glossary.md#ef-core) 变更按项目的[迁移](../../glossary.md#migration)流程执行，并在服务实际使用的数据库引擎上验证行为。

- **COD-15 MUST（必须）** 明确共享内部协议的维护责任，并将其放在各消费方的实现之外。分离线上传输模型及校验、客户端会话策略、服务端持久化及公开 [SDK](../../glossary.md#sdk) 声明。记录各边界的依赖方，并验证受影响的消费方。
- **COD-16 MUST（必须）** 实现通用传输、序列化或生命周期能力前，先检查项目固定版本的框架是否已提供同类能力。现有能力能保持[契约](../../glossary.md#contract)时须复用。确需专用适配器时，记录框架与需求的差异，并验证适配器保障的行为，例如响应大小限制、取消或认证重试策略。

### TypeScript

- **COD-11 MUST（必须）** 新 [TypeScript](../../glossary.md#ts) 项目在 `tsconfig.json` 开启 `strict`，已开启的项目保留严格检查。将不可信数据视为 `unknown`，通过运行时校验后再使用。使用 `any` 时说明理由并限制其范围。类型和组件使用 [PascalCase](../../glossary.md#naming-case)，值和函数使用 [camelCase](../../glossary.md#naming-case)。使用项目配置的 [Lint](../../glossary.md#lint) 与[格式化器](../../glossary.md#formatter)。声明受支持的 [Node.js](../../glossary.md#node-js) 版本与包管理器，提交其[锁文件](../../glossary.md#dependency-lock)，并在 [CI](../../glossary.md#ci-cd) 中执行锁定安装。
- **COD-12 MUST（必须）** 公开软件包的行为及类型声明须源自同一实现。软件包入口、生成的声明及消费方示例须与编译后的 JavaScript 一致。C# 与 [TypeScript](../../glossary.md#ts) 客户端共享[接口契约](../../glossary.md#contract)时，同步更新受影响的客户端，并针对兼容的服务或宿主验证实际调用及错误行为。

### CSS 与 Web 界面

- **COD-13 MUST（必须）** 将 [CSS](../../glossary.md#css) 作用域限制在负责的组件或功能内。添加覆盖样式前，优先使用已有组件库和主题。[Blazor](../../glossary.md#blazor) 使用对应的 `.razor.css`，[Vue 单文件组件](../../glossary.md#vue-single-file-component)使用 `<style scoped>`。全局样式用于重置、[设计变量](../../glossary.md#design-token)、公共布局和明确的集成样式。全局类名带功能前缀。需要表达运行时数值时可使用内联样式，覆盖组件库样式时使用项目支持的主题或扩展点。
- **COD-14 MUST（必须）** 受影响的界面在支持的视口尺寸下应可用，并支持键盘操作。保留可见的焦点提示及文本对比度，确保内容换行或缩放后仍可读。纯视觉布局变更使用响应式样式，新增动画时尊重减少动态效果的偏好。按需验证弹层、窄屏布局和受支持主题下的实际效果。

### 按技术栈验证

| 技术栈 | 适用的验收证据 |
| --- | --- |
| C# / .NET | 依次执行依赖还原、格式校验、Release 构建、适用的 [EF Core](../../glossary.md#ef-core) 模型检查和测试。步骤失败时先解决再继续。变更涉及真实持久化或宿主行为时，运行对应的[集成测试](../../glossary.md#integration-test)。 |
| [TypeScript](../../glossary.md#ts) | 按声明的[锁文件](../../glossary.md#dependency-lock)安装依赖，执行类型检查、[Lint](../../glossary.md#lint)、受影响的测试和生产构建。[Vue](../../glossary.md#vue) 项目使用 `vue-tsc` 检查组件类型。发布软件包时检查打包后的导出与声明。 |
| [CSS](../../glossary.md#css) | 执行已配置的样式检查和前端构建。在受影响的组件或页面验证视觉变更，并在[变更请求](../../glossary.md#change-request)提供截图或可复现的审查路径。 |

Python 与 Go 组件适用通用编码规范，并使用项目声明的工具。Python 通常运行 Ruff、配置好的测试与类型检查，Go 通常运行 gofmt、go vet 与 go test。

**流程与证据：** 从干净依赖还原开始执行项目检查，检查格式化差异，测试受影响行为，并在[变更请求](../../glossary.md#change-request)附检查结果。按上表顺序执行，并在各仓库记录确切的解决方案、项目和命令。另见[测试](../03-quality/testing-standards.md)、[安全](../03-quality/security-standards.md)及[参考实践](../reference-patterns.md)。
