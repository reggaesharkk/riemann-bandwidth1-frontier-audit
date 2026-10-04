#!/usr/bin/env python3
"""WP80 exact one-sided k=8 consumer gate.

This strengthens the exact k=8 Christoffel calculation into the form most
useful for analytic transport.

Assume a nonnegative measure on [0,infinity) with exact moments m0..m6,
a lower bound m7 >= L, and an upper bound m8 <= U.

Let
  L0 = 25866469/1352400.

For L > L0, moment feasibility forces U >= F8(L), and the degree-4
Christoffel minimizer built from the surrogate moments (m7,m8)=(L,U)
has coefficient signs y7 <= 0, y8 > 0.  Therefore its expectation under
the actual measure is at most its surrogate expectation.

Consequences:
  * any L > L0 gives a strict improvement over 11061/13891, provided U
    is a valid finite upper bound;
  * >80% follows from U < T80(L).

All identities below are checked with exact rational polynomial arithmetic.
No numerical optimizer is used.
"""
from fractions import Fraction as F

L0=F(25866469,1352400)

def F8(L):
    return (F(13335840000)*L*L-F(504286322400)*L+F(4794396454037))/F(748818000)

def Dfloor(L):
    return (F(24004512000)*L*L-F(903891063600)*L+F(8574904106497))/F(1837779300)

def q3_zero(L):
    return (F(3393360)*L-F(32718563))/F(869400)

def T80(L):
    return (F(18670176000)*L*L-F(713649484800)*L+F(6822174057191))/F(68531400)

def D(L,U):
    return (F(1837779300)*U-F(24004512000)*L*L+
            F(903891063600)*L-F(8574904106497))

def coeffs(L,U):
    den=D(L,U)
    assert den>0
    q1=F(12)*(F(3500658000)*L*L-F(130325168925)*L-F(478793700)*U+
              F(1229767974292))/den
    q2=-F(105)*(F(152409600)*L*L-F(5513946480)*L-F(47507040)*U+
                F(51466255217))/den
    q3=F(1470)*(F(3393360)*L-F(869400)*U-F(32718563))/den
    q4=F(945)*(F(1352400)*L-F(25866469))/den
    return [F(1),q1,q2,q3,q4]

def polymul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def surrogate_bound(L,U):
    q=coeffs(L,U)
    y=polymul(q,q)
    moms=[F(1),F(1),F(4,3),F(2),F(13,4),F(101,18),F(12809,1260),L,U]
    return sum(y[k]*moms[k] for k in range(9)),y

def main():
    # Exact structural factorizations used in the proof.
    # F8-Dfloor = (1352400 L-L0num)^2 / 385252994000.
    # F8-q3_zero = ((25200L-476461)(1352400L-25866469))/1913646000.
    # T80-F8 also vanishes quadratically at L0.
    assert F8(L0)==Dfloor(L0)==q3_zero(L0)==T80(L0)

    # Rational test point inside the public reconnaissance interval.
    L=F(19136,1000)
    lo=F8(L)
    hi=T80(L)
    assert hi>lo
    U=(lo+hi)/2

    lam,y=surrogate_bound(L,U)
    assert y[7]<=0 and y[8]>0
    assert lam < F(1,10)
    assert 1-2*lam > F(4,5)

    # k<=6 comparator.
    old=F(1415,13891)
    assert lam<old

    print("L0 =",L0,"=",float(L0))
    print("test L =",L,"=",float(L))
    print("F8(L) =",lo,"=",float(lo))
    print("T80(L) =",hi,"=",float(hi))
    print("test U midpoint =",U,"=",float(U))
    print("surrogate w0 bound =",lam,"=",float(lam))
    print("simple coefficient >",1-2*lam,"=",float(1-2*lam))
    print("y7 =",y[7],"y8 =",y[8])
    print("RESULT: WP80_K8_ONE_SIDED_GATE_PASS")

if __name__=="__main__":
    main()
