# Repository instructions

- Follow the [English Software Development Standards](docs/en/README.md). Read the modules relevant to your change and follow the nearest applicable repository or component instructions.
- Follow the [Git branching standards](docs/en/02-development/git-branching.md) before editing: inspect the current branch and working tree, refresh the approved target, and create or reuse a compliant topic branch without discarding unrelated work. Do not edit, commit or push directly on protected branches. Merge only through a change request with required checks and approvals; administrator access and passing tests do not waive this workflow.
- Keep acceptance logs, per-run verification history and temporary investigation/handoff records outside this repository, following [MNT-09](docs/en/05-maintenance/maintenance-standards.md#keep-acceptance-records-outside-source-repositories). Put evidence in CI reports, issues, change requests or the approved external system.
- When editing standards or templates here, update the corresponding English and Simplified Chinese files in the same change. Keep rule IDs and requirement levels aligned; run the CI check with `python .ci/check-standards.py` before handoff.
- Keep normative requirements independent of the hosting platform. Put provider-specific setup in the platform examples. Use repository-relative links and fictional examples in public files; omit workstation paths and non-public repository or service identifiers.
- Follow [MNT-07](docs/en/05-maintenance/maintenance-standards.md#explain-engineering-terminology) when writing or reviewing terminology. Keep existing glossary heading anchors stable.

- Use the contributor-approved Git identity for both author and committer; never invent a placeholder identity. Follow COM-05 before creating commits.
