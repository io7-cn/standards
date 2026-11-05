# 02. Coding Standards

[Standards index](../README.md) · [简体中文](../../zh-CN/02-development/coding-standards.md) · [P0](../../glossary.md#priority) · [Shared coding style and file organization](coding-style.md)


**Scope and owner:** Handwritten code, build inputs and shared runtime behavior. Component owners maintain stack profiles; contributors follow the nearest [formatter](../../glossary.md#formatter) and architecture rules.

## Standards

- **COD-01 MUST** use the configured [formatter](../../glossary.md#formatter), [linter](../../glossary.md#lint) and import ordering. Apply the [shared coding style](coding-style.md), including [UTF-8](../../glossary.md#utf-8), [LF](../../glossary.md#lf) and a final newline for text. Keep formatting-only churn separate. Use domain terms for names, verbs for operations, noun phrases for types and affirmative names for booleans; use each language's casing conventions.
- **COD-02 MUST** keep validation and [authorization](../../glossary.md#authentication-and-authorization) at trust boundaries and business invariants in their owning domain or equivalent layer. Separate contracts from storage models. Keep routines cohesive and side effects visible; extract when independent behavior, duplication or complexity impedes testing or review. Avoid speculative abstractions.
- **COD-03 MUST** model absence explicitly, validate external input and handle expected domain errors separately from infrastructure failures. Preserve useful error context and map errors at the transport boundary. Catch only to recover, translate or add useful context; propagate cancellation and avoid silent fallbacks.
- **COD-04 MUST** pass structured fields to loggers, with [correlation IDs](../../glossary.md#correlation-id) where available. Use Debug for diagnostics, Information for meaningful transitions, Warning for recoverable anomalies and Error for failed operations. Avoid duplicate logging as errors propagate. Redact sensitive fields and keep metrics labels bounded.
- **COD-05 MUST** bound [I/O](../../glossary.md#io) with timeout/cancellation and limit concurrent work. Retry only transient, safely repeatable operations, with a capped attempt count, [backoff and jitter](../../glossary.md#backoff-and-jitter). Guard shared state with suitable [transactions](../../glossary.md#transaction), locks or conditional updates; test replay and race behavior when it matters.
- **COD-06 SHOULD** document why, invariants and external constraints rather than restating code. Document [public contracts](../../glossary.md#contract), error behavior and ownership of resources. Use a [TODO](../../glossary.md#todo) marker such as `TODO(#123): reason` or an equivalent tracked reference for deferred work; remove stale comments.
- **COD-07 MUST** justify new dependencies and review license, maintenance, vulnerabilities and transitive impact. Pin toolchains and resolve deployable dependencies with checked-in locks or equivalent controls. Update manifests and locks together; keep dependency upgrades independently reviewable.

## Primary technology stack

| Work | Reference stack |
| --- | --- |
| .NET services and libraries | C# and .NET. Use [ASP.NET Core](../../glossary.md#asp-net-core) for hosted services where it fits. Existing [NOF](../../glossary.md#nof) applications use its registered request pipeline and generated clients. [EF Core](../../glossary.md#ef-core) with [PostgreSQL](../../glossary.md#postgresql) is the reference combination for relational services that use EF Core. |
| Internal administration interfaces | Default to [Blazor](../../glossary.md#blazor). The backend team usually implements the administration pages alongside the service. Use the project's selected [component library](../../glossary.md#component-library). |
| Public product interfaces | Default to [Vue](../../glossary.md#vue) with [TypeScript](../../glossary.md#ts) and [Vite](../../glossary.md#vite). |
| JavaScript-facing libraries | [TypeScript](../../glossary.md#ts) source with [Node.js](../../glossary.md#node-js) tooling. Publish JavaScript and matching type declarations when the package exposes a typed public interface. |
| Web styles | [CSS](../../glossary.md#css) with the project's theme and component scoping mechanism. |

Record the selected stack, supported versions and verification commands in the project [README](../../glossary.md#readme). Evaluate a new stack or substantial framework change against the project's delivery, compatibility and maintenance needs. Record significant decisions in an [ADR](../../glossary.md#adr).

### C# and .NET

- **COD-08 MUST** declare the target frameworks and the supported .NET [SDK](../../glossary.md#sdk). Use `global.json` to pin SDK selection when the build depends on it. Keep shared build settings in `Directory.Build.props` and prefer [NuGet](../../glossary.md#nuget) central version management with `Directory.Packages.props` for multi-project repositories. Use project references within the same repository and versioned packages across independently built repositories.
- **COD-09 MUST** follow the repository's `.editorconfig` and enable [nullable reference types](../../glossary.md#nullable-reference-types) for new projects. Use [PascalCase](../../glossary.md#naming-case) for types and public members and [camelCase](../../glossary.md#naming-case) for locals and parameters. The reference formatting uses four spaces, braces for control blocks and file-scoped namespaces where appropriate. Apply the `Async` suffix to asynchronous methods where the interface permits it. Propagate `CancellationToken` through cancellable [I/O](../../glossary.md#io) and await asynchronous work.
- **COD-10 MUST** preserve dependency boundaries. Where the project uses [layered architecture](../../glossary.md#layered-architecture), keep business rules in Domain and use case orchestration in Application. Keep Domain independent of transport and persistence, and keep transport models separate from domain entities. Place runtime registration and persistence wiring in Host or Infrastructure as appropriate. The [UI](../../glossary.md#ui) calls the contract or an approved client. For [NOF](../../glossary.md#nof) projects, reuse the framework's registered handlers, client generation and request context. For [EF Core](../../glossary.md#ef-core) changes, use the project's [migration](../../glossary.md#migration) workflow and verify behavior with the database engine the service uses.

- **COD-15 MUST** give shared internal protocols an explicit owner and place them outside any one consumer's implementation. Keep wire models and validation separate from client session policy, server persistence and public [SDK](../../glossary.md#sdk) declarations. Document which components depend on each boundary and verify the affected consumers.
- **COD-16 MUST** check the project's pinned framework for existing transport, serialization and lifecycle primitives before implementing an equivalent. Reuse a supported primitive when it preserves the [contract](../../glossary.md#contract). Where a requirement needs a dedicated adapter, document the gap and verify the behavior it protects, such as a response-size limit, cancellation or authentication retry policy.

### TypeScript

- **COD-11 MUST** enable `strict` in `tsconfig.json` for new [TypeScript](../../glossary.md#ts) projects and preserve strictness in projects that already use it. Treat untrusted data as `unknown` until it is validated. Justify and narrowly scope any use of `any`. Use [PascalCase](../../glossary.md#naming-case) for types and components and [camelCase](../../glossary.md#naming-case) for values and functions. Use the project's configured [linter](../../glossary.md#lint) and [formatter](../../glossary.md#formatter). Declare the supported [Node.js](../../glossary.md#node-js) version and package manager, commit its [lockfile](../../glossary.md#dependency-lock) for reproducible builds and use a locked install in [CI](../../glossary.md#ci-cd).
- **COD-12 MUST** maintain a single source for a public package's exported behavior and type declarations. Keep package entry points, generated declarations and consumer examples aligned with the compiled JavaScript. When C# and [TypeScript](../../glossary.md#ts) clients share a [contract](../../glossary.md#contract), update affected clients and verify actual calls and errors against the compatible service or host.

### CSS and web interfaces

- **COD-13 MUST** scope [CSS](../../glossary.md#css) to the component or feature that owns it. Use the existing component library and theme before adding overrides. Use the matching `.razor.css` file in [Blazor](../../glossary.md#blazor) and `<style scoped>` in a [Vue single-file component](../../glossary.md#vue-single-file-component). Reserve global styles for resets, [design tokens](../../glossary.md#design-token), shared layout and deliberate integration styles. Namespace global classes by feature. Use inline styles for runtime values when needed, and use the project's supported theme or extension points for library overrides.
- **COD-14 MUST** keep affected interfaces usable at supported viewport sizes and with keyboard navigation. Preserve visible focus, text contrast and readable content when it wraps or is zoomed. Use responsive styles for visual layout changes and respect reduced-motion preferences when adding animation. Verify changed states in context, including overlays, narrow layouts and supported themes where applicable.

### Verification by stack

| Stack | Required evidence where applicable |
| --- | --- |
| C# / .NET | Run restore, format verification, Release build, the applicable [EF Core](../../glossary.md#ef-core) model check, then tests. Stop at a failed step and resolve it before continuing. Run the relevant [integration tests](../../glossary.md#integration-test) for changes that depend on real persistence or hosting behavior. |
| [TypeScript](../../glossary.md#ts) | Install from the declared [lockfile](../../glossary.md#dependency-lock). Run type checking, [lint](../../glossary.md#lint), affected tests and the production build. For [Vue](../../glossary.md#vue), include component type checking with `vue-tsc`. For published packages, check the packaged exports and declarations. |
| [CSS](../../glossary.md#css) | Run configured style checks and the frontend build. Verify visible changes in the affected component or page. Include screenshots or a reproducible review path in the [change request](../../glossary.md#change-request). |

Python and Go components follow the common coding standards and their own declared tools. Typical checks include Ruff and the configured tests and type checks for Python, or gofmt, go vet and go test for Go.

**Procedure and evidence:** Run repository checks from a clean dependency restore, inspect [formatter](../../glossary.md#formatter) changes, test the changed behavior and attach check results to the [change request](../../glossary.md#change-request). Use the verification order above. Document the exact solution, projects and commands in each repository. See [testing](../03-quality/testing-standards.md), [security](../03-quality/security-standards.md) and [reference patterns](../reference-patterns.md).
