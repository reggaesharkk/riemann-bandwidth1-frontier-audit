#!/usr/bin/env python3
"""Write the source inventory, file manifest, and manifest digest."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def main() -> None:
    summary = json.loads((ROOT / "logs/replay2/verification_summary.json").read_text(encoding="utf-8"))
    paths = sorted(p for p in ROOT.rglob("*") if p.is_file()
                   and p.name not in {"SHA256SUMS.txt", "MANIFEST_SHA256.txt", "source_hash_inventory.json"})
    hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in paths}
    inventory = {
        "upstream_repository": "anthropics/formal-math",
        "upstream_commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
        "audit_worktree_commit": "eb36159ee7e57053fcae3de025fe4dac539435ab",
        "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
        "lean_toolchain": "leanprover/lean4:v4.33.0-rc2",
        "lean_commit": "d8b18978322de05a8f3dba51ef03cf5461676c17",
        "frozen_v2_zip_sha256": summary["source_zip_sha256"],
        "v2_stream_sha256": summary["source_stream_sha256"],
        "source_replay_status": summary["status"],
        "file_sha256": hashes,
    }
    (ROOT / "source_hash_inventory.json").write_text(
        json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    all_files = sorted(p for p in ROOT.rglob("*") if p.is_file()
                       and p.name not in {"SHA256SUMS.txt", "MANIFEST_SHA256.txt"})
    manifest = "".join(f"{sha(p)}  {p.relative_to(ROOT).as_posix()}\n" for p in all_files)
    (ROOT / "SHA256SUMS.txt").write_text(manifest, encoding="utf-8", newline="\n")
    (ROOT / "MANIFEST_SHA256.txt").write_text(
        f"{sha(ROOT / 'SHA256SUMS.txt')}  SHA256SUMS.txt\n", encoding="utf-8", newline="\n")
    print(f"wrote inventory for {len(hashes)} files")

if __name__ == "__main__":
    main()
