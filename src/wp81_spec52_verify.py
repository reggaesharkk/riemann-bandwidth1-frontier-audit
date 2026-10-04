#!/usr/bin/env python3
"""Independent fail-closed verifier for WP81 exact {5,2} evidence.

The producer is not imported. Every primitive work unit must appear exactly
once: three placement classes times 150 connected C5 terms = 450 rows.
A canonical SHA-256 binds the normalized evidence stream.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from fractions import Fraction as F
from pathlib import Path

RX = re.compile(r"^spec52 d ([123]) term (\d+) sign (-?1) value ([^ ]+) wall ")
EXPECTED = {(d,i) for d in (1,2,3) for i in range(150)}

def fs(x):
    return str(x.numerator) if x.denominator == 1 else "%d/%d" % (x.numerator,x.denominator)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("logs",nargs="+")
    ap.add_argument("--receipt")
    a=ap.parse_args()
    rows={}
    for rawpath in a.logs:
        p=Path(rawpath)
        for raw in p.read_text(encoding="utf-8").splitlines():
            m=RX.match(raw.strip())
            if not m:
                continue
            d,i,sgn=int(m.group(1)),int(m.group(2)),int(m.group(3))
            v=F(m.group(4))
            key=(d,i)
            if key in rows:
                raise SystemExit("duplicate work unit %r" % (key,))
            if key not in EXPECTED:
                raise SystemExit("out-of-range work unit %r" % (key,))
            rows[key]=(sgn,v)
    missing=sorted(EXPECTED-set(rows))
    if missing:
        raise SystemExit("coverage failure: got=%d/450 missing=%r" % (len(rows),missing[:30]))
    U={}
    for d in (1,2,3):
        U[d]=sum((F(rows[(d,i)][0])*rows[(d,i)][1] for i in range(150)),F(0))
    total=F(7)*(U[1]+U[2]+U[3])
    normalized="".join(
        "d=%d\tterm=%d\tsign=%d\tvalue=%s\n" % (d,i,rows[(d,i)][0],fs(rows[(d,i)][1]))
        for d in (1,2,3) for i in range(150)
    ).encode("utf-8")
    rec={
      "schema":"wp81-spec52-independent-verification-receipt-v1",
      "status":"PASS",
      "coverage":{"covered":450,"expected":450,"exact":True},
      "U1":fs(U[1]),"U2":fs(U[2]),"U3":fs(U[3]),
      "spec52":fs(total),"spec52_decimal":float(total),
      "normalized_evidence_sha256":hashlib.sha256(normalized).hexdigest(),
      "source_log_count":len(a.logs),
    }
    out=json.dumps(rec,indent=2,sort_keys=True)
    print(out)
    print("RESULT: WP81_SPEC52_INDEPENDENT_VERIFY_PASS")
    if a.receipt:
        Path(a.receipt).write_text(out+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
