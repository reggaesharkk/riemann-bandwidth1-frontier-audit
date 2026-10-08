"""Independent fail-closed replay for the fifth-block determinant audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(data: dict, verify_disk: bool = True) -> list[str]:
    errors: list[str] = []
    if data.get("status") != "BLOCKED_ON_MISSING_SOURCE_MATRIX_DATA":
        errors.append("status must preserve the missing-source-data boundary")
    basis = data.get("frozen_basis", {})
    if basis.get("candidate_coordinates") != 73 or basis.get("J") != 9:
        errors.append("frozen 73 -> 9 basis changed")
    if basis.get("master_moments") != [f"S_{j}" for j in range(2, 11)]:
        errors.append("master moment list changed")
    if data.get("R") != 6000:
        errors.append("R changed")
    if data.get("global_K") is not None:
        errors.append("unsupported global K claimed")
    if data.get("new_fifth_analytic_rank") != 0:
        errors.append("unsupported rank promotion claimed")
    if data.get("existing_fifth_rank_bounds") != [38, 72]:
        errors.append("existing rank bounds changed")
    expected = {
        "B6": (6, 5, 7),
        "B8a": (8, 7, 7),
        "B16": (16, 15, 9),
        "B8b": (8, 7, 7),
    }
    blocks = {b.get("name"): b for b in data.get("blocks", [])}
    if set(blocks) != set(expected):
        errors.append("block set changed")
    for name, (m, deficit, n_moments) in expected.items():
        b = blocks.get(name, {})
        if b.get("size") != m or b.get("formal_first_possible_deficit") != deficit:
            errors.append(f"{name}: section size/first possible deficit changed")
        if b.get("candidate_moment_count") != n_moments:
            errors.append(f"{name}: moment count changed")
        if b.get("determinant_visible_K") is not None:
            errors.append(f"{name}: unsupported K claimed")
        if b.get("first_nonzero_deficit") is not None or b.get("correction_span_rank") is not None:
            errors.append(f"{name}: unsupported exact coefficient/rank claimed")
        if b.get("visible_only_minor") is not None or b.get("promotion") != 0:
            errors.append(f"{name}: unsupported visible minor/promotion claimed")
    if verify_disk:
        for rel, digest in data.get("source_sha256", {}).items():
            path = ROOT / rel
            if not path.is_file():
                errors.append(f"missing pinned source: {rel}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"source hash mismatch: {rel}")
    return errors


def main() -> None:
    path = ROOT / "notes/WP84_DETERMINANT_VISIBLE_HIDDEN_PRIME_COMPRESSION.json"
    data = json.loads(path.read_text())
    errors = validate(data)
    if errors:
        raise SystemExit("FAIL: " + "; ".join(errors))
    print("PASS independent replay: exact claims match pinned inputs; unsupported K/rank/minors rejected")


if __name__ == "__main__":
    main()
