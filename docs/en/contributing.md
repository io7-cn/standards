# Contributing and support

[Standards index](README.md) · [简体中文](../zh-CN/contributing.md)

The product engineering team at 艾欧柒（杭州）智能科技有限公司 maintains these standards. Use the repository issue tracker for questions, corrections and proposed changes. Maintainers coordinate review and can assign a backup reviewer through the same tracker. These are engineering requirements, not a representation that every adopting project already satisfies every control.

For a confidential security concern, first request a private contact channel in an issue without including the sensitive details. Share details only after a maintainer provides that channel. Never post credentials, private service identifiers or personal data in public reports.

Use Python 3.9 or later; checks use only its standard library. There is no application runtime, deployment environment, required environment variable or secret. Run:

```sh
python .ci/check-standards.py
```

Maintain matching English and Simplified Chinese files under docs/en and docs/zh-CN. Keep rule identifiers and requirement levels aligned, preserve glossary anchors, and link jargon to its entry. AGENTS.md stays English only. Put auxiliary tools under .ci. Validate relative links and the adoption helper when changing layout.

Submit a focused [change request](../glossary.md#change-request) with the reason, affected rules, compatibility implications and validation. Reviewers check both editions, examples and enforcement expectations. Publish only final maintained guidance and fictional examples; omit workstation paths, non-public identifiers, transient investigations and generated output. Consumers adopt updates by reviewing and recording a new exact commit; publishing standards does not rewrite their pins.

[Apache License 2.0](../../LICENSE) applies to the documentation, templates and verification helpers in this repository. Copied templates do not automatically change a consuming project’s license. Preserve applicable attribution.
