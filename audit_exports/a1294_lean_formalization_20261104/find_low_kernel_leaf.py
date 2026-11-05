#!/usr/bin/env python3
"""Find a tiny early complete leaf provable from the pinned kernel low-range lemma.

Only a bounded preorder prefix is visited. It does not evaluate terminal payloads
or replay the complete A1294 certificate.
"""
import hashlib
import json
import struct
import sys
from fractions import Fraction
from pathlib import Path

WEIGHTS = (5, 8, 9, 8, 5)
NODE_CAP = 200_000


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: find_low_kernel_leaf.py <A1294_SOURCE_FREE_REPLAY_PACKAGE_V2>")
    root = Path(sys.argv[1])
    cert = root / "certificate"
    topology_path = cert / "topology-u8.bin"
    kinds_path = cert / "terminal-kinds-u8.bin"
    anchors_path = cert / "anchors-u16le.bin"
    topology = topology_path.read_bytes()
    kinds = kinds_path.read_bytes()
    anchors = anchors_path.read_bytes()
    manifest = json.loads((cert / "manifest.json").read_text())

    root_box = [(Fraction(0), Fraction(60)) for _ in range(5)]
    stack = [(root_box, ())]
    kind_cursor = 0
    anchor_cursor = 0
    for node_index, token in enumerate(topology[:NODE_CAP]):
        if not stack:
            raise SystemExit(f"empty traversal stack at node {node_index}")
        box, path = stack.pop()
        if token == 0:
            if kind_cursor >= len(kinds):
                raise SystemExit("terminal-kind stream exhausted early")
            kind = kinds[kind_cursor]
            leaf_index = kind_cursor
            kind_cursor += 1
            codes = None
            if kind == 1:
                off = anchor_cursor
                codes = list(struct.unpack_from("<5H", anchors, off))
                anchor_cursor += 10
                low_partial = None
                for i in range(5):
                    for j in range(i, 5):
                        lo = sum((box[k][0] for k in range(i, j + 1)), Fraction(0))
                        hi = sum((box[k][1] for k in range(i, j + 1)), Fraction(0))
                        if hi <= 2:
                            low_partial = {"left": i, "right": j, "lo": str(lo), "hi": str(hi)}
                            break
                    if low_partial is not None:
                        break
                if low_partial is not None:
                    result = {
                        "status": "PREFIX_LEAF_DECODED",
                        "scope": f"bounded preorder prefix, at most {NODE_CAP} nodes; no terminal replay",
                        "source_node_index_zero_based": node_index,
                        "source_leaf_index_zero_based": leaf_index,
                        "source_terminal_kind": "quadratic",
                        "source_anchor_codes_u16le": codes,
                        "root_path_axis_zero_based": [axis for axis, _side in path],
                        "root_path_sides": [side for _axis, side in path],
                        "root_path_split_count": len(path),
                        "root_box_exact": [[str(lo), str(hi)] for lo, hi in box],
                        "low_kernel_partial_gap": low_partial,
                        "A": manifest["A"],
                        "B": manifest["B"],
                        "stream_sha256": {
                            "topology": sha(topology_path),
                            "kinds": sha(kinds_path),
                            "anchors": sha(anchors_path),
                        },
                    }
                    print(json.dumps(result, indent=2))
                    return
        else:
            widths = [(box[i][1] - box[i][0]) * WEIGHTS[i] for i in range(5)]
            axis = max(range(5), key=widths.__getitem__)
            if token != axis + 1:
                raise SystemExit(f"axis mismatch at node {node_index}: {token} != {axis + 1}")
            lo, hi = box[axis]
            mid = (lo + hi) / 2
            left, right = list(box), list(box)
            left[axis] = (lo, mid)
            right[axis] = (mid, hi)
            stack.append((right, path + ((axis, "R"),)))
            stack.append((left, path + ((axis, "L"),)))
    raise SystemExit(f"no low-kernel quadratic leaf found in first {NODE_CAP} nodes")


if __name__ == "__main__":
    main()
