#!/usr/bin/env python3
"""Verify the extracted packet manifest and all listed file hashes."""
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS.txt"
MANIFEST_HASH = ROOT / "MANIFEST_SHA256.txt"

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def main() -> int:
    expected_manifest = MANIFEST_HASH.read_text(encoding="utf-8").split()[0]
    if sha(MANIFEST) != expected_manifest:
        raise SystemExit("manifest hash mismatch")
    rows = MANIFEST.read_text(encoding="utf-8").splitlines()
    checked = 0
    for row in rows:
        if not row.strip():
            continue
        expected, rel = row.split("  ", 1)
        path = (ROOT / rel).resolve()
        if ROOT.resolve() not in path.parents:
            raise SystemExit(f"path escapes packet: {rel}")
        if not path.is_file() or sha(path) != expected:
            raise SystemExit(f"file hash mismatch: {rel}")
        checked += 1
    print(f"PASS: manifest and {checked} packet files verified")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
