# 04. Git 提交规范

[规范目录](../README.md) · [English](../../en/02-development/commit-convention.md) · [P0](../../glossary.md#priority)


**适用范围与责任人：** 作者编写[提交信息](../../glossary.md#commit)；[维护者](../../glossary.md#ownership)在受保护历史上强制执行提交约定。

## 规范

- **COM-01 MUST（必须）** 对进入受保护历史的人工提交（含 [squash](../../glossary.md#squash) 提交）使用 [Conventional Commits 1.0.0](../../glossary.md#conventional-commits)。类型和可选作用域用小写；主题简明描述动作，不加句号，建议不超过 72 个字符。描述默认英文，项目可记录使用其他语言。采用[合并提交](../../glossary.md#merge-commit)时保留平台生成的合并消息。
- **COM-02 MUST（必须）** 每条最终提交只包含一个完整变更，连同所需测试和文档。拆开独立工作和大批机械编辑。[工作分支](../../glossary.md#topic-branch)可含 [fixup](../../glossary.md#wip)、[WIP](../../glossary.md#wip) 或临时调试提交；合并前须移除或压缩。
- **COM-03 MUST（必须）** 用冒号前的 `!` 或 `BREAKING CHANGE:` [尾注](../../glossary.md#trailer)标记[破坏性变更](../../glossary.md#breaking-change)，并在正文／[尾注](../../glossary.md#trailer)和[变更请求](../../glossary.md#change-request)说明兼容影响及迁移方法。正文和[尾注](../../glossary.md#trailer)用空行分隔；用 `Refs: #123` 或带项目名的引用关联任务。只有跟踪系统支持且合并已满足验收与交付条件时，才自动关闭[工作项](../../glossary.md#issue)；其他情况使用普通引用。
- **COM-04 MUST（必须）** 在服务端或必过 [CI](../../glossary.md#ci-cd) 门禁校验提交格式。保留的每条人工提交都应校验；[squash](../../glossary.md#squash) 时通过受控合并模板或合并服务校验实际落库信息。本地 Hook 可提供提前反馈。受保护发布[标签](../../glossary.md#tag)须使用可验证签名；仓库细则要求时也验证提交签名。签署[尾注](../../glossary.md#trailer)不等于密码学签名。

- **COM-05 MUST（必须）** 作者与提交者均使用贡献者认可的提交身份。创建提交前配置仓库用户名与邮箱；个人账号使用与该贡献者在托管服务上关联的邮箱，也可使用其选定且已验证的隐私邮箱。自动化使用明确获准的身份。不得编造占位身份或冒用他人身份；应用他人的变更时保留原作者。修正已发布元数据须获维护者授权并同步更新受影响的固定引用；除非所有者明确批准另行修复，否则保留不可变的既有发布引用。

| 类型 | 用途 |
| --- | --- |
| `feat`、`fix` | 新增行为或修复问题 |
| `refactor`、`perf`、`style` | 重构、性能优化或纯格式调整 |
| `docs`、`test` | 仅文档或仅测试变更 |
| `build`、`ci`、`chore` | 工具与依赖、[流水线](../../glossary.md#pipeline)或其他维护 |
| [`revert`](../../glossary.md#revert) | 撤销先前改动，引用其 [SHA](../../glossary.md#sha) 并说明原因 |

## 示例与流程

```text
feat(auth): support OIDC sign-in

fix(api): return a stable error for expired sessions

feat(api)!: return order identifiers as strings

BREAKING CHANGE: Consumers must parse order IDs as strings.
Refs: #123
```

暂存一个完整变更，检查暂存差异，编写消息并执行相关检查。合并前核对最终[提交信息](../../glossary.md#commit)及[变更请求](../../glossary.md#change-request)、[工作项](../../glossary.md#issue)链接。撤销时保留原提交引用；若已部署，遵循[发布规范](../04-delivery/release-standards.md)。
