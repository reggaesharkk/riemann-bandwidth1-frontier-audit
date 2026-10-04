#!/usr/bin/env python3
"""
Independent exact verifier for the public per-term connected-constant archives.

Deliberately does not import upstream tally/polytope code.  It parses only the
frozen text archives, enforces uniqueness/completeness of term indices, sums
signed values with Fraction, and checks the three target constants.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, re, sys

UP=Path(__file__).resolve().parents[1]/"upstream"/"gpu"/"exact"
PAT=re.compile(r"term\s+(\d+)\s+sign\s+(-?\d+)\s+value\s+(\S+)")

EXPECTED_SHA={
 "exact_42.txt":"a2326b672f541aa0678f74820a36f762fafa6283",
 "exact_c5.txt":"b4bfd254b86c4d2bf4101511f3201cd6e05d6f33",
 "exact_c6.txt":"1eaa0f3799c22be7367ebc89eeb715111acf2ed3",
}

def blob_sha(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def parse_cycle(path,n):
    vals={}
    for ln in path.read_text().splitlines():
        m=PAT.search(ln)
        if not m: continue
        i=int(m.group(1)); s=int(m.group(2)); v=F(m.group(3))
        if i in vals:
            raise AssertionError(f"duplicate term {i} in {path.name}")
        assert s in (-1,1)
        vals[i]=s*v
    assert set(vals)==set(range(n)), (path.name,len(vals),sorted(set(range(n))-set(vals))[:20])
    return sum(vals.values(),F(0)),vals

def parse_42(path):
    vals={1:{},2:{},3:{}}
    classpat=re.compile(r"poly\s+42\['([123])'")
    for ln in path.read_text().splitlines():
        cm=classpat.search(ln); m=PAT.search(ln)
        if not cm or not m: continue
        d=int(cm.group(1)); i=int(m.group(1)); s=int(m.group(2)); v=F(m.group(3))
        if i in vals[d]: raise AssertionError(f"duplicate class {d} term {i}")
        assert s in (-1,1)
        vals[d][i]=s*v
    out={}
    for d in (1,2,3):
        assert set(vals[d])==set(range(26)), (d,len(vals[d]))
        out[d]=sum(vals[d].values(),F(0))
    return out

def main():
    for name,sha in EXPECTED_SHA.items():
        got=blob_sha(UP/name)
        assert got==sha,(name,got,sha)
        print("blob_sha",name,got,"PASS")

    c5,_=parse_cycle(UP/"exact_c5.txt",150)
    c6,_=parse_cycle(UP/"exact_c6.txt",1082)
    u=parse_42(UP/"exact_42.txt")
    g42=6*u[1]+6*u[2]+3*u[3]

    assert c5==F(1,36)
    assert c6==-F(1,126)
    assert u[1]==-F(2,315)
    assert u[2]==-F(1,1260)
    assert u[3]==-F(1,252)
    assert g42==-F(23,420)

    m5=F(67,12)+c5
    m6=F(39,4)+F(131,420)+F(1,6)+g42+c6
    assert m5==F(101,18)
    assert m6==F(12809,1260)

    print("U1 =",u[1])
    print("U2 =",u[2])
    print("U3 =",u[3])
    print("{4,2} =",g42)
    print("C5 =",c5)
    print("{6} =",c6)
    print("m5 =",m5)
    print("m6 =",m6)
    print("RESULT: INDEPENDENT_ARCHIVE_SUM_PASS")

if __name__=="__main__":
    main()
