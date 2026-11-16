#!/usr/bin/env python3
"""WP71 G9-B moving-interval structural gate.

For fixed b1,b2,J and an outer m-window [lo,hi], let
  g=gcd(b1,b2), r=b1/g, q=b2/g.

After the exact welding reindexing m' = m-rk, n' = n-qk, the allowed m
for fixed (k,n) is

  A_k = max(lo, lo+rk)
  B_k = min(hi, hi+rk)

  L_k(n) = max(A_k, ceil((b1*n-J)/b2))
  U_k(n) = min(B_k, floor((b1*n+J)/b2)).

The original j!=0 condition removes at most one point:
  m0 = b1*n/b2 = r*(n/q), present iff q|n and A_k<=m0<=B_k.

Thus I_k(n) is one integer interval with at most one puncture.

This script verifies, using arbitrary integer weights:
  * exact equivalence to the original predicates;
  * same-j invariance under the welding shift;
  * prefix-sum representation;
  * exact main/remainder decomposition against any chosen constant S;
  * monotonicity and bounded increments of L_k,U_k;
  * at most one source switch in each endpoint;
  * exact characterization/count of j=0 holes.

No number-theoretic estimate is used.
"""
from __future__ import annotations
from math import gcd, ceil

def cdiv(a,b):
    return -((-a)//b)

def static_bounds(b1,b2,lo,hi,k):
    g=gcd(b1,b2); r=b1//g; q=b2//g
    A=max(lo,lo+r*k)
    B=min(hi,hi+r*k)
    return g,r,q,A,B

def full_bounds(b1,b2,J,lo,hi,k,n):
    g,r,q,A,B=static_bounds(b1,b2,lo,hi,k)
    jl=cdiv(b1*n-J,b2)
    ju=(b1*n+J)//b2
    L=max(A,jl)
    U=min(B,ju)
    lsrc="static" if A>=jl else "jlower"
    usrc="static" if B<=ju else "jupper"
    return g,r,q,A,B,jl,ju,L,U,lsrc,usrc

def hole(b1,b2,lo,hi,k,n):
    g,r,q,A,B=static_bounds(b1,b2,lo,hi,k)
    if n%q:
        return None
    m0=r*(n//q)
    return m0 if A<=m0<=B else None

def formula_points(b1,b2,J,lo,hi,k,n):
    vals=full_bounds(b1,b2,J,lo,hi,k,n)
    L,U=vals[7],vals[8]
    if L>U:
        return []
    pts=list(range(L,U+1))
    h=hole(b1,b2,lo,hi,k,n)
    if h is not None and L<=h<=U:
        pts.remove(h)
    return pts

def direct_points(b1,b2,J,lo,hi,k,n):
    g=gcd(b1,b2); r=b1//g; q=b2//g
    out=[]
    for m in range(lo,hi+1):
        mp=m-r*k
        if not (lo<=mp<=hi):
            continue
        j=b1*n-b2*m
        if j==0 or abs(j)>J:
            continue
        np=n-q*k
        jp=b1*np-b2*mp
        assert jp==j
        out.append(m)
    return out

def prefix(values,lo,hi):
    P={lo-1:0}
    s=0
    for m in range(lo,hi+1):
        s+=values.get(m,0)
        P[m]=s
    return P

def check_case(b1,b2,J,lo,hi):
    g=gcd(b1,b2); r=b1//g; q=b2//g
    a={m:((7*m*m+5*m+13)%29)-9 for m in range(lo-50,hi+51)}
    max_inc=ceil(b1/b2)
    tested=0

    kmax=(hi-lo)//r+2
    for k in range(-kmax,kmax+1):
        g0,r0,q0,A,B=static_bounds(b1,b2,lo,hi,k)
        if A>B:
            for n in range(-10,80):
                assert formula_points(b1,b2,J,lo,hi,k,n)==[]
            continue

        ns=list(range(-10,81))
        Ls=[]; Us=[]; lsrc=[]; usrc=[]; holes=[]
        for n in ns:
            vals=full_bounds(b1,b2,J,lo,hi,k,n)
            L,U,ls,us=vals[7],vals[8],vals[9],vals[10]
            Ls.append(L); Us.append(U); lsrc.append(ls); usrc.append(us)

            d=direct_points(b1,b2,J,lo,hi,k,n)
            f=formula_points(b1,b2,J,lo,hi,k,n)
            assert d==f,(b1,b2,J,lo,hi,k,n,d,f)

            x={m:a.get(m,0)*a.get(m-r*k,0) for m in range(A,B+1)}
            P=prefix(x,A,B)
            fullsum=0 if L>U else P[U]-P[L-1]
            h=hole(b1,b2,lo,hi,k,n)
            actual=fullsum-(x[h] if h is not None and L<=h<=U else 0)
            direct=sum(x[m] for m in f)
            assert actual==direct

            S=17
            length=max(0,U-L+1)
            h_in=int(h is not None and L<=h<=U)
            allowed_len=length-h_in

            def count_to(t):
                if t<A:
                    return 0
                return max(0,min(t,B)-A+1)

            def pval(t):
                if t<A:
                    return 0
                return P[min(t,B)]

            EU=pval(U)-S*count_to(U)
            EL=pval(L-1)-S*count_to(L-1)
            hole_dev=(x[h]-S) if h_in else 0
            assert direct == S*allowed_len + (EU-EL-hole_dev)

            if h is not None:
                assert n%q==0
                assert h==r*(n//q)
                holes.append((n,h))
            tested+=1

        for arr in (Ls,Us):
            for x,y in zip(arr,arr[1:]):
                assert y>=x
                assert y-x<=max_inc

        lc=sum(x!=y for x,y in zip(lsrc,lsrc[1:]))
        uc=sum(x!=y for x,y in zip(usrc,usrc[1:]))
        assert lc<=1,(lsrc,lc)
        assert uc<=1,(usrc,uc)

        if holes:
            for (n0,m0),(n1,m1) in zip(holes,holes[1:]):
                assert n1-n0==q
                assert m1-m0==r

    return {"case":(b1,b2,J,lo,hi),"tested_states":tested}

def main():
    cases=[
      (5,3,7,2,18),
      (5,4,9,3,21),
      (6,4,8,2,19),
      (7,9,11,4,25),
      (8,12,10,3,20),
      (11,6,17,5,34),
    ]
    total=0
    for c in cases:
        out=check_case(*c)
        total+=out["tested_states"]
        print(out)
    print("tested states =",total)
    print("RESULT: WP71_G9_B_MOVING_INTERVAL_PASS")

if __name__=="__main__":
    main()
