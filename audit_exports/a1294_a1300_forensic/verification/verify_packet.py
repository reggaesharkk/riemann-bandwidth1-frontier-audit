#!/usr/bin/env python3
"""Verify recovered source-free replay package integrity using stdlib only."""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    local = root / "evidence" / "local" / "C_Users_Asus_Downloads"
    extracted = local / "A1294_SOURCE_FREE_REPLAY_V2" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2"
    archive = local / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    manifest = json.loads((extracted / "PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
    need(manifest.get("schema") == "a1294-source-free-package-v2", "unexpected V2 manifest schema")
    files = manifest["files"]

    checked = []
    for relative, expected in files.items():
        path = extracted / Path(relative)
        raw = path.read_bytes()
        need(len(raw) == expected["bytes"], f"byte count mismatch: {relative}")
        need(sha256(raw) == expected["sha256"], f"SHA-256 mismatch: {relative}")
        checked.append(relative)

    with zipfile.ZipFile(archive) as zf:
        need(zf.testzip() is None, "V2 ZIP CRC failure")
        names = set(zf.namelist())
        prefix = "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/"
        for relative, expected in files.items():
            member = prefix + relative
            need(member in names, f"manifest member absent from ZIP: {member}")
            raw = zf.read(member)
            need(len(raw) == expected["bytes"] and sha256(raw) == expected["sha256"], f"ZIP member mismatch: {member}")
        for name in names:
            parts = Path(name).parts
            need(not Path(name).is_absolute() and ".." not in parts, f"unsafe ZIP member path: {name}")
        with tempfile.TemporaryDirectory(prefix="v2-extract-", dir=root / "verification") as temporary:
            zf.extractall(temporary)
            fresh = Path(temporary) / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2"
            fresh_manifest = json.loads((fresh / "PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
            need(fresh_manifest == manifest, "fresh extraction manifest differs")
            for relative, expected in fresh_manifest["files"].items():
                raw = (fresh / Path(relative)).read_bytes()
                need(len(raw) == expected["bytes"] and sha256(raw) == expected["sha256"], f"fresh extraction member mismatch: {relative}")

    result = json.loads((extracted / "A1294_SOURCE_FREE_REPLAY_RESULT.json").read_text(encoding="utf-8"))
    with zipfile.ZipFile(archive) as zf:
        archived_replay = json.loads(zf.read("A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/replay.json"))
    for field in ("A", "B", "status", "visited_nodes", "leaves", "quadratic_leaves", "tail_leaves", "smallest_quadratic_margin", "smallest_tail_margin", "stream_sha256"):
        need(archived_replay.get(field) == result.get(field), f"archive replay record differs from saved result field {field}")
    need(result["status"] == "PASS", "historical V2 replay record is not PASS")
    need(result["visited_nodes"] == 13_454_121, "historical V2 node count mismatch")
    need(result["leaves"] == 6_727_061, "historical V2 leaf count mismatch")
    need(result["quadratic_leaves"] == 6_725_258 and result["tail_leaves"] == 1_803, "historical V2 leaf partition mismatch")
    stream_members = {
        "anchors": "certificate/anchors-u16le.bin",
        "kinds": "certificate/terminal-kinds-u8.bin",
        "topology": "certificate/topology-u8.bin",
    }
    for key, relative in stream_members.items():
        need(sha256((extracted / relative).read_bytes()) == result["stream_sha256"][key], f"replay stream hash mismatch: {key}")

    print(json.dumps({
        "result": "PASS",
        "v2_manifest_files_verified": len(checked),
        "v2_zip_crc": "PASS",
        "fresh_v2_extraction_manifest": "PASS",
        "archive_replay_record_matches_saved_result": "PASS",
        "historical_full_replay_record": result["status"],
        "historical_replay_visited_nodes": result["visited_nodes"],
        "historical_replay_seconds": result["elapsed_seconds"],
        "note": "This script verifies package, streams, and the saved replay record; it does not repeat the 18,897.781-second traversal.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
