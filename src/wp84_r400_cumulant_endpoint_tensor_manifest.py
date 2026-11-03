#!/usr/bin/env python3
"""Build/verify source and SHA-256 evidence for the cumulant tensor audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "0d3bc919451df298ef2a945569d8c3b1eb65192f"
BRANCH = "codex/wp84-physical-cumulant-tensor-lift-20261103"
SOURCE_INPUTS = [
    "notes/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_AND_NEAR_PRODUCT_CLOSURE.md",
    "notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md",
    "notes/WP84_R400_ENDPOINT_QUANTIFIERS_AND_NEAR_PRODUCT_AUDIT.md",
    "notes/WP84_DECISION_D_ENDPOINT_ADMISSIBILITY_DENSITY.md",
    "notes/WP84_F1C_FIRST_STRIKE_ENDPOINT_SOURCE_AUDIT.md",
    "notes/WP84_E2_PRINCIPAL_ARC_NORMALIZATION_AUDIT.md",
    "notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md",
    "notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md",
    "notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md",
    "src/wp84_r400_physical_endpoint_averaging.py",
    "src/wp84_r400_physical_endpoint_averaging_manifest.py",
    "src/wp84_r400_source_interval_replay.py",
    "src/wp84_r400_endpoint_near_product_audit.py",
    "src/wp84_decision_d_endpoint_admissibility.py",
    "src/wp84_decision_d_endpoint_admissibility_replay.py",
    "src/wp84_r400_filtered_connected_kernel.py",
    "src/wp84_r400_filtered_sharp_repair.py",
    "tests/test_wp84_r400_physical_endpoint_averaging.py",
    "tests/test_wp84_r400_endpoint_near_product_audit.py",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_LEDGER.json",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SOURCE_HASHES.json",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SHA256_MANIFEST.json",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SHA256_MANIFEST.sha256",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json",
    "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json",
    "evidence/WP84_R400_SOURCE_INTERVAL_REPLAY.json",
    "evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json",
]
ARTIFACTS = [
    "notes/WP84_R400_PHYSICAL_CUMULANT_ENDPOINT_DIFFERENCE_AND_TENSOR_LIFT.md",
    "src/wp84_r400_cumulant_endpoint_tensor.py",
    "src/wp84_r400_cumulant_endpoint_tensor_manifest.py",
    "tests/test_wp84_r400_cumulant_endpoint_tensor.py",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_INITIAL_TEST_FAILURE.log",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_TEST_NORMAL.log",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_TEST_O.log",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_TEST_OO.log",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_CHECKER_REPLAY.log",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_PARENT_MANIFEST_REPLAY.log",
]
SOURCE_HASH_PATH = "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SOURCE_HASHES.json"
MANIFEST_PATH = "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SHA256_MANIFEST.json"
SIDECAR_PATH = "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SHA256_MANIFEST.sha256"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).stdout


def source_inventory() -> dict:
    resolved = git_bytes("rev-parse", "--verify", f"{BASE}^{{commit}}").decode().strip()
    if resolved != BASE:
        raise RuntimeError("requested base commit does not resolve exactly")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT, check=False
    )
    if ancestor.returncode != 0:
        raise RuntimeError("base commit is not an ancestor of this audit revision")
    files = {}
    for path in SOURCE_INPUTS:
        base_data = git_bytes("show", f"{BASE}:{path}")
        worktree_data = (ROOT / path).read_bytes()
        base_norm = base_data.replace(b"\r\n", b"\n")
        work_norm = worktree_data.replace(b"\r\n", b"\n")
        if base_norm != work_norm:
            raise RuntimeError(f"historical input changed from base: {path}")
        files[path] = {
            "base_git_blob": git_bytes("rev-parse", f"{BASE}:{path}").decode().strip(),
            "base_sha256": sha256(base_data),
            "base_bytes": len(base_data),
            "worktree_sha256": sha256(worktree_data),
            "worktree_normalized_sha256": sha256(work_norm),
            "worktree_bytes": len(worktree_data),
            "line_ending_normalized_identical_to_base": True,
        }
    return {
        "schema": "wp84.r400.cumulant-endpoint-tensor.source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "method": "SHA-256 over raw git-show base bytes and worktree bytes; CRLF/LF normalized only for unchanged-input comparison",
        "files": files,
    }


def artifact_manifest(source_digest: str) -> dict:
    artifacts = {}
    for path in ARTIFACTS + [SOURCE_HASH_PATH]:
        data = (ROOT / path).read_bytes()
        artifacts[path] = {"bytes": len(data), "sha256": sha256(data)}
    return {
        "schema": "wp84.r400.cumulant-endpoint-tensor.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "decisions": {
            "CUMULANT_ENDPOINT_IDENTITY": "PROVED",
            "TENSOR_AVERAGING": "EXACT",
            "SOURCE_WEIGHTED_CORRECTION": "OPEN",
            "ORDINARY_CONNECTED_RECORD_BOUND": "OPEN",
            "R400_CONSUMER": "CONDITIONAL",
            "68_820273_PERCENT": "OPEN",
            "STRICT_GT_79_PERCENT": "OPEN",
            "RIEMANN_HYPOTHESIS": "OPEN",
        },
        "source_hash_inventory": {"path": SOURCE_HASH_PATH, "sha256": source_digest},
        "artifacts": artifacts,
        "self_hash_excluded": [MANIFEST_PATH, SIDECAR_PATH],
        "claim_boundary": "Exact cumulant variation and tensor identities are established; no source-weighted ordinary-prime record estimate is established.",
    }


def write_all() -> None:
    source_data = source_inventory()
    source_bytes = (json.dumps(source_data, indent=2, sort_keys=True) + "\n").encode()
    (ROOT / SOURCE_HASH_PATH).write_bytes(source_bytes)
    manifest = artifact_manifest(sha256(source_bytes))
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    (ROOT / MANIFEST_PATH).write_bytes(manifest_bytes)
    (ROOT / SIDECAR_PATH).write_text(sha256(manifest_bytes) + "  " + MANIFEST_PATH + "\n", encoding="ascii")
    print(f"WROTE {SOURCE_HASH_PATH}: {len(source_data['files'])} unchanged base inputs")
    print(f"WROTE {MANIFEST_PATH}: {len(manifest['artifacts'])} hashed artifacts")
    print(f"MANIFEST_SHA256 {sha256(manifest_bytes)}")


def verify() -> None:
    manifest_bytes = (ROOT / MANIFEST_PATH).read_bytes()
    manifest = json.loads(manifest_bytes)
    expected = sha256(manifest_bytes) + "  " + MANIFEST_PATH
    if (ROOT / SIDECAR_PATH).read_text(encoding="ascii").strip() != expected:
        raise RuntimeError("manifest sidecar mismatch")
    for path, record in manifest["artifacts"].items():
        data = (ROOT / path).read_bytes()
        if len(data) != record["bytes"] or sha256(data) != record["sha256"]:
            raise RuntimeError(f"artifact hash mismatch: {path}")
    source_data = (ROOT / SOURCE_HASH_PATH).read_bytes()
    if sha256(source_data) != manifest["source_hash_inventory"]["sha256"]:
        raise RuntimeError("source inventory digest mismatch")
    inventory = json.loads(source_data)
    for path, record in inventory["files"].items():
        data = (ROOT / path).read_bytes()
        if not record["line_ending_normalized_identical_to_base"]:
            raise RuntimeError(f"historical input changed from base: {path}")
        if sha256(data) != record["worktree_sha256"]:
            raise RuntimeError(f"source hash changed: {path}")
    print(f"PASS manifest, sidecar, {len(manifest['artifacts'])} artifacts, {len(inventory['files'])} unchanged base inputs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify() if args.verify else write_all()
