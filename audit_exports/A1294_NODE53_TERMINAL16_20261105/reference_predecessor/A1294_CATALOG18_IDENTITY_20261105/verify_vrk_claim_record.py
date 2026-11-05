from __future__ import annotations

import json
from pathlib import Path

from vrk.canonical import digest_object, sha256_file
from vrk.evidence import evidence_root


ROOT = Path(__file__).resolve().parent
record = json.loads((ROOT / "VRK_CLAIM_EVIDENCE.json").read_text(encoding="utf-8"))
if record["schema"] != "a1294-vrk-claim-evidence-v1":
    raise RuntimeError("unexpected claim/evidence schema")
for evidence in record["evidence"]:
    path = ROOT / evidence["path"]
    if not path.is_file():
        raise RuntimeError(f"missing evidence file: {evidence['path']}")
    if sha256_file(path) != evidence["sha256"]:
        raise RuntimeError(f"evidence hash mismatch: {evidence['path']}")
if evidence_root(record["evidence"]) != record["evidence_root"]:
    raise RuntimeError("evidence root mismatch")
for claim in record["claims"]:
    expected = digest_object({k: v for k, v in claim.items() if k != "claim_digest"})
    if claim["claim_digest"] != expected:
        raise RuntimeError(f"claim digest mismatch: {claim['name']}")
body = {k: v for k, v in record.items() if k != "record_digest"}
if record["record_digest"] != digest_object(body):
    raise RuntimeError("record digest mismatch")
lineage = json.loads((ROOT / "lineage_identification.json").read_text(encoding="utf-8"))
if lineage["intentseal_verification_kernel_lineage_final_published_v0_1_1_to_v0_5_0"]["sha256"] != "05ba923c90dfc481a70a3784b72d1cd71a0adeac2c34a22631169f545ae5d4c0":
    raise RuntimeError("final published lineage hash misidentified")
if lineage["intentseal_verification_kernel_lineage_historical_inventory"]["sha256"] != "14f920b5fcb970f8a97eaf98aa80c83e8ff4125bb85e311705f86edad5dd56db":
    raise RuntimeError("historical lineage inventory hash mismatch")
print("PASS VRK canonical claim digests, local file hashes, evidence root, record digest, and separate final/historical lineage identities")
print("STATUS IS PROVENANCE ONLY; it does not authenticate mathematical truth or source bytes in Lean")
