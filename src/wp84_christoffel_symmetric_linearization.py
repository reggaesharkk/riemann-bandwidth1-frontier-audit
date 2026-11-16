#!/usr/bin/env python3
"""Exact symbolic gate for the WP84 symmetric cubic Christoffel linearization."""

import sympy as sp

x,z=sp.symbols("x z")
p0=sp.Rational(1)
p1=-sp.Rational(43428,13891)
p2=sp.Rational(37704,13891)
p3=-sp.Rational(9660,13891)

P=p0+p1*x+p2*x**2+p3*x**3

r=-p3
b=-p2/(2*r)
c=-p1-r*b*b

L=sp.Matrix([
    [r*x, 1, 0],
    [1, 0, x+b],
    [0, x+b, c*x+z-p0],
])

def main():
    assert r==sp.Rational(9660,13891)
    assert b==-sp.Rational(1571,805)
    assert c==sp.Rational(5343048,11182255)

    det=sp.factor(L.det())
    assert sp.expand(det-(P-z))==0

    # (3,3) cofactor is exactly -1, so inverse corner is -1/(P-z).
    cof33=sp.det(sp.Matrix([[r*x,1],[1,0]]))
    assert cof33==-1
    inv33=sp.factor(L.inv()[2,2])
    assert sp.simplify(inv33 + 1/(P-z))==0

    # Exact delta=61 target arithmetic.
    delta=sp.Integer(61)
    w0=sp.Rational(1415,13891)
    rhs=sp.factor(1-w0/delta)
    cap=sp.factor(sp.Rational(delta+1,delta)*w0)
    simple=sp.factor(1-2*cap)

    assert rhs==sp.Rational(845936,847351)
    assert cap==sp.Rational(87730,847351)
    assert simple==sp.Rational(671891,847351)
    assert simple>sp.Rational(79,100)

    # Internal H-coefficient matrix has full rank 3, so a rank-2
    # displacement commutator lifts to rank at most 6.
    K=sp.Matrix([[r,0,0],[0,0,1],[0,1,c]])
    assert K.det()!=0
    assert K.rank()==3

    print("r =",r)
    print("b =",b)
    print("c =",c)
    print("det L =",det)
    print("(L^-1)_33 =",inv33)
    print("delta=61 corner target =",rhs,"~",float(rhs))
    print("F61 negative-mass cap =",cap,"~",float(cap))
    print("simple-zero rung =",simple,"~",float(simple))
    print("internal K rank =",K.rank())
    print("displacement-rank lift: 2 -> <=6")
    print("RESULT: WP84_CHRISTOFFEL_SYMMETRIC_LINEARIZATION_PASS")

if __name__=="__main__":
    main()
