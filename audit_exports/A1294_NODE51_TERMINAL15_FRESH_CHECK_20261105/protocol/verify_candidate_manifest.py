#!/usr/bin/env python3
"""Strict candidate source manifest verifier; also rejects unlisted regular files."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".lake", "build", "dist"}


def main() -> int:
    manifest = ROOT / "MANIFEST_SHA256.txt"
    expected = {}
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        digest, rel = raw.split(None, 1)
        expected[rel.strip()] = digest
    actual = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in EXCLUDED or part.endswith(".egg-info") for part in path.relative_to(ROOT).parts):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == "MANIFEST_SHA256.txt":
            continue
        actual[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    missing = sorted(set(expected) - set(actual))
    unlisted = sorted(set(actual) - set(expected))
    mismatched = sorted(p for p in expected.keys() & actual.keys() if expected[p] != actual[p])
    print(f"manifest entries={len(expected)} actual={len(actual)} missing={missing} unlisted={unlisted} mismatched={mismatched}")
    return int(bool(missing or unlisted or mismatched))


if __name__ == "__main__":
    raise SystemExit(main())
