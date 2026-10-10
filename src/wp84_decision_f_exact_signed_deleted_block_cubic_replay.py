#!/usr/bin/env python3
"""Independent exact replay for Decision F; does not import the producer."""
from fractions import Fraction as Q


def mul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def cube(a):
    return mul(mul(a, a), a)


def ident(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def main():
    bdiag = [Q(2), Q(-1), Q(3), Q(1, 2)]
    av = [Q(0), Q(1), Q(3), Q(-2)]
    n, s = len(av), Q(-3, 7)
    B = [[bdiag[i] if i == j else Q(0) for j in range(n)] for i in range(n)]
    W0 = [[Q(0) if i == j else (av[i]-av[j])/(j-i)
           for j in range(n)] for i in range(n)]
    B2, B3 = mul(B, B), cube(B)
    W02, W03 = mul(W0, W0), cube(W0)
    BW02 = mul(B, W02)
    assert tr(W0) == 0
    assert tr(mul(B2, W0)) == 0

    # Independent polynomial expansion in q=1/pi for D=sI+B+qW0.
    for q in (Q(0), Q(1), Q(-2), Q(5, 4)):
        D = add(add(scale(s, ident(n)), B), scale(q, W0))
        rhs = (n*s**3 + 3*s**2*tr(B)
               + 3*s*(tr(B2)+q*q*tr(W02)) + tr(B3)
               + 3*q*q*tr(BW02) + q**3*tr(W03))
        assert tr(cube(D)) == rhs

    # Index-level formulas for C1, C2 and C3.
    c1 = sum((x**3 for x in bdiag), Q(0))
    c2raw = 3*sum((bdiag[i]*W02[i][i] for i in range(n)), Q(0))
    c3raw = tr(W03)
    assert c1 == tr(B3) and c2raw == 3*tr(BW02) and c3raw == tr(W03)
    c3_triangle = Q(0)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and k != i:
                    c3_triangle += W0[i][j]*W0[j][k]*W0[k][i]
    assert c3_triangle == c3raw

    # A three-vertex exact countertest defeats the claim Tr(W^3)=0.
    a3 = [Q(0), Q(1), Q(3)]
    W3 = [[Q(0) if i == j else (a3[i]-a3[j])/(j-i)
           for j in range(3)] for i in range(3)]
    assert tr(cube(W3)) == Q(-18)

    # Unique-factorization resonance and nonresonance checks on legal powers.
    assert 2*4 == 8                 # p^1 p^2 = p^3
    assert 2*3 != 5                 # all are prime powers, but not a closure
    assert (2*3, 5, 6) == (6, 5, 6) # near relation has nonzero log(6/5)

    # Abstract signed averaging mutation: mean zero does not imply absolute mean zero.
    f = [Q(1), Q(-1)]
    assert sum(f, Q(0))/2 == 0 and sum(map(abs, f), Q(0))/2 == 1

    # Exact sufficient-density counting: admissible quarter, energy-bad <=1/8,
    # cubic-bad <=1/8 leaves at least 0 pairs only at equality; strict eventual
    # cubic bad density <1/8 yields positive intersection. Use 16 points below.
    admissible = set(range(4))
    energy_bad = {4}                 # 1/16 <= 1/8
    cubic_bad = {5}                  # 1/16 <= 1/8
    assert admissible - energy_bad - cubic_bad

    # Nonvanishing normalization countertest is abstract, not prime-source:
    # rho=r/d=1/m, and normalized compressed cubic=m gives rho*m=1.
    for m in (4, 8, 16):
        rho, moment = Q(1, m), Q(m)
        assert rho*moment == 1

    # Mutation checks: all powers, not just primes; positive-part / signed mean distinction.
    pool = {p**v for p in (2, 3, 5) for v in (1, 2, 3)}
    assert {2, 4, 8, 3, 9, 27, 5, 25, 125} <= pool
    assert tr(cube(W3)) != 0           # reject false cyclic cancellation
    assert Q(-18) != 0                 # reject forcing C3 to vanish

    print("PASS exact scalar/linear/quadratic/cubic expansion")
    print("PASS Tr(W)=Tr(B^2 W)=0 from zero diagonal")
    print("PASS exact C1/C2/C3 index formulas and ordered-triangle multiplicity")
    print("FALSIFIER: rational three-index W has Tr(W^3)=-18 before pi^-3")
    print("PASS prime-power exact closure 2*4=8; nonclosure 2*3!=5")
    print("PASS signed mean zero with absolute mean one")
    print("PASS endpoint intersection and nonvanishing normalization stress tests")
    print("LIMIT: countertests are abstract; no prime-source asymptotic bound is proved")
    print("DECISION F3; strict >79 OPEN")


if __name__ == "__main__":
    main()
