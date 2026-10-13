#!/usr/bin/env python3
"""Copie les sessions et le template en clair vers un dossier Obsidian.

Usage : python3 scripts/sync_obsidian.py <dossier-de-destination>

Le dépôt reste la source de vérité : relancer le script écrase les fichiers copiés.
Les encadrés mkdocs (!!! / ???) sont convertis en encadrés Obsidian (> [!type]).
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = re.compile(r'^(!!!|\?\?\?)\s+(\w+)(?:\s+"(.*)")?\s*$')


def to_obsidian(text: str) -> str:
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        m = START.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        fold = "-" if m.group(1) == "???" else ""
        out.append(f"> [!{m.group(2)}]{fold} {m.group(3) or ''}".rstrip())
        i += 1
        # le corps : lignes indentées de 4 espaces, ou vides suivies d'une ligne indentée
        while i < len(lines):
            if lines[i].startswith("    "):
                out.append("> " + lines[i][4:])
            elif lines[i] == "" and i + 1 < len(lines) and lines[i + 1].startswith("    "):
                out.append(">")
            else:
                break
            i += 1
    return "\n".join(out)


def copy_dir(src: Path, dest: Path) -> int:
    n = 0
    for f in sorted(src.glob("*.md")):
        dest.mkdir(parents=True, exist_ok=True)
        (dest / f.name).write_text(to_obsidian(f.read_text(encoding="utf-8")), encoding="utf-8")
        n += 1
    return n


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    dest = Path(sys.argv[1]).expanduser()
    total = copy_dir(ROOT / "_template", dest / "_template")
    sessions = ROOT / "docs" / "sessions"
    for d in sorted(p for p in sessions.iterdir() if p.is_dir()):
        total += copy_dir(d, dest / d.name)
    print(f"{total} fichiers copiés vers {dest}")


if __name__ == "__main__":
    main()
