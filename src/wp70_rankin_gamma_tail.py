#!/usr/bin/env python3
"""
Rankin/Euler-product upper bound for the omitted d>DCAP part of the
paper's gamma-resummed singular-series tail.

Key identity:
  gamma_d(b1,b2) = product_p f_p(v_p(d)),
  f_p(v) = beta_p(v)-beta_p(v+1).

Hence for sigma in (0,1),
  sum_d d^sigma |gamma_d| = product_p L_p(sigma),
  L_p = sum_v |f_p(v)| p^(sigma v),
and
  sum_{d>D} |gamma_d| <= D^(-sigma) product_p L_p(sigma).

For generic p not dividing 2*b1*b2, beta_p(0)=1,
beta_p(1)=1/(p-1)^2, beta_p(v>=2)=0, so
  L_p = 1 + (p^sigma-1)/(p-1)^2   (p>2),
while p=2 is handled by the same finite local rule.

All pair dependence is therefore a finite correction to one generic Euler
product.  This script uses sigma=1/2 so the only irrational local operation is
sqrt, evaluated at high precision.  The uncomputed generic prime product
above PRIME_CUTOFF is bounded by all integers:
  log prod_{p>Q} L_p <= sum_{n>Q} 4 n^(-3/2) <= 8/sqrt(Q).
That inequality is intentionally crude but rigorous in shape.

The finite d<=D coefficients are still imported from the public float helper,
so this is a theorem-shaped *tail closure diagnostic*, not yet an all-rational
certificate.  If the margin is sufficient, the next pass exactifies those
finite coefficients and quadrature.
"""
from __future__ import annotations
import argparse, math, sys
from pathlib import Path
import numpy as np
import mpmath as mp

UP=Path(__file__).resolve().parents[1]/"upstream"/"scripts"
sys.path.insert(0,str(UP))
from m1_suite import primepowers, prime_factors, vp_int
from tail_bound import gamma_signed_array, _gamma_free_exact, mu, class_split, beta_q

TWO_PI=2*math.pi
LOG2=math.log(2.0)
C_SAW=2.10
SIGMA=mp.mpf('0.5')
PRIME_CUTOFF=1_000_000

def primes_upto(n):
    s=bytearray(b"\x01")*(n+1)
    s[0:2]=b"\x00\x00"
    r=int(n**0.5)
    for p in range(2,r+1):
        if s[p]:
            s[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if s[i]]

def beta_loc(p,a,e1,e2):
    z=mp.mpf(1)
    for e in (e1,e2):
        aa=max(a-e,0)
        if aa>=2:
            return mp.mpf(0)
        if aa==1:
            z *= -mp.mpf(1)/(p-1)
    return z

def local_L(p,e1,e2):
    vmax=max(e1,e2)+2
    z=mp.mpf(0)
    ps=mp.sqrt(p)
    for v in range(vmax+1):
        f=beta_loc(p,v,e1,e2)-beta_loc(p,v+1,e1,e2)
        if f:
            z += abs(f)*(ps**v)
    return z

def generic_product_upper():
    mp.mp.dps=60
    logp=mp.mpf(0)
    for p in primes_upto(PRIME_CUTOFF):
        L=local_L(p,0,0)
        logp += mp.log(L)
    # For n>Q>=2:
    # (sqrt(n)-1)/(n-1)^2 <= sqrt(n)/(n/2)^2 = 4 n^(-3/2).
    # log(1+x)<=x and sum_{n>Q} n^-3/2 <= int_Q^inf x^-3/2 dx.
    rem=mp.mpf(8)/mp.sqrt(PRIME_CUTOFF)
    return mp.e**(logp+rem), rem

GENERIC_UPPER, GENERIC_LOG_REM = generic_product_upper()

def rankin_pair_tail(b1,b2,D):
    val=GENERIC_UPPER
    for p in sorted(prime_factors(2*b1*b2)):
        p=int(p)
        val *= local_L(p,vp_int(b1,p),vp_int(b2,p))/local_L(p,0,0)
    return val/mp.sqrt(D)

def finite_tail_coeff_l1(b1,b2,P,D):
    g=gamma_signed_array(D,b1,b2).copy()
    for d in range(1,min(P,D)+1):
        gg=_gamma_free_exact(d,b1,b2)
        for e in range(1,P//d+1):
            q=d*e
            if mu(e)!=0 and not class_split(q,b1,b2):
                gg -= mu(e)*beta_q(q,b1,b2)
        g[d]=gg
    return float(np.sum(np.abs(g[1:])))

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

def reconstruct(T,P=40,D=20000,density=320):
    X=int(T/TWO_PI)
    l=math.log(T/TWO_PI)
    ell1=l+2*LOG2-1
    norm4=l*X*ell1**4
    thmin=4*math.pi**2/T
    th=np.exp(np.linspace(math.log(thmin),math.log(200.0),
                          int(math.log(200.0/thmin)*density)+2))
    om=np.log(TWO_PI/th)
    pp,lw=primepowers(X)
    total=0.0
    max_rankin=(0,None)
    npair=0
    for i in range(len(pp)):
        for k in range(i,len(pp)):
            b1,b2=int(pp[i]),int(pp[k])
            w=lw[i]*lw[k]/(b1*b2)
            sel=th<=T/max(b1,b2)**2
            sel &= (min(b1,b2)>=TWO_PI/th) | (th>=TWO_PI)
            if not sel.any(): continue
            ths=th[sel]
            q=qvec(l,om,math.log(b1),math.log(b2))[sel]
            if b1!=b2:
                q=q+qvec(l,om,math.log(b2),math.log(b1))[sel]
            if not q.any(): continue
            npair+=1
            finite=finite_tail_coeff_l1(b1,b2,P,D)
            rank=float(rankin_pair_tail(b1,b2,D))
            if rank>max_rankin[0]: max_rankin=(rank,(b1,b2,finite))
            amp=C_SAW*(finite+rank)
            total += w*T*np.trapezoid(amp*np.abs(q)/ths**2,ths)
    return {
      "T":T,"P":P,"D":D,"pairs":npair,
      "generic_rankin_moment_upper":str(GENERIC_UPPER),
      "generic_uncomputed_log_product_bound":str(GENERIC_LOG_REM),
      "max_pair_rankin_tail":max_rankin,
      "rankin_closed_tail_charge_factor1":total/(math.pi*norm4),
      "quoted_target":0.0115 if int(T)==2400 else (0.0111 if int(T)==4800 else None),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("T",type=float)
    ap.add_argument("--P",type=int,default=40)
    ap.add_argument("--D",type=int,default=20000)
    a=ap.parse_args()
    r=reconstruct(a.T,a.P,a.D)
    for k,v in r.items(): print(k,"=",v)

if __name__=="__main__":
    main()
