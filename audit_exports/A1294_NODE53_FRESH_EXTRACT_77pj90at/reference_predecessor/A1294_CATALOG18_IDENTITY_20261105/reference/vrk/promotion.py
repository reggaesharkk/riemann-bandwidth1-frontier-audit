from __future__ import annotations

from typing import Any

from .canonical import digest_object

ALLOWED = {
    "EVIDENCE_BOUND": {"EVIDENCE_BOUND", "LOCALLY_REPLAYED", "CERTIFIED"},
    "LOCALLY_REPLAYED": {"LOCALLY_REPLAYED", "CERTIFIED"},
    "CERTIFIED": {"CERTIFIED"},
}


def validate_promotion(old: dict, new: dict) -> tuple[bool, str]:
    if old.get("claim_id") != new.get("claim_id"):
        return False, "claim_id changed"
    if old.get("proposition_digest") != new.get("proposition_digest"):
        return False, "scientific proposition changed; this is a new claim, not a promotion"
    if old.get("claim_class") != new.get("claim_class"):
        return False, "claim class changed; reclassification requires a new claim record"
    if old.get("dependency_root") != new.get("dependency_root"):
        return False, "dependency set changed; promotion must not silently rewrite assumptions"
    old_s, new_s = old.get("kernel_status"), new.get("kernel_status")
    if new_s not in ALLOWED.get(old_s, set()):
        return False, f"illegal status transition {old_s}->{new_s}"
    if new_s == "CERTIFIED" and not new.get("certified"):
        return False, "CERTIFIED status without certified flag"
    return True, f"valid promotion {old_s}->{new_s} for unchanged proposition"


def build_promotion_receipt(old: dict[str, Any], new: dict[str, Any], *, certificate_digest: str) -> dict[str, Any]:
    ok, detail = validate_promotion(old, new)
    if not ok:
        raise ValueError(detail)
    if not isinstance(certificate_digest, str) or len(certificate_digest) != 64:
        raise ValueError("certificate_digest must be SHA-256 hex")
    body = {
        "schema": "intentseal-vrk-promotion-v1",
        "claim_id": new["claim_id"],
        "claim_class": new["claim_class"],
        "proposition_digest": new["proposition_digest"],
        "dependency_root": new["dependency_root"],
        "from_claim_digest": old["claim_digest"],
        "to_claim_digest": new["claim_digest"],
        "from_status": old["kernel_status"],
        "to_status": new["kernel_status"],
        "certificate_digest": certificate_digest,
    }
    body["promotion_digest"] = digest_object(body)
    return body


def verify_promotion_receipt(
    receipt: dict[str, Any], old: dict[str, Any], new: dict[str, Any], *, certificate_digest: str
) -> tuple[bool, str]:
    try:
        if receipt.get("schema") != "intentseal-vrk-promotion-v1":
            return False, "promotion schema mismatch"
        unsigned = dict(receipt)
        claimed = unsigned.pop("promotion_digest", None)
        if digest_object(unsigned) != claimed:
            return False, "promotion digest mismatch"
        ok, detail = validate_promotion(old, new)
        if not ok:
            return False, detail
        expected = {
            "claim_id": new.get("claim_id"),
            "claim_class": new.get("claim_class"),
            "proposition_digest": new.get("proposition_digest"),
            "dependency_root": new.get("dependency_root"),
            "from_claim_digest": old.get("claim_digest"),
            "to_claim_digest": new.get("claim_digest"),
            "from_status": old.get("kernel_status"),
            "to_status": new.get("kernel_status"),
            "certificate_digest": certificate_digest,
        }
        for k, v in expected.items():
            if receipt.get(k) != v:
                return False, f"promotion {k} mismatch"
        if new.get("kernel_status") == "CERTIFIED" and not new.get("certified"):
            return False, "promotion target lacks certified flag"
        return True, f"certificate-bound {detail}"
    except Exception as e:
        return False, f"malformed promotion receipt: {e}"
