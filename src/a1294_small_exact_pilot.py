#!/usr/bin/env python3
"""Exact small feasibility pilot for the A1294 same-B certificate target.

This is deliberately not a full certificate generator.  It uses only exact
Fraction arithmetic for every accepting comparison.  Floating point is used
only to propose tangent anchors; anchors are rationalized to a 2^14 relative
grid before the exact tangent inequality is checked.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json, time

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "research/rh_bandwidth1_20261003/v0_2/upstream/macro-data-exact.json"
V1 = ROOT / "research/rh_bandwidth1_20261003/v0_2/upstream/refinement-catalog-v1-exact.json"
V3 = ROOT / "research/rh_bandwidth1_20261003/v0_2/upstream/refinement-catalog-v3.json"

A = F(1294, 100000)
B = F(1094977, 5000000000)
LIMIT = F(59)
CUTOFF = A / B
WEIGHTS = (5, 8, 9, 8, 5)
PARTIALS = tuple((i, j) for i in range(5) for j in range(i, 5))
VECTORS = tuple(tuple(F(1) if i <= k <= j else F(0) for k in range(5))
                for i, j in PARTIALS)

@dataclass(frozen=True)
class Piece:
    lo: F
    hi: F
    q: F
    a: F
    c: F

def q(x: str | int) -> F:
    s = str(x)
    if "/" in s:
        a, b = s.split("/")
        return F(int(a), int(b))
    return F(int(s))

def model_min(p: Piece, lo: F, hi: F) -> F:
    x = p.q if lo <= p.q <= hi else lo if p.q < lo else hi
    return p.a + p.c * (x - p.q) ** 2

def load_catalog() -> list[Piece]:
    out: list[Piece] = []
    for it in json.loads(DATA.read_text())["pieces"]:
        lo, hi, kind = q(it["lo"]), q(it["hi"]), it["kind"]
        if kind == "low":
            p = Piece(lo, hi, F(0), F(1,4), F(0))
        elif kind == "zero":
            p = Piece(lo, hi, F(0), F(0), F(0))
        elif kind == "barrier":
            p = Piece(lo, hi, F(0), q(it["a"]), F(0))
        elif kind == "well":
            m, v, endpoint = q(it["m"]), q(it["v"]), q(it["q"])
            center = endpoint + v/m if it["side"] == "left" else endpoint - v/m
            p = Piece(lo, hi, center, F(0), 2*m*m)
        else:
            raise ValueError(kind)
        out.append(p)

    for it in json.loads(V1.read_text())["pieces"]:
        lo, hi = q(it["lo"]), q(it["hi"])
        m, v, endpoint = q(it["m"]), q(it["v"]), q(it["q"])
        center = endpoint + v/m if it["side"] == "left" else endpoint - v/m
        out.append(Piece(lo, hi, center, F(0), 2*m*m))

    for it in json.loads(V3.read_text())["pieces"]:
        lo, hi = q(it["lo"]), q(it["hi"])
        if it["kind"] == "well":
            m, v, endpoint = q(it["m"]), q(it["v"]), q(it["q"])
            center = endpoint + v/m if it["side"] == "left" else endpoint - v/m
            out.append(Piece(lo, hi, center, F(0), 2*m*m))
        elif it["kind"] == "barrier":
            out.append(Piece(lo, hi, F(0), q(it["a"]), F(0)))
        else:
            raise ValueError(it["kind"])
    assert len(out) == 666
    return out

CATALOG = load_catalog()

def containing_best(lo: F, hi: F):
    cand = [(model_min(p, lo, hi), i, p) for i, p in enumerate(CATALOG)
            if p.lo <= lo and hi <= p.hi]
    if not cand:
        return None
    _v, i, p = max(cand, key=lambda row: (row[0], -row[1]))
    return i, p

def scalar_lower(lo: F, hi: F) -> F:
    hi = min(hi, CUTOFF)
    if hi < lo:
        return F(0)
    if lo == hi:
        vals = [model_min(p, lo, hi) for p in CATALOG if p.lo <= lo <= p.hi]
        return max(vals) if vals else F(0)
    bounds = {lo, hi}
    for p in CATALOG:
        if lo < p.lo < hi:
            bounds.add(p.lo)
        if lo < p.hi < hi:
            bounds.add(p.hi)
    vals = []
    ordered = sorted(bounds)
    for left, right in zip(ordered, ordered[1:]):
        seg = [model_min(p, left, right) for p in CATALOG
               if p.lo <= left and right <= p.hi]
        if not seg:
            return F(0)
        vals.append(max(seg))
    return min(vals)

def quadratic_data(box):
    M = [[F(0) for _ in range(5)] for _ in range(5)]
    linear = [B for _ in range(5)]
    constant = F(0)
    for vector, (li, ri) in zip(VECTORS, PARTIALS):
        lo = sum((box[k][0] for k in range(li, ri+1)), F(0))
        hi = sum((box[k][1] for k in range(li, ri+1)), F(0))
        clipped_hi = min(hi, CUTOFF)
        selected = containing_best(lo, clipped_hi) if lo <= clipped_hi else None
        if selected is None:
            constant += scalar_lower(lo, hi)
            continue
        _idx, p = selected
        constant += p.a + p.c * p.q * p.q
        if p.c:
            for r in range(5):
                if not vector[r]:
                    continue
                linear[r] -= 2 * p.c * p.q
                for c in range(5):
                    if vector[c]:
                        M[r][c] += p.c
    return M, linear, constant

def tangent_lower(box) -> F:
    M, linear, constant = quadratic_data(box)
    mf = [[float(x) for x in row] for row in M]
    lf = [float(x) for x in linear]
    lo = [float(x[0]) for x in box]
    hi = [float(x[1]) for x in box]
    point = [(a+b)/2 for a,b in zip(lo,hi)]
    for _ in range(10):
        for r in range(5):
            d = mf[r][r]
            if d > 0:
                off = sum(mf[r][c] * point[c] for c in range(5) if c != r)
                v = -(lf[r] + 2*off)/(2*d)
                point[r] = min(max(v, lo[r]), hi[r])
            else:
                point[r] = lo[r] if lf[r] >= 0 else hi[r]

    exact = []
    for v, (a,b) in zip(point, box):
        if a == b:
            exact.append(a)
        else:
            code = round((v-float(a))/float(b-a)*16384)
            code = max(0, min(16384, code))
            exact.append(a + F(code,16384)*(b-a))

    value = constant + sum(linear[i]*exact[i] for i in range(5))
    value += sum(M[i][j]*exact[i]*exact[j] for i in range(5) for j in range(5))
    gradient = [linear[i] + 2*sum(M[i][j]*exact[j] for j in range(5))
                for i in range(5)]
    return value + sum(min(gradient[i]*(box[i][0]-exact[i]),
                           gradient[i]*(box[i][1]-exact[i])) for i in range(5))

def split(box):
    widths = [(hi-lo)*WEIGHTS[i] for i,(lo,hi) in enumerate(box)]
    axis = max(range(5), key=widths.__getitem__)
    lo, hi = box[axis]
    mid = (lo+hi)/2
    left, right = list(box), list(box)
    left[axis] = (lo,mid)
    right[axis] = (mid,hi)
    return tuple(left), tuple(right)

def local_bnb(root, max_nodes=100000):
    stack=[(root,0)]
    visited=leaves=maximum_depth=0
    smallest=None
    started=time.monotonic()
    while stack:
        box, depth = stack.pop()
        visited += 1
        maximum_depth=max(maximum_depth,depth)
        tail = B*sum((x[0] for x in box),F(0))-A
        if tail >= 0:
            margin=tail
        else:
            margin=tangent_lower(box)-A
            if margin < 0:
                if visited >= max_nodes:
                    return {"status":"NODE_CAP","visited":visited,"pending":len(stack)+1,
                            "leaves":leaves,"maximum_depth":maximum_depth,
                            "elapsed_seconds":time.monotonic()-started}
                left,right=split(box)
                stack.append((right,depth+1))
                stack.append((left,depth+1))
                continue
        leaves += 1
        if smallest is None or margin < smallest:
            smallest=margin
    return {"status":"PASS","visited":visited,"leaves":leaves,
            "maximum_depth":maximum_depth,
            "smallest_margin":str(smallest),
            "smallest_margin_float":float(smallest),
            "elapsed_seconds":time.monotonic()-started}

def exact_point_value(point):
    value=B*sum(point,F(0))
    for i,j in PARTIALS:
        s=sum(point[i:j+1],F(0))
        vals=[p.a+p.c*(s-p.q)**2 for p in CATALOG if p.lo <= s <= p.hi]
        value += max(vals) if vals else F(0)
    return value

def main():
    # Public A1293 report's tightest quadratic leaf.
    tight = tuple((q(a),q(b)) for a,b in [
        ("105/16","6735/1024"), ("25815/2048","12915/1024"),
        ("12945/1024","25905/2048"), ("6465/512","25875/2048"),
        ("6735/1024","3375/512")])
    expanded2=[]
    for lo,hi in tight:
        mid=(lo+hi)/2
        half=(hi-lo)
        expanded2.append((mid-half,mid+half))

    # Rationalization of the best numerical point found by a separate
    # multistart differential-evolution diagnostic.
    point=[F(6912667,1048576), F(6541989,524288), F(860015,131072),
           F(13083885,1048576), F(6912651,1048576)]
    pv=exact_point_value(point)

    report={
        "schema":"a1294-small-exact-feasibility-pilot-v1",
        "A":str(A), "B":str(B), "catalog_piece_count":len(CATALOG),
        "exact_adversarial_point":{
            "point":[str(x) for x in point],
            "value":str(pv),
            "value_float":float(pv),
            "margin":str(pv-A),
            "margin_float":float(pv-A),
            "classification":"NOT_COUNTEREXAMPLE" if pv >= A else "COUNTEREXAMPLE"
        },
        "public_a1293_tight_leaf_rechecked_at_A1294": local_bnb(tight,100000),
        "twofold_expansion_of_that_leaf": local_bnb(tuple(expanded2),100000),
        "status":"PASS_LOCAL_PILOT_NOT_FULL_CERTIFICATE"
    }
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
