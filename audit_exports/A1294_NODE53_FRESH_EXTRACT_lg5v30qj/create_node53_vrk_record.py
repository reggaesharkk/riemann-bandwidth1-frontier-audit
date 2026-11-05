from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VRK_SOURCE = ROOT / "reference_predecessor/A1294_CATALOG18_IDENTITY_20261105/reference"
sys.path.insert(0, str(VRK_SOURCE))
from vrk.canonical import digest_object, sha256_file
from vrk.evidence import evidence_root

EVIDENCE_PATHS = [
    ("node55-predecessor-archive", "reference_inputs/A1294_NODE55_TERMINAL17_PROOF_PACKET_20261105.zip"),
    ("frozen-v2-archive", "reference_inputs/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"),
    ("terminal16-reconstructed-input", "terminal16_authentic_input.json"),
    ("terminal16-catalog-identity-proof", "Catalog16Identity.lean"),
    ("terminal16-all-original-lookups-proof", "Catalog16AllLookups.lean"),
    ("terminal16-acceptance-proof", "Terminal16Compositional.lean"),
    ("terminal16-acceptance-object", "Terminal16Compositional.olean"),
    ("node53-replay-proof", "Node53Replay.lean"),
    ("node53-replay-object", "Node53Replay.olean"),
    ("python-independent-source-check", "verify_terminal16_reconstruction.py"),
    ("pinned-environment-record", "ENVIRONMENT_CHECK.log"),
]

CLAIMS = [
    {
        "name": "terminal16_quadratic_acceptance",
        "status": "KERNEL_PROVED",
        "proposition": "AuthenticCompact16.accepted_original is true for the generated 15-row/357-segment compact payload over Catalog16.original.",
    },
    {
        "name": "terminal16_leaf_soundness",
        "status": "KERNEL_PROVED",
        "proposition": "The accepted terminal-16 tangent data implies the upstream affine energy goal on AuthenticCompact16.box.",
    },
    {
        "name": "node53_replay",
        "status": "KERNEL_PROVED",
        "proposition": "The decoded node-53 subtree replays with exact terminal/payload cursor pair (15,8).",
    },
    {
        "name": "node53_source_connected_predicate",
        "status": "KERNEL_PROVED_OVER_COMPILED_SOURCE_LITERALS",
        "proposition": "The node-53 source adapter and accepted replay imply BoxPredicate (affineEnergyGoal A B) A1294Source.box37 for the compiled source literals.",
    },
    {
        "name": "v2_byte_stream_to_lean_literals",
        "status": "EXTERNALLY_CHECKED",
        "proposition": "The independent Python replay compares frozen V2 bytes and catalogs to the generated Lean literals; this conversion is not proved by Lean.",
    },
    {
        "name": "catalog_selection_algorithm_correspondence",
        "status": "EXTERNALLY_CHECKED",
        "proposition": "The frozen deterministic model selector output is compared to generated terminal-16 catalog/row/segment data by exact external verification.",
    },
    {
        "name": "full_initial_root_predicate",
        "status": "INCOMPLETE",
        "proposition": "No proof of BoxPredicate for initialGapBox 60 or complete A1294 theorem is provided by this packet.",
    },
]

def main() -> None:
    evidence = []
    for role, rel in EVIDENCE_PATHS:
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(path)
        evidence.append({"role": role, "path": rel, "sha256": sha256_file(path)})
    claims = []
    for original in CLAIMS:
        claim = dict(original)
        claim["claim_digest"] = digest_object(claim)
        claims.append(claim)
    body = {
        "schema": "a1294-vrk-claim-evidence-v1",
        "project": "A1294 terminal-16 acceptance and source-connected node-53 replay",
        "claims": claims,
        "evidence": evidence,
        "evidence_root": evidence_root(evidence),
        "source_environment": {
            "formal_math_commit": "fba91d214655aaa1fd0504bb893c8859c20c79f9",
            "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
            "lean_toolchain": "leanprover/lean4:v4.33.0-rc2",
            "lean_commit": "d8b18978322de05a8f3dba51ef03cf5461676c17",
            "lake_version": "5.0.0-src+d8b1897",
            "lake_manifest_sha256": "1847b362e15efd927e75aa8b5442e491f998e4a3f730f9dcaca9841f2957c448",
        },
        "authentication": "Unsigned local provenance record; no protocol-signed ledger, external trust anchor, source-byte parser theorem, or mathematical proof is supplied by the record itself.",
    }
    body["record_digest"] = digest_object(body)
    (ROOT / "VRK_CLAIM_EVIDENCE.json").write_text(
        json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("VRK_RECORD_CREATED", body["record_digest"], body["evidence_root"])

if __name__ == "__main__":
    main()
