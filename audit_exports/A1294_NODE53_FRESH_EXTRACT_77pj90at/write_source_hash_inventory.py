from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "terminal16_authentic_input.json"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    record = json.loads(INPUT.read_text(encoding="utf-8-sig"))
    names = [
        "reference_inputs/A1294_NODE55_TERMINAL17_PROOF_PACKET_20261105.zip",
        "reference_inputs/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip",
        "terminal16_authentic_input.json",
        "terminal16_catalog_reindex.json",
        "extract16_reconstruct.py",
        "verify_terminal16_reconstruction.py",
        "generate_terminal16_catalog.py",
        "generate_terminal16_compositional.py",
        "independent_extract_check.py",
        "Catalog16.lean", "Catalog16.olean",
        "Catalog16Identity.lean", "Catalog16Identity.olean",
        "Catalog16BoundaryBlocks.lean", "Catalog16BoundaryBlocks.olean",
        "Catalog16AllLookups.lean", "Catalog16AllLookups.olean",
        "Terminal16Compositional.lean", "Terminal16Compositional.olean",
        "Node53Replay.lean", "Node53Replay.olean",
        "reference_packet/Node55Replay.lean", "reference_packet/Node55Replay.olean",
        "reference_predecessor/A1294_CATALOG18_IDENTITY_20261105/Node57Replay.lean",
        "reference_predecessor/A1294_CATALOG18_IDENTITY_20261105/Node57Replay.olean",
    ]
    files = {}
    for rel in names:
        path = ROOT / Path(rel)
        if path.is_file():
            files[rel] = {"bytes": path.stat().st_size, "sha256": sha(path)}
    payload = {
        "format": "A1294-source-hash-inventory-v1",
        "source_archives": {
            "node55_packet": {
                "sha256": record["source_input_sha256"].get("node55_packet", "ba18a4a2993cf3941ffa1c13c11db812852b4a3ea3b485bd850f0b481264ab14"),
                "bytes": (ROOT / "reference_inputs/A1294_NODE55_TERMINAL17_PROOF_PACKET_20261105.zip").stat().st_size,
            },
            "v2_zip_sha256": record["v2_zip_sha256"],
            "streams": record["source_stream_sha256"],
            "catalog_inputs": record["source_input_sha256"],
        },
        "pinned_environment": {
            "formal_math_commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
            "lean": "4.33.0-rc2; d8b18978322de05a8f3dba51ef03cf5461676c17",
            "lake": "5.0.0-src+d8b1897",
            "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
            "lake_manifest_sha256": "1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448",
        },
        "local_files": files,
        "note": "SHA-256 values establish byte identity relative to this inventory, not publisher authenticity or mathematical truth.",
    }
    (ROOT / "SOURCE_HASH_INVENTORY.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"WROTE SOURCE_HASH_INVENTORY.json entries={len(files)}")

if __name__ == "__main__":
    main()
