# Reference patterns

[Standards index](README.md) · [简体中文](../zh-CN/reference-patterns.md)

Choose a pattern that fits the project and record the decision.

| Situation | Recommended approach |
| --- | --- |
| Multiple components in one repository | Keep a top-level index and component owners, with component-specific build instructions and release triggers. Test shared dependencies across affected components. |
| Existing integration or maintenance branches | Document each branch's purpose and protection, who promotes changes, and how fixes reach all supported versions. Keep release environments independent of branch names where practical. |
| Configuration spans several layers | Update safe defaults, bindings, [deployment manifests](../glossary.md#manifest), validation and onboarding docs together as applicable. |
| A [shared contract](../glossary.md#contract) changes | Inventory consumers, stage a compatible contract as needed, and verify clients against the exact version they consume. Track [rollout](../glossary.md#rollout) order and old-version support. |
| Build and deployment have different owners | Hand off the [immutable artifact](../glossary.md#artifact) identifier and build evidence. The deployment owner approves [promotion](../glossary.md#promotion), reconciles [desired state](../glossary.md#desired-state) and verifies what is running. |
| A [migration](../glossary.md#migration) or restore needs rehearsal | Use an isolated environment and representative sanitized or synthetic data. Record the tested version, duration, recovery result and unverified production conditions. |
