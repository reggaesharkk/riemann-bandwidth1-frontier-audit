#!/usr/bin/env python3
"""Check copied WP19 ZIPs and the v0.25b payload checksum/path anomaly."""
from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    archive_dir = root / "evidence" / "wp19_archives"
    archives = sorted(archive_dir.glob("*.zip"))
    need(len(archives) == 9, f"expected 9 copied WP19 archives, found {len(archives)}")
    all_manifest_rows = []
    v025b_payload_rows = []
    v025b_self_mismatch = False
    for archive in archives:
        with zipfile.ZipFile(archive) as z:
            need(z.testzip() is None, f"ZIP CRC failure: {archive.name}")
            names = set(z.namelist())
            manifest_name = next((n for n in names if "sha256" in n.lower()), None)
            if manifest_name is None:
                continue
            raw = z.read(manifest_name)
            if manifest_name.lower().endswith(".json"):
                listed_hashes = json.loads(raw.decode("utf-8"))
            else:
                listed_hashes = {}
                for line in raw.decode("utf-8").splitlines():
                    m = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line.strip())
                    if m:
                        listed_hashes[m.group(2).strip()] = m.group(1).lower()
            rows = []
            for listed, expected_raw in listed_hashes.items():
                expected = expected_raw.lower()
                exact = listed if listed in names else Path(listed).name
                if exact not in names:
                    # v0.25b uses one canonical path-prefix convention only.
                    raise RuntimeError(f"unresolved manifest entry in {archive.name}: {listed}")
                actual = sha(z.read(exact))
                row = {"archive": archive.name, "listed_path": listed, "resolved_member": exact, "expected": expected, "actual": actual, "matches": actual == expected}
                is_self = Path(exact).name.lower().startswith("sha256sum")
                row["manifest_self_entry"] = is_self
                if is_self:
                    if archive.name == "wp19-v0-25b-signed-c500-n11-n18.zip":
                        v025b_self_mismatch = actual != expected
                    elif actual != expected:
                        # Other archives do not list a self-entry in this recovered set.
                        raise RuntimeError(f"unexpected self-manifest mismatch in {archive.name}")
                else:
                    need(actual == expected, f"payload checksum mismatch: {archive.name}:{listed}")
                rows.append(row)
            all_manifest_rows.append({"archive": archive.name, "manifest": manifest_name, "entries_checked": len(rows), "payload_entries_match": all(r["matches"] for r in rows if not r["manifest_self_entry"]), "rows": rows})
            if archive.name == "wp19-v0-25b-signed-c500-n11-n18.zip":
                v025b_payload_rows = [r for r in rows if not r["manifest_self_entry"]]
    need(len(v025b_payload_rows) == 6, f"expected five N payloads plus summary, got {len(v025b_payload_rows)}")
    need(v025b_self_mismatch, "expected recorded v0.25b self-manifest digest mismatch was not reproduced")
    out = {
        "status": "PASS_WITH_DOCUMENTED_MANIFEST_SELF_HASH_MISMATCH",
        "archive_count": len(archives),
        "zip_crc": "PASS for all 9 copied archives",
        "internal_manifest_replays": all_manifest_rows,
        "v0_25b_payload_entries_verified": len(v025b_payload_rows),
        "v0_25b_payload_checksums": v025b_payload_rows,
        "manifest_path_note": "listed final/... members resolve to archive-root basenames",
        "self_hash_mismatch": True,
    }
    (root / "results" / "wp19_manifest_replay.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
