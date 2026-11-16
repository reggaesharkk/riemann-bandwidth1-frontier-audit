#!/usr/bin/env python3
"""
Reconstruct the tail charge stated in the public paper from the *actual*
Lemma E3 uniform sawtooth bound, rather than the separate F-E3c Abel/V
diagnostic in tail_bound.py.

This is a diagnostic reconstruction, not yet a rigorous enclosure.  It keeps
the public finite-height geometry and gamma machinery pinned by the workflow,
then compares the two natural normalization conventions:

    |sum_j tail_P(j) row_j(theta)| <= C_saw * sum_d |gamma_d^{>P}|

and, because mains_envelope.py forms the even j-sum with an explicit factor 2,
also the doubled version.

The d>DCAP remainder uses the same empirical 'double the upper half' rule as
the public helper only as a convergence diagnostic.  A theorem-grade run must
replace that with a proved Euler-product tail estimate.
"""
from __future__ import annotations
import argparse, math, sys
from pathlib import Path
import numpy as np

UP = Path(__file__).resolve().parents[1] / "upstream" / "scripts"
sys.path.insert(0, str(UP))

from m1_suite import primepowers
from tail_bound import (
    gamma_signed_array, _gamma_free_exact, mu, class_split, beta_q,
)

TWO_PI=2*math.pi
LOG2=math.log(2.0)
C_SAW=2.10

def tail_gamma_abs(b1,b2,P,DCAP):
    g=gamma_signed_array(DCAP,b1,b2).copy()
    # gamma^{>P}: gamma_free already excludes the Dbar/class part.
    # Remove the explicitly retained non-class q<=P oscillating modes.
    for d in range(1,min(P,DCAP)+1):
        gg=_gamma_free_exact(d,b1,b2)
        for e in range(1,P//d+1):
            q=d*e
            if mu(e)!=0 and not class_split(q,b1,b2):
                gg -= mu(e)*beta_q(q,b1,b2)
        g[d]=gg
    main=float(np.sum(np.abs(g[1:])))
    upper_half=float(np.sum(np.abs(g[DCAP//2:])))
    # convergence-only tail proxy copied in spirit from the public helper.
    with_proxy=main+2.0*upper_half
    return main,upper_half,with_proxy

def qvec(l,om,be1,be2):
    m1_,m2_=l+om-be1,l+om-be2
    def o4v(a,b,c):
        z=np.zeros_like(a)
        mx=np.maximum.reduce([z,a,b,c])
        mn=np.minimum.reduce([z,a,b,c])
        return np.clip(l-(mx-mn),0,None)
    tot=np.zeros_like(om)
    for u1,u3 in ((be1+0*om,m1_),(m1_,be1+0*om)):
        for u2,u4 in ((be2+0*om,m2_),(m2_,be2+0*om)):
            de=u1+u3-u2-u4
            tot += (o4v(-u1+de,u3-u4,-u4)
                    +o4v(u2-u3-u4,-u3-u4,-u4)
                    +o4v(-u2-u3+u4,-u3+u4,u4))
    return tot

def reconstruct(T,P=40,DCAP=20000,theta_density=320):
    X=int(T/TWO_PI)
    l=math.log(T/TWO_PI)
    ell1=l+2*LOG2-1
    norm4=l*X*ell1**4
    thmin=4*math.pi**2/T
    th=np.exp(np.linspace(math.log(thmin),math.log(200.0),
                          int(math.log(200.0/thmin)*theta_density)+2))
    om=np.log(TWO_PI/th)
    pp,lw=primepowers(X)

    total1=total2=0.0
    npair=0
    sums=[]
    for i in range(len(pp)):
        for k in range(i,len(pp)):
            b1,b2=int(pp[i]),int(pp[k])
            w=lw[i]*lw[k]/(b1*b2)
            sel=th <= T/max(b1,b2)**2
            sel &= (min(b1,b2)>=TWO_PI/th) | (th>=TWO_PI)
            if not sel.any():
                continue
            ths=th[sel]
            q=qvec(l,om,math.log(b1),math.log(b2))[sel]
            if b1!=b2:
                q=q+qvec(l,om,math.log(b2),math.log(b1))[sel]
            if not q.any():
                continue
            npair+=1
            s,half,sproxy=tail_gamma_abs(b1,b2,P,DCAP)
            sums.append((sproxy,b1,b2,s,half))
            amp=C_SAW*sproxy
            integ=w*T*np.trapezoid(amp*np.abs(q)/ths**2,ths)
            total1 += integ
            total2 += 2.0*integ
    z=math.pi*norm4
    sums.sort(reverse=True)
    return {
      "T":T,"P":P,"DCAP":DCAP,"pairs":npair,
      "paper_lemma_tail_factor1":total1/z,
      "paper_lemma_tail_factor2_even_sum":total2/z,
      "largest_gamma_abs_pairs":sums[:12],
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("T",type=float)
    ap.add_argument("--P",type=int,default=40)
    ap.add_argument("--DCAP",type=int,default=20000)
    a=ap.parse_args()
    r=reconstruct(a.T,a.P,a.DCAP)
    for k,v in r.items():
        print(k,"=",v)
    print("quoted_target =",0.0115 if int(a.T)==2400 else (0.0111 if int(a.T)==4800 else None))

if __name__=="__main__":
    main()
