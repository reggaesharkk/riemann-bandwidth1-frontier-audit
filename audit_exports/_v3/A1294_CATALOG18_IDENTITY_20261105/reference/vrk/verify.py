from __future__ import annotations

import copy
import json
import platform
from pathlib import Path
from typing import Any

from . import __version__
from .canonical import digest_object, sha256_file
from .evidence import evidence_root
from .domains import DOMAIN_ADAPTERS
from .plugins import PLUGINS
from .types import CLAIM_CLASSES, REQUIRED_ROLES, REPLAY_REQUIRED_ROLES, Check


class VerificationError(ValueError):
    pass


def _require(cond: bool, msg: str) -> None:
    if not cond:
        raise VerificationError(msg)


def kernel_fingerprint() -> str:
    here = Path(__file__).resolve().parent
    files = sorted(p for p in here.glob("*.py") if p.is_file())
    return digest_object([{"name": p.name, "sha256": sha256_file(p)} for p in files])


def validate_claim_shape(claim: dict[str, Any]) -> None:
    for key in ("schema", "claim_id", "claim_text", "claim_class", "domain", "scope", "evidence", "dependencies", "sealed"):
        _require(key in claim, f"missing required field: {key}")
    _require(claim["schema"] == "intentseal-vrk-claim-v2", "schema mismatch")
    _require(isinstance(claim["claim_id"], str) and claim["claim_id"], "claim_id must be nonempty")
    _require(isinstance(claim["claim_text"], str) and claim["claim_text"], "claim_text must be nonempty")
    _require(claim["claim_class"] in CLAIM_CLASSES, f"unknown claim_class: {claim['claim_class']}")
    _require(isinstance(claim["domain"], dict) and claim["domain"], "domain must be nonempty object")
    _require(isinstance(claim["scope"], dict), "scope must be object")
    _require(isinstance(claim["evidence"], list), "evidence must be array")
    _require(isinstance(claim["dependencies"], list), "dependencies must be array")
    _require(isinstance(claim["sealed"], bool), "sealed must be boolean")
    if claim["sealed"]:
        _require(isinstance(claim.get("claim_digest"), str) and len(claim["claim_digest"]) == 64,
                 "sealed claim requires claim_digest")


def _receipt(claim: dict[str, Any], checks: list[Check], computed_digest: str, proposition_digest: str,
             ev_root: str, dep_root: str, kernel_status: str) -> dict[str, Any]:
    return {
        "schema": "intentseal-vrk-verification-v2",
        "claim_id": claim["claim_id"],
        "claim_class": claim["claim_class"],
        "kernel_status": kernel_status,
        "claim_digest": computed_digest,
        "proposition_digest": proposition_digest,
        "evidence_root": ev_root,
        "dependency_root": dep_root,
        "kernel": {
            "version": __version__,
            "source_fingerprint": kernel_fingerprint(),
            "python": platform.python_version(),
        },
        "checks": [c.__dict__ for c in checks],
        "pass": kernel_status != "UNVERIFIED",
        "verification_ok": kernel_status != "UNVERIFIED",
        "certified": kernel_status == "CERTIFIED",
    }


def verify_claim(claim_path: str | Path) -> dict[str, Any]:
    """Fail-closed claim verifier with cheap preflight before expensive replay.

    Semantic/scope/dependency/path/hash failures are rejected before executable
    replay.  A hash mismatch also suppresses the corresponding plugin execution.
    This is both safer and makes adversarial suites practical without weakening
    the proof path for well-formed claims.
    """
    claim_path = Path(claim_path).resolve()
    root = claim_path.parent
    claim = json.loads(claim_path.read_text(encoding="utf-8"))
    validate_claim_shape(claim)

    checks: list[Check] = []
    required = REQUIRED_ROLES[claim["claim_class"]]
    roles_present: set[str] = set()
    required_external = False
    required_local_without_replay = False
    evidence_records: list[tuple[int, dict[str, Any], Path | None, bool]] = []

    # Stable identities are computed regardless of pass/fail so a failure receipt
    # can still say exactly what object was examined.
    claim_for_digest = copy.deepcopy(claim)
    claimed_digest = claim_for_digest.pop("claim_digest", None)
    computed_digest = digest_object(claim_for_digest)
    proposition = {
        "claim_id": claim["claim_id"],
        "claim_text": claim["claim_text"],
        "domain": claim["domain"],
        "scope": claim["scope"],
    }
    proposition_digest = digest_object(proposition)
    ev_root = evidence_root(claim["evidence"])
    dep_records = [{"claim_id": d.get("claim_id"), "claim_digest": d.get("claim_digest"), "relation": d.get("relation")} for d in claim["dependencies"]]
    dep_root = digest_object(sorted(dep_records, key=lambda x: (str(x["claim_id"]), str(x["relation"]))))

    # Preflight: roles, safe paths/external bindings, replay policy.
    preflight_ok = True
    for i, ev in enumerate(claim["evidence"]):
        role = ev.get("role")
        if not role:
            checks.append(Check(f"evidence[{i}].role", False, "missing role"))
            preflight_ok = False
            evidence_records.append((i, ev, None, False))
            continue
        roles_present.add(role)
        rel = ev.get("path")
        if rel:
            p = (root / rel).resolve()
            safe = True
            try:
                p.relative_to(root)
            except ValueError:
                safe = False
            if not safe:
                checks.append(Check(f"{role}.path", False, "path escapes claim directory"))
                preflight_ok = False
                evidence_records.append((i, ev, None, False))
                continue
            if not p.exists() or not p.is_file():
                checks.append(Check(f"{role}.artifact", False, f"missing file {rel}"))
                preflight_ok = False
                evidence_records.append((i, ev, p, False))
                continue
            plugin_name = ev.get("plugin")
            if role in required and role in REPLAY_REQUIRED_ROLES and not plugin_name:
                checks.append(Check(f"{role}.replay_policy", False, "required replay role lacks verifier plugin"))
                required_local_without_replay = True
                preflight_ok = False
            evidence_records.append((i, ev, p, True))
        else:
            ext = ev.get("external")
            ok = isinstance(ext, dict) and all(ext.get(k) for k in ("repository", "commit", "path", "git_blob_sha"))
            if ok:
                commit = str(ext["commit"]); blob = str(ext["git_blob_sha"])
                ok = len(commit) in (40, 64) and all(c in "0123456789abcdef" for c in commit.lower()) and len(blob) in (40, 64) and all(c in "0123456789abcdef" for c in blob.lower())
            checks.append(Check(f"{role}.external_binding", bool(ok), "immutable repository binding" if ok else "incomplete/invalid external binding"))
            preflight_ok &= bool(ok)
            if role in required:
                required_external = True
            evidence_records.append((i, ev, None, bool(ok)))

    missing_roles = sorted(required - roles_present)
    checks.append(Check("required_evidence_roles", not missing_roles, "complete" if not missing_roles else f"missing {missing_roles}"))
    preflight_ok &= not missing_roles

    if claim["claim_class"] != "CONJECTURE":
        applies = claim["scope"].get("applies_to")
        excludes = claim["scope"].get("does_not_imply")
        scope_ok = isinstance(applies, list) and bool(applies) and isinstance(excludes, list) and bool(excludes)
        checks.append(Check("scope_boundary", scope_ok, "explicit applies_to + does_not_imply" if scope_ok else "scope boundary incomplete"))
    else:
        scope_ok = True
    preflight_ok &= scope_ok

    dep_ok = True
    for d in claim["dependencies"]:
        good = isinstance(d, dict) and d.get("claim_id") and d.get("relation") and isinstance(d.get("claim_digest"), str) and len(d["claim_digest"]) == 64
        dep_ok &= bool(good)
    checks.append(Check("dependencies", dep_ok, f"{len(claim['dependencies'])} digest-bound dependency records" if dep_ok else "dependency missing id/relation/digest"))
    preflight_ok &= dep_ok

    digest_ok = (not claim["sealed"] and claimed_digest is None) or claimed_digest == computed_digest
    checks.append(Check("claim_digest", digest_ok, f"computed={computed_digest}"))
    preflight_ok &= digest_ok

    # Only allow a domain adapter to read local evidence after path safety passed.
    adapter = DOMAIN_ADAPTERS.get(claim["domain"].get("system"))
    if adapter and preflight_ok:
        try:
            domain_ok, domain_detail = adapter(claim, root)
        except Exception as e:
            domain_ok, domain_detail = False, f"domain adapter exception: {type(e).__name__}: {e}"
    elif not adapter:
        domain_ok, domain_detail = False, "no domain adapter registered"
    else:
        domain_ok, domain_detail = False, "domain semantics skipped because structural preflight failed"
    checks.append(Check("domain_semantics", domain_ok, domain_detail))
    preflight_ok &= domain_ok

    if not preflight_ok:
        return _receipt(claim, checks, computed_digest, proposition_digest, ev_root, dep_root, "UNVERIFIED")

    # Artifact hashes. Do not execute a plugin against bytes that fail their binding.
    all_artifacts_bound = True
    all_plugins_pass = True
    for i, ev, p, usable in evidence_records:
        role = ev.get("role")
        if p is None:
            continue
        expected_sha = ev.get("sha256")
        actual = sha256_file(p)
        ok = isinstance(expected_sha, str) and actual == expected_sha
        checks.append(Check(f"{role}.sha256", ok, f"actual={actual}"))
        all_artifacts_bound &= ok
        if not ok:
            all_plugins_pass = False
            continue
        plugin_name = ev.get("plugin")
        if plugin_name:
            plugin = PLUGINS.get(plugin_name)
            if not plugin:
                checks.append(Check(f"{role}.plugin", False, f"unknown plugin {plugin_name}"))
                all_plugins_pass = False
            else:
                ok2, detail = plugin(p, ev.get("plugin_args", {}))
                checks.append(Check(f"{role}.plugin:{plugin_name}", ok2, detail))
                all_plugins_pass &= ok2

    if not all_artifacts_bound or not all_plugins_pass:
        kernel_status = "UNVERIFIED"
    elif required_external or required_local_without_replay:
        kernel_status = "EVIDENCE_BOUND"
    elif claim["sealed"]:
        kernel_status = "CERTIFIED"
    else:
        kernel_status = "LOCALLY_REPLAYED"

    return _receipt(claim, checks, computed_digest, proposition_digest, ev_root, dep_root, kernel_status)
