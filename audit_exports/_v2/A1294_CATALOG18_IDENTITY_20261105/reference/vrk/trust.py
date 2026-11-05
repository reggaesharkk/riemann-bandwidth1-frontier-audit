from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .canonical import canonical_json_bytes, digest_object, sha256_file

TRUST_ROOT_SCHEMA = "intentseal-vrk-verifier-trust-root-v1"
EXTERNAL_ANCHOR_SCHEMA = "intentseal-vrk-external-source-anchor-v1"


def _hex(value: object, length: int) -> bool:
    return isinstance(value, str) and len(value) == length and all(c in "0123456789abcdef" for c in value.lower())


def trust_root_payload(obj: dict[str, Any]) -> dict[str, Any]:
    out = dict(obj)
    out.pop("trust_root_digest", None)
    return out


def compute_trust_root_digest(obj: dict[str, Any]) -> str:
    return digest_object(trust_root_payload(obj))


def verify_trust_root(root: str | Path, trust_root_path: str | Path) -> tuple[bool, str, dict[str, Any]]:
    root = Path(root).resolve()
    path = Path(trust_root_path).resolve()
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        if obj.get("schema") != TRUST_ROOT_SCHEMA:
            return False, "trust-root schema mismatch", obj
        if obj.get("version") != "0.3.1":
            return False, "trust-root version mismatch", obj
        sources = obj.get("sources")
        if not isinstance(sources, dict) or not sources:
            return False, "trust-root sources missing", obj
        claimed = obj.get("trust_root_digest")
        computed = compute_trust_root_digest(obj)
        if claimed != computed:
            return False, f"trust-root digest mismatch: computed={computed}", obj
        for rel, expected in sources.items():
            rp = Path(rel)
            if rp.is_absolute() or ".." in rp.parts:
                return False, f"unsafe trust-root path: {rel}", obj
            if not _hex(expected, 64):
                return False, f"invalid SHA-256 in trust root: {rel}", obj
            p = (root / rp).resolve()
            try:
                p.relative_to(root)
            except ValueError:
                return False, f"trust-root path escapes root: {rel}", obj
            if not p.is_file():
                return False, f"trusted source missing: {rel}", obj
            actual = sha256_file(p)
            if actual != expected:
                return False, f"trusted source hash mismatch: {rel}: {actual}", obj
        return True, f"{len(sources)} verifier-source hashes match trust root {claimed}", obj
    except Exception as e:
        return False, f"malformed trust root: {type(e).__name__}: {e}", {}


def verify_external_anchor(
    trust_root_path: str | Path,
    external_anchor_path: str | Path,
) -> tuple[bool, str, dict[str, Any]]:
    """Verify the local descriptor for the immutable external trust anchor.

    This deliberately does not perform network access.  A package-only attacker can
    rewrite both package and descriptor, so an independent release audit must compare
    repository/commit/path/blob against the public repository.  The descriptor makes
    that external dependency explicit instead of pretending the package is its own
    root of trust.
    """
    tp = Path(trust_root_path)
    ap = Path(external_anchor_path)
    try:
        obj = json.loads(ap.read_text(encoding="utf-8"))
        if obj.get("schema") != EXTERNAL_ANCHOR_SCHEMA:
            return False, "external-anchor schema mismatch", obj
        if obj.get("repository") != "reggaesharkk/intentseal":
            return False, "external-anchor repository mismatch", obj
        if not _hex(obj.get("commit"), 40):
            return False, "external-anchor commit is not a 40-hex Git commit", obj
        if obj.get("path") != "anchors/VRK_v0_3_1_VERIFIER_TRUST_ROOT.json":
            return False, "external-anchor path mismatch", obj
        if not _hex(obj.get("git_blob_sha"), 40):
            return False, "external-anchor blob id is invalid", obj
        actual_sha = hashlib.sha256(tp.read_bytes()).hexdigest()
        if obj.get("trust_root_sha256") != actual_sha:
            return False, f"external anchor does not bind local trust root: {actual_sha}", obj
        if obj.get("trust_root_digest") != json.loads(tp.read_text(encoding="utf-8")).get("trust_root_digest"):
            return False, "external anchor trust-root digest mismatch", obj
        return True, "external anchor descriptor binds this trust root; public Git commit remains the independent root of trust", obj
    except Exception as e:
        return False, f"malformed external anchor: {type(e).__name__}: {e}", {}
