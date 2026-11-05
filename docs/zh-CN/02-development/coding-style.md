# 代码写法与文件组织

[代码开发规范](coding-standards.md) · [English](../../en/02-development/coding-style.md) · [EditorConfig 模板](../../../templates/repository/.editorconfig) · [Prettier 模板](../../../templates/repository/.prettierrc.json)

这是 C#、[TypeScript](../../glossary.md#ts) 和 [CSS](../../glossary.md#css) 的统一写法。新代码及既有文件中本次修改的部分均按此执行。无关旧代码的格式归一化单独提交审查。

- **STY-01 MUST（必须）** 接入统一 [EditorConfig](../../glossary.md#editorconfig) 并执行项目配置的检查。前端代码使用统一的 [Prettier](../../glossary.md#prettier) 设置，格式校验范围限定在适用的前端文件。局部覆盖时记录文件范围、替代规则和原因。偏离强制要求须遵循[例外流程](../README.md)。配置与书面规则同步维护。
- **STY-02 MUST（必须）** 根据项目职责选择源码目录结构。领域层按业务能力组织，宿主层按技术职责组织。其他项目按自身职责选择。同级目录采用一致的划分原则。相关代码需要进一步区分时，增设子目录。保留构建框架要求的路径。分开放置生成代码、构建产物及第三方资源。对入库的生成文件记录再生成方法。测试放在被测代码旁或可对应查找的测试目录。

## 文本与空白

模板先应用通用段，再应用匹配文件类型的配置段。各工具只执行自己支持的配置键。后缀为 `.g.cs` 的文件用 `generated_code = true` 标记为生成代码，由生成工具维护。涉及行为或数据变化的生成结果仍须审查。

| 写法 | EditorConfig 键与取值 |
| --- | --- |
| 以仓库根目录为配置查找边界。更细粒度的覆盖须记录适用范围。 | `root = true` |
| 文本使用不带字节顺序标记的 UTF-8。 | `charset = utf-8` |
| 使用 LF 换行。 | `end_of_line = lf` |
| 文本文件以换行结束。 | `insert_final_newline = true` |
| 去除行尾空白。Markdown 硬换行通过 `[*.md]` 下的 `false` 保留。 | `trim_trailing_whitespace = true` |
| 用空格缩进。旧式 `.sln` 文件保留制表符。 | `indent_style = space` |
| C# 与 Razor 用四空格。[Vue](../../glossary.md#vue)、TypeScript、JavaScript、CSS、JSON、YAML 和项目 XML 用两空格。旧式 `.sln` 段设置 `tab`。 | `indent_size = 4` |
| 制表符显示宽度与适用缩进宽度一致。 | `tab_width = 4` |

导入、声明和逻辑块之间留一个空行。长表达式在语法边界处换行。避免用连续空格把代码排成列。格式化工具无法覆盖的分组和可读性由审查确认。

两空格文件段设置 `indent_size = 2` 和 `tab_width = 2`。旧式解决方案段设置 `indent_style = tab` 和 `indent_size = tab`。Markdown 段设置 `trim_trailing_whitespace = false`。

## 文件与目录组织

| 范围 | 规则 | 示例 |
| --- | --- | --- |
| 仓库 | 新仓库与独立文档文件名使用[全小写连字符命名](../../glossary.md#naming-case)。工具按约定识别的文件保留标准名称。 | `order-service`、`docs/order-lifecycle.md`、`README.md` |
| 源码与测试 | 新仓库使用 `src/` 与 `tests/`。功能代码放在所属功能下，具有明确共用职责后再提取。 | `src/Orders.Domain/Orders/`、`tests/Orders.Domain.Tests/Orders/` |
| C# | 文件名与主类型同名，默认一个文件一个顶级类型。拆分 partial 类型时加表示用途的后缀。 | `OrderService.cs`、`OrderEditor.Validation.cs`、`OrderClient.g.cs` |
| C# 分层 | 分层服务的 Domain、Application、Contract、Infrastructure 和 Host 放在所属项目或等效目录。使用项目命名空间及有实际意义的子命名空间。移动文件时保留已发布的契约命名空间。 | `Orders.Application/Orders/`、`Orders.Contract/Requests/` |
| C# 契约 | 操作的请求与直接响应同放在 `<Operation>Request.cs`。共用模型与枚举放在 `Models/`，服务接口放在契约项目根目录。 | `Requests/CreateOrderRequest.cs` 包含 `CreateOrderRequest` 与 `CreateOrderResponse`。 |
| [Blazor](../../glossary.md#blazor) | Razor 标记、可选后台代码和隔离样式就近放置。公开静态资源放入 `wwwroot/`。 | `OrderSummary.razor`、`OrderSummary.razor.cs`、`OrderSummary.razor.css` |
| [Vue](../../glossary.md#vue) 与 [TypeScript](../../glossary.md#ts) | 组件文件用大驼峰。其他模块及功能目录用全小写连字符命名。仅在明确的功能或包入口使用 `index.ts`。 | `src/features/orders/OrderSummary.vue`、`order-client.ts` |
| 测试 | 在独立测试项目中，单个功能的测试沿用被测源码在源项目内的相对目录结构。用名称或目录区分单元、集成与端到端测试。 | `src/Orders/Payments/OrderService.cs` → `tests/Orders.Tests/Payments/OrderServiceTests.cs` |

文件名、布局、归属和依赖方向由审查或项目结构检查执行。EditorConfig 根据文件路径选择设置。

## C# 标识符

- **STY-03 MUST（必须）** 遵循下表的命名规则。使用完整领域术语。操作用动词，类型和属性用名词，布尔值优先用肯定式名称，如 `IsEnabled` 或 `hasItems`。异步接口允许时使用 `Async` 后缀。测试名说明行为及预期结果，例如 `CreateOrderRejectsEmptyItems`。

下表给出准确的 `dotnet_naming_rule` 前缀。其 `.symbols`、`.style` 和 `.severity` 属性关联 `dotnet_naming_symbols` 选择器与 `dotnet_naming_style`。模板定义适用类型、可见性、修饰符、前缀及大小写。`IDE0005`、`IDE0055` 和 `IDE1006` 在诊断编号层级沿用工具默认级别。每条自定义命名规则保留其必需的 `.severity` 字段。

| 命名对象及写法 | EditorConfig 规则前缀 |
| --- | --- |
| 接口类型用 I 前缀和大驼峰，如 IOrderStore。 | `dotnet_naming_rule.interfaces` |
| private 和 private protected 常量用大驼峰。这条规则处理与私有字段规则的重叠。 | `dotnet_naming_rule.private_constants` |
| 字段和局部常量均用大驼峰，如 DefaultPageSize。 | `dotnet_naming_rule.constants` |
| 静态字段使用 PascalCase，包括 private 和 private protected 静态字段。 | `dotnet_naming_rule.static_fields`、`dotnet_naming_rule.private_static_fields` |
| private 和 private protected 实例字段用下划线加小驼峰。 | `dotnet_naming_rule.private_fields` |
| 类、记录、结构体、枚举、委托用大驼峰。 | `dotnet_naming_rule.types` |
| 属性、事件、方法用大驼峰。 | `dotnet_naming_rule.members` |
| 局部变量、参数和局部函数用小驼峰，局部常量遵循常量规则。 | `dotnet_naming_rule.locals_and_parameters` |
| 泛型类型参数以 T 开头。含义简单的单参数用 T，其他情况用 TResult 等描述性名称。 | `dotnet_naming_rule.type_parameters` |

现有接口要求使用公开字段时，字段名用大驼峰。保持外部规定名称及序列化字段名稳定。名称语义、测试命名和 `Async` 后缀由审查核对。

## C# 格式与语言写法

- **STY-04 MUST（必须）** 手写 C# 遵循下表映射规则。新建单命名空间文件用文件范围命名空间。含多个命名空间的文件可保留块范围写法，直至拆分。修改导入时删除未使用的 `using`。

| 写法 | EditorConfig 键与取值 |
| --- | --- |
| 新建单命名空间文件采用文件范围命名空间。 | `csharp_style_namespace_declarations = file_scoped:warning` |
| 将 using 指令放在命名空间外。 | `csharp_using_directive_placement = outside_namespace:warning` |
| 所有 using 指令统一按字母顺序排列，包括 System。 | `dotnet_sort_system_directives_first = false` |
| using 指令放在同一组，组内不插空行。 | `dotnet_separate_import_directive_groups = false` |
| 控制流块一律加花括号，包括单语句。 | `csharp_prefer_braces = true:warning` |
| 多行块的左花括号另起一行。 | `csharp_new_line_before_open_brace = all` |
| 右花括号之后另起一行写 else。 | `csharp_new_line_before_else = true` |
| 右花括号之后另起一行写 catch。 | `csharp_new_line_before_catch = true` |
| 右花括号之后另起一行写 finally。 | `csharp_new_line_before_finally = true` |
| 多行对象初始化器中每个成员单独一行。 | `csharp_new_line_before_members_in_object_initializers = true` |
| 块内容缩进一级。 | `csharp_indent_block_contents = true` |
| 花括号与块头对齐。 | `csharp_indent_braces = false` |
| switch 标签在 switch 块内缩进。 | `csharp_indent_switch_labels = true` |
| case 内容比标签多缩进一级。 | `csharp_indent_case_contents = true` |
| 控制关键字与左圆括号之间加空格。 | `csharp_space_after_keywords_in_control_flow_statements = true` |
| 类型转换括号与操作数之间不加空格。 | `csharp_space_after_cast = false` |
| 表达式、类型转换和控制流圆括号内侧不留空格。 | `csharp_space_between_parentheses = false` |
| 方法声明名称紧跟左圆括号。 | `csharp_space_between_method_declaration_name_and_open_parenthesis = false` |
| 方法调用名称紧跟左圆括号。 | `csharp_space_between_method_call_name_and_opening_parenthesis = false` |
| 形参列表的圆括号内侧不留空格。 | `csharp_space_between_method_declaration_parameter_list_parentheses = false` |
| 实参列表的圆括号内侧不留空格。 | `csharp_space_between_method_call_parameter_list_parentheses = false` |
| 逗号前不加空格。 | `csharp_space_before_comma = false` |
| 同一行的逗号后加一个空格。 | `csharp_space_after_comma = true` |
| 二元运算符两侧加空格。 | `csharp_space_around_binary_operators = before_and_after` |
| 继承声明的冒号前加空格。 | `csharp_space_before_colon_in_inheritance_clause = true` |
| 继承声明的冒号后加空格。 | `csharp_space_after_colon_in_inheritance_clause = true` |
| 不同语句分行书写。 | `csharp_preserve_single_line_statements = false` |
| 简单自动属性等紧凑成员可在清晰时保留单行。控制块使用多行。 | `csharp_preserve_single_line_blocks = true` |
| 内置类型优先使用 var。 | `csharp_style_var_for_built_in_types = true:suggestion` |
| 初始化表达式能直接看出类型时优先使用 var。 | `csharp_style_var_when_type_is_apparent = true:suggestion` |
| 其他可推断的声明也优先使用 var。需要由声明指定目标类型时，使用显式类型。 | `csharp_style_var_elsewhere = true:suggestion` |
| 声明内置类型时使用 C# 类型关键字。 | `dotnet_style_predefined_type_for_locals_parameters_members = true:warning` |
| 访问内置类型成员时使用 C# 类型关键字，如 int.MaxValue。 | `dotnet_style_predefined_type_for_member_access = true:warning` |
| 可声明可见性时显式声明，接口成员沿用隐式可见性。 | `dotnet_style_require_accessibility_modifiers = for_non_interface_members:warning` |
| 字段只在构造或初始化时赋值的，标记为 readonly。 | `dotnet_style_readonly_field = true:warning` |
| 能写成一行的方法优先用表达式体（`=>`）。需要多行时使用块体。 | `csharp_style_expression_bodied_methods = when_on_single_line:suggestion` |
| 多行匿名类型的每个成员另起一行。 | `csharp_new_line_before_members_in_anonymous_types = true` |
| 查询表达式的每个子句另起一行。 | `csharp_new_line_between_query_expression_clauses = true` |
| case 内容用块包裹时仍按规则缩进。 | `csharp_indent_case_contents_when_block = true` |
| 空形参列表的括号内不留空格。 | `csharp_space_between_method_declaration_empty_parameter_list_parentheses = false` |
| 空实参列表的括号内不留空格。 | `csharp_space_between_method_call_empty_parameter_list_parentheses = false` |
| 左方括号紧跟前面的标记。 | `csharp_space_before_open_square_brackets = false` |
| 方括号内侧不留空格。 | `csharp_space_between_square_brackets = false` |
| 空方括号内不留空格。 | `csharp_space_between_empty_square_brackets = false` |
| 成员访问点号前不留空格。 | `csharp_space_before_dot = false` |
| 成员访问点号后不留空格。 | `csharp_space_after_dot = false` |
| for 循环分隔分号前不留空格。 | `csharp_space_before_semicolon_in_for_statement = false` |
| for 循环分号后有子句时留一个空格。 | `csharp_space_after_semicolon_in_for_statement = true` |
| 字段访问省略多余的 this。 | `dotnet_style_qualification_for_field = false:warning` |
| 属性访问省略多余的 this。 | `dotnet_style_qualification_for_property = false:warning` |
| 方法调用省略多余的 this。 | `dotnet_style_qualification_for_method = false:warning` |
| 事件访问省略多余的 this。 | `dotnet_style_qualification_for_event = false:warning` |
| 判定引用为空时使用 is null，替代 ReferenceEquals。 | `dotnet_style_prefer_is_null_check_over_reference_equality_method = true:warning` |
| 确需在当前作用域末尾释放资源时，使用 using 声明。 | `csharp_prefer_simple_using_statement = true:warning` |

- **STY-05 MUST（必须）** 成员按常量与字段、构造器、属性与事件、公开操作、私有辅助方法排列。相关重载就近放置，框架生命周期方法遵循既定顺序。用提前返回处理前置条件，在合适边界处理预期失败。传播取消，等待异步操作，并用 `using` 或 `await using` 释放所拥有的资源。方法签名不足以说明时，记录公开行为、异常及兼容承诺。通过编译器诊断、分析器及审查核对。
- **STY-06 MUST（必须）** 将契约源码视为对外接口。新 C# [RPC](../../glossary.md#rpc) 契约模型使用属性体记录，由对象初始化器赋值。请求和响应沿用同一操作名称。写入操作只返回调用方需要的最少数据，例如新建资源的 [ID](../../glossary.md#id)。显式做跨层映射，保留消费方使用的名称和编码。遵循[契约兼容规范](api-data-standards.md)。

## TypeScript 与 Vue 组织

- **STY-07 MUST（必须）** 类型、类和组件用大驼峰。函数、值及参数用小驼峰。表示固定配置或协议值的模块级常量使用全大写下划线命名。[Vue 组合式函数](../../glossary.md#vue-composable)使用 `use` 加描述性名称，例如 `use-order-summary.ts` 中的 `useOrderSummary`。保留外部定义的对象键。适用时用 `@typescript-eslint/naming-convention` 检查标识符，文件名、组合式函数的用途及功能边界由审查核对。
- **STY-08 MUST（必须）** 导入按外部包、仓库别名和相对模块分组。会执行副作用的导入要明确其执行顺序。纯类型依赖使用 `import type`。共用应用模块使用具名导出，框架要求默认导出时按其约定。组件负责视图状态及渲染，API 访问和可复用业务逻辑放在独立模块。避免功能之间循环依赖。用 `@typescript-eslint/consistent-type-imports` 检查纯类型导入，分组和依赖边界由审查核对。
- **STY-09 MUST（必须）** 新项目在 `tsconfig.json` 启用 `strict`，已启用的项目保留该设置。默认使用 `const`，需要重新赋值时使用 `let`，比较使用严格相等。局部类型清楚时用推断，公开输入和输出声明类型。在运行时边界校验 `unknown`。需要跳过类型检查时说明原因并限制范围。明确处理 Promise 拒绝及取消。使用编译器和已配置的 [Lint](../../glossary.md#lint) 规则，例如 `no-var`、`prefer-const`、`eqeqeq`、`@typescript-eslint/no-explicit-any` 与 `@typescript-eslint/no-floating-promises`。需要类型信息的规则须启用带类型检查的 Lint 配置。

新建 [Vue 单文件组件](../../glossary.md#vue-single-file-component)依次放置 `<script setup lang="ts">`、`<template>` 和按需添加的 `<style scoped>`。为组件输入及事件声明类型，并将组件类型检查纳入 TypeScript 验证流程。

### 格式与工具映射

| 写法 | 工具及设置 |
| --- | --- |
| Vue、TypeScript、JavaScript 与 CSS 使用两空格缩进和 LF | EditorConfig 的 `indent_style`、`indent_size`、`tab_width` 及 `end_of_line`。Prettier 如有覆盖，保持取值一致。 |
| TypeScript 字符串用单引号。Vue 模板属性用双引号。 | 脚本由 Prettier 的 `singleQuote: true` 控制，属性使用 Vue 模板的常规格式。 |
| 语句使用分号，多行结构在语法允许时保留末尾逗号 | Prettier 的 `semi: true` 与 `trailingComma: "all"`。 |
| 对象花括号内有空格，单参数箭头函数保留圆括号 | Prettier 的 `bracketSpacing: true` 与 `arrowParens: "always"`。 |
| 以 100 列为自动换行目标 | Prettier 的 `printWidth: 100`。这是排版目标，可读性由审查确认。 |

## CSS 与界面样式

- **STY-10 MUST（必须）** 组件样式就近隔离。[Blazor](../../glossary.md#blazor) 使用 `Component.razor.css`，[Vue 单文件组件](../../glossary.md#vue-single-file-component)在所属组件内使用 `<style scoped>`。全局样式用于重置、[设计变量](../../glossary.md#design-token)、共享布局及明确的集成规则。类名和自定义属性使用全小写连字符命名，全局名称带功能前缀，例如 `.orders-summary` 与 `--orders-gap`。
- **STY-11 MUST（必须）** 使用层级浅的选择器，并用共用设计变量表达重复的颜色、间距与字号。相关声明按布局、盒模型、排版、视觉和交互顺序组织。组件状态规则放在基础规则之后，响应式覆盖靠近被修改的规则。优先使用主题扩展点。确需 `!important` 时由审查核对原因。适用时检查键盘焦点、窄屏布局、受支持主题及减少动态效果的行为。

| CSS 要求 | 执行方式 |
| --- | --- |
| 每行一条声明，左花括号前及属性冒号后加空格，每条声明以分号结尾 | Prettier 处理声明布局及空格。缩进、换行、文件末尾换行及行尾空白使用 EditorConfig。 |
| 类名和自定义属性使用全小写连字符命名 | 配置 [Stylelint](../../glossary.md#stylelint) 时使用 `selector-class-pattern` 与 `custom-property-pattern`。功能前缀由审查核对。 |
| 作用域、选择器意图、声明顺序及可访问性 | 审查及前端验证。Stylelint 的 `declaration-no-important` 可提示覆盖，并保留已批准的例外。 |

## 验证

执行项目检查并随变更记录证据。C# 完成还原后，对选定解决方案或项目运行 `dotnet format --verify-no-changes --no-restore`。用已配置的 .NET 工具检查格式和代码写法。格式检查使用与贡献者一致的配置。用单元或集成测试验证受影响行为，并在实际使用场景验证可见的界面变更。验证顺序见[代码开发规范](coding-standards.md)。

[EditorConfig 规范](https://spec.editorconfig.org/) · [C# 格式选项](https://learn.microsoft.com/dotnet/fundamentals/code-analysis/style-rules/csharp-formatting-options) · [.NET 命名规则](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/naming-rules) · [Prettier 选项](https://prettier.io/docs/options)
