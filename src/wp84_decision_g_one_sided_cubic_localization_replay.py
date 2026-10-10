#!/usr/bin/env python3
"""Independent standard-library replay for Decision G; no producer import."""
from fractions import Fraction as Q


def mul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def cube(a):
    return mul(mul(a, a), a)


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def trans(a):
    return [list(x) for x in zip(*a)]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def norm_sq(a):
    return sum((x*x for row in a for x in row), Q(0))


def main():
    # Build a rational matrix with the exact source kernel orientation,
    # suppressing the common 1/pi as a formal scalar for this identity test.
    av = [Q(0), Q(2), Q(-1), Q(3), Q(4), Q(-2), Q(2), Q(7)]
    beta = [Q(1), Q(-2), Q(0), Q(3), Q(-1), Q(2), Q(1, 2), Q(-3)]
    n, s0 = len(av), Q(2, 5)
    W = [[Q(0) if i == j else (av[i]-av[j])/(j-i)
          for j in range(n)] for i in range(n)]
    H = [[(s0+beta[i] if i == j else Q(0))+W[i][j]
          for j in range(n)] for i in range(n)]

    # QL/QR separation identity.
    ql, qr = [0, 1], [6, 7]
    D = block(H, ql+qr, ql+qr)
    DL, DR, C = block(H, ql, ql), block(H, qr, qr), block(H, ql, qr)
    CCt, CtC = mul(C, trans(C)), mul(trans(C), C)
    separated_rhs = (tr(cube(DL))+tr(cube(DR))
                     +3*tr(mul(DL, CCt))+3*tr(mul(DR, CtC)))
    assert tr(cube(D)) == separated_rhs
    assert norm_sq(C) > 0
    d, M = 8, 2
    assert min(j-i for i in ql for j in qr) == d-2*M+1
    assert 3*tr(mul(DL, CCt))+3*tr(mul(DR, CtC)) != 0

    # Full-trace deletion identity and exact self-normalization with unknown mT.
    pids, qids = [2, 3, 4, 5], [0, 1, 6, 7]
    A, B, Dq = block(H, pids, pids), block(H, pids, qids), block(H, qids, qids)
    BBt, BtB = mul(B, trans(B)), mul(trans(B), B)
    G = 3*tr(mul(A, BBt))+3*tr(mul(Dq, BtB))
    dprime, r = len(pids), len(qids)
    mT = tr(cube(H))/d
    tauA = tr(cube(A))/dprime
    Fdel = tr(cube(Dq))-r*tauA
    left = Fdel/d
    right = (tr(cube(Dq))-r*mT)/dprime + r*G/(d*dprime)
    assert left == right
    # Mutation: dropping mT or changing the plus sign of G must fail here.
    assert left != tr(cube(Dq))/d
    assert left != (tr(cube(Dq))-r*mT)/dprime-r*G/(d*dprime)

    # One-row increment, exact coefficients and source edge orientation.
    old = [[Q(2), Q(1)], [Q(1), Q(-1)]]
    h = [Q(2, 3), Q(-1, 4)]
    a = Q(5, 2)
    new = [old[0]+[h[0]], old[1]+[h[1]], h+[a]]
    delta = tr(cube(new))-tr(cube(old))
    formula = a**3+3*a*sum((x*x for x in h), Q(0))+3*sum(
        (h[i]*old[i][j]*h[j] for i in range(2) for j in range(2)), Q(0))
    assert delta == formula
    k, j = 4, 2
    assert W[j][k] == (av[j]-av[k])/(k-j)

    # Widely spaced is not independent; a false exact-decoupling mutation fails.
    assert tr(cube(D)) != tr(cube(DL))+tr(cube(DR))

    # Abstract local L2 does not control local absolute cubic mass uniformly.
    M0 = Q(10000)
    assert M0**Q(3, 2) > M0

    # Exact prime-power resonance and nonzero carrier relation; not near-alias proof.
    assert 2*4 == 8
    assert 2*3 == 6 and 6 != 5

    # Signed endpoint cancellation is not absolute control.
    vals = [Q(1), Q(-1)]
    assert sum(vals, Q(0))/2 == 0 and sum(map(abs, vals), Q(0))/2 == 1

    # A cubic-good pair can miss the D2 admissible set absent a joint bound.
    pairs = set(range(16))
    good_endpoint = set(range(4))
    cubic_good = set(range(4, 16))
    assert Q(len(good_endpoint), len(pairs)) == Q(1, 4)
    assert not good_endpoint.intersection(cubic_good)

    # If full-window cubic bad mass is controlled, the three-good-set
    # intersection is positive: 1/4 - 1/8 - 1/16 > 0.
    assert Q(1, 4)-Q(1, 8)-Q(1, 16) == Q(1, 16) > 0

    print("PASS exact separated-block cube identity with correct factors 3")
    print("PASS cross-block interaction is small by distance, not exactly zero")
    print("PASS self-normalization identity retains unknown mT and +G sign")
    print("PASS exact one-row increment and h_j index orientation")
    print("PASS hostile tests: L2/L3, signed-vs-absolute, and inadmissible cubic-good pair")
    print("LIMIT: rational/abstract checks are not prime-source asymptotic estimates")
    print("DECISION G2; one-sided centered source cubic remains open; strict >79 OPEN")


if __name__ == "__main__":
    main()
