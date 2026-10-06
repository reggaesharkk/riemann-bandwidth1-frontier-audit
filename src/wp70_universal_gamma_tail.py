#!/usr/bin/env python3
"""
Proof-oriented absolute tail bound for the universal (1,1) gamma series.

For the universal class, the public paper proves
  gamma_{2m} = C2 * prod_{p|m} 1/[p(p-2)]
for odd squarefree m, and gamma_d=0 otherwise, with
  C2 = prod_{p>2} (1 - 1/(p-1)^2).

The coefficients are nonnegative and the Euler products telescope:
  sum_d gamma_d = 1.

Hence the infinite tail after D is exactly
  1 - C2 * sum_{2m<=D} prod_{p|m} 1/[p(p-2)].

We bound C2 from below using a finite exact-prime product evaluated with
directed Decimal rounding and the elementary product tail inequality
  prod(1-x_i) >= 1-sum x_i,
together with
  sum_{p>P} 1/(p-1)^2
    <= sum_{n>P} 1/(n-1)^2
    <= 1/P + 1/P^2.

No unproved prime-distribution estimate is used.
"""

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import isqrt

PREC=90
PRIME_CUTOFF=1_000_000

def primes_upto(n):
    s=bytearray(b"\x01")*(n+1)
    s[0:2]=b"\x00\x00"
    for p in range(2,isqrt(n)+1):
        if s[p]:
            start=p*p
            s[start:n+1:p]=b"\x00"*(((n-start)//p)+1)
    return [p for p in range(2,n+1) if s[p]]

def spf_upto(n):
    spf=list(range(n+1))
    if n>=1: spf[1]=1
    for p in range(2,isqrt(n)+1):
        if spf[p]==p:
            for k in range(p*p,n+1,p):
                if spf[k]==k: spf[k]=p
    return spf

def universal_partial_rational(D):
    M=D//2
    spf=spf_upto(M)
    S=F(0)
    for m in range(1,M+1,2):
        x=m
        last=0
        a=F(1)
        squarefree=True
        while x>1:
            p=spf[x]
            if p==last:
                squarefree=False
                break
            last=p
            x//=p
            if x>1 and spf[x]==p:
                squarefree=False
                break
            a*=F(1,p*(p-2))
        if squarefree:
            S+=a
    return S

def frac_decimal_down(x):
    with localcontext() as ctx:
        ctx.prec=PREC
        ctx.rounding=ROUND_FLOOR
        return Decimal(x.numerator)/Decimal(x.denominator)

def frac_decimal_up(x):
    with localcontext() as ctx:
        ctx.prec=PREC
        ctx.rounding=ROUND_CEILING
        return Decimal(x.numerator)/Decimal(x.denominator)

def c2_lower():
    ps=primes_upto(PRIME_CUTOFF)
    with localcontext() as ctx:
        ctx.prec=PREC
        ctx.rounding=ROUND_FLOOR
        prod=Decimal(1)
        for p in ps:
            if p<=2: continue
            f=Decimal(p*(p-2))/Decimal((p-1)*(p-1))
            prod=prod*f
        # Sum_{m=P}^infty 1/m^2 <= 1/P^2 + integral_P^infty x^-2 dx.
        eps=Decimal(1)/Decimal(PRIME_CUTOFF) + Decimal(1)/Decimal(PRIME_CUTOFF**2)
        tail_factor=Decimal(1)-eps
        return prod*tail_factor, prod, eps

def tail_upper(D):
    S=universal_partial_rational(D)
    c2lo,c2finite,eps=c2_lower()
    Slo=frac_decimal_down(S)
    with localcontext() as ctx:
        ctx.prec=PREC
        ctx.rounding=ROUND_FLOOR
        captured_lo=c2lo*Slo
    with localcontext() as ctx:
        ctx.prec=PREC
        ctx.rounding=ROUND_CEILING
        tail=Decimal(1)-captured_lo
    return S,c2lo,c2finite,eps,tail

def main():
    for D in (40,400,4000):
        S,c2lo,c2fin,eps,tail=tail_upper(D)
        print("D =",D)
        print("partial_rational_digits =",len(str(S.numerator)),len(str(S.denominator)))
        print("C2_finite_directed =",c2fin)
        print("C2_lower =",c2lo)
        print("C2_tail_eps_bound =",eps)
        print("universal_gamma_tail_upper =",tail)
        print()

    _,_,_,_,t4000=tail_upper(4000)
    assert t4000 < Decimal("0.000252")
    print("CERTIFIED_UNIVERSAL_TAIL_D4000_LT =",Decimal("0.000252"))
    print("RESULT: UNIVERSAL_GAMMA_INFINITE_TAIL_PASS")

if __name__=="__main__":
    main()
