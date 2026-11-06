"""Verify that a parent repository adopts the exact reviewed standards commit."""

import re
import subprocess
import sys
from pathlib import Path

STANDARDS = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")


def git(directory, *arguments, required=True):
    result = subprocess.run(
        ["git", "-C", str(directory), *arguments],
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if required and result.returncode:
        raise ValueError(f"Git command failed: {' '.join(arguments)}")
    return result.stdout.strip()


def verify(parent):
    parent = parent.resolve()
    if (parent / ".standards").resolve() != STANDARDS:
        raise ValueError("Run this check from the parent repository root.")
    recorded = git(parent, "ls-tree", "HEAD", "--", ".standards")
    match = re.fullmatch(r"160000 commit ([0-9a-f]{40,64})\t\.standards", recorded)
    if not match:
        raise ValueError("Commit the .standards submodule in the parent repository.")
    expected = match[1]
    if git(STANDARDS, "rev-parse", "HEAD") != expected:
        raise ValueError("The standards checkout differs from the parent-recorded commit.")
    if git(STANDARDS, "status", "--porcelain"):
        raise ValueError("The standards checkout has local changes or untracked files.")
    if git(parent, "diff", "HEAD", "--", ".standards", ".gitmodules"):
        raise ValueError("Commit the standards reference and configuration before checking.")
    path = git(parent, "config", "-f", ".gitmodules", "--get", "submodule.standards.path")
    if path != ".standards":
        raise ValueError("The standards submodule must use the .standards path.")
    if git(parent, "config", "-f", ".gitmodules", "--get", "submodule.standards.branch", required=False):
        raise ValueError("Do not configure branch tracking for the standards submodule.")
    agent = (parent / "AGENTS.md").read_text(encoding="utf-8-sig")
    if ".standards/docs/en/README.md" not in LINK.findall(agent):
        raise ValueError("AGENTS.md must directly link the adopted English standards.")
    if ".standards/docs/en/02-development/git-branching.md" not in LINK.findall(agent):
        raise ValueError("AGENTS.md must directly link the English Git branching standards.")
    for edition in ("en", "zh-CN"):
        source = parent / "docs" / edition / "README.md"
        target = f"../../.standards/docs/{edition}/README.md"
        if target not in LINK.findall(source.read_text(encoding="utf-8-sig")):
            raise ValueError(f"Project docs/{edition}/README.md must link the matching standards edition.")
    print(f"Standards adoption verified: {expected}")
    result = subprocess.run([sys.executable, str(STANDARDS / ".ci" / "check-standards.py")])
    return result.returncode


if __name__ == "__main__":
    try:
        raise SystemExit(verify(Path.cwd()))
    except (ValueError, OSError) as error:
        print(f"Standards adoption failed: {error}", file=sys.stderr)
        raise SystemExit(1)
