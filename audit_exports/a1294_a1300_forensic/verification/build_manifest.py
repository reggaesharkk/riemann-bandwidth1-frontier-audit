#!/usr/bin/env python3
"""Write SHA256SUMS.txt for all packet files except the manifest itself."""

from __future__ import annotations

import hashlib
from pathlib import Path


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    manifest = root / "SHA256SUMS.txt"
    rows = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p != manifest):
        rows.append(f"{sha(path)}  {path.relative_to(root).as_posix()}")
    manifest.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"wrote {manifest.name} with {len(rows)} file hashes")


if __name__ == "__main__":
    main()
