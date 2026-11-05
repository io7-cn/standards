# 05. [Code Review](../../glossary.md#code-review)

[Standards index](../README.md) · [简体中文](../../zh-CN/01-governance/review-standards.md) · [P0](../../glossary.md#priority)


**Scope and owner:** All changes entering [protected branches](../../glossary.md#protected-branch), including docs, migrations, [CI](../../glossary.md#ci-cd), [deployment manifests](../../glossary.md#manifest) and bot changes. Maintainers configure gates; authors and reviewers own the review record.

## Standards

- **REV-01 MUST** open a [change request](../../glossary.md#change-request) with a clear title, linked issue, behavior before/after, scope, risks, verification evidence and [rollout](../../glossary.md#rollout)/[rollback](../../glossary.md#rollback) when relevant. Include sanitized screenshots for visual changes or representative request/response examples for public [APIs](../../glossary.md#api). Mark incomplete work as draft.
- **REV-02 MUST** obtain at least one qualified human approval independent of the author and contributors to the change. For changes affecting [authentication](../../glossary.md#authentication-and-authorization)/[authorization](../../glossary.md#authentication-and-authorization), secrets, [destructive migrations](../../glossary.md#migration), critical delivery controls or protected production infrastructure, obtain at least two independent approvals, including the relevant [domain owner](../../glossary.md#ownership). Use [ownership rules](../../glossary.md#ownership) to route reviews and require eligible owner approval where supported.
- **REV-03 MUST** block merge while the [change request](../../glossary.md#change-request) is a draft, [required checks](../../glossary.md#gate) are missing or failing, conflicts remain, blocking discussions are open, or approvals are stale. Verify the latest candidate, reset or explicitly renew approvals after substantive updates and rerun affected checks when the target changes. Use a [merge queue](../../glossary.md#merge-queue), verify the proposed merge result, or revalidate against the current target if concurrent merges can invalidate the checks.
- **REV-04 MUST** restrict merge permission to designated maintainers or a controlled merge service. Keep rules server-side where possible. If the hosting platform or plan lacks an enforcement feature, limit merge access to designated maintainers who verify and record the equivalent gate, or use a protected merge service. A checklist alone is not automatic enforcement.
- **REV-05 SHOULD** keep [change requests](../../glossary.md#change-request) small enough to review in one sitting. Review correctness and negative paths, [auth](../../glossary.md#authentication-and-authorization)/[tenant isolation](../../glossary.md#tenant-isolation), tests, readability, dependencies, compatibility, [observability](../../glossary.md#observability) and [rollback](../../glossary.md#rollback). Mark blocking feedback explicitly, explain its impact and distinguish optional suggestions. Authors address or discuss findings before closing them.

## Procedure: author to merge

1. Fill the [change request template](../templates/change-request/Change.md), run relevant local checks and request reviewers for the affected areas.
2. Reviewers inspect the current diff and evidence, rerun high-risk scenarios where needed and approve the reviewed version. For an expedited [hotfix](../../glossary.md#hotfix), use the same review route; record any approved deviation using the [exception procedure](../README.md).
3. The authorized merger verifies approvals, open threads, required [pipeline](../../glossary.md#pipeline) and effective commit message; merge according to [branching](../02-development/git-branching.md). Monitor the post-merge [pipeline](../../glossary.md#pipeline) and [revert](../../glossary.md#revert) or fix failures promptly.

**Evidence:** Review history, linked issue, checked [SHA](../../glossary.md#sha), successful [required jobs](../../glossary.md#gate) and final commit. See the [enforcement matrix](../enforcement.md).
