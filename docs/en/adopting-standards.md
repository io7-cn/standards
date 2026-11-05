# Adopt and update the standards

[Standards index](README.md) · [简体中文](../zh-CN/adopting-standards.md)

The project maintainer owns the adopted revision and applicable project profile. A [Git submodule](../glossary.md#git-submodule) keeps the standards in a separate repository while the parent records one exact commit. The recorded commit is the version in force; the newest upstream branch does not automatically replace it. This standards repository does not add a submodule pointing to itself.

Add the approved standards repository at .standards/, then select the reviewed full commit. Replace the fictional URL and commit placeholder below. Do not add a branch-tracking option to .gitmodules.

```sh
git submodule add --name standards https://code.example.com/example/standards.git .standards
git -C .standards checkout --detach <reviewed-full-commit>
git add .gitmodules .standards
```

Add a direct English entry in AGENTS.md and links to both language editions in project documentation. Record project-specific owners, toolchains, applicable controls and approved exceptions beside those links; do not duplicate the shared requirements.

```md
- Follow the [English development standards](.standards/docs/en/README.md).
```

Clone with submodules or initialize an existing checkout:

```sh
git clone --recurse-submodules <project-url>
git submodule update --init --recursive
python .standards/.ci/check-adoption.py
```

The adoption check validates the [gitlink](../glossary.md#gitlink), initialized commit, clean standards tree, agent link and bilingual project entry points, then checks the pinned standards documents. Run it from the parent repository after committing the adoption change. Configure [CI](../glossary.md#ci-cd) to initialize submodules and run the same command; provider examples are [here](01-governance/platform-examples.md#consume-the-standards).

To update, fetch upstream commits inside .standards, inspect the changes, check out the approved commit without selecting a branch, and stage .standards in the parent. Review the changed requirements and affected configuration together. Run adoption and applicable product checks. Restore an earlier approved revision by recording that exact commit in a new reviewed parent change. Never use git submodule update --remote in verification or release.
