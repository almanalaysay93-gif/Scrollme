#!/usr/bin/env python3
"""Create Scrollme planning documents without replacing existing work."""

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = {
    "BRIEF.md": "BRIEF.md",
    "PLAN.md": "PLAN.md",
    "CONTEXT.md": "references/CONTEXT.md",
    "QC_REPORT.md": "QC_REPORT.md",
}


def initialize(destination: Path) -> list[Path]:
    """Preflight all paths, then create files exclusively; roll back on failure."""
    destination = destination.expanduser().absolute()
    targets = [destination / relative for relative in DOCUMENTS.values()]
    directories = [destination, destination / "references", destination / "references/images"]
    for path in targets + directories:
        for candidate in (path, *path.parents):
            if candidate.is_symlink():
                raise ValueError(f"Refusing symlink path: {candidate}")
    for path in targets:
        if path.exists():
            raise FileExistsError(f"Refusing to overwrite: {path}")
    for path in directories:
        if path.exists() and not path.is_dir():
            raise NotADirectoryError(f"Not a directory: {path}")
    # Read everything before making any project changes.
    contents = [(ROOT / "templates" / source).read_text(encoding="utf-8")
                for source in DOCUMENTS]
    created = []
    try:
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
        for path, content in zip(targets, contents):
            with path.open("x", encoding="utf-8") as handle:
                created.append(path)
                handle.write(content)
    except Exception:
        for path in reversed(created):
            path.unlink()
        raise
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New or existing project directory")
    args = parser.parse_args()
    try:
        for path in initialize(args.destination):
            print(f"Created {path}")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Initialization failed: {error}\n")
    print("Planning documents only. Confirm BRIEF.md before building the website.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
