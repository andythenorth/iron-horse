#!/usr/bin/env python3
import re, json, sys
from pathlib import Path

PATTERN = re.compile(
    r"""define_description\(\s*
        (?P<q>'''|""" + '"""' + r"""|'|")
        (?P<desc>.*?)
        (?P=q)
        \s*\)
    """,
    re.DOTALL | re.VERBOSE,
)

if len(sys.argv) < 2:
    print("usage: extract_descriptions.py <dir> [out.json]")
    sys.exit(1)

src_dir = Path(sys.argv[1])
out_file = sys.argv[2] if len(sys.argv) > 2 else "descriptions.json"

out = {}

for path in src_dir.rglob("*.py"):
    text = path.read_text(encoding="utf-8", errors="ignore")
    for m in PATTERN.finditer(text):
        desc = m.group("desc").strip()
        if desc and desc != ".":
            out[desc] = path.name

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"wrote {len(out)} descriptions → {out_file}")
