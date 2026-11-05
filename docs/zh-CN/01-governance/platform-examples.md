# 平台接入示例

[规范目录](../README.md) · [门禁执行矩阵](../enforcement.md) · [English](../../en/01-governance/platform-examples.md)

以下示例展示两个平台如何落实同一套控制。具体功能取决于套餐、仓库可见性及托管方式。缺少某项功能时，可通过受保护的集成或[代码审查规范](review-standards.md)所述等效控制达到相同结果。访问规则须在 [CI](../../glossary.md#ci-cd) 文件之外配置和验证。

| 目标 | GitHub 示例 | GitLab 示例 |
| --- | --- | --- |
| [保护分支](../../glossary.md#protected-branch) | 用[分支规则集](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)要求通过 [Pull Request](../../glossary.md#change-request)，禁止[强推](../../glossary.md#force-push)和删除，限制绕过并验证合并权限。 | 用[保护分支](https://docs.gitlab.com/user/project/repository/protect/)禁止直接推送，限制合并角色，并阻止[强推](../../glossary.md#force-push)和删除。 |
| 要求当前版本通过审查与检查 | 要求批准及适用的[代码所有者](../../glossary.md#ownership)审查，撤销[过时审批](../../glossary.md#stale-approval)，要求讨论解决及状态检查通过。按需使用合并队列或验证当前目标分支。 | 要求审批、有效的[代码所有者](../../glossary.md#ownership)审查、讨论解决及[流水线](../../glossary.md#pipeline)成功；重置[过时审批](../../glossary.md#stale-approval)。按需使用[合并结果流水线](../../glossary.md#merge-queue)或合并队列。 |
| 保护发布与部署 | 用[标签](../../glossary.md#tag)规则集限制发布[标签](../../glossary.md#tag)的变动，使用[环境保护规则](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)或受控部署服务；在 [CI](../../glossary.md#ci-cd) 中验证[标签](../../glossary.md#tag)签名和[制品](../../glossary.md#artifact)身份。 | 用保护[标签](../../glossary.md#tag)限制发布[标签](../../glossary.md#tag)的创建，使用[保护环境](https://docs.gitlab.com/ci/environments/protected_environments/)或受控部署服务；在 [CI](../../glossary.md#ci-cd) 中验证[标签](../../glossary.md#tag)签名和[制品](../../glossary.md#artifact)身份。 |
| 安装模板 | 审查模板放入 `.github/pull_request_template.md`；[工作项](../../glossary.md#issue)模板添加所需元数据后放入 `.github/ISSUE_TEMPLATE/`。参阅[模板设置](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)。 | 审查模板放入 `.gitlab/merge_request_templates/`，[工作项](../../glossary.md#issue)模板放入 `.gitlab/issue_templates/`。参阅[模板设置](https://docs.gitlab.com/user/project/description_templates/)。 |

## [CI](../../glossary.md#ci-cd) 示例：验证本套规范

两个示例均用 Python 3.9 或更高版本运行同一个[检查脚本](../../../.ci/check-standards.py)。在受保护目标上要求该检查通过；确认检查缺失、跳过或失败均不能放行。拟议变更应在隔离且不具备发布或生产[凭据](../../glossary.md#secret)的执行环境中运行。

### GitHub Actions

将工作流放在 `.github/workflows/`。[默认分支](../../glossary.md#branch)不是 `main` 时替换其名称。若合并队列要求此检查，保留[合并队列触发事件](https://docs.github.com/en/enterprise-cloud%40latest/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)。检出 Action 固定到具体提交，按依赖变更流程审查更新。

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

在 `.gitlab-ci.yml` 添加该作业。使用已安装 Python 的 [Runner](../../glossary.md#runner) 或[固定镜像](../../glossary.md#pinning)；没有 `test` 阶段时使用已有验证阶段。如有全局工作流规则，还需在其中允许[合并请求流水线](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/)与[默认分支](../../glossary.md#branch)推送。

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

## 在使用方检出规范

使用方仓库检查接入前须初始化已记录的[子模块](../../glossary.md#git-submodule)。提交来自父仓库的 [gitlink](../../glossary.md#gitlink)，不是上游分支。上面的检出 Action 添加：

```yaml
with:
  persist-credentials: false
  submodules: recursive
```

随后运行 python3 .standards/.ci/check-adoption.py。GitLab 设置 GIT_SUBMODULE_STRATEGY: recursive 并执行同一命令。公开规范仓库的检出不需要发布凭据。
