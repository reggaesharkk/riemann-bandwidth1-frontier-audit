#!/usr/bin/env python3
"""WP71 exact p-local coupling for the centered four-point model.

For
    b1*n - b2*m = j,
    m' = m-r*k,  n' = n-q*k,
    g=gcd(b1,b2), r=b1/g, q=b2/g,

define the p-local four-point weight K4_p(k,j) by the exact count of
solutions modulo p^s with all four variables p-units, normalized by
p^s*(1-1/p)^4 exactly as in the public two-point kappa_p convention.

This file proves/checks three facts.

(1) Closed pointwise formula.
(2) j-marginal:
      E_j K4_p(k,j) = tau_p(rk) tau_p(qk).
(3) k-marginal:
      E_k K4_p(k,j) = kappa_p(e1,e2;v_p(j))^2 / p^e,
    e=min(e1,e2).

Thus K4_p is the exact local coupling between the j-side squared lock
singular series and the k-side product of twin singular series.

For e1=e2, the pointwise factor contains genuine cross-lock
coincidences involving j and k.  These disappear only after the relevant
marginal average; they must not be omitted from S4(k,j).

Pure Fraction arithmetic.  A small brute-force modulo-p^(e+1) audit
cross-checks the closed formula on representative cells.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd


def vp(n:int,p:int,cap:int=100)->int:
    if n==0:
        return cap
    n=abs(n); e=0
    while e<cap and n%p==0:
        n//=p; e+=1
    return e


def kap2(p:int,e1:int,e2:int,v:int)->F:
    """Exact public two-point local factor kappa_p."""
    if e1==0 and e2==0:
        return F(p,p-1) if v>0 else F(p*(p-2),(p-1)**2)
    if min(e1,e2)==0:
        return F(0) if v>0 else F(p,p-1)
    e=min(e1,e2)
    if e1==e2:
        if v<e:
            return F(0)
        if v==e:
            return F(p**e)*F(p*(p-2),(p-1)**2)
        return F(p**e)*F(p,p-1)
    return F(p**e)*F(p,p-1) if v==e else F(0)


def tau(p:int,v:int)->F:
    return kap2(p,0,0,v)


def k4_formula(p:int,b1:int,b2:int,k:int,j:int)->F:
    """Closed exact four-point p-local factor."""
    e1,e2=vp(b1,p),vp(b2,p)
    e=min(e1,e2)
    pe=p**e
    if j%pe:
        return F(0)

    g=gcd(b1,b2)
    c=(g//pe)%p
    assert c%p
    J=((j//pe)*pow(c,-1,p))%p
    r,q=b1//g,b2//g
    base=F(p-1,p)**4

    if e1==e2:
        assert r%p and q%p
        a=(r*k)%p
        d=(J*pow(q,-1,p))%p
        # Normalized forbidden offsets of
        # m, m-rk, n, n-qk.
        D=len({0,(-a)%p,d,(d-a)%p})
        return F(p**e)*F(p-D,p)/base

    if e1>e2:
        # r is p-divisible, q is a unit.  The lock fixes m mod p.
        assert r%p==0 and q%p
        if J==0:
            return F(0)
        Dn=1 if (q*k)%p==0 else 2
        return F(p**e)*F(p-Dn,p)/base

    # Symmetric case: q p-divisible, r a unit; the lock fixes n.
    assert q%p==0 and r%p
    if J==0:
        return F(0)
    Dm=1 if (r*k)%p==0 else 2
    return F(p**e)*F(p-Dm,p)/base


def k4_bruteforce(p:int,b1:int,b2:int,k:int,j:int)->F:
    """Direct local count at level p^(e+1), enough for unit support."""
    e=min(vp(b1,p),vp(b2,p))
    P=p**(e+1)
    g=gcd(b1,b2); r,q=b1//g,b2//g
    good=0
    for m in range(P):
        for n in range(P):
            if (b1*n-b2*m-j)%P:
                continue
            if all(x%p for x in (m,m-r*k,n,n-q*k)):
                good+=1
    return F(good,P)/(F(p-1,p)**4)


def marginal_gate(p:int,b1:int,b2:int)->int:
    e1,e2=vp(b1,p),vp(b2,p)
    e=min(e1,e2)
    g=gcd(b1,b2); r,q=b1//g,b2//g
    Jmod=p**(e+1)
    checks=0

    # j-marginal -> product of the two ordinary twin local factors.
    for k in range(p):
        got=sum((k4_formula(p,b1,b2,k,j) for j in range(Jmod)),F(0))/Jmod
        want=tau(p,vp(r*k,p))*tau(p,vp(q*k,p))
        assert got==want,("j marginal",p,b1,b2,k,got,want)
        checks+=1

    # k-marginal -> square of the two-point lock factor, with the
    # common p^e lock-density normalization removed once.
    for j in range(Jmod):
        got=sum((k4_formula(p,b1,b2,k,j) for k in range(p)),F(0))/p
        want=kap2(p,e1,e2,vp(j,p,e+1))**2/F(p**e)
        assert got==want,("k marginal",p,b1,b2,j,got,want)
        checks+=1

    return checks


def generic_cross_gate(p:int,b1:int,b2:int)->int:
    """For p not dividing b1*b2, expose the four coincidence hyperplanes."""
    assert b1%p and b2%p
    L=(b1*b2)//gcd(b1,b2)
    checked=0
    for k in range(p):
        for j in range(p):
            # Cross events in the original integer variables:
            # p|k, p|j, p|(j-Lk), p|(j+Lk).
            events=(
                k%p==0,
                j%p==0,
                (j-L*k)%p==0,
                (j+L*k)%p==0,
            )
            # The exact factor is evaluated independently from the events;
            # this loop records that all pointwise variation occurs on these
            # coincidence loci (for odd p; p=2 has merged +/- loci).
            if p>2 and not any(events):
                # Generic four distinct forbidden residues.
                base=F(p-1,p)**4
                want=F(p-4,p)/base
                assert k4_formula(p,b1,b2,k,j)==want
            checked+=1
    return checked


def main():
    # Representative prime-power / special-prime configurations.
    cells=[]
    for p in (2,3,5,7):
        units=[u for u in (1,2,3,5) if u%p]
        u1=units[0]
        u2=units[-1]
        for e1,e2 in (
            (0,0),(1,0),(0,1),(1,1),(2,1),(1,2),(2,2)
        ):
            cells.append((p,(p**e1)*u1,(p**e2)*u2))

    marginal_checks=0
    brute_checks=0
    for p,b1,b2 in cells:
        marginal_checks+=marginal_gate(p,b1,b2)
        e=min(vp(b1,p),vp(b2,p))
        Pj=p**(e+1)
        # Small target-blind sample of exact direct counts.
        for k in range(min(p,3)):
            for j in range(min(Pj,7)):
                got=k4_bruteforce(p,b1,b2,k,j)
                want=k4_formula(p,b1,b2,k,j)
                assert got==want,("brute",p,b1,b2,k,j,got,want)
                brute_checks+=1

    cross_checks=0
    for p in (3,5,7,11):
        # p-free outer coefficients, deliberately nontrivial gcd patterns.
        for b1,b2 in ((1,1),(2,3),(5,3),(6,10)):
            if b1%p and b2%p:
                cross_checks+=generic_cross_gate(p,b1,b2)

    print("marginal identities checked =",marginal_checks)
    print("direct local counts checked =",brute_checks)
    print("generic cross-locus states checked =",cross_checks)
    print("RESULT: WP71_S4_LOCAL_COUPLING_EXACT_PASS")


if __name__=="__main__":
    main()
