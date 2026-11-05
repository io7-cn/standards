# 12. Documentation and Maintenance

[Standards index](../README.md) · [简体中文](../../zh-CN/05-maintenance/maintenance-standards.md) · [P1](../../glossary.md#priority)


**Scope and owner:** Documentation, operational readiness, incidents, [deprecation](../../glossary.md#deprecation) and [technical debt](../../glossary.md#technical-debt). Repository and service owners maintain durable docs; [on-call](../../glossary.md#on-call) owns incident coordination until a commander is assigned.

## Standards

- **MNT-01 MUST** update affected docs in the same change as public interface, architecture behavior, config, deployment or operational changes. Keep [README](../../glossary.md#readme), onboarding, architecture diagrams, [API](../../glossary.md#api) reference and [runbooks](../../glossary.md#runbook) discoverable. Name owners and review dates for operational docs; validate links and commands after meaningful changes. Before publishing, remove workstation paths, private repository or service identifiers, and sensitive content from examples, logs and screenshots. Use repository-relative links and fictional examples.
- **MNT-02 SHOULD** record significant cross-component, compatibility or operational decisions as an [ADR](../../glossary.md#adr) with context, options, decision, consequences, status and supersession links. Put long-lived instructions in maintained docs; link transient investigation and handoff notes instead of making them permanent rules.
- **MNT-03 MUST** provide [runbooks](../../glossary.md#runbook) for critical services: contact/escalation, alerts and dashboards, [health checks](../../glossary.md#health-and-readiness), safe diagnosis, mitigation/[rollback](../../glossary.md#rollback), backup/restore and verification. Define service indicators and alert ownership; keep examples free of real credentials.
- **MNT-04 MUST** assign an [incident commander](../../glossary.md#incident-commander) or responsible [on-call](../../glossary.md#on-call), record [severity](../../glossary.md#priority)/impact and timeline, prioritize containment and restoration, and communicate status via the approved channel. Verify customer-visible recovery and data integrity before closing. For major incidents write a [blameless review](../../glossary.md#incident-review) with contributing factors, detection gaps, actions, owners and deadlines.
- **MNT-05 MUST** announce [deprecation](../../glossary.md#deprecation) with affected versions/users, replacement, migration steps, notice period and earliest removal date. The owner sets a documented window consistent with support commitments, monitors usage and coordinates consumers. Remove only after the notice period and readiness checks; record extensions or emergency exceptions.
- **MNT-06 SHOULD** track [technical debt](../../glossary.md#technical-debt) as issues with impact, risk, ownership and suggested remediation. Review on a regular cadence, prioritize debt that blocks reliability or delivery, and record the reason when deferring. Handoffs include outstanding risks, operational responsibilities and where to find evidence.

## Explain engineering terminology

- **MNT-07 MUST** explain [jargon](../../glossary.md#jargon), specialist terms and abbreviations used in engineering documents, including standards and templates. Prefer plain language where it is equally precise. When a term is needed, link its mentions in prose directly to its glossary entry and give the expansion or a brief explanation on first use when readers need it to understand the text. Add or update both language definitions in the same change. Reviewers verify that the definition matches the intended meaning and the link opens the right entry. Keep commands, literal examples and machine-readable identifiers intact.

For example, write “[ADR](../../glossary.md#adr) (Architecture Decision Record)” the first time you introduce it to readers unfamiliar with the term.

## Maintain separate language editions

- **MNT-08 MUST** provide project documentation in English and Simplified Chinese. Put each edition in its own file under `docs/en/` and `docs/zh-CN/`, respectively. Use matching filenames, link each edition directly to the other, and update both in the same change. Write `AGENTS.md` in English only and link it directly to the English documentation entry point under `docs/en/`.

## Procedures

1. **Architectural change:** Draft an [ADR](../../glossary.md#adr) using the [template](../templates/maintenance/ADR.md); review with affected owners, then link it from the architecture index and [change request](../../glossary.md#change-request).
2. **Incident:** [Triage](../../glossary.md#triage) → assign command → contain → recover → verify → review. Use the [incident review template](../templates/maintenance/Incident-review.md); track corrective actions as issues and verify their outcomes. Follow the restricted [security process](../03-quality/security-standards.md) for sensitive incidents.
3. **Retirement:** Inventory consumers → announce → provide migration and compatibility window → observe adoption → approve removal → update contracts, dashboards and [runbooks](../../glossary.md#runbook) → verify no residual dependency. Link the [release notes](../../glossary.md#release-notes-and-changelog) and migration issue.

**Evidence:** Versioned docs, [ADR](../../glossary.md#adr) decision and supersession links, [runbook](../../glossary.md#runbook) and verified restore links, incident timeline and actions, [deprecation](../../glossary.md#deprecation) notice and consumer readiness.
