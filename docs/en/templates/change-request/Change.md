## Change

- [Issue](../../../glossary.md#issue) reference or tracker-supported closing directive under [COM-03](../../02-development/commit-convention.md) (use closure when this change completes the issue):
- Before / after:
- Scope and affected components:

## Risk, compatibility and [rollout](../../../glossary.md#rollout)

- [Auth](../../../glossary.md#authentication-and-authorization)/data/config/[API](../../../glossary.md#api) and downstream consumer impact:
- Deployment/[migration](../../../glossary.md#migration) order, observation and [rollback](../../../glossary.md#rollback) or [forward fix](../../../glossary.md#roll-forward):
- [ADR](../../../glossary.md#adr) or [approved exception](../../../glossary.md#exception), if any:

## Verification

| Check / scenario | Result | Build, environment or evidence |
| --- | --- | --- |
| Relevant test or check | Pass / fail / not run | Link or command |

Add sanitized screenshots or request/response examples where applicable. State what remains unverified.

## Before merge

- [ ] An authorized maintainer confirmed merge readiness and the current candidate passed [required jobs](../../../glossary.md#gate).
- Recommended local [review](../../01-governance/review-standards.md#approval-eligibility-and-evidence) by a colleague or Code Review subagent, findings and follow-up (state if not performed):
- [ ] Blocking threads are resolved and the final commit message conforms.
- [ ] Tests, contracts, docs and [rollout](../../../glossary.md#rollout) records are updated as applicable.
