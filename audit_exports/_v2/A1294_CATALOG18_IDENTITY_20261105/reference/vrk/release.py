from __future__ import annotations

import hashlib
import math
from pathlib import Path
from typing import Any

from .canonical import canonical_json_bytes
from .promotion import verify_promotion_receipt
from .capsule import verify_capsule
from .trust import verify_trust_root, verify_external_anchor

FORBIDDEN_TELEMETRY_KEYS = {
    "platform", "architecture", "python", "compiler", "compile_flags",
    "stage_seconds", "total_seconds", "seconds", "hostname", "pid", "timestamp",
}


def canonical_certificate_bytes(certificate: dict[str, Any]) -> bytes:
    return canonical_json_bytes(certificate) + b"\n"


def certificate_digest(certificate: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_certificate_bytes(certificate)).hexdigest()


def _contains_forbidden_key(value: Any) -> str | None:
    if isinstance(value, dict):
        for k, v in value.items():
            if k in FORBIDDEN_TELEMETRY_KEYS:
                return k
            hit = _contains_forbidden_key(v)
            if hit:
                return hit
    elif isinstance(value, list):
        for v in value:
            hit = _contains_forbidden_key(v)
            if hit:
                return hit
    return None


def verify_deterministic_certificate(
    certificate: dict[str, Any], *, root: str | Path,
    trust_root_path: str | Path, external_anchor_path: str | Path,
) -> tuple[bool, str]:
    try:
        if certificate.get("schema") != "intentseal-vrk-deterministic-certificate-v2":
            return False, "deterministic certificate schema mismatch"
        forbidden = _contains_forbidden_key(certificate)
        if forbidden:
            return False, f"telemetry key leaked into deterministic certificate: {forbidden}"
        if certificate.get("claim_id") != "lrsc.m99.theta007.k0001.eq14":
            return False, "certificate claim id mismatch"
        if certificate.get("claim_class") != "EXHAUSTIVE_FINITE_RESULT":
            return False, "certificate claim class mismatch"
        if certificate.get("epistemic_result") != "CERTIFIED":
            return False, "certificate epistemic result is not CERTIFIED"
        expected_params = {"M": 99, "k_idx": 49, "A": "1/2", "theta": "0.07", "relative_tolerance": "1e-3"}
        if certificate.get("parameters") != expected_params:
            return False, "certificate parameters mismatch"
        searches = certificate.get("searches", [])
        if len(searches) != 13 or [x.get("K") for x in searches] != list(range(1, 14)):
            return False, "certificate K1..K13 rows incomplete"
        total = 1
        for row in searches:
            k = int(row["K"]); expected = math.comb(50, k)
            if row.get("covered") != expected or row.get("expected") != expected:
                return False, f"certificate K{k} coverage mismatch"
            if row.get("capped") or row.get("unresolved") or row.get("status") != "PROVED_NO_PASS_AT_K":
                return False, f"certificate K{k} search incomplete"
            total += expected
        expected_total = sum(math.comb(50, k) for k in range(14))
        if total != expected_total or certificate.get("coverage_total_K0_to_K13") != expected_total or certificate.get("coverage_expected_K0_to_K13") != expected_total:
            return False, "certificate aggregate coverage mismatch"
        w = certificate.get("K14_witness", {})
        if w.get("subset") != [0, 1, 2, 4, 5, 6, 42, 43, 44, 45, 46, 47, 48, 49]:
            return False, "certificate K14 witness mismatch"
        upper = int(w["residual_r2_interval_scaled_1e35"][1])
        lower = int(w["target_norm2_interval_scaled_1e35"][0])
        if upper * 10**6 >= lower or certificate.get("K14_integer_gate_pass") is not True:
            return False, "certificate K14 integer gate failed"
        perm = certificate.get("channel_permutation", [])
        if sorted(perm) != list(range(50)) or len(set(perm)) != 50:
            return False, "certificate channel permutation is not a bijection"
        ok, detail, trust = verify_trust_root(root, trust_root_path)
        if not ok:
            return False, detail
        if certificate.get("trust_root_digest") != trust.get("trust_root_digest"):
            return False, "certificate trust-root digest mismatch"
        ok2, detail2, anchor = verify_external_anchor(trust_root_path, external_anchor_path)
        if not ok2:
            return False, detail2
        if certificate.get("external_source_anchor") != {
            "repository": anchor.get("repository"),
            "commit": anchor.get("commit"),
            "path": anchor.get("path"),
            "git_blob_sha": anchor.get("git_blob_sha"),
        }:
            return False, "certificate external source anchor mismatch"
        if certificate.get("independent_post_run_verification") is not True:
            return False, "certificate independent recheck flag missing"
        return True, f"deterministic certificate valid; {detail}; {detail2}"
    except Exception as e:
        return False, f"malformed deterministic certificate: {type(e).__name__}: {e}"


def verify_release_bundle(
    *, certificate: dict[str, Any], promotion: dict[str, Any], old_receipt: dict[str, Any],
    new_receipt: dict[str, Any], capsule: dict[str, Any], authority_key: bytes,
    root: str | Path, trust_root_path: str | Path, external_anchor_path: str | Path,
    now: float,
) -> tuple[bool, str]:
    ok, detail = verify_deterministic_certificate(
        certificate, root=root, trust_root_path=trust_root_path, external_anchor_path=external_anchor_path,
    )
    if not ok:
        return False, detail
    cd = certificate_digest(certificate)
    ok, detail = verify_promotion_receipt(promotion, old_receipt, new_receipt, certificate_digest=cd)
    if not ok:
        return False, detail
    if capsule.get("certificate_digest") != cd:
        return False, "capsule/certificate digest mismatch"
    ok, detail = verify_capsule(capsule, authority_key=authority_key, now=now)
    if not ok:
        return False, detail
    return True, "deterministic certificate + promotion + certificate-bound authority capsule valid"
