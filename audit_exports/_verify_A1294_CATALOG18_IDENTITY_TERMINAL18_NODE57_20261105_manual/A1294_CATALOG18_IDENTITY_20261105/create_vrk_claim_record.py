from __future__ import annotations

import json
from pathlib import Path

from vrk.canonical import digest_object, sha256_file
from vrk.evidence import evidence_root

ROOT = Path(__file__).resolve().parent
EVIDENCE_PATHS = [
    ("frozen-input", "reference/input/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"),
    ("predecessor-record", "reference/checkpoints/A1294_VRK_INTENTSEAL_BRIDGE_CHECKPOINT_20261105.zip"),
    ("terminal18-source-checkpoint", "reference/checkpoints/A1294_NODE57_AUTHENTIC_TERMINAL18_INCOMPLETE_20261105.zip"),
    ("terminal19-predecessor", "reference/checkpoints/A1294_NODE59_TERMINAL19_SOURCE_CONNECTED_20261105.zip"),
    ("generic-array-proof", "generic_linux/GenericArrayIdentity.lean"),
    ("catalog-identity-proof", "Catalog18Identity.lean"),
    ("all-catalog-lookups-proof", "Catalog18AllLookups.lean"),
    ("historical-catalog-connection-proof", "Terminal18CatalogConnection.lean"),
    ("terminal18-acceptance-proof", "Terminal18Compositional.lean"),
    ("historical-terminal18-acceptance-proof", "Terminal18HistoricalAcceptance.lean"),
    ("node57-source-geometry-proof", "Source57.lean"),
    ("node57-helper-proof", "Node57Helpers.lean"),
    ("node57-replay-proof", "Node57Replay.lean"),
    ("node57-final-proof", "Node57Final.lean"),
    ("source-catalog-reconstruction-check", "verify_catalog_source.py"),
    ("terminal18-exact-provenance-check", "verify_terminal18_provenance.py"),
    ("archive-identity-check", "verify_archive_inputs.py"),
    ("final-published-lineage", "reference/lineage/IntentSeal_lineage_final_published.zip"),
    ("historical-lineage-inventory", "reference/lineage/IntentSeal_lineage_historical_inventory.zip"),
    ("vrk-canonical-code", "reference/vrk/canonical.py"),
    ("vrk-evidence-code", "reference/vrk/evidence.py"),
]
evidence = []
for role, rel in EVIDENCE_PATHS:
    path = ROOT / rel
    if not path.is_file():
        raise FileNotFoundError(path)
    evidence.append({"role": role, "path": rel, "sha256": sha256_file(path)})

claims = [
    {"name": "generic_array_split", "status": "KERNEL_PROVED", "proposition": "For all element types and lists xs ys zs, ((xs ++ ys) ++ zs).toArray = (xs.toArray ++ ys.toArray) ++ zs.toArray; concrete six/nine-element examples follow."},
    {"name": "original_catalog_identity", "status": "KERNEL_PROVED", "proposition": "Catalog18.original = Catalog18.catalog for the exact 171 declaration references and 57+57+57 order in the Lean modules."},
    {"name": "historical_terminal18_catalog_connection", "status": "KERNEL_PROVED", "proposition": "The historical inline terminal-18 catalog expression equals Catalog18.original and hence Catalog18.catalog."},
    {"name": "terminal18_acceptance", "status": "KERNEL_PROVED", "proposition": "The supplied terminal-18 compact leaf checker evaluates to true on the historical catalog expression and upstream soundness yields the leaf box predicate."},
    {"name": "node57_bounded_replay", "status": "KERNEL_PROVED", "proposition": "The supplied node-57 source structure replays with exact exhaustion (11 topology entries, 6 payloads) and upstream soundness yields its parent BoxPredicate."},
    {"name": "v2_bytes_to_lean_literals", "status": "EXTERNALLY_CHECKED", "proposition": "Python/source checks compare frozen V2 bytes, catalog-selection output, and supplied Lean literals; this is not proved by the Lean kernel."},
    {"name": "full_root_predicate", "status": "INCOMPLETE", "proposition": "The initial root BoxPredicate and complete A1294 theorem have not been established."},
]
for claim in claims:
    claim["claim_digest"] = digest_object(claim)

body = {
    "schema": "a1294-vrk-claim-evidence-v1",
    "project": "A1294 terminal-18 catalog identity and bounded node-57 replay",
    "claim_digest_algorithm": "sha256-canonical-json-v1",
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
    "authentication": "Unsigned local evidence record. Hashes bind file identities only. No signature, external trust anchor, byte-parser theorem, or mathematical proof is supplied by this record.",
}
body["record_digest"] = digest_object(body)
(ROOT / "VRK_CLAIM_EVIDENCE.json").write_text(json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("wrote VRK_CLAIM_EVIDENCE.json", body["record_digest"], body["evidence_root"])
