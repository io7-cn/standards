# Repository instructions

- Follow the [English development standards](.standards/docs/en/README.md) at the exact revision recorded by this repository and read the [English project documentation](docs/en/README.md).
- Follow the [Git branching standards](.standards/docs/en/02-development/git-branching.md) before editing. Inspect the current branch and working tree, refresh the approved target, and create or reuse a compliant topic branch without discarding unrelated work. Do not edit, commit or push directly on protected branches. Merge only through a change request with required checks and approvals. Administrator access and passing tests do not waive this workflow; emergency deviations follow the documented exception procedure.
- Keep acceptance logs, per-run verification history and temporary investigation/handoff records outside source control under [MNT-09](.standards/docs/en/05-maintenance/maintenance-standards.md#keep-acceptance-records-outside-source-repositories). Link execution evidence from the relevant issue or change request; keep reusable criteria and procedures in maintained docs.
- Keep project documentation in separate docs/en and docs/zh-CN files, with reciprocal links and matching updates. Keep this file English only.
- Follow repository-specific formatting, build and verification instructions. Keep secrets, workstation paths and private identifiers out of public files.
- Use the contributor-approved Git identity for both author and committer.
