#!/usr/bin/env python3
"""Generate/replay hashes and independent runtime checks for the additive audit."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "13752ebd5cc399bf5cd04b74b679a0f59ab8eb41"
BRANCH = "codex/wp84-endpoint-restricted-ordinary-attack-20261103"
SOURCE_INPUTS = [
    "notes/WP84_F1C_FIRST_STRIKE_ENDPOINT_SOURCE_AUDIT.md",
    "notes/WP84_F1_ENDPOINT_FEATURE_LENGTH_INVESTIGATION.md",
    "notes/WP84_F1B_PRODUCT_FREQUENCY_ENDPOINT_BUDGET.md",
    "notes/WP84_DECISION_D_ENDPOINT_ADMISSIBILITY_DENSITY.md",
    "notes/WP84_GOOD_ENDPOINT_TRIMMING.md",
    "notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md",
    "notes/WP84_R400_ORDINARY_AGGREGATE_THEOREM_FEASIBILITY_HARD_STOP.md",
    "notes/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_AND_NEAR_PRODUCT_CLOSURE.md",
    "notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md",
    "notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_LEDGER.json",
    "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.json",
    "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.sha256",
]
ARTIFACTS = [
    "notes/WP84_R400_ENDPOINT_RESTRICTED_ORDINARY_PRIME_THEOREM_ATTACK.md",
    "src/wp84_r400_endpoint_restricted_attack.py",
    "src/wp84_r400_endpoint_restricted_attack_manifest.py",
    "tests/test_wp84_r400_endpoint_restricted_attack.py",
    "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_CHECKS.json",
    "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_TEST_NORMAL.log",
    "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_TEST_O.log",
    "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_TEST_OO.log",
    "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_PARENT_REPLAY.log",
]
SOURCE_HASH_PATH = "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_SOURCE_HASHES.json"
MANIFEST_PATH = "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_SHA256_MANIFEST.json"
SIDECAR_PATH = "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_SHA256_MANIFEST.sha256"
PARENT_MANIFEST = "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.json"
PARENT_SIDECAR = "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.sha256"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def replay_parent_manifest() -> str:
    manifest_bytes = (ROOT / PARENT_MANIFEST).read_bytes()
    manifest = json.loads(manifest_bytes)
    expected = sha256(manifest_bytes) + "  " + PARENT_MANIFEST
    if (ROOT / PARENT_SIDECAR).read_text(encoding="ascii").strip() != expected:
        raise RuntimeError("predecessor feasibility manifest sidecar mismatch")
    for path, record in manifest["artifacts"].items():
        data = (ROOT / path).read_bytes()
        if len(data) != record["bytes"] or sha256(data) != record["sha256"]:
            raise RuntimeError(f"predecessor manifest artifact mismatch: {path}")
    return (f"PASS predecessor manifest sidecar and {len(manifest['artifacts'])} "
            f"artifacts; parent base={manifest['base_commit']}\n")


def source_inventory() -> dict:
    if git("rev-parse", "--verify", f"{BASE}^{{commit}}").decode().strip() != BASE:
        raise RuntimeError("requested base commit does not resolve exactly")
    if git("branch", "--show-current").decode().strip() != BRANCH:
        raise RuntimeError("wrong audit branch")
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"],
                              cwd=ROOT, check=False)
    if ancestor.returncode:
        raise RuntimeError("requested base is not an ancestor of HEAD")
    files = {}
    for relative in SOURCE_INPUTS:
        base_data = git("show", f"{BASE}:{relative}")
        work_data = (ROOT / relative).read_bytes()
        same = base_data.replace(b"\r\n", b"\n") == work_data.replace(b"\r\n", b"\n")
        if not same:
            raise RuntimeError(f"historical source changed: {relative}")
        files[relative] = {
            "base_git_blob": git("rev-parse", f"{BASE}:{relative}").decode().strip(),
            "base_sha256": sha256(base_data),
            "worktree_sha256": sha256(work_data),
            "bytes": len(work_data),
            "unchanged_from_base_after_line_ending_normalization": True,
        }
    return {
        "schema": "wp84.r400.endpoint-restricted-attack.source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "method": "SHA-256 of raw base blobs and worktree bytes; historical inputs checked unchanged after CRLF/LF normalization",
        "files": files,
        "predecessor_manifest_sha256": sha256((ROOT / PARENT_MANIFEST).read_bytes()),
    }


def run_tests() -> dict:
    commands = [
        ("NORMAL", [sys.executable, "-m", "unittest", "discover", "-s", "tests",
                    "-p", "test_wp84_r400_endpoint_restricted_attack.py", "-v"]),
        ("O", [sys.executable, "-O", "-m", "unittest", "discover", "-s", "tests",
               "-p", "test_wp84_r400_endpoint_restricted_attack.py", "-v"]),
        ("OO", [sys.executable, "-OO", "-m", "unittest", "discover", "-s", "tests",
                "-p", "test_wp84_r400_endpoint_restricted_attack.py", "-v"]),
    ]
    results = {}
    for label, command in commands:
        proc = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
        log_path = f"evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_TEST_{label}.log"
        (ROOT / log_path).write_text(proc.stdout, encoding="utf-8", newline="\n")
        if proc.returncode:
            raise RuntimeError(f"{label} test run failed; see {log_path}")
        results[label] = {"command": command, "exit_code": proc.returncode,
                          "log": log_path, "sha256": sha256(proc.stdout.encode())}
    return results


def write_evidence() -> None:
    parent_log = replay_parent_manifest()
    (ROOT / "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_PARENT_REPLAY.log").write_text(
        parent_log, encoding="utf-8", newline="\n")
    sys.path.insert(0, str(ROOT))
    from src.wp84_r400_endpoint_restricted_attack import exact_summary
    checks = {
        "decisions": {
            "GOOD_SECTION_SET": "INCOMPLETE",
            "RESTRICTED_THEOREM": "OPEN",
            "SOURCE_CONDITIONING_ADVANTAGE": "NONE_FOUND",
            "R400_RECORD_BUDGET": "OPEN",
            "NEXT_ACTION": "FREEZE_R400_ROUTE",
        },
        "exact_arithmetic": exact_summary(),
        "test_runs": run_tests(),
        "claim_boundary": "Finite exact logic checks only; no legal prime-source counterexample or asymptotic ordinary-prime bound is claimed.",
    }
    checks_path = ROOT / "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_CHECKS.json"
    checks_path.write_text(json.dumps(checks, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8", newline="\n")
    source_data = source_inventory()
    source_bytes = (json.dumps(source_data, indent=2, sort_keys=True) + "\n").encode()
    (ROOT / SOURCE_HASH_PATH).write_bytes(source_bytes)
    artifacts = {}
    for relative in ARTIFACTS + [SOURCE_HASH_PATH]:
        data = (ROOT / relative).read_bytes()
        artifacts[relative] = {"bytes": len(data), "sha256": sha256(data)}
    manifest = {
        "schema": "wp84.r400.endpoint-restricted-attack.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "decisions": checks["decisions"],
        "source_hash_inventory": {"path": SOURCE_HASH_PATH, "sha256": sha256(source_bytes)},
        "artifacts": artifacts,
        "self_hash_excluded": [MANIFEST_PATH, SIDECAR_PATH],
        "claim_boundary": checks["claim_boundary"],
    }
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    (ROOT / MANIFEST_PATH).write_bytes(manifest_bytes)
    (ROOT / SIDECAR_PATH).write_text(
        sha256(manifest_bytes) + "  " + MANIFEST_PATH + "\n", encoding="ascii", newline="\n")
    print(f"PASS source hashes: {len(source_data['files'])} unchanged parent inputs")
    print(f"PASS independent runtime checks: {len(checks['test_runs'])} modes")
    print(f"PASS artifacts hashed: {len(artifacts)}")
    print(f"MANIFEST_SHA256 {sha256(manifest_bytes)}")


def verify() -> None:
    manifest_bytes = (ROOT / MANIFEST_PATH).read_bytes()
    manifest = json.loads(manifest_bytes)
    sidecar = sha256(manifest_bytes) + "  " + MANIFEST_PATH
    if (ROOT / SIDECAR_PATH).read_text(encoding="ascii").strip() != sidecar:
        raise RuntimeError("new manifest sidecar mismatch")
    for relative, record in manifest["artifacts"].items():
        data = (ROOT / relative).read_bytes()
        if len(data) != record["bytes"] or sha256(data) != record["sha256"]:
            raise RuntimeError(f"new artifact hash mismatch: {relative}")
    inventory_bytes = (ROOT / SOURCE_HASH_PATH).read_bytes()
    if sha256(inventory_bytes) != manifest["source_hash_inventory"]["sha256"]:
        raise RuntimeError("source hash inventory digest mismatch")
    for relative, record in json.loads(inventory_bytes)["files"].items():
        data = (ROOT / relative).read_bytes()
        if sha256(data) != record["worktree_sha256"]:
            raise RuntimeError(f"source hash mismatch: {relative}")
    print(f"PASS manifest and sidecar, {len(manifest['artifacts'])} artifacts, "
          f"{len(json.loads(inventory_bytes)['files'])} parent inputs")


if __name__ == "__main__":
    if "--verify" in sys.argv:
        verify()
    else:
        write_evidence()
