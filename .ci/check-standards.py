"""CI check for mirrored Markdown editions, relative links and glossary anchors."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
EDITIONS = ("docs/en", "docs/zh-CN")
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")
RULE = re.compile(r"^- \*\*([A-Z]{3}-[0-9]{2}) (MUST|SHOULD|MAY)\b", re.M)
MODULE = re.compile(r"^# ([0-9]{2})\. ", re.M)
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})(.*)$")
GLOSSARY = Path("docs/glossary.md")
TERM = re.compile(r"^### ([A-Za-z0-9]+(?:[ -][A-Za-z0-9]+)*)\n(.*?)(?=^#{1,3} |\Z)", re.M | re.S)
TERM_ROW = re.compile(r"^\| \[[^\]\n]+\]\(#([a-z0-9-]+)\) \| [^|\n]+ \|$", re.M)


def outside_code(content):
    """Ignore examples in fenced blocks when reading headings and links."""
    fence = ""
    for line in content.splitlines(keepends=True):
        marker = FENCE.match(line)
        if not fence and marker:
            fence = marker[1]
        elif fence and marker and marker[1].startswith(fence) and not marker[2].strip():
            fence = ""
        elif not fence:
            yield line


def main():
    errors = []
    contents = {}
    files = {Path("README.md"), Path("AGENTS.md"), GLOSSARY}
    mirrored = {}
    for edition in EDITIONS:
        folder = ROOT / edition
        mirrored[edition] = {p.relative_to(folder) for p in folder.rglob("*.md")}
        files.update(Path(edition) / p for p in mirrored[edition])

    left, right = EDITIONS
    for relative in sorted(mirrored[left] ^ mirrored[right]):
        errors.append(f"{relative}: missing from one edition")

    for relative in sorted(files):
        source = ROOT / relative
        try:
            raw = source.read_bytes()
            if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw or not raw.endswith(b"\n"):
                errors.append(f"{relative}: expected UTF-8 without BOM and LF with final newline")
            body = "".join(outside_code(raw.decode("utf-8")))
        except (OSError, UnicodeError) as exc:
            errors.append(f"{relative}: {exc}")
            continue
        contents[relative] = body

    glossary_body = contents.get(GLOSSARY, "")
    anchors = set()
    for heading, entry in TERM.findall(glossary_body):
        anchor = heading.lower().replace(" ", "-")
        if anchor in anchors:
            errors.append(f"{GLOSSARY}: duplicate glossary anchor #{anchor}")
        if not re.search(r"^\*\*EN:\*\* \S", entry, re.M) or not re.search(r"^\*\*中：\*\* \S", entry, re.M):
            errors.append(f"{GLOSSARY}#{anchor}: missing English or Chinese explanation")
        anchors.add(anchor)
    listed = TERM_ROW.findall(glossary_body)
    if not anchors or sorted(listed) != sorted(anchors):
        errors.append(f"{GLOSSARY}: each glossary entry needs exactly one comparison row")

    for relative, body in contents.items():
        source = ROOT / relative
        for match in LINK.finditer(body):
            target = urlsplit(match[1].strip("<>"))
            if target.scheme or target.netloc:
                continue
            path = (source.parent / unquote(target.path)).resolve() if target.path else source
            if not path.is_relative_to(ROOT) or not path.exists():
                errors.append(f"{relative}: unresolved relative link {match[1]}")
            elif path == ROOT / GLOSSARY and target.fragment and unquote(target.fragment) not in anchors:
                errors.append(f"{relative}: unknown glossary anchor {match[1]}")

    if "docs/en/README.md" not in LINK.findall(contents.get(Path("AGENTS.md"), "")):
        errors.append("AGENTS.md: missing direct link to docs/en/README.md")

    for edition in EDITIONS:
        index = contents.get(Path(edition) / "README.md", "")
        indexed = set(LINK.findall(index))
        if "../glossary.md" not in indexed:
            errors.append(f"{edition}/README.md: missing link to {GLOSSARY}")
        module_numbers = []
        rule_ids = set()
        for relative in sorted(mirrored[edition]):
            body = contents.get(Path(edition) / relative, "")
            number = MODULE.search(body)
            if not number:
                continue
            module_numbers.append(number[1])
            if relative.as_posix() not in indexed:
                errors.append(f"{edition}/{relative}: missing from index")
            rules = RULE.findall(body)
            if not rules:
                errors.append(f"{edition}/{relative}: no rule IDs")
            for rule, _ in rules:
                if rule in rule_ids:
                    errors.append(f"{edition}/{relative}: duplicate rule {rule}")
                rule_ids.add(rule)
        expected = [f"{n:02}" for n in range(1, 13)]
        if sorted(module_numbers) != expected:
            errors.append(f"{edition}: expected each module number 01–12 exactly once")

    for relative in sorted(mirrored[left] & mirrored[right]):
        en = contents.get(Path(left) / relative, "")
        zh = contents.get(Path(right) / relative, "")
        if MODULE.findall(en) != MODULE.findall(zh) or RULE.findall(en) != RULE.findall(zh):
            errors.append(f"{relative}: module number, rule IDs or levels differ")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked {len(files)} Markdown files, 12 modules per edition, rule parity, links and {len(anchors)} glossary entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
