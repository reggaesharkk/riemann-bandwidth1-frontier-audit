#!/usr/bin/env python3
"""
A1294 source-free exact replay.

Design:
  * Python standard library only.
  * Does NOT import the search generator, project Checker, or any repository code.
  * Reconstructs the deterministic dyadic tree from the canonical topology stream.
  * Rebuilds all 666 scalar lower models from the three frozen JSON inputs.
  * Recomputes every tail and quadratic terminal inequality with Fraction arithmetic.
  * Checks stream/input hashes and full stream exhaustion.

This is an independent-environment replay of an already generated certificate.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import struct
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
ANCHOR_DEN = 16384

def Q(x) -> F:
    return x if isinstance(x, F) else F(str(x))

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

@dataclass(frozen=True)
class Model:
    lo: F
    hi: F
    center: F
    floor: F
    curvature: F
    owner: int
    idx: int

def well_model(item: dict, owner: int, idx: int) -> Model:
    lo, hi = Q(item["lo"]), Q(item["hi"])
    m, v, endpoint = Q(item["m"]), Q(item["v"]), Q(item["q"])
    side = item["side"]
    if side == "left":
        center = endpoint + v / m
    elif side == "right":
        center = endpoint - v / m
    else:
        raise AssertionError(("bad well side", side, idx))
    return Model(lo, hi, center, F(0), 2 * m * m, owner, idx)

def generic_model(item: dict, owner: int, idx: int) -> Model:
    if item.get("kind") == "well":
        return well_model(item, owner, idx)
    lo, hi = Q(item["lo"]), Q(item["hi"])
    return Model(lo, hi, F(0), Q(item.get("a", "0")), F(0), owner, idx)

def interval_infimum(p: Model, lo: F, hi: F) -> F:
    if p.center < lo:
        x = lo
    elif p.center > hi:
        x = hi
    else:
        x = p.center
    return p.floor + p.curvature * (x - p.center) ** 2

class ExactCatalog:
    def __init__(self, stable_path: Path, v1_path: Path, v3_path: Path, A: F, B: F):
        stable_raw = json.loads(stable_path.read_text(encoding="utf-8"))["pieces"]
        v1_raw = json.loads(v1_path.read_text(encoding="utf-8"))["pieces"]
        v3_raw = json.loads(v3_path.read_text(encoding="utf-8"))["pieces"]

        assert len(stable_raw) == 56
        assert len(v1_raw) == 216
        assert len(v3_raw) == 394

        self.stable = [generic_model(it, i, i) for i, it in enumerate(stable_raw)]
        self.highs = [p.hi for p in self.stable]
        self.groups = {i: [] for i in range(56)}
        self.groups[-1] = []

        idx = 56
        for it in v1_raw:
            owner = int(it["stable_piece_index"])
            self.groups[owner].append(well_model(it, owner, idx))
            idx += 1

        for it in v3_raw:
            owner = int(it["stable_piece_index"])
            self.groups[owner].append(generic_model(it, owner, idx))
            idx += 1

        assert idx == 666

        self.A = A
        self.B = B
        self.cutoff = A / B
        self._scalar_cache: dict[tuple[F, F], F] = {}

        self.group_boundaries = {}
        for owner, pieces in self.groups.items():
            values = []
            if owner >= 0:
                values.extend((self.stable[owner].lo, self.stable[owner].hi))
            for p in pieces:
                values.extend((p.lo, p.hi))
            self.group_boundaries[owner] = sorted(set(values))

    def stable_owner(self, x: F) -> int:
        return min(bisect.bisect_left(self.highs, x), 55)

    def strongest_full_cover(self, lo: F, hi: F) -> Model | None:
        owner = self.stable_owner(lo)
        candidates: list[Model] = []

        for o in (owner, max(0, owner - 1), min(55, owner + 1)):
            s = self.stable[o]
            if s.lo <= lo and hi <= s.hi:
                candidates.append(s)
                candidates.extend(
                    p for p in self.groups[o]
                    if p.lo <= lo and hi <= p.hi
                )

        candidates.extend(
            p for p in self.groups[-1]
            if p.lo <= lo and hi <= p.hi
        )

        if not candidates:
            return None
        return max(candidates, key=lambda p: (interval_infimum(p, lo, hi), -p.idx))

    def segmented_scalar_lower(self, lo: F, hi: F) -> F:
        hi = min(hi, self.cutoff)
        if hi < lo:
            return F(0)

        key = (lo, hi)
        cached = self._scalar_cache.get(key)
        if cached is not None:
            return cached

        if lo == hi:
            p = self.strongest_full_cover(lo, hi)
            ans = F(0) if p is None else interval_infimum(p, lo, hi)
            self._scalar_cache[key] = ans
            return ans

        boundaries = {lo, hi}
        first = self.stable_owner(lo)
        last = self.stable_owner(min(hi, F(59)))

        for owner in range(max(0, first - 1), min(55, last + 1) + 1):
            for x in self.group_boundaries[owner]:
                if lo < x < hi:
                    boundaries.add(x)

        for x in self.group_boundaries[-1]:
            if lo < x < hi:
                boundaries.add(x)

        ordered = sorted(boundaries)
        segment_lowers = []

        for left, right in zip(ordered, ordered[1:]):
            p = self.strongest_full_cover(left, right)
            if p is None:
                # Exhaustive fallback over every refinement. Reaching this path is
                # allowed only if an exact covering model exists.
                all_refinements = [
                    z
                    for ps in self.groups.values()
                    for z in ps
                    if z.lo <= left and right <= z.hi
                ]
                if not all_refinements:
                    raise AssertionError(("catalog gap", str(left), str(right)))
                p = max(
                    all_refinements,
                    key=lambda z: (interval_infimum(z, left, right), -z.idx),
                )
            segment_lowers.append(interval_infimum(p, left, right))

        ans = min(segment_lowers)
        self._scalar_cache[key] = ans
        return ans

    def quadratic_form(self, box):
        M = [[F(0) for _ in range(5)] for _ in range(5)]
        linear = [self.B for _ in range(5)]
        constant = F(0)

        for vector, (li, ri) in zip(VECTORS, PARTIALS):
            lo = sum((box[k][0] for k in range(li, ri + 1)), F(0))
            hi = sum((box[k][1] for k in range(li, ri + 1)), F(0))
            clipped_hi = min(hi, self.cutoff)

            direct = self.strongest_full_cover(lo, clipped_hi) if lo <= clipped_hi else None

            if direct is None:
                constant += self.segmented_scalar_lower(lo, hi)
                continue

            # Stable parent pieces may be weaker than the exact segmented
            # refinement envelope. Use the stronger certified lower bound.
            if direct.idx < 56 and self.groups.get(direct.owner):
                segmented = self.segmented_scalar_lower(lo, hi)
                if segmented > interval_infimum(direct, lo, clipped_hi):
                    constant += segmented
                    continue

            constant += direct.floor + direct.curvature * direct.center * direct.center
            if direct.curvature:
                for r in range(5):
                    if not vector[r]:
                        continue
                    linear[r] -= 2 * direct.curvature * direct.center
                    for c in range(5):
                        if vector[c]:
                            M[r][c] += direct.curvature

        return M, linear, constant

    def tangent_lower_from_codes(self, box, codes) -> F:
        M, linear, constant = self.quadratic_form(box)
        point = [
            lo + F(code, ANCHOR_DEN) * (hi - lo)
            for code, (lo, hi) in zip(codes, box)
        ]

        value = constant
        value += sum(linear[i] * point[i] for i in range(5))
        value += sum(
            M[i][j] * point[i] * point[j]
            for i in range(5)
            for j in range(5)
        )

        grad = [
            linear[i] + 2 * sum(M[i][j] * point[j] for j in range(5))
            for i in range(5)
        ]

        for i in range(5):
            value += min(
                grad[i] * (box[i][0] - point[i]),
                grad[i] * (box[i][1] - point[i]),
            )
        return value

def split_box(box):
    weighted = [(hi - lo) * WEIGHTS[i] for i, (lo, hi) in enumerate(box)]
    axis = max(range(5), key=weighted.__getitem__)
    lo, hi = box[axis]
    mid = (lo + hi) / 2
    left, right = list(box), list(box)
    left[axis] = (lo, mid)
    right[axis] = (mid, hi)
    return axis, tuple(left), tuple(right)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package-root", default=".")
    ap.add_argument("--progress", type=int, default=250000)
    args = ap.parse_args()

    root = Path(args.package_root).resolve()
    cert = root / "certificate"
    data = root / "data"

    manifest = json.loads((cert / "manifest.json").read_text(encoding="utf-8"))
    previous = json.loads((cert / "replay.json").read_text(encoding="utf-8"))

    A, B = Q(manifest["A"]), Q(manifest["B"])
    assert manifest["schema"] == "a1294-seam-aware-certificate-v1"
    assert manifest["full_stack_exhaustion"] is True
    assert manifest["weights"] == list(WEIGHTS)
    assert manifest["anchor_denominator"] == ANCHOR_DEN

    stable_path = data / "macro-data-exact.json"
    v1_path = data / "refinement-catalog-v1-exact.json"
    v3_path = data / "refinement-catalog-v3.json"

    actual_input_hashes = {
        "stable": sha256(stable_path),
        "v1": sha256(v1_path),
        "v3": sha256(v3_path),
    }
    assert actual_input_hashes == manifest["input_sha256"]

    topology_path = cert / "topology-u8.bin"
    kinds_path = cert / "terminal-kinds-u8.bin"
    anchors_path = cert / "anchors-u16le.bin"

    actual_stream_hashes = {
        "topology": sha256(topology_path),
        "kinds": sha256(kinds_path),
        "anchors": sha256(anchors_path),
    }
    assert actual_stream_hashes == manifest["stream_sha256"]

    topology = topology_path.read_bytes()
    kinds = kinds_path.read_bytes()
    anchors = anchors_path.read_bytes()

    assert len(topology) == manifest["visited_nodes"]
    assert len(kinds) == manifest["leaves"]
    assert len(anchors) == 10 * manifest["quadratic_leaves"]

    model = ExactCatalog(stable_path, v1_path, v3_path, A, B)

    stack = [tuple((F(0), F(manifest["limit"])) for _ in range(5))]
    token_cursor = 0
    kind_cursor = 0
    anchor_cursor = 0
    tail = 0
    quad = 0
    smallest_tail = None
    smallest_quad = None
    max_stack = 1
    started = time.monotonic()

    while stack:
        box = stack.pop()
        if token_cursor >= len(topology):
            raise AssertionError("topology stream exhausted before reconstructed tree")

        token = topology[token_cursor]
        token_cursor += 1

        if token:
            axis, left, right = split_box(box)
            if token != axis + 1:
                raise AssertionError(("split-axis mismatch", token_cursor, token, axis + 1))
            stack.append(right)
            stack.append(left)
            max_stack = max(max_stack, len(stack))
        else:
            if kind_cursor >= len(kinds):
                raise AssertionError("terminal-kind stream exhausted early")

            kind = kinds[kind_cursor]
            kind_cursor += 1

            if kind == 0:
                margin = B * sum((lo for lo, _ in box), F(0)) - A
                if margin < 0:
                    raise AssertionError(("negative tail margin", token_cursor, str(margin)))
                tail += 1
                smallest_tail = margin if smallest_tail is None else min(smallest_tail, margin)

            elif kind == 1:
                if anchor_cursor + 10 > len(anchors):
                    raise AssertionError("anchor stream exhausted early")
                codes = struct.unpack_from("<5H", anchors, anchor_cursor)
                anchor_cursor += 10
                if any(code > ANCHOR_DEN for code in codes):
                    raise AssertionError(("bad anchor code", token_cursor, codes))
                margin = model.tangent_lower_from_codes(box, codes) - A
                if margin < 0:
                    raise AssertionError(("negative quadratic margin", token_cursor, str(margin)))
                quad += 1
                smallest_quad = margin if smallest_quad is None else min(smallest_quad, margin)

            else:
                raise AssertionError(("bad terminal kind", token_cursor, kind))

        if args.progress and token_cursor % args.progress == 0:
            elapsed = time.monotonic() - started
            print(json.dumps({
                "visited": token_cursor,
                "pending": len(stack),
                "tail": tail,
                "quadratic": quad,
                "elapsed_seconds": elapsed,
                "nodes_per_second": token_cursor / elapsed if elapsed else 0.0,
            }), flush=True)

    # Full stream exhaustion is part of the proof object.
    assert token_cursor == len(topology)
    assert kind_cursor == len(kinds)
    assert anchor_cursor == len(anchors)

    assert tail == manifest["tail_leaves"]
    assert quad == manifest["quadratic_leaves"]
    assert tail + quad == manifest["leaves"]

    assert str(smallest_tail) == manifest["smallest_tail_margin"]
    assert str(smallest_quad) == manifest["smallest_quadratic_margin"]

    # Cross-check against the GitHub independent replay report as a consistency
    # test; this external run is still computing every inequality itself.
    assert previous["status"] == "PASS"
    assert previous["visited_nodes"] == token_cursor
    assert previous["tail_leaves"] == tail
    assert previous["quadratic_leaves"] == quad
    assert previous["stream_sha256"] == actual_stream_hashes
    assert previous["input_sha256"] == actual_input_hashes

    elapsed = time.monotonic() - started
    report = {
        "schema": "a1294-source-free-third-replay-v1",
        "status": "PASS",
        "A": str(A),
        "B": str(B),
        "visited_nodes": token_cursor,
        "leaves": tail + quad,
        "tail_leaves": tail,
        "quadratic_leaves": quad,
        "smallest_tail_margin": str(smallest_tail),
        "smallest_quadratic_margin": str(smallest_quad),
        "input_sha256": actual_input_hashes,
        "stream_sha256": actual_stream_hashes,
        "elapsed_seconds": elapsed,
        "nodes_per_second": token_cursor / elapsed if elapsed else 0.0,
        "maximum_pending_stack": max_stack,
        "environment": {
            "python": __import__("sys").version,
            "platform": __import__("platform").platform(),
            "machine": __import__("platform").machine(),
        },
        "trust_note": (
            "Standard-library source-free replay. No generator, project Checker, "
            "or project verifier is imported. Every terminal inequality is "
            "recomputed with fractions.Fraction."
        ),
    }

    out = root / "A1294_SOURCE_FREE_REPLAY_RESULT.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n=== A1294 SOURCE-FREE REPLAY ===")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("\nRESULT:", out)

if __name__ == "__main__":
    main()
