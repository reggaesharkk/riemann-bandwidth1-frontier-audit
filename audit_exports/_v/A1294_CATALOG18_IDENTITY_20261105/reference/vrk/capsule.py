from __future__ import annotations

from typing import Any

from .authority import verify_authority_receipt
from .canonical import digest_object

PUBLISHABLE_STATUSES = {"EVIDENCE_BOUND", "LOCALLY_REPLAYED", "CERTIFIED"}


def build_capsule(
    verification_receipt: dict[str, Any], authority_receipt: dict[str, Any], *,
    certificate_digest: str | None = None,
) -> dict[str, Any]:
    v2 = certificate_digest is not None
    body: dict[str, Any] = {
        "schema": "intentseal-vrk-capsule-v2" if v2 else "intentseal-vrk-capsule-v1",
        "claim_id": verification_receipt["claim_id"],
        "claim_digest": verification_receipt["claim_digest"],
        "epistemic_status": verification_receipt["kernel_status"],
        "evidence_root": verification_receipt["evidence_root"],
        "verification_receipt": verification_receipt,
        "authority_receipt": authority_receipt,
    }
    if v2:
        if not isinstance(certificate_digest, str) or len(certificate_digest) != 64:
            raise ValueError("certificate_digest must be SHA-256 hex")
        body.update({
            "proposition_digest": verification_receipt["proposition_digest"],
            "dependency_root": verification_receipt["dependency_root"],
            "certificate_digest": certificate_digest,
        })
    body["capsule_digest"] = digest_object(body)
    return body


def verify_capsule(capsule: dict[str, Any], *, authority_key: bytes, now: float | None = None) -> tuple[bool, str]:
    schema = capsule.get("schema")
    if schema not in {"intentseal-vrk-capsule-v1", "intentseal-vrk-capsule-v2"}:
        return False, "capsule schema mismatch"
    vr = capsule.get("verification_receipt", {})
    ar = capsule.get("authority_receipt", {})
    if vr.get("claim_digest") != capsule.get("claim_digest"):
        return False, "verification/claim digest mismatch"
    if vr.get("kernel_status") != capsule.get("epistemic_status"):
        return False, "verification/status mismatch"
    if vr.get("evidence_root") != capsule.get("evidence_root"):
        return False, "verification/evidence root mismatch"
    if vr.get("kernel_status") not in PUBLISHABLE_STATUSES or not vr.get("pass"):
        return False, "claim is not publishable at stated epistemic status"
    kwargs: dict[str, Any] = {}
    if schema == "intentseal-vrk-capsule-v2":
        for field in ("proposition_digest", "dependency_root"):
            if vr.get(field) != capsule.get(field):
                return False, f"verification/{field} mismatch"
        cert = capsule.get("certificate_digest")
        if not isinstance(cert, str) or len(cert) != 64:
            return False, "certificate digest missing from capsule"
        kwargs = {
            "certificate_digest": cert,
            "proposition_digest": vr["proposition_digest"],
            "evidence_root": vr["evidence_root"],
        }
    ok, detail = verify_authority_receipt(
        ar, key=authority_key, claim_digest=vr["claim_digest"],
        publish_status=vr["kernel_status"], now=now, **kwargs,
    )
    if not ok:
        return False, detail
    unsigned = dict(capsule); claimed = unsigned.pop("capsule_digest", None)
    if digest_object(unsigned) != claimed:
        return False, "capsule digest mismatch"
    return True, "authority + evidence dual seal valid"
