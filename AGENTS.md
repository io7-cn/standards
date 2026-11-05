# Repository instructions

- Follow the [English Software Development Standards](docs/en/README.md). Read the modules relevant to your change and follow the nearest applicable repository or component instructions.
- When editing standards or templates here, update the corresponding English and Simplified Chinese files in the same change. Keep rule IDs and requirement levels aligned; run the CI check with `python .ci/check-standards.py` before handoff.
- Keep normative requirements independent of the hosting platform. Put provider-specific setup in the platform examples. Use repository-relative links and fictional examples in public files; omit workstation paths and non-public repository or service identifiers.
- Follow [MNT-07](docs/en/05-maintenance/maintenance-standards.md#explain-engineering-terminology) when writing or reviewing terminology. Keep existing glossary heading anchors stable.

- Use the contributor-approved Git identity for both author and committer; never invent a placeholder identity. Follow COM-05 before creating commits.
