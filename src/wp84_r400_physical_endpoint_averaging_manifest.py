#!/usr/bin/env python3
"""Create and verify the additive WP84 endpoint-averaging SHA-256 inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "1139e81c5fdfc0ecfc054b892697c6f76f78db31"
BRANCH = "codex/wp84-physical-endpoint-averaging-20261103"
SOURCE_INPUTS = [
    "notes/WP84_R400_ENDPOINT_QUANTIFIERS_AND_NEAR_PRODUCT_AUDIT.md",
    "notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md",
    "notes/WP84_DECISION_D_ENDPOINT_ADMISSIBILITY_DENSITY.md",
    "notes/WP84_F1C_FIRST_STRIKE_ENDPOINT_SOURCE_AUDIT.md",
    "notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md",
    "notes/WP84_E2_PRINCIPAL_ARC_NORMALIZATION_AUDIT.md",
    "notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md",
    "notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md",
    "notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md",
    "src/wp84_r400_endpoint_near_product_audit.py",
    "src/wp84_r400_endpoint_near_product_manifest.py",
    "src/wp84_r400_schatten_absorption_audit.py",
    "src/wp84_r400_source_interval_replay.py",
    "src/wp84_decision_d_endpoint_admissibility.py",
    "src/wp84_decision_d_endpoint_admissibility_replay.py",
    "src/wp84_e2_shift_range_safe_lobe.py",
    "src/wp84_r400_filtered_connected_kernel.py",
    "src/wp84_r400_filtered_sharp_repair.py",
    "src/wp84_r400_pair_layer_exact.py",
    "tests/test_wp84_r400_endpoint_near_product_audit.py",
    "tests/test_wp84_r400_schatten_absorption_audit.py",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SOURCE_HASHES.json",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SHA256_MANIFEST.json",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SHA256_MANIFEST.sha256",
    "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json",
    "evidence/WP84_R400_SOURCE_INTERVAL_REPLAY.json",
    "evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json",
    "evidence/WP84_R400_PARENT_PHYSICAL_ATOM_REPLAY.json",
]
ARTIFACTS = [
    "notes/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_AND_NEAR_PRODUCT_CLOSURE.md",
    "src/wp84_r400_physical_endpoint_averaging.py",
    "src/wp84_r400_physical_endpoint_averaging_manifest.py",
    "tests/test_wp84_r400_physical_endpoint_averaging.py",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_LEDGER.json",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_INITIAL_SERIALIZATION_FAILURE.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_TEST_NORMAL.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_TEST_O.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_TEST_OO.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_PARENT_TEST_NORMAL.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_PARENT_TEST_O.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_PARENT_TEST_OO.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_PARENT_MANIFEST_REPLAY.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_DENSITY_REPLAY.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_DENSITY_BUILD.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_E2_SAFE_LOBE_REPLAY.log",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SOURCE_INTERVAL_REPLAY.log",
]
SOURCE_HASH_PATH = "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SOURCE_HASHES.json"
MANIFEST_PATH = "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SHA256_MANIFEST.json"
SIDECAR_PATH = "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SHA256_MANIFEST.sha256"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).stdout


def source_inventory() -> dict:
    if git_bytes("rev-parse", "--verify", f"{BASE}^{{commit}}").decode().strip() != BASE:
        raise RuntimeError("requested base commit does not resolve exactly")
    files = {}
    for path in SOURCE_INPUTS:
        base_data = git_bytes("show", f"{BASE}:{path}")
        worktree_data = (ROOT / path).read_bytes()
        base_normalized = base_data.replace(b"\r\n", b"\n")
        worktree_normalized = worktree_data.replace(b"\r\n", b"\n")
        identical = worktree_normalized == base_normalized
        if not identical:
            raise RuntimeError(f"historical source/input changed from base: {path}")
        files[path] = {
            "base_git_blob": git_bytes("rev-parse", f"{BASE}:{path}").decode().strip(),
            "base_sha256": sha256(base_data),
            "base_bytes": len(base_data),
            "worktree_sha256": sha256(worktree_data),
            "worktree_normalized_sha256": sha256(worktree_normalized),
            "worktree_bytes": len(worktree_data),
            "line_ending_normalized_identical_to_base": True,
        }
    return {
        "schema": "wp84.r400.physical-endpoint-averaging.source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "method": "SHA-256 over raw git-show base bytes and worktree bytes; only CRLF/LF is normalized for unchanged-input comparison",
        "files": files,
    }


def artifact_manifest(source_hash_digest: str) -> dict:
    artifacts = {}
    for path in ARTIFACTS + [SOURCE_HASH_PATH]:
        data = (ROOT / path).read_bytes()
        artifacts[path] = {"bytes": len(data), "sha256": sha256(data)}
    return {
        "schema": "wp84.r400.physical-endpoint-averaging.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "decisions": {
            "AVERAGED_FOURIER_KERNEL": "EXACT",
            "PHYSICAL_CUMULANT_AVERAGING": "CORRECTION_REQUIRED",
            "JOINT_ENDPOINT_SELECTION": "CONDITIONAL",
            "ORDINARY_CONNECTED_AGGREGATE": "OPEN",
            "R400_CONSUMER": "CONDITIONAL",
            "STRICT_GT_79_PERCENT": "OPEN",
            "RIEMANN_HYPOTHESIS": "OPEN",
        },
        "source_hash_inventory": {"path": SOURCE_HASH_PATH, "sha256": source_hash_digest},
        "artifacts": artifacts,
        "self_hash_excluded": [MANIFEST_PATH, SIDECAR_PATH],
        "claim_boundary": "Exact finite identities and inherited replays are checked; the source-weighted ordinary-prime record-budget estimate remains open.",
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
    expected_sidecar = sha256(manifest_bytes) + "  " + MANIFEST_PATH
    actual_sidecar = (ROOT / SIDECAR_PATH).read_text(encoding="ascii").strip()
    if actual_sidecar != expected_sidecar:
        raise RuntimeError("manifest sidecar mismatch")
    for path, record in manifest["artifacts"].items():
        data = (ROOT / path).read_bytes()
        if len(data) != record["bytes"] or sha256(data) != record["sha256"]:
            raise RuntimeError(f"artifact hash mismatch: {path}")
    source_bytes = (ROOT / SOURCE_HASH_PATH).read_bytes()
    if sha256(source_bytes) != manifest["source_hash_inventory"]["sha256"]:
        raise RuntimeError("source inventory digest mismatch")
    inventory = json.loads(source_bytes)
    for path, record in inventory["files"].items():
        current = (ROOT / path).read_bytes()
        if not record["line_ending_normalized_identical_to_base"]:
            raise RuntimeError(f"source input differs from base: {path}")
        if sha256(current) != record["worktree_sha256"]:
            raise RuntimeError(f"source input hash changed: {path}")
    print(f"PASS manifest, sidecar, {len(manifest['artifacts'])} artifacts, {len(inventory['files'])} unchanged base inputs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify() if args.verify else write_all()
