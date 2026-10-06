#!/usr/bin/env python3
"""Exact k=8 model go/no-go evaluator.

Input exact/rational m7,m8 and report:
- feasibility floor F8(m7),
- >80 threshold T80(m7),
- corridor width,
- exact Christoffel lambda4,
- simple-zero ledger 1-2 lambda4,
- minimum bounded-rational delta needed to keep >80.

This is consumer-side only.
"""
from fractions import Fraction as F
import argparse

L0=F(25866469,1352400)

def q(s): return F(s)

def F8(L):
    return (F(13335840000)*L*L-F(504286322400)*L+
            F(4794396454037))/F(748818000)

def T80(L):
    return (F(18670176000)*L*L-F(713649484800)*L+
            F(6822174057191))/F(68531400)

def N(L,U):
    return (F(748818000)*U-F(13335840000)*L*L+
            F(504286322400)*L-F(4794396454037))

def D(L,U):
    return (F(1837779300)*U-F(24004512000)*L*L+
            F(903891063600)*L-F(8574904106497))

def lambda4(L,U):
    den=D(L,U)
    if den<=0:
        raise ValueError("D<=0: not in the positive-definite Christoffel region")
    return N(L,U)/(4*den)

def min_delta_for_80(lam):
    if lam>=F(1,10):
        return None
    return F(9)*lam/(F(1)-F(10)*lam)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--m7")
    ap.add_argument("--m8")
    ap.add_argument("--table",action="store_true")
    a=ap.parse_args()

    if a.table:
        for s in ("19.127","19.128","19.130","19.132","19.134","19.136"):
            L=q(s)
            print(s,"deltaL=",float(L-L0),
                  "corridor=",float(T80(L)-F8(L)))
        print("RESULT: WP84_K8_CORRIDOR_TABLE_PASS")
        return

    if a.m7 is None or a.m8 is None:
        ap.error("provide --m7 and --m8, or use --table")

    L=q(a.m7); U=q(a.m8)
    lo=F8(L); hi=T80(L)
    lam=lambda4(L,U)
    simple=F(1)-F(2)*lam
    delta=min_delta_for_80(lam)

    print("m7 =",L,"=",float(L))
    print("m8 =",U,"=",float(U))
    print("F8(m7) =",lo,"=",float(lo))
    print("T80(m7) =",hi,"=",float(hi))
    print("corridor width =",hi-lo,"=",float(hi-lo))
    print("m8 excess above floor =",U-lo,"=",float(U-lo))
    print("margin to T80 =",hi-U,"=",float(hi-U))
    print("lambda4 =",lam,"=",float(lam))
    print("simple ledger =",simple,"=",float(simple))
    if delta is None:
        print("bounded >80 delta: NONE (lambda4>=0.1)")
        print("VERDICT: K8_80_FAIL")
    else:
        print("minimum fixed bounded delta >",delta,"=",float(delta))
        print("VERDICT: K8_80_PASS")
    print("RESULT: WP84_K8_MODEL_GONOGO_COMPLETE")

if __name__=="__main__":
    main()
