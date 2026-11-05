from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKTREE = ROOT.parents[1]


def digest(path: Path) -> tuple[str, int]:
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            size += len(chunk)
            h.update(chunk)
    return h.hexdigest(), size


def entry(role: str, rel: str) -> dict[str, object]:
    path = ROOT / rel
    sha, size = digest(path)
    return {"role": role, "path": rel, "bytes": size, "sha256": sha}


def main() -> int:
    inputs = json.loads((ROOT / "terminal15_authentic_input.json").read_text(encoding="utf-8-sig"))
    files = [
        ("input_v4_packet", "reference_inputs/A1294_NODE53_TERMINAL16_PROOF_PACKET_V4_20261105.zip"),
        ("frozen_v2_package", "reference_inputs/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"),
        ("terminal15_source_record", "terminal15_authentic_input.json"),
        ("source_extractor", "extract15_reconstruct.py"),
        ("independent_exact_verifier", "verify15_reconstruction.py"),
        ("catalog_generator", "generate_terminal15_catalog.py"),
        ("leaf_literal_generator", "generate_terminal15_compositional.py"),
        ("catalog_array", "Catalog15.lean"),
        ("catalog_identity_proof", "Catalog15Identity.lean"),
        ("catalog_boundary_proofs", "Catalog15BoundaryBlocks.lean"),
        ("catalog_lookup_proofs", "Catalog15AllLookups.lean"),
        ("leaf_acceptance_source", "Terminal15Compositional.lean"),
        ("leaf_acceptance_object", "Terminal15Compositional.olean"),
        ("node51_replay_template", "Node51Replay.lean.template"),
        ("node51_replay_generator", "generate_node51_replay.py"),
        ("generator_negative_controls", "test_node51_generator_rejections.py"),
        ("node51_replay_source", "Node51Replay.lean"),
        ("node51_replay_object", "Node51Replay.olean"),
        ("generated_node51_replay_source", "Node51Replay.generated.lean"),
        ("node53_predecessor_source", "reference_dependencies/Node53Replay.lean"),
        ("node53_predecessor_object", "reference_dependencies/Node53Replay.olean"),
        ("v4_predecessor_manifest_copy", "reference_dependencies/V4_SHA256SUMS.txt"),
        ("proof_decisions", "DECISIONS.json"),
        ("mathematical_report", "REPORT.md"),
        ("bulk_generation_report", "BULK_GENERATION.md"),
        ("resource_benchmark", "RESOURCE_BENCHMARK.json"),
        ("vrk_source_canonical", "reference_dependencies/vrk/canonical.py"),
        ("vrk_source_evidence", "reference_dependencies/vrk/evidence.py"),
        ("protocol_manifest_verifier", "protocol/verify_candidate_manifest.py"),
        ("environment_check", "ENVIRONMENT_CHECK.log"),
    ]
    artifacts = [entry(role, rel) for role, rel in files]
    source_hashes = {
        **{f"stream_{k}": v for k, v in inputs["source_stream_sha256"].items()},
        **{f"catalog_{k}": v for k, v in inputs["source_input_sha256"].items()},
    }
    local_head = subprocess.check_output(["git", "-C", str(WORKTREE), "rev-parse", "HEAD"], text=True).strip()
    inventory = {
        "scope": "Terminal 15 / node 51 bounded proof packet; no full-certificate authentication claimed",
        "local_worktree_head": local_head,
        "pinned_environment": {
            "formal_math_commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
            "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
            "lean_commit": "d8b18978322de05a8f3dba51ef03cf5461676c17",
            "lake": "5.0.0-src+d8b1897",
            "lake_manifest_sha256": "1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448",
        },
        "frozen_source_stream_and_catalog_hashes": source_hashes,
        "artifact_hashes": artifacts,
        "authenticity_boundary": "The archive and file hashes identify these local bytes. Source stream to Lean literal translation and deterministic catalog selection remain externally replayed, not kernel proved.",
    }
    (ROOT / "SOURCE_HASH_INVENTORY.json").write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"SOURCE_INVENTORY_WRITTEN artifacts={len(artifacts)} local_head={local_head}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
