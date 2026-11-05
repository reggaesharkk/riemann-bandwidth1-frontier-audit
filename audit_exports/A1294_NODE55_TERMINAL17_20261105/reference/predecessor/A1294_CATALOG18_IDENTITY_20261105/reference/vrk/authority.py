from __future__ import annotations

import hmac
import secrets
import time
from hashlib import sha256
from typing import Any

from .canonical import canonical_json_bytes


def issue_authority_receipt(
    *, key: bytes, actor: str, claim_digest: str, publish_status: str,
    certificate_digest: str | None = None, proposition_digest: str | None = None,
    evidence_root: str | None = None,
    audience: str = "intentseal-vrk", issuer: str = "intentseal-authority",
    key_id: str = "hmac-demo-key", policy_ref: str = "default-publication-policy",
    ttl_seconds: int = 300, now: float | None = None, nonce: str | None = None,
) -> dict[str, Any]:
    """Prototype authority seal.

    v1 binds claim digest + exact epistemic label.  When certificate_digest is
    provided, v2 additionally binds the deterministic scientific certificate,
    proposition identity and evidence root.  HMAC remains intentionally symmetric;
    this is a prototype authorization mechanism, not a public signature scheme.
    """
    if ttl_seconds <= 0:
        raise ValueError("ttl_seconds must be positive")
    issued = float(time.time() if now is None else now)
    v2 = certificate_digest is not None
    if v2:
        for name, value in (("certificate_digest", certificate_digest), ("proposition_digest", proposition_digest), ("evidence_root", evidence_root)):
            if not isinstance(value, str) or len(value) != 64:
                raise ValueError(f"{name} must be SHA-256 hex for authority v2")
    body: dict[str, Any] = {
        "schema": "intentseal-vrk-authority-v2" if v2 else "intentseal-vrk-authority-v1",
        "actor": actor,
        "action": "publish_claim",
        "claim_digest": claim_digest,
        "publish_status": publish_status,
        "audience": audience,
        "issuer": issuer,
        "key_id": key_id,
        "policy_ref": policy_ref,
        "issued_at": issued,
        "expires_at": issued + ttl_seconds,
        "nonce": nonce or secrets.token_hex(16),
    }
    if v2:
        body.update({
            "certificate_digest": certificate_digest,
            "proposition_digest": proposition_digest,
            "evidence_root": evidence_root,
        })
    body["mac"] = hmac.new(key, canonical_json_bytes(body), sha256).hexdigest()
    return body


def verify_authority_receipt(
    receipt: dict[str, Any], *, key: bytes, claim_digest: str,
    publish_status: str, actor: str | None = None,
    certificate_digest: str | None = None, proposition_digest: str | None = None,
    evidence_root: str | None = None,
    audience: str = "intentseal-vrk", now: float | None = None,
) -> tuple[bool, str]:
    try:
        mac = receipt["mac"]
        unsigned = dict(receipt); unsigned.pop("mac")
        expected = hmac.new(key, canonical_json_bytes(unsigned), sha256).hexdigest()
        if not hmac.compare_digest(mac, expected):
            return False, "authority MAC mismatch"
        schema = receipt.get("schema")
        if schema not in {"intentseal-vrk-authority-v1", "intentseal-vrk-authority-v2"}:
            return False, "authority schema mismatch"
        if receipt.get("action") != "publish_claim":
            return False, "authority action mismatch"
        if receipt.get("claim_digest") != claim_digest:
            return False, "authority claim digest mismatch"
        if receipt.get("publish_status") != publish_status:
            return False, "authority epistemic-label mismatch"
        if receipt.get("audience") != audience:
            return False, "authority audience mismatch"
        for field in ("issuer", "key_id", "policy_ref"):
            if not isinstance(receipt.get(field), str) or not receipt.get(field):
                return False, f"authority {field} missing"
        if actor is not None and receipt.get("actor") != actor:
            return False, "authority actor mismatch"
        if schema == "intentseal-vrk-authority-v2":
            expected_v2 = {
                "certificate_digest": certificate_digest,
                "proposition_digest": proposition_digest,
                "evidence_root": evidence_root,
            }
            for field, value in expected_v2.items():
                if not isinstance(value, str) or len(value) != 64:
                    return False, f"authority verifier missing expected {field}"
                if receipt.get(field) != value:
                    return False, f"authority {field} mismatch"
        elif any(v is not None for v in (certificate_digest, proposition_digest, evidence_root)):
            return False, "authority v1 cannot satisfy certificate-bound verification"
        t = float(time.time() if now is None else now)
        if t < float(receipt["issued_at"]):
            return False, "authority not yet valid"
        if t > float(receipt["expires_at"]):
            return False, "authority expired"
        return True, "authority receipt valid"
    except Exception as e:
        return False, f"malformed authority receipt: {e}"
