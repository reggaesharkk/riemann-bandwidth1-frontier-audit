#!/usr/bin/env python3
"""
Tighter Rankin closure for d>D with sigma=2/3, including the finite
special-prime "class" correction present in gamma^free.

This remains a diagnostic because d<=D coefficients and theta quadrature are
evaluated in float, but the omitted-tail theorem shape is now conservative:

  |gamma_free(d)| <= |gamma_full(d)| + |gamma_class(d)|,

the first tail being Rankin-bounded by an Euler product and the second being
enumerated exactly over its finite special-prime support.
"""
from __future__ import annotations
import argparse, itertools, math, sys
from pathlib import Path
import numpy as np
import mpmath as mp

UP=Path(__file__).resolve().parents[1]/"upstream"/"scripts"
sys.path.insert(0,str(UP))
from m1_suite import primepowers, prime_factors, vp_int
from tail_bound import gamma_signed_array, _gamma_free_exact, mu, class_split, beta_q
from mains_envelope import _beta_loc

TWO_PI=2*math.pi
LOG2=math.log(2.0)
C_SAW=2.10
SIGMA=mp.mpf(2)/3
QPRIME=1_000_000

def primes_upto(n):
    s=bytearray(b"\x01")*(n+1)
    s[0:2]=b"\x00\x00"
    for p in range(2,int(n**0.5)+1):
        if s[p]:
            s[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if s[i]]

def beta_loc_mp(p,a,e1,e2):
    z=mp.mpf(1)
    for e in (e1,e2):
        aa=max(a-e,0)
        if aa>=2: return mp.mpf(0)
        if aa==1: z *= -mp.mpf(1)/(p-1)
    return z

def local_f_mp(p,v,e1,e2):
    return beta_loc_mp(p,v,e1,e2)-beta_loc_mp(p,v+1,e1,e2)

def local_L(p,e1,e2):
    vmax=max(e1,e2)+2
    return mp.fsum(abs(local_f_mp(p,v,e1,e2))*(mp.mpf(p)**(SIGMA*v))
                   for v in range(vmax+1))

def generic_product_upper():
    mp.mp.dps=60
    z=mp.mpf(1)
    for p in primes_upto(QPRIME):
        z *= local_L(p,0,0)
    # generic p>Q: log L_p <= 4 p^(sigma-2);
    # sum over primes <= sum over integers <= 4 Q^(sigma-1)/(1-sigma).
    rem=4*(mp.mpf(QPRIME)**(SIGMA-1))/(1-SIGMA)
    return z*mp.e**rem, rem

GEN,REM=generic_product_upper()

def rankin_full_tail(b1,b2,D):
    z=GEN
    for p in sorted(prime_factors(2*b1*b2)):
        p=int(p)
        z *= local_L(p,vp_int(b1,p),vp_int(b2,p))/local_L(p,0,0)
    return z/(mp.mpf(D)**SIGMA)

def class_correction_tail(b1,b2,D):
    ps=sorted(int(p) for p in prime_factors(2*b1*b2))
    opts=[]
    for p in ps:
        e1,e2=vp_int(b1,p),vp_int(b2,p)
        arr=[]
        for v in range(max(e1,e2)+3):
            f=float(_beta_loc(p,v,e1,e2)-_beta_loc(p,v+1,e1,e2))
            if f!=0.0:
                arr.append((v,f))
        opts.append((p,arr))
    s=0.0
    count=0
    for choice in itertools.product(*[a for _,a in opts]):
        d=1; vc=1.0
        for (p,_),(v,f) in zip(opts,choice):
            d*=p**v; vc*=f
        if d>D and vc!=0.0:
            s += abs(vc); count += 1
    return s,count

def finite_tail_l1(b1,b2,P,D):
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

def reconstruct(T,P=40,D=100000,density=320):
    X=int(T/TWO_PI); l=math.log(T/TWO_PI); ell1=l+2*LOG2-1
    norm4=l*X*ell1**4
    thmin=4*math.pi**2/T
    th=np.exp(np.linspace(math.log(thmin),math.log(200.0),
                          int(math.log(200.0/thmin)*density)+2))
    om=np.log(TWO_PI/th)
    pp,lw=primepowers(X)
    total=0.0; npair=0; worst=(0,None); class_nonzero=0
    for i in range(len(pp)):
        for k in range(i,len(pp)):
            b1,b2=int(pp[i]),int(pp[k])
            w=lw[i]*lw[k]/(b1*b2)
            sel=th<=T/max(b1,b2)**2
            sel &= (min(b1,b2)>=TWO_PI/th) | (th>=TWO_PI)
            if not sel.any(): continue
            ths=th[sel]
            q=qvec(l,om,math.log(b1),math.log(b2))[sel]
            if b1!=b2: q=q+qvec(l,om,math.log(b2),math.log(b1))[sel]
            if not q.any(): continue
            npair+=1
            finite=finite_tail_l1(b1,b2,P,D)
            rt=float(rankin_full_tail(b1,b2,D))
            cc,nc=class_correction_tail(b1,b2,D)
            class_nonzero += nc
            omitted=rt+cc
            if omitted>worst[0]: worst=(omitted,(b1,b2,finite,rt,cc,nc))
            amp=C_SAW*(finite+omitted)
            total += w*T*np.trapezoid(amp*np.abs(q)/ths**2,ths)
    charge=total/(math.pi*norm4)
    return dict(T=T,P=P,D=D,sigma="2/3",pairs=npair,
                generic_moment_upper=str(GEN),
                generic_log_tail_bound=str(REM),
                class_terms_beyond_D=class_nonzero,
                worst_pair_omitted_l1=worst,
                closed_tail_charge_factor1=charge,
                quoted_target=0.0115 if int(T)==2400 else 0.0111 if int(T)==4800 else None)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("T",type=float)
    ap.add_argument("--P",type=int,default=40)
    ap.add_argument("--D",type=int,default=100000)
    a=ap.parse_args()
    for k,v in reconstruct(a.T,a.P,a.D).items(): print(k,"=",v)

if __name__=="__main__":
    main()
