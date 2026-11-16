#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

TARGET=-F(17,360)

def parse(s): return F(s)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()

    files=sorted(Path(a.root).rglob("batch_*.json"))
    assert files, "no batch artifacts"
    seen={}
    total=F(0)
    batches=set()

    for p in files:
        d=json.loads(p.read_text(encoding="utf-8"))
        assert d["schema"]=="c7-orbit-batch-v1"
        assert d["complete"] is True, ("incomplete batch",p)
        batches.add(d["batch"])
        assert d["completed_orbits"]==d["expected_batch_orbits"]
        chk=F(0)
        for row in d["rows"]:
            rep=int(row["rep"])
            assert rep not in seen, ("duplicate rep",rep,p,seen.get(rep))
            v=parse(row["value"])
            c=parse(row["contribution"])
            assert c == int(row["sign"])*int(row["multiplicity"])*v
            chk+=c
            seen[rep]=str(p)
        assert chk==parse(d["partial"])
        total+=chk

    assert batches==set(range(32)), ("missing batches",sorted(set(range(32))-batches))
    assert len(seen)==397, ("orbit coverage",len(seen))
    assert total==TARGET, ("C7 mismatch",total,TARGET)

    result={
        "schema":"c7-full-exact-orbit-certificate-v1",
        "batches":32,
        "canonical_orbits":397,
        "original_terms":9366,
        "exact_sum":f"{total.numerator}/{total.denominator}",
        "target":"-17/360",
        "status":"PASS",
    }
    Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2,sort_keys=True))
    print("RESULT: C7_FULL_EXACT_ORBIT_CERTIFICATE_PASS")

if __name__=="__main__":
    main()
