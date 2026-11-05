from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VRK_SOURCE = ROOT / "reference_predecessor/A1294_CATALOG18_IDENTITY_20261105/reference"
sys.path.insert(0, str(VRK_SOURCE))
from vrk.canonical import digest_object, sha256_file
from vrk.evidence import evidence_root

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

def main() -> None:
    record = json.loads((ROOT / "VRK_CLAIM_EVIDENCE.json").read_text(encoding="utf-8"))
    require(record.get("schema") == "a1294-vrk-claim-evidence-v1", "schema mismatch")
    for evidence in record["evidence"]:
        path = ROOT / evidence["path"]
        require(path.is_file(), f"missing evidence: {evidence['path']}")
        require(sha256_file(path) == evidence["sha256"], f"evidence digest mismatch: {evidence['path']}")
    require(evidence_root(record["evidence"]) == record["evidence_root"], "evidence-root mismatch")
    for claim in record["claims"]:
        original = {k: v for k, v in claim.items() if k != "claim_digest"}
        require(digest_object(original) == claim["claim_digest"], f"claim digest mismatch: {claim.get('name')}")
    body = {k: v for k, v in record.items() if k != "record_digest"}
    require(digest_object(body) == record["record_digest"], "record digest mismatch")
    require(any(c["name"] == "full_initial_root_predicate" and c["status"] == "INCOMPLETE" for c in record["claims"]), "root status not kept open")
    print("PASS VRK canonical digests, evidence hashes, and evidence root")
    print("STATUS=UNSIGNED_PROVENANCE_ONLY; no Lean theorem was inferred from hashes")

if __name__ == "__main__":
    main()
