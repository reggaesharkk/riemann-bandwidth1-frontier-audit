#!/usr/bin/env python3
"""Build the packet's source/evidence SHA-256 inventory from recovered bytes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    evidence = root / "evidence"
    files = []
    for path in sorted(p for p in evidence.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        origin = "recovered local Downloads evidence"
        if rel.startswith("evidence/screenshots/"):
            origin = "user-supplied screenshot copied from OneDrive Pictures/Screenshots"
        elif rel.startswith("evidence/github/"):
            origin = "read-only GitHub connector metadata recorded in this audit"
        elif rel.startswith("evidence/drive/"):
            origin = "read-only Google Drive connector inventory recorded in this audit"
        elif rel.startswith("evidence/git/"):
            origin = "read-only local Git history observations recorded in this audit"
        files.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha(path), "origin": origin})

    notable = {
        "original_github_artifact_claim": {
            "artifact_id": 11286675906,
            "reported_sha256": "11c1ab1820039284f60e492fe609f6a497175284acdd0c3c53d6ab62b8b1cd19",
            "recovered": False,
            "reason": "expired; listing empty and direct download returned 404"
        },
        "local_v2_replay_zip": {
            "path": "evidence/local/C_Users_Asus_Downloads/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip",
            "sha256": sha(evidence / "local" / "C_Users_Asus_Downloads" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"),
            "bytes": (evidence / "local" / "C_Users_Asus_Downloads" / "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip").stat().st_size,
            "is_original_github_artifact": False
        },
        "catalog_inputs": {
            "stable": "961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b",
            "v1": None,
            "v3": None
        },
        "source_free_v2_replay": {
            "A": "647/50000",
            "B": "1094977/5000000000",
            "status": "PASS",
            "visited_nodes": 13454121,
            "leaves": 6727061,
            "quadratic_leaves": 6725258,
            "tail_leaves": 1803,
            "elapsed_seconds": 18897.781,
            "stream_sha256": {
                "anchors": None,
                "kinds": None,
                "topology": None
            }
        }
    }
    # Derive and validate the copied catalog hashes rather than relying on literals.
    inv_by_path = {item["path"]: item for item in files}
    for key, relative in (
        ("stable", "evidence/local/C_Users_Asus_Downloads/A1294_LOCAL_BENCHMARK/A1294_LOCAL_BENCHMARK_PACKAGE/data/macro-data-exact.json"),
        ("v1", "evidence/local/C_Users_Asus_Downloads/A1294_LOCAL_BENCHMARK/A1294_LOCAL_BENCHMARK_PACKAGE/data/refinement-catalog-v1-exact.json"),
        ("v3", "evidence/local/C_Users_Asus_Downloads/A1294_LOCAL_BENCHMARK/A1294_LOCAL_BENCHMARK_PACKAGE/data/refinement-catalog-v3.json"),
    ):
        notable["catalog_inputs"][key] = inv_by_path[relative]["sha256"]
    stream_paths = {
        "anchors": "evidence/local/C_Users_Asus_Downloads/A1294_SOURCE_FREE_REPLAY_V2/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/anchors-u16le.bin",
        "kinds": "evidence/local/C_Users_Asus_Downloads/A1294_SOURCE_FREE_REPLAY_V2/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/terminal-kinds-u8.bin",
        "topology": "evidence/local/C_Users_Asus_Downloads/A1294_SOURCE_FREE_REPLAY_V2/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/topology-u8.bin",
    }
    for key, relative in stream_paths.items():
        notable["source_free_v2_replay"]["stream_sha256"][key] = inv_by_path[relative]["sha256"]

    result = {
        "schema": "a1294-a1300-forensic-inventory-v1",
        "generated_from": "the byte-preserved evidence tree in this packet",
        "file_count": len(files),
        "evidence_bytes": sum(item["bytes"] for item in files),
        "files": files,
        "notable_claims_and_hashes": notable,
        "repository_observations": {
            "downloads_clone_head": "908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5",
            "downloads_clone_branch": "research/frontier-7962-hostile-audit-v0.1",
            "second_worktree_head": "e61f116ac3eb4b07bf1df3e91960d84a6f730034",
            "current_audit_worktree_head": "eb36159ee7e57053fcae3de025fe4dac539435ab"
        },
        "limits": [
            "The expired GitHub Actions artifact bytes were not recovered; its reported SHA is metadata, not a locally recomputed source hash.",
            "File hashes in files[] are recomputed from packet evidence bytes.",
            "This inventory contains no credentials or authorization headers."
        ]
    }
    output = root / "SOURCE_AND_EXECUTION_HASH_INVENTORY.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output.relative_to(root)} with {len(files)} evidence files")


if __name__ == "__main__":
    main()
