#!/usr/bin/env python3
"""Build/verify source hashes and artifact hashes for the endpoint audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "6d4d43cea2479966ba0081dfbb38058fe6fffb87"
BRANCH = "codex/wp84-r400-endpoint-near-product-20261103"
SOURCES = [
    "notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md",
    "notes/WP84_GOOD_ENDPOINT_TRIMMING.md",
    "notes/WP84_F1C_FIRST_STRIKE_ENDPOINT_SOURCE_AUDIT.md",
    "notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md",
    "notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md",
    "notes/WP84_DETUNING_COMMUTATOR_ENDPOINT.md",
    "src/wp84_r400_schatten_absorption_audit.py",
    "src/wp84_r400_source_interval_replay.py",
    "src/wp84_r400_pair_layer_exact.py",
    "src/wp84_r400_first_record_assembly.py",
    "tests/test_wp84_r400_schatten_absorption_audit.py",
    "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json",
    "evidence/WP84_R400_SOURCE_INTERVAL_REPLAY.json",
    "evidence/WP84_R400_PARENT_PHYSICAL_ATOM_REPLAY.json",
    "evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json",
]
ARTIFACTS = [
    "notes/WP84_R400_ENDPOINT_QUANTIFIERS_AND_NEAR_PRODUCT_AUDIT.md",
    "src/wp84_r400_endpoint_near_product_audit.py",
    "src/wp84_r400_endpoint_near_product_manifest.py",
    "tests/test_wp84_r400_endpoint_near_product_audit.py",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_TEST_NORMAL.log",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_TEST_O.log",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_TEST_OO.log",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_PARENT_INTERVAL_REPLAY.log",
]
SOURCE_HASH_PATH = "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SOURCE_HASHES.json"
MANIFEST_PATH = "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SHA256_MANIFEST.json"
SIDECAR_PATH = "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SHA256_MANIFEST.sha256"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).stdout


def source_inventory() -> dict:
    files = {}
    for path in SOURCES:
        base_data = git_bytes("show", f"{BASE}:{path}")
        worktree_data = (ROOT / path).read_bytes()
        normalized = worktree_data.replace(b"\r\n", b"\n")
        base_normalized = base_data.replace(b"\r\n", b"\n")
        files[path] = {
            "base_git_blob": git_bytes("rev-parse", f"{BASE}:{path}").decode().strip(),
            "base_sha256": sha256(base_data),
            "base_bytes": len(base_data),
            "worktree_sha256": sha256(worktree_data),
            "worktree_normalized_sha256": sha256(normalized),
            "worktree_bytes": len(worktree_data),
            "line_ending_normalized_identical_to_base": normalized == base_normalized,
        }
        if normalized != base_normalized:
            raise RuntimeError(f"historical input changed from base: {path}")
    return {
        "schema": "wp84.r400.endpoint-near-product.source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "method": "base bytes are read from git show BASE:path; worktree comparison normalizes CRLF only",
        "files": files,
        "external_primary_reference": {
            "title": "Montgomery and Vaughan, The Large Sieve, Mathematika 20 (1973), Theorem 1 and Lemma 1",
            "url": "https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf",
            "use": "separated-point trigonometric-polynomial inequality and explicit matrix self-duality",
        },
    }


def artifact_manifest(source_hash_digest: str) -> dict:
    artifacts = {}
    for path in ARTIFACTS + [SOURCE_HASH_PATH]:
        data = (ROOT / path).read_bytes()
        artifacts[path] = {"bytes": len(data), "sha256": sha256(data)}
    return {
        "schema": "wp84.r400.endpoint-near-product.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "decisions": {
            "SCHATTEN_TRANSFER": "PROVED",
            "EXISTENTIAL_ENDPOINT_REDUCTION": "NOT_SUFFICIENT",
            "ORDINARY_CONNECTED_AGGREGATE": "OPEN",
            "R400_CONSUMER": "CONDITIONAL",
        },
        "source_hash_inventory": {"path": SOURCE_HASH_PATH, "sha256": source_hash_digest},
        "artifacts": artifacts,
        "self_hash_excluded": [MANIFEST_PATH, SIDECAR_PATH],
        "claim_boundary": "Tests verify finite bookkeeping; the source-weighted asymptotic connected inequality remains open.",
    }


def write_all() -> None:
    source_data = source_inventory()
    source_bytes = (json.dumps(source_data, indent=2, sort_keys=True) + "\n").encode()
    source_path = ROOT / SOURCE_HASH_PATH
    source_path.write_bytes(source_bytes)
    manifest = artifact_manifest(sha256(source_bytes))
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    (ROOT / MANIFEST_PATH).write_bytes(manifest_bytes)
    (ROOT / SIDECAR_PATH).write_text(sha256(manifest_bytes) + "  " + MANIFEST_PATH + "\n", encoding="ascii")
    print(f"WROTE {SOURCE_HASH_PATH}: {len(source_data['files'])} unchanged historical inputs")
    print(f"WROTE {MANIFEST_PATH}: {len(manifest['artifacts'])} artifacts")
    print(f"MANIFEST_SHA256 {sha256(manifest_bytes)}")


def verify() -> None:
    manifest_bytes = (ROOT / MANIFEST_PATH).read_bytes()
    manifest = json.loads(manifest_bytes)
    expected_sidecar = sha256(manifest_bytes) + "  " + MANIFEST_PATH
    actual_sidecar = (ROOT / SIDECAR_PATH).read_text(encoding="ascii").strip()
    if expected_sidecar != actual_sidecar:
        raise RuntimeError("manifest sidecar mismatch")
    for path, record in manifest["artifacts"].items():
        data = (ROOT / path).read_bytes()
        if len(data) != record["bytes"] or sha256(data) != record["sha256"]:
            raise RuntimeError(f"artifact hash mismatch: {path}")
    source_bytes = (ROOT / SOURCE_HASH_PATH).read_bytes()
    if sha256(source_bytes) != manifest["source_hash_inventory"]["sha256"]:
        raise RuntimeError("source hash inventory mismatch")
    inventory = json.loads(source_bytes)
    for path, record in inventory["files"].items():
        if not record["line_ending_normalized_identical_to_base"]:
            raise RuntimeError(f"historical source mismatch: {path}")
    print(f"PASS: manifest, sidecar, {len(manifest['artifacts'])} artifacts, and {len(inventory['files'])} base inputs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify() if args.verify else write_all()
