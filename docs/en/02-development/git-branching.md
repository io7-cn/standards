# 03. Git Branching

[Standards index](../README.md) · [简体中文](../../zh-CN/02-development/git-branching.md) · [P0](../../glossary.md#priority)


**Scope and owner:** Maintainers configure branches; authors maintain [topic branches](../../glossary.md#topic-branch).

## Standards

- **GIT-01 MUST** protect the [default branch](../../glossary.md#branch) and any active release/integration branch. Disallow direct pushes, [force pushes](../../glossary.md#force-push) and deletion through normal roles. Allow merges only by designated roles or a controlled merge service, through a [change request](../../glossary.md#change-request) with required approvals and [CI](../../glossary.md#ci-cd). Document the platform controls and any equivalent enforcement.
- **GIT-02 SHOULD** use a [short-lived topic branch](../../glossary.md#topic-branch) from current `main` and merge back to it. Existing `master`, `develop` or supported release lines may remain under a documented profile with target, [promotion](../../glossary.md#promotion), [backport](../../glossary.md#backport-and-forward-port) and protection rules. A deployment environment alone does not require a branch.
- **GIT-03 MUST** use lowercase [kebab-case](../../glossary.md#naming-case) topic names, e.g. `feature/123-login`, `fix/124-timeout`, `hotfix/125-auth`. Also allow `refactor/`, `docs/`, `test/`, `chore/` and `spike/`; an existing documented alias such as `feat/` is valid. Include the issue identifier when practical and keep one purpose per branch.
- **GIT-04 SHOULD** [squash](../../glossary.md#squash) a normal [change request](../../glossary.md#change-request) into one [Conventional Commit](../../glossary.md#conventional-commits). Use a [merge commit](../../glossary.md#merge-commit) when preserving independently useful commits, for integration branches or for [backports](../../glossary.md#backport-and-forward-port) that need ancestry; record the strategy in the repository profile. [Rebase](../../glossary.md#rebase) a private branch when useful, never rewrite shared history without coordination. On an agreed [topic branch](../../glossary.md#topic-branch) use [`--force-with-lease`](../../glossary.md#force-push) after verifying the remote tip; [protected branches](../../glossary.md#protected-branch) are never rewritten as routine work.
- **GIT-05 MUST** resolve conflicts on the source branch with awareness of both sides, rerun affected checks and obtain renewed review after material changes. Remove merged [topic branches](../../glossary.md#topic-branch) after checking for dependent [change requests](../../glossary.md#change-request). Close abandoned work with a reason; prune obsolete branches without losing unmerged work.

## Procedure: normal change and emergency fix

1. Link an issue, refresh the target from the authorized remote, branch from it and open a draft [change request](../../glossary.md#change-request) when early feedback is useful.
2. Before merging, update against the target if required, resolve conflicts and verify the current commit or merge result. Use [review rules](../01-governance/review-standards.md) and delete the merged source branch.
3. For an active incident, branch from the affected supported release if it differs from the [trunk](../../glossary.md#branch), use an expedited [change request](../../glossary.md#change-request), follow the [release procedure](../04-delivery/release-standards.md), and [forward-port/backport](../../glossary.md#backport-and-forward-port) to other affected lines with separate tracked [change requests](../../glossary.md#change-request). Use the logged [exception procedure](../README.md) for any emergency deviation.

**Evidence:** Branch rules, linked [change request](../../glossary.md#change-request), [pipeline](../../glossary.md#pipeline) for the merge candidate, reviewed conflict resolution and linked [backports](../../glossary.md#backport-and-forward-port).
