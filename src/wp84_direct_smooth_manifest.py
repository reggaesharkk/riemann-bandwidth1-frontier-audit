"""Build provenance and SHA-256 evidence for the direct smooth audit."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "7f3394c5655238b1e9736f91233d0bcc4c49fd43"
PACKET = Path(r"C:\Users\Asus\Downloads\WP84_SCHATTEN_INDEPENDENT_REFEREE_PACKET_V2_20261103.zip")
SOURCE_PATHS = [
    "notes/WP84_BOUNDED_RESOLVENT_CONSUMER.md",
    "notes/WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER.md",
    "notes/WP84_PHYSICAL_KERNEL_PROPER_POWER_AGGREGATE_AUDIT.md",
    "notes/WP84_R400_SCHATTEN_ABSORPTION_AND_ORDINARY_AGGREGATE_AUDIT.md",
    "notes/WP84_SHARP_CARRIER_GAUGE.md",
    "src/wp84_r400_schatten_absorption_audit.py",
    "tests/test_wp84_r400_schatten_absorption_audit.py",
]
NEW_ARTIFACTS = [
    "notes/WP84_DIRECT_SMOOTH_POWER_ABSORPTION.md",
    "src/wp84_direct_smooth_power_absorption.py",
    "src/wp84_direct_smooth_manifest.py",
    "tests/test_wp84_direct_smooth_power_absorption.py",
    "evidence/WP84_DIRECT_SMOOTH_CHECKER.json",
    "evidence/WP84_DIRECT_SMOOTH_REPLAY_NORMAL.txt",
    "evidence/WP84_DIRECT_SMOOTH_REPLAY_OPTIMIZED.txt",
    "evidence/WP84_DIRECT_SMOOTH_REPLAY_DOUBLE_OPTIMIZED.txt",
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(spec: str) -> bytes:
    return subprocess.run(
        ["git", "show", spec], cwd=ROOT, check=True, stdout=subprocess.PIPE
    ).stdout


def git_text(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, stdout=subprocess.PIPE,
        text=True, encoding="utf-8"
    ).stdout.strip()


def build_source_map() -> dict:
    source_files = []
    for rel in SOURCE_PATHS:
        frozen_data = git_bytes(f"{BASE}:{rel}")
        frozen_blob = git_text("rev-parse", f"{BASE}:{rel}")
        work_path = ROOT / rel
        work_data = work_path.read_bytes()
        normalized_worktree_blob = git_text("hash-object", f"--path={rel}", rel)
        source_files.append({
            "path": rel,
            "git_blob_at_frozen_commit": frozen_blob,
            "sha256_at_frozen_commit": sha256(frozen_data),
            "sha256_current_worktree_raw": sha256(work_data),
            "worktree_normalized_git_blob": normalized_worktree_blob,
            "raw_bytes_equal_to_frozen_blob": frozen_data == work_data,
            "unchanged_from_frozen_commit": frozen_blob == normalized_worktree_blob,
        })
    packet = None
    if PACKET.exists():
        packet_bytes = PACKET.read_bytes()
        packet = {
            "path": str(PACKET),
            "size_bytes": len(packet_bytes),
            "sha256": sha256(packet_bytes),
            "preserved_in_place": True,
        }
    else:
        packet = {
            "path": str(PACKET),
            "size_bytes": 321803,
            "sha256": "1c365afd03ed3b5694bee8c60587831a11c439b31339eaa91643db4a0087f996",
            "preserved_in_place": "previously verified; not currently readable",
        }
    return {
        "frozen_reference_commit": BASE,
        "frozen_tree": git_text("rev-parse", f"{BASE}^{{tree}}"),
        "frozen_parent": git_text("rev-list", "--parents", "-n", "1", BASE).split()[1:],
        "external_referee_packet_v2": packet,
        "mathematical_dependencies": [
            {
                "source": "Alpöge-Furman, arXiv:2608.13637v2, §§2.1-2.3, (2.6)-(2.11), Lemma 2.1",
                "url": "https://arxiv.org/html/2608.13637v2",
                "used_for": "actual smooth taper, a_phi normalization, finite Weil/Gabor matrix, source prime polynomial and exact smooth overlap formula",
                "status": "source hypotheses matched; no fixed chi formula assumed",
            },
            {
                "source": "Montgomery-Vaughan, The Large Sieve, Mathematika 20 (1973), 119-134, Theorem 1",
                "doi": "10.1112/S0025579300004708",
                "url": "https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf",
                "used_for": "separated-point inequality (m + delta^-1) sum |b_j|^2 for m consecutive integers",
                "status": "hypotheses and logarithmic-grid mapping verified in proof note",
            },
            {
                "source": "Elementary Chebyshev bound theta(x) <= 4 log(2) x plus partial summation",
                "used_for": "proper-power absolute coefficient mass and operator norm",
                "status": "explicitly stated and mapped; no prime number theorem input",
            },
        ],
        "frozen_local_source_files": source_files,
        "all_frozen_local_files_unchanged": all(
            x["unchanged_from_frozen_commit"] for x in source_files
        ),
    }


def build_manifest(source_map: dict) -> dict:
    entries = []
    for rel in NEW_ARTIFACTS:
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(f"manifest input missing: {rel}")
        data = path.read_bytes()
        git_text_bytes = data.replace(b"\r\n", b"\n")
        entries.append({
            "path": rel,
            "size_bytes_worktree": len(data),
            "size_bytes_git_text": len(git_text_bytes),
            "sha256_worktree_raw": sha256(data),
            "sha256_git_text_normalized": sha256(git_text_bytes),
        })
    source_map_bytes = json.dumps(source_map, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    dep_rel = "evidence/WP84_DIRECT_SMOOTH_SOURCE_DEPENDENCIES.json"
    (ROOT / dep_rel).write_bytes(source_map_bytes)
    entries.append({
        "path": dep_rel,
        "size_bytes_worktree": len(source_map_bytes),
        "size_bytes_git_text": len(source_map_bytes),
        "sha256_worktree_raw": sha256(source_map_bytes),
        "sha256_git_text_normalized": sha256(source_map_bytes),
    })
    return {
        "audit": "WP84 direct smooth-taper proper-power absorption",
        "frozen_reference_commit": BASE,
        "branch": "codex/wp84-direct-smooth-taper-20261103",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "artifacts": sorted(entries, key=lambda item: item["path"]),
        "manifest_excludes": [
            "this manifest (hash is recorded in the .sha256 sidecar)",
            "the .sha256 sidecar itself",
            "all pre-existing untracked unrelated repository files",
        ],
    }


def main() -> None:
    evidence = ROOT / "evidence"
    evidence.mkdir(exist_ok=True)
    source_map = build_source_map()
    if not source_map["all_frozen_local_files_unchanged"]:
        raise SystemExit("a frozen local source differs from its reference blob")
    manifest = build_manifest(source_map)
    manifest_path = evidence / "WP84_DIRECT_SMOOTH_SHA256_MANIFEST.json"
    payload = json.dumps(manifest, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    manifest_path.write_bytes(payload)
    sidecar = evidence / "WP84_DIRECT_SMOOTH_SHA256_MANIFEST.sha256"
    sidecar.write_text(f"{sha256(payload)}  {manifest_path.name}\n", encoding="ascii")
    print(json.dumps({
        "source_map": "evidence/WP84_DIRECT_SMOOTH_SOURCE_DEPENDENCIES.json",
        "manifest": "evidence/WP84_DIRECT_SMOOTH_SHA256_MANIFEST.json",
        "manifest_sha256": sha256(payload),
        "frozen_local_sources_unchanged": source_map["all_frozen_local_files_unchanged"],
        "packet_v2_sha256": source_map["external_referee_packet_v2"]["sha256"],
        "packet_v2_size_bytes": source_map["external_referee_packet_v2"]["size_bytes"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
