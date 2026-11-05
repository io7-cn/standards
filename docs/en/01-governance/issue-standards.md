# 06. Requirements and issues

[Standards index](../README.md) · [简体中文](../../zh-CN/01-governance/issue-standards.md) · [P0](../../glossary.md#priority)


**Scope and owner:** Product requirements, defects, incidents, engineering upkeep and discovery. Product or technical owners [triage](../../glossary.md#triage) and prioritize; the assignee drives the work; the acceptance owner confirms the outcome.

## Standards

- **ISS-01 MUST** track planned work in an issue before implementation, or create/link an incident record promptly for emergency work. Classify as feature, bug, maintenance, [spike](../../glossary.md#spike), security or incident. Put sensitive evidence in restricted tracking with sanitized references in public records.
- **ISS-02 MUST** capture the problem, affected users/systems, expected outcome, in/out scope, measurable [acceptance criteria](../../glossary.md#acceptance-criteria), owner, [priority](../../glossary.md#priority) and dependencies. For a bug add affected version/environment, reproduction, expected/actual behavior, impact and sanitized evidence. Document nonfunctional requirements when they affect acceptance.
- **ISS-03 SHOULD** estimate after clarifying scope; record major assumptions, effort range and uncertainty. Split work by independently verifiable outcomes, with an owner and [acceptance criteria](../../glossary.md#acceptance-criteria) for each. [Timebox](../../glossary.md#spike) unknowns as a [spike](../../glossary.md#spike) with a decision or evidence deliverable.
- **ISS-04 MUST** track status and keep blocker, dependency and ownership information current. Default lifecycle: [Triage](../../glossary.md#triage) → Ready → In progress → In review → Accepted → Done. Use a Blocked label with cause and next action; record why when closing as duplicate, declined or deferred. Use tracker states, labels or board columns.
- **ISS-05 MUST** link issue → branch where practical → [change request](../../glossary.md#change-request) → [pipeline](../../glossary.md#pipeline) → release/deployment if applicable. Partial [change requests](../../glossary.md#change-request) use a reference; close only after acceptance evidence is attached and the agreed delivery condition is met. Where auto-closing at merge conflicts with production acceptance, use a reference and close after deployment verification.

## [Priority](../../glossary.md#priority) defaults

| [Priority](../../glossary.md#priority) | Meaning and next action |
| --- | --- |
| [P0](../../glossary.md#priority) | Active severe outage, loss or security exposure. Start incident [triage](../../glossary.md#triage) immediately. |
| [P1](../../glossary.md#priority) | Major impact or critical delivery blocker. Assign an owner and plan in the current cycle. |
| [P2](../../glossary.md#priority) | Normal delivery. Prioritize in the [backlog](../../glossary.md#backlog). |
| [P3](../../glossary.md#priority) | Minor improvement or low impact. Batch or defer with a reason. |

[Priority](../../glossary.md#priority) expresses urgency; record [severity](../../glossary.md#priority) (actual impact) separately. These labels are independent of document adoption priorities.

## Procedure: ready and done

[Triage](../../glossary.md#triage) with the [feature](../templates/issue/Feature.md) or [bug](../templates/issue/Bug.md) template. Move to Ready when scope, acceptance, owner and dependencies are clear. Before Done, compare expected outcomes to test/demo evidence, confirm the agreed delivery state, link remaining work and record the acceptance owner. For an architecture decision, add an [ADR](../../glossary.md#adr) per [maintenance](../05-maintenance/maintenance-standards.md).

**Evidence:** issue history, [acceptance criteria](../../glossary.md#acceptance-criteria) and result, related [change request](../../glossary.md#change-request), verification and delivery links.
