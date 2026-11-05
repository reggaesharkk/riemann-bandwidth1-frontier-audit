#!/usr/bin/env python3
"""Write the source hash inventory and packet-wide SHA256SUMS file."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("packet_root", type=Path)
    ap.add_argument("--worktree-commit", required=True)
    args = ap.parse_args()
    root = args.packet_root.resolve()

    v2 = root / "source" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    with zipfile.ZipFile(v2) as zf:
        prefix = "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/"
        cert = json.loads(zf.read(prefix + "certificate/manifest.json"))
        v2_inputs = {}
        for name, member in {
            "stable": "data/macro-data-exact.json",
            "refinement_v1": "data/refinement-catalog-v1-exact.json",
            "refinement_v2": "data/refinement-catalog-v3.json",
            "topology": "certificate/topology-u8.bin",
            "terminal_kinds": "certificate/terminal-kinds-u8.bin",
            "anchors": "certificate/anchors-u16le.bin",
        }.items():
            v2_inputs[name] = hashlib.sha256(zf.read(prefix + member)).hexdigest()

    lock = json.loads((root / "source" / "zeta23" / "lake-manifest.json").read_text(encoding="utf-8"))
    mathlib = next(p["rev"] for p in lock["packages"] if p["name"] == "mathlib")
    lean_toolchain = (root / "source" / "zeta23" / "lean-toolchain").read_text(encoding="utf-8").strip()
    lean_src = root / "lean" / "A1294QuadraticLeaf.lean"
    upstream_files = {
        p.relative_to(root / "source" / "zeta23").as_posix(): sha(p)
        for p in sorted((root / "source" / "zeta23").rglob("*"))
        if p.is_file()
    }
    inventory = {
        "local_worktree_commit": args.worktree_commit,
        "upstream_formal_math_commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
        "mathlib_commit_from_lake_manifest": mathlib,
        "lean_toolchain_file": lean_toolchain,
        "lean_compiler_commit": "d8b18978322de05a8f3dba51ef03cf5461676c17",
        "final_lean_source_sha256": sha(lean_src),
        "frozen_v2_zip_sha256": sha(v2),
        "prior_pilot_zip_sha256": sha(root / "source" / "A1294_LEAN_KERNEL_PILOT_PACKET_20261104.zip"),
        "frozen_v2_entry_sha256": v2_inputs,
        "pinned_upstream_source_file_sha256": upstream_files,
        "evidence_file_sha256": {
            rel: sha(root / rel)
            for rel in (
                "reports/source_prefix.json",
                "reports/ledger_normal.json",
                "reports/ledger_O.json",
                "reports/ledger_OO.json",
                "reports/catalog_normal.json",
                "reports/catalog_O.json",
                "reports/catalog_OO.json",
                "logs/build_final_axioms.log",
            )
        },
        "scope_note": "Hashes authenticate packaged bytes; the serialized-node-to-Lean-path link and owner selector are not kernel formalized.",
    }
    (root / "source_hash_inventory.json").write_text(
        json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    lines = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "SHA256SUMS.txt"):
        lines.append(f"{sha(path)}  {path.relative_to(root).as_posix()}")
    (root / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"SOURCE_HASH_INVENTORY=PASS upstream_source_files={len(upstream_files)}")
    print(f"PACKET_SHA256_ENTRIES={len(lines)}")
    print(f"FINAL_LEAN_SHA256={sha(lean_src)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
