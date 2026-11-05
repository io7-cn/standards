# Coding style and file organization

[Code development standards](coding-standards.md) · [简体中文](../../zh-CN/02-development/coding-style.md) · [EditorConfig template](../../../templates/repository/.editorconfig) · [Prettier template](../../../templates/repository/.prettierrc.json)

This is the shared style for C#, [TypeScript](../../glossary.md#ts) and [CSS](../../glossary.md#css). Apply it to new code and the parts of existing files you change. Make unrelated legacy reformatting a separate change.

- **STY-01 MUST** install the shared [EditorConfig](../../glossary.md#editorconfig) settings and run the configured checks. For frontend code, use the shared [Prettier](../../glossary.md#prettier) settings and limit the formatter's check to applicable frontend files. Document a narrower override with the affected files, the rule it replaces and the reason. A deviation from a mandatory rule follows the [exception process](../README.md). Keep settings and written rules aligned.
- **STY-02 MUST** choose the directory structure according to the project's role. Group domain code by business capability and host code by technical responsibility. For other projects, choose the structure that fits the project's role. Use one organizing principle for sibling directories. Add subdirectories where they make related code easier to find. Keep paths required by the build framework. Separate generated code, build outputs and third-party assets. Document how to regenerate checked-in outputs. Keep tests discoverable alongside the code or in the corresponding test tree.

## Text and whitespace

The template applies the general section first and then the matching file-type sections. Each tool enforces the keys it implements. Files ending in `.g.cs` use `generated_code = true` and are maintained by the generator. Review generated changes that affect behavior or data.

| Convention | EditorConfig key and value |
| --- | --- |
| Resolve style from the repository root. Document any narrower override and its scope. | `root = true` |
| Save text as UTF-8 without a byte order mark. | `charset = utf-8` |
| Use LF line endings. | `end_of_line = lf` |
| End text files with a newline. | `insert_final_newline = true` |
| Trim trailing whitespace. Preserve Markdown line breaks with `false` under `[*.md]`. | `trim_trailing_whitespace = true` |
| Indent with spaces. Preserve tabs for legacy `.sln` files. | `indent_style = space` |
| Use four spaces for C# and Razor and two for [Vue](../../glossary.md#vue), TypeScript, JavaScript, CSS, JSON, YAML and project XML. The legacy `.sln` section uses `tab`. | `indent_size = 4` |
| Set the tab display width to match the applicable indent width. | `tab_width = 4` |

Use one blank line between imports, declarations and logical blocks. Wrap long expressions at syntactic boundaries. Avoid padding with spaces to align columns. Review checks grouping and readable wrapping where the formatter has no rule.

The two-space section sets `indent_size = 2` and `tab_width = 2`. The legacy solution section sets `indent_style = tab` and `indent_size = tab`. The Markdown section sets `trim_trailing_whitespace = false`.

## File and directory layout

| Scope | Rule | Example |
| --- | --- | --- |
| Repository | Use lowercase [kebab-case](../../glossary.md#naming-case) for new repository names and standalone documentation filenames. Preserve standard names that tools discover. | `order-service`, `docs/order-lifecycle.md`, `README.md` |
| Source and tests | Use `src/` and `tests/` in new repositories. Keep feature code with its feature and move it into shared code once it has a clear shared responsibility. | `src/Orders.Domain/Orders/`, `tests/Orders.Domain.Tests/Orders/` |
| C# | Match the primary type and filename. Use one top-level type per file by default. Use a purpose suffix for split partial types. | `OrderService.cs`, `OrderEditor.Validation.cs`, `OrderClient.g.cs` |
| C# layers | In a layered service, put Domain, Application, Contract, Infrastructure and Host in their owning projects or equivalent folders. Use the project namespace and meaningful subnamespaces. Preserve a published contract namespace when moving files. | `Orders.Application/Orders/`, `Orders.Contract/Requests/` |
| C# contracts | Put an operation's request and direct response together in `<Operation>Request.cs`. Keep reusable models and enums in `Models/` and the service interface at the contract root. | `Requests/CreateOrderRequest.cs` holds `CreateOrderRequest` and `CreateOrderResponse`. |
| [Blazor](../../glossary.md#blazor) | Place Razor markup, optional code-behind and isolated styles together. Keep public assets in `wwwroot/`. | `OrderSummary.razor`, `OrderSummary.razor.cs`, `OrderSummary.razor.css` |
| [Vue](../../glossary.md#vue) and [TypeScript](../../glossary.md#ts) | Use PascalCase for component filenames and lowercase kebab-case for other modules and feature directories. Use `index.ts` at intentional feature or package entry points. | `src/features/orders/OrderSummary.vue`, `order-client.ts` |
| Tests | In a separate test project, mirror the source project's relative directory structure for tests of individual features. Distinguish unit, integration and end-to-end suites by name or directory. | `src/Orders/Payments/OrderService.cs` → `tests/Orders.Tests/Payments/OrderServiceTests.cs` |

Review or a repository structure check enforces filenames, layout, ownership and dependency direction. EditorConfig selects settings by path.

## C# identifiers

- **STY-03 MUST** use the identifier rules below. Spell out domain words. Use verbs for operations, nouns for types and properties, and affirmative boolean names such as `IsEnabled` or `hasItems`. Use the `Async` suffix where an asynchronous interface allows it. Name tests after the behavior and outcome, as in `CreateOrderRejectsEmptyItems`.

The table shows the exact `dotnet_naming_rule` prefix. Its `.symbols`, `.style` and `.severity` properties bind a `dotnet_naming_symbols` selector to a `dotnet_naming_style`. The template defines applicable kinds and accessibility, required modifiers, prefixes and casing. The template uses the tooling defaults at the diagnostic-ID level for `IDE0005`, `IDE0055` and `IDE1006`. Each custom naming rule includes its required `.severity` field.

| Symbol and convention | EditorConfig rule prefix |
| --- | --- |
| Interface types use an I prefix and PascalCase, as in IOrderStore. | `dotnet_naming_rule.interfaces` |
| Private and private protected constants use PascalCase. This rule resolves overlap with private fields. | `dotnet_naming_rule.private_constants` |
| Constants use PascalCase, including local constants, as in DefaultPageSize. | `dotnet_naming_rule.constants` |
| Static fields use PascalCase, including private and private protected static fields. | `dotnet_naming_rule.static_fields` and `dotnet_naming_rule.private_static_fields` |
| Private and private protected instance fields use _camelCase. | `dotnet_naming_rule.private_fields` |
| Classes, records, structs, enums and delegates use PascalCase. | `dotnet_naming_rule.types` |
| Properties, events and methods use PascalCase. | `dotnet_naming_rule.members` |
| Local variables, parameters and local functions use camelCase, apart from local constants. | `dotnet_naming_rule.locals_and_parameters` |
| Generic type parameters start with T. Use T for a simple single parameter or a descriptive name such as TResult. | `dotnet_naming_rule.type_parameters` |

Use PascalCase for public fields required by existing interfaces. Preserve external names and serialized field names. Review checks semantic names, test names and the `Async` suffix.

## C# formatting and language idioms

- **STY-04 MUST** follow the EditorConfig rules below in handwritten C#. Use file-scoped namespaces for new single-namespace files. A file with multiple namespaces may retain block-scoped namespaces until it is split. Remove unused `using` directives when editing imports.

| Convention | EditorConfig key and value |
| --- | --- |
| Use file-scoped namespaces in new single-namespace files. | `csharp_style_namespace_declarations = file_scoped:warning` |
| Place imports outside the namespace. | `csharp_using_directive_placement = outside_namespace:warning` |
| Sort imports in one alphabetical sequence, including System imports. | `dotnet_sort_system_directives_first = false` |
| Keep a single import group without a blank separator. | `dotnet_separate_import_directive_groups = false` |
| Use braces on control blocks, including single statements. | `csharp_prefer_braces = true:warning` |
| Put opening braces of multiline blocks on the next line. | `csharp_new_line_before_open_brace = all` |
| Put else on its own line after the closing brace. | `csharp_new_line_before_else = true` |
| Put catch on its own line after the closing brace. | `csharp_new_line_before_catch = true` |
| Put finally on its own line after the closing brace. | `csharp_new_line_before_finally = true` |
| Give each member its own line in multiline object initializers. | `csharp_new_line_before_members_in_object_initializers = true` |
| Indent block contents by one level. | `csharp_indent_block_contents = true` |
| Align braces with the block header. | `csharp_indent_braces = false` |
| Indent switch labels within the switch block. | `csharp_indent_switch_labels = true` |
| Indent case contents beneath their labels. | `csharp_indent_case_contents = true` |
| Put a space between a control keyword and its opening parenthesis. | `csharp_space_after_keywords_in_control_flow_statements = true` |
| Put the operand directly after a cast. | `csharp_space_after_cast = false` |
| Keep the insides of expression, cast and control parentheses unpadded. | `csharp_space_between_parentheses = false` |
| Put the opening parenthesis directly after the declared method name. | `csharp_space_between_method_declaration_name_and_open_parenthesis = false` |
| Put the opening parenthesis directly after the called method name. | `csharp_space_between_method_call_name_and_opening_parenthesis = false` |
| Keep the insides of parameter-list parentheses unpadded. | `csharp_space_between_method_declaration_parameter_list_parentheses = false` |
| Keep the insides of argument-list parentheses unpadded. | `csharp_space_between_method_call_parameter_list_parentheses = false` |
| Keep the comma next to the preceding token. | `csharp_space_before_comma = false` |
| Use one space after a comma on the same line. | `csharp_space_after_comma = true` |
| Use spaces on both sides of binary operators. | `csharp_space_around_binary_operators = before_and_after` |
| Use a space before the inheritance colon. | `csharp_space_before_colon_in_inheritance_clause = true` |
| Use a space after the inheritance colon. | `csharp_space_after_colon_in_inheritance_clause = true` |
| Split statements onto separate lines. | `csharp_preserve_single_line_statements = false` |
| Keep compact members such as simple auto-properties on one line when readable. Write control blocks over multiple lines. | `csharp_preserve_single_line_blocks = true` |
| Prefer var for built-in types. | `csharp_style_var_for_built_in_types = true:suggestion` |
| Prefer var when the initializer makes the type apparent. | `csharp_style_var_when_type_is_apparent = true:suggestion` |
| Prefer var in other inferable declarations. Use an explicit type when the declaration needs to specify its target type. | `csharp_style_var_elsewhere = true:suggestion` |
| Use C# keywords for built-in types in declarations. | `dotnet_style_predefined_type_for_locals_parameters_members = true:warning` |
| Use C# keywords for built-in types in member access, as in int.MaxValue. | `dotnet_style_predefined_type_for_member_access = true:warning` |
| Declare accessibility where applicable, with implicit interface accessibility. | `dotnet_style_require_accessibility_modifiers = for_non_interface_members:warning` |
| Mark fields readonly when assignment is limited to construction or initialization. | `dotnet_style_readonly_field = true:warning` |
| Prefer an expression body (`=>`) when the method fits on one line. Use a block body for longer methods. | `csharp_style_expression_bodied_methods = when_on_single_line:suggestion` |
| Put each member of a multiline anonymous type on its own line. | `csharp_new_line_before_members_in_anonymous_types = true` |
| Put each query expression clause on its own line. | `csharp_new_line_between_query_expression_clauses = true` |
| Indent case contents when they are enclosed in a block. | `csharp_indent_case_contents_when_block = true` |
| Use an unpadded empty parameter list. | `csharp_space_between_method_declaration_empty_parameter_list_parentheses = false` |
| Use an unpadded empty argument list. | `csharp_space_between_method_call_empty_parameter_list_parentheses = false` |
| Keep opening square brackets adjacent to the preceding token. | `csharp_space_before_open_square_brackets = false` |
| Keep the insides of square brackets unpadded. | `csharp_space_between_square_brackets = false` |
| Use unpadded empty square brackets. | `csharp_space_between_empty_square_brackets = false` |
| Do not pad the member-access dot on the left. | `csharp_space_before_dot = false` |
| Do not pad the member-access dot on the right. | `csharp_space_after_dot = false` |
| Keep a for-loop separator adjacent to the preceding token. | `csharp_space_before_semicolon_in_for_statement = false` |
| Put a space after a for-loop separator where another clause follows. | `csharp_space_after_semicolon_in_for_statement = true` |
| Omit redundant this qualification for fields. | `dotnet_style_qualification_for_field = false:warning` |
| Omit redundant this qualification for properties. | `dotnet_style_qualification_for_property = false:warning` |
| Omit redundant this qualification for methods. | `dotnet_style_qualification_for_method = false:warning` |
| Omit redundant this qualification for events. | `dotnet_style_qualification_for_event = false:warning` |
| Use is null for a reference-null test instead of calling ReferenceEquals. | `dotnet_style_prefer_is_null_check_over_reference_equality_method = true:warning` |
| Use a using declaration when disposal at the end of the enclosing scope is intended. | `csharp_prefer_simple_using_statement = true:warning` |

- **STY-05 MUST** order members as constants and fields, constructors, properties and events, public operations, and private helpers. Keep related overloads together and honor framework lifecycle order. Use early guards and handle expected failures at the appropriate boundary. Propagate cancellation, await asynchronous work and dispose owned resources with `using` or `await using`. Document public behavior, exceptions and compatibility when the signature is insufficient. Use compiler diagnostics, analyzers and review for these rules.
- **STY-06 MUST** treat contract source as an external interface. Use property-body records with object initializers for new C# [RPC](../../glossary.md#rpc) contract models. Match request and response stems. Keep command output minimal, for example a newly created [ID](../../glossary.md#id). Map across layers explicitly and preserve consumer-facing names and encodings. Follow the [contract compatibility rules](api-data-standards.md).

## TypeScript and Vue structure

- **STY-07 MUST** use PascalCase for types, classes and components. Use camelCase for functions, values and parameters. Use UPPER_SNAKE_CASE for module-level constants that represent fixed configuration or protocol values. Use `use` plus a descriptive name for [Vue composables](../../glossary.md#vue-composable), for example `useOrderSummary` in `use-order-summary.ts`. Preserve externally defined object keys. Check identifiers with `@typescript-eslint/naming-convention` where applicable, and filenames, composable purpose and feature boundaries in review.
- **STY-08 MUST** keep imports grouped as external packages, repository aliases and relative modules. Put side-effect imports where execution order is explicit. Use `import type` for type-only dependencies and named exports for shared application modules unless a framework requires a default export. Keep view state and rendering in components, and put API access and reusable domain logic in separate modules. Avoid cycles across features. Check type-only imports with `@typescript-eslint/consistent-type-imports` and verify grouping and boundaries in review.
- **STY-09 MUST** enable `strict` in `tsconfig.json` for new projects and retain it where already enabled. Use `const` by default, `let` for reassignment and strict equality for comparisons. Use inferred local types when clear and declare the types of public inputs and outputs. Validate `unknown` at runtime boundaries. Scope and explain any escape from checking. Handle rejected promises and cancellation deliberately. Use the compiler and configured [lint](../../glossary.md#lint) rules such as `no-var`, `prefer-const`, `eqeqeq`, `@typescript-eslint/no-explicit-any` and `@typescript-eslint/no-floating-promises`. Configure typed linting for rules that require type information.

For new [Vue single-file components](../../glossary.md#vue-single-file-component), use `<script setup lang="ts">`, then `<template>`, then `<style scoped>` when local styles are needed. Declare typed component inputs and events. Use the component type checker as part of the TypeScript verification step.

### Formatting by tool

| Convention | Tool and setting |
| --- | --- |
| Two-space indentation and LF in Vue, TypeScript, JavaScript and CSS | EditorConfig `indent_style`, `indent_size`, `tab_width` and `end_of_line`. Keep any Prettier overrides consistent with these values. |
| Single quotes for TypeScript strings. Double quotes for Vue template attributes. | Prettier `singleQuote: true` for the script and normal Vue template formatting for attributes. |
| Statement semicolons and multiline trailing commas where valid | Prettier `semi: true`, `trailingComma: "all"`. |
| Spaces inside object braces and parentheses around single arrow parameters | Prettier `bracketSpacing: true`, `arrowParens: "always"`. |
| Target 100 columns for automatic wrapping | Prettier `printWidth: 100`. It is a wrapping preference. Use review for readability. |

## CSS and UI styles

- **STY-10 MUST** keep component styles local. Use `Component.razor.css` in [Blazor](../../glossary.md#blazor) and `<style scoped>` in the owning [Vue single-file component](../../glossary.md#vue-single-file-component). Use globally scoped CSS for resets, [design tokens](../../glossary.md#design-token), shared layout and deliberate integration rules. Use lowercase kebab-case class names and custom properties, with a feature prefix for global names such as `.orders-summary` and `--orders-gap`.
- **STY-11 MUST** use shallow selectors and shared tokens for recurring colors, spacing and type. Keep related declarations together in layout, box, typography, visual and interaction order. Put component state rules after base rules and put responsive overrides alongside the styles they change. Prefer theme extension points over specificity escalation. Review any necessary `!important` with its reason. Check keyboard focus, narrow layouts, supported themes and reduced-motion behavior when applicable.

| CSS requirement | Enforcement |
| --- | --- |
| One declaration per line, a space before an opening brace and after a property colon, and a semicolon after each declaration | Prettier formats declaration layout and spacing. EditorConfig sets indentation, line endings, final newline and trailing whitespace. |
| Lowercase kebab-case class names and custom properties | [Stylelint](../../glossary.md#stylelint) `selector-class-pattern` and `custom-property-pattern` where configured, plus review for feature prefixes. |
| Scope, selector intent, declaration order and accessibility | Review and frontend verification. Stylelint `declaration-no-important` can flag overrides and preserve approved exceptions. |

## Verification

Run the project checks and keep the evidence with the change. For C#, run `dotnet format --verify-no-changes --no-restore` on the chosen solution or project after restore. Check formatting and code style with the configured .NET tooling. Verify formatting against the same configuration used by contributors. Check the changed behavior in unit or integration tests and exercise visible UI changes in context. Use the baseline verification order in the [coding standards](coding-standards.md).

[EditorConfig specification](https://spec.editorconfig.org/) · [C# formatting options](https://learn.microsoft.com/dotnet/fundamentals/code-analysis/style-rules/csharp-formatting-options) · [.NET naming rules](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/naming-rules) · [Prettier options](https://prettier.io/docs/options)
