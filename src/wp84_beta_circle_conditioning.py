#!/usr/bin/env python3
"""WP84 beta fixed-circle conditioning audit.

Computes the Laurent coefficients of b_m at +i exactly with SymPy, uses
conjugation for -i, and reports the worst-case Cauchy transfer constant

    C_m(rho)=2 sum_k |a_k| rho^(-(k-1)).

The model q_m values are recomputed exactly by reduction modulo the current
Christoffel cubic.

Requires sympy.
"""
import sympy as sp

x,y,s=sp.symbols("x y s")
I=sp.I
P = 1-sp.Rational(43428,13891)*x+sp.Rational(37704,13891)*x**2-sp.Rational(9660,13891)*x**3
w0=sp.Rational(1415,13891)

def beta(m):
    D=sp.integrate((1-s**2)**m,(s,0,1))
    t=2*x/(1+x**2)
    p=sum((-1)**j*sp.binomial(m,j)*t**(2*j+1)/sp.Rational(2*j+1)
          for j in range(m+1))/D
    return sp.cancel(p)

def model_q(f):
    num,den=sp.fraction(sp.cancel(f))
    inv=sp.invert(den,P,domain=sp.QQ)
    rem=sp.rem(num*inv,P,domain=sp.QQ)
    c=[sp.expand(rem).coeff(x,j) for j in range(3)]
    return sp.simplify(c[0]+c[1]+sp.Rational(4,3)*c[2]-w0*c[0])

def laurent_coeffs(f,m):
    ser=sp.series(f.subs(x,I+y),y,0,1).removeO().expand()
    return [sp.simplify(ser.coeff(y,-k)) for k in range(1,2*m+2)]

def abs_gaussian_rational(z):
    re=sp.simplify(sp.re(z)); im=sp.simplify(sp.im(z))
    if im==0:
        return abs(re)
    if re==0:
        return abs(im)
    # This branch is not expected for this family.
    return sp.sqrt(re**2+im**2)

def C(coeffs,rho):
    rr=sp.Rational(str(rho))
    return sp.N(2*sum(abs_gaussian_rational(a)/rr**j
                      for j,a in enumerate(coeffs)),20)

def main():
    threshold=sp.Rational(179,200)
    rho=0.9
    print("rho =",rho)
    best=None
    for m in range(1,11):
        f=beta(m)
        q=sp.simplify(model_q(f))
        margin=sp.N(q-threshold,20)
        coeff=laurent_coeffs(f,m)
        cm=C(coeff,rho)
        eps=(margin/cm) if margin>0 else None
        print("m=%2d pole=%2d q=%.12f margin=%+.6e C=%.6e eps=%s" %
              (m,2*m+1,float(q),float(margin),float(cm),
               "n/a" if eps is None else ("%.6e"%float(eps))))
        if eps is not None and (best is None or eps>best[0]):
            best=(eps,m)
    assert best[1]==3, best
    print("BEST_WORST_CASE_CONSUMER_AT_RHO_0.9 = b3")
    print("RESULT: WP84_BETA_CIRCLE_CONDITIONING_PASS")

if __name__=="__main__":
    main()
