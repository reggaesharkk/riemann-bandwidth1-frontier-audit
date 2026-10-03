#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

HD = F(1345001407358823291468759581606590377186806057252528157859,
       2000000000000000000000000000000000000000000000000000000000)
PIU = F(157079632679489661923,50000000000000000000)
B6 = F(1094977,5000000000)

def c(A,B):
    return (6*HD - 10*PIU*B)/(6-A)

A1293=F(1293,100000)
c1293=c(A1293,B6)
B=F(21,20)*B6
A_threshold=6-(6*HD-10*PIU*B)/c1293
A=F(269,20000)
cc=c(A,B)

getcontext().prec=90
D=lambda x: Decimal(x.numerator)/Decimal(x.denominator)
print("public_A1293_arithmetic", D(c1293))
print("candidate_B", B, D(B))
print("A_threshold", D(A_threshold))
print("A_target", A, D(A))
print("candidate_feedback", D(cc))
print("gain", D(cc-c1293))
assert A>A_threshold
assert cc>c1293
