# 接入与更新规范

[规范目录](README.md) · [English](../en/adopting-standards.md)

项目维护者负责采用的规范版本与适用配置。[Git 子模块](../glossary.md#git-submodule)使规范保留在独立仓库，父仓库记录一个确切提交；该提交才是当前生效版本，上游最新分支不会自动替换它。规范仓库自身不添加指向自身的子模块。

将获准的规范仓库添加到 .standards/，然后选择经过审查的完整提交。替换下方虚构地址及提交占位符，不在 .gitmodules 中配置分支跟踪。

```sh
git submodule add --name standards https://code.example.com/example/standards.git .standards
git -C .standards checkout --detach <reviewed-full-commit>
git add .gitmodules .standards
```

在 AGENTS.md 添加直接指向英文入口的链接，项目文档提供两种语言的入口，并在其附近记录项目所有者、工具链、适用控制与获准例外，不复制共享规范正文。

```md
- Follow the [English development standards](.standards/docs/en/README.md).
- Follow the [Git branching standards](.standards/docs/en/02-development/git-branching.md) before editing. Check the branch and working tree, use a compliant topic branch, and merge only through a change request with required checks and approvals. Do not edit, commit or push directly on protected branches; administrator access and passing tests do not waive this workflow.
```

可使用[纯英文 AGENTS.md 模板](../../templates/repository/AGENTS.md)作为起点。接入检查要求同时直接链接英文入口及 Git 分支模块。升级到此要求时，在更新规范固定提交的同一变更中更新父仓库 AGENTS.md。

克隆时包含子模块，或初始化既有检出：

```sh
git clone --recurse-submodules <project-url>
git submodule update --init --recursive
python .standards/.ci/check-adoption.py
```

接入检查核对 [gitlink](../glossary.md#gitlink)、初始化提交、规范工作区是否干净、智能体入口／分支规范链接及项目双语入口，再检查固定版本的规范文档。提交接入变更后，在父仓库根目录运行；[CI](../glossary.md#ci-cd) 初始化子模块并执行同一命令，托管平台示例见[此处](01-governance/platform-examples.md#consume-the-standards)。

升级时在 .standards 中获取上游提交，审查差异，检出获准的提交，不选择分支，然后在父仓库暂存 .standards。规范变更与受影响的配置一并审查，并运行接入检查及适用产品检查。恢复既有规范版本时，通过新的父仓库审查变更重新记录该确切提交。不在验证或发布时运行 git submodule update --remote。
