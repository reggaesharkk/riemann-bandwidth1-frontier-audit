#!/usr/bin/env python3
"""Regression gate for exact grouped Q_p geometric formulas."""

import cmath
import math

def direct_Q(p,L,a,tau):
    M=int(math.floor(L/math.log(p)+1e-14))
    return -(math.log(p)/(a*L))*sum(
        p**(-m/2)*cmath.exp(1j*tau*m*math.log(p))
        for m in range(1,M+1)
    )

def closed_Q(p,L,a,tau):
    M=int(math.floor(L/math.log(p)+1e-14))
    z=p**(-0.5)*cmath.exp(1j*tau*math.log(p))
    return -(math.log(p)/(a*L))*z*(1-z**M)/(1-z)

def direct_Qp(p,L,a,tau):
    M=int(math.floor(L/math.log(p)+1e-14))
    return -1j*(math.log(p)**2/(a*L))*sum(
        m*(p**(-0.5)*cmath.exp(1j*tau*math.log(p)))**m
        for m in range(1,M+1)
    )

def closed_Qp(p,L,a,tau):
    M=int(math.floor(L/math.log(p)+1e-14))
    z=p**(-0.5)*cmath.exp(1j*tau*math.log(p))
    sm=z*(1-(M+1)*z**M+M*z**(M+1))/(1-z)**2
    return -1j*(math.log(p)**2/(a*L))*sm

def main():
    L=17.3
    a=0.73
    worst=0.0
    for p in (2,3,5,7,11,17,31,97,997):
        if math.log(p)>L:
            continue
        for tau in (13.1,17.0,23.7,41.3):
            e1=abs(direct_Q(p,L,a,tau)-closed_Q(p,L,a,tau))
            e2=abs(direct_Qp(p,L,a,tau)-closed_Qp(p,L,a,tau))
            worst=max(worst,e1,e2)
            assert e1<2e-14,(p,tau,e1)
            assert e2<2e-12,(p,tau,e2)

            q=closed_Q(p,L,a,tau)
            bd=(math.log(p)/(a*L))/(math.sqrt(p)-1)
            assert abs(q)<=bd*(1+1e-13)

    print("worst closed-form error =",worst)
    print("RESULT: WP84_PRIME_BASE_GEOMETRIC_Q_PASS")

if __name__=="__main__":
    main()
