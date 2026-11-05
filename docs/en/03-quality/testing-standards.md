# 07. Testing and Quality

[Standards index](../README.md) · [简体中文](../../zh-CN/03-quality/testing-standards.md) · [P0](../../glossary.md#priority)


**Scope and owner:** Code, infrastructure and release verification. Component owners define risk-based checks; contributors add [coverage](../../glossary.md#coverage); maintainers make [required jobs](../../glossary.md#gate) enforceable.

## Standards

- **TST-01 MUST** test changed behavior at the lowest reliable layer, including meaningful negative and boundary cases. Add [regression coverage](../../glossary.md#regression-test) for defects; if automation cannot reliably reproduce a defect, record a repeatable manual check and the reason. Cover critical paths and failure modes even when a global percentage is high.
- **TST-02 MUST** make automated tests isolated and repeatable with controlled clocks, [fixtures](../../glossary.md#fixture) and seeded data where needed. Avoid live production credentials, data and dependencies. Exercise the real provider in [integration tests](../../glossary.md#integration-test) when behavior depends on it; [mocks](../../glossary.md#mock) or in-memory databases alone do not prove real database, identity or network behavior.
- **TST-03 MUST** block merge on applicable [required jobs](../../glossary.md#gate): formatting/[lint](../../glossary.md#lint)/[static analysis](../../glossary.md#static-analysis), build, test and [security gates](security-standards.md). Publish reports even on failure. Mark optional checks explicitly; [required jobs](../../glossary.md#gate) may not be skipped or marked allowed-to-fail. Verify path filters against shared dependencies and the latest candidate.
- **TST-04 SHOULD** track overall and [changed coverage](../../glossary.md#coverage) trends, plus critical path [coverage](../../glossary.md#coverage). If a threshold is enforced, document its scope, measurement and justified exceptions. Review new or changed security and reliability warnings as defects; baseline unrelated legacy findings in a tracked cleanup plan.
- **TST-05 MUST** record [flaky test](../../glossary.md#flaky-test) ownership, reproduction and repair deadline. Temporary [quarantine](../../glossary.md#flaky-test) needs an [approved exception](../../glossary.md#exception) and replacement evidence for blocked critical [coverage](../../glossary.md#coverage); blind retries do not prove a pass.
- **TST-06 MUST** state what ran, against which build and environment, and what remains unverified. For documentation-only changes use relevant links, [lint](../../glossary.md#lint) and example validation; run executable checks when commands or behavior change.
- **TST-07 MUST** keep tests of a single component with that component. Use a separate [integration test](../../glossary.md#integration-test) suite for behavior that depends on multiple components, with explicit dependencies on the components or their built [artifacts](../../glossary.md#artifact). Verify that a component's own suite can run with its declared dependencies and without unrelated components' source trees.

| Layer | Minimum use |
| --- | --- |
| Unit | Domain invariants, transformations, validation and error branches |
| Integration | Real persistence/migrations, [authorization](../../glossary.md#authentication-and-authorization) adapters and external [I/O](../../glossary.md#io) with representative dependencies |
| [Contract](../../glossary.md#contract) | Check [API schema](../../glossary.md#schema)/[proto](../../glossary.md#protobuf) and consumer compatibility; exercise serializers and generated clients when changed |
| [E2E](../../glossary.md#e2e) / [smoke](../../glossary.md#smoke-test) | Critical user journeys and post-deploy readiness against the deployed [artifact](../../glossary.md#artifact) |
| Performance / resilience | High-risk changes to latency, concurrency, capacity or failure handling; compare against a documented workload/budget |

## Procedure: [quality gates](../../glossary.md#gate)

Select the affected suites, then run the repository verification entry point. For .NET, follow the [baseline verification order](../02-development/coding-standards.md#verification-by-stack) with the project's documented commands. Add contract, [migration](../../glossary.md#migration) or performance gates when triggered. Before release, rerun required evidence for the exact [artifact](../../glossary.md#artifact)/commit and exercise the critical deployed path.

**Evidence:** Required job results, test report, selected scope and risks, manual evidence or exception link, and any performance comparison.
