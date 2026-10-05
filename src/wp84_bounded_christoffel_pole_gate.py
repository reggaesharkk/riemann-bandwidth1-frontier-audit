#!/usr/bin/env python3
"""WP84 exact pole-strip certificate for the bounded Christoffel consumer.

For delta=61, prove that every root of P(z)^2+61 has |Im z|>1.

Write z=x+i y and s=y^2.  A pole satisfies

    Re P(x+i y)=0,
    (Im P(x+i y))^2=61.

Eliminate x exactly.  The resultant is a degree-9 polynomial in s.
A Sturm root count shows it has no roots on [0,1].  Since the denominator has
no real roots, every pole therefore satisfies |Im z|>1.

SymPy's count_roots uses exact algebraic/Sturm machinery.
"""
import sympy as sp

x,s=sp.symbols("x s", real=True)
a=sp.Rational(43428,13891)
b=sp.Rational(37704,13891)
c=sp.Rational(9660,13891)
delta=sp.Integer(61)

# P(z)=1-a z+b z^2-c z^3.
# For z=x+i y and s=y^2:
ReP=sp.expand(1-a*x+b*x**2-c*x**3 + s*(-b+3*c*x))
A=sp.expand(-a+2*b*x-3*c*x**2)
# Im P = y*(A+c*s), so square it.
ImEq=sp.expand(s*(A+c*s)**2-delta)

def main():
    resultant=sp.resultant(ReP,ImEq,x)
    num=sp.Poly(sp.together(resultant).as_numer_denom()[0],s)
    # Remove irrelevant integer content.
    _,prim=sp.polys.polytools.primitive(num)
    prim=sp.Poly(prim,s)

    assert prim.degree()==9
    assert sp.count_roots(prim,0,1)==0

    # Denominator P^2+61 is strictly positive on R.
    xr=sp.symbols("xr", real=True)
    P=1-a*xr+b*xr**2-c*xr**3
    D=sp.Poly(sp.expand(P**2+delta),xr)
    assert sp.count_roots(D,-sp.oo,sp.oo)==0
    assert sp.gcd(D,D.diff()).degree()==0

    roots=sp.nroots(D.as_expr(),n=50,maxsteps=200)
    min_im=min(abs(complex(r).imag) for r in roots)

    print("resultant degree in s =",prim.degree())
    print("exact roots s in [0,1] =",sp.count_roots(prim,0,1))
    print("real denominator roots =",sp.count_roots(D,-sp.oo,sp.oo))
    print("diagnostic min |Im pole| ~",min_im)
    print("RESULT: WP84_BOUNDED_CHRISTOFFEL_POLE_STRIP_PASS")

if __name__=="__main__":
    main()
