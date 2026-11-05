# 04. Commit Convention

[Standards index](../README.md) · [简体中文](../../zh-CN/02-development/commit-convention.md) · [P0](../../glossary.md#priority)


**Scope and owner:** Authors write commit messages; maintainers enforce the convention on protected history.

## Standards

- **COM-01 MUST** use [Conventional Commits 1.0.0](../../glossary.md#conventional-commits) for authored commits entering protected history, including [squash](../../glossary.md#squash) messages. Use a lowercase type, optional lowercase scope and a concise imperative description with no trailing period; aim for a subject within 72 characters. Use English by default; a documented project language may replace it for descriptions. Preserve platform-generated merge messages if the merge strategy uses them.
- **COM-02 MUST** keep each final commit focused on one coherent change and include its necessary tests/docs. Split independent work and large mechanical edits. [Fixup](../../glossary.md#wip), [WIP](../../glossary.md#wip) and temporary debugging commits may exist on [topic branches](../../glossary.md#topic-branch) but must be removed or [squashed](../../glossary.md#squash) before merging.
- **COM-03 MUST** mark a [breaking change](../../glossary.md#breaking-change) with `!` before the colon or a `BREAKING CHANGE:` [footer](../../glossary.md#trailer). Describe compatibility impact and [migration](../../glossary.md#migration) in the body/[footer](../../glossary.md#trailer) and [change request](../../glossary.md#change-request). Separate body and [trailers](../../glossary.md#trailer) with blank lines; use `Refs: #123` or a project-qualified reference for related work. Use automatic closure if the tracker supports it and merging satisfies the issue’s acceptance and delivery conditions; otherwise use a reference.
- **COM-04 MUST** enforce message format at the server or in a required [CI](../../glossary.md#ci-cd) gate. Validate every authored commit retained in protected history; for [squash](../../glossary.md#squash), validate the effective final subject/message by controlling the merge template or merge service. Local hooks are optional feedback. Configure verified signatures for protected release tags and commit signatures where the repository profile requires them. A sign-off [trailer](../../glossary.md#trailer) is not a cryptographic signature.

- **COM-05 MUST** use the contributor-approved commit identity for both author and committer. Configure the repository name and email before creating commits; for a human account, use an address associated with that contributor on the hosting service, including a verified privacy address when chosen by the contributor. Automation uses its explicitly approved identity. Never invent a placeholder identity or substitute another person’s identity. Preserve original authorship when applying someone else’s work. Correct published metadata only with maintainer authorization and update affected pinned references; preserve immutable published release references unless their owner explicitly approves a separate repair.

| Type | Use |
| --- | --- |
| `feat`, `fix` | New behavior or correction |
| `refactor`, `perf`, `style` | Restructuring, performance, or formatting only |
| `docs`, `test` | Documentation or test-only changes |
| `build`, `ci`, `chore` | Tooling/dependencies, [pipelines](../../glossary.md#pipeline), or other upkeep |
| [`revert`](../../glossary.md#revert) | Reverses an earlier change; reference its [SHA](../../glossary.md#sha) and explain why |

## Examples and procedure

```text
feat(auth): support OIDC sign-in

fix(api): return a stable error for expired sessions

feat(api)!: return order identifiers as strings

BREAKING CHANGE: Consumers must parse order IDs as strings.
Refs: #123
```

Stage one change, inspect the staged diff, write the message and run the relevant checks. Before merging, verify the final message and check that the [change request](../../glossary.md#change-request) and issue links resolve. For a [revert](../../glossary.md#revert), preserve the original reference and follow [release rules](../04-delivery/release-standards.md) if already deployed.
