#!/usr/bin/env python3
"""Authenticate and exact-reconstruct terminal 20 within the node-61 prefix.

This is a bounded prefix parser, not a full-tree certificate replay or search.
It validates every stream/catalog hash before using source data.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import struct
import sys
import zipfile
from fractions import Fraction as F
from pathlib import Path

EXPECTED_ZIP = "3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5"
TARGET_NODES = {61, 62, 63, 64, 65, 66, 67}


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def load_replay(path: Path):
    spec = importlib.util.spec_from_file_location("a1294_v2_replay_siblings", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load frozen replay code at {path}")
    import sys as _sys
    module = importlib.util.module_from_spec(spec)
    _sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def qs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: extract_siblings.py <V2-package-root> <V2-package.zip>")
    root, zip_path = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if sha_path(zip_path) != EXPECTED_ZIP:
        raise SystemExit("frozen V2 ZIP hash mismatch")

    cert, data = root / "certificate", root / "data"
    manifest = json.loads((cert / "manifest.json").read_text(encoding="utf-8"))
    stream_paths = {
        "topology": cert / "topology-u8.bin",
        "kinds": cert / "terminal-kinds-u8.bin",
        "anchors": cert / "anchors-u16le.bin",
    }
    catalog_paths = {
        "stable": data / "macro-data-exact.json",
        "v1": data / "refinement-catalog-v1-exact.json",
        "v3": data / "refinement-catalog-v3.json",
    }
    for name, path in stream_paths.items():
        if sha_path(path) != manifest["stream_sha256"][name]:
            raise SystemExit(f"stream hash mismatch: {name}")
    for name, path in catalog_paths.items():
        if sha_path(path) != manifest["input_sha256"][name]:
            raise SystemExit(f"catalog hash mismatch: {name}")

    # Check every file listed in the ZIP's own package manifest as well.
    with zipfile.ZipFile(zip_path) as zf:
        if zf.testzip() is not None:
            raise SystemExit("V2 package CRC failure")
        prefix = "A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/"
        package_manifest = json.loads(zf.read(prefix + "PACKAGE_MANIFEST.json"))
        for rel, entry in package_manifest["files"].items():
            payload = zf.read(prefix + rel)
            if len(payload) != entry["bytes"] or sha_bytes(payload) != entry["sha256"]:
                raise SystemExit(f"package manifest mismatch: {rel}")

    sys.dont_write_bytecode = True
    replay = load_replay(root / "replay_a1294_source_free.py")
    topology = stream_paths["topology"].read_bytes()
    kinds = stream_paths["kinds"].read_bytes()
    anchors = stream_paths["anchors"].read_bytes()
    pending = [([(F(0), F(60)) for _ in range(5)], [])]
    terminal_index = 0
    nodes = {}
    for node_index, token in enumerate(topology):
        if node_index > max(TARGET_NODES):
            break
        if not pending:
            raise SystemExit(f"empty DFS stack at node {node_index}")
        box, path = pending.pop()
        if node_index in TARGET_NODES:
            nodes[node_index] = {"box": box, "path": list(path), "token": token,
                                 "terminal_index": terminal_index if token == 0 else None}
        if token == 0:
            terminal_index += 1
            continue
        if not 1 <= token <= 5:
            raise SystemExit(f"invalid split token {token} at node {node_index}")
        scaled_widths = [(box[i][1] - box[i][0]) * replay.WEIGHTS[i] for i in range(5)]
        selected_axis = max(range(5), key=scaled_widths.__getitem__)
        if token != selected_axis + 1:
            raise SystemExit(f"weighted split mismatch at node {node_index}")
        lo, hi = box[selected_axis]
        mid = (lo + hi) / 2
        left_box, right_box = list(box), list(box)
        left_box[selected_axis] = (lo, mid)
        right_box[selected_axis] = (mid, hi)
        pending.append((right_box, path + [(selected_axis, "R")]))
        pending.append((left_box, path + [(selected_axis, "L")]))

    if set(nodes) != TARGET_NODES:
        raise SystemExit("target nodes not found in bounded prefix")
    parent, left, right = nodes[61], nodes[62], nodes[67]
    if list(topology[61:68]) != [2,0,4,0,1,0,0]:
        raise SystemExit("five-node topology mismatch")
    if kinds[20:24] != bytes((1,1,1,1)):
        raise SystemExit("quadratic kinds mismatch")
    if left["terminal_index"] != 20 or right["terminal_index"] != 23:
        raise SystemExit("terminal indices")
    if left["path"] != parent["path"]+[(1,"L")] or nodes[63]["path"] != parent["path"]+[(1,"R")]:
        raise SystemExit("node63 child paths")
    anchor_codes = {}
    for label, leaf in (("left", left), ("right", right)):
        ti = leaf["terminal_index"]
        codes = struct.unpack_from("<5H", anchors, sum(k == 1 for k in kinds[:ti]) * 10)
        if any(code > replay.ANCHOR_DEN for code in codes):
            raise SystemExit(f"anchor code out of range for {label} child")
        anchor_codes[label] = codes

    catalog = replay.ExactCatalog(
        catalog_paths["stable"], catalog_paths["v1"], catalog_paths["v3"],
        replay.Q(manifest["A"]), replay.Q(manifest["B"]),
    )

    raw_catalogs = [json.loads(path.read_text(encoding="utf-8"))["pieces"]
                    for path in catalog_paths.values()]

    def source_piece(index):
        if index < 56:
            return raw_catalogs[0][index], f"macroPiece{index}"
        if index < 272:
            return raw_catalogs[1][index - 56], f"refinementPiece{index - 56}"
        return raw_catalogs[2][index - 272], f"refinement2Piece{index - 272}"

    def segment_rows(lo, hi):
        clipped_hi = min(hi, catalog.cutoff)
        if clipped_hi <= lo:
            return []
        boundaries = {lo, clipped_hi}
        first = catalog.stable_owner(lo)
        last = catalog.stable_owner(min(clipped_hi, F(59)))
        for owner in range(max(0, first - 1), min(55, last + 1) + 1):
            boundaries.update(x for x in catalog.group_boundaries[owner] if lo < x < clipped_hi)
        boundaries.update(x for x in catalog.group_boundaries[-1] if lo < x < clipped_hi)
        ordered = sorted(boundaries)
        rows = []
        for seg_lo, seg_hi in zip(ordered, ordered[1:]):
            piece = catalog.strongest_full_cover(seg_lo, seg_hi)
            if piece is None:
                candidates = [p for group in catalog.groups.values() for p in group
                              if p.lo <= seg_lo and seg_hi <= p.hi]
                if not candidates:
                    raise SystemExit(f"catalog coverage gap [{seg_lo},{seg_hi}]")
                piece = max(candidates,
                            key=lambda p: (replay.interval_infimum(p, seg_lo, seg_hi), -p.idx))
            raw, name = source_piece(piece.idx)
            rows.append({
                "segment": [qs(seg_lo), qs(seg_hi)],
                "catalog_index_zero_based": piece.idx,
                "declaration": name,
                "owner_index": piece.owner,
                "source_item": raw,
                "model_infimum": qs(replay.interval_infimum(piece, seg_lo, seg_hi)),
            })
        return rows

    def model_terms(box):
        out = []
        for pair_index, (gap_lo, gap_hi) in enumerate(replay.PARTIALS):
            d_lo = sum((box[i][0] for i in range(gap_lo, gap_hi + 1)), F(0))
            d_hi = sum((box[i][1] for i in range(gap_lo, gap_hi + 1)), F(0))
            clipped_hi = min(d_hi, catalog.cutoff)
            direct = catalog.strongest_full_cover(d_lo, clipped_hi) if d_lo <= clipped_hi else None
            use_segmented = direct is None
            if direct is not None and direct.idx < 56 and catalog.groups.get(direct.owner):
                segmented = catalog.segmented_scalar_lower(d_lo, d_hi)
                direct_lower = replay.interval_infimum(direct, d_lo, clipped_hi)
                use_segmented = segmented > direct_lower
            if use_segmented:
                scalar = catalog.segmented_scalar_lower(d_lo, d_hi)
                term = {"base": qs(scalar), "weight": "0", "offset": "0", "kind": "segmented_constant",
                        "direct_catalog_index": None,
                        "segments": segment_rows(d_lo, d_hi)}
            else:
                term = {"base": qs(direct.floor), "weight": qs(direct.curvature),
                        "offset": qs(-direct.center), "kind": "direct_piece",
                        "direct_catalog_index": direct.idx, "owner_index": direct.owner,
                        "piece_interval": [qs(direct.lo), qs(direct.hi)],
                        "piece_center": qs(direct.center), "piece_floor": qs(direct.floor),
                        "piece_curvature": qs(direct.curvature),
                        "segments": []}
            term.update({"pair_index_zero_based": pair_index,
                         "distance_interval": [qs(d_lo), qs(d_hi)],
                         "gap_index_range_inclusive": [gap_lo, gap_hi]})
            out.append(term)
        return out

    leaves = {}
    A, B = replay.Q(manifest["A"]), replay.Q(manifest["B"])
    for label, leaf in (("left", left), ("right", right)):
        ti = leaf["terminal_index"]
        box = leaf["box"]
        codes = anchor_codes[label]
        point = [lo + F(code, replay.ANCHOR_DEN) * (hi - lo)
                 for code, (lo, hi) in zip(codes, box)]
        term_data = model_terms(box)
        tangent = catalog.tangent_lower_from_codes(box, codes)
        leaves[label] = {
            "topology_node_zero_based": 62 if label == "left" else 67,
            "terminal_index_zero_based": ti,
            "terminal_kind_byte": kinds[ti],
            "path_axes_zero_based": [axis for axis, _ in leaf["path"]],
            "path_sides": [side for _, side in leaf["path"]],
            "topology_prefix_through_node": list(topology[:(62 if label == "left" else 67) + 1]),
            "box_exact": [[qs(lo), qs(hi)] for lo, hi in box],
            "anchor_stream_byte_offset": sum(k == 1 for k in kinds[:ti])*10,
            "anchor_codes_u16le": list(codes),
            "anchor_denominator": replay.ANCHOR_DEN,
            "anchor_coordinates_exact": [qs(x) for x in point],
            "A": qs(A), "B": qs(B),
            "rank_tangent_lower": qs(tangent),
            "exact_margin": qs(tangent - A),
            "fifteen_models": term_data,
        }
    parent_data = {
        "topology_node_zero_based": 61,
        "token": parent["token"],
        "split_axis_zero_based": parent["token"] - 1,
        "path_axes_zero_based": [axis for axis, _ in parent["path"]],
        "path_sides": [side for _, side in parent["path"]],
        "box_exact": [[qs(lo), qs(hi)] for lo, hi in parent["box"]],
        "left_child_node": 62,
        "right_child_node": 63,
    }
    result = {
        "status": "NODE61_BOUNDED_TERMINAL20_RECONSTRUCTION_PASS",
        "scope": "bounded DFS reconstruction through topology node 67; no full-tree replay or search",
        "v2_zip_sha256": EXPECTED_ZIP,
        "source_stream_sha256": {name: sha_path(path) for name, path in stream_paths.items()},
        "source_input_sha256": {name: sha_path(path) for name, path in catalog_paths.items()},
        "weighted_split_checks_in_prefix": sum(t != 0 for t in topology[:68]),
        "parent": parent_data,
        "children": leaves,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
