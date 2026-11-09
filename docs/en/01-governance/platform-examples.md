# Platform implementation examples

[Standards index](../README.md) · [Enforcement matrix](../enforcement.md) · [简体中文](../../zh-CN/01-governance/platform-examples.md)

These examples implement the same controls on two platforms. Features depend on the plan, repository visibility and hosting model. Where a feature is unavailable, meet the same outcome with a protected integration or the equivalent control described in [code review](review-standards.md). Configure and test access rules separately from the [CI](../../glossary.md#ci-cd) file.

| Outcome | GitHub example | GitLab example |
| --- | --- | --- |
| Protect branches | Use [branch rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets) to require pull requests, prevent [force pushes](../../glossary.md#force-push) and deletion, and restrict bypass. Verify merge permissions. | Use [protected branches](https://docs.gitlab.com/user/project/repository/protect/) to deny direct pushes, restrict merge roles and prevent [force pushes](../../glossary.md#force-push) and deletion. |
| Require current reviews and checks | Require approval and applicable [code owner](../../glossary.md#ownership) reviews, dismiss [stale approvals](../../glossary.md#stale-approval), and require conversation resolution and status checks. Use a [merge queue](../../glossary.md#merge-queue) or current-base checks where needed. | Require approvals, eligible [code owner](../../glossary.md#ownership) reviews, resolved discussions and successful [pipelines](../../glossary.md#pipeline); reset [stale approvals](../../glossary.md#stale-approval). Use [merged-results pipelines](../../glossary.md#merge-queue) or [merge trains](../../glossary.md#merge-queue) where needed. |
| Protect releases and deployments | Restrict release tag changes with tag rulesets; use [environment protection rules](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) or a controlled deployment service. Verify tag signatures and [artifact](../../glossary.md#artifact) identity in [CI](../../glossary.md#ci-cd). | Restrict release tag creation with protected tags; use [protected environments](https://docs.gitlab.com/ci/environments/protected_environments/) or a controlled deployment service. Verify tag signatures and [artifact](../../glossary.md#artifact) identity in [CI](../../glossary.md#ci-cd). |
| Install templates | Put the review template in `.github/pull_request_template.md` and issue templates with the required metadata in `.github/ISSUE_TEMPLATE/`. See [template setup](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates). | Put the review template in `.gitlab/merge_request_templates/` and issue templates in `.gitlab/issue_templates/`. See [template setup](https://docs.gitlab.com/user/project/description_templates/). |

When adopting AI-assisted approval, verify that the platform counts a decision from the explicitly authorized [review identity](../../glossary.md#qualified-reviewer) for the current candidate. If the platform cannot count it natively, use the equivalent gate in [REV-04](review-standards.md). Verify that unauthorized or stale decisions cannot satisfy the gate.

## [CI](../../glossary.md#ci-cd) examples: validate this standards package

Both examples use Python 3.9 or later and run the same [checker](../../../.ci/check-standards.py). Require the check on protected targets and confirm that missing, skipped and failed runs cannot authorize a merge. Run proposed changes on isolated executors without publishing or production credentials.

### GitHub Actions

Place the workflow under `.github/workflows/`. Replace `main` if the [default branch](../../glossary.md#branch) differs. Keep the [merge queue trigger](https://docs.github.com/en/enterprise-cloud%40latest/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks) when the queue requires this check. Review updates to the [pinned checkout](../../glossary.md#pinning) action as dependency changes.

```yaml
name: Standards validation
"on":
  pull_request:
  merge_group:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  check-standards:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          persist-credentials: false
      - run: python3 .ci/check-standards.py
```

### GitLab [CI](../../glossary.md#ci-cd)

Add the job to `.gitlab-ci.yml`. Use a [runner](../../glossary.md#runner) or [pinned image](../../glossary.md#pinning) with Python installed; use an existing validation stage if there is no `test` stage. If global workflow rules are present, allow [merge request pipelines](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/) and [default-branch](../../glossary.md#branch) pushes there too.

```yaml
check-standards:
  stage: test
  script:
    - python3 .ci/check-standards.py
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
```

<a id="consume-the-standards"></a>

## Consume the standards

For an adopting repository, initialize the recorded [submodule](../../glossary.md#git-submodule) before checking adoption. The commit comes from the parent [gitlink](../../glossary.md#gitlink), not an upstream branch. Use the checkout action above with:

```yaml
with:
  persist-credentials: false
  submodules: recursive
```

Then run python3 .standards/.ci/check-adoption.py. On GitLab, set GIT_SUBMODULE_STRATEGY: recursive and run the same command. Neither setup needs publishing credentials for a public standards repository.
