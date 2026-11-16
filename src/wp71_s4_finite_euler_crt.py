#!/usr/bin/env python3
"""Finite Euler/CRT assembly check for the WP71 S4 local coupling."""
from fractions import Fraction as F
from math import gcd
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location(
    "s4local", HERE/"wp71_s4_local_coupling_exact.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def prod(xs):
    z=F(1)
    for x in xs: z*=x
    return z

def prime_data(primes,b1,b2):
    out=[]
    for p in primes:
        e=min(mod.vp(b1,p),mod.vp(b2,p))
        out.append((p,e,p**(e+1)))
    return out

def check(primes,b1,b2):
    g=gcd(b1,b2); r,q=b1//g,b2//g
    pd=prime_data(primes,b1,b2)
    Jmod=1
    Kmod=1
    gP=1
    for p,e,jm in pd:
        Jmod*=jm
        Kmod*=p
        gP*=p**e

    # j marginal of the finite Euler product.
    for k in range(Kmod):
        lhs=F(0)
        for j in range(Jmod):
            lhs+=prod(mod.k4_formula(p,b1,b2,k,j) for p,_,_ in pd)
        lhs/=Jmod
        rhs=prod(
            mod.tau(p,mod.vp(r*k,p))*mod.tau(p,mod.vp(q*k,p))
            for p,_,_ in pd
        )
        assert lhs==rhs,(primes,b1,b2,"javg",k,lhs,rhs)

    # k marginal of the finite Euler product.
    for j in range(Jmod):
        lhs=F(0)
        for k in range(Kmod):
            lhs+=prod(mod.k4_formula(p,b1,b2,k,j) for p,_,_ in pd)
        lhs/=Kmod
        rhs=prod(
            mod.kap2(p,mod.vp(b1,p),mod.vp(b2,p),mod.vp(j,p,e+1))**2
            for p,e,_ in pd
        )/gP
        assert lhs==rhs,(primes,b1,b2,"kavg",j,lhs,rhs)

    return Jmod,Kmod,gP

def main():
    cases=[
      ((2,3),(4,9)),
      ((2,3,5),(8,5)),
      ((2,3,5),(10,15)),
      ((2,3),(12,18)),
    ]
    for primes,pair in cases:
        J,K,gP=check(primes,*pair)
        print("primes",primes,"pair",pair,
              "Jmod",J,"Kmod",K,"gP",gP,"PASS")
    print("RESULT: WP71_S4_FINITE_EULER_CRT_PASS")

if __name__=="__main__":
    main()
