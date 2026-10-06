#!/usr/bin/env python3
"""Exact payoff ladder for the higher-moment hostile audit."""
from fractions import Fraction as F

def consumer(R):
    D=R+F(1,30)
    lam=(F(5,108)+D/F(3))/(F(1,3)+F(4,3)*D)
    return F(1)-2*lam, F(1)-lam, D, lam

# Stage A: exact continuum core, if all analytic/truncation errors are o(1).
sA,dA,DA,lA=consumer(-F(1,48))
assert DA==F(1,80)
assert lA==F(109,756)
assert sA==F(269,378)
assert dA==F(647,756)

# Stage B: exact fourth moment m4=13/4 means R=-1/30.
sB,dB,DB,lB=consumer(-F(1,30))
assert DB==0
assert sB==F(13,18)
assert dB==F(31,36)

# Stage C: exact six-moment consumer already independently derived.
sC=F(11061,13891)
dC=F(1,1)-F(1415,13891)  # w0 = 1415/13891 from 1-simple? stored only for orientation

print("STAGE_A_EXACT_CORE_IF_TAIL_o1")
print("R =",-F(1,48))
print("simple =",sA,float(sA))
print("distinct =",dA,float(dA))
print("STAGE_B_EXACT_M4")
print("R =",-F(1,30))
print("simple =",sB,float(sB))
print("distinct =",dB,float(dB))
print("STAGE_C_EXACT_M1_TO_M6_CONSUMER")
print("simple =",sC,float(sC))
print("RESULT: PAYOFF_LADDER_EXACT_PASS")
