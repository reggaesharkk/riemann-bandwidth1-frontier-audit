#!/usr/bin/env python3
"""Exact-rational regression for the cross-scale Brownian reference."""

from fractions import Fraction as F
from itertools import combinations

import wp84_phi4_balanced_nonclosed_nonpositive as nc

Z=F(0); O=F(1)

def amp(v):
    return nc.overlap(nc.WALK,v)*nc.B4(v)

def six_words(s,t,x,y):
    base=[x,s-x,-y,-(t-y)]
    out=Z
    for pos in combinations(range(4),2):
        P=set(pos)
        ip=iter([0,1]); im=iter([2,3])
        order=[]
        for k in range(4):
            order.append(next(ip) if k in P else next(im))
        out += amp(tuple(base[j] for j in order))
    return out

def ref_g(s,t,x,y):
    cs=s-1; ct=t-1
    rs=min(x,s-x); rt=min(y,t-y)
    gap=max(Z,min(rs,rt)-max(cs,ct))
    return 2*min(cs,ct)*gap

def rho(s,t):
    d=abs(s-t)
    return min(d,1-d)

def main():
    checked=0
    worst=Z

    # Equal-scale identity and coarse torus-detuning regression.
    for den in (6,8,10):
        scales=[F(i,den) for i in range(den,2*den+1)]
        for s in scales:
            xs=[
                F(j,den)
                for j in range(den+1)
                if s-1<=F(j,den)<=1
            ]
            for x in xs:
                for y in xs:
                    got=six_words(s,s,x,y)
                    want=-ref_g(s,s,x,y)
                    assert got==want,(s,x,y,got,want)

        for s in scales:
            xs=[F(j,den) for j in range(den+1) if s-1<=F(j,den)<=1]
            for t in scales:
                ys=[F(j,den) for j in range(den+1) if t-1<=F(j,den)<=1]
                rr=rho(s,t)
                for x in xs:
                    for y in ys:
                        E=six_words(s,t,x,y)+ref_g(s,t,x,y)
                        if rr==0:
                            assert E==0,(s,t,x,y,E)
                        else:
                            ratio=abs(E)/rr
                            worst=max(worst,ratio)
                            # Regression only; theorem note proves 630.
                            assert ratio<=F(630)

    # PSD check for G on deterministic exact point families.
    pts=[
        (F(6,5),F(1,2)),
        (F(5,4),F(3,5)),
        (F(7,5),F(3,4)),
        (F(3,2),F(4,5)),
        (F(8,5),F(9,10)),
    ]
    G=[[ref_g(*pts[i],*pts[j]) for j in range(len(pts))] for i in range(len(pts))]
    vecs=[
        [F(((3*j+5*k)%11)-5) for j in range(len(pts))]
        for k in range(8)
    ]
    for z in vecs:
        q=sum(z[i]*G[i][j]*z[j] for i in range(len(pts)) for j in range(len(pts)))
        assert q>=0,q

    print("worst sampled |E|/rho =",worst)
    print("RESULT: WP84_CROSS_SCALE_BROWNIAN_REFERENCE_PASS")

if __name__=="__main__":
    main()
