from __future__ import annotations

import json
from pathlib import Path

from reference_dependencies.vrk.canonical import digest_object, sha256_file
from reference_dependencies.vrk.evidence import evidence_root

ROOT = Path(__file__).resolve().parent
EVIDENCE_PATHS = [
    ("v4-predecessor-archive", "reference_inputs/A1294_NODE53_TERMINAL16_PROOF_PACKET_V4_20261105.zip"),
    ("frozen-v2-source-archive", "reference_inputs/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"),
    ("terminal15-source-reconstruction", "terminal15_authentic_input.json"),
    ("terminal15-independent-reconstruction-checker", "verify15_reconstruction.py"),
    ("terminal15-catalog-identity-proof", "Catalog15Identity.lean"),
    ("terminal15-catalog-lookup-proofs", "Catalog15AllLookups.lean"),
    ("terminal15-acceptance-proof", "Terminal15Compositional.lean"),
    ("terminal15-acceptance-object", "Terminal15Compositional.olean"),
    ("node51-replay-proof", "Node51Replay.lean"),
    ("node51-replay-object", "Node51Replay.olean"),
    ("reused-node53-proof", "reference_dependencies/Node53Replay.lean"),
    ("reused-node53-object", "reference_dependencies/Node53Replay.olean"),
    ("source-bound-multileaf-generator", "generate_node51_replay.py"),
    ("generator-mutation-tests", "test_node51_generator_rejections.py"),
    ("generator-mutation-test-results", "generator_rejection_tests_normal.log"),
    ("generated-multileaf-replay-source", "Node51Replay.generated.lean"),
    ("resource-measurements", "RESOURCE_BENCHMARK.json"),
    ("mathematical-proof-report", "REPORT.md"),
    ("bounded-generator-feasibility-report", "BULK_GENERATION.md"),
    ("proof-decisions", "DECISIONS.json"),
    ("source-hash-inventory", "SOURCE_HASH_INVENTORY.json"),
    ("pinned-environment-check", "ENVIRONMENT_CHECK.log"),
]

CLAIMS = [
    {
        "name": "terminal15_compact_acceptance",
        "status": "KERNEL_PROVED",
        "proposition": "AuthenticCompact15.accepted_original is true for the recovered terminal-15 source payload over Catalog15.original.",
    },
    {
        "name": "terminal15_leaf_soundness",
        "status": "KERNEL_PROVED",
        "proposition": "The accepted exact tangent data implies the upstream affine energy goal on AuthenticCompact15.box.",
    },
    {
        "name": "node51_replay_and_cursor_exhaustion",
        "status": "KERNEL_PROVED",
        "proposition": "The 17-token/9-payload node-51 replay consumes exactly (17,9), reusing Node53.replay53.",
    },
    {
        "name": "node51_source_connected_boxpredicate",
        "status": "KERNEL_PROVED_OVER_COMPILED_SOURCE_LITERALS",
        "proposition": "The source path, literal topology/kinds/anchors and accepted replay imply BoxPredicate (affineEnergyGoal A B) A1294Source.box36.",
    },
    {
        "name": "v2_source_byte_to_lean_literal_correspondence",
        "status": "EXTERNALLY_CHECKED",
        "proposition": "The independent verifier compares the frozen V2 source streams and catalogs to the compiled Lean literal data; that conversion is not proved in Lean.",
    },
    {
        "name": "deterministic_catalog_selection_correspondence",
        "status": "EXTERNALLY_CHECKED",
        "proposition": "The exact Python verifier recomputes all fifteen model selections and their segment intervals from the frozen catalogs; Lean proves the resulting compact payload checks, not the selector implementation's equivalence to the source algorithm.",
    },
    {
        "name": "complete_initial_root_predicate",
        "status": "INCOMPLETE",
        "proposition": "This chunk proves no BoxPredicate for initialGapBox 60 and no complete A1294 theorem.",
    },
]


def main() -> None:
    evidence = []
    for role, relative in EVIDENCE_PATHS:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        evidence.append({"role": role, "path": relative, "sha256": sha256_file(path)})
    claims = []
    for original in CLAIMS:
        claim = dict(original)
        claim["claim_digest"] = digest_object(claim)
        claims.append(claim)
    body = {
        "schema": "a1294-vrk-claim-evidence-v1",
        "project": "A1294 authentic terminal-15 acceptance and source-connected node-51 replay",
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
        "authentication": "Unsigned local provenance record using the archived VRK canonical digest and evidence-root implementation. It does not verify Lean proofs, authenticate the source publisher, prove byte-to-literal or selector correspondence, or provide a signed IntentSeal ledger/head.",
    }
    body["record_digest"] = digest_object(body)
    (ROOT / "VRK_CLAIM_EVIDENCE.json").write_text(
        json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"VRK_RECORD_CREATED record_digest={body['record_digest']} evidence_root={body['evidence_root']}")


if __name__ == "__main__":
    main()
