#!/usr/bin/env python3
"""WP71 G9-B local-factor identity for the signed welding main term.

Let e1=v_p(b1), e2=v_p(b2), e=min(e1,e2),
a=e1-e=v_p(r), b=e2-e=v_p(q), where
r=b1/gcd(b1,b2), q=b2/gcd(b1,b2).

Let kappa_p(e1,e2;v) be the public local density and
tau_p(v)=kappa_p(0,0;v) the ordinary prime-pair local factor.

For the p-adic valuation V of a uniformly random integer,
P(V=v)=(1-1/p)p^{-v}, this script proves exactly

 E[kappa_p(e1,e2;V)^2]
   = p^e E[tau_p(V+a) tau_p(V+b)].

Consequently, multiplying over primes,

 E_j S_{b1,b2}(j)^2
   = gcd(b1,b2) * E_k S(rk) S(qk),

at the Euler-product/main-term level.

Pure Fraction arithmetic; no numerical approximation.
"""
from fractions import Fraction as F

def kappa(p,e1,e2,v):
    p=F(p)
    if e1==0 and e2==0:
        return 1+1/(p-1) if v>0 else 1-1/(p-1)**2
    if min(e1,e2)==0:
        return F(0) if v>0 else p/(p-1)
    e=min(e1,e2)
    if e1==e2:
        if v<e:
            return F(0)
        if v==e:
            return p**e*(1-1/(p-1)**2)
        return p**e*(1+1/(p-1))
    return p**e*p/(p-1) if v==e else F(0)

def geom_expect(p,func,stable_from):
    """Exact geometric expectation once func is constant for v>=stable_from."""
    p=F(p)
    tot=F(0)
    for v in range(stable_from):
        tot+=(1-F(1,p))*F(1,p**v)*func(v)
    # P(V>=stable_from)=p^{-stable_from}.
    tot+=F(1,p**stable_from)*func(stable_from)
    return tot

def lhs(p,e1,e2):
    s=max(e1,e2)+2
    return geom_expect(p,lambda v:kappa(p,e1,e2,v)**2,s)

def rhs(p,e1,e2):
    e=min(e1,e2)
    a=e1-e; b=e2-e
    s=2
    return F(p)**e*geom_expect(
        p,
        lambda v:kappa(p,0,0,v+a)*kappa(p,0,0,v+b),
        s,
    )

def main():
    checked=0
    for p in (2,3,5,7,11,13,17,19,23,29,31):
        for e1 in range(5):
            for e2 in range(5):
                L=lhs(p,e1,e2)
                R=rhs(p,e1,e2)
                assert L==R,(p,e1,e2,L,R)
                checked+=1
    print("exact local cases checked =",checked)
    print("RESULT: WP71_G9_B_LOCAL_FACTOR_IDENTITY_PASS")

if __name__=="__main__":
    main()
