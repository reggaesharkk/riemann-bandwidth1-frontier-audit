#!/usr/bin/env python3
"""WP84 round-3 exact Hankel/Christoffel audit.

Verifies:
- det of the 4x4 Hamburger Hankel matrix;
- Christoffel kernel K(0,0)=e0^T H^{-1}e0;
- reciprocal Christoffel function 1/K(0,0)=1415/13891;
- exact minimizer polynomial coefficients;
- exact fixed-moment identity int P(x)^2 dnu = 1415/13891;
- one-line half-line domination P(x)>=1 for x<=0;
- the displayed shifted 3x3 determinant is already determined by m1..m5
  and equals 23/1296>0.

Pure exact rational arithmetic via sympy.
"""
import sympy as sp

x=sp.symbols("x", real=True)
u=sp.symbols("u", nonnegative=True)

m=[
    sp.Rational(1),
    sp.Rational(1),
    sp.Rational(4,3),
    sp.Rational(2),
    sp.Rational(13,4),
    sp.Rational(101,18),
    sp.Rational(12809,1260),
]

H=sp.Matrix([[m[i+j] for j in range(4)] for i in range(4)])
e0=sp.Matrix([1,0,0,0])

P=(
    1
    -sp.Rational(43428,13891)*x
    +sp.Rational(37704,13891)*x**2
    -sp.Rational(9660,13891)*x**3
)

def main():
    detH=sp.factor(H.det())
    assert detH==sp.Rational(283,108864)

    K00=sp.factor((H.inv())[0,0])
    lam0=sp.factor(1/K00)
    assert K00==sp.Rational(13891,1415)
    assert lam0==sp.Rational(1415,13891)

    # Christoffel minimizer with p(0)=1.
    coeff=sp.simplify(H.inv()*e0/K00)
    P_from_H=sum(coeff[j]*x**j for j in range(4))
    assert sp.expand(P_from_H-P)==0

    g=sp.expand(P**2)
    Ig=sp.factor(sum(g.coeff(x,k)*m[k] for k in range(7)))
    assert Ig==lam0

    # One-line half-line sign certificate:
    # P(x)-1=x Q(x),
    # Q(x)=-(43428-37704 x+9660 x^2)/13891.
    Q=sp.factor((P-1)/x)
    Q_expected=-(
        sp.Integer(43428)-sp.Integer(37704)*x+sp.Integer(9660)*x**2
    )/sp.Integer(13891)
    assert sp.expand(Q-Q_expected)==0

    # For x=-u with u>=0, Q(-u) is the negative of a polynomial
    # with strictly positive coefficients, hence Q(-u)<0 and
    # (-u)Q(-u)>=0, so P(-u)>=1.
    pos_poly=sp.expand(-sp.Integer(13891)*Q.subs(x,-u))
    assert all(c>0 for c in sp.Poly(pos_poly,u).all_coeffs())

    Hshift3=sp.Matrix([[m[i+j+1] for j in range(3)] for i in range(3)])
    det_shift=sp.factor(Hshift3.det())
    assert det_shift==sp.Rational(23,1296)

    roots=sp.nroots(P,n=40)
    assert all(abs(complex(r).imag)<1e-30 and complex(r).real>0 for r in roots)

    positive_floor=1-lam0
    simple_floor=2*positive_floor-1
    assert positive_floor==sp.Rational(12476,13891)
    assert simple_floor==sp.Rational(11061,13891)

    print("det H =",detH)
    print("K(0,0) =",K00)
    print("Christoffel function lambda(0) =",lam0)
    print("minimizer P =",sp.factor(P))
    print("integral P^2 dnu =",Ig)
    print("shifted 3x3 determinant =",det_shift)
    print("roots =",[sp.N(r,16) for r in roots])
    print("positive-index floor =",positive_floor,"~",float(positive_floor))
    print("simple-zero ledger floor =",simple_floor,"~",float(simple_floor))
    print("RESULT: WP84_ROUND3_HANKEL_CHRISTOFFEL_AUDIT_PASS")

if __name__=="__main__":
    main()
