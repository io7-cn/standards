# 05. [Code Review](../../glossary.md#code-review)

[Standards index](../README.md) · [简体中文](../../zh-CN/01-governance/review-standards.md) · [P0](../../glossary.md#priority)


**Scope and owner:** All changes entering [protected branches](../../glossary.md#protected-branch), including docs, migrations, [CI](../../glossary.md#ci-cd), [deployment manifests](../../glossary.md#manifest) and bot changes. Maintainers configure gates; authors and reviewers own the review record.

## Standards

- **REV-01 MUST** open a [change request](../../glossary.md#change-request) with a clear title, linked issue, behavior before/after, scope, risks, verification evidence and [rollout](../../glossary.md#rollout)/[rollback](../../glossary.md#rollback) when relevant. Include sanitized screenshots for visual changes or representative request/response examples for public [APIs](../../glossary.md#api). Mark incomplete work as draft.
- **REV-02 SHOULD** obtain an independent [code review](../../glossary.md#code-review) during local development before requesting merge. A knowledgeable colleague or a local [code review subagent](../../glossary.md#code-review-subagent) can review the current diff and relevant evidence. For changes affecting [authentication](../../glossary.md#authentication-and-authorization)/[authorization](../../glossary.md#authentication-and-authorization), secrets, [destructive migrations](../../glossary.md#migration), critical delivery controls or protected production infrastructure, seek relevant [domain owner](../../glossary.md#ownership) input and review failure and recovery paths in greater depth.
- **REV-03 MUST** block merge while the [change request](../../glossary.md#change-request) is a draft, [required checks](../../glossary.md#gate) are missing or failing, conflicts remain or blocking discussions are open. Verify the latest candidate and rerun affected checks when the target changes. Use a [merge queue](../../glossary.md#merge-queue), verify the proposed merge result, or revalidate against the current target if concurrent merges can invalidate the checks.
- **REV-04 MUST** restrict merge permission to designated maintainers or a controlled merge service and enforce the checks in REV-03 on the hosting platform. Configure the required code review approval count as zero and disable mandatory last-push and code-owner approval gates. Use [ownership rules](../../glossary.md#ownership) to route review requests. A maintainer with write access decides whether the change is ready to merge after considering review findings and verification. If the platform lacks a required technical enforcement feature, use a controlled merge service or a designated maintainer to verify and record the equivalent check.
- **REV-05 SHOULD** keep [change requests](../../glossary.md#change-request) small enough to review in one sitting. Review correctness and negative paths, [auth](../../glossary.md#authentication-and-authorization)/[tenant isolation](../../glossary.md#tenant-isolation), tests, readability, dependencies, compatibility, [observability](../../glossary.md#observability) and [rollback](../../glossary.md#rollback). Mark blocking feedback explicitly, explain its impact and distinguish optional suggestions. Authors address or discuss findings before closing them.

## Approval eligibility and evidence

A [qualified reviewer](../../glossary.md#qualified-reviewer) has the knowledge and context to assess the change. A colleague or a local [code review subagent](../../glossary.md#code-review-subagent) can fulfill this role. For independent review, use a reviewer or a separate agent invocation that did not author the change and give it the current diff, applicable standards and relevant test results.

Review findings should identify the reviewed [SHA](../../glossary.md#sha) or current working diff, affected files, reasoning and relevant verification. After material changes, seek a focused follow-up review. Retain useful findings in the change request or an approved external review record under [MNT-09](../05-maintenance/maintenance-standards.md#keep-acceptance-records-outside-source-repositories). Hosting-platform approval counts and reviewer account permissions are separate from this recommended local review practice.

## Procedure: author to merge

1. Fill the [change request template](../templates/change-request/Change.md), run relevant local checks and select a local reviewer for the affected areas when following REV-02.
2. Reviewers inspect the current diff and evidence and report findings. Authors address findings and rerun affected checks. Follow REV-02 for recommended local review. For an expedited [hotfix](../../glossary.md#hotfix), record any approved deviation from mandatory controls using the [exception procedure](../README.md).
3. The authorized merger considers review findings and verifies open threads, required [pipeline](../../glossary.md#pipeline) and effective commit message. Merge according to [branching](../02-development/git-branching.md). Monitor the post-merge [pipeline](../../glossary.md#pipeline) and [revert](../../glossary.md#revert) or fix failures promptly.

**Evidence:** Review history, linked issue, checked [SHA](../../glossary.md#sha), successful [required jobs](../../glossary.md#gate) and final commit. See the [enforcement matrix](../enforcement.md).
