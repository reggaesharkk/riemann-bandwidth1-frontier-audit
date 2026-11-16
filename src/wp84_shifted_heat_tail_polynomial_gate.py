#!/usr/bin/env python3
"""Exact rational regression for the shifted consumer's large-|x| tail.

This verifies the scalar polynomial only; no uniform Gaussian small-ball
estimate or large-T theorem is asserted.
"""
from fractions import Fraction as F

def conv(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j]+=x*y
    return out

def main():
    A,B,C=F(43428,13891),F(37704,13891),F(9660,13891)
    c=a=F(4,5)
    r2=c*c+a*a
    r6=r2**3
    P=[F(1),-A,B,-C]
    D0=[r2,-2*c,F(1)]
    D=conv(conv(D0,D0),D0)
    E_inf=r6*C*C
    P2=conv(P,P)
    Fnum=[r6*P2[k]-E_inf*D[k] for k in range(7)]
    expected=[
        F(-56056139186176,1884373837890625),
        F(-1935986510266368,376874767578125),
        F(43996384591872,2599136328125),
        F(-330024542797824,15074990703125),
        F(1339674329088,103965453125),
        F(-367691563008,120599925625),
        F(0),
    ]
    assert Fnum==expected,(Fnum,expected)
    assert E_inf==F(122310623232,120599925625)
    S=sum(abs(x) for x in Fnum)
    assert S==F(112913213256073216,1884373837890625)
    C_tail=F(5,3)**6*S
    assert C_tail==F(112913213256073216,87917345780625)
    print('E_infinity =',E_inf)
    print('tail numerator coefficients =',Fnum)
    print('sum_abs_coefficients =',S)
    print('C_tail for |x|>=2 =',C_tail,'~',float(C_tail))
    print('RESULT: SHIFTED_HEAT_TAIL_POLYNOMIAL_PASS (scalar exact algebra only)')

if __name__=='__main__':
    main()
