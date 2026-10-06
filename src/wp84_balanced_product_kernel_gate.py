#!/usr/bin/env python3
"""Finite regression gate for the exact balanced product-kernel identity."""
import cmath, math, random

def Dd(d,s):
    return sum(cmath.exp(2j*math.pi*k*s) for k in range(d))/d

def main():
    random.seed(8402)
    nums=[6,10,14,15,21,22,26,33]
    c={n:complex(random.random()-0.5,random.random()-0.5) for n in nums}
    T=173.0
    L=29.0
    d=71

    lhs=0.0
    for k in range(d):
        tau=T+2*math.pi*k/L
        z=sum(c[n]*cmath.exp(1j*tau*math.log(n)) for n in nums)
        lhs += abs(z)**2
    lhs/=d

    rhs=0j
    for m in nums:
        for n in nums:
            y=math.log(m/n)
            rhs += (c[m]*c[n].conjugate()
                    *cmath.exp(1j*T*y)
                    *Dd(d,y/L))

    assert abs(lhs-rhs.real)<2e-12,(lhs,rhs)
    assert abs(rhs.imag)<2e-12,rhs

    # Scale conversion: |log(n/m)| <= C/T on one dyadic M-block implies
    # |n-m| <= exp(C/T)*2M*C/T by exp(x)-1 <= exp(x)x.
    M=10_000
    C=3.0
    for m in range(M+1,2*M+1,137):
        for h in range(-200,201,19):
            n=m+h
            if not (M<n<=2*M) or n==m:
                continue
            y=abs(math.log(n/m))
            if y<=C/T:
                bound=2*M*math.exp(C/T)*C/T
                assert abs(h)<=bound+1e-12

    print("balanced quadratic form =",lhs)
    print("product-kernel form     =",rhs.real)
    print("difference              =",abs(lhs-rhs.real))
    print("RESULT: WP84_BALANCED_PRODUCT_KERNEL_PASS")

if __name__=="__main__":
    main()
