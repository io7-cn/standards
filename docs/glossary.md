# 工程术语表 · Engineering glossary

[English standards](en/README.md) · [中文规范](zh-CN/README.md)

本表统一两种语言的术语、缩写和团队惯用表达。点击对照表中的术语可跳转到独立词条，查看中英解释及容易混淆的概念。

This glossary gives the preferred terms, abbreviations and shorthand used across both editions. Select a term in the comparison tables to jump to its bilingual explanation.

## 用法 · Usage

术语解释是工程文档的正式要求。参见[中文 MNT-07](zh-CN/05-maintenance/maintenance-standards.md#解释工程术语)。

Explaining terminology is a requirement for engineering documents. See [English MNT-07](en/05-maintenance/maintenance-standards.md#explain-engineering-terminology).

- 中文正文优先用表中的中文术语；读者需要识别英文缩写时，可在首次出现时并列注明。英文正文使用表中的英文术语或缩写。新增术语时先补中英文对照和解释，再在正文与模板说明中链接到词条。
- Prefer the listed term in each language. On first use, give the expansion when readers need it. Link terms in prose to their entries; leave commands, code examples and machine-readable identifiers intact.

## 治理与协作 · Governance and collaboration

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [MUST / SHOULD / MAY](#requirement-levels) | 必须／推荐／可选 |
| [Jargon / team shorthand](#jargon) | 行话／团队惯用语（也称黑话） |
| [Priority (P0–P3)](#priority) | 优先级 |
| [Repository (repo)](#repository) | 仓库 |
| [Git submodule](#git-submodule) | Git 子模块 |
| [Gitlink](#gitlink) | 子模块提交记录 |
| [Monorepo / multirepo](#repository-layout) | 单仓库／多仓库 |
| [README](#readme) | 项目说明 |
| [Code owner / maintainer](#ownership) | 代码所有者／维护者 |
| [Issue / work item](#issue) | 工作项 |
| [Acceptance criteria](#acceptance-criteria) | 验收标准 |
| [Spike / timeboxed investigation](#spike) | 限时调研 |
| [Triage](#triage) | 分诊 |
| [Backlog](#backlog) | 待办列表 |
| [Change request (PR / MR)](#change-request) | 变更请求 |
| [Code review](#code-review) | 代码审查 |
| [Stale approval](#stale-approval) | 过时审批 |
| [Gate / quality gate / required check](#gate) | 门禁／质量门禁／必过检查 |
| [Exception / waiver](#exception) | 例外／豁免 |
| [ADR — Architecture Decision Record](#adr) | 架构决策记录 |

### Requirement levels

**MUST / SHOULD / MAY · 必须／推荐／可选**

**EN:** MUST is mandatory, SHOULD is the recommended default, and MAY permits a choice. An exception to a MUST requires approval under the standards.

**中：** MUST 是强制要求，SHOULD 是建议默认做法，MAY 表示可以自行选择。偏离 MUST 须按规范审批。

### Jargon

**Jargon / team shorthand · 行话／团队惯用语**

**EN:** A word or phrase whose meaning depends on experience with a field or familiarity with a team. Explain the intended meaning where readers encounter it.

**中：** 依赖专业经验或团队背景才能理解的词语，也称黑话。使用时应说明它在当前语境中的意思。

### Priority

**Priority (P0–P3) · 优先级**

**EN:** For work items, P0 means immediate triage, P1 major impact, P2 normal delivery and P3 minor improvement. For adoption, P0 is the initial baseline and P1 is a later phase. Priority is urgency or adoption order; severity is actual impact.

**中：** 工作项中 P0 须立即分诊，P1 影响重大，P2 常规交付，P3 小改进。规范接入中 P0 是首批基线，P1 可后续引入。优先级表示紧迫性或接入次序，严重度表示实际影响。

### Repository

**Repository (repo) · 仓库**

**EN:** A versioned collection of files and history. A code hosting platform stores and exposes the repository and may provide review or automation features.

**中：** 保存版本化文件及历史的集合。代码托管平台提供仓库访问，也可能提供审查或自动化能力。

### Repository layout

**Monorepo / multirepo · 单仓库／多仓库**

**EN:** A monorepo contains multiple related components in one repository. A multirepo setup gives components or services separate repositories, usually with independent access or releases.

**中：** 单仓库将多个相关组件放在同一个仓库。多仓库将组件或服务拆到不同仓库，通常各自管理权限或发布。

### README

**README · 项目说明**

**EN:** The first document to read in a repository. It points readers to setup, verification, ownership and contribution instructions.

**中：** 项目的首读文档，指向环境配置、验证、所有权和贡献说明。

### Ownership

**Code owner / maintainer · 代码所有者／维护者**

**EN:** A code owner is accountable for a component or path; a maintainer has ongoing repository responsibilities. Ownership rules route review and can require an eligible owner's approval.

**中：** 代码所有者负责特定组件或路径；维护者承担仓库持续维护职责。所有权规则可以分配审查并要求合格所有者批准。

### Issue

**Issue / work item · 工作项**

**EN:** A tracked unit of work such as a feature, defect, maintenance task or investigation. It records scope, ownership and delivery evidence.

**中：** 用于跟踪需求、缺陷、维护或调研的记录，包含范围、责任与交付证据。

### Acceptance criteria

**Acceptance criteria · 验收标准**

**EN:** Observable conditions that show the requested outcome has been delivered. Acceptance is the decision that the evidence meets those conditions.

**中：** 证明预期结果已交付的可观察条件。验收是根据证据判断这些条件是否满足。

### Spike

**Spike / timeboxed investigation · 限时调研**

**EN:** A short investigation that reduces uncertainty and produces a decision, prototype or evidence. Its output need not be production code.

**中：** 在限定时间内澄清不确定性，产出决策、原型或证据，不一定交付生产代码。

### Triage

**Triage · 分诊**

**EN:** Classify incoming work or incidents by impact and urgency, assign an owner, and choose the next action.

**中：** 按影响和紧迫性对工作项或故障分类，明确负责人和下一步。

### Backlog

**Backlog · 待办列表**

**EN:** The ordered queue of work that has not yet been delivered. A backlog item is not necessarily ready to start.

**中：** 按优先级排列的未交付工作；进入待办并不代表已具备开工条件。

### Change request

**Change request (PR / MR) · 变更请求**

**EN:** The review record for a proposed merge. PR means Pull Request and MR means Merge Request. Both carry the diff, checks, discussion and approval history.

**中：** 拟合并变更的审查记录。PR 是 Pull Request，MR 是 Merge Request；二者都承载差异、检查、讨论及审批历史。

### Code review

**Code review · 代码审查**

**EN:** Peer examination of a proposed change and its evidence before merge. A blocking finding must be addressed or resolved through the recorded review process.

**中：** 合并前由同行检查变更与证据；阻塞意见须处理或按有记录的审查流程解决。

### Stale approval

**Stale approval · 过时审批**

**EN:** Approval that no longer applies to the version being merged, for example after a material change to the reviewed diff.

**中：** 对拟合并版本不再有效的审批，例如已审查差异发生实质变更。

### Gate

**Gate / quality gate / required check · 门禁／质量门禁／必过检查**

**EN:** A condition that must pass before merge, publication or deployment. A failing, missing or skipped required check cannot authorize the action.

**中：** 合并、发布或部署前必须满足的条件。必过检查失败、缺失或被跳过时均不可放行。

### Exception

**Exception / waiver · 例外／豁免**

**EN:** An approved, scoped and time-limited deviation from a requirement, with mitigations, ownership and a restoration plan.

**中：** 经批准的、有范围和时限的规则偏离，应记录缓解措施、责任人与恢复计划。

### ADR

**ADR — Architecture Decision Record · 架构决策记录**

**EN:** A durable record of the context, options, decision, rationale and consequences of an architecture choice. It can link to the decision that supersedes it.

**中：** 记录架构选择的背景、选项、决定、理由与后果，并可链接替代它的新决策。

## Git 与版本管理 · Git and versioning

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [Git reference (ref)](#ref) | Git 引用 |
| [Commit](#commit) | 提交 |
| [SHA — Secure Hash Algorithm; Git commit ID](#sha) | 安全散列算法；Git 提交 ID |
| [Branch](#branch) | 分支 |
| [Topic branch / short-lived branch](#topic-branch) | 工作分支／短生命周期分支 |
| [Protected branch](#protected-branch) | 保护分支 |
| [Force push / force with lease](#force-push) | 强制推送／带租约的强推 |
| [Merge commit](#merge-commit) | 合并提交 |
| [Squash merge](#squash) | 压缩合并 |
| [Rebase](#rebase) | 变基 |
| [Merge queue / merge train](#merge-queue) | 合并队列／合并列车 |
| [Backport / forward-port](#backport-and-forward-port) | 向旧版移植／向新版移植 |
| [Git tag / annotated tag](#tag) | Git 标签／附注标签 |
| [Conventional Commits](#conventional-commits) | 约定式提交 |
| [Breaking change](#breaking-change) | 破坏性变更 |
| [Git trailer / footer](#trailer) | 提交尾注 |
| [WIP — Work in Progress](#wip) | 进行中／未完成 |
| [SemVer — Semantic Versioning](#semver) | 语义化版本 |
| [Release Candidate (RC)](#release-candidate) | 候选发布版本 |
| [Release notes / changelog](#release-notes-and-changelog) | 发布说明／变更日志 |
| [Hotfix](#hotfix) | 紧急修复／热修复 |
| [Revert](#revert) | 撤销提交 |

### Ref

**Git reference (ref) · Git 引用**

**EN:** A Git name that points to an object or another ref. Branches and tags are refs; a protected ref is subject to access or update rules.

**中：** Git 中指向对象或另一个引用的名称。分支和标签都是引用；受保护引用有访问或更新约束。

### Commit

**Commit · 提交**

**EN:** A recorded Git snapshot with metadata and parent history. A commit message describes that snapshot; a commit ID identifies it.

**中：** 包含元数据和父提交历史的 Git 快照。提交消息描述快照，提交 ID 标识该快照。

### SHA

**SHA — Secure Hash Algorithm; Git commit ID · 安全散列算法；Git 提交 ID**

**EN:** SHA is a family of hash algorithms. In “source SHA,” the standards mean the Git commit object ID, using the repository's configured hash format.

**中：** SHA 是一族散列算法。“源码 SHA”在本文指 Git 提交对象 ID，采用仓库配置的散列格式。

### Branch

**Branch · 分支**

**EN:** A moving ref at the tip of a line of work. The default branch is the repository's designated starting branch; the trunk is the main line of integration.

**中：** 指向一条工作线末端、可随提交移动的引用。默认分支是仓库指定的起始分支；主干是主要集成线。

### Topic branch

**Topic branch / short-lived branch · 工作分支／短生命周期分支**

**EN:** A branch focused on one change and normally removed after merge.

**中：** 聚焦单一变更、通常在合并后删除的分支。

### Protected branch

**Protected branch · 保护分支**

**EN:** A branch with server-side constraints on pushes, merges, deletion or force pushes; the standards specify the minimum outcomes.

**中：** 服务端对推送、合并、删除或强推设置限制的分支；规范规定最低控制目标。

### Force push

**Force push / force with lease · 强制推送／带租约的强推**

**EN:** A force push can replace remote history. The lease form checks the expected remote ref before updating it; it does not make rewriting shared history routine.

**中：** 强推可能改写远端历史。带租约的形式更新前核对远端引用是否符合预期，仍不能随意改写共享历史。

### Merge commit

**Merge commit · 合并提交**

**EN:** A commit with multiple parents that preserves the ancestry of the merged lines of work.

**中：** 含多个父提交、保留合并各方祖先关系的提交。

### Squash

**Squash merge · 压缩合并**

**EN:** Combine the net effect of a topic branch into one commit on the target branch, without retaining the individual topic commits in target history.

**中：** 将工作分支的最终差异合为目标分支上的一条提交，不在目标历史保留源分支的逐条提交。

### Rebase

**Rebase · 变基**

**EN:** Replay commits onto a different base. Replayed commits generally get new IDs, so rebasing a shared branch requires coordination.

**中：** 把一组提交重新应用到另一基点。重新生成的提交通常有新 ID，共享分支变基须协调。

### Merge queue

**Merge queue / merge train · 合并队列／合并列车**

**EN:** A service that orders proposed merges and runs checks against the resulting candidate including relevant queued changes. A merged-result check evaluates a proposed merge with its target.

**中：** 按序安排拟合并变更，并对包含相关排队变更的候选运行检查。合并结果检查验证拟议变更与目标分支结合后的结果。

### Backport and forward port

**Backport / forward-port · 向旧版移植／向新版移植**

**EN:** Apply an existing fix to an older supported line (backport) or a newer line (forward-port), then verify it against that target.

**中：** 将已有修复应用到仍受支持的旧版本线或较新版本线，并针对目标验证。

### Tag

**Git tag / annotated tag · Git 标签／附注标签**

**EN:** A named Git ref commonly used to mark a release. An annotated tag has a tag object with metadata and can carry a cryptographic signature.

**中：** 常用于标记发布的 Git 命名引用。附注标签有保存元数据的标签对象，可带密码学签名。

### Conventional Commits

**Conventional Commits · 约定式提交**

**EN:** A commit message convention with a type, optional scope and description, and explicit markers for incompatible changes.

**中：** 提交消息约定，含类型、可选作用域和描述，并提供不兼容变更标记。

### Breaking change

**Breaking change · 破坏性变更**

**EN:** A change that can break supported consumers or violate a published compatibility promise. It requires migration guidance and the applicable versioning action.

**中：** 可能破坏已支持消费方或公开兼容性承诺的变更，须提供迁移说明并执行适用的版本策略。

### Trailer

**Git trailer / footer · 提交尾注**

**EN:** Structured metadata at the end of a commit message, such as an issue reference or sign-off. A sign-off is not a cryptographic signature.

**中：** 提交消息末尾的结构化元数据，如工作项引用或签署记录。签署记录不是密码学签名。

### WIP

**WIP — Work in Progress · 进行中／未完成**

**EN:** A label for unfinished work or temporary commits. A fixup is a temporary correction intended to be folded into another commit.

**中：** 表示未完成工作或临时提交。fixup 是准备折叠进另一条提交的临时修正。

### SemVer

**SemVer — Semantic Versioning · 语义化版本**

**EN:** A versioning scheme using major, minor and patch numbers, with optional prerelease and build metadata. The required increment follows the public compatibility contract.

**中：** 由主、次、补丁号组成的版本方案，可带预发布及构建元数据。按公开兼容性承诺决定升哪一位。

### Release candidate

**Release Candidate (RC) · 候选发布版本**

**EN:** A prerelease considered for stable publication after verification. An RC label is different from a generic merge candidate or an already stable release.

**中：** 经验证后可考虑正式发布的预发布版本。RC 不等于普通合并候选，也不等于已稳定发布的版本。

### Release notes and changelog

**Release notes / changelog · 发布说明／变更日志**

**EN:** Release notes explain one release's changes and upgrade impact; a changelog is a chronological record across releases.

**中：** 发布说明解释单次发布的变更与升级影响；变更日志按时间记录多个版本。

### Hotfix

**Hotfix · 紧急修复／热修复**

**EN:** An expedited correction for an urgent defect on a deployed or supported line. It still follows applicable review and immutable release controls.

**中：** 针对已部署或受支持版本紧急缺陷的加急修复，仍适用审查和不可变发布要求。

### Revert

**Revert · 撤销提交**

**EN:** Create a new commit that reverses an earlier change. Reverting source does not by itself restore a running service or its data.

**中：** 新建提交撤销之前的变更。撤销源码不会自动恢复运行服务或数据。

## 代码与质量 · Code and quality

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [UTF-8 — Unicode Transformation Format, 8-bit](#utf-8) | UTF-8 字符编码 |
| [LF — Line Feed](#lf) | LF 换行符 |
| [kebab-case / snake_case / camelCase / PascalCase](#naming-case) | 连字符命名／下划线命名／小驼峰／大驼峰 |
| [Formatter](#formatter) | 格式化器 |
| [Lint / linter](#lint) | 静态规则检查／检查工具 |
| [Static analysis](#static-analysis) | 静态分析 |
| [SDK — Software Development Kit](#sdk) | 软件开发工具包 |
| [CLI — Command-Line Interface](#cli) | 命令行接口 |
| [UI — User Interface](#ui) | 用户界面 |
| [TS — TypeScript](#ts) | TypeScript |
| [I/O — Input/Output](#io) | 输入／输出 |
| [TODO — To Do](#todo) | 待办注释 |
| [Dependency lockfile / locked install](#dependency-lock) | 依赖锁文件／锁定安装 |
| [Correlation ID](#correlation-id) | 关联 ID |
| [Backoff and jitter](#backoff-and-jitter) | 退避与随机抖动 |
| [Test fixture](#fixture) | 测试夹具 |
| [Mock / test double](#mock) | 模拟对象／测试替身 |
| [Unit test](#unit-test) | 单元测试 |
| [Integration test](#integration-test) | 集成测试 |
| [Contract test](#contract-test) | 契约测试 |
| [E2E — End to End](#e2e) | 端到端测试 |
| [Smoke test / smoke check](#smoke-test) | 冒烟测试／冒烟检查 |
| [Regression test](#regression-test) | 回归测试 |
| [Test coverage](#coverage) | 测试覆盖率 |
| [Flaky test / quarantine](#flaky-test) | 不稳定测试／隔离 |

### UTF-8

**UTF-8 — Unicode Transformation Format, 8-bit · UTF-8 字符编码**

**EN:** A Unicode encoding using one to four bytes per code point. The repository uses it without a byte order mark for Markdown.

**中：** 每个 Unicode 码点用一到四字节编码；本仓库的 Markdown 使用不带字节顺序标记的 UTF-8。

### LF

**LF — Line Feed · LF 换行符**

**EN:** The newline character used for normalized repository text. CRLF is a carriage return followed by a line feed.

**中：** 本仓库文本采用的换行字符。CRLF 是回车后接换行。

### Naming case

**kebab-case / snake_case / camelCase / PascalCase · 连字符命名／下划线命名／小驼峰／大驼峰**

**EN:** Examples: order-api, order_api, orderApi and OrderApi, respectively. Select the convention specified for the language or interface.

**中：** 示例依次为 order-api、order_api、orderApi、OrderApi；按语言或接口规定选择。

### Formatter

**Formatter · 格式化器**

**EN:** Automatically normalizes layout such as indentation or whitespace. A formatter check can verify consistency without rewriting files.

**中：** 自动规范缩进、空格等排版；格式校验可在不改写文件的情况下检查一致性。

### Lint

**Lint / linter · 静态规则检查／检查工具**

**EN:** Lint checks source against configured rules and reports style or likely defects. The program that runs these checks is a linter.

**中：** 按配置规则检查源文件，报告风格问题或潜在缺陷；执行检查的工具称为 linter。

### Static analysis

**Static analysis · 静态分析**

**EN:** Analyze source or other program representations without running the application; findings can cover correctness, quality or security.

**中：** 不运行应用程序，分析源码或其他程序表示；可检查正确性、质量或安全问题。

### SDK

**SDK — Software Development Kit · 软件开发工具包**

**EN:** A packaged toolset or library for building software or integrating with an API. A toolchain SDK and a client SDK serve different purposes.

**中：** 用于构建软件或集成 API 的工具集或库。工具链 SDK 与客户端 SDK 用途不同。

### CLI

**CLI — Command-Line Interface · 命令行接口**

**EN:** An interface for running a tool or managing a system through commands and arguments.

**中：** 通过命令与参数运行工具或管理系统的接口。

### UI

**UI — User Interface · 用户界面**

**EN:** The part of the system users interact with, such as a web or desktop interface.

**中：** 用户直接操作的部分，例如网页或桌面界面。

### TS

**TS — TypeScript · TypeScript**

**EN:** A language that adds a static type system to JavaScript and produces JavaScript output.

**中：** 为 JavaScript 添加静态类型系统、可输出 JavaScript 的语言。

### IO

**I/O — Input/Output · 输入／输出**

**EN:** Operations that interact with resources such as files, networks or databases. Use the applicable timeout and cancellation controls.

**中：** 访问文件、网络、数据库等资源的操作，应使用适用的超时与取消控制。

### TODO

**TODO — To Do · 待办注释**

**EN:** A marker for deferred work. Include a reason and a tracked issue or equivalent reference so the item can be found later.

**中：** 标注延期处理的工作，附原因及可追踪的工作项或等效引用。

### Dependency lock

**Dependency lockfile / locked install · 依赖锁文件／锁定安装**

**EN:** Records resolved dependency versions and often integrity data. Locked installation uses those resolutions and rejects unexpected drift.

**中：** 记录已解析的依赖版本，通常也含完整性信息。锁定安装使用已记录结果，并拒绝意外漂移。

### Correlation ID

**Correlation ID · 关联 ID**

**EN:** An identifier carried through related events so logs, errors or requests can be connected during diagnosis. Do not put secrets into it.

**中：** 随相关事件传递的标识，便于诊断时串联日志、错误或请求；不得写入密钥。

### Backoff and jitter

**Backoff and jitter · 退避与随机抖动**

**EN:** Backoff spaces retries farther apart; jitter varies their timing so many clients do not retry together.

**中：** 退避拉长重试间隔，随机抖动打散重试时间，避免大量客户端同步重试。

### Fixture

**Test fixture · 测试夹具**

**EN:** Reusable test setup, such as known state, input files or data. It should support isolated, repeatable tests.

**中：** 可复用的测试准备，例如已知状态、输入文件或数据，应支持隔离和可重复的测试。

### Mock

**Mock / test double · 模拟对象／测试替身**

**EN:** A test substitute for a dependency. A mock can verify expected interactions but does not prove the real dependency behaves the same way.

**中：** 测试中代替真实依赖的对象。Mock 可验证预期交互，但无法证明真实依赖具有相同行为。

### Unit test

**Unit test · 单元测试**

**EN:** Exercises a small unit of logic in isolation, such as a transformation or domain invariant.

**中：** 隔离验证小范围逻辑，例如数据转换或领域不变量。

### Integration test

**Integration test · 集成测试**

**EN:** Exercises interaction between components, often using representative external systems such as the actual database engine.

**中：** 验证组件间交互，通常使用代表性的外部系统，例如实际数据库引擎。

### Contract test

**Contract test · 契约测试**

**EN:** Checks that a producer and consumer agree on observable interface behavior, such as request and response shapes or status codes.

**中：** 核对提供方和消费方是否遵循一致的接口行为，例如请求／响应结构和状态码。

### E2E

**E2E — End to End · 端到端测试**

**EN:** Exercises a complete user or system journey across the integrated stack. A smoke check is narrower and faster.

**中：** 在已集成的技术栈中验证完整用户或系统流程；冒烟检查范围更窄、速度更快。

### Smoke test

**Smoke test / smoke check · 冒烟测试／冒烟检查**

**EN:** A short check of critical functions or deployment readiness. Passing it does not establish comprehensive correctness.

**中：** 快速检查关键功能或部署就绪状态；通过不代表已全面验证。

### Regression test

**Regression test · 回归测试**

**EN:** Verifies that a previously working behavior remains correct or that a fixed defect does not recur.

**中：** 验证原有行为未退化，或已经修复的缺陷不再出现。

### Coverage

**Test coverage · 测试覆盖率**

**EN:** A measurement of exercised code or behavior, such as statements, branches or changed lines. A high number is not proof of useful assertions.

**中：** 衡量已执行的代码或行为，例如语句、分支或变更行。数值高不能证明断言有效。

### Flaky test

**Flaky test / quarantine · 不稳定测试／隔离**

**EN:** A test that passes and fails under unchanged relevant inputs or code. Quarantine is temporary isolation with ownership and replacement evidence as needed.

**中：** 相关输入和代码不变，却时而通过、时而失败的测试。隔离是临时措施，须指定负责人并按需提供替代证据。

## 交付与安全 · Delivery and security

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [CI/CD — Continuous Integration and Continuous Delivery or Deployment](#ci-cd) | 持续集成与持续交付／持续部署 |
| [Pipeline / workflow](#pipeline) | 流水线／工作流 |
| [Runner / CI executor](#runner) | 运行器／CI 执行环境 |
| [Build artifact / immutable artifact](#artifact) | 构建制品／不可变制品 |
| [Artifact registry](#registry) | 制品库 |
| [Digest / checksum](#digest) | 摘要／校验和 |
| [Pinning](#pinning) | 固定版本／固定引用 |
| [Deployment environment](#environment) | 部署环境 |
| [Artifact promotion](#promotion) | 制品晋级 |
| [Desired state](#desired-state) | 期望状态 |
| [Deployment manifest](#manifest) | 部署清单 |
| [Rollout](#rollout) | 上线／部署展开 |
| [Rollback](#rollback) | 回滚 |
| [Roll forward / forward fix](#roll-forward) | 向前修复 |
| [Health check / readiness check](#health-and-readiness) | 健康检查／就绪检查 |
| [RBAC — Role-Based Access Control](#rbac) | 基于角色的访问控制 |
| [Least privilege](#least-privilege) | 最小权限 |
| [Secret / credential](#secret) | 密钥／凭据 |
| [Secret detection / secret scanning](#secret-detection) | 密钥检测／密钥扫描 |
| [Workload identity](#workload-identity) | 工作负载身份 |
| [SAST — Static Application Security Testing](#sast) | 静态应用安全测试 |
| [Dependency scanning](#dependency-scanning) | 依赖扫描 |
| [SBOM — Software Bill of Materials](#sbom) | 软件物料清单 |
| [Build provenance](#provenance) | 构建来源证明 |
| [TLS — Transport Layer Security](#tls) | 传输层安全协议 |
| [Authentication / authorization](#authentication-and-authorization) | 认证／授权 |
| [OIDC — OpenID Connect](#oidc) | OpenID Connect 身份认证协议 |
| [Tenant isolation](#tenant-isolation) | 租户隔离 |

### CI CD

**CI/CD — Continuous Integration and Continuous Delivery or Deployment · 持续集成与持续交付／持续部署**

**EN:** CI integrates and verifies changes frequently. Continuous delivery keeps changes ready for release; continuous deployment automatically deploys eligible changes. CD can mean either; production authorization still applies.

**中：** CI 持续集成并验证变更。持续交付保持随时可发布；持续部署自动上线符合条件的变更。CD 可指两者之一，生产授权要求仍适用。

### Pipeline

**Pipeline / workflow · 流水线／工作流**

**EN:** An automated sequence or graph of jobs. A job performs a unit of work, and a stage groups related jobs.

**中：** 由多个作业组成的自动化序列或依赖图。作业执行一个工作单元，阶段用于组织相关作业。

### Runner

**Runner / CI executor · 运行器／CI 执行环境**

**EN:** The worker or environment that runs a CI job. Its trust level determines what credentials, caches and networks it may access.

**中：** 执行 CI 作业的工作进程或环境；信任等级决定可访问的凭据、缓存和网络。

### Artifact

**Build artifact / immutable artifact · 构建制品／不可变制品**

**EN:** An output from a build, such as a package or image. An immutable artifact has a fixed identity and must not be replaced in place.

**中：** 构建的产物，例如软件包或镜像。不可变制品身份固定，不得原地覆盖。

### Registry

**Artifact registry · 制品库**

**EN:** A service for storing and retrieving versioned packages or container images. Access and retention are managed by policy.

**中：** 存储和拉取带版本软件包或容器镜像的服务，按政策管理访问与保留。

### Digest

**Digest / checksum · 摘要／校验和**

**EN:** A digest is computed from content and can identify a specific image manifest or artifact. A checksum validates expected bytes; neither alone proves who built or approved the artifact.

**中：** 摘要由内容计算，可标识确定的镜像清单或制品。校验和用于核对字节是否符合预期；二者都不能单独证明构建者或审批者。

### Pinning

**Pinning · 固定版本／固定引用**

**EN:** Choose an explicit reviewed version, commit or digest instead of following a moving reference. A digest or commit fixes identity more strongly than a movable tag.

**中：** 选择经审查的明确版本、提交或摘要，而非跟随可移动引用。摘要或提交比可移动标签更可靠地固定身份。

### Environment

**Deployment environment · 部署环境**

**EN:** A target with its own configuration, credentials and access. Preproduction is a production-like target for checks before a production rollout.

**中：** 具有独立配置、凭据和访问权限的部署目标；预生产模拟生产，用于上线前验证。

### Promotion

**Artifact promotion · 制品晋级**

**EN:** Approve an already built artifact for the next environment using the same immutable identity. It does not mean rebuilding for that environment.

**中：** 批准已构建制品进入下一环境，并保持同一不可变身份；不会为该环境重新构建。

### Desired state

**Desired state · 期望状态**

**EN:** A reviewed declaration of how a service should run. Compare it with observed state, then reconcile differences through the authorized deployment process.

**中：** 经过审查的运行状态声明。与实际观测状态对比后，通过授权部署流程消除差异。

### Manifest

**Deployment manifest · 部署清单**

**EN:** A versioned declaration of deployment inputs such as image identity, configuration and resources. Other contexts may use manifest for package metadata.

**中：** 以版本管理记录部署输入，例如镜像身份、配置及资源；软件包上下文中的 manifest 也可指包元数据。

### Rollout

**Rollout · 上线／部署展开**

**EN:** The process of applying a new version or configuration to a target. Confirm its health and actual revision after rollout.

**中：** 向部署目标应用新版本或配置的过程；完成后核对健康状态与实际版本。

### Rollback

**Rollback · 回滚**

**EN:** Restore a previously verified compatible artifact and configuration. Check data and schema compatibility before doing so.

**中：** 恢复到先前验证过且仍兼容的制品与配置；执行前核对数据和 Schema 兼容性。

### Roll forward

**Roll forward / forward fix · 向前修复**

**EN:** Recover by applying a new corrective change instead of restoring the previous release, often because existing data cannot safely go back.

**中：** 通过发布新修正恢复，而非恢复旧版本；常见原因是现有数据无法安全退回。

### Health and readiness

**Health check / readiness check · 健康检查／就绪检查**

**EN:** A health check probes operating condition. Readiness asks whether an instance can receive traffic now; it is distinct from liveness.

**中：** 健康检查探测运行状况；就绪检查关注实例当前能否接流量，与存活检查不同。

### RBAC

**RBAC — Role-Based Access Control · 基于角色的访问控制**

**EN:** Assign permissions to roles and grant roles to actors. This is one way to enforce scoped access and least privilege.

**中：** 权限赋予角色，角色再授予主体；这是实现限域访问和最小权限的一种方式。

### Least privilege

**Least privilege · 最小权限**

**EN:** Give a person or workload only the access needed for the authorized task, for only as long as needed.

**中：** 仅授予人员或工作负载执行已授权任务所需的权限，并限制有效时间。

### Secret

**Secret / credential · 密钥／凭据**

**EN:** Sensitive material used to prove identity or obtain access, such as a password, token or private key. Keep it out of tracked files, logs and artifacts.

**中：** 用于证明身份或获取访问权的敏感材料，例如密码、令牌或私钥。不得写入跟踪文件、日志和制品。

### Secret detection

**Secret detection / secret scanning · 密钥检测／密钥扫描**

**EN:** Searches for exposed credential patterns or known secret material. Treat a confirmed exposure as requiring revocation or rotation, not merely removal from text.

**中：** 搜索暴露的凭据特征或已知密钥材料。确认暴露后需撤销或轮换，仅删除文本不够。

### Workload identity

**Workload identity · 工作负载身份**

**EN:** An identity assigned to a process, job or service. It can be used to obtain scoped and often short-lived credentials.

**中：** 分配给进程、作业或服务的身份，可用于取得限域且通常短期有效的凭据。

### SAST

**SAST — Static Application Security Testing · 静态应用安全测试**

**EN:** Finds potential security flaws by analyzing source, bytecode or binaries without executing the application.

**中：** 不运行应用，通过分析源码、字节码或二进制产物发现潜在安全缺陷。

### Dependency scanning

**Dependency scanning · 依赖扫描**

**EN:** Checks resolved components against known vulnerabilities and applicable policy, including transitive dependencies where available.

**中：** 按已知漏洞及适用政策检查解析后的组件，尽可能覆盖传递依赖。

### SBOM

**SBOM — Software Bill of Materials · 软件物料清单**

**EN:** A structured inventory of software components and versions in an artifact. It supports vulnerability and license review but does not prove build origin.

**中：** 制品内软件组件与版本的结构化清单，用于漏洞和许可证检查，不能单独证明构建来源。

### Provenance

**Build provenance · 构建来源证明**

**EN:** Verifiable information linking an artifact to its builder, source and build inputs or process. It answers where and how the artifact was produced.

**中：** 将制品关联到构建者、源码及构建输入或过程的可验证信息，说明产物从哪里、如何生成。

### TLS

**TLS — Transport Layer Security · 传输层安全协议**

**EN:** Protects data in transit and authenticates peers according to how certificates and validation are configured. HTTPS uses TLS.

**中：** 保护传输中的数据，并按证书及校验配置认证通信对端。HTTPS 使用 TLS。

### Authentication and authorization

**Authentication / authorization · 认证／授权**

**EN:** Authentication establishes who the caller is. Authorization decides what that caller can do or access.

**中：** 认证确定调用者是谁；授权决定调用者能操作或访问什么。

### OIDC

**OIDC — OpenID Connect · OpenID Connect 身份认证协议**

**EN:** An identity layer built on OAuth 2.0. It lets an application authenticate a user and receive identity claims; OAuth 2.0 alone is an authorization framework.

**中：** 建立在 OAuth 2.0 上的身份层，让应用认证用户并获取身份声明；OAuth 2.0 本身是授权框架。

### Tenant isolation

**Tenant isolation · 租户隔离**

**EN:** Prevents one tenant from accessing another tenant's data or capabilities, including indirect access through identifiers, logs and jobs.

**中：** 阻止一个租户访问另一租户的数据或能力，也要防止通过标识、日志和作业间接访问。

## 接口与数据 · Interfaces and data

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [API — Application Programming Interface](#api) | 应用程序编程接口 |
| [Interface contract](#contract) | 接口契约 |
| [Schema](#schema) | 模式／结构定义 |
| [REST — Representational State Transfer](#rest) | 表述性状态转移 |
| [HTTP — Hypertext Transfer Protocol](#http) | 超文本传输协议 |
| [RFC — Request for Comments](#rfc) | 互联网技术文档编号体系 |
| [OpenAPI Specification](#openapi) | OpenAPI 接口描述规范 |
| [RPC — Remote Procedure Call](#rpc) | 远程过程调用 |
| [gRPC](#grpc) | gRPC 远程调用框架 |
| [Protocol Buffers (Protobuf)](#protobuf) | 协议缓冲区 |
| [Pagination](#pagination) | 分页 |
| [Rate limit](#rate-limit) | 限流 |
| [Idempotency / idempotency key](#idempotency) | 幂等／幂等键 |
| [SQL — Structured Query Language](#sql) | 结构化查询语言 |
| [EF Core — Entity Framework Core](#ef-core) | Entity Framework Core 数据访问框架 |
| [Primary key](#primary-key) | 主键 |
| [Database transaction](#transaction) | 数据库事务 |
| [Schema or data migration](#migration) | 结构迁移／数据迁移 |
| [Backfill](#backfill) | 回填 |
| [Expand and contract](#expand-and-contract) | 先扩展后收紧 |
| [UTC — Coordinated Universal Time](#utc) | 协调世界时 |
| [ID — Identifier](#id) | 标识符 |

### API

**API — Application Programming Interface · 应用程序编程接口**

**EN:** A defined boundary through which one program uses another component or service. Its contract covers inputs, outputs, errors and compatibility.

**中：** 程序调用另一组件或服务的约定边界，契约包括输入、输出、错误及兼容性。

### Contract

**Interface contract · 接口契约**

**EN:** The agreed observable behavior of an interface. A schema describes shape; semantics, errors, timing and compatibility can also be part of the contract.

**中：** 接口可观察行为的约定。Schema 描述结构；语义、错误、时序和兼容性也可属于契约。

### Schema

**Schema · 模式／结构定义**

**EN:** A formal description of data shape and constraints. An API schema specifies message structure; a database schema defines structures such as tables, indexes and constraints.

**中：** 对数据结构与约束的正式描述。API Schema 规定消息结构；数据库 Schema 定义表、索引与约束等。

### REST

**REST — Representational State Transfer · 表述性状态转移**

**EN:** An architectural style for distributed systems. In this standard, REST APIs model resources and use HTTP methods, status codes and representations consistently.

**中：** 一种分布式系统架构风格；本文中的 REST API 以资源建模，并一致使用 HTTP 方法、状态码与资源表示。

### HTTP

**HTTP — Hypertext Transfer Protocol · 超文本传输协议**

**EN:** The application protocol for requests and responses on the web. Methods such as GET describe intent; status codes describe the result.

**中：** Web 请求与响应的应用层协议。GET 等方法描述意图，状态码描述结果。

### RFC

**RFC — Request for Comments · 互联网技术文档编号体系**

**EN:** RFCs are numbered publications; not every RFC is a standard. RFC 9457 defines a structured HTTP problem-details format for communicating API errors.

**中：** RFC 是带编号的出版物，并非每篇都是标准。RFC 9457 定义了表达 API 错误的 HTTP 问题详情结构。

### OpenAPI

**OpenAPI Specification · OpenAPI 接口描述规范**

**EN:** A language-independent description of HTTP APIs, usable for documentation, validation, compatibility checks and client generation.

**中：** 与编程语言无关的 HTTP API 描述格式，可用于文档、校验、兼容性检查及客户端生成。

### RPC

**RPC — Remote Procedure Call · 远程过程调用**

**EN:** A client invokes a named operation provided by another process or service using an agreed request and response contract.

**中：** 客户端按约定的请求与响应契约调用另一进程或服务提供的命名操作。

### gRPC

**gRPC · gRPC 远程调用框架**

**EN:** A remote-call framework commonly using HTTP/2 and Protocol Buffers to describe services and exchange messages. It has its own canonical status codes.

**中：** 远程调用框架，通常用 HTTP/2 和 Protocol Buffers 描述服务及交换消息，并有自己的标准状态码。

### Protobuf

**Protocol Buffers (Protobuf) · 协议缓冲区**

**EN:** A schema language and serialization format that identifies fields by number. Reserve deleted field names and numbers to avoid accidental reuse.

**中：** 一种 Schema 语言及序列化格式，按编号标识字段；应保留已删除字段的名称和编号，防止被误用。

### Pagination

**Pagination · 分页**

**EN:** Returns a bounded subset of a collection per request, with stable ordering and a mechanism for continuing to the next page.

**中：** 每次请求返回集合中有上限的一部分，保证稳定排序并提供继续读取下一页的机制。

### Rate limit

**Rate limit · 限流**

**EN:** A bound on requests or operations over a period. Clients can use documented retry signals and a total retry budget.

**中：** 对一段时间内请求或操作数量的限制。客户端可依据已记录的重试信号与总预算处理。

### Idempotency

**Idempotency / idempotency key · 幂等／幂等键**

**EN:** Repeating an operation leaves the same intended effect as applying it once. An idempotency key lets the server recognize a retry of the same logical write.

**中：** 重复执行与执行一次的预期效果相同。幂等键让服务端识别同一逻辑写入的重试。

### SQL

**SQL — Structured Query Language · 结构化查询语言**

**EN:** A language for defining, querying and modifying data in relational database systems.

**中：** 用于在关系型数据库中定义结构、查询和修改数据的语言。

### EF Core

**EF Core — Entity Framework Core · Entity Framework Core 数据访问框架**

**EN:** A .NET object-relational mapper that maps application models to data stores and provides schema migration tooling.

**中：** .NET 对象关系映射框架，将应用模型映射到数据存储，并提供 Schema 迁移工具。

### Primary key

**Primary key · 主键**

**EN:** The column or column set that uniquely identifies each table row. A foreign key constrains references to another key.

**中：** 唯一标识表中一行的列或列组合。外键限制对另一键的引用。

### Transaction

**Database transaction · 数据库事务**

**EN:** A group of operations whose changes commit together or are rolled back together. Isolation governs how concurrent transactions interact.

**中：** 一组一起提交或回滚的操作；隔离规则决定并发事务之间如何相互影响。

### Migration

**Schema or data migration · 结构迁移／数据迁移**

**EN:** A controlled change to database structures or existing data. Rehearse it with representative data and plan verification and recovery.

**中：** 对数据库结构或现有数据的受控更改。用代表性数据演练，并计划验证及恢复。

### Backfill

**Backfill · 回填**

**EN:** Populate new or derived values for existing records. A safe backfill preserves identities, can resume if interrupted, and verifies row counts or invariants.

**中：** 为既有记录填充新字段或派生值。安全回填保留身份，支持中断续跑，并核对行数或不变量。

### Expand and contract

**Expand and contract · 先扩展后收紧**

**EN:** Introduce a compatible structure, upgrade readers and writers, backfill and verify, then remove old structure or enforce tighter constraints after the compatibility window.

**中：** 先引入兼容结构，升级读写方、回填和验证，再在兼容窗口结束后移除旧结构或收紧约束。

### UTC

**UTC — Coordinated Universal Time · 协调世界时**

**EN:** A common time reference for recording and comparing instants. Preserve the original business time zone separately where it affects interpretation.

**中：** 记录及比较时间点的通用时间基准。业务时区影响解释时应另外保存。

### ID

**ID — Identifier · 标识符**

**EN:** A value that identifies an object, record or event within a defined scope. IDs can be opaque; their serialization is part of a public contract when exposed.

**中：** 在约定范围内标识对象、记录或事件的值。ID 可以不携带业务含义，对外暴露时其序列化方式属于公开契约。

## 运维与维护 · Operations and maintenance

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [Observability](#observability) | 可观测性 |
| [Runbook](#runbook) | 运维操作手册 |
| [On-call](#on-call) | 值班 |
| [Incident commander](#incident-commander) | 故障指挥人 |
| [Blameless incident review / postmortem](#incident-review) | 非追责故障复盘 |
| [RPO — Recovery Point Objective](#rpo) | 恢复点目标 |
| [RTO — Recovery Time Objective](#rto) | 恢复时间目标 |
| [Deprecation](#deprecation) | 弃用 |
| [Technical debt](#technical-debt) | 技术债 |

### Observability

**Observability · 可观测性**

**EN:** The ability to investigate system behavior from signals such as logs, metrics and traces. It supports diagnosis beyond known alert conditions.

**中：** 通过日志、指标、链路追踪等信号理解系统行为，可用于排查未被预设告警覆盖的问题。

### Runbook

**Runbook · 运维操作手册**

**EN:** A step-by-step guide for operating or recovering a service, including escalation, safe commands and checks that confirm the result.

**中：** 用于运维或恢复服务的分步操作说明，含升级联络、安全命令及结果核验。

### On call

**On-call · 值班**

**EN:** The person or rotation responsible for responding to alerts and incidents within an agreed scope and time.

**中：** 在约定范围和时间内负责响应告警与故障的人员或轮值机制。

### Incident commander

**Incident commander · 故障指挥人**

**EN:** Coordinates incident response, assigns responsibilities and keeps decisions and communication aligned until recovery or handoff.

**中：** 协调故障响应、分配职责，并保持决策与沟通一致，直至恢复或交接。

### Incident review

**Blameless incident review / postmortem · 非追责故障复盘**

**EN:** An evidence-based review of impact, timeline and contributing factors. It assigns preventive actions without blaming individuals for systemic conditions.

**中：** 基于证据回顾影响、时间线与促成因素，并分配预防行动，不把系统性条件归咎于个人。

### RPO

**RPO — Recovery Point Objective · 恢复点目标**

**EN:** The maximum acceptable data loss expressed as a time interval. For example, an RPO of 15 minutes means recovery should not lose more than 15 minutes of updates.

**中：** 用时间间隔表示的最大可接受数据损失。例如 RPO 为 15 分钟，表示恢复后丢失的更新不得超过 15 分钟。

### RTO

**RTO — Recovery Time Objective · 恢复时间目标**

**EN:** The target elapsed time to restore a service to an agreed usable state after disruption. Measure the whole recovery procedure, not just data restoration.

**中：** 服务中断后恢复至约定可用状态的目标耗时。应测量完整恢复流程，而不只是数据恢复步骤。

### Deprecation

**Deprecation · 弃用**

**EN:** A documented warning that a supported feature is planned for retirement. Provide a replacement and migration window before removing it.

**中：** 声明某项受支持功能计划退役；移除前应提供替代项及迁移窗口。

### Technical debt

**Technical debt · 技术债**

**EN:** An existing design or implementation tradeoff that increases the cost or risk of future work. Track its impact, owner and remediation.

**中：** 已经作出的设计或实现权衡，增加未来工作成本或风险。记录影响、负责人及处理计划。

## 补充交付术语 · Product delivery terms

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [Release / deployment](#release-and-deployment) | 发布／部署 |
| [Container image / base image](#container-image) | 容器镜像／基础镜像 |
| [Kubernetes (K8s)](#kubernetes) | Kubernetes 容器编排系统 |
| [Compose](#compose) | Compose 多容器应用配置 |
| [Feature flag](#feature-flag) | 功能开关 |
| [Telemetry](#telemetry) | 遥测 |

### Release and deployment

**Release / deployment · 发布／部署**

**EN:** Release makes a version available to its audience, for example in a registry. Deployment installs or updates an artifact in an environment. A released version may not be deployed yet.

**中：** 发布让目标用户可以取得版本，例如发布到制品库；部署将制品安装或更新到某环境。已发布的版本不一定已经部署。

### Container image

**Container image / base image · 容器镜像／基础镜像**

**EN:** A packaged filesystem and configuration for creating containers. A base image is an input to building another image; a tag can move while a digest identifies specific content.

**中：** 用于创建容器的文件系统与配置包。基础镜像是构建其他镜像的输入；标签可能变动，摘要标识确定内容。

### Kubernetes

**Kubernetes (K8s) · Kubernetes 容器编排系统**

**EN:** A platform for declaring, deploying and operating containerized workloads. The standards also permit equivalent deployment workflows.

**中：** 用于声明、部署和运维容器化工作负载的平台。规范也允许使用等效部署流程。

### Compose

**Compose · Compose 多容器应用配置**

**EN:** A way to describe services, networks and volumes for a multi-container application using a declarative file.

**中：** 通过声明式文件描述多容器应用中的服务、网络和卷。

### Feature flag

**Feature flag · 功能开关**

**EN:** A control that changes whether a feature is active without rebuilding. Assign an owner and retire temporary flags after rollout.

**中：** 不重新构建即可改变功能启用状态的控制项。为开关指定责任人，上线后清理临时开关。

### Telemetry

**Telemetry · 遥测**

**EN:** Operational signals emitted for collection and analysis, such as logs, metrics and traces. They must not carry unauthorized sensitive data.

**中：** 为收集和分析而输出的运行信号，如日志、指标和链路追踪，不得包含未经授权的敏感数据。

## 技术栈 · Technology stack

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [ASP.NET Core](#asp-net-core) | ASP.NET Core 应用框架 |
| [Blazor](#blazor) | Blazor 组件框架 |
| [Component library](#component-library) | 组件库 |
| [CSS — Cascading Style Sheets](#css) | 层叠样式表 |
| [Design token](#design-token) | 设计变量 |
| [Layered architecture](#layered-architecture) | 分层架构 |
| [Node.js](#node-js) | Node.js 运行时 |
| [NOF](#nof) | NOF 应用框架 |
| [NuGet](#nuget) | NuGet 包管理 |
| [Nullable reference types](#nullable-reference-types) | 可空引用类型 |
| [PostgreSQL](#postgresql) | PostgreSQL 关系型数据库 |
| [React](#react) | React 界面库 |
| [Vite](#vite) | Vite 前端构建工具 |
| [Vue](#vue) | Vue 前端框架 |

### ASP NET Core

**ASP.NET Core · ASP.NET Core 应用框架**

**EN:** The .NET framework used to host web applications and network services. It provides request handling, configuration and service registration.

**中：** 用于托管 Web 应用和网络服务的 .NET 框架，提供请求处理、配置与服务注册。

### Blazor

**Blazor · Blazor 组件框架**

**EN:** A .NET framework for building interactive web interfaces from Razor components. A matching `.razor.css` file scopes selectors to the owning component's rendered markup.

**中：** 使用 Razor 组件构建交互式 Web 界面的 .NET 框架。配套的 `.razor.css` 将选择器作用域限定到所属组件渲染的标记。

### Component library

**Component library · 组件库**

**EN:** A set of reusable interface components with common behavior and theme settings. MudBlazor and Ant Design Blazor are examples for Blazor.

**中：** 共享行为与主题设置的一组可复用界面组件。MudBlazor 和 Ant Design Blazor 是 Blazor 组件库示例。

### CSS

**CSS — Cascading Style Sheets · 层叠样式表**

**EN:** The language for web presentation, including layout, typography and responsive behavior. Scoping keeps a selector within its intended component or feature.

**中：** 描述 Web 界面布局、排版和响应式表现的语言。样式隔离将选择器限定在预期组件或功能范围内。

### Design token

**Design token · 设计变量**

**EN:** A named design value such as a color, spacing or type size. Web themes often expose tokens as CSS custom properties so components share the same values.

**中：** 为颜色、间距或字号等设计值设置的名称。Web 主题常用 CSS 自定义属性提供这些值，供组件复用。

### Layered architecture

**Layered architecture · 分层架构**

**EN:** Organizes code by responsibility. Business rules, use case orchestration, external contracts and runtime wiring have defined boundaries and dependency directions.

**中：** 按职责组织代码，为业务规则、用例编排、对外契约和运行时装配划定边界，并约定依赖方向。

### Node js

**Node.js · Node.js 运行时**

**EN:** A JavaScript runtime used outside the browser. Frontend and library projects use it to run package management, builds and checks.

**中：** 在浏览器之外运行 JavaScript 的运行时。前端和软件库项目常用它执行包管理、构建及检查。

### NOF

**NOF · NOF 应用框架**

**EN:** A .NET application framework that provides facilities such as request handling, remote-call contracts, generated clients and host integration.

**中：** 提供请求处理、远程调用契约、客户端生成与宿主集成等能力的 .NET 应用框架。

### NuGet

**NuGet · NuGet 包管理**

**EN:** The .NET package management system. Multi-project repositories can declare common versions in `Directory.Packages.props`.

**中：** 用于 .NET 的包管理系统。多项目仓库可在 `Directory.Packages.props` 中集中声明共用版本。

### Nullable reference types

**Nullable reference types · 可空引用类型**

**EN:** C# annotations and compiler analysis for whether a reference can be null. The analysis helps catch unsafe usage before runtime.

**中：** C# 用于标记引用是否可能为空并据此进行分析的机制，可在编译时发现不安全的用法。

### PostgreSQL

**PostgreSQL · PostgreSQL 关系型数据库**

**EN:** A relational database system. When a service uses it in production, verify database-specific behavior with the same database engine.

**中：** 关系型数据库系统。生产服务使用 PostgreSQL 时，依赖该数据库特性的行为应在同一数据库引擎上验证。

### React

**React · React 界面库**

**EN:** A JavaScript library for building user interfaces from components. React projects choose their own styling and build tools.

**中：** 用组件构建用户界面的 JavaScript 库。React 项目按需要选择样式方案与构建工具。

### Vite

**Vite · Vite 前端构建工具**

**EN:** A development server and build tool for web projects. Run the project's separate type checks when the Vite build does not perform them.

**中：** 面向 Web 项目的开发服务器及构建工具。如果 Vite 构建流程没有检查类型，则需另行运行项目的类型检查。

### Vue

**Vue · Vue 前端框架**

**EN:** A framework for building user interfaces with components and reactive state.

**中：** 通过组件和响应式状态构建用户界面的前端框架。

## 编码工具与写法 · Coding tools and conventions

| English term / abbreviation | 中文规范用语 |
| --- | --- |
| [EditorConfig](#editorconfig) | 编辑器配置规范 |
| [Prettier](#prettier) | Prettier 格式化工具 |
| [Stylelint](#stylelint) | Stylelint 样式检查工具 |
| [JSX](#jsx) | JavaScript 语法扩展 |
| [React hook](#react-hook) | React Hook（钩子） |
| [CSS Modules](#css-modules) | CSS 模块化样式 |
| [Vue single-file component (SFC)](#vue-single-file-component) | Vue 单文件组件 |
| [Vue composable](#vue-composable) | Vue 组合式函数 |

### EditorConfig

**EditorConfig · 编辑器配置规范**

**EN:** A file-based convention for sharing text and formatting settings across editors. Language tools may recognize additional keys, so run the repository's checks to enforce its rules.

**中：** 通过配置文件跨编辑器共享文本与格式规则的规范。语言工具还可能识别扩展键，仓库应运行实际检查来执行规则。

### Prettier

**Prettier · Prettier 格式化工具**

**EN:** A formatter for languages including TypeScript, JavaScript and CSS. Its configuration fixes formatting choices such as quotes and wrapping.

**中：** 用于 TypeScript、JavaScript 和 CSS 等语言的格式化工具。通过配置统一引号、换行等排版取值。

### Stylelint

**Stylelint · Stylelint 样式检查工具**

**EN:** A configurable checker for stylesheet rules such as class naming and declaration restrictions.

**中：** 可配置的样式表检查工具，可检查类名及声明限制等规则。

### JSX

**JSX · JavaScript 语法扩展**

**EN:** Markup-like syntax used to declare interface elements in JavaScript. TypeScript files using it typically have the .tsx extension.

**中：** 在 JavaScript 中以类似标记的语法声明界面元素。使用该语法的 TypeScript 文件通常采用 .tsx 扩展名。

### React hook

**React hook · React Hook（钩子）**

**EN:** A function that uses React features such as component state or effects. Custom hooks follow React's calling conventions and start with use.

**中：** 使用组件状态或副作用等 React 特性的函数。自定义 Hook 遵循 React 的调用约定，名称以 use 开头。

### CSS Modules

**CSS Modules · CSS 模块化样式**

**EN:** A build-tool mechanism that scopes class names to a stylesheet and exposes their generated names through imports.

**中：** 由构建工具将类名限定在样式文件内，并通过导入提供生成后类名的机制。

### Vue single-file component

**Vue single-file component (SFC) · Vue 单文件组件**

**EN:** A `.vue` file that groups a component's script, template and optional styles. Use `<style scoped>` to scope styles to the component. [Vue single-file components](https://vuejs.org/guide/scaling-up/sfc.html)

**中：** 在一个 `.vue` 文件中组织组件脚本、模板和可选样式。用 `<style scoped>` 将样式作用域限制在组件内。[Vue 单文件组件](https://cn.vuejs.org/guide/scaling-up/sfc.html)

### Vue composable

**Vue composable · Vue 组合式函数**

**EN:** A function that uses Vue's component composition features to encapsulate and reuse stateful logic. Give it a descriptive name beginning with `use`.

**中：** 使用 Vue 的组件组合能力封装并复用有状态逻辑的函数。名称以 `use` 开头，并说明其用途。

## 参考资料 · References

[Git glossary](https://git-scm.com/docs/gitglossary) · [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) · [Semantic Versioning](https://semver.org/spec/v2.0.0.html) · [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) · [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) · [SLSA provenance](https://slsa.dev/spec/v1.1/provenance)

### Git submodule

**Git submodule · Git 子模块**

**EN:** A separate Git repository included at a path in a parent repository. The parent records an exact child commit; initializing it checks out that recorded commit rather than the latest branch. Updates require changing the parent’s recorded commit.

**中：** 放在父仓库某个路径下的独立 Git 仓库。父仓库记录子仓库的确切提交，初始化时检出该提交而非最新分支；升级须改变父仓库记录的提交。

### Gitlink

**Gitlink · 子模块提交记录**

**EN:** A Git tree entry with mode 160000 that records the exact submodule commit. It identifies the adopted revision independently of branches or tags.

**中：** 模式为 160000 的 Git 树条目，用于记录子模块的确切提交；它独立于分支或标签标识采用的版本。
