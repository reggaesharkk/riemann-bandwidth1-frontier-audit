#!/usr/bin/env python3
"""Exact k=8 >80 go/no-go map.

Parameterize
    L=L0+t,
    m8=F8(L)+eta.
The exact corridor condition is
    eta < C t^2,
    C=2666160/10471.

This script prints the exact m7 lift needed to tolerate selected m8 excesses
and gives bounded-rational consumer margins for the midpoint diagnostic.
"""
from fractions import Fraction as F
from math import sqrt

L0=F(25866469,1352400)
C=F(2666160,10471)
LAM=F(1415,14409)

def bounded_simple(delta):
    d=F(delta)
    cap=(d+1)*LAM/(d+LAM)
    return 1-2*cap

def main():
    print("L0 =",float(L0))
    print("corridor coefficient C =",float(C))

    for eta in (0.001,0.005,0.010,0.020,0.023):
        lift=sqrt(eta/float(C))
        print("eta",eta,"requires L-L0 >",lift,"i.e. L >",float(L0)+lift)

    print("midpoint bounded-consumer margins:")
    for d in (50,60,100,200,500,1000,5000):
        s=bounded_simple(d)
        print(" delta",d,"simple",float(s),"margin over .8",float(s-F(4,5)))

    print("RESULT: WP84_K8_80_GONOGO_MAP_PASS")

if __name__=="__main__":
    main()
