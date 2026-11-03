#!/usr/bin/env python3
"""Replay and hash the frozen WP84 R400 theorem inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "99712a495db3258f938f2509d1eaa37cbc966a03"
BRANCH = "codex/wp84-frozen-theorem-inventory-20261103"

PARENT_MANIFESTS = [
    ("evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.json",
     "evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.sha256"),
    ("evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.json",
     "evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.sha256"),
    ("evidence/WP84_R400_SHA256_MANIFEST.json",
     "evidence/WP84_R400_SHA256_MANIFEST.sha256"),
    ("evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SHA256_MANIFEST.json",
     "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SHA256_MANIFEST.sha256"),
    ("evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SHA256_MANIFEST.json",
     "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_SHA256_MANIFEST.sha256"),
    ("evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SHA256_MANIFEST.json",
     "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_SHA256_MANIFEST.sha256"),
    ("evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.json",
     "evidence/WP84_R400_ORDINARY_THEOREM_FEASIBILITY_SHA256_MANIFEST.sha256"),
    ("evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_SHA256_MANIFEST.json",
     "evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_SHA256_MANIFEST.sha256"),
]

SOURCE_INPUTS = [
    "notes/WP84_SOURCE_WEIGHT_CONE_FOURTH_ORDER_OPERATOR_AUDIT.md",
    "notes/WP84_PHYSICAL_KERNEL_PROPER_POWER_AGGREGATE_AUDIT.md",
    "notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md",
    "notes/WP84_R400_EXACT_PAIR_LAYER.md",
    "notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md",
    "notes/WP84_R400_PHYSICAL_CUMULANT_ENDPOINT_DIFFERENCE_AND_TENSOR_LIFT.md",
    "notes/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_AND_NEAR_PRODUCT_CLOSURE.md",
    "notes/WP84_R400_ORDINARY_AGGREGATE_THEOREM_FEASIBILITY_HARD_STOP.md",
    "notes/WP84_R400_ENDPOINT_RESTRICTED_ORDINARY_PRIME_THEOREM_ATTACK.md",
    "notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md",
    "notes/WP84_CROSS_SCALE_SHARP_DETUNING.md",
    "notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md",
    "notes/WP84_R400_COMPLETE_WORD_LEDGER_REPLAY.md",
    "src/wp84_physical_kernel_proper_power_reconciliation.py",
    "src/wp84_r400_filtered_connected_kernel.py",
    "src/wp84_r400_pair_layer_exact.py",
    "src/wp84_r400_schatten_absorption_audit.py",
    "src/wp84_r400_cumulant_endpoint_tensor.py",
    "src/wp84_r400_physical_endpoint_averaging.py",
    "src/wp84_fixed_scale_connected_kernel.py",
    "src/wp84_cross_scale_sharp_detuning.py",
    "src/wp84_balanced_orientation_normalization.py",
    "src/wp84_phi4_equal_scale_brownian_kernel.py",
    "tests/test_wp84_physical_kernel_reconciliation.py",
    "tests/test_wp84_r400_schatten_absorption_audit.py",
    "tests/test_wp84_r400_cumulant_endpoint_tensor.py",
    "evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json",
    "evidence/WP84_SOURCE_WEIGHT_CONE_ORIENTATION_INTERVALS.json",
    "evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json",
    "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json",
    "evidence/WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json",
    "evidence/WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_LEDGER.json",
    "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json",
]

CORE_TESTS = [
    "tests.test_wp84_physical_kernel_reconciliation",
    "tests.test_wp84_r400_schatten_absorption_audit",
    "tests.test_wp84_r400_cumulant_endpoint_tensor",
]
AUX_TESTS = [
    "tests.test_wp84_r400_physical_endpoint_averaging",
    "tests.test_wp84_r400_endpoint_near_product_audit",
    "tests.test_wp84_r400_theorem_feasibility",
    "tests.test_wp84_r400_endpoint_restricted_attack",
]
CERTIFICATES = [
    ("PAIR_LAYER", ["src/wp84_r400_pair_layer_exact.py"]),
    ("PHYSICAL_FILTERED_KERNEL", ["src/wp84_r400_filtered_connected_kernel.py", "--certificate"]),
    ("GEOMETRIC_FIXED_SCALE", ["src/wp84_fixed_scale_connected_kernel.py"]),
    ("GEOMETRIC_CROSS_SCALE", ["src/wp84_cross_scale_sharp_detuning.py"]),
    ("ORIENTATION_NORMALIZATION", ["src/wp84_balanced_orientation_normalization.py"]),
    ("EQUAL_SCALE_BROWNIAN", ["src/wp84_phi4_equal_scale_brownian_kernel.py"]),
]

DECISION_PATH = "evidence/WP84_FROZEN_R400_DECISION_RECORD.json"
CHECKS_PATH = "evidence/WP84_FROZEN_R400_REPLAY_CHECKS.json"
SOURCE_HASH_PATH = "evidence/WP84_FROZEN_R400_SOURCE_HASHES.json"
MANIFEST_PATH = "evidence/WP84_FROZEN_R400_SHA256_MANIFEST.json"
SIDECAR_PATH = "evidence/WP84_FROZEN_R400_SHA256_MANIFEST.sha256"
ARTIFACTS = [
    "notes/WP84_FROZEN_R400_THEOREM_INVENTORY.md",
    "notes/WP84_FROZEN_R400_HOSTILE_PROOF_READINESS.md",
    "notes/WP84_FROZEN_R400_PUBLICATION_PRIORITY.md",
    "notes/WP84_FROZEN_R400_REPRODUCIBILITY.md",
    "src/wp84_frozen_r400_theorem_inventory_manifest.py",
    DECISION_PATH,
    CHECKS_PATH,
    "evidence/WP84_FROZEN_R400_CORE_TEST_NORMAL.log",
    "evidence/WP84_FROZEN_R400_CORE_TEST_O.log",
    "evidence/WP84_FROZEN_R400_CORE_TEST_OO.log",
    "evidence/WP84_FROZEN_R400_AUX_TEST_NORMAL.log",
    "evidence/WP84_FROZEN_R400_CERTIFICATE_REPLAYS.json",
    "evidence/WP84_FROZEN_R400_PARENT_MANIFEST_REPLAY.json",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def current_branch() -> str:
    return git_bytes("branch", "--show-current").decode().strip()


def require_repo_state() -> None:
    if git_bytes("rev-parse", "--verify", f"{BASE}^{{commit}}").decode().strip() != BASE:
        raise RuntimeError("frozen base commit does not resolve exactly")
    if current_branch() != BRANCH:
        raise RuntimeError(f"expected audit branch {BRANCH}, found {current_branch()}")
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"],
                              cwd=ROOT, check=False)
    if ancestor.returncode:
        raise RuntimeError("frozen base is not an ancestor of HEAD")


def check_parent_manifests() -> list[dict]:
    rows = []
    for manifest_path, sidecar_path in PARENT_MANIFESTS:
        data = (ROOT / manifest_path).read_bytes()
        manifest = json.loads(data)
        sidecar_tokens = (ROOT / sidecar_path).read_text(encoding="ascii").split()
        if not sidecar_tokens or sidecar_tokens[0] != sha(data):
            raise RuntimeError(f"parent sidecar hash mismatch: {manifest_path}")
        # The earliest source-weight-cone inventory predates the unified
        # manifest schema and calls this mapping ``audit_artifacts``.
        artifacts = manifest.get("artifacts", manifest.get("audit_artifacts", {}))
        for relative, record in artifacts.items():
            artifact = (ROOT / relative).read_bytes()
            expected_hash = record.get("sha256")
            expected_len = record.get("bytes")
            if expected_hash != sha(artifact) or expected_len != len(artifact):
                raise RuntimeError(f"parent artifact mismatch: {relative}")
        rows.append({
            "manifest": manifest_path,
            "base_commit": manifest.get("base_commit"),
            "audit_branch": manifest.get("audit_branch"),
            "sidecar_sha256": sidecar_tokens[0],
            "artifacts_verified": len(artifacts),
            "result": "PASS",
        })
    return rows


def source_inventory() -> dict:
    require_repo_state()
    files = {}
    for relative in SOURCE_INPUTS:
        base_data = git_bytes("show", f"{BASE}:{relative}")
        work_data = (ROOT / relative).read_bytes()
        normalized_equal = base_data.replace(b"\r\n", b"\n") == work_data.replace(b"\r\n", b"\n")
        if not normalized_equal:
            raise RuntimeError(f"frozen source/evidence changed: {relative}")
        files[relative] = {
            "base_git_blob": git_bytes("rev-parse", f"{BASE}:{relative}").decode().strip(),
            "base_sha256": sha(base_data),
            "worktree_sha256": sha(work_data),
            "bytes": len(work_data),
            "unchanged_from_base_after_line_ending_normalization": True,
        }
    return {
        "schema": "wp84.frozen-r400.source-hashes.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "method": "SHA-256 raw bytes and Git blob IDs; historical inputs compared after CRLF/LF normalization",
        "files": files,
    }


def run_command(label: str, command: list[str], log_path: str) -> dict:
    proc = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    (ROOT / log_path).write_text(proc.stdout, encoding="utf-8", newline="\n")
    if proc.returncode:
        raise RuntimeError(f"{label} failed with {proc.returncode}; see {log_path}")
    return {"command": command, "exit_code": proc.returncode, "log": log_path,
            "log_sha256": sha(proc.stdout.encode("utf-8")), "result": "PASS"}


def run_replays() -> tuple[dict, list[dict]]:
    modes = [
        ("NORMAL", []),
        ("O", ["-O"]),
        ("OO", ["-OO"]),
    ]
    core = {}
    for label, optimization in modes:
        log_path = f"evidence/WP84_FROZEN_R400_CORE_TEST_{label}.log"
        command = [sys.executable, *optimization, "-m", "unittest", *CORE_TESTS, "-v"]
        core[label] = run_command(f"core test suite {label}", command, log_path)
    aux_log = "evidence/WP84_FROZEN_R400_AUX_TEST_NORMAL.log"
    aux_command = [sys.executable, "-m", "unittest", *AUX_TESTS, "-v"]
    aux = run_command("auxiliary source-gate tests", aux_command, aux_log)

    certificate_rows = []
    for label, path_args in CERTIFICATES:
        log_path = f"evidence/WP84_FROZEN_R400_CERT_{label}.log"
        command = [sys.executable, *path_args]
        certificate_rows.append(run_command(label, command, log_path))
    cert_payload = json_bytes({"certificates": certificate_rows})
    (ROOT / "evidence/WP84_FROZEN_R400_CERTIFICATE_REPLAYS.json").write_bytes(cert_payload)
    return {"core_tests": core, "auxiliary_tests": aux}, certificate_rows


def write_all() -> None:
    require_repo_state()
    parent_rows = check_parent_manifests()
    (ROOT / "evidence/WP84_FROZEN_R400_PARENT_MANIFEST_REPLAY.json").write_bytes(
        json_bytes({"parent_manifests": parent_rows,
                    "note": "Artifact and sidecar hashes were checked directly. The historical Schatten verifier's hard-coded branch-name guard is intentionally not changed or required."}))
    test_rows, certificate_rows = run_replays()
    commits = git_bytes("rev-list", "--first-parent", BASE).decode().splitlines()[:14]
    decisions = {
        "frozen_base": BASE,
        "audit_branch": BRANCH,
        "first_parent_chain_head_to_older": commits,
        "ordinary_prime_connected_aggregate": "OPEN",
        "complete_product_frequency_endpoint_selection": "INCOMPLETE",
        "r400_record_budget": "OPEN",
        "conditional_68_820273_percent_route": "NOT_PROMOTED",
        "strict_greater_than_79_percent": "OPEN",
        "riemann_hypothesis": "OPEN",
        "push_merge_publication": "NONE",
    }
    (ROOT / DECISION_PATH).write_bytes(json_bytes(decisions))
    checks = {
        "decisions": decisions,
        "parent_manifest_replays": parent_rows,
        "tests": test_rows,
        "certificate_replays": certificate_rows,
        "scope": "Finite identities/certificates and source-inventory integrity only. No ordinary-prime asymptotic aggregate theorem is claimed.",
    }
    (ROOT / CHECKS_PATH).write_bytes(json_bytes(checks))
    inventory = source_inventory()
    source_payload = json_bytes(inventory)
    (ROOT / SOURCE_HASH_PATH).write_bytes(source_payload)
    artifact_rows = {}
    # Include the six individual certificate logs in the hash manifest.
    artifact_paths = ARTIFACTS + [row["log"] for row in certificate_rows]
    for relative in artifact_paths:
        data = (ROOT / relative).read_bytes()
        artifact_rows[relative] = {"bytes": len(data), "sha256": sha(data)}
    manifest = {
        "schema": "wp84.frozen-r400.sha256-manifest.v1",
        "base_commit": BASE,
        "audit_branch": BRANCH,
        "decisions": {
            "ordinary_prime_connected_aggregate": "OPEN",
            "complete_product_frequency_endpoint_selection": "INCOMPLETE",
            "r400_record_budget": "OPEN",
            "68_820273_percent": "NOT_PROMOTED",
            "strict_gt_79_percent": "OPEN",
            "riemann_hypothesis": "OPEN",
        },
        "source_inventory": {"path": SOURCE_HASH_PATH, "sha256": sha(source_payload),
                             "file_count": len(inventory["files"])},
        "artifacts": artifact_rows,
        "self_hash_excluded": [MANIFEST_PATH, SIDECAR_PATH],
        "claim_boundary": "No open R400 aggregate, percentage, or RH claim is promoted.",
    }
    manifest_payload = json_bytes(manifest)
    (ROOT / MANIFEST_PATH).write_bytes(manifest_payload)
    (ROOT / SIDECAR_PATH).write_text(
        sha(manifest_payload) + "  " + MANIFEST_PATH + "\n", encoding="ascii", newline="\n")
    print(f"PASS base/branch/ancestry: {BASE} on {BRANCH}")
    print(f"PASS parent manifests: {len(parent_rows)}")
    print(f"PASS base-matched source files: {len(inventory['files'])}")
    print(f"PASS test groups/modes: 4 groups, core modes normal/-O/-OO")
    print(f"PASS deterministic certificates: {len(certificate_rows)}")
    print(f"MANIFEST_SHA256 {sha(manifest_payload)}")


def verify() -> None:
    require_repo_state()
    manifest_payload = (ROOT / MANIFEST_PATH).read_bytes()
    manifest = json.loads(manifest_payload)
    sidecar_tokens = (ROOT / SIDECAR_PATH).read_text(encoding="ascii").split()
    if not sidecar_tokens or sidecar_tokens[0] != sha(manifest_payload):
        raise RuntimeError("new manifest sidecar mismatch")
    for relative, record in manifest["artifacts"].items():
        data = (ROOT / relative).read_bytes()
        if record["bytes"] != len(data) or record["sha256"] != sha(data):
            raise RuntimeError(f"new artifact hash mismatch: {relative}")
    source_payload = (ROOT / SOURCE_HASH_PATH).read_bytes()
    if sha(source_payload) != manifest["source_inventory"]["sha256"]:
        raise RuntimeError("source inventory digest mismatch")
    inventory = json.loads(source_payload)
    for relative, record in inventory["files"].items():
        data = (ROOT / relative).read_bytes()
        if record["worktree_sha256"] != sha(data):
            raise RuntimeError(f"source hash mismatch: {relative}")
        if not record["unchanged_from_base_after_line_ending_normalization"]:
            raise RuntimeError(f"base source not preserved: {relative}")
    parents = check_parent_manifests()
    print(f"PASS new manifest/artifacts: {len(manifest['artifacts'])}")
    print(f"PASS base source inventory: {len(inventory['files'])}")
    print(f"PASS predecessor manifests: {len(parents)}")
    print(f"MANIFEST_SHA256 {sidecar_tokens[0]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify() if args.verify else write_all()
