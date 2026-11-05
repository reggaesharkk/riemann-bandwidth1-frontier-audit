#!/usr/bin/env python3
"""Reconstruct and ledger the first actual quadratic terminal in the frozen V2.

Reads only a bounded first-terminal prefix, verifies its weighted split axes,
and reuses the frozen source-free exact catalog implementation to report each
of the fifteen scalar lower-model segment selections. It does not run the full
certificate replay or generate anchors.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import struct
import sys
from fractions import Fraction as F
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_replay(path: Path):
    spec = importlib.util.spec_from_file_location("a1294_v2_replay_ledger", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    import sys as _sys
    module = importlib.util.module_from_spec(spec)
    _sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def qstr(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: extract_first_quadratic_ledger.py <V2-package-root>")
    root = Path(sys.argv[1]).resolve()
    cert, data = root / "certificate", root / "data"
    manifest = json.loads((cert / "manifest.json").read_text(encoding="utf-8"))
    replay = load_replay(root / "replay_a1294_source_free.py")
    input_paths = {
        "stable": data / "macro-data-exact.json",
        "v1": data / "refinement-catalog-v1-exact.json",
        "v3": data / "refinement-catalog-v3.json",
    }
    stream_paths = {
        "topology": cert / "topology-u8.bin",
        "kinds": cert / "terminal-kinds-u8.bin",
        "anchors": cert / "anchors-u16le.bin",
    }
    for name, path in input_paths.items():
        if sha(path) != manifest["input_sha256"][name]:
            raise SystemExit(f"source catalog hash mismatch: {name}")
    for name, path in stream_paths.items():
        if sha(path) != manifest["stream_sha256"][name]:
            raise SystemExit(f"source stream hash mismatch: {name}")

    topology = stream_paths["topology"].read_bytes()
    kinds = stream_paths["kinds"].read_bytes()
    anchors = stream_paths["anchors"].read_bytes()
    node = topology.find(b"\x00")
    if node < 0 or node >= len(topology):
        raise SystemExit("no first terminal in topology")
    if not kinds or kinds[0] != 1:
        raise SystemExit("first terminal is not quadratic")

    box = [(F(0), F(60)) for _ in range(5)]
    pending = [box]
    path = []
    for node_index, token in enumerate(topology[:node]):
        if token == 0 or not pending:
            raise SystemExit(f"invalid prefix at node {node_index}")
        current = pending.pop()
        widths = [(current[i][1] - current[i][0]) * replay.WEIGHTS[i] for i in range(5)]
        axis = max(range(5), key=widths.__getitem__)
        if token != axis + 1:
            raise SystemExit(f"weighted split mismatch at source node {node_index}")
        lo, hi = current[axis]
        midpoint = (lo + hi) / 2
        left, right = list(current), list(current)
        left[axis] = (lo, midpoint)
        right[axis] = (midpoint, hi)
        pending.extend((right, left))
        path.append((axis, "L"))
    if not pending or topology[node] != 0:
        raise SystemExit("invalid first leaf pending stack")
    exact_box = tuple(pending[-1])
    codes = struct.unpack_from("<5H", anchors, 0)
    if any(code > replay.ANCHOR_DEN for code in codes):
        raise SystemExit("anchor code outside declared denominator")

    catalog = replay.ExactCatalog(
        input_paths["stable"], input_paths["v1"], input_paths["v3"],
        replay.Q(manifest["A"]), replay.Q(manifest["B"]),
    )
    raw_catalogs = [
        json.loads(path.read_text(encoding="utf-8"))["pieces"]
        for path in input_paths.values()
    ]

    def source_piece(index: int):
        if index < 56:
            return raw_catalogs[0][index], f"macroPiece{index}"
        if index < 272:
            j = index - 56
            return raw_catalogs[1][j], f"refinementPiece{j}"
        j = index - 272
        return raw_catalogs[2][j], f"refinement2Piece{j}"

    def segments(lo: F, hi: F):
        clipped_hi = min(hi, catalog.cutoff)
        boundaries = {lo, clipped_hi}
        first = catalog.stable_owner(lo)
        last = catalog.stable_owner(min(clipped_hi, F(59)))
        for owner in range(max(0, first - 1), min(55, last + 1) + 1):
            boundaries.update(x for x in catalog.group_boundaries[owner] if lo < x < clipped_hi)
        boundaries.update(x for x in catalog.group_boundaries[-1] if lo < x < clipped_hi)
        ordered = sorted(boundaries)
        rows = []
        for left, right in zip(ordered, ordered[1:]):
            piece = catalog.strongest_full_cover(left, right)
            if piece is None:
                refinements = [
                    candidate for group in catalog.groups.values() for candidate in group
                    if candidate.lo <= left and right <= candidate.hi
                ]
                if not refinements:
                    raise SystemExit(f"catalog coverage gap [{left},{right}]")
                piece = max(
                    refinements,
                    key=lambda candidate: (replay.interval_infimum(candidate, left, right), -candidate.idx),
                )
            raw, lean_name = source_piece(piece.idx)
            lower = replay.interval_infimum(piece, left, right)
            rows.append({
                "segment": [qstr(left), qstr(right)],
                "catalog_index_zero_based": piece.idx,
                "lean_declaration": lean_name,
                "owner_index": piece.owner,
                "source_item": raw,
                "source_item_sha256_canonical_json": hashlib.sha256(
                    json.dumps(raw, sort_keys=True, separators=(",", ":")).encode()
                ).hexdigest(),
                "model_infimum_on_segment": qstr(lower),
                "active_minimizer": False,
            })
        return rows

    terms = []
    for pair_index, (left_gap, right_gap) in enumerate(replay.PARTIALS):
        lo = sum((exact_box[k][0] for k in range(left_gap, right_gap + 1)), F(0))
        hi = sum((exact_box[k][1] for k in range(left_gap, right_gap + 1)), F(0))
        piece = catalog.strongest_full_cover(lo, min(hi, catalog.cutoff)) if lo <= catalog.cutoff else None
        segment_rows = segments(lo, hi)
        scalar = min((F(row["model_infimum_on_segment"]) for row in segment_rows), default=F(0))
        for row in segment_rows:
            row["active_minimizer"] = F(row["model_infimum_on_segment"]) == scalar
        segmented = catalog.segmented_scalar_lower(lo, hi)
        if segmented != scalar:
            raise SystemExit(f"segmented lower mismatch at pair {pair_index}")
        if piece is not None:
            direct = replay.interval_infimum(piece, lo, min(hi, catalog.cutoff))
            if piece.idx < 56 and catalog.groups.get(piece.owner) and scalar > direct:
                mode, selected = "segmented_override", scalar
            else:
                mode, selected = "direct", direct
        else:
            mode, selected = "segmented", scalar
        if mode != "segmented":
            raise SystemExit(f"expected a segmented source model for pair {pair_index}, got {mode}")
        terms.append({
            "pair_index_zero_based": pair_index,
            "gap_indices_zero_based_inclusive": [left_gap, right_gap],
            "distance_interval": [qstr(lo), qstr(hi)],
            "effective_selected_constant_lower_model": qstr(selected),
            "selection_mode": mode,
            "direct_full_cover_piece": None if piece is None else piece.idx,
            "catalog_segments": segment_rows,
        })

    tangent = catalog.tangent_lower_from_codes(exact_box, codes)
    A, B = catalog.A, catalog.B
    report = {
        "status": "FIRST_QUADRATIC_SOURCE_LEAF_LEDGER_PASS",
        "scope": "source first-terminal prefix plus exact fifteen-term scalar-envelope reconstruction; not full certificate replay",
        "source_node_index_zero_based": node,
        "source_leaf_index_zero_based": 0,
        "source_terminal_kind": "quadratic",
        "source_topology_prefix_tokens": list(topology[:node + 1]),
        "root_path_axis_zero_based": [axis for axis, _side in path],
        "root_path_sides": [side for _axis, side in path],
        "weighted_split_checks": len(path),
        "source_box_exact": [[qstr(lo), qstr(hi)] for lo, hi in exact_box],
        "anchor_stream_byte_offset": 0,
        "anchor_codes_u16le": list(codes),
        "anchor_denominator": replay.ANCHOR_DEN,
        "anchor_coordinates_exact": [
            qstr(lo + F(code, replay.ANCHOR_DEN) * (hi - lo))
            for code, (lo, hi) in zip(codes, exact_box)
        ],
        "A": qstr(A),
        "B": qstr(B),
        "rank_tangent_lower": qstr(tangent),
        "exact_positive_margin": qstr(tangent - A),
        "fifteen_models": terms,
        "source_stream_sha256": {name: sha(path) for name, path in stream_paths.items()},
        "source_input_sha256": {name: sha(path) for name, path in input_paths.items()},
    }
    if len(terms) != 15 or sum(F(t["effective_selected_constant_lower_model"]) for t in terms) != tangent:
        raise SystemExit("fifteen-term constant model does not reproduce the exact tangent")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
