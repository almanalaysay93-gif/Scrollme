#!/usr/bin/env python3
"""Validate Scrollme metadata, required files, local links and Python syntax."""

import argparse
import ast
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

REQUIRED = (
    "SKILL.md", "README.md", "LICENSE",
    "references/architecture.md", "references/agents.md",
    "references/superlite-integration.md",
    "references/ux-laws.md", "references/ux-laws-workflow.md",
    "references/sources-and-licenses.md", "references/verification.md",
    "templates/BRIEF.md", "templates/PLAN.md", "templates/CONTEXT.md",
    "templates/QC_REPORT.md", "scripts/init_project.py",
    "scripts/validate_skill.py", "tests/test_tools.py",
    ".github/workflows/validate.yml",
)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for relative in REQUIRED:
        path = root / relative
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty required file: {relative}")
    skill = root / "SKILL.md"
    if skill.is_file():
        content = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not match:
            errors.append("SKILL.md must start with YAML frontmatter")
        else:
            fields = dict(re.findall(r"^(name|description):\s*(.+)$", match[1], re.M))
            if fields.get("name") != "scrollme":
                errors.append("Skill name must be scrollme")
            if len(fields.get("description", "")) < 30:
                errors.append("Skill description must explain when to use it")
    files = [p for p in root.rglob("*") if p.is_file()
             and not any(part.startswith(".") or part == "__pycache__"
                         for part in p.relative_to(root).parts)]
    for path in files:
        if path.suffix == ".md":
            content = path.read_text(encoding="utf-8")
            # The package uses inline Markdown links without nested parentheses.
            for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
                parsed = urlsplit(link.strip("<>"))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (path.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(root) or not target.exists():
                    errors.append(f"Broken local link in {path.relative_to(root)}: {link}")
        elif path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except SyntaxError as error:
                errors.append(f"Invalid Python: {path.relative_to(root)}: {error}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: skill metadata, package files, local links and Python syntax")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
