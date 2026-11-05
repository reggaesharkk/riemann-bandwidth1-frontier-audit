from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
inventory_path = ROOT / "source_hash_inventory.json"
manifest_path = ROOT / "SHA256SUMS.txt"
files = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or "__pycache__" in path.parts or path in {inventory_path, manifest_path}:
        continue
    rel = path.relative_to(ROOT).as_posix()
    data = path.read_bytes()
    files.append({"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
record = {
    "scope": "Every regular packet file except this inventory, the top-level SHA256SUMS.txt, and generated __pycache__ files. Nested dependency SHA256SUMS.txt files are included.",
    "formal_math_commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
    "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
    "lean_toolchain": "leanprover/lean4:v4.33.0-rc2",
    "lean_commit": "d8b18978322de05a8f3dba51ef03cf5461676c17",
    "lake_version": "5.0.0-src+d8b1897",
    "lake_manifest_sha256": "1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448",
    "files": files,
}
(inventory_path).write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"inventory entries={len(files)}")
