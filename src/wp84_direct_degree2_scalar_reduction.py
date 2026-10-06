#!/usr/bin/env python3
"""Exact algebra certificate for the direct degree-two Cayley scalar reduction."""
import sympy as sp

def main():
    I=sp.I
    u=sp.symbols("u")

    q0=-(sp.Rational(557,1000)+sp.Rational(58,1000)*I)
    q1=sp.Rational(55,1000)-sp.Rational(1058,1000)*I
    q2=sp.Rational(623,1000)

    coeff=[q0,q1,q2]

    c={}
    for r in range(-2,3):
        s=0
        for k in range(3):
            j=k+r
            if 0<=j<3:
                s += coeff[j]*sp.conjugate(coeff[k])
        c[r]=sp.simplify(s)

    assert c[0]==sp.Rational(1824131,1000000)
    assert c[1]==sp.Rational(32497,500000)+sp.Rational(125163,100000)*I
    assert c[2]==-sp.Rational(347011,1000000)+sp.Rational(18067,500000)*I

    const=sp.simplify(c[0]+2*sp.re(c[1]+c[2]))
    A=sp.simplify(2*I*c[1]+4*I*c[2])
    B=sp.simplify(-4*c[2])

    assert const==sp.Rational(1260097,1000000)
    assert A==-sp.Rational(661949,250000)-sp.Rational(157257,125000)*I
    assert B==sp.Rational(347011,250000)-sp.Rational(18067,125000)*I

    Q0=sp.simplify(q0+q1+q2)
    Q1=sp.simplify(2*I*q1+4*I*q2)
    Q2=sp.simplify(-4*q2)

    assert Q0==sp.Rational(121,1000)-sp.Rational(279,250)*I
    assert Q1==sp.Rational(529,250)+sp.Rational(1301,500)*I
    assert Q2==-sp.Rational(623,250)

    print("constant =",const)
    print("A =",A)
    print("B =",B)
    print("Q resolvent coefficients =",Q0,Q1,Q2)
    print("RESULT: WP84_DIRECT_DEGREE2_SCALAR_REDUCTION_PASS")

if __name__=="__main__":
    main()
