# 01. Repository Standards

[Standards index](../README.md) · [简体中文](../../zh-CN/01-governance/repository-standards.md) · [P0](../../glossary.md#priority)


**Scope and owner:** All source, documentation and infrastructure repositories. The repository maintainer owns onboarding, ownership and baseline configuration.

## Standards

- **REP-01 MUST** assign an accountable team and a backup contact. Use a short, descriptive lowercase [kebab-case](../../glossary.md#naming-case) name for new repositories (for example, `order-api` or `order-deploy-manifests`). Preserve established names unless a migration includes redirects, [CI](../../glossary.md#ci-cd), package references and integrations.
- **REP-02 SHOULD** use a [monorepo](../../glossary.md#repository-layout) when components change together and share access and tooling; use separate repositories when ownership, permissions or release cycles differ. Document the decision and, in a [monorepo](../../glossary.md#repository-layout), record component boundaries, build targets, owners and independent release rules.
- **REP-03 MUST** provide a root [README](../../glossary.md#readme) with purpose, owners/support, prerequisites and supported toolchain, setup and configuration, local run/build/test commands, architecture and release links, and contribution and license/usage terms. Record the approved license or internal usage terms; do not apply an open source license without [authorization](../../glossary.md#authentication-and-authorization). Add `AGENTS.md`, a contribution entry point and a security reporting route.
- **REP-04 MUST** version format settings, ignores, reproducible build inputs and applicable [CI](../../glossary.md#ci-cd) and [change request](../../glossary.md#change-request) templates. Include `.editorconfig`, `.gitattributes`, `.gitignore`, a toolchain declaration and [dependency locks](../../glossary.md#dependency-lock) as applicable. Reserve top-level directories without a leading dot for core repository content, such as `src/`, `tests/` and `docs/`. Place convenience scripts and CI-only helpers in dot-prefixed directories such as `.scripts/` or `.ci/`. Update callers, workflow paths and documentation when relocating helpers. Document generated sources committed for consumer use and how to regenerate them.
- **REP-05 MUST** document each environment variable or setting with its type, requirement, safe default, precedence, example and secret classification. Keep safe defaults and placeholder examples in Git; inject secrets externally. Fail startup on missing required configuration. Change app settings, bindings, container and deployment definitions, tests and docs together when affected.
- **REP-06 MUST** exclude local overrides, credentials, databases, logs, caches and build/test outputs from version control. Publish distributable packages/images to a [registry](../../glossary.md#registry) and build reports to [CI](../../glossary.md#ci-cd); a Git ignore rule does not protect a file already tracked.
- **REP-07 MUST** adopt the shared standards through a [Git submodule](../../glossary.md#git-submodule) at .standards/, with a reviewed exact commit recorded by the parent repository. Link the root AGENTS.md directly to .standards/docs/en/README.md and expose both language entry points in project documentation. Initialize the recorded commit in clean checkouts and [CI](../../glossary.md#ci-cd). Update the recorded commit through a normal reviewed change; never follow a moving branch or run remote updates during verification or release. See [adoption and updates](../adopting-standards.md).

## Procedure: initialize or adopt

1. Choose the layout and create the [README](../../glossary.md#readme) from the [repository template](../templates/repository/README-template.md). Put component instructions in the nearest `AGENTS.md` when necessary.
2. Enable [branch protection](../02-development/git-branching.md), assign reviewers and add the applicable [quality gates](../03-quality/testing-standards.md). Install issue and [change request](../../glossary.md#change-request) templates where your platform discovers them; see the [implementation examples](platform-examples.md).
3. Ask a contributor to follow the [README](../../glossary.md#readme) from a clean checkout. Record the successful build/check and confirm secrets and outputs remain untracked.

**Evidence:** [README](../../glossary.md#readme) and owner paths, clean-checkout commands, [CI](../../glossary.md#ci-cd) status and checked-in configuration. See [reference patterns](../reference-patterns.md) for examples of component ownership and configuration coordination.
