#!/usr/bin/env python3
"""WP84/WP80 bounded support-free >80 consumer gate.

This script strengthens the one-sided k=8 Christoffel consumer:

1. In the feasible parametrization
       L=L0+t,
       U=F8(L)+eta,
   the degree-4 minimizer Q has alternating coefficient signs
       q1<=0, q2>=0, q3<=0, q4>=0.
   Hence Q(x)>=1 for every x<=0.

2. If actual m7>=L and m8<=U, the sign pattern y7<=0,y8>0 gives
       E_actual[Q^2] <= lambda_surrogate.

3. If lambda_surrogate<1/10, then a bounded rationalized consumer
       F_delta=(delta+1)Q^2/(Q^2+delta)
   also certifies >80 for every fixed
       delta > 9 lambda/(1-10 lambda).

At the exact midpoint test L=19.136 and U=(F8+T80)/2:
       lambda = 1415/14409,
and delta=50 already gives
       simple coefficient = 115507/144373 > 0.8.
"""
from fractions import Fraction as F
import sympy as sp

L0=F(25866469,1352400)

def F8(L):
    return (F(13335840000)*L*L-F(504286322400)*L+
            F(4794396454037))/F(748818000)

def T80(L):
    return (F(18670176000)*L*L-F(713649484800)*L+
            F(6822174057191))/F(68531400)

def D(L,U):
    return (F(1837779300)*U-F(24004512000)*L*L+
            F(903891063600)*L-F(8574904106497))

def coeffs(L,U):
    den=D(L,U)
    assert den>0
    q1=F(12)*(F(3500658000)*L*L-F(130325168925)*L-
              F(478793700)*U+F(1229767974292))/den
    q2=-F(105)*(F(152409600)*L*L-F(5513946480)*L-
                F(47507040)*U+F(51466255217))/den
    q3=F(1470)*(F(3393360)*L-F(869400)*U-F(32718563))/den
    q4=F(945)*(F(1352400)*L-F(25866469))/den
    return [F(1),q1,q2,q3,q4]

def square(a):
    out=[F(0)]*(2*len(a)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(a):
            out[i+j]+=u*v
    return out

def surrogate_lambda(L,U):
    q=coeffs(L,U)
    y=square(q)
    moms=[F(1),F(1),F(4,3),F(2),F(13,4),F(101,18),
          F(12809,1260),L,U]
    return sum(y[k]*moms[k] for k in range(9)),q,y

def bounded_cap(lam,delta):
    d=F(delta)
    return (d+1)*lam/(d+lam)

def main():
    # Exact symbolic sign factorizations.
    t,e=sp.symbols("t e", nonnegative=True)
    L=sp.Rational(L0.numerator,L0.denominator)+t
    F8s=(sp.Integer(13335840000)*L**2-sp.Integer(504286322400)*L+
         sp.Integer(4794396454037))/sp.Integer(748818000)
    U=F8s+e

    N1=sp.expand(sp.Integer(3500658000)*L**2-
                 sp.Integer(130325168925)*L-
                 sp.Integer(478793700)*U+
                 sp.Integer(1229767974292))
    B2=sp.expand(sp.Integer(152409600)*L**2-
                 sp.Integer(5513946480)*L-
                 sp.Integer(47507040)*U+
                 sp.Integer(51466255217))
    N3=sp.expand(sp.Integer(3393360)*L-
                 sp.Integer(869400)*U-sp.Integer(32718563))
    N4=sp.expand(sp.Integer(1352400)*L-sp.Integer(25866469))

    assert sp.factor(N1) == -sp.Rational(11025,283)*(
        sp.Integer(12290124)*e+sp.Integer(129018960)*t**2+
        sp.Integer(3931153)*t)
    assert sp.factor(B2) == -sp.Rational(15120,283)*(
        sp.Integer(889186)*e+sp.Integer(12983040)*t**2+
        sp.Integer(1024177)*t)
    assert sp.factor(N3) == -sp.Rational(1080,283)*(
        sp.Integer(227815)*e+sp.Integer(4057200)*t**2+
        sp.Integer(889186)*t)
    assert sp.factor(N4)==sp.Integer(1352400)*t

    # Exact midpoint example inside the >80 corridor.
    Lm=F(19136,1000)
    Um=(F8(Lm)+T80(Lm))/2
    lam,q,y=surrogate_lambda(Lm,Um)

    assert q[1]<0 and q[2]>0 and q[3]<0 and q[4]>0
    assert y[7]<=0 and y[8]>0
    assert lam==F(1415,14409)
    assert lam<F(1,10)

    threshold=F(9)*lam/(F(1)-F(10)*lam)
    assert threshold < F(50)

    cap50=bounded_cap(lam,50)
    simple50=F(1)-F(2)*cap50
    assert simple50==F(115507,144373)
    assert simple50>F(4,5)

    print("midpoint lambda =",lam,"=",float(lam))
    print("minimum fixed delta for bounded >80:",float(threshold))
    print("delta=50 cap =",cap50,"=",float(cap50))
    print("delta=50 simple floor =",simple50,"=",float(simple50))
    print("Q coefficient signs =",["+" if v>0 else "-" if v<0 else "0" for v in q])
    print("RESULT: WP84_BOUNDED_K8_SUPPORT_FREE_80_GATE_PASS")

if __name__=="__main__":
    main()
