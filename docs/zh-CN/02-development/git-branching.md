# 03. Git 分支规范

[规范目录](../README.md) · [English](../../en/02-development/git-branching.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** [维护者](../../glossary.md#ownership)配置分支，作者维护[工作分支](../../glossary.md#topic-branch)。

## 规范

- **GIT-01 MUST（必须）** 保护[默认分支](../../glossary.md#branch)以及仍在使用的发布／集成分支。普通角色不得直接推送、[强推](../../glossary.md#force-push)或删除[保护分支](../../glossary.md#protected-branch)。仅指定角色或受控合并服务可通过[变更请求](../../glossary.md#change-request)合并，并满足审批和 [CI](../../glossary.md#ci-cd) 门禁。记录平台设置或等效强制手段。
- **GIT-02 SHOULD（推荐）** 从最新的 `main` 创建短生命周期[工作分支](../../glossary.md#topic-branch)，并合回[主干](../../glossary.md#branch)。既有 `master`、`develop` 或受支持发布分支可保留，但须记录目标分支、[晋级](../../glossary.md#promotion)、[回移植](../../glossary.md#backport-and-forward-port)与保护规则。仅因[部署环境](../../glossary.md#environment)不同，不必创建分支。
- **GIT-03 MUST（必须）** 使用全小写连字符[工作分支](../../glossary.md#topic-branch)名，例如 `feature/123-login`、`fix/124-timeout`、`hotfix/125-auth`。也可用 `refactor/`、`docs/`、`test/`、`chore/` 和 `spike/`；已记录的既有别名（如 `feat/`）有效。可行时包含[工作项](../../glossary.md#issue)编号，每个分支只服务一个目的。
- **GIT-04 SHOULD（推荐）** 普通[变更请求](../../glossary.md#change-request)压缩成一条符合 [Conventional Commits](../../glossary.md#conventional-commits) 的提交。独立提交有保留价值、集成分支合并或[回移植](../../glossary.md#backport-and-forward-port)需要保留祖先关系时，可用[合并提交](../../glossary.md#merge-commit)，并在仓库细则记录策略。可以 [rebase](../../glossary.md#rebase) 私有分支；改写共享历史须先协调。对约定的[工作分支](../../glossary.md#topic-branch)，核对远端末端后使用 [`--force-with-lease`](../../glossary.md#force-push)；日常工作不得改写[保护分支](../../glossary.md#protected-branch)。
- **GIT-05 MUST（必须）** 在源分支理解双方改动后解决冲突，重跑受影响检查；实质变更后重新审查。确认没有依赖[变更请求](../../glossary.md#change-request)后删除已合并的[工作分支](../../glossary.md#topic-branch)。放弃任务时记录原因，清理过时分支前确认不会丢失未合并工作。
- **GIT-06 MUST（必须）** 在根目录纯英文 `AGENTS.md` 中明确写出分支工作流程，并直接链接本模块。贡献者与自动化编码智能体在编辑前检查当前分支和工作区，刷新获准的目标分支，在保留无关工作的前提下创建或复用合规[工作分支](../../glossary.md#topic-branch)。不直接在[保护分支](../../glossary.md#protected-branch)上编辑或提交；通过[变更请求](../../glossary.md#change-request)合并，并满足 GIT-01 要求的检查与审批。管理员权限、工具访问权限及测试通过均不豁免这些要求。紧急偏离遵循[例外流程](../README.md)。

## 流程：日常变更与[紧急修复](../../glossary.md#hotfix)

1. 关联[工作项](../../glossary.md#issue)，从已获[授权](../../glossary.md#authentication-and-authorization)的远端刷新目标分支，从目标分支创建[工作分支](../../glossary.md#topic-branch)；需要尽早反馈时开 草稿[变更请求](../../glossary.md#change-request)。
2. 合并前按需同步目标分支、解决冲突，并验证当前提交或合并结果。按[审查规则](../01-governance/review-standards.md)合并后删除[工作分支](../../glossary.md#topic-branch)。
3. 故障期间，如果受影响的受支持版本与[主干](../../glossary.md#branch)不同，从该版本创建分支，走加急[变更请求](../../glossary.md#change-request)和[发布流程](../04-delivery/release-standards.md)，并用单独关联的[变更请求](../../glossary.md#change-request)把修复[移植](../../glossary.md#backport-and-forward-port)到其他受影响分支。紧急偏离须遵循[例外流程](../README.md)并留痕。

**验收证据：** 分支规则、关联[变更请求](../../glossary.md#change-request)、合并候选[流水线](../../glossary.md#pipeline)、已审查的冲突处理及关联的[移植](../../glossary.md#backport-and-forward-port)[变更请求](../../glossary.md#change-request)。
