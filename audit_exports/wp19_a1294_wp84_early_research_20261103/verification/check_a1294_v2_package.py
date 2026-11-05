#!/usr/bin/env python3
"""Verify every member covered by the copied A1294 V2 package manifest."""
from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    path = root / "evidence" / "a1294_source_free_v2" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    with zipfile.ZipFile(path) as z:
        need(z.testzip() is None, "A1294 V2 ZIP CRC failure")
        prefix = "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/"
        manifest = json.loads(z.read(prefix + "PACKAGE_MANIFEST.json"))
        checked = []
        for name, record in manifest["files"].items():
            member = prefix + name
            data = z.read(member)
            got = hashlib.sha256(data).hexdigest()
            need(len(data) == record["bytes"], f"byte count mismatch: {name}")
            need(got == record["sha256"], f"SHA-256 mismatch: {name}")
            checked.append(name)
    result_path = root / "evidence" / "a1294_source_free_v2" / "A1294_SOURCE_FREE_REPLAY_RESULT.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    need(result["A"] == "647/50000" and result["B"] == "1094977/5000000000", "unexpected A1294 V2 target")
    need(result["status"] == "PASS" and result["visited_nodes"] == 13454121, "unexpected V2 replay result record")
    print(json.dumps({"status": "PASS", "manifest_members_checked": len(checked), "result": {k: result[k] for k in ("A", "B", "status", "visited_nodes", "leaves")}}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
