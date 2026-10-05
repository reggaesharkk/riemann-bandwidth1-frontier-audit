#!/usr/bin/env python3
"""Exact uniform pole-strip certificate for the whole F_delta ladder.

Proves:
  for every real delta>=61, every zero of P(z)^2+delta satisfies |Im z|>1,
  and every zero is simple.

The proof uses:
  (i) the real-part cubic has three distinct real branches for s=y^2>=0;
  (ii) at delta=61 the equality |Im P|^2=61 has no branch point in s in [0,1];
  (iii) at s=0 all three branches have |Im P|^2=0;
  (iv) larger delta can only require a larger imaginary target;
  (v) P' has only real roots, so P^2+delta cannot have multiple nonreal roots.
"""
import sympy as sp

x,s=sp.symbols("x s", real=True)
a=sp.Rational(43428,13891)
b=sp.Rational(37704,13891)
c=sp.Rational(9660,13891)

ReP=sp.expand(1-a*x+b*x**2-c*x**3+s*(-b+3*c*x))
A=sp.expand(-a+2*b*x-3*c*x**2)
ImSq=sp.expand(s*(A+c*s)**2)

def main():
    disc_re=sp.factor(sp.discriminant(ReP,x))
    num_disc=sp.Poly(sp.together(disc_re).as_numer_denom()[0],s)
    # Every coefficient is positive, so discriminant >0 for s>=0.
    assert all(cc>0 for cc in num_disc.all_coeffs())

    eq61=sp.expand(ImSq-sp.Integer(61))
    res=sp.resultant(ReP,eq61,x)
    prim=sp.Poly(sp.polys.polytools.primitive(
        sp.Poly(sp.together(res).as_numer_denom()[0],s)
    )[1],s)
    assert sp.count_roots(prim,0,1)==0

    # At s=0, ImSq=0 on every branch. Since the three ReP roots remain
    # distinct and real for all s in [0,1], each branch is continuous.
    # No equality ImSq=61 occurs, hence ImSq<61 on every branch.
    assert sp.expand(ImSq.subs(s,0))==0

    P=1-a*x+b*x**2-c*x**3
    Pp=sp.diff(P,x)
    disc_pp=sp.factor(sp.discriminant(Pp,x))
    assert disc_pp>0

    print("ReP discriminant =",disc_re)
    print("resultant degree =",prim.degree())
    print("roots of equality resultant on [0,1] =",sp.count_roots(prim,0,1))
    print("P' discriminant =",disc_pp)
    print("CONCLUSION: for every delta>=61, all poles satisfy |Im z|>1 and are simple")
    print("RESULT: WP84_BOUNDED_CHRISTOFFEL_FAMILY_POLE_GATE_PASS")

if __name__=="__main__":
    main()
