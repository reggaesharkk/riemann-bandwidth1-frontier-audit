#!/usr/bin/env python3
"""Build/verify hashes for the additive WP84 R400 Schatten audit revision."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "b1ff152df352216aa44c9a2535f04306a39df859"
BRANCH = "codex/wp84-r400-schatten-ordinary-aggregate-20261103"

HISTORICAL_SOURCES = (
    "notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md",
    "src/wp84_r400_filtered_connected_kernel.py",
    "src/wp84_r400_filtered_sharp_repair.py",
    "notes/WP84_R400_EXACT_PAIR_LAYER.md",
    "src/wp84_r400_pair_layer_exact.py",
    "notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md",
    "notes/WP84_ADAPTIVE_BOUNDARY_LOCAL_LARGE_SIEVE.md",
    "src/wp84_adaptive_boundary_large_sieve.py",
    "notes/WP84_SOURCE_WEIGHT_CONE_FOURTH_ORDER_OPERATOR_AUDIT.md",
    "src/wp84_source_weight_cone_audit.py",
    "evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_ORIENTATION_INTERVALS.json",
    "evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json",
    "src/wp84_physical_kernel_proper_power_reconciliation.py",
    "evidence/WP84_PHYSICAL_KERNEL_SOURCE_HASHES.json",
    "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.json",
)

NEW_SOURCES = (
    "notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md",
    "src/wp84_r400_schatten_absorption_audit.py",
    "src/wp84_r400_source_interval_replay.py",
    "src/wp84_r400_schatten_manifest.py",
    "tests/test_wp84_r400_schatten_absorption_audit.py",
)

ARTIFACTS = (
    *NEW_SOURCES,
    "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json",
    "evidence/WP84_R400_SOURCE_INTERVAL_REPLAY.json",
    "evidence/WP84_R400_SOURCE_INTERVAL_REPLAY.log",
    "evidence/WP84_R400_PHYSICAL_ATOM_INTERVAL_REPLAY.log",
    "evidence/WP84_R400_PARENT_PHYSICAL_ATOM_REPLAY.json",
    "evidence/WP84_R400_PARENT_ATOM_REPLAY.log",
    "evidence/WP84_R400_PARENT_PAIR_CERT_REPLAY.log",
    "evidence/WP84_R400_SCHATTEN_CHECKER_NORMAL.log",
    "evidence/WP84_R400_TEST_NORMAL.log",
    "evidence/WP84_R400_TEST_O.log",
    "evidence/WP84_R400_TEST_OO.log",
    "evidence/WP84_R400_SOURCE_HASHES.json",
)

SOURCE_HASH_PATH = "evidence/WP84_R400_SOURCE_HASHES.json"
MANIFEST_PATH = ROOT / "evidence" / "WP84_R400_SHA256_MANIFEST.json"
SIDECAR_PATH = ROOT / "evidence" / "WP84_R400_SHA256_MANIFEST.sha256"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_eol(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def git_bytes(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def build_source_inventory() -> dict:
    rows = {}
    for relative in HISTORICAL_SOURCES:
        blob = git("rev-parse", f"{BASE}:{relative}")
        base_bytes = git_bytes("cat-file", "blob", blob)
        worktree = (ROOT / relative).read_bytes()
        rows[relative] = {
            "base_git_blob_sha1": blob,
            "base_git_blob_sha256": sha(base_bytes),
            "base_normalized_sha256": sha(normalize_eol(base_bytes)),
            "worktree_sha256": sha(worktree),
            "worktree_normalized_sha256": sha(normalize_eol(worktree)),
            "base_bytes": len(base_bytes),
            "worktree_bytes": len(worktree),
            "byte_identical_to_base": base_bytes == worktree,
            "line_ending_normalized_identical": normalize_eol(base_bytes) == normalize_eol(worktree),
        }
    for relative in NEW_SOURCES:
        data = (ROOT / relative).read_bytes()
        rows[relative] = {
            "base_git_blob_sha1": None,
            "base_git_blob_sha256": None,
            "base_normalized_sha256": None,
            "worktree_sha256": sha(data),
            "worktree_normalized_sha256": sha(normalize_eol(data)),
            "base_bytes": None,
            "worktree_bytes": len(data),
            "byte_identical_to_base": None,
            "line_ending_normalized_identical": None,
        }
    return rows


def write_json(path: Path, value: dict) -> bytes:
    payload = json.dumps(value, indent=2, sort_keys=True) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(payload)
    return payload.encode("utf-8")


def build() -> None:
    require_branch_and_base()
    inventory = {
        "schema": "wp84.r400.schatten.source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "files": build_source_inventory(),
    }
    write_json(ROOT / SOURCE_HASH_PATH, inventory)

    artifact_rows = {}
    for relative in ARTIFACTS:
        data = (ROOT / relative).read_bytes()
        artifact_rows[relative] = {"sha256": sha(data), "bytes": len(data)}

    manifest = {
        "schema": "wp84.r400.schatten.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "decisions": {
            "PROPER_POWER_SCHATTEN_ABSORPTION": "PROVED",
            "ORDINARY_PHYSICAL_CONNECTED_AGGREGATE": "OPEN",
            "R400_CONSUMER": "OPEN",
        },
        "source_hash_file": SOURCE_HASH_PATH,
        "artifacts": artifact_rows,
        "manifest_self_hash_excluded": [
            "evidence/WP84_R400_SHA256_MANIFEST.json",
            "evidence/WP84_R400_SHA256_MANIFEST.sha256",
        ],
    }
    payload = write_json(MANIFEST_PATH, manifest)
    SIDECAR_PATH.write_text(f"{sha(payload)}  {MANIFEST_PATH.name}\n", encoding="ascii")


def require_branch_and_base() -> None:
    branch = git("branch", "--show-current")
    if branch != BRANCH:
        raise RuntimeError(f"unexpected branch {branch!r}")
    merge_base = git("merge-base", "HEAD", BASE)
    if merge_base != BASE:
        raise RuntimeError(f"base commit is not an ancestor: {merge_base}")


def verify() -> None:
    require_branch_and_base()
    inventory = json.loads((ROOT / SOURCE_HASH_PATH).read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    expected_self_hash = SIDECAR_PATH.read_text(encoding="ascii").split()[0]
    if sha(MANIFEST_PATH.read_bytes()) != expected_self_hash:
        raise RuntimeError("SHA-256 manifest sidecar mismatch")
    if inventory["base_commit"] != BASE or manifest["base_commit"] != BASE:
        raise RuntimeError("base commit mismatch")
    for relative, row in inventory["files"].items():
        current = (ROOT / relative).read_bytes()
        if sha(current) != row["worktree_sha256"]:
            raise RuntimeError(f"source hash mismatch: {relative}")
        if row["base_git_blob_sha1"] and not row["line_ending_normalized_identical"]:
            raise RuntimeError(f"historical source changed from base: {relative}")
        if row["base_git_blob_sha1"]:
            base = git_bytes("cat-file", "blob", row["base_git_blob_sha1"])
            if sha(base) != row["base_git_blob_sha256"]:
                raise RuntimeError(f"base blob hash mismatch: {relative}")
            if normalize_eol(base) != normalize_eol(current):
                raise RuntimeError(f"historical source differs after EOL normalization: {relative}")
    for relative, row in manifest["artifacts"].items():
        current = (ROOT / relative).read_bytes()
        if sha(current) != row["sha256"] or len(current) != row["bytes"]:
            raise RuntimeError(f"artifact hash mismatch: {relative}")
    print(f"VERIFIED historical source files={len(HISTORICAL_SOURCES)}")
    print(f"VERIFIED new source files={len(NEW_SOURCES)}")
    print(f"VERIFIED manifest artifacts={len(manifest['artifacts'])}")
    print(f"BASE={BASE}")
    print(f"SHA256 manifest={expected_self_hash}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if not args.verify:
        build()
    verify()


if __name__ == "__main__":
    main()
