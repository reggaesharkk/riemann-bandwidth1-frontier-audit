#!/usr/bin/env python3
"""WP71 p-adic lift gate for the j-first four-point local factor.

Let e=min(v_p(b1),v_p(b2)) and take s>e.  For
    b1*n-b2*m = j (mod p^s),
if v_p(j)<e there are no solutions.

Otherwise divide the congruence by p^e.  The unit/nonunit pattern modulo p
determines a level-p admissible count Np for the four positions
    m, m-rk, n, n-qk.

Every admissible mod-p solution has exactly p^(s+e-1) lifts to mod p^s
satisfying the original congruence.  Hence

    Count_s = Np * p^(s+e-1).

This script brute-force verifies the formula for small prime powers and
several outer valuation/unit patterns.
"""
from math import gcd

def vp(n,p):
    if n==0:
        return 10**9
    n=abs(n); e=0
    while n%p==0:
        n//=p; e+=1
    return e

def brute_count(p,s,b1,b2,k,j):
    P=p**s
    g=gcd(b1,b2); r=b1//g; q=b2//g
    cnt=0
    for m in range(P):
        if m%p==0 or (m-r*k)%p==0:
            continue
        for n in range(P):
            if n%p==0 or (n-q*k)%p==0:
                continue
            if (b1*n-b2*m-j)%P==0:
                cnt+=1
    return cnt

def modp_count_after_division(p,b1,b2,k,j):
    e=min(vp(b1,p),vp(b2,p))
    if vp(j,p)<e:
        return 0
    B1=b1//(p**e)
    B2=b2//(p**e)
    J=j//(p**e)
    g=gcd(b1,b2); r=b1//g; q=b2//g
    cnt=0
    for m in range(p):
        if m==0 or (m-r*k)%p==0:
            continue
        for n in range(p):
            if n==0 or (n-q*k)%p==0:
                continue
            if (B1*n-B2*m-J)%p==0:
                cnt+=1
    return cnt

def main():
    cases=0
    # Keep brute-force sizes small but vary valuation and unit patterns.
    families=[
      (2,2,3),(2,4,3),(2,4,6),(2,8,3),(2,12,5),
      (3,3,2),(3,9,2),(3,9,6),(3,6,5),
    ]
    for p,b1,b2 in families:
        e=min(vp(b1,p),vp(b2,p))
        for s in range(max(e+1,2),min(e+4,5)):
            P=p**s
            # A deterministic set covering v_p(j)<e, =e, >e and j=0.
            js={0,1,p**e if e<10 else 1}
            if e>0:
                js.add(p**(e-1))
            js.add(p**(e+1))
            js={j%P for j in js}
            for k in range(min(p,4)):
                for j in sorted(js):
                    got=brute_count(p,s,b1,b2,k,j)
                    Np=modp_count_after_division(p,b1,b2,k,j)
                    want=0 if Np==0 else Np*(p**(s+e-1))
                    assert got==want,(p,s,b1,b2,k,j,got,want,Np,e)
                    cases+=1
    print("p-adic lift cases checked =",cases)
    print("RESULT: WP71_JFIRST_PADIC_LIFT_PASS")

if __name__=="__main__":
    main()
