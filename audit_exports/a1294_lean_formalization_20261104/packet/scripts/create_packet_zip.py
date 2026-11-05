#!/usr/bin/env python3
"""Create the named ZIP beside the packet directory, without replacing an archive."""
from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT.parent / "A1294_LEAN_KERNEL_PILOT_PACKET_20261104.zip"


def main() -> None:
    if DEST.exists():
        raise SystemExit(f"refusing to overwrite existing archive: {DEST}")
    with ZipFile(DEST, "x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
            archive.write(path, path.relative_to(ROOT).as_posix())
    print(f"created {DEST} ({DEST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
