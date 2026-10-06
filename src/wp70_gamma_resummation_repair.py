#!/usr/bin/env python3
"""
Repair audit for the public gamma-resummation helper.

Public source identity:
  JoshuaHKU/zeta-0.7947-reproduction
  d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8

The public helper mains_envelope.py defines
    gamma_d = sum_e mu(e) beta_{d e}
and attempts a multiplicative local formula.

For a multiplicative beta_q and squarefree e,
    gamma_d = prod_p [ beta_p(v_p(d)) - beta_p(v_p(d)+1) ].

The old helper starts from the generic odd-prime product C2, but when an odd
prime divides BOTH d and 2*b1*b2 it fails to remove the generic local factor
before inserting the special one.  It also needs the p=2 local factor even
when 2 does not divide b1*b2 or d; in the generic odd-odd case that factor is
zero and forces odd d to vanish.

This script compares:
  * the public helper formula;
  * the corrected Euler-local formula;
  * a direct finite Möbius convolution gamma_d = sum_{e<=E} mu(e) beta_{de}
    for spot checks;
  * the full finite-j kernel from the public Sieves implementation.

The goal is to test the algebraic identity, not to claim an asymptotic theorem.
"""

from __future__ import annotations

import argparse, math, sys
from pathlib import Path
import numpy as np

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--upstream", required=True)
    ap.add_argument("--D", type=int, default=4000)
    ap.add_argument("--J", type=int, default=20000)
    args=ap.parse_args()

    up=Path(args.upstream).resolve()
    sys.path.insert(0,str(up/"scripts"))
    from m1_suite import (
        Sieves, C2_TWIN, g0_sawtooth, prime_factors, vp_int
    )
    import mains_envelope as old

    D=args.D
    J=args.J

    def beta_loc(p,a,e1,e2):
        f=1.0
        for ei in (e1,e2):
            ai=max(a-ei,0)
            if ai>=2:
                return 0.0
            if ai==1:
                f *= -1.0/(p-1)
        return f

    def generic_odd(p):
        return 1.0 - 1.0/(p-1)**2

    def gamma_fixed(d,b1,b2):
        # Baseline product over every odd prime in the generic (e1=e2=v=0)
        # state.  Replace that baseline at every odd prime that is special
        # because it divides d or b1*b2.
        val=float(C2_TWIN)
        ps=set(prime_factors(d)) | set(prime_factors(b1)) | set(prime_factors(b2))
        for p in sorted(ps):
            if p==2:
                continue
            e1,e2=vp_int(b1,p),vp_int(b2,p)
            v=vp_int(d,p)
            loc=beta_loc(p,v,e1,e2)-beta_loc(p,v+1,e1,e2)
            val *= loc/generic_odd(p)

        # p=2 is excluded from C2_TWIN and must always be inserted.
        p=2
        e1,e2=vp_int(b1,p),vp_int(b2,p)
        v=vp_int(d,p)
        loc2=beta_loc(p,v,e1,e2)-beta_loc(p,v+1,e1,e2)
        val *= loc2
        return val

    def mu(n):
        if n==1: return 1
        r=1
        for p in prime_factors(n):
            if n%(p*p)==0:
                return 0
            r=-r
        return r

    def phi(n):
        out=n
        for p in prime_factors(n):
            out=out//p*(p-1)
        return out

    def beta_q(q,b1,b2):
        q1=q//math.gcd(q,b1)
        q2=q//math.gcd(q,b2)
        m1,m2=mu(q1),mu(q2)
        if m1==0 or m2==0:
            return 0.0
        return m1*m2/(phi(q1)*phi(q2))

    # Direct Möbius-convolution spot check.  Because beta_{de} vanishes once
    # local exponents exceed the allowed range, a modest squarefree support is
    # enough for the chosen small d,b pairs; we report convergence at E.
    def gamma_direct(d,b1,b2,E=200000):
        s=0.0
        for e in range(1,E+1):
            me=mu(e)
            if me:
                s += me*beta_q(d*e,b1,b2)
        return s

    pairs=[(2,2),(2,3),(3,5),(5,5),(7,11)]
    print("=== local coefficient spot checks ===")
    for b1,b2 in pairs:
        for d in [1,2,3,5,6,10,15,30]:
            gf=gamma_fixed(d,b1,b2)
            go=old.gamma_d(d,b1,b2,C2_TWIN)
            gd=gamma_direct(d,b1,b2,20000)
            print(
                f"pair=({b1},{b2}) d={d:2d} "
                f"old={go:+.8e} fixed={gf:+.8e} directE20k={gd:+.8e} "
                f"|fixed-direct|={abs(gf-gd):.3e}"
            )

    sv=Sieves(J)
    thetas=np.array([0.02,0.035,0.06,0.10,0.17,0.30,0.55,1.0,1.7,2.8])
    print("\n=== kernel identity comparison ===")
    worst_old=0.0
    worst_fixed=0.0
    summary=[]
    for b1,b2 in pairs:
        sarr=sv.s_array(b1,b2)
        g_old={d:old.gamma_d(d,b1,b2,C2_TWIN) for d in range(1,D+1)}
        g_fix={d:gamma_fixed(d,b1,b2) for d in range(1,D+1)}
        g_old={d:g for d,g in g_old.items() if g}
        g_fix={d:g for d,g in g_fix.items() if g}

        errs_old=[]
        errs_fix=[]
        scales=[]
        j=np.arange(1,J+1)
        for t in thetas:
            row=(np.sin(2*t*j)-np.sin(t*j))/j
            gex=2*float(np.dot(sarr[1:J+1],row))
            gold=sum(g*float(g0_sawtooth(np.array([d*t]))[0]) for d,g in g_old.items())
            gfix=sum(g*float(g0_sawtooth(np.array([d*t]))[0]) for d,g in g_fix.items())
            errs_old.append(abs(gold-gex))
            errs_fix.append(abs(gfix-gex))
            scales.append(max(abs(gex),1e-12))

        ro=max(e/s for e,s in zip(errs_old,scales))
        rf=max(e/s for e,s in zip(errs_fix,scales))
        ao=max(errs_old)
        af=max(errs_fix)
        worst_old=max(worst_old,ro)
        worst_fixed=max(worst_fixed,rf)
        summary.append((b1,b2,ao,af,ro,rf))
        print(
            f"pair=({b1},{b2}) max_abs old={ao:.3e} fixed={af:.3e} "
            f"max_rel old={ro:.3e} fixed={rf:.3e}"
        )

    # Structural checks implied by the exact local product.
    for b1,b2 in [(3,5),(5,5),(7,11)]:
        # odd b1,b2 => generic p=2 local factor kills odd d
        assert all(abs(gamma_fixed(d,b1,b2)) < 1e-15 for d in range(1,100,2))

    # Require a meaningful improvement on each pair where the old helper was
    # known to misbehave.  We do NOT require zero residual because D,J finite.
    bad_pairs={(2,3),(3,5),(5,5)}
    for b1,b2,ao,af,ro,rf in summary:
        if (b1,b2) in bad_pairs:
            assert af < ao/2, (b1,b2,ao,af)

    print("worst_relative_old =",worst_old)
    print("worst_relative_fixed =",worst_fixed)
    print("RESULT: GAMMA_EULER_LOCAL_REPAIR_DIAGNOSTIC_PASS")

if __name__=="__main__":
    main()
