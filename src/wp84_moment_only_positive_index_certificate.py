#!/usr/bin/env python3
"""WP84 exact moment-only positive-index certificate.

Let
    P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3,
    g(x)=P(x)^2.

For the pinned moments m0..m6,
    int g dnu = 1415/13891.

P has three distinct positive roots:
- discriminant(P)>0, so all roots are real and distinct;
- P(-x)>0 for x>=0, so P has no nonpositive root.

Since P(0)=1 and all roots xi are positive,
    P(x)=prod_i (1-x/xi),
so for x<=0 every factor is >=1 and therefore
    g(x)>=1.

Hence for every positive Borel measure nu on R with the pinned moments,
    nu((-infty,0]) <= int g dnu = 1415/13891,
and
    nu((0,infty)) >= 12476/13891.

This uses no support restriction on nu.
"""
import sympy as sp

x=sp.symbols("x")
P=1-sp.Rational(43428,13891)*x+sp.Rational(37704,13891)*x**2-sp.Rational(9660,13891)*x**3
mom=[
    sp.Rational(1),
    sp.Rational(1),
    sp.Rational(4,3),
    sp.Rational(2),
    sp.Rational(13,4),
    sp.Rational(101,18),
    sp.Rational(12809,1260),
]
w0=sp.Rational(1415,13891)
q=sp.Rational(12476,13891)
simple=sp.Rational(11061,13891)

def main():
    disc=sp.factor(sp.discriminant(P,x))
    assert disc>0

    # No x<=0 root: P(-u) has strictly positive coefficients for u>=0.
    u=sp.symbols("u", nonnegative=True)
    Pminus=sp.expand(P.subs(x,-u))
    assert all(c>0 for c in sp.Poly(Pminus,u).all_coeffs())

    roots=[complex(r) for r in sp.nroots(P, n=40)]
    assert all(abs(z.imag)<1e-30 and z.real>0 for z in roots)

    g=sp.expand(P**2)
    Ig=sp.simplify(sum(g.coeff(x,k)*mom[k] for k in range(7)))
    assert Ig==w0
    assert 1-w0==q
    assert 2*q-1==simple

    print("discriminant =",disc)
    print("positive roots =",[z.real for z in roots])
    print("int g dnu =",Ig)
    print("positive-index floor =",q,"~",float(q))
    print("counting-conversion floor =",simple,"~",float(simple))
    print("RESULT: WP84_MOMENT_ONLY_POSITIVE_INDEX_CERTIFICATE_PASS")

if __name__=="__main__":
    main()
