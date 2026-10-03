#!/usr/bin/env python3
"""Exact feasibility search for the six-translate bandwidth-one certificate.

This is a search program, not the final serialized certificate generator.
Every terminal decision is made with fractions.Fraction arithmetic. Floating
point is used only to propose a tangent anchor; the anchor is snapped to a
fixed rational grid before the exact lower bound is evaluated.

The search is checkpointable. A PASS says that the specified box/domain was
covered by exact tail/quadratic leaves for the supplied lower-bound catalogs.
A PASS is still not by itself the zeta-density theorem: the one-dimensional
catalog soundness and analytic bridge remain separate obligations.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import heapq
import json
import math
import os
import tempfile
import time
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

WEIGHTS = (5, 8, 9, 8, 5)
PARTIALS = tuple((i, j) for i in range(5) for j in range(i, 5))
VECTORS = tuple(tuple(1 if i <= k <= j else 0 for k in range(5)) for i, j in PARTIALS)
ANCHOR_DENOMINATOR = 16384
SCHEMA = "rh-bandwidth1-a1295-exact-feasibility-v1"


def q(value) -> F:
    if isinstance(value, F):
        return value
    text = str(value)
    if "/" in text:
        a, b = text.split("/", 1)
        return F(int(a), int(b))
    return F(text)


def qs(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def box_json(box):
    return [[qs(lo), qs(hi)] for lo, hi in box]


def box_from_json(raw):
    return tuple((q(lo), q(hi)) for lo, hi in raw)


@dataclass(frozen=True)
class Piece:
    lo: F
    hi: F
    center: F
    a: F
    c: F
    index: int
    owner: int

    def minimum(self, lo: F, hi: F) -> F:
        assert self.lo <= lo <= hi <= self.hi
        point = self.center if lo <= self.center <= hi else lo if self.center < lo else hi
        return self.a + self.c * (point - self.center) ** 2


def make_piece(item: dict, index: int, owner: int, default_kind: str | None = None) -> Piece:
    kind = item.get("kind", default_kind)
    lo, hi = q(item["lo"]), q(item["hi"])
    if kind == "well" or (kind is None and "m" in item):
        m, v, endpoint = q(item["m"]), q(item["v"]), q(item["q"])
        center = endpoint + v / m if item["side"] == "left" else endpoint - v / m
        return Piece(lo, hi, center, F(0), 2 * m * m, index, owner)
    if kind in ("low", "zero", "barrier") or kind is None:
        return Piece(lo, hi, F(0), q(item.get("a", "0")), F(0), index, owner)
    raise ValueError(f"unknown piece kind {kind!r}")


class Checker:
    def __init__(self, stable_path: Path, v1_path: Path, v3_path: Path, A: F, B: F):
        self.A, self.B, self.cutoff = A, B, A / B
        stable_raw = json.loads(stable_path.read_text())["pieces"]
        v1_raw = json.loads(v1_path.read_text())["pieces"]
        v3_payload = json.loads(v3_path.read_text())
        v3_raw = v3_payload["pieces"]
        self.stable = [make_piece(item, i, i, item.get("kind")) for i, item in enumerate(stable_raw)]
        if len(self.stable) != 56:
            raise ValueError(f"expected 56 stable pieces, got {len(self.stable)}")
        if self.stable[0].lo != 0:
            raise ValueError("stable catalog must start at 0")
        if any(a.hi != b.lo for a, b in zip(self.stable, self.stable[1:])):
            raise ValueError("stable catalog is not contiguous")
        self.highs = [p.hi for p in self.stable]
        self.catalog = list(self.stable)
        self.groups = {i: [self.stable[i]] for i in range(56)}
        self.extra = []
        v1_owners = (3, 9, 17, 23, 24, 27, 29, 35, 42)
        if len(v1_raw) != 216:
            raise ValueError(f"expected 216 v1 pieces, got {len(v1_raw)}")
        for i, item in enumerate(v1_raw):
            owner = int(item.get("stable_piece_index", v1_owners[i // 24]))
            piece = make_piece(item, 56 + i, owner, "well")
            self.catalog.append(piece)
            self.groups.setdefault(owner, []).append(piece)
        if v3_payload.get("base_catalog_index") not in (None, 272):
            raise ValueError("unexpected v3 base_catalog_index")
        for item in v3_raw:
            owner = int(item["stable_piece_index"])
            index = int(item["catalog_index"])
            if index != len(self.catalog):
                raise ValueError(f"catalog index gap: {index} != {len(self.catalog)}")
            piece = make_piece(item, index, owner, item.get("kind", "well"))
            self.catalog.append(piece)
            (self.groups.setdefault(owner, []) if owner >= 0 else self.extra).append(piece)
        if len(self.catalog) != 666:
            raise ValueError(f"expected 666 catalog pieces, got {len(self.catalog)}")
        self.scalar_cache = {}
        self.input_hashes = {
            "stable": sha256(stable_path),
            "v1": sha256(v1_path),
            "v3": sha256(v3_path),
        }

    def stable_index(self, lo: F) -> int:
        return bisect.bisect_left(self.highs, lo)

    def containing_best(self, lo: F, hi: F):
        if hi < lo:
            return None
        idx = self.stable_index(lo)
        candidates = []
        for stable_index in (idx, idx + 1):
            if 0 <= stable_index < len(self.stable):
                stable = self.stable[stable_index]
                if stable.lo <= lo and hi <= stable.hi:
                    candidates.extend(
                        p for p in self.groups.get(stable_index, ()) if p.lo <= lo and hi <= p.hi
                    )
        candidates.extend(p for p in self.extra if p.lo <= lo and hi <= p.hi)
        if not candidates:
            return None
        return max(candidates, key=lambda p: (p.minimum(lo, hi), -p.index))

    def scalar_min(self, lo: F, hi: F) -> F:
        hi = min(hi, self.cutoff)
        if hi < lo:
            return F(0)
        key = (lo, hi)
        cached = self.scalar_cache.get(key)
        if cached is not None:
            return cached
        boundaries = {lo, hi}
        candidates = []
        for piece in self.catalog:
            if piece.hi < lo or piece.lo > hi:
                continue
            candidates.append(piece)
            if lo < piece.lo < hi:
                boundaries.add(piece.lo)
            if lo < piece.hi < hi:
                boundaries.add(piece.hi)
        ordered = sorted(boundaries)
        values = []
        if lo == hi:
            values = [p.minimum(lo, hi) for p in candidates if p.lo <= lo and hi <= p.hi]
        else:
            for left, right in zip(ordered, ordered[1:]):
                local = [p.minimum(left, right) for p in candidates if p.lo <= left and right <= p.hi]
                if not local:
                    raise ArithmeticError(f"catalog gap on [{qs(left)}, {qs(right)}]")
                values.append(max(local))
        if not values:
            raise ArithmeticError(f"no scalar lower bound on [{qs(lo)}, {qs(hi)}]")
        result = min(values)
        self.scalar_cache[key] = result
        return result

    def quadratic_data(self, box):
        matrix = [[F(0) for _ in range(5)] for _ in range(5)]
        linear = [self.B for _ in range(5)]
        constant = F(0)
        for vector, (left_index, right_index) in zip(VECTORS, PARTIALS):
            lo = sum((box[k][0] for k in range(left_index, right_index + 1)), F(0))
            hi = min(sum((box[k][1] for k in range(left_index, right_index + 1)), F(0)), self.cutoff)
            piece = self.containing_best(lo, hi)
            if piece is None:
                constant += self.scalar_min(lo, hi)
                continue
            constant += piece.a + piece.c * piece.center * piece.center
            if piece.c:
                for i in range(5):
                    if not vector[i]:
                        continue
                    linear[i] -= 2 * piece.c * piece.center
                    for j in range(5):
                        if vector[j]:
                            matrix[i][j] += piece.c
        return matrix, linear, constant

    @staticmethod
    def float_coordinate_descent(matrix, linear, box, sweeps: int):
        mf = [[float(x) for x in row] for row in matrix]
        lf = [float(x) for x in linear]
        lo = [float(bounds[0]) for bounds in box]
        hi = [float(bounds[1]) for bounds in box]
        point = [(a + b) / 2 for a, b in zip(lo, hi)]
        for _ in range(sweeps):
            for i in range(5):
                diagonal = mf[i][i]
                if diagonal > 0:
                    off = sum(mf[i][j] * point[j] for j in range(5) if j != i)
                    candidate = -(lf[i] + 2 * off) / (2 * diagonal)
                    point[i] = min(max(candidate, lo[i]), hi[i])
                else:
                    point[i] = lo[i] if lf[i] >= 0 else hi[i]
        return point

    @staticmethod
    def rational_anchor(float_point, box):
        point = []
        for value, (lo, hi) in zip(float_point, box):
            if hi == lo:
                point.append(lo)
                continue
            rel = (F.from_float(float(value)) - lo) / (hi - lo)
            code = round(float(rel) * ANCHOR_DENOMINATOR)
            code = max(0, min(ANCHOR_DENOMINATOR, code))
            point.append(lo + F(code, ANCHOR_DENOMINATOR) * (hi - lo))
        return point

    @staticmethod
    def tangent_lower(matrix, linear, constant, box, point) -> F:
        value = constant + sum(linear[i] * point[i] for i in range(5)) + sum(
            matrix[i][j] * point[i] * point[j] for i in range(5) for j in range(5)
        )
        gradient = [
            linear[i] + 2 * sum(matrix[i][j] * point[j] for j in range(5)) for i in range(5)
        ]
        return value + sum(
            min(gradient[i] * (box[i][0] - point[i]), gradient[i] * (box[i][1] - point[i]))
            for i in range(5)
        )

    def lower(self, box, sweeps: int):
        matrix, linear, constant = self.quadratic_data(box)
        proposal = self.float_coordinate_descent(matrix, linear, box, sweeps)
        point = self.rational_anchor(proposal, box)
        return self.tangent_lower(matrix, linear, constant, box, point)


def split_box(box, axis: int):
    lo, hi = box[axis]
    midpoint = (lo + hi) / 2
    left, right = list(box), list(box)
    left[axis] = (lo, midpoint)
    right[axis] = (midpoint, hi)
    return tuple(left), tuple(right)


def choose_axis(box) -> int:
    return max(range(5), key=lambda i: (box[i][1] - box[i][0]) * WEIGHTS[i])


def checkpoint_payload(args, checker, stack, counters, hard_heap, started: float):
    return {
        "schema": SCHEMA,
        "status": "CHECKPOINT",
        "parameters": {
            "A": qs(q(args.a)), "B": qs(q(args.b)), "limit": qs(q(args.limit)),
            "max_depth": args.max_depth, "sweeps": args.sweeps, "split": "weighted",
        },
        "input_sha256": checker.input_hashes,
        "stack": [{"box": box_json(box), "depth": depth} for box, depth in stack],
        "counters": counters,
        "hard": [item[2] for item in sorted(hard_heap, reverse=True)],
        "elapsed_seconds_accumulated":
            counters.get("elapsed_seconds_accumulated", 0.0) + (time.monotonic() - started),
    }


def restore_checkpoint(path: Path, args, checker):
    raw = json.loads(path.read_text())
    if raw.get("schema") != SCHEMA or raw.get("status") != "CHECKPOINT":
        raise ValueError("checkpoint schema/status mismatch")
    expected = raw["parameters"]
    current = {"A": qs(q(args.a)), "B": qs(q(args.b)), "limit": qs(q(args.limit)),
               "max_depth": args.max_depth, "sweeps": args.sweeps, "split": "weighted"}
    if expected != current:
        raise ValueError(f"checkpoint parameter mismatch: {expected} != {current}")
    if raw["input_sha256"] != checker.input_hashes:
        raise ValueError("checkpoint input hash mismatch")
    stack = [(box_from_json(item["box"]), int(item["depth"])) for item in raw["stack"]]
    counters = dict(raw["counters"])
    counters["elapsed_seconds_accumulated"] = float(raw.get("elapsed_seconds_accumulated", 0.0))
    hard_heap = []
    for serial, item in enumerate(raw.get("hard", [])):
        heapq.heappush(hard_heap, (q(item["deficit"]), serial, item))
        if len(hard_heap) > args.hard_limit:
            heapq.heappop(hard_heap)
    return stack, counters, hard_heap


def run(args):
    A, B = q(args.a), q(args.b)
    checker = Checker(args.data, args.v1, args.v3, A, B)
    for key, expected in {
        "stable": args.expect_data_sha, "v1": args.expect_v1_sha, "v3": args.expect_v3_sha
    }.items():
        if expected and checker.input_hashes[key] != expected:
            raise SystemExit(f"{key} SHA-256 mismatch: {checker.input_hashes[key]} != {expected}")

    if args.resume:
        stack, counters, hard_heap = restore_checkpoint(args.resume, args, checker)
    else:
        root = tuple((F(0), q(args.limit)) for _ in range(5))
        stack = [(root, 0)]
        counters = {
            "visited": 0, "closed_leaves": 0, "tail_leaves": 0, "quadratic_leaves": 0,
            "maximum_depth": 0, "minimum_quadratic_margin": None,
            "elapsed_seconds_accumulated": 0.0,
        }
        hard_heap = []

    started = time.monotonic()
    serial = 0
    segment_start_visited = int(counters["visited"])
    next_checkpoint = (
        int(counters["visited"]) + args.checkpoint_every if args.checkpoint_every else math.inf
    )

    while stack:
        box, depth = stack.pop()
        counters["visited"] += 1
        counters["maximum_depth"] = max(int(counters["maximum_depth"]), depth)
        segment_nodes = int(counters["visited"]) - segment_start_visited
        if args.max_nodes and segment_nodes > args.max_nodes:
            stack.append((box, depth))
            status = "NODE_CAP"
            break
        if depth > args.max_depth:
            stack.append((box, depth))
            status = "DEPTH_CAP"
            break

        span_lower = sum((bounds[0] for bounds in box), F(0))
        if B * span_lower - A >= 0:
            counters["closed_leaves"] += 1
            counters["tail_leaves"] += 1
        else:
            lower = checker.lower(box, args.sweeps)
            margin = lower - A
            if margin >= 0:
                counters["closed_leaves"] += 1
                counters["quadratic_leaves"] += 1
                old = counters["minimum_quadratic_margin"]
                if old is None or margin < q(old):
                    counters["minimum_quadratic_margin"] = qs(margin)
            else:
                axis = choose_axis(box)
                left, right = split_box(box, axis)
                stack.append((right, depth + 1))
                stack.append((left, depth + 1))
                item = {
                    "depth": depth, "box": box_json(box), "lower": qs(lower),
                    "deficit": qs(-margin), "axis": axis,
                }
                heapq.heappush(hard_heap, (-margin, serial, item))
                serial += 1
                if len(hard_heap) > args.hard_limit:
                    heapq.heappop(hard_heap)

        if args.progress and counters["visited"] % args.progress == 0:
            print(
                f"progress visited={counters['visited']} pending={len(stack)} "
                f"depth={counters['maximum_depth']} cache={len(checker.scalar_cache)} "
                f"seconds={counters['elapsed_seconds_accumulated'] + time.monotonic() - started:.1f}",
                flush=True,
            )
        if args.checkpoint and counters["visited"] >= next_checkpoint:
            atomic_json(args.checkpoint,
                        checkpoint_payload(args, checker, stack, counters, hard_heap, started))
            next_checkpoint += args.checkpoint_every
    else:
        status = "PASS"

    counters["elapsed_seconds_accumulated"] = (
        float(counters.get("elapsed_seconds_accumulated", 0.0)) + time.monotonic() - started
    )
    result = {
        "schema": SCHEMA, "status": status, "A": qs(A), "B": qs(B),
        "limit": qs(q(args.limit)), "visited": counters["visited"],
        "closed_leaves": counters["closed_leaves"], "tail_leaves": counters["tail_leaves"],
        "quadratic_leaves": counters["quadratic_leaves"],
        "maximum_depth": counters["maximum_depth"],
        "minimum_quadratic_margin": counters["minimum_quadratic_margin"],
        "pending": len(stack), "scalar_cache_size_current_process": len(checker.scalar_cache),
        "elapsed_seconds": counters["elapsed_seconds_accumulated"],
        "hard": [item[2] for item in sorted(hard_heap, reverse=True)],
        "input_sha256": checker.input_hashes,
        "trust_note": (
            "Every tail and quadratic terminal decision uses exact Fraction arithmetic. "
            "Float coordinate descent proposes only an anchor, which is snapped to denominator 16384 "
            "before the exact convex tangent lower bound is evaluated. This is a feasibility search, "
            "not the final serialized proof certificate or analytic zeta theorem."
        ),
    }
    if args.checkpoint and status != "PASS":
        atomic_json(args.checkpoint,
                    checkpoint_payload(args, checker, stack, counters, hard_heap, time.monotonic()))
    atomic_json(args.output, result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, required=True)
    ap.add_argument("--v1", type=Path, required=True)
    ap.add_argument("--v3", type=Path, required=True)
    ap.add_argument("--a", default="259/20000")
    ap.add_argument("--b", default="1094977/5000000000")
    ap.add_argument("--limit", default="60")
    ap.add_argument("--max-nodes", type=int, default=100000)
    ap.add_argument("--max-depth", type=int, default=512)
    ap.add_argument("--sweeps", type=int, default=8)
    ap.add_argument("--progress", type=int, default=10000)
    ap.add_argument("--hard-limit", type=int, default=32)
    ap.add_argument("--checkpoint", type=Path)
    ap.add_argument("--checkpoint-every", type=int, default=250000)
    ap.add_argument("--resume", type=Path)
    ap.add_argument("--expect-data-sha")
    ap.add_argument("--expect-v1-sha")
    ap.add_argument("--expect-v3-sha")
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    result = run(args)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 2)


if __name__ == "__main__":
    main()
