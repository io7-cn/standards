# 10. Secure Development

[Standards index](../README.md) · [简体中文](../../zh-CN/03-quality/security-standards.md) · [P0](../../glossary.md#priority)


**Scope and owner:** Code, dependencies, credentials, [CI](../../glossary.md#ci-cd), runtime and data handling. The security owner sets policy and coordinates restricted incidents; service owners remediate.

## Standards

- **SEC-01 MUST** keep secrets out of Git, build arguments/layers, [artifacts](../../glossary.md#artifact), example [fixtures](../../glossary.md#fixture), [telemetry](../../glossary.md#telemetry) and ordinary logs. Store them in the approved secrets manager; use short-lived, scoped [workload identity](../../glossary.md#workload-identity) where available. Restrict access by environment and audit retrieval, rotation and revocation. Masking alone does not make a variable safe for untrusted jobs.
- **SEC-02 MUST** authenticate at trust boundaries and authorize every protected operation and object on the server. Deny by default; use [least privilege](../../glossary.md#least-privilege) and verify [tenant isolation](../../glossary.md#tenant-isolation). Validate input size, type and semantics; use parameterized queries, safe output encoding and destination allowlists for server-side requests where applicable. Use [TLS](../../glossary.md#tls) and protect browser sessions against token theft and request forgery.
- **SEC-03 MUST** run [secret detection](../../glossary.md#secret-detection), [static analysis](../../glossary.md#static-analysis) and [dependency scanning](../../glossary.md#dependency-scanning) on relevant changes; scan shipped [container images](../../glossary.md#container-image) and recheck supported releases for newly disclosed issues. Block exposed credentials and respond immediately. Block new applicable critical/high findings unless a documented exception with mitigation is approved. [Triage](../../glossary.md#triage) findings against reachability and impact; record accepted false positives separately.
- **SEC-04 MUST** build in a trusted environment from approved sources, review new/transitive dependencies and pin toolchain/[base image](../../glossary.md#container-image) inputs. For deployable [artifacts](../../glossary.md#artifact) publish an [SBOM](../../glossary.md#sbom) and [provenance](../../glossary.md#provenance), bind them to [artifact](../../glossary.md#artifact) identity and verify required signatures/[provenance](../../glossary.md#provenance) before [promotion](../../glossary.md#promotion). Run containers without root/extra capabilities where feasible; authorize and document exceptions.
- **SEC-05 MUST** classify sensitive data and minimize collection and retention. Encrypt protected data in transit and at rest under the applicable policy; restrict logs and backups and audit privileged actions. Use synthetic or approved sanitized data outside production. Review new trust boundaries, [auth](../../glossary.md#authentication-and-authorization) flows and sensitive processing for abuse cases.
- **SEC-06 MUST** publish a safe vulnerability-reporting route, restrict disclosure until coordinated, and track [severity](../../glossary.md#priority), owner and remediation deadline. Defaults from confirmation: active exploitation or exposed credentials trigger immediate incident response; critical findings are remediated within 72 hours, high within 14 calendar days. If the deadline cannot be met, apply documented mitigation and get a time-bound security-owner exception before expiry.

## Procedure: suspected credential leak

1. Restrict the report and identify credential scope without copying the value. Immediately revoke or contain and rotate the credential, then update affected consumers. Verify that the old credential no longer works.
2. Check audit records for misuse, preserve evidence and determine affected environments and data. Remove exposures from code, [artifacts](../../glossary.md#artifact), logs and caches; coordinate history cleanup only if needed. History rewriting does not revoke a secret.
3. Verify the replacement and restored service, add prevention checks, and document the incident and follow-up per [maintenance](../05-maintenance/maintenance-standards.md).

**Evidence:** Scan results, [SBOM](../../glossary.md#sbom)/[provenance](../../glossary.md#provenance) references, restricted risk decision, rotation/revocation and audit records. Evidence must not contain raw secrets or unauthorized personal data.
