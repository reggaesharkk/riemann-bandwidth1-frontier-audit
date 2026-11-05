from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT.parent.parent / "A1294_CATALOG18_IDENTITY_TERMINAL18_NODE57_20261105.zip"
if OUTPUT == ROOT or ROOT in OUTPUT.parents:
    raise SystemExit("output ZIP must be outside the packet source directory")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
root_name = ROOT.name
with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as archive:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        archive.write(path, Path(root_name) / path.relative_to(ROOT))
with zipfile.ZipFile(OUTPUT) as archive:
    bad = archive.testzip()
    if bad is not None:
        raise RuntimeError(f"ZIP CRC failed: {bad}")
print(f"created {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
