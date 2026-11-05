#!/usr/bin/env python3
"""Verify SHA256SUMS.txt and replay the packet's lightweight checks."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    manifest = root / "SHA256SUMS.txt"
    need(manifest.exists(), "SHA256SUMS.txt not found")
    seen = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        path = root / rel
        need(path.is_file(), f"manifest path missing: {rel}")
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        need(got == digest, f"SHA-256 mismatch: {rel}")
        seen.add(rel.replace("\\", "/"))
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and p.name != "SHA256SUMS.txt"}
    need(seen == actual, f"manifest coverage differs: absent={sorted(actual-seen)}, extra={sorted(seen-actual)}")
    checks = [
        [sys.executable, str(root / "verification" / "verify_a12994_erratum.py"), "--root", str(root)],
        [sys.executable, str(root / "verification" / "check_wp19_archives.py")],
        [sys.executable, str(root / "verification" / "check_a1294_v2_package.py")],
    ]
    outputs = []
    for command in checks:
        done = subprocess.run(command, check=False, capture_output=True, text=True)
        need(done.returncode == 0, f"replay command failed: {command[-1]}\n{done.stderr}")
        outputs.append(done.stdout)
    print(f"SHA-256 manifest: PASS ({len(seen)} files)")
    print("A12994 exact checker: PASS")
    print("WP19 archive check: PASS WITH DOCUMENTED SELF-MANIFEST MISMATCH")
    print("A1294 V2 package check: PASS")


if __name__ == "__main__":
    main()
