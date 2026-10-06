#!/usr/bin/env python3
"""
Full exact C7 certification by validated dihedral/translation/sign orbits.

This script consumes:
  * upstream exact_connected.compile_terms(7)
  * upstream exact_polytope.run_term
  * our symmetry canonicalizer, already validated term-by-term on the
    complete exact C5 and C6 archives.

Each canonical orbit is evaluated at one representative with exact Fraction
polytope arithmetic, then multiplied by the exact orbit multiplicity and sign.
Batches are assigned round-robin to spread expensive representatives.
"""
from __future__ import annotations
import argparse, json, sys, time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent

def fracstr(x): return f"{x.numerator}/{x.denominator}" if x.denominator!=1 else str(x.numerator)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--upstream",required=True)
    ap.add_argument("--batch",type=int,required=True)
    ap.add_argument("--batches",type=int,default=32)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()

    up=Path(a.upstream).resolve()
    sys.path.insert(0,str(up/"gpu"))
    sys.path.insert(0,str(ROOT/"src"))

    from exact_connected import compile_terms
    from exact_polytope import run_term
    from wp80_c7_symmetry_reduce import canonical

    terms=compile_terms(7)
    groups=defaultdict(list)
    for i,(sign,masks) in enumerate(terms):
        groups[canonical(sign,masks,7)].append(i)

    orbits=[]
    for key,ids in groups.items():
        rep=min(ids)
        sign,masks=terms[rep]
        assert all(terms[i][0]==sign for i in ids)
        orbits.append((rep,sign,tuple(ids),masks))
    orbits.sort(key=lambda x:x[0])

    assert len(terms)==9366
    assert len(orbits)==397

    selected=[x for j,x in enumerate(orbits) if j % a.batches == a.batch]
    rows=[]
    partial=F(0)
    t0=time.time()
    for ordinal,(rep,sign,ids,masks) in enumerate(selected,1):
        ts=time.time()
        val=run_term("cycle",7,masks)
        contrib=sign*len(ids)*val
        partial+=contrib
        row={
            "rep":rep,
            "sign":sign,
            "multiplicity":len(ids),
            "value":fracstr(val),
            "contribution":fracstr(contrib),
            "wall_seconds":time.time()-ts,
        }
        rows.append(row)
        print(json.dumps(row,sort_keys=True),flush=True)
        # checkpoint after every exact orbit
        Path(a.out).write_text(json.dumps({
            "schema":"c7-orbit-batch-v1",
            "batch":a.batch,
            "batches":a.batches,
            "total_orbits":len(orbits),
            "total_terms":len(terms),
            "completed_orbits":len(rows),
            "expected_batch_orbits":len(selected),
            "partial":fracstr(partial),
            "rows":rows,
            "elapsed_seconds":time.time()-t0,
            "complete":False,
        },indent=2,sort_keys=True)+"\n",encoding="utf-8")

    result={
        "schema":"c7-orbit-batch-v1",
        "batch":a.batch,
        "batches":a.batches,
        "total_orbits":len(orbits),
        "total_terms":len(terms),
        "completed_orbits":len(rows),
        "expected_batch_orbits":len(selected),
        "partial":fracstr(partial),
        "rows":rows,
        "elapsed_seconds":time.time()-t0,
        "complete":True,
    }
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("BATCH_RESULT",a.batch,fracstr(partial),"orbits",len(rows),flush=True)

if __name__=="__main__":
    main()
