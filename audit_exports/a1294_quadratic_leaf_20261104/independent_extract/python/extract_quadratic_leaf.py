#!/usr/bin/env python3
"""Targeted prefix extraction of an authentic, directly modeled V2 quadratic leaf.

This is not a certificate replay or optimization search. It scans a bounded
preorder prefix, verifies each split against the frozen weighted-midpoint rule,
and asks the frozen exact catalog replay which source piece is selected for
each of the fifteen distances. A candidate is emitted only when all fifteen
source selections are single, full-cover catalog pieces and the exact anchor
tangent margin exceeds the requested threshold.
"""
from __future__ import annotations

import argparse
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
    spec = importlib.util.spec_from_file_location("a1294_v2_replay_module", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load replay source: {path}")
    import sys as _sys
    module = importlib.util.module_from_spec(spec)
    _sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def json_fraction(x: F) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("package_root", type=Path)
    ap.add_argument("--max-nodes", type=int, default=250_000)
    ap.add_argument("--min-margin", default="1/1000000")
    args = ap.parse_args()
    root = args.package_root.resolve()
    cert, data = root / "certificate", root / "data"
    manifest = json.loads((cert / "manifest.json").read_text(encoding="utf-8"))
    replay = load_replay(root / "replay_a1294_source_free.py")
    input_paths = {
        "stable": data / "macro-data-exact.json",
        "v1": data / "refinement-catalog-v1-exact.json",
        "v3": data / "refinement-catalog-v3.json",
    }
    for name, path in input_paths.items():
        if sha(path) != manifest["input_sha256"][name]:
            raise SystemExit(f"input hash mismatch: {name}")
    stream_paths = {
        "topology": cert / "topology-u8.bin",
        "kinds": cert / "terminal-kinds-u8.bin",
        "anchors": cert / "anchors-u16le.bin",
    }
    for name, path in stream_paths.items():
        if sha(path) != manifest["stream_sha256"][name]:
            raise SystemExit(f"stream hash mismatch: {name}")

    topology = stream_paths["topology"].read_bytes()
    kinds = stream_paths["kinds"].read_bytes()
    anchors = stream_paths["anchors"].read_bytes()
    catalog = replay.ExactCatalog(
        input_paths["stable"], input_paths["v1"], input_paths["v3"],
        replay.Q(manifest["A"]), replay.Q(manifest["B"]),
    )
    raw_catalogs = [
        json.loads(path.read_text(encoding="utf-8"))["pieces"]
        for path in input_paths.values()
    ]

    def source_item(index: int):
        if index < 56:
            return raw_catalogs[0][index], f"macroPiece{index}"
        if index < 272:
            j = index - 56
            return raw_catalogs[1][j], f"refinementPiece{j}"
        j = index - 272
        return raw_catalogs[2][j], f"refinement2Piece{j}"

    def selections(box):
        out = []
        for pair_index, (left, right) in enumerate(replay.PARTIALS):
            lo = sum((box[k][0] for k in range(left, right + 1)), F(0))
            hi = sum((box[k][1] for k in range(left, right + 1)), F(0))
            clipped_hi = min(hi, catalog.cutoff)
            piece = catalog.strongest_full_cover(lo, clipped_hi) if lo <= clipped_hi else None
            if piece is None:
                return None
            if piece.idx < 56 and catalog.groups.get(piece.owner):
                segmented = catalog.segmented_scalar_lower(lo, hi)
                if segmented > replay.interval_infimum(piece, lo, clipped_hi):
                    return None
            if piece.lo > lo or piece.hi < hi:
                return None
            item, lean_name = source_item(piece.idx)
            out.append({
                "pair_index_zero_based": pair_index,
                "partial_gap_indices_zero_based_inclusive": [left, right],
                "distance_interval": [json_fraction(lo), json_fraction(hi)],
                "catalog_index_zero_based": piece.idx,
                "lean_declaration": lean_name,
                "stable_owner_index": piece.owner,
                "source_catalog_item": item,
            })
        return out

    scale = 1 << 128
    root_box = tuple((F(0), F(60)) for _ in range(5))
    stack = [(root_box, [])]
    node_cursor = kind_cursor = anchor_cursor = 0
    quadratic_seen = candidates = 0
    threshold = F(args.min_margin)

    while stack and node_cursor < args.max_nodes:
        box, path = stack.pop()
        if node_cursor >= len(topology):
            raise SystemExit("topology ended before stack")
        node = node_cursor
        token = topology[node_cursor]
        node_cursor += 1
        if token:
            axis, lower, upper = replay.split_box(box)
            if token != axis + 1:
                raise SystemExit(f"weighted split mismatch at node {node}")
            stack.append((upper, path + [(axis, "R")]))
            stack.append((lower, path + [(axis, "L")]))
            continue

        if kind_cursor >= len(kinds):
            raise SystemExit("terminal-kind stream ended early")
        kind = kinds[kind_cursor]
        leaf_index = kind_cursor
        kind_cursor += 1
        if kind == 0:
            continue
        if kind != 1:
            raise SystemExit(f"invalid terminal kind {kind} at leaf {leaf_index}")
        if anchor_cursor + 10 > len(anchors):
            raise SystemExit("anchor stream ended early")
        anchor_offset = anchor_cursor
        codes = struct.unpack_from("<5H", anchors, anchor_cursor)
        anchor_cursor += 10
        if any(code > replay.ANCHOR_DEN for code in codes):
            raise SystemExit(f"anchor code out of range at leaf {leaf_index}")
        quadratic_seen += 1
        margin = catalog.tangent_lower_from_codes(box, codes) - catalog.A
        if margin < 0:
            raise SystemExit(f"negative source tangent margin at leaf {leaf_index}")
        if margin < threshold:
            continue
        selected = selections(box)
        if selected is None:
            continue
        candidates += 1
        payload = {
            "status": "AUTHENTIC_QUADRATIC_LEAF_EXTRACTED",
            "scope": "bounded source preorder prefix; no quadratic optimization or full-tree replay",
            "source_node_index_zero_based": node,
            "source_leaf_index_zero_based": leaf_index,
            "source_terminal_kind": "quadratic",
            "anchor_stream_byte_offset": anchor_offset,
            "anchor_codes_u16le": list(codes),
            "anchor_denominator": replay.ANCHOR_DEN,
            "source_path_axis_zero_based": [axis for axis, _side in path],
            "source_path_sides": [side for _axis, side in path],
            "source_box_exact": [[json_fraction(lo), json_fraction(hi)] for lo, hi in box],
            "A": json_fraction(catalog.A),
            "B": json_fraction(catalog.B),
            "exact_tangent_margin": json_fraction(margin),
            "fifteen_source_selections": selected,
            "source_stream_sha256": {name: sha(path) for name, path in stream_paths.items()},
            "source_input_sha256": {name: sha(path) for name, path in input_paths.items()},
            "prefix_scan_nodes": node_cursor,
            "prefix_scan_quadratic_terminals": quadratic_seen,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    print(json.dumps({
        "status": "NO_DIRECT_MODEL_CANDIDATE_IN_PREFIX",
        "nodes_scanned": node_cursor,
        "quadratic_terminals_scanned": quadratic_seen,
        "tangent_threshold": json_fraction(threshold),
        "stack_pending": len(stack),
    }, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
