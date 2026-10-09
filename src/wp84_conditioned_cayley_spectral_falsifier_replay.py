#!/usr/bin/env python3
"""Independent Fraction replay of the conditioned Cayley spectral falsifier."""
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CERT=ROOT/"notes/WP84_CONDITIONED_CAYLEY_SPECTRAL_FALSIFIER_CERTIFICATE.json"
def need(ok:bool,msg:str)->None:
    if not ok: raise AssertionError(msg)
def frac(s:str)->F: return F(s)
def p(x:F)->F:
    return (F(12502645)*x**6-F(82863712)*x**5+F(221347891)*x**4-F(303496416)*x**3+F(224073135)*x**2-F(84028544)*x+F(12502001))/(F(12500000)*(x*x+1)**3)
def raw(atoms,k): return sum(w*x**k for w,x in atoms)

def main()->None:
    c=json.loads(CERT.read_text(encoding="utf-8"))
    need(c["schema"]=="wp84-conditioned-cayley-spectral-falsifier-v1","schema")
    need(c["decision"]=="MOMENT_ONLY_ROUTE_KILLED_BY_EXACT_ABSTRACT_SPECTRUM","decision")
    need(c["consumer"]["threshold"]=="21/200","threshold")
    A2=((F(1,4),F(0)),(F(3,4),F(4,3)))
    need([raw(A2,k) for k in range(3)]==[F(1),F(1),F(4,3)],"certified moments m0-m2")
    e2=sum(w*p(x) for w,x in A2)
    need(e2==F(48861622601,195312500000),"primary exact energy")
    need(e2-F(21,200)==F(28353810101,195312500000)>0,"primary strict excess")
    need([p(x) for _,x in A2]==[F(12502001,12500000),F(34241593,195312500000)],"atom energies")
    # Matrix realization also meets the rank-six consumer's inherited
    # displacement-rank ceiling (indeed rank zero), without claiming source law.
    eig=[F(0),F(4,3),F(4,3),F(4,3)]
    need(sum(eig)/4==1 and sum(x*x for x in eig)/4==F(4,3),"finite matrix moments")
    need(len({eig[i] for i in range(4)})==2,"diagonal finite spectrum")
    A3=((F(1,54),F(-2)),(F(26,27),F(1)),(F(1,54),F(4)))
    need([raw(A3,k) for k in range(4)]==[F(1),F(1),F(4,3),F(2)],"optional m3 stress moments")
    e3=sum(w*p(x) for w,x in A3)
    need(e3==F(2921277517807,23029687500000),"optional m3 stress energy")
    need(e3>F(21,200),"optional m3 stress excess")
    need(c["scope"]["strict_gt79"]=="OPEN","theorem status")
    need("No counterexample to the actual zeta spectrum" in c["scope"]["not_proved"],"source boundary")
    print("PASS: exact rational Cayley energy and both finite-atomic moment checks.")
    print("Primary excess over 0.105 =",e2-F(21,200))
    print("Optional m3=2 excess =",e3-F(21,200))
    print("ABSTRACT MOMENT-ONLY ROUTE FALSIFIED; source-specific theorem remains open.")

if __name__=="__main__": main()
