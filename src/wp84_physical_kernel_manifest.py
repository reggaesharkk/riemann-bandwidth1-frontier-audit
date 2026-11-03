#!/usr/bin/env python3
"""Build and verify machine-readable WP84 physical-kernel audit hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "0185e68f53b50e2085eb30aaecc623861ccc107b"
SOURCE_PATHS = (
    "notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md",
    "src/wp84_r400_filtered_connected_kernel.py",
    "notes/WP84_R400_FILTERED_SHARP_REPAIR.md",
    "src/wp84_r400_filtered_sharp_repair.py",
    "notes/WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md",
    "notes/WP84_ADAPTIVE_BOUNDARY_LOCAL_LARGE_SIEVE.md",
    "src/wp84_adaptive_boundary_large_sieve.py",
    "notes/WP84_SOURCE_WEIGHT_CONE_FOURTH_ORDER_OPERATOR_AUDIT.md",
    "src/wp84_source_weight_cone_audit.py",
    "src/wp84_source_weight_cone_certificate_replay.py",
    "src/wp84_source_weight_cone_orientation_replay.py",
    "evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_ORIENTATION_INTERVALS.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.sha256",
)
NEW_SOURCE_PATHS = (
    "notes/WP84_PHYSICAL_KERNEL_PROPER_POWER_AGGREGATE_AUDIT.md",
    "src/wp84_physical_kernel_proper_power_reconciliation.py",
    "src/wp84_physical_kernel_manifest.py",
    "tests/test_wp84_physical_kernel_reconciliation.py",
)
ARTIFACT_PATHS = (
    *NEW_SOURCE_PATHS,
    "evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json",
    "evidence/WP84_PHYSICAL_KERNEL_TESTS_NORMAL.log",
    "evidence/WP84_PHYSICAL_KERNEL_TESTS_O.log",
    "evidence/WP84_PHYSICAL_KERNEL_TESTS_OO.log",
    "evidence/WP84_PHYSICAL_KERNEL_CHECKER_NORMAL.log",
    "evidence/WP84_PHYSICAL_KERNEL_CHECKER_O.log",
    "evidence/WP84_PHYSICAL_KERNEL_CHECKER_OO.log",
    "evidence/WP84_PUBLIC_KERNEL_CROSSCHECK.log",
    "evidence/WP84_SOURCE_WEIGHT_CERTIFICATE_REPLAY_20261103.log",
    "evidence/WP84_SOURCE_WEIGHT_ORIENTATION_REPLAY_20261103.log",
    "evidence/WP84_PHYSICAL_KERNEL_SOURCE_HASHES.json",
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def original_source_hashes() -> dict:
    rows = {}
    for relative in SOURCE_PATHS:
        blob = git("rev-parse", f"{BASE}:{relative}")
        source = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        worktree = (ROOT / relative).read_bytes()
        rows[relative] = {
            "base_git_blob_sha1": blob,
            "base_git_blob_sha256": sha(source),
            "worktree_sha256": sha(worktree),
            "base_bytes": len(source),
            "worktree_bytes": len(worktree),
            "byte_identical_to_base": source == worktree,
        }
    for relative in NEW_SOURCE_PATHS:
        data = (ROOT / relative).read_bytes()
        rows[relative] = {
            "base_git_blob_sha1": None,
            "base_git_blob_sha256": None,
            "worktree_sha256": sha(data),
            "base_bytes": None,
            "worktree_bytes": len(data),
            "byte_identical_to_base": None,
        }
    return rows


def write_json(path: Path, value: dict) -> bytes:
    payload = json.dumps(value, indent=2, sort_keys=True) + "\n"
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(payload)
    return payload.encode("utf-8")


def build() -> tuple[dict, dict]:
    source_hashes = {
        "schema": "wp84.physical-kernel-source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": "codex/wp84-physical-kernel-proper-power-aggregate-20261103",
        "files": original_source_hashes(),
    }
    source_path = ROOT / "evidence/WP84_PHYSICAL_KERNEL_SOURCE_HASHES.json"
    write_json(source_path, source_hashes)

    artifacts = {}
    for relative in ARTIFACT_PATHS:
        data = (ROOT / relative).read_bytes()
        artifacts[relative] = {"sha256": sha(data), "bytes": len(data)}
    manifest = {
        "schema": "wp84.physical-kernel-proper-power.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": "codex/wp84-physical-kernel-proper-power-aggregate-20261103",
        "decision": "PROPER_POWER_EXCEPTION_CONTROLLED",
        "decision_scope": "complete one-base family for the reported positive atom only; full R400 aggregate remains open",
        "source_hash_file": "evidence/WP84_PHYSICAL_KERNEL_SOURCE_HASHES.json",
        "artifacts": artifacts,
        "manifest_self_hash_excluded": [
            "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.json",
            "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.sha256",
        ],
    }
    manifest_path = ROOT / "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.json"
    payload_bytes = write_json(manifest_path, manifest)
    digest = sha(payload_bytes)
    with (ROOT / "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.sha256").open(
        "w", encoding="ascii", newline="\n"
    ) as stream:
        stream.write(f"{digest}  {manifest_path.name}\n")
    return source_hashes, manifest


def verify() -> None:
    source_path = ROOT / "evidence/WP84_PHYSICAL_KERNEL_SOURCE_HASHES.json"
    manifest_path = ROOT / "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.json"
    sidecar_path = ROOT / "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.sha256"
    source_hashes = json.loads(source_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected_manifest_hash = sidecar_path.read_text(encoding="ascii").split()[0]
    if sha(manifest_path.read_bytes()) != expected_manifest_hash:
        raise RuntimeError("manifest sidecar mismatch")
    if source_hashes["base_commit"] != BASE or manifest["base_commit"] != BASE:
        raise RuntimeError("base commit mismatch")
    for relative, row in source_hashes["files"].items():
        actual = sha((ROOT / relative).read_bytes())
        if actual != row["worktree_sha256"]:
            raise RuntimeError(f"source hash mismatch: {relative}")
        if row["byte_identical_to_base"] is False:
            raise RuntimeError(f"preserved source differs from base: {relative}")
    for relative, row in manifest["artifacts"].items():
        data = (ROOT / relative).read_bytes()
        if sha(data) != row["sha256"] or len(data) != row["bytes"]:
            raise RuntimeError(f"artifact hash mismatch: {relative}")
    print(f"VERIFIED source files={len(source_hashes['files'])}")
    print(f"VERIFIED manifest artifacts={len(manifest['artifacts'])}")
    print(f"SHA256 manifest={expected_manifest_hash}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify()
        return
    source_hashes, manifest = build()
    print(f"WROTE source hashes for {len(source_hashes['files'])} files")
    print(f"WROTE manifest for {len(manifest['artifacts'])} artifacts")
    verify()


if __name__ == "__main__":
    main()
