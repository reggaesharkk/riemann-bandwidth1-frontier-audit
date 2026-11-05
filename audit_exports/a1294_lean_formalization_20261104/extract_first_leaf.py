#!/usr/bin/env python3
"""Decode only the first complete A1294 leaf from the frozen preorder stream.

This is a prefix decoder, not a full-tree replay. It validates the declared
weighted midpoint split axes along the first root-to-leaf path and emits the
exact rational box plus source stream indices/hashes.
"""
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

WEIGHTS = (5, 8, 9, 8, 5)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fs(s: str) -> str:
    return str(s)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: extract_first_leaf.py <A1294_SOURCE_FREE_REPLAY_PACKAGE_V2>")
    root = Path(sys.argv[1])
    cert = root / "certificate"
    topology = (cert / "topology-u8.bin").read_bytes()
    kinds = (cert / "terminal-kinds-u8.bin").read_bytes()
    anchors_path = cert / "anchors-u16le.bin"
    target = topology.find(b"\x00")
    if target < 0:
        raise SystemExit("topology has no terminal")
    if kinds[0] not in (0, 1):
        raise SystemExit("invalid first terminal kind")

    box = [(Fraction(0), Fraction(60)) for _ in range(5)]
    stack = [box]
    path_axes = []
    path_sides = []
    for node, token in enumerate(topology[:target]):
        if token == 0 or not stack:
            raise SystemExit(f"unexpected terminal/empty stack at node {node}")
        current = stack.pop()
        widths = [(current[i][1] - current[i][0]) * WEIGHTS[i] for i in range(5)]
        axis = max(range(5), key=widths.__getitem__)
        if token != axis + 1:
            raise SystemExit(f"axis mismatch at node {node}: stream={token}, expected={axis + 1}")
        lo, hi = current[axis]
        mid = (lo + hi) / 2
        left, right = list(current), list(current)
        left[axis] = (lo, mid)
        right[axis] = (mid, hi)
        stack.append(right)
        stack.append(left)
        path_axes.append(axis)
        path_sides.append("L")

    if topology[target] != 0 or not stack:
        raise SystemExit("first terminal is not a valid pending node")
    leaf = stack[-1]
    if kinds[0] == 1:
        anchors = anchors_path.read_bytes()
        codes = [int.from_bytes(anchors[i:i+2], "little") for i in range(0, 10, 2)]
    else:
        codes = None
    manifest = json.loads((cert / "manifest.json").read_text())
    result = {
        "status": "PREFIX_LEAF_DECODED",
        "scope": "first root-to-leaf prefix only; no full replay",
        "source_node_index_zero_based": target,
        "source_leaf_index_zero_based": 0,
        "source_topology_prefix_tokens": list(topology[:target + 1]),
        "source_terminal_kind": kinds[0],
        "kind_interpretation": "tail" if kinds[0] == 0 else "quadratic",
        "anchor_codes_if_quadratic": codes,
        "root_path_axis_zero_based": path_axes,
        "root_path_sides": path_sides,
        "root_box_exact": [[fs(a), fs(b)] for a, b in leaf],
        "weighted_split_checks": len(path_axes),
        "A": manifest["A"],
        "B": manifest["B"],
        "stream_sha256": {
            "topology": sha(cert / "topology-u8.bin"),
            "kinds": sha(cert / "terminal-kinds-u8.bin"),
            "anchors": sha(anchors_path),
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
