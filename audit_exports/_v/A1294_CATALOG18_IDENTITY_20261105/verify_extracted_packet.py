from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent).resolve()
manifest = ROOT / "SHA256SUMS.txt"
expected: dict[str, str] = {}
for line in manifest.read_text(encoding="utf-8").splitlines():
    digest, rel = line.split("  ", 1)
    rel_path = Path(rel)
    if rel_path.is_absolute() or ".." in rel_path.parts:
        raise RuntimeError(f"unsafe manifest path: {rel}")
    expected[rel_path.as_posix()] = digest
actual: dict[str, str] = {}
for path in ROOT.rglob("*"):
    if not path.is_file() or "__pycache__" in path.parts or path == manifest:
        continue
    rel = path.relative_to(ROOT).as_posix()
    actual[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
if expected.keys() != actual.keys():
    raise RuntimeError(f"manifest path mismatch missing={sorted(expected.keys()-actual.keys())} extra={sorted(actual.keys()-expected.keys())}")
mismatched = [name for name in expected if expected[name] != actual[name]]
if mismatched:
    raise RuntimeError(f"manifest hash mismatch: {mismatched}")
inventory = json.loads((ROOT / "source_hash_inventory.json").read_text(encoding="utf-8"))
for row in inventory["files"]:
    path = ROOT / row["path"]
    data = path.read_bytes()
    if len(data) != row["bytes"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
        raise RuntimeError(f"source inventory mismatch: {row['path']}")
env = os.environ.copy()
env["PYTHONPATH"] = str(ROOT / "reference")
result = subprocess.run([sys.executable, "replay_local_tests.py"], cwd=ROOT, env=env, text=True)
if result.returncode:
    raise SystemExit(result.returncode)
print(f"PASS extracted packet manifest: {len(expected)} entries; source inventory: {len(inventory['files'])} entries")
