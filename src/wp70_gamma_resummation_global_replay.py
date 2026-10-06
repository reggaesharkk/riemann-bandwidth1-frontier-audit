#!/usr/bin/env python3
"""Global replay of public env_gamma after correcting its Euler-local gamma_d."""

from __future__ import annotations
import argparse, sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("T",type=float)
    ap.add_argument("--upstream",required=True)
    ap.add_argument("--D-eval",type=int,default=400)
    ap.add_argument("--D-tail",type=int,default=4000)
    a=ap.parse_args()

    up=Path(a.upstream).resolve()
    sys.path.insert(0,str(up/"scripts"))
    import mains_envelope as me
    from m1_suite import C2_TWIN, prime_factors, vp_int

    def beta_loc(p,x,e1,e2):
        f=1.0
        for ei in (e1,e2):
            ai=max(x-ei,0)
            if ai>=2:
                return 0.0
            if ai==1:
                f *= -1.0/(p-1)
        return f

    def generic_odd(p):
        return 1.0-1.0/(p-1)**2

    def gamma_fixed(d,b1,b2,base_odd=None):
        # base_odd arg retained for drop-in API compatibility.
        val=float(C2_TWIN)
        ps=set(prime_factors(d)) | set(prime_factors(b1)) | set(prime_factors(b2))
        for p in sorted(ps):
            p=int(p)
            if p==2:
                continue
            v=vp_int(d,p)
            e1,e2=vp_int(b1,p),vp_int(b2,p)
            loc=beta_loc(p,v,e1,e2)-beta_loc(p,v+1,e1,e2)
            val *= loc/generic_odd(p)
        p=2
        v=vp_int(d,2)
        e1,e2=vp_int(b1,2),vp_int(b2,2)
        val *= beta_loc(2,v,e1,e2)-beta_loc(2,v+1,e1,e2)
        return val

    me.gamma_d=gamma_fixed
    ev,tb,rep=me.env_gamma(a.T,D_EVAL=a.D_eval,D_TAIL=a.D_tail)
    print("T =",a.T)
    print("D_eval =",a.D_eval)
    print("D_tail =",a.D_tail)
    for pair,e,sc in rep:
        print("identity",pair,"abs_error",e,"scale",sc,"relative",e/max(sc,1e-300))
    print("signed_eval =",ev)
    print("finite_omitted_tail_bound =",tb)
    print("global_envelope =",abs(ev)+tb)
    print("RESULT: CORRECTED_GAMMA_GLOBAL_REPLAY_COMPLETE")

if __name__=="__main__":
    main()
