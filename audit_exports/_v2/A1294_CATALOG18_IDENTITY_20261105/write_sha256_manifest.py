from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifest = ROOT / "SHA256SUMS.txt"
lines = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or "__pycache__" in path.parts or path == manifest:
        continue
    rel = path.relative_to(ROOT).as_posix()
    lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {rel}")
manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"wrote {manifest.name}: {len(lines)} entries")
