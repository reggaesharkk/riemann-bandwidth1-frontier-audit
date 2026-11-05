#!/usr/bin/env python3
"""Locate the first complete, multi-leaf all-tail subtree in the frozen V2 tree.

This is a structural extraction pass only: it verifies preorder topology,
weighted split axes, terminal-kind alignment, and exact affine-tail margins. It
does not evaluate any quadratic leaf and is not a full A1294 certificate replay.
"""
from __future__ import annotations

import hashlib
import json
import struct
import sys
from fractions import Fraction
from pathlib import Path

WEIGHTS = (5, 8, 9, 8, 5)
SCALE = 1 << 128
A_NUM, A_DEN = 647, 50_000
B_NUM, B_DEN = 1_094_977, 5_000_000_000


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def box_json(box: tuple[tuple[int, int], ...]) -> list[list[str]]:
    return [[str(Fraction(lo, SCALE)), str(Fraction(hi, SCALE))] for lo, hi in box]


def main() -> None:
    if len(sys.argv) not in (2, 3):
        raise SystemExit("usage: extract_tail_subtree.py <A1294_SOURCE_FREE_REPLAY_PACKAGE_V2> [output.json]")
    root = Path(sys.argv[1])
    cert = root / "certificate"
    top_path, kind_path, anchor_path = (cert / x for x in (
        "topology-u8.bin", "terminal-kinds-u8.bin", "anchors-u16le.bin"))
    topology, kinds, anchors = top_path.read_bytes(), kind_path.read_bytes(), anchor_path.read_bytes()
    manifest = json.loads((cert / "manifest.json").read_text(encoding="utf-8"))
    if len(topology) != manifest["token_count"] or len(kinds) != manifest["leaves"]:
        raise SystemExit("stream length differs from source manifest")

    root_box = tuple((0, 60 * SCALE) for _ in range(5))
    frames: list[dict] = [{"state": 0, "box": root_box, "start": 0, "path_len": 0}]
    path: list[tuple[int, str]] = []
    pos = kind_cursor = anchor_cursor = 0
    max_depth = 0

    while frames:
        frame = frames[-1]
        state = frame["state"]
        if state == 0:
            token_pos = pos
            token = topology[pos]
            pos += 1
            frame["start"] = token_pos
            if token == 0:
                leaf_index = kind_cursor
                if kind_cursor >= len(kinds):
                    raise SystemExit("terminal-kind stream exhausted")
                kind = kinds[kind_cursor]
                kind_cursor += 1
                anchor_offset = anchor_cursor
                if kind == 1:
                    anchor_cursor += 10
                margin_num = None
                if kind == 0:
                    lower_sum = sum(lo for lo, _hi in frame["box"])
                    margin_num = B_NUM * lower_sum - A_NUM * (B_DEN // A_DEN) * SCALE
                result = {
                    "start": token_pos, "end": pos,
                    "leaf_start": leaf_index, "leaf_end": leaf_index + 1,
                    "nodes": 1, "leaves": 1,
                    "all_tail": kind == 0 and margin_num is not None and margin_num >= 0,
                    "min_margin_num": margin_num if kind == 0 else None,
                }
                if kind == 0 and margin_num is not None and margin_num >= 0:
                    leaf_out = {
                        "status": "SOURCE_TAIL_LEAF_EXTRACTED",
                        "scope": "prefix traversal to first source tail terminal; structural extraction only, no quadratic leaf replay",
                        "source_node_index_zero_based": token_pos,
                        "source_leaf_index_zero_based": leaf_index,
                        "source_terminal_kind": "tail",
                        "anchor_stream_byte_offset_before_leaf": anchor_offset,
                        "source_path_axis_zero_based": [i for i, _ in path],
                        "source_path_sides": [side for _, side in path],
                        "source_root_box_exact": box_json(frame["box"]),
                        "A": manifest["A"], "B": manifest["B"],
                        "exact_tail_margin": str(Fraction(margin_num, B_DEN * SCALE)),
                        "source_stream_sha256": {
                            "topology": sha(top_path), "kinds": sha(kind_path),
                            "anchors": sha(anchor_path),
                        },
                    }
                    rendered = json.dumps(leaf_out, indent=2) + "\n"
                    print(rendered, end="")
                    if len(sys.argv) == 3:
                        Path(sys.argv[2]).write_text(rendered, encoding="utf-8")
                    return
                frames.pop()
                if not frames:
                    break
                parent = frames[-1]
                path[:] = path[:parent["path_len"]]
                if parent["state"] == 1:
                    parent["left"] = result
                    parent["state"] = 2
                elif parent["state"] == 3:
                    parent["right"] = result
                    parent["state"] = 4
                else:
                    raise SystemExit("invalid parser state after terminal")
                continue

            axis = token - 1
            if not 0 <= axis < 5:
                raise SystemExit(f"invalid split token {token} at node {token_pos}")
            widths = [(hi - lo) * WEIGHTS[i] for i, (lo, hi) in enumerate(frame["box"])]
            expected = max(range(5), key=widths.__getitem__)
            if axis != expected:
                raise SystemExit(f"weighted-axis mismatch at node {token_pos}: {axis} != {expected}")
            lo, hi = frame["box"][axis]
            if (lo + hi) % 2:
                raise SystemExit(f"dyadic midpoint precision exhausted at node {token_pos}")
            mid = (lo + hi) // 2
            left = list(frame["box"])
            right = list(frame["box"])
            left[axis] = (lo, mid)
            right[axis] = (mid, hi)
            frame["axis"] = axis
            frame["right_box"] = tuple(right)
            frame["state"] = 1
            path.append((axis, "L"))
            max_depth = max(max_depth, len(frames))
            frames.append({"state": 0, "box": tuple(left), "start": token_pos,
                           "path_len": len(path)})
        elif state == 2:
            frame["state"] = 3
            path.append((frame["axis"], "R"))
            max_depth = max(max_depth, len(frames))
            frames.append({"state": 0, "box": frame["right_box"], "start": pos,
                           "path_len": len(path)})
        elif state == 4:
            left, right = frame["left"], frame["right"]
            result = {
                "start": frame["start"], "end": pos,
                "leaf_start": left["leaf_start"], "leaf_end": right["leaf_end"],
                "nodes": 1 + left["nodes"] + right["nodes"],
                "leaves": left["leaves"] + right["leaves"],
                "all_tail": left["all_tail"] and right["all_tail"],
                "min_margin_num": min(left["min_margin_num"], right["min_margin_num"])
                    if left["min_margin_num"] is not None and right["min_margin_num"] is not None
                    else None,
            }
            if result["all_tail"] and 2 <= result["leaves"] and result["nodes"] <= 31:
                # Three nodes is the smallest possible nontrivial complete binary tree.
                margin_den = B_DEN * SCALE
                token_slice = list(topology[result["start"]:result["end"]])
                kind_slice = list(kinds[result["leaf_start"]:result["leaf_end"]])
                if result["nodes"] == 3:
                    split_axis = token_slice[0] - 1
                    lo, hi = frame["box"][split_axis]
                    mid = (lo + hi) // 2
                    child_boxes = []
                    for child_lo, child_hi in ((lo, mid), (mid, hi)):
                        child_box = list(frame["box"])
                        child_box[split_axis] = (child_lo, child_hi)
                        child_boxes.append(tuple(child_box))
                    tail_margin_nums = [
                        B_NUM * sum(xlo for xlo, _xhi in child_box) -
                        A_NUM * (B_DEN // A_DEN) * SCALE
                        for child_box in child_boxes
                    ]
                    out = {
                        "status": "STRUCTURAL_SUBTREE_EXTRACTED",
                        "scope": "prefix traversal to first 3-node all-tail subtree; no quadratic leaves replayed",
                        "source_node_interval_half_open": [result["start"], result["end"]],
                        "source_leaf_interval_half_open": [result["leaf_start"], result["leaf_end"]],
                        "complete_subtree_nodes": result["nodes"],
                        "complete_subtree_leaves": result["leaves"],
                        "root_path_axis_zero_based": [i for i, _ in path],
                        "root_path_sides": [side for _, side in path],
                        "root_box_exact": box_json(frame["box"]),
                        "A": manifest["A"], "B": manifest["B"],
                        "subtree_topology_tokens": token_slice,
                        "subtree_leaf_kinds": kind_slice,
                        "subtree_tail_margins": [str(Fraction(x, B_DEN * SCALE))
                                                  for x in tail_margin_nums],
                        "minimum_tail_margin": str(Fraction(result["min_margin_num"], margin_den)),
                        "stream_sha256": {
                            "topology": sha(top_path), "kinds": sha(kind_path),
                            "anchors": sha(anchor_path),
                        },
                        "anchors_sha256": sha(anchor_path),
                        "anchor_stream_bytes_consumed_before_subtree": None,
                        "parser_max_depth": max_depth,
                    }
                    # The chosen subtree consists of a split and two tail leaves.
                    if token_slice[0] == 0 or token_slice.count(0) != 2 or kind_slice != [0, 0]:
                        raise SystemExit("candidate does not have exact split/tail/tail form")
                    print(json.dumps(out, indent=2))
                    return
            frames.pop()
            if not frames:
                break
            parent = frames[-1]
            path[:] = path[:parent["path_len"]]
            if parent["state"] == 1:
                parent["left"] = result
                parent["state"] = 2
            elif parent["state"] == 3:
                parent["right"] = result
                parent["state"] = 4
            else:
                raise SystemExit("invalid parser state after internal node")
        else:
            raise SystemExit(f"invalid parser state {state}")
    raise SystemExit("no complete 3-node all-tail subtree exists")


if __name__ == "__main__":
    main()
