#!/usr/bin/env python3
"""Build and verify the additive theorem-feasibility audit manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "d81bb1b6e46fb571906e7098e11372a5c38e8a2c"
BRANCH = "codex/wp84-ordinary-aggregate-feasibility-20261103"
SOURCE_INPUTS = [
    "notes/WP84_R400_PHYSICAL_CUMULANT_ENDPOINT_DIFFERENCE_AND_TENSOR_LIFT.md",
    "notes/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_AND_NEAR_PRODUCT_CLOSURE.md",
    "notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md",
    "notes/WP84_E2_PRINCIPAL_ARC_NORMALIZATION_AUDIT.md",
    "notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md",
    "notes/WP84_PRODUCT_BLOCK_LARGE_SIEVE.md",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SHA256_MANIFEST.json",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SHA256_MANIFEST.sha256",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json",
    "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_LEDGER.json",
    "evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json",
    "evidence/WP84_R400_PARENT_PHYSICAL_ATOM_REPLAY.json",
    "src/wp84_r400_cumulant_endpoint_tensor.py",
    "src/wp84_r400_cumulant_endpoint_tensor_manifest.py",
    "src/wp84_r400_physical_endpoint_averaging.py",
    "src/wp84_r400_schatten_absorption_audit.py",
    "src/wp84_physical_kernel_proper_power_reconciliation.py",
    "tests/test_wp84_r400_cumulant_endpoint_tensor.py",
    "tests/test_wp84_r400_schatten_absorption_audit.py",
]
ARTIFACTS = [
    "notes/WP84_R400_ORDINARY_AGGREGATE_THEOREM_FEASIBILITY_HARD_STOP.md",
    "src/wp84_r400_theorem_feasibility.py",
    "src/wp84_r400_theorem_feasibility_manifest.py",
    "tests/test_wp84_r400_theorem_feasibility.py",
    "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_CHECKS.json",
    "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_TEST_NORMAL.log",
    "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_TEST_O.log",
    "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_TEST_OO.log",
    "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_PARENT_MANIFEST_REPLAY.log",
]
SOURCE_HASH_PATH = "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SOURCE_HASHES.json"
MANIFEST_PATH = "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.json"
SIDECAR_PATH = "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.sha256"
EXTERNAL_REFERENCES = {
    "evans": {
        "title": "Natalie Evans, Correlations of Almost Primes",
        "url": "https://arxiv.org/abs/2102.12297",
        "version_checked": "arXiv source page and full text opened 2026-11-03",
        "local_source_file": None,
    },
    "guth_maynard": {
        "title": "Larry Guth and James Maynard, New Large Value Estimates for Dirichlet Polynomials",
        "url": "https://annals.math.princeton.edu/2026/203-2/p06",
        "accepted_manuscript": "https://ora.ox.ac.uk/objects/uuid:ad11b8bf-ad2b-4ebf-a627-647f023c378f/files/s73666708v",
        "local_source_file": None,
    },
    "montgomery_vaughan": {
        "title": "H. L. Montgomery and R. C. Vaughan, The Large Sieve, Mathematika 20 (1973), 119-134",
        "doi": "https://doi.org/10.1112/S0025579300004708",
        "author_pdf": "https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf",
        "local_source_file": None,
    },
}


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
        raise RuntimeError("requested base is not an ancestor of HEAD")
    branch = git_bytes("branch", "--show-current").decode().strip()
    if branch != BRANCH:
        raise RuntimeError(f"wrong audit branch: {branch}")
    files = {}
    for relative in SOURCE_INPUTS:
        base_data = git_bytes("show", f"{BASE}:{relative}")
        work_data = (ROOT / relative).read_bytes()
        normalized_same = base_data.replace(b"\r\n", b"\n") == work_data.replace(b"\r\n", b"\n")
        if not normalized_same:
            raise RuntimeError(f"historical source changed from base: {relative}")
        files[relative] = {
            "base_git_blob": git_bytes("rev-parse", f"{BASE}:{relative}").decode().strip(),
            "base_sha256": sha256(base_data),
            "base_bytes": len(base_data),
            "worktree_sha256": sha256(work_data),
            "worktree_bytes": len(work_data),
            "unchanged_from_base_after_line_ending_normalization": True,
        }
    return {
        "schema": "wp84.r400.ordinary-theorem-feasibility.source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "method": "SHA-256 of raw git-show base blobs and worktree files; only CRLF/LF normalization is used to check historical-input immutability",
        "files": files,
        "external_primary_sources": EXTERNAL_REFERENCES,
    }


def manifest_for(source_digest: str) -> dict:
    artifacts = {}
    for relative in ARTIFACTS + [SOURCE_HASH_PATH]:
        data = (ROOT / relative).read_bytes()
        artifacts[relative] = {"bytes": len(data), "sha256": sha256(data)}
    return {
        "schema": "wp84.r400.ordinary-theorem-feasibility.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "decisions": {
            "PUBLISHED_SOURCE_TRANSFER": "INSUFFICIENT",
            "ENDPOINT_CORRECTION": "OPEN",
            "ORDINARY_CONNECTED_AGGREGATE": "OPEN",
            "R400_CONSUMER": "OPEN",
            "NEXT_ACTION": "NEW_ANALYTIC_THEOREM_REQUIRED",
            "STRICT_GT_79_PERCENT": "OPEN",
            "RIEMANN_HYPOTHESIS": "OPEN",
        },
        "source_hash_inventory": {"path": SOURCE_HASH_PATH, "sha256": source_digest},
        "artifacts": artifacts,
        "self_hash_excluded": [MANIFEST_PATH, SIDECAR_PATH],
        "claim_boundary": "Published estimates checked here do not prove the source-weighted positive-part bound; no ordinary-prime source counterexample is claimed.",
    }


def write_all() -> None:
    source_data = source_inventory()
    source_bytes = (json.dumps(source_data, indent=2, sort_keys=True) + "\n").encode()
    (ROOT / SOURCE_HASH_PATH).write_bytes(source_bytes)
    manifest = manifest_for(sha256(source_bytes))
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    (ROOT / MANIFEST_PATH).write_bytes(manifest_bytes)
    (ROOT / SIDECAR_PATH).write_text(
        sha256(manifest_bytes) + "  " + MANIFEST_PATH + "\n", encoding="ascii"
    )
    print(f"WROTE {SOURCE_HASH_PATH}: {len(source_data['files'])} unchanged base inputs")
    print(f"WROTE {MANIFEST_PATH}: {len(manifest['artifacts'])} hashed artifacts")
    print(f"MANIFEST_SHA256 {sha256(manifest_bytes)}")


def verify() -> None:
    manifest_bytes = (ROOT / MANIFEST_PATH).read_bytes()
    manifest = json.loads(manifest_bytes)
    expected_sidecar = sha256(manifest_bytes) + "  " + MANIFEST_PATH
    if (ROOT / SIDECAR_PATH).read_text(encoding="ascii").strip() != expected_sidecar:
        raise RuntimeError("new manifest sidecar mismatch")
    for relative, record in manifest["artifacts"].items():
        data = (ROOT / relative).read_bytes()
        if len(data) != record["bytes"] or sha256(data) != record["sha256"]:
            raise RuntimeError(f"artifact hash mismatch: {relative}")
    source_bytes = (ROOT / SOURCE_HASH_PATH).read_bytes()
    if sha256(source_bytes) != manifest["source_hash_inventory"]["sha256"]:
        raise RuntimeError("source inventory digest mismatch")
    inventory = json.loads(source_bytes)
    for relative, record in inventory["files"].items():
        data = (ROOT / relative).read_bytes()
        if sha256(data) != record["worktree_sha256"]:
            raise RuntimeError(f"source hash mismatch: {relative}")
        if not record["unchanged_from_base_after_line_ending_normalization"]:
            raise RuntimeError(f"historical input was not confirmed unchanged: {relative}")
    print(
        f"PASS new manifest and sidecar, {len(manifest['artifacts'])} artifacts, "
        f"{len(inventory['files'])} unchanged base inputs"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify() if args.verify else write_all()
