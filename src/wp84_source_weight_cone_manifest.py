#!/usr/bin/env python3
"""Create a SHA-256 manifest for the additive WP84 source-weight audit."""

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "861bdad5f6f6495c5b755546b4b2fa43367e2901"
PACKAGE = Path(r"C:\Users\Asus\SHARK_AGENT_LAB\wp84_source_weight_mask_hostile_20261102")

SOURCE_PATHS = [
    "notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md",
    "src/wp84_r400_filtered_connected_kernel.py",
    "notes/WP84_R400_FILTERED_SHARP_REPAIR.md",
    "src/wp84_r400_filtered_sharp_repair.py",
    "notes/WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md",
    "notes/WP84_ADAPTIVE_BOUNDARY_LOCAL_LARGE_SIEVE.md",
    "src/wp84_adaptive_boundary_large_sieve.py",
    "notes/WP84_FOURIER_REPROJECTION_BRIDGE_AUDIT.md",
    "notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md",
    "notes/WP84_SOURCE_MATCHED_26_TERM_SIGN_AUDIT.md",
    "evidence/WP84_SOURCE_MATCHED_26_TERM_SIGN_AUDIT.json",
    "src/wp84_source_matched_26_term_sign_replay.py",
    "tests/test_wp84_source_matched_26_term_sign.py",
    "src/wp84_fifth_full_pool_amplitude.py",
]

PACKAGE_PATHS = [
    "CODEX_TASK.md", "README.md", "SHA256_MANIFEST.json", "SHA256_MANIFEST.sha256",
    "verify.py", "notes/DECISION.md", "src/audit.py", "tests/test_audit.py",
    "evidence/tests_normal.log", "evidence/tests_O.log", "evidence/tests_OO.log",
]

AUDIT_PATHS = [
    "notes/WP84_SOURCE_WEIGHT_CONE_FOURTH_ORDER_OPERATOR_AUDIT.md",
    "src/wp84_source_weight_cone_audit.py",
    "src/wp84_source_weight_cone_run_modes.py",
    "src/wp84_source_weight_cone_orientation_replay.py",
    "src/wp84_source_weight_cone_certificate_replay.py",
    "src/wp84_source_weight_cone_manifest.py",
    "tests/test_wp84_source_weight_cone_audit.py",
    "evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_ORIENTATION_INTERVALS.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_BASE_REPLAY.log",
    "evidence/WP84_SOURCE_WEIGHT_CONE_KERNEL_CERTIFICATE.log",
    "evidence/WP84_SOURCE_WEIGHT_CONE_ORIENTATION_REPLAY.log",
    "evidence/WP84_SOURCE_WEIGHT_CONE_TESTS_NORMAL.log",
    "evidence/WP84_SOURCE_WEIGHT_CONE_TESTS_O.log",
    "evidence/WP84_SOURCE_WEIGHT_CONE_TESTS_OO.log",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def is_ancestor(base: str) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", base, "HEAD"],
                          cwd=ROOT, check=False).returncode == 0


def source_entry(relative: str) -> dict:
    blob = git("rev-parse", f"{BASE}:{relative}")
    content = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
    checkout = (ROOT / relative).read_bytes()
    return {
        "git_blob_sha1": blob,
        "git_blob_sha256": sha(content),
        "worktree_sha256": sha(checkout),
        "bytes_in_git_blob": len(content),
        "bytes_in_worktree": len(checkout),
    }


def main():
    package_manifest = json.loads((PACKAGE / "SHA256_MANIFEST.json").read_text(encoding="utf-8"))
    package_manifest_bytes = (PACKAGE / "SHA256_MANIFEST.json").read_bytes()
    package_expected = (PACKAGE / "SHA256_MANIFEST.sha256").read_text(encoding="utf-8").split()[0]
    if sha(package_manifest_bytes) != package_expected:
        raise RuntimeError("extracted package manifest sidecar mismatch")

    package_files = {}
    for relative in PACKAGE_PATHS:
        data = (PACKAGE / Path(relative)).read_bytes()
        package_files[relative] = {
            "sha256": sha(data),
            "bytes": len(data),
            "matches_package_manifest": (
                sha(data) == package_manifest["files"].get(relative, package_expected)
                if relative not in ("SHA256_MANIFEST.json", "SHA256_MANIFEST.sha256")
                else None
            ),
        }

    audit_files = {}
    for relative in AUDIT_PATHS:
        data = (ROOT / Path(relative)).read_bytes()
        audit_files[relative] = {"sha256": sha(data), "bytes": len(data)}

    previous_evidence_blob = subprocess.check_output(
        ["git", "show", f"{BASE}:evidence/WP84_SOURCE_MATCHED_26_TERM_SIGN_AUDIT.json"],
        cwd=ROOT,
    )
    replay_log = (ROOT / "evidence/WP84_SOURCE_WEIGHT_CONE_BASE_REPLAY.log").read_text(encoding="utf-8")

    manifest = {
        "schema": "wp84.source-weight-cone.sha256-manifest.v1",
        "audit_branch": "codex/wp84-source-weight-cone-operator-audit-20261103",
        "base_commit": BASE,
        "base_commit_verified": is_ancestor(BASE),
        "decision": "LEGAL_SOURCE_COUNTEREXAMPLE",
        "decision_scope": "pointwise source-admissible balanced fourth-order kernel atom; complete aggregate open",
        "prior_audit_replay": {
            "git_blob_sha256": sha(previous_evidence_blob),
            "git_blob_byte_match": "git_blob_replay_byte_match=True" in replay_log,
            "checked_out_worktree_sha256": sha((ROOT / "evidence/WP84_SOURCE_MATCHED_26_TERM_SIGN_AUDIT.json").read_bytes()),
            "worktree_line_ending_normalization": "worktree_crlf_normalization_only=True" in replay_log,
        },
        "repository_source_files": {relative: source_entry(relative) for relative in SOURCE_PATHS},
        "extracted_task_package": {
            "root": str(PACKAGE),
            "manifest_sha256": sha(package_manifest_bytes),
            "manifest_entries_verified": len(package_manifest.get("files", {})),
            "files": package_files,
        },
        "audit_artifacts": audit_files,
        "manifest_files_excluded_from_self_hash": [
            "evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.json",
            "evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.sha256",
        ],
    }
    path = ROOT / "evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.json"
    payload = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    path.write_text(payload, encoding="utf-8", newline="\n")
    digest = sha(payload.encode("utf-8"))
    sidecar = ROOT / "evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.sha256"
    sidecar.write_text(f"{digest}  {path.name}\n", encoding="ascii", newline="\n")
    print(f"WROTE {path.relative_to(ROOT)}")
    print(f"SHA256 {digest}")
    print(f"SOURCE_FILES {len(SOURCE_PATHS)}; PACKAGE_FILES {len(PACKAGE_PATHS)}; AUDIT_FILES {len(AUDIT_PATHS)}")
    print(f"BASE_REPLAY_MATCH {manifest['prior_audit_replay']['git_blob_byte_match']}")
    if not manifest["base_commit_verified"]:
        raise RuntimeError("base commit must be an ancestor of the audit revision")
    if not manifest["prior_audit_replay"]["git_blob_byte_match"]:
        raise RuntimeError("prior audit did not replay byte-for-byte against its Git blob")
    if not manifest["prior_audit_replay"]["worktree_line_ending_normalization"]:
        raise RuntimeError("unexpected prior evidence worktree difference")
    if any(not row["matches_package_manifest"] for row in package_files.values()
           if row["matches_package_manifest"] is not None):
        raise RuntimeError("extracted package entry differs from its manifest")


if __name__ == "__main__":
    main()
