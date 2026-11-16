#!/usr/bin/env python3
"""Numerical regression for the continuous spread-Dirichlet identity."""
import numpy as np

def interval_for_word(L, ys):
    ps=[0.0]
    for y in ys:
        ps.append(ps[-1]+y)
    lo=-L/2-min(ps)
    hi= L/2-max(ps)
    # Depending on shift convention, translating x by partial sums requires
    # x+p_j in I.  Intersection:
    lo=max(-L/2-p for p in ps)
    hi=min( L/2-p for p in ps)
    return ps,lo,hi

def direct_diag(L,d,ys):
    ps,lo,hi=interval_for_word(L,ys)
    if hi<=lo:
        return 0j
    Y=sum(ys)
    vals=[]
    for k in range(d):
        # <e_k, T_Y e_k> on surviving x interval.
        vals.append((hi-lo)/L*np.exp(1j*2*np.pi*k*Y/L))
    return sum(vals)/d

def formula(L,d,ys):
    ps=[0.0]
    for y in ys:
        ps.append(ps[-1]+y)
    R=max(ps)-min(ps)
    O=max(0.0,1-R/L)
    Y=ps[-1]
    D=sum(np.exp(1j*2*np.pi*np.arange(d)*Y/L))/d
    return O*D

def main():
    cases=[
        [1.2,-0.7,-0.5],   # closed
        [1.2,-0.7,-0.4],   # small leakage
        [3.0,-1.1,0.2],
        [-2.2,0.4,1.1],
    ]
    L=10.0
    d=37
    for ys in cases:
        a=direct_diag(L,d,ys)
        b=formula(L,d,ys)
        err=abs(a-b)
        print(ys,a,b,err)
        assert err<1e-13
    print("RESULT: WP84_CONTINUOUS_SPREAD_DIRICHLET_PASS")

if __name__=="__main__":
    main()
