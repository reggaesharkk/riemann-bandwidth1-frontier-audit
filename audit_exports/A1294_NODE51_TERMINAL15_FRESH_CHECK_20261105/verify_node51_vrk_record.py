from __future__ import annotations

import json
from pathlib import Path

from reference_dependencies.vrk.canonical import digest_object, sha256_file
from reference_dependencies.vrk.evidence import evidence_root

ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    record = json.loads((ROOT / "VRK_CLAIM_EVIDENCE.json").read_text(encoding="utf-8"))
    require(record.get("schema") == "a1294-vrk-claim-evidence-v1", "schema mismatch")
    for evidence in record["evidence"]:
        path = ROOT / evidence["path"]
        require(path.is_file(), f"missing evidence: {evidence['path']}")
        require(sha256_file(path) == evidence["sha256"], f"evidence digest mismatch: {evidence['path']}")
    require(evidence_root(record["evidence"]) == record["evidence_root"], "evidence-root mismatch")
    for claim in record["claims"]:
        unsigned = {key: value for key, value in claim.items() if key != "claim_digest"}
        require(digest_object(unsigned) == claim["claim_digest"], f"claim digest mismatch: {claim.get('name')}")
    unsigned_record = {key: value for key, value in record.items() if key != "record_digest"}
    require(digest_object(unsigned_record) == record["record_digest"], "record digest mismatch")
    require(any(claim["name"] == "complete_initial_root_predicate" and claim["status"] == "INCOMPLETE"
                for claim in record["claims"]), "root status was promoted")
    print("PASS VRK canonical evidence hashes, evidence root, claim digests and record digest")
    print("STATUS=UNSIGNED_PROVENANCE_ONLY; no Lean theorem or source authenticity was inferred from hashes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
