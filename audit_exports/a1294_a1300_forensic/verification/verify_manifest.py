#!/usr/bin/env python3
"""Verify SHA256SUMS.txt for an extracted packet (stdlib only)."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = root / "SHA256SUMS.txt"
    lines = [line for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip()]
    checked = 0
    for line in lines:
        expected, relative = line.split("  ", 1)
        path = root / Path(relative)
        if not path.is_file():
            raise RuntimeError(f"manifest file missing: {relative}")
        actual = sha(path)
        if actual != expected:
            raise RuntimeError(f"SHA-256 mismatch: {relative}: {actual} != {expected}")
        checked += 1
    print(f"SHA256SUMS PASS: {checked} files")


if __name__ == "__main__":
    main()
