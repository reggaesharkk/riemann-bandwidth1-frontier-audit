#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, os, struct, time
from array import array
from fractions import Fraction as F
from pathlib import Path

from a1294_seam_pilot import Checker, WEIGHTS, q

ANCHOR_DEN = 16384

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def atomic_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".new")
    tmp.write_bytes(data)
    os.replace(tmp, path)

def atomic_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".new")
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)

def proposal_codes(matrix, linear, box):
    mf = [[float(value) for value in row] for row in matrix]
    lf = [float(value) for value in linear]
    lo = [float(bounds[0]) for bounds in box]
    hi = [float(bounds[1]) for bounds in box]
    point = [(left + right) / 2 for left, right in zip(lo, hi)]
    for _ in range(12):
        for row in range(5):
            diagonal = mf[row][row]
            if diagonal > 0:
                off = sum(mf[row][column] * point[column]
                          for column in range(5) if column != row)
                value = -(lf[row] + 2 * off) / (2 * diagonal)
                point[row] = min(max(value, lo[row]), hi[row])
            else:
                point[row] = lo[row] if lf[row] >= 0 else hi[row]

    codes, exact = [], []
    for value, (left, right) in zip(point, box):
        if left == right:
            code = 0
        else:
            width = float(right - left)
            rel = 0.5 if width == 0.0 else (value - float(left)) / width
            code = round(max(0.0, min(1.0, rel)) * ANCHOR_DEN)
        codes.append(code)
        exact.append(left + F(code, ANCHOR_DEN) * (right - left))
    return codes, exact

def lower_with_anchor(checker: Checker, box):
    matrix, linear, constant = checker.quadratic_data(box)
    codes, point = proposal_codes(matrix, linear, box)
    lower = checker.tangent(matrix, linear, constant, box, point)
    return lower, codes

def split_box(box):
    weighted = [(hi - lo) * WEIGHTS[i] for i, (lo, hi) in enumerate(box)]
    axis = max(range(5), key=weighted.__getitem__)
    lo, hi = box[axis]
    midpoint = (lo + hi) / 2
    left, right = list(box), list(box)
    left[axis] = (lo, midpoint)
    right[axis] = (midpoint, hi)
    return axis, tuple(left), tuple(right)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stable", required=True)
    ap.add_argument("--v1", required=True)
    ap.add_argument("--v3", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--a", default="1294/100000")
    ap.add_argument("--b", default="1094977/5000000000")
    ap.add_argument("--limit", type=int, default=60)
    ap.add_argument("--max-nodes", type=int, default=30_000_000)
    ap.add_argument("--max-depth", type=int, default=512)
    ap.add_argument("--progress", type=int, default=250_000)
    args = ap.parse_args()

    A, B = q(args.a), q(args.b)
    checker = Checker(args.stable, args.v1, args.v3, A, B)
    root = tuple((F(0), F(args.limit)) for _ in range(5))
    stack = [(root, 0)]

    topology = bytearray()
    kinds = bytearray()
    anchors = array("H")

    visited = leaves = tail_leaves = quadratic_leaves = max_depth = 0
    smallest_tail = smallest_quad = None
    started = time.monotonic()

    while stack:
        box, depth = stack.pop()
        visited += 1
        max_depth = max(max_depth, depth)
        if visited > args.max_nodes:
            raise ArithmeticError(f"node cap exceeded: visited={visited} pending={len(stack)}")
        if depth > args.max_depth:
            raise ArithmeticError(f"depth cap exceeded: depth={depth} visited={visited}")

        tail_margin = B * sum((bounds[0] for bounds in box), F(0)) - A
        if tail_margin >= 0:
            topology.append(0)
            kinds.append(0)
            leaves += 1
            tail_leaves += 1
            smallest_tail = tail_margin if smallest_tail is None else min(smallest_tail, tail_margin)
            continue

        lower, codes = lower_with_anchor(checker, box)
        margin = lower - A
        if margin >= 0:
            topology.append(0)
            kinds.append(1)
            anchors.extend(codes)
            leaves += 1
            quadratic_leaves += 1
            smallest_quad = margin if smallest_quad is None else min(smallest_quad, margin)
            continue

        axis, left, right = split_box(box)
        topology.append(axis + 1)
        stack.append((right, depth + 1))
        stack.append((left, depth + 1))

        if args.progress and visited % args.progress == 0:
            print(json.dumps({
                "visited": visited, "pending": len(stack), "leaves": leaves,
                "maximum_depth": max_depth, "elapsed_seconds": time.monotonic() - started
            }), flush=True)

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    atomic_bytes(out / "topology-u8.bin", bytes(topology))
    atomic_bytes(out / "terminal-kinds-u8.bin", bytes(kinds))
    anchor_bytes = anchors.tobytes()
    if struct.pack("=H", 1) != struct.pack("<H", 1):
        # GitHub runners are little-endian; keep format explicit if ported.
        anchor_bytes = b"".join(struct.pack("<H", x) for x in anchors)
    atomic_bytes(out / "anchors-u16le.bin", anchor_bytes)

    manifest = {
        "schema": "a1294-seam-aware-certificate-v1",
        "A": str(A), "B": str(B), "limit": args.limit,
        "weights": list(WEIGHTS), "anchor_denominator": ANCHOR_DEN,
        "input_sha256": {
            "stable": sha256(Path(args.stable)),
            "v1": sha256(Path(args.v1)),
            "v3": sha256(Path(args.v3))
        },
        "visited_nodes": visited,
        "token_count": len(topology),
        "leaves": leaves,
        "tail_leaves": tail_leaves,
        "quadratic_leaves": quadratic_leaves,
        "maximum_depth": max_depth,
        "smallest_tail_margin": None if smallest_tail is None else str(smallest_tail),
        "smallest_quadratic_margin": None if smallest_quad is None else str(smallest_quad),
        "scalar_cache_entries": len(checker.scalar_cache),
        "elapsed_seconds": time.monotonic() - started,
        "stream_sha256": {
            "topology": hashlib.sha256(bytes(topology)).hexdigest(),
            "kinds": hashlib.sha256(bytes(kinds)).hexdigest(),
            "anchors": hashlib.sha256(anchor_bytes).hexdigest()
        },
        "stream_bytes": {
            "topology": len(topology), "kinds": len(kinds), "anchors": len(anchor_bytes)
        },
        "full_stack_exhaustion": True,
        "trust_note": "Float arithmetic proposes anchor codes only. Every terminal acceptance uses exact Fraction arithmetic."
    }
    atomic_json(out / "manifest.json", manifest)
    print(json.dumps(manifest, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
