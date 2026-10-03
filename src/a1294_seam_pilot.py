from __future__ import annotations

import argparse
import bisect
import json
import time
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

WEIGHTS = (5, 8, 9, 8, 5)
PARTIALS = tuple((i, j) for i in range(5) for j in range(i, 5))
VECTORS = tuple(
    tuple(1 if i <= k <= j else 0 for k in range(5))
    for i, j in PARTIALS
)


@dataclass(frozen=True)
class Piece:
    lo: F
    hi: F
    q: F
    a: F
    c: F
    owner: int
    idx: int


def q(x) -> F:
    return x if isinstance(x, F) else F(str(x))


def parse_model(item, owner: int, idx: int) -> Piece:
    lo, hi = q(item["lo"]), q(item["hi"])
    kind = item["kind"]
    if kind in ("low", "barrier", "zero"):
        return Piece(lo, hi, F(0), q(item.get("a", "0")), F(0), owner, idx)
    if kind == "well":
        m, v, endpoint = q(item["m"]), q(item["v"]), q(item["q"])
        center = endpoint + v / m if item["side"] == "left" else endpoint - v / m
        return Piece(lo, hi, center, F(0), 2 * m * m, owner, idx)
    raise ValueError(kind)


def model_min(piece: Piece, lo: F, hi: F) -> F:
    point = piece.q if lo <= piece.q <= hi else lo if piece.q < lo else hi
    return piece.a + piece.c * (point - piece.q) ** 2


class Checker:
    """Exact finite lower-bound checker with refinement-seam scalar fallback.

    Float arithmetic is used only to propose an anchor.  Every accepted lower
    bound is evaluated with Fraction arithmetic.
    """

    def __init__(self, stable_path, v1_path, v3_path, A: F, B: F):
        stable_raw = json.loads(Path(stable_path).read_text())["pieces"]
        self.stable = [parse_model(item, i, i) for i, item in enumerate(stable_raw)]
        assert len(self.stable) == 56
        self.highs = [piece.hi for piece in self.stable]

        groups = {i: [] for i in range(56)}
        groups[-1] = []  # v3 extension on [59,60]
        idx = 56

        for item in json.loads(Path(v1_path).read_text())["pieces"]:
            owner = int(item["stable_piece_index"])
            copy = dict(item)
            copy["kind"] = "well"
            groups[owner].append(parse_model(copy, owner, idx))
            idx += 1

        for item in json.loads(Path(v3_path).read_text())["pieces"]:
            owner = int(item["stable_piece_index"])
            groups[owner].append(parse_model(item, owner, idx))
            idx += 1

        assert idx == 666
        self.groups = groups
        self.A, self.B, self.cutoff = A, B, A / B
        self.scalar_cache = {}
        self.group_bounds = {
            owner: sorted(
                set(
                    ([self.stable[owner].lo, self.stable[owner].hi] if owner >= 0 else [])
                    + [piece.lo for piece in pieces]
                    + [piece.hi for piece in pieces]
                )
            )
            for owner, pieces in groups.items()
        }

    def stable_owner(self, x: F) -> int:
        index = bisect.bisect_left(self.highs, x)
        return min(index, 55)

    def containing_best(self, lo: F, hi: F):
        owner0 = self.stable_owner(lo)
        candidates = []
        for owner in (owner0, max(0, owner0 - 1), min(55, owner0 + 1)):
            stable = self.stable[owner]
            if stable.lo <= lo and hi <= stable.hi:
                candidates.append(stable)
                candidates.extend(
                    piece for piece in self.groups[owner]
                    if piece.lo <= lo and hi <= piece.hi
                )
        candidates.extend(
            piece for piece in self.groups[-1]
            if piece.lo <= lo and hi <= piece.hi
        )
        if not candidates:
            return None
        return max(candidates, key=lambda piece: (model_min(piece, lo, hi), -piece.idx))

    def scalar_min(self, lo: F, hi: F) -> F:
        hi = min(hi, self.cutoff)
        if hi < lo:
            return F(0)
        key = (lo, hi)
        cached = self.scalar_cache.get(key)
        if cached is not None:
            return cached

        boundaries = {lo, hi}
        first = self.stable_owner(lo)
        last = self.stable_owner(min(hi, F(59)))
        for owner in range(max(0, first - 1), min(55, last + 1) + 1):
            for boundary in self.group_bounds[owner]:
                if lo < boundary < hi:
                    boundaries.add(boundary)
        for boundary in self.group_bounds[-1]:
            if lo < boundary < hi:
                boundaries.add(boundary)

        ordered = sorted(boundaries)
        if lo == hi:
            piece = self.containing_best(lo, hi)
            result = F(0) if piece is None else model_min(piece, lo, hi)
            self.scalar_cache[key] = result
            return result

        values = []
        for left, right in zip(ordered, ordered[1:]):
            piece = self.containing_best(left, right)
            if piece is None:
                all_refinements = [
                    p for pieces in self.groups.values() for p in pieces
                    if p.lo <= left and right <= p.hi
                ]
                if not all_refinements:
                    raise RuntimeError(f"catalog gap {left} {right}")
                piece = max(
                    all_refinements,
                    key=lambda p: model_min(p, left, right),
                )
            values.append(model_min(piece, left, right))
        result = min(values)
        self.scalar_cache[key] = result
        return result

    def quadratic_data(self, box):
        matrix = [[F(0) for _ in range(5)] for _ in range(5)]
        linear = [self.B for _ in range(5)]
        constant = F(0)

        for vector, (left_index, right_index) in zip(VECTORS, PARTIALS):
            lo = sum((box[k][0] for k in range(left_index, right_index + 1)), F(0))
            hi = sum((box[k][1] for k in range(left_index, right_index + 1)), F(0))
            clipped_hi = min(hi, self.cutoff)
            piece = self.containing_best(lo, clipped_hi) if lo <= clipped_hi else None
            if piece is None:
                constant += self.scalar_min(lo, hi)
                continue

            # New v0.2 mechanism.  If only the parent stable piece covers the
            # entire interval, a refinement seam can make the parent model much
            # weaker than the certified refined envelope.  Compute an exact
            # segmented scalar certificate and use it when stronger.
            if piece.idx < 56 and self.groups.get(piece.owner):
                scalar = self.scalar_min(lo, hi)
                if scalar > model_min(piece, lo, clipped_hi):
                    constant += scalar
                    continue

            constant += piece.a + piece.c * piece.q * piece.q
            if piece.c:
                for row in range(5):
                    if not vector[row]:
                        continue
                    linear[row] -= 2 * piece.c * piece.q
                    for column in range(5):
                        if vector[column]:
                            matrix[row][column] += piece.c
        return matrix, linear, constant

    @staticmethod
    def proposal(matrix, linear, box):
        mf = [[float(value) for value in row] for row in matrix]
        lf = [float(value) for value in linear]
        lo = [float(bounds[0]) for bounds in box]
        hi = [float(bounds[1]) for bounds in box]
        point = [(left + right) / 2 for left, right in zip(lo, hi)]

        for _ in range(12):
            for row in range(5):
                diagonal = mf[row][row]
                if diagonal > 0:
                    off = sum(
                        mf[row][column] * point[column]
                        for column in range(5)
                        if column != row
                    )
                    value = -(lf[row] + 2 * off) / (2 * diagonal)
                    point[row] = min(max(value, lo[row]), hi[row])
                else:
                    point[row] = lo[row] if lf[row] >= 0 else hi[row]

        exact = []
        for value, (left, right) in zip(point, box):
            if left == right:
                exact.append(left)
                continue
            width = float(right - left)
            if width == 0.0:
                exact.append((left + right) / 2)
                continue
            rel = (value - float(left)) / width
            code = round(max(0.0, min(1.0, rel)) * 16384)
            exact.append(left + F(code, 16384) * (right - left))
        return exact

    @staticmethod
    def tangent(matrix, linear, constant, box, point):
        value = (
            constant
            + sum(linear[i] * point[i] for i in range(5))
            + sum(
                matrix[i][j] * point[i] * point[j]
                for i in range(5)
                for j in range(5)
            )
        )
        gradient = [
            linear[i]
            + 2 * sum(matrix[i][j] * point[j] for j in range(5))
            for i in range(5)
        ]
        return value + sum(
            min(
                gradient[i] * (box[i][0] - point[i]),
                gradient[i] * (box[i][1] - point[i]),
            )
            for i in range(5)
        )

    def lower(self, box):
        matrix, linear, constant = self.quadratic_data(box)
        point = self.proposal(matrix, linear, box)
        return self.tangent(matrix, linear, constant, box, point)


def run_prefix(args):
    A, B = q(args.a), q(args.b)
    checker = Checker(args.stable, args.v1, args.v3, A, B)
    stack = [(tuple((F(0), F(args.limit)) for _ in range(5)), 0)]
    visited = leaves = tail = quadratic = max_depth = 0
    smallest = None
    started = time.monotonic()

    while stack:
        box, depth = stack.pop()
        visited += 1
        max_depth = max(max_depth, depth)
        if visited > args.max_nodes:
            return {
                "status": "NODE_CAP",
                "visited": visited - 1,
                "pending": len(stack) + 1,
                "leaves": leaves,
                "tail": tail,
                "quadratic": quadratic,
                "maximum_depth": max_depth,
                "smallest_closed_margin": None if smallest is None else str(smallest),
                "scalar_cache_entries": len(checker.scalar_cache),
                "elapsed_seconds": time.monotonic() - started,
            }

        margin = B * sum((bounds[0] for bounds in box), F(0)) - A
        if margin >= 0:
            leaves += 1
            tail += 1
            smallest = margin if smallest is None else min(smallest, margin)
            continue

        margin = checker.lower(box) - A
        if margin >= 0:
            leaves += 1
            quadratic += 1
            smallest = margin if smallest is None else min(smallest, margin)
            continue

        weighted = [
            (hi - lo) * WEIGHTS[index]
            for index, (lo, hi) in enumerate(box)
        ]
        axis = max(range(5), key=weighted.__getitem__)
        lo, hi = box[axis]
        midpoint = (lo + hi) / 2
        left, right = list(box), list(box)
        left[axis] = (lo, midpoint)
        right[axis] = (midpoint, hi)
        stack.append((tuple(right), depth + 1))
        stack.append((tuple(left), depth + 1))

    return {
        "status": "PASS",
        "visited": visited,
        "pending": 0,
        "leaves": leaves,
        "tail": tail,
        "quadratic": quadratic,
        "maximum_depth": max_depth,
        "smallest_closed_margin": str(smallest),
        "scalar_cache_entries": len(checker.scalar_cache),
        "elapsed_seconds": time.monotonic() - started,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stable", required=True)
    parser.add_argument("--v1", required=True)
    parser.add_argument("--v3", required=True)
    parser.add_argument("--a", default="1294/100000")
    parser.add_argument("--b", default="1094977/5000000000")
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--max-nodes", type=int, default=10000)
    args = parser.parse_args()
    print(json.dumps(run_prefix(args), indent=2))
