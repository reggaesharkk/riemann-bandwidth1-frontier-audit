#!/usr/bin/env python3
"""Verify packet file hashes and source V2 ZIP integrity."""
from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    manifest_path = ROOT / "SHA256SUMS.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checked = 0
    for item in manifest["files"]:
        path = ROOT / item["path"]
        if not path.is_file():
            raise SystemExit(f"missing file: {item['path']}")
        if path.stat().st_size != item["size_bytes"]:
            raise SystemExit(f"size mismatch: {item['path']}")
        if sha256(path) != item["sha256"]:
            raise SystemExit(f"SHA-256 mismatch: {item['path']}")
        checked += 1

    source_zip = ROOT / "source/input_v2/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    with zipfile.ZipFile(source_zip) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise SystemExit(f"source ZIP CRC failure: {bad}")
        zip_entries = len(archive.infolist())
    if sha256(source_zip) != "3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5":
        raise SystemExit("source V2 ZIP hash differs from frozen expected SHA-256")
    if zip_entries != 15:
        raise SystemExit(f"unexpected source ZIP entry count: {zip_entries}")
    print(f"PACKET_MANIFEST_PASS files={checked} source_zip_entries={zip_entries} source_zip_crc=PASS")


if __name__ == "__main__":
    main()
