#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

HD = F(1345001407358823291468759581606590377186806057252528157859,
       2000000000000000000000000000000000000000000000000000000000)
PIU = F(157079632679489661923,50000000000000000000)
B = F(1094977,5000000000)

def c(A):
    return (6*HD - 10*PIU*B)/(6-A)

A1293=F(1293,100000)
A1294=F(1294,100000)
c1293=c(A1293)
c1294=c(A1294)

getcontext().prec=90
D=lambda x: Decimal(x.numerator)/Decimal(x.denominator)
print("A1293", D(c1293))
print("A1294", D(c1294))
print("gain", D(c1294-c1293))
assert c1294 > c1293
