#!/usr/bin/env python3
"""
WP81 exact {5,2} spectator-pair model certificate driver.

Fast path: use the pinned public exact POLYTOPE engine, not the much slower
nested Newton--Cotes piece enumerator.

Pinned upstream:
    JoshuaHKU/zeta-0.7947-reproduction
    d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8

The public exact_polytope.py already certifies the {4,2} spectator-pair
geometry.  This adapter generalizes exactly that convention from a connected
4-block plus spectator pair to a connected 5-block plus spectator pair.

For {5,2}:
    free variables = (v,c1,c2,c3,c4), c5=-(c1+c2+c3+c4)
    C2(v)=min(|v|,1)=|v| on the support of the full overlap
    three pair-distance classes d=1,2,3
    multiplicity of each class = 7
    {5,2} = 7*(U1+U2+U3)

Each U_d is the signed sum of the 150 partition-cyclic C5 terms, so the full
certificate contains 450 exact rational term integrals.

Fail-closed convention gate:
before any {5,2} term is evaluated, the generalized position builder is
required to reproduce the public exact_polytope.spec42_pos arrays EXACTLY for
all 26 C4 terms and all three {4,2} placement classes.  This checks the
spectator-pair geometry without relying on a numerical value.

No expected target for {5,2} is hard-coded.

Usage:
    python src/wp81_spec52_exact.py --upstream PATH --d 1 \
        --terms 0:10 --out work/spec52_d1_000_010.txt
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import subprocess
import sys
import time
from fractions import Fraction as F

PINNED = "d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_upstream(root, allow_unpinned=False):
    root = os.path.abspath(root)
    ec_path = os.path.join(root, "gpu", "exact_connected.py")
    ep_path = os.path.join(root, "gpu", "exact_polytope.py")
    for p in (ec_path, ep_path):
        if not os.path.isfile(p):
            raise SystemExit(f"missing pinned upstream file: {p}")

    if not allow_unpinned:
        try:
            head = subprocess.check_output(
                ["git", "-C", root, "rev-parse", "HEAD"],
                text=True,
                stderr=subprocess.STDOUT,
            ).strip()
        except Exception as exc:
            raise SystemExit(
                "cannot verify upstream git HEAD; use a real checkout or "
                "--allow-unpinned for exploratory work only"
            ) from exc
        if head != PINNED:
            raise SystemExit(f"upstream HEAD {head} != pinned {PINNED}")

    # exact_polytope imports exact_connected by module name.
    gpu = os.path.join(root, "gpu")
    if gpu not in sys.path:
        sys.path.insert(0, gpu)
    ec = load_module("exact_connected", ec_path)
    sys.modules["exact_connected"] = ec
    ep = load_module("exact_polytope", ep_path)
    return ec, ep


def vadd(a, b):
    return [x + y for x, y in zip(a, b)]


def vsub(a, b):
    return [x - y for x, y in zip(a, b)]


def spec_pair_pos(block_b, dcls, masks, zero, one):
    """General spectator-pair position builder.

    block_b is the connected block size (4 recovers public {4,2};
    5 gives the new {5,2}).  Coordinates are
        (v,c1,...,c_{block_b-1})
    and c_block_b = -sum(c1,...,c_{block_b-1}).
    """
    if dcls not in (1, 2, 3):
        raise ValueError("d must be 1, 2, or 3")
    if block_b < 4:
        raise ValueError("block_b must be >=4")

    dim = block_b
    Z = [zero] * dim
    V = [one] + [zero] * (dim - 1)

    # S_j = c1+...+cj in coordinates (v,c1,...).
    S = []
    cur = Z[:]
    for j in range(1, block_b):
        e = [zero] * dim
        e[j] = one
        cur = vadd(cur, e)
        S.append(cur[:])

    # Pair +v,-v at cyclic distance dcls, followed by connected edges.
    if dcls == 1:
        A = [Z[:], V[:], Z[:]] + [s[:] for s in S]
    elif dcls == 2:
        A = [Z[:], V[:], vadd(V, S[0]), S[0][:]] + [s[:] for s in S[1:]]
    else:
        A = [
            Z[:],
            V[:],
            vadd(V, S[0]),
            vadd(V, S[1]),
            S[1][:],
        ] + [s[:] for s in S[2:]]

    assert len(A) == block_b + 2

    # Connected frequencies c1,...,c_block_b.
    W = [S[0][:]]
    for j in range(1, block_b - 1):
        W.append(vsub(S[j], S[j - 1]))
    W.append([-x for x in S[-1]])
    assert len(W) == block_b

    B = [Z[:]]
    for mk in masks:
        co = Z[:]
        for j in mk:
            co = vadd(co, W[j])
        B.append(co)

    return dim, A, B


def convention_gate(ec, ep):
    """Exact structural regression against every public {4,2} term."""
    terms4 = ec.compile_terms(4)
    assert len(terms4) == 26
    for dcls in (1, 2, 3):
        for _, masks in terms4:
            d0, A0, B0 = ep.spec42_pos(dcls, masks)
            d1, A1, B1 = spec_pair_pos(
                4, dcls, masks, ep.ZERO, ep.ONE
            )
            assert d0 == d1 == 4
            assert A0 == A1, ("A convention mismatch", dcls, masks)
            assert B0 == B1, ("B convention mismatch", dcls, masks)
    print("CONVENTION_GATE: generic spectator builder == public spec42_pos "
          "for 26 terms x 3 classes PASS", flush=True)


def run_term(ep, dcls, masks):
    d, A, B = spec_pair_pos(5, dcls, masks, ep.ZERO, ep.ONE)
    n, rows = ep.hrep(A, B, d)
    # On O_7 support |v|<1, hence C2(v)=min(|v|,1)=|v|.
    return ep.weighted_x0(rows, n)


def parse_terms(spec, n):
    if ":" not in spec:
        i = int(spec)
        lo, hi = i, i + 1
    else:
        a, b = spec.split(":", 1)
        lo, hi = int(a), int(b)
    if not (0 <= lo <= hi <= n):
        raise SystemExit(f"bad term range {lo}:{hi}; expected inside 0:{n}")
    return lo, hi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream", required=True)
    ap.add_argument("--d", type=int, choices=(1, 2, 3), required=True)
    ap.add_argument("--terms", default="0:150")
    ap.add_argument("--out")
    ap.add_argument("--allow-unpinned", action="store_true")
    args = ap.parse_args()

    ec, ep = load_upstream(args.upstream, args.allow_unpinned)
    convention_gate(ec, ep)

    terms = ec.compile_terms(5)
    assert len(terms) == 150
    lo, hi = parse_terms(args.terms, len(terms))

    print(f"# WP81 {{5,2}} d={args.d}: 150 terms, doing [{lo},{hi})")
    print(f"# upstream pin = {PINNED}")
    print("# engine = gpu/exact_polytope.py (exact Fraction arithmetic)")
    print("# class multiplicity = 7")
    sys.stdout.flush()

    fh = open(args.out, "a", encoding="utf-8") if args.out else None
    total = F(0)
    t0 = time.time()
    try:
        for i in range(lo, hi):
            sign, masks = terms[i]
            ts = time.time()
            val = run_term(ep, args.d, masks)
            total += sign * val
            line = (
                f"spec52 d {args.d} term {i} sign {sign} "
                f"value {val} wall {time.time()-ts:.6f}"
            )
            print(line, flush=True)
            if fh:
                fh.write(line + "\n")
                fh.flush()
    finally:
        if fh:
            fh.close()

    print(
        f"# partial U{args.d} [{lo},{hi}) = {total} = "
        f"{float(total):+.15f} wall={time.time()-t0:.3f}s",
        flush=True,
    )
    if lo == 0 and hi == len(terms):
        print(f"RESULT: SPEC52_D{args.d}_EXACT_CLASS_COMPLETE", flush=True)


if __name__ == "__main__":
    main()
