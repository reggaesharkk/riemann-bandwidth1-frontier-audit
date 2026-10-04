#!/usr/bin/env python3
"""
Dihedral/translation symmetry reduction for exact cycle polytope terms.

The integral for a cycle term is
    I(B)=∫ O_A(v) O_B(v) dv,  sum_i v_i=0.
O_A is the fixed b-cycle overlap.  The following transformations preserve I:

  * dihedral relabelings of the b cycle edges (rotate/reverse A);
  * translation of every B-position by the same affine form;
  * global sign reversal of every B-position.

We build a canonical exact integer signature under those actions.

Fail-closed validation:
  * parse every archived exact per-term value for b=5 and b=6;
  * require every term in one canonical orbit to have the SAME exact Fraction;
  * require the full signed sums to reproduce C5=1/36 and C6=-1/126.

Only after those checks do we report the b=7 orbit count.
"""
from __future__ import annotations

import argparse, re, sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)

def coeff_of_subset(S,b):
    """Subset-sum affine vector in free coords v0..v_{b-2}, vb-1=-sum."""
    has_last = (b-1) in S
    return tuple((1 if j in S else 0) - (1 if has_last else 0)
                 for j in range(b-1))

def transform_subset(S,b,r,reflect):
    if reflect:
        return frozenset((r-i) % b for i in S)
    return frozenset((i+r) % b for i in S)

def normalize_family(vecs):
    vecs=tuple(sorted(set(vecs)))
    candidates=[]
    for base in vecs:
        tr=tuple(sorted(sub(v,base) for v in vecs))
        candidates.append(tr)
        candidates.append(tuple(sorted(neg(v) for v in tr)))
    return min(candidates)

def canonical(sign,masks,b):
    subsets=(frozenset(),)+tuple(frozenset(m) for m in masks)
    keys=[]
    for reflect in (False,True):
        for r in range(b):
            ss=[transform_subset(S,b,r,reflect) for S in subsets]
            vv=[coeff_of_subset(S,b) for S in ss]
            keys.append(normalize_family(vv))
    return (sign,min(keys))

LINE_RE=re.compile(r"term\s+(\d+)\s+sign\s+(-?\d+)\s+value\s+([^\s]+)")

def parse_archive(path):
    vals={}
    signs={}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m=LINE_RE.search(line)
        if not m: continue
        i=int(m.group(1)); s=int(m.group(2)); v=F(m.group(3))
        if i in vals and vals[i]!=v:
            raise AssertionError(("duplicate term inconsistent",i,vals[i],v))
        vals[i]=v; signs[i]=s
    return vals,signs

def validate(b,terms,archive,target):
    vals,signs=parse_archive(archive)
    assert len(vals)==len(terms),(b,len(vals),len(terms))
    groups=defaultdict(list)
    total=F(0)
    for i,(sign,masks) in enumerate(terms):
        assert signs[i]==sign
        key=canonical(sign,masks,b)
        groups[key].append(i)
        total += sign*vals[i]
    assert total==target,(b,total,target)
    bad=[]
    for key,ids in groups.items():
        vv={vals[i] for i in ids}
        if len(vv)!=1:
            bad.append((ids[:20],vv))
    assert not bad,("symmetry class value mismatch",b,bad[:3])
    mults=sorted((len(ids) for ids in groups.values()),reverse=True)
    print(f"b={b}: terms={len(terms)} canonical_orbits={len(groups)} "
          f"reduction={len(terms)/len(groups):.3f}x")
    print(f"b={b}: max_orbit={mults[0]} median_orbit={mults[len(mults)//2]}")
    print(f"b={b}: exact archive sum={total} target={target} PASS")
    return groups

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--upstream",required=True)
    a=ap.parse_args()
    up=Path(a.upstream).resolve()
    sys.path.insert(0,str(up/"gpu"))
    from exact_connected import compile_terms

    t5=compile_terms(5)
    t6=compile_terms(6)
    t7=compile_terms(7)

    validate(5,t5,up/"gpu/exact/exact_c5.txt",F(1,36))
    validate(6,t6,up/"gpu/exact/exact_c6.txt",-F(1,126))

    g7=defaultdict(list)
    for i,(sign,masks) in enumerate(t7):
        g7[canonical(sign,masks,7)].append(i)

    mults=sorted((len(v) for v in g7.values()),reverse=True)
    reps=sorted(min(v) for v in g7.values())
    print(f"b=7: terms={len(t7)} canonical_orbits={len(g7)} "
          f"predicted_reduction={len(t7)/len(g7):.3f}x")
    print(f"b=7: max_orbit={mults[0]} median_orbit={mults[len(mults)//2]}")
    print("b=7 representative_indices =",",".join(map(str,reps)))
    print("RESULT: C7_SYMMETRY_REDUCTION_VALIDATED_ON_C5_C6")

if __name__=="__main__":
    main()
