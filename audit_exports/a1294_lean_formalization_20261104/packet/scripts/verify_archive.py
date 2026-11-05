#!/usr/bin/env python3
"""Safely extract the packet ZIP and independently verify all manifested files."""
from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path, PurePosixPath


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: verify_archive.py <packet.zip> <new-empty-extraction-directory>")
    archive_path, destination = Path(sys.argv[1]), Path(sys.argv[2])
    if destination.exists() and any(destination.iterdir()):
        raise SystemExit(f"destination must be new or empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(archive_path) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise SystemExit(f"outer ZIP CRC failure: {bad}")
        for name in archive.namelist():
            item = PurePosixPath(name)
            if item.is_absolute() or ".." in item.parts:
                raise SystemExit(f"unsafe ZIP path: {name}")
        archive.extractall(destination)

    manifest_path = destination / "SHA256SUMS.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checked = 0
    for item in manifest["files"]:
        path = destination / item["path"]
        if not path.is_file() or path.stat().st_size != item["size_bytes"]:
            raise SystemExit(f"missing/size mismatch: {item['path']}")
        if sha256(path) != item["sha256"]:
            raise SystemExit(f"hash mismatch: {item['path']}")
        checked += 1
    print(f"ARCHIVE_EXTRACTION_PASS files={checked} outer_zip_crc=PASS")


if __name__ == "__main__":
    main()
