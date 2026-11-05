from __future__ import annotations

from typing import Any
from .canonical import digest_object


def evidence_binding_descriptor(ev: dict[str, Any]) -> dict[str, Any]:
    """Return the immutable part of an evidence record used in receipt roots."""
    out = {"role": ev.get("role")}
    if ev.get("path"):
        out.update({
            "mode": "local",
            "path": ev.get("path"),
            "sha256": ev.get("sha256"),
            "plugin": ev.get("plugin"),
            "plugin_args": ev.get("plugin_args", {}),
        })
    else:
        out.update({"mode": "external", "external": ev.get("external")})
    return out


def evidence_root(evidence: list[dict[str, Any]]) -> str:
    # Order-independent over the evidence collection while preserving exact records.
    leaves = sorted(digest_object(evidence_binding_descriptor(ev)) for ev in evidence)
    return digest_object({"algorithm": "sha256-canonical-json-v1", "leaves": leaves})
