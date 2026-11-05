#!/usr/bin/env python3
"""Create packet source inventory and SHA-256 file manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory_file(path: Path) -> dict[str, object]:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "size_bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def main() -> None:
    source_root = ROOT / "source/upstream/zeta23"
    upstream_files = sorted(
        p for p in source_root.rglob("*")
        if p.is_file() and (p.suffix == ".lean" or p.name in {
            "lean-toolchain", "lakefile.toml", "lake-manifest.json"
        })
    )
    input_zip = ROOT / "source/input_v2/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"
    result_path = ROOT / "evidence/prior_A1294_SOURCE_FREE_REPLAY_RESULT.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "evidence/catalog_comparison.json").read_text(encoding="utf-8"))
    stream = json.loads((ROOT / "evidence/source_tail_leaf.json").read_text(encoding="utf-8"))

    source_inventory = {
        "schema": "a1294-lean-pilot-source-inventory-v1",
        "local_worktree": {
            "commit": "eb36159ee7e57053fcae3de025fe4dac539435ab",
            "tracked_files_changed": False,
        },
        "local_frozen_reference": "7f3394c5655238b1e9736f91233d0bcc4c49fd43",
        "upstream": {
            "repository": "anthropics/formal-math",
            "commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
            "project": "zeta23",
            "lean_toolchain": "leanprover/lean4:v4.33.0-rc2",
            "lean_compiler_commit": "d8b18978322de05a8f3dba51ef03cf5461676c17",
            "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
        },
        "source_package": {
            **inventory_file(input_zip),
            "expected_sha256": "3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5",
            "zip_entries": 15,
            "zip_crc": "PASS",
            "preflight": "PASS",
        },
        "prior_source_free_replay": {
            **inventory_file(result_path),
            "status": result["status"],
            "visited_nodes": result["visited_nodes"],
            "leaves": result["leaves"],
            "replayed_in_this_pilot": False,
            "stream_sha256": result["stream_sha256"],
        },
        "catalog_comparison": {
            "script": inventory_file(ROOT / "scripts/compare_catalogs.py"),
            "result": inventory_file(ROOT / "evidence/catalog_comparison.json"),
            "catalogs": catalog,
            "owner_selection_mapping_formalized_in_Lean": False,
        },
        "selected_tail_leaf": {
            "extractor": inventory_file(ROOT / "scripts/extract_tail_subtree.py"),
            "result": inventory_file(ROOT / "evidence/source_tail_leaf.json"),
            "source_node_index_zero_based": stream["source_node_index_zero_based"],
            "source_leaf_index_zero_based": stream["source_leaf_index_zero_based"],
            "kind": stream["source_terminal_kind"],
            "box": stream["source_root_box_exact"],
            "tail_margin": stream["exact_tail_margin"],
            "stream_sha256": stream["source_stream_sha256"],
            "prefix_location_proved_by": "SHA-256-authenticated streams plus deterministic Python structural extraction; not kernel-encoded",
        },
        "pilot_artifacts": {
            "lean_module": inventory_file(ROOT / "A1294Pilot.lean"),
            "preflight_log": inventory_file(ROOT / "logs/input_preflight.log"),
            "affine_tree_build_log": inventory_file(ROOT / "logs/upstream_affinetree_build.log"),
            "pilot_build_log": inventory_file(ROOT / "logs/a1294_pilot_build_final.log"),
            "aborted_a1290_target_log": inventory_file(
                ROOT / "logs/upstream_a1290_certificate_build_aborted_oversized.log"
            ),
        },
        "upstream_relevant_files": [inventory_file(p) for p in upstream_files],
        "build_decisions": {
            "affine_tree_module": "PASS",
            "a1294_pilot_module": "PASS",
            "a1290_certificate_target": "INTERRUPTED_AFTER_LAKE_GRAPH_EXPANDED_TO_55731_JOBS",
            "full_a1294_theorem": "NOT_YET_PROVED",
        },
        "mathlib_distribution_note": "The exact Mathlib revision is pinned and was restored for the build; its source/cache is not bundled in this packet.",
    }
    (ROOT / "SOURCE_HASH_INVENTORY.json").write_text(
        json.dumps(source_inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    files = sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and p.name != "SHA256SUMS.json"
    )
    manifest = {
        "schema": "sha256-file-manifest-v1",
        "root": ".",
        "self_excluded": "SHA256SUMS.json does not hash itself; the final ZIP hash is reported separately.",
        "files": [inventory_file(p) for p in files],
    }
    (ROOT / "SHA256SUMS.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
