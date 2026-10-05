#!/usr/bin/env python3
"""Exact calculus / finite-rank bookkeeping gate for beta quarantine."""
import sympy as sp

def main():
    s=sp.symbols("s", real=True)
    val=2*sp.integrate(s*(1-s)**2,(s,0,1))
    assert sp.simplify(val-sp.Rational(1,6))==0

    x=sp.symbols("x", real=True)
    r2=1-((x-1)**2/(x**2+1))**2
    dr=sp.factor(sp.diff(r2,x))
    target=-4*(x-1)**3*(x+1)/(x**2+1)**3
    assert sp.simplify(dr-target)==0

    # Critical points are -1 and 1; endpoint limits are zero.
    vals=[
        sp.limit(r2,x,-sp.oo),
        sp.simplify(r2.subs(x,-1)),
        sp.simplify(r2.subs(x,1)),
        sp.limit(r2,x,sp.oo),
    ]
    assert vals==[0,-3,1,0],vals
    TV=abs(vals[1]-vals[0])+abs(vals[2]-vals[1])+abs(vals[3]-vals[2])
    assert TV==8

    print("beta square-mass limit =",val)
    print("r2 derivative =",dr)
    print("r2 extrema/endpoints =",vals)
    print("total variation =",TV)
    print("RESULT: WP84_R2_BETA_QUARANTINE_PASS")

if __name__=="__main__":
    main()
