from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from .verify import verify_claim
from .canonical import digest_object


def run_mutation_suite(claim_path: str | Path) -> dict:
    src = Path(claim_path).resolve()
    root = src.parent
    original = json.loads(src.read_text(encoding="utf-8"))
    cases = []

    def reseal_artifact(obj: dict, dst: Path, rel: str) -> None:
        p = dst / rel
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        for ev in obj["evidence"]:
            if ev.get("path") == rel:
                ev["sha256"] = h

    def case(name, mutator):
        with tempfile.TemporaryDirectory() as td:
            import shutil
            dst = Path(td) / "claimdir"
            shutil.copytree(root, dst)
            p = dst / src.name
            obj = json.loads(p.read_text(encoding="utf-8"))
            mutator(obj, dst)
            # Strong attacker model: semantic mutations are re-sealed. Rejection
            # must come from domain/evidence policy or fresh replay, not stale hashes.
            obj.pop("claim_digest", None)
            if obj.get("sealed"):
                obj["claim_digest"] = digest_object(obj)
            p.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
            try:
                result = verify_claim(p)
                rejected = not result["pass"]
                status = result["kernel_status"]
                failed = [c["name"] for c in result["checks"] if not c["ok"]]
            except Exception as e:
                rejected = True
                status = f"EXCEPTION:{type(e).__name__}"
                failed = [str(e)]
            cases.append({"name": name, "rejected": rejected, "status": status, "failed_checks": failed})

    case("silent_theorem_promotion", lambda o,d: o.__setitem__("claim_class", "ANALYTIC_THEOREM"))
    case("scope_boundary_deleted", lambda o,d: o["scope"].__setitem__("does_not_imply", []))
    case("claim_text_changed", lambda o,d: o.__setitem__("claim_text", o["claim_text"] + " Universal."))

    def mutate_hash(o, d):
        for ev in o["evidence"]:
            if ev.get("path"):
                ev["sha256"] = "0" * 64
                break
    case("evidence_hash_forged", mutate_hash)

    def mutate_plugin(o, d):
        for ev in o["evidence"]:
            if ev.get("role") == "passing_witness":
                ev.pop("plugin", None)
                break
    case("verifier_removed", mutate_plugin)

    def mutate_dependency(o, d):
        if o["dependencies"]:
            o["dependencies"][0].pop("claim_digest", None)
    case("dependency_digest_removed", mutate_dependency)

    def mutate_predicate(o, d):
        o["domain"]["predicate"]["value"] = 13
    case("predicate_value_changed", mutate_predicate)

    def mutate_tolerance(o, d):
        o["domain"]["parameters"]["relative_L2_tolerance"] = "1e-2"
    case("tolerance_widened", mutate_tolerance)

    def remove_independent(o, d):
        o["evidence"] = [ev for ev in o["evidence"] if ev.get("role") != "independent_verification"]
    case("independent_verification_removed", remove_independent)

    # Stronger attacks modify evidence and update ordinary SHA-256 bindings before
    # re-sealing the claim digest.
    def forge_coverage(o, d):
        rel = "replay/full_replay_manifest.json"
        p = d / rel
        m = json.loads(p.read_text())
        m["K1_to_K13"][-1]["covered"] -= 1
        p.write_text(json.dumps(m, indent=2) + "\n")
        reseal_artifact(o, d, rel)
    case("coverage_manifest_forged_and_rehashed", forge_coverage)

    def forge_source_binding(o, d):
        rel = "replay/full_replay_manifest.json"
        p = d / rel
        m = json.loads(p.read_text())
        m["source_provenance"]["lrsc_interval_certificate.py"]["git_blob_sha"] = "0" * 40
        p.write_text(json.dumps(m, indent=2) + "\n")
        reseal_artifact(o, d, rel)
    case("source_provenance_forged_and_rehashed", forge_source_binding)

    def forge_witness(o, d):
        rel = "replay/witness_k14.json"
        p = d / rel
        w = json.loads(p.read_text())
        w["subset"] = w["subset"][:-1]
        p.write_text(json.dumps(w, indent=2) + "\n")
        reseal_artifact(o, d, rel)
    case("witness_forged_and_rehashed", forge_witness)

    def forge_recheck(o, d):
        rel = "replay/independent_recheck.json"
        p = d / rel
        r = json.loads(p.read_text())
        r["coverage_K0_to_K13"] -= 1
        p.write_text(json.dumps(r, indent=2) + "\n")
        reseal_artifact(o, d, rel)
    case("independent_recheck_forged_and_rehashed", forge_recheck)

    def change_theta(o, d):
        o["domain"]["parameters"]["theta"] = "0.08"
    case("theta_changed", change_theta)

    def substitute_dependency(o, d):
        o["dependencies"][0]["claim_digest"] = "1" * 64
    case("dependency_version_substituted", substitute_dependency)

    def path_traversal(o, d):
        for ev in o["evidence"]:
            if ev.get("path"):
                ev["path"] = "../../outside-evidence.json"
                break
    case("path_traversal_evidence_reference", path_traversal)

    def mutate_coordinate(o, d):
        p = d / "replay/mask_theta_07_coordinate_intervals.txt"
        p.write_text(p.read_text().replace("0", "1", 1))
    case("rigorous_coordinate_mutated", mutate_coordinate)

    def mutate_search_log(o, d):
        p = d / "replay/k13.txt"
        p.write_text(p.read_text() + "# forged tail\n")
    case("search_log_mutated", mutate_search_log)

    def forge_permutation(o, d):
        rel = "replay/full_replay_manifest.json"
        p = d / rel
        m = json.loads(p.read_text())
        perm = m["construction"]["channel_permutation"]
        perm[0], perm[1] = perm[1], perm[0]
        p.write_text(json.dumps(m, indent=2) + "\n")
        reseal_artifact(o, d, rel)
    case("channel_permutation_changed_and_rehashed", forge_permutation)

    def duplicate_channel(o, d):
        rel = "replay/full_replay_manifest.json"
        p = d / rel
        m = json.loads(p.read_text())
        m["construction"]["channel_permutation"][0] = m["construction"]["channel_permutation"][1]
        p.write_text(json.dumps(m, indent=2) + "\n")
        reseal_artifact(o, d, rel)
    case("channel_permutation_duplicate_drop", duplicate_channel)

    return {
        "schema": "intentseal-vrk-redteam-v3",
        "claim_id": original.get("claim_id"),
        "attacker_model": "semantic/evidence mutations may recompute artifact hashes and claim digest",
        "cases": cases,
        "all_rejected": all(c["rejected"] for c in cases),
    }


def run_release_mutation_suite(
    *, root: str | Path, certificate: dict, promotion: dict, old_receipt: dict,
    new_receipt: dict, authority_receipt: dict, capsule: dict,
    trust_root_path: str | Path, external_anchor_path: str | Path, authority_key: bytes,
    now: float,
) -> dict:
    """Adversarial release-layer tests.

    Ordinary hashes may be recomputed. The external Git commit and the HMAC key
    are the two deliberately external roots of trust in this prototype model.
    """
    import copy
    import shutil
    from .promotion import verify_promotion_receipt
    from .authority import verify_authority_receipt
    from .capsule import verify_capsule
    from .release import certificate_digest, verify_deterministic_certificate
    from .trust import verify_trust_root, verify_external_anchor, compute_trust_root_digest

    root = Path(root).resolve()
    trust_root_path = Path(trust_root_path).resolve()
    external_anchor_path = Path(external_anchor_path).resolve()
    base_cd = certificate_digest(certificate)
    cases = []

    def record(name: str, rejected: bool, detail: str):
        cases.append({"name": name, "rejected": bool(rejected), "detail": detail})

    c = copy.deepcopy(certificate)
    c["epistemic_result"] = "EVIDENCE_BOUND"
    new_cd = certificate_digest(c)
    ok, detail = verify_promotion_receipt(promotion, old_receipt, new_receipt, certificate_digest=new_cd)
    record("deterministic_certificate_result_forged_and_rehashed", not ok, detail)

    c = copy.deepcopy(certificate)
    c["parameters"]["theta"] = "0.08"
    ok, detail = verify_deterministic_certificate(c, root=root, trust_root_path=trust_root_path, external_anchor_path=external_anchor_path)
    record("deterministic_certificate_theta_changed", not ok, detail)

    c = copy.deepcopy(certificate)
    c["searches"][-1]["covered"] -= 1
    ok, detail = verify_deterministic_certificate(c, root=root, trust_root_path=trust_root_path, external_anchor_path=external_anchor_path)
    record("deterministic_certificate_coverage_reduced", not ok, detail)

    c = copy.deepcopy(certificate)
    c["searches"][-1]["capped"] = True
    ok, detail = verify_deterministic_certificate(c, root=root, trust_root_path=trust_root_path, external_anchor_path=external_anchor_path)
    record("deterministic_certificate_capped_search", not ok, detail)

    c = copy.deepcopy(certificate)
    c["channel_permutation"][0] = c["channel_permutation"][1]
    ok, detail = verify_deterministic_certificate(c, root=root, trust_root_path=trust_root_path, external_anchor_path=external_anchor_path)
    record("deterministic_certificate_permutation_duplicate", not ok, detail)

    c = copy.deepcopy(certificate)
    c["K14_witness"]["subset"] = c["K14_witness"]["subset"][:-1]
    ok, detail = verify_deterministic_certificate(c, root=root, trust_root_path=trust_root_path, external_anchor_path=external_anchor_path)
    record("deterministic_certificate_witness_changed", not ok, detail)

    c = copy.deepcopy(certificate)
    c["platform"] = "forged-host"
    ok, detail = verify_deterministic_certificate(c, root=root, trust_root_path=trust_root_path, external_anchor_path=external_anchor_path)
    record("telemetry_injected_into_deterministic_certificate", not ok, detail)

    p = copy.deepcopy(promotion)
    p["certificate_digest"] = "0" * 64
    p["promotion_digest"] = digest_object({k: v for k, v in p.items() if k != "promotion_digest"})
    ok, detail = verify_promotion_receipt(p, old_receipt, new_receipt, certificate_digest=base_cd)
    record("promotion_certificate_digest_forged_and_resealed", not ok, detail)

    a = copy.deepcopy(authority_receipt)
    a["publish_status"] = "EVIDENCE_BOUND"
    ok, detail = verify_authority_receipt(
        a, key=authority_key, claim_digest=new_receipt["claim_digest"], publish_status="CERTIFIED",
        certificate_digest=base_cd, proposition_digest=new_receipt["proposition_digest"],
        evidence_root=new_receipt["evidence_root"], now=now,
    )
    record("authority_receipt_replayed_for_stronger_status", not ok, detail)

    cap = copy.deepcopy(capsule)
    cap["certificate_digest"] = "0" * 64
    cap["capsule_digest"] = digest_object({k: v for k, v in cap.items() if k != "capsule_digest"})
    ok, detail = verify_capsule(cap, authority_key=authority_key, now=now)
    record("capsule_certificate_digest_changed_and_resealed", not ok, detail)

    # Attacker changes a verifier source and reseals the local trust root. The
    # fixed external anchor still binds the original root and therefore rejects.
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td) / "pkg"
        shutil.copytree(root, temp)
        trp = temp / trust_root_path.relative_to(root)
        eap = temp / external_anchor_path.relative_to(root)
        trust = json.loads(trp.read_text())
        victim = sorted(trust["sources"])[0]
        vp = temp / victim
        vp.write_text(vp.read_text() + "\n# adversarial replacement\n")
        trust["sources"][victim] = hashlib.sha256(vp.read_bytes()).hexdigest()
        trust["trust_root_digest"] = compute_trust_root_digest(trust)
        trp.write_text(json.dumps(trust, indent=2, sort_keys=True) + "\n")
        ok1, detail1, _ = verify_trust_root(temp, trp)
        ok2, detail2, _ = verify_external_anchor(trp, eap)
        record("verifier_source_replaced_and_local_trust_root_resealed", not (ok1 and ok2), detail1 + "; " + detail2)

    with tempfile.TemporaryDirectory() as td:
        temp = Path(td) / "pkg"
        shutil.copytree(root, temp)
        trp = temp / trust_root_path.relative_to(root)
        trust = json.loads(trp.read_text())
        first = sorted(trust["sources"])[0]
        value = trust["sources"].pop(first)
        trust["sources"]["../escape.py"] = value
        trust["trust_root_digest"] = compute_trust_root_digest(trust)
        trp.write_text(json.dumps(trust, indent=2, sort_keys=True) + "\n")
        ok, detail, _ = verify_trust_root(temp, trp)
        record("trust_root_path_traversal", not ok, detail)

    # A complete internally consistent ledger rewrite is detected by the preserved
    # external head anchor, rather than by the hash chain alone.
    from .ledger import append_event, seal_ledger_head, verify_ledger, verify_ledger_anchor
    with tempfile.TemporaryDirectory() as td:
        lp = Path(td) / "ledger.jsonl"
        key = b"release-redteam-ledger-anchor"
        append_event(lp, {"type": "CLAIM_REGISTERED", "claim_id": "x"})
        anchor = seal_ledger_head(lp, key, anchor_id="release-redteam-anchor")
        lp.unlink()
        append_event(lp, {"type": "CLAIM_REGISTERED", "claim_id": "evil"})
        chain_ok = verify_ledger(lp)[0]
        anchor_ok, detail = verify_ledger_anchor(lp, anchor, key)
        record("ledger_rewritten_from_genesis", chain_ok and not anchor_ok, detail)

    return {
        "schema": "intentseal-vrk-release-redteam-v1",
        "attacker_model": "ordinary hashes may be recomputed; external Git anchor and HMAC key remain outside attacker control",
        "cases": cases,
        "all_rejected": all(c["rejected"] for c in cases),
    }
