#!/usr/bin/env python3
"""Exact regression gate for the shifted full-frontier rank-six consumer."""

from fractions import Fraction as F
import sympy as sp

A=F(43428,13891)
B=F(37704,13891)
C=F(9660,13891)
W0=F(1415,13891)

def conv(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j]+=x*y
    return out

def main():
    c=F(4,5)
    a=F(4,5)
    r2=c*c+a*a
    r6=r2**3

    # N(y)=r^6 P(-y)^2-((y+c)^2+a^2)^3.
    p=[F(1),A,B,C]
    num=[r6*x for x in conv(p,p)]
    d=[r2,2*c,F(1)]
    den=conv(conv(d,d),d)
    N=[num[k]-den[k] for k in range(7)]

    expected=[
        F(0),
        F(1139171328,217046875),
        F(51666437692416,3014998140625),
        F(66705610299392,3014998140625),
        F(39343236454368,3014998140625),
        F(1879514557608,602999628125),
        F(1710697607,120599925625),
    ]
    assert N==expected,(N,expected)
    assert all(x>0 for x in N[1:])

    Einf=r6*C*C
    assert Einf==F(122310623232,120599925625)

    simple=1-2*W0
    cushion=F(21,200)-W0
    assert simple==F(11061,13891)
    assert cushion==F(8711,2778200)

    # Exact Cayley coefficients.
    u=sp.symbols('u')
    As=sp.Rational(A.numerator,A.denominator)
    Bs=sp.Rational(B.numerator,B.denominator)
    Cs=sp.Rational(C.numerator,C.denominator)
    cc=sp.Rational(4,5)
    aa=sp.Rational(4,5)
    rr=sp.sqrt(cc**2+aa**2)
    xn=sp.Poly((-cc+sp.I*aa)+(cc+sp.I*aa)*u,u)
    dd=sp.Poly(u-1,u)

    expr=sp.expand(
        sp.I*rr**3/(8*aa**3)
        *(
            dd.as_expr()**3
            -As*xn.as_expr()*dd.as_expr()**2
            +Bs*xn.as_expr()**2*dd.as_expr()
            -Cs*xn.as_expr()**3
        )
    )
    q=list(reversed(sp.Poly(expr,u).all_coeffs()))

    expected_q=[
        sp.sqrt(2)*(-90672+273989*sp.I)/1389100,
        sp.sqrt(2)*(-403920+107313*sp.I)/1389100,
        sp.sqrt(2)*(-403920-107313*sp.I)/1389100,
        sp.sqrt(2)*(-90672-273989*sp.I)/1389100,
    ]
    assert all(sp.simplify(q[k]-expected_q[k])==0 for k in range(4))

    def conj(z):
        return sp.conjugate(z).subs(sp.conjugate(sp.sqrt(2)),sp.sqrt(2))

    c1=sp.simplify(q[1]*conj(q[0])+q[2]*conj(q[1])+q[3]*conj(q[2]))
    c2=sp.simplify(q[2]*conj(q[0])+q[3]*conj(q[1]))
    c3=sp.simplify(q[3]*conj(q[0]))

    Ah=sp.simplify(2*sp.I*aa*(c1+2*c2+3*c3))
    Bh=sp.simplify((2*sp.I*aa)**2*(c2+3*c3))
    Ch=sp.simplify((2*sp.I*aa)**3*c3/2)

    expected_A=-sp.Rational(183845781504,120599925625)+sp.I*sp.Rational(112029847146,602999628125)
    expected_B=sp.Rational(297763801992,602999628125)-sp.I*sp.Rational(623773801728,602999628125)
    expected_C=sp.Rational(1589960358912,15074990703125)+sp.I*sp.Rational(2139153937184,15074990703125)

    assert sp.simplify(Ah-expected_A)==0
    assert sp.simplify(Bh-expected_B)==0
    assert sp.simplify(Ch-expected_C)==0

    print("support coefficients:",N)
    print("E_infinity =",Einf,"~",float(Einf))
    print("model simple =",simple,"~",float(simple))
    print(">79 cushion =",cushion,"~",float(cushion))
    print("A_s =",Ah,"~",sp.N(Ah,18))
    print("B_s =",Bh,"~",sp.N(Bh,18))
    print("C_s =",Ch,"~",sp.N(Ch,18))
    print("RESULT: WP84_SHIFTED_EXACT_FRONTIER_RANK6_PASS")

if __name__=="__main__":
    main()
