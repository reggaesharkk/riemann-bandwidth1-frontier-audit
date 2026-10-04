#!/usr/bin/env python3
"""
WP81 exact {5,2} spectator-pair model certificate driver.

This is a thin fail-closed adapter around the pinned public exact-polytope
engine

    JoshuaHKU/zeta-0.7947-reproduction
    commit d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8
    gpu/exact_connected.py

It generalizes the public {4,2} spectator-pair specification to the
7-cycle {5,2} class.

Free variables:
    (v,c1,c2,c3,c4), with c5=-(c1+c2+c3+c4).

The pair frequencies are (+v,-v).  Up to dihedral/cyclic symmetry in a
7-cycle there are three cyclic-distance classes d=1,2,3, each with
multiplicity 7.  Therefore

    {5,2} = 7 * (U1 + U2 + U3).

For each class the integrand is

    O7(full walk) * C5(c1,...,c5) * C2(v),

where C2(v)=min(|v|,1), C5 is the 150-term partition-cyclic cumulant,
and both overlap factors are integrated exactly by the pinned rational
polytope engine.

This file contains no numerical target for {5,2}.  It is an identification
driver: all 450 exact term values must be produced and then aggregated by
wp81_spec52_aggregate.py.

Usage:
    python src/wp81_spec52_exact.py --upstream PATH --d 1 --terms 0:10 \
        --out work/spec52_d1_000_010.txt

To run a full class locally:
    python src/wp81_spec52_exact.py --upstream PATH --d 1 --terms 0:150 \
        --out work/spec52_d1_all.txt

The upstream checkout must be exactly at the pinned commit unless
--allow-unpinned is supplied explicitly.
"""

import argparse
import importlib.util
import os
import subprocess
import sys
import time
from fractions import Fraction as F

PINNED = "d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8"


def load_upstream(root, allow_unpinned=False):
    root = os.path.abspath(root)
    engine = os.path.join(root, "gpu", "exact_connected.py")
    if not os.path.isfile(engine):
        raise SystemExit(f"missing pinned engine: {engine}")

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

    spec = importlib.util.spec_from_file_location("wp81_exact_connected", engine)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_terms(ec, dcls):
    if dcls not in (1, 2, 3):
        raise ValueError("d must be 1, 2, or 3")

    Z, O = ec.ZERO, ec.ONE
    dim = 5

    # Affine coordinates are (constant,v,c1,c2,c3,c4).
    ZERO = (Z, Z, Z, Z, Z, Z)
    V = (Z, O, Z, Z, Z, Z)
    S1 = (Z, Z, O, Z, Z, Z)
    S2 = (Z, Z, O, O, Z, Z)
    S3 = (Z, Z, O, O, O, Z)
    S4 = (Z, Z, O, O, O, O)

    def add(a, b):
        return tuple(x + y for x, y in zip(a, b))

    # Frequency sequences:
    # d=1: +v,-v,c1,c2,c3,c4,c5
    # d=2: +v,c1,-v,c2,c3,c4,c5
    # d=3: +v,c1,c2,-v,c3,c4,c5
    # walk contains the seven prefix positions before the final return to 0.
    if dcls == 1:
        walk = [ZERO, V, ZERO, S1, S2, S3, S4]
    elif dcls == 2:
        walk = [ZERO, V, add(V, S1), S1, S2, S3, S4]
    else:
        walk = [ZERO, V, add(V, S1), add(V, S2), S2, S3, S4]

    # Five connected-block frequencies c1,...,c5.
    W = [
        S1,
        ec.aff_sub(S2, S1),
        ec.aff_sub(S3, S2),
        ec.aff_sub(S4, S3),
        tuple(-x for x in S4),
    ]

    out = []
    terms5 = ec.compile_terms(5)
    assert len(terms5) == 150

    for sign, masks in terms5:
        pos = [ZERO]
        for mk in masks:
            co = ZERO
            for j in mk:
                co = add(co, W[j])
            pos.append(co)
        out.append(
            (
                sign,
                ec.Cls(dim, walk, pos, 0, f"52d{dcls}"),
            )
        )
    return out


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

    ec = load_upstream(args.upstream, args.allow_unpinned)
    terms = build_terms(ec, args.d)
    lo, hi = parse_terms(args.terms, len(terms))

    print(f"# WP81 {{5,2}} d={args.d}: {len(terms)} terms, doing [{lo},{hi})")
    print(f"# upstream pin = {PINNED}")
    print("# class multiplicity = 7")
    if terms:
        print(f"# breakpoint counts term0 = {terms[0][1].cost()}")
    sys.stdout.flush()

    fh = open(args.out, "a", encoding="utf-8") if args.out else None
    total = F(0)
    t0 = time.time()

    try:
        for i in range(lo, hi):
            sign, cls = terms[i]
            ts = time.time()
            val = cls.integrate()
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
        f"# partial U{args.d} [{lo},{hi}) = {total} = {float(total):+.15f} "
        f"wall={time.time()-t0:.3f}s",
        flush=True,
    )
    if lo == 0 and hi == len(terms):
        print(f"RESULT: SPEC52_D{args.d}_EXACT_CLASS_COMPLETE", flush=True)


if __name__ == "__main__":
    main()
