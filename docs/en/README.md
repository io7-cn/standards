# Software Development Standards

[简体中文](../zh-CN/README.md) · [Enforcement matrix](enforcement.md) · [Reference patterns](reference-patterns.md) · [Platform examples](01-governance/platform-examples.md) · [Engineering glossary](../glossary.md)

[Adopt a pinned revision](adopting-standards.md) · [Contribute and report issues](contributing.md)

This is the normative English edition for all product engineering at 艾欧柒（杭州）智能科技有限公司. It applies to open-source and internal projects, including applications, libraries and the infrastructure that supports them. Apply each requirement where the corresponding activity or component exists, across code hosting platforms and [CI/CD](../glossary.md#ci-cd) systems. The [coding standards](02-development/coding-standards.md#primary-technology-stack) define the profiles for C#, [TypeScript](../glossary.md#ts) and [CSS](../glossary.md#css).

A **[change request](../glossary.md#change-request)** is the record used to review and merge a proposed change (for example, a [pull request](../glossary.md#change-request) or [merge request](../glossary.md#change-request)). An **issue** is a tracked [work item](../glossary.md#issue) and may live in a separate tracker.

## How to apply the standards

- **[MUST](../glossary.md#requirement-levels)** is required; **[SHOULD](../glossary.md#requirement-levels)** is the recommended default, with the reason for a different choice recorded when material; **[MAY](../glossary.md#requirement-levels)** is optional. Standards set the rules, guidance describes defaults and alternatives, and procedures describe how to do the work.
- Record the adopted revision, accountable owners, toolchain, branch model, gates, release triggers and operational profile in the repository [README](../glossary.md#readme) or contribution docs. Project-specific instructions supply implementation detail. Conflicts with a [MUST](../glossary.md#requirement-levels) require an explicit exception; stronger applicable policies still apply.
- To request an exception, record the rule [ID](../glossary.md#id), scope, reason, risk, mitigation, owner, expiration and restoration plan in an issue or restricted record. Obtain the repository owner and affected [domain owner](../glossary.md#ownership)'s approval before bypass; include the security owner for security controls and the production owner for production controls. Link the record to the change. In an active incident, only a pre-authorized emergency process can expedite approval; log the actor, action and rationale at the time, review by the next business day and restore controls. Review expired exceptions and close them with evidence.
- Maintain both language editions in the same change, matching rule [IDs](../glossary.md#id) and requirement levels. If interpretations differ, use the English edition and correct the translation. Standards maintainers review cross-cutting changes with affected domain owners.
- Explain [jargon](../glossary.md#jargon), specialist terms and abbreviations in engineering documents, including these standards. See [MNT-07](05-maintenance/maintenance-standards.md#explain-engineering-terminology).

Use the [shared coding style and file organization](02-development/coding-style.md) for C#, TypeScript and CSS.

## Modules

| No. | Standard | Adoption [priority](../glossary.md#priority) |
| --- | --- | --- |
| 01 | [Repository Standards](01-governance/repository-standards.md) | [P0](../glossary.md#priority) |
| 02 | [Coding Standards](02-development/coding-standards.md) | [P0](../glossary.md#priority) |
| 03 | [Git Branching](02-development/git-branching.md) | [P0](../glossary.md#priority) |
| 04 | [Commit Convention](02-development/commit-convention.md) | [P0](../glossary.md#priority) |
| 05 | [Code Review](01-governance/review-standards.md) | [P0](../glossary.md#priority) |
| 06 | [Requirements and issues](01-governance/issue-standards.md) | [P0](../glossary.md#priority) |
| 07 | [Testing and Quality](03-quality/testing-standards.md) | [P0](../glossary.md#priority) |
| 08 | [CI/CD, Build and Deployment](04-delivery/cicd-standards.md) | [P0](../glossary.md#priority) |
| 09 | [Versioning and Release](04-delivery/release-standards.md) | [P0](../glossary.md#priority) |
| 10 | [Secure Development](03-quality/security-standards.md) | [P0](../glossary.md#priority) |
| 11 | [API and Data](02-development/api-data-standards.md) | [P1](../glossary.md#priority) |
| 12 | [Documentation and Maintenance](05-maintenance/maintenance-standards.md) | [P1](../glossary.md#priority) |

[P0](../glossary.md#priority) is the initial baseline; [P1](../glossary.md#priority) can be phased in as the project grows. [Priority](../glossary.md#priority) governs [rollout](../glossary.md#rollout) order, not whether an applicable [MUST](../glossary.md#requirement-levels) is binding after adoption.

## Adoption sequence

1. **Collaboration:** Choose the branch model, enforce review and commit rules, and adopt issue and [change request](../glossary.md#change-request) templates. Verify an example change from issue through merge.
2. **Quality and delivery:** Make [lint](../glossary.md#lint), build, tests, security and release controls required. Prove rejected and accepted paths and [promote](../glossary.md#promotion) an immutable candidate end to end.
3. **Long-term governance:** Add contract compatibility, [migration](../glossary.md#migration) and restore exercises, operational docs, [ADRs](../glossary.md#adr), incident reviews and [deprecation](../glossary.md#deprecation) tracking. Assign owners and dates to remaining gaps.

## Templates

When copying a template, update its glossary links for the destination or remove the link markup while keeping the labels.

[Repository README](templates/repository/README-template.md) · [Feature](templates/issue/Feature.md) · [Bug](templates/issue/Bug.md) · [Change request](templates/change-request/Change.md) · [Release record](templates/release/Release.md) · [ADR](../glossary.md#adr) [template](templates/maintenance/ADR.md) · [Incident review](templates/maintenance/Incident-review.md)
