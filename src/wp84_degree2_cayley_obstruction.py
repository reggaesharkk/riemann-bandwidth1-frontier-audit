#!/usr/bin/env python3
"""Exact dual certificate excluding every degree-2 Cayley majorant."""
import sympy as sp

def main():
    x=sp.symbols("x", real=True)

    # Exact model moments of [1, cos theta, sin theta, cos2theta, sin2theta].
    m=sp.Matrix([
        1,
        -sp.Rational(164937945,1707336793),
        sp.Rational(1372449200,1707336793),
        -sp.Rational(1307813823907483055,2914998924731524849),
        sp.Rational(107171791159706464,2914998924731524849),
    ])

    pts=[
        sp.Rational(63,50),
        sp.Rational(5,4),
        sp.Rational(51,200),
        sp.Rational(1,4),
        -sp.Rational(17,5),
    ]

    def phi(t):
        c=(t*t-1)/(t*t+1)
        s=2*t/(t*t+1)
        return sp.Matrix([
            1,
            c,
            s,
            sp.simplify(c*c-s*s),
            sp.simplify(2*c*s),
        ])

    A=sp.Matrix.hstack(*[phi(t) for t in pts])
    lam=A.LUsolve(m)

    expected=[
      sp.Rational(
        387171110253290672241298027,
        919222173922473455238327800
      ),
      sp.Rational(
        1834489883571625240911761,
        6905329292800810288696704
      ),
      sp.Rational(
        4657455326768729568018424151,
        22728650051982882090692101600
      ),
      sp.Rational(
        258108011731484438197093,
        2751012745221828187094656
      ),
      sp.Rational(
        242761394878395404388960772,
        16853399278237477620234625515
      ),
    ]

    assert list(lam)==expected
    assert all(v>0 for v in lam)
    assert sp.simplify(sum(lam)-1)==0
    assert A*lam==m

    Ast=sp.Rational(82,25)
    b=sp.Rational(9,4)

    def defect(t):
        return sp.factor(
            (t*t-Ast*t+b)**2
            /
            ((t*t+1)*(t*t+b*b))
        )

    L=sp.factor(sum(lam[j]*defect(pts[j]) for j in range(5)))

    expected_L=sp.Rational(
      202255841048454875843203393363533529,
      1212298386228020210032390410776980000
    )
    assert L==expected_L

    gap=sp.factor(L-sp.Rational(653,4000))
    expected_gap=sp.Rational(
      543516187091322069426957350523943,
      151537298278502526254048801347122500
    )
    assert gap==expected_gap
    assert gap>0

    print("dual weights:")
    for v in lam:
        print(" ",v,"~",float(v))
    print("degree-2 lower bound =",L,"~",float(L))
    print("gap above 0.16325 =",gap,"~",float(gap))
    print("RESULT: WP84_DEGREE2_CAYLEY_OBSTRUCTION_PASS")

if __name__=="__main__":
    main()
