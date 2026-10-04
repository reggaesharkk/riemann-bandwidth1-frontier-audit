#!/usr/bin/env python3
"""
WP80 exact Stieltjes moment-cone lower bound for m7.

Assume a nonnegative measure nu on [0, infinity) with the exact moments

    m0 = 1
    m1 = 1
    m2 = 4/3
    m3 = 2
    m4 = 13/4
    m5 = 101/18
    m6 = 12809/1260.

For every cubic r(x),

    int x r(x)^2 dnu(x) >= 0.

Using the shifted Hankel matrix H = (m_{i+j+1})_{0<=i,j<=3},
the Schur-complement optimum in the unknown m7 is exact:

    m7 >= 25866469 / 1352400
       = 19.126345016267...

A witness polynomial is

    r(x) = x^3 - (3142/805)x^2 + (517/115)x - 13891/9660,

for which

    int x r(x)^2 dnu
      = m7 - 25866469/1352400.

This is exact rational algebra only.  It does not certify the analytic
transport of m5 or m6; it strengthens the consumer-side consequence once
those moment premises are available.
"""

from fractions import Fraction as F


M = {
    0: F(1),
    1: F(1),
    2: F(4, 3),
    3: F(2),
    4: F(13, 4),
    5: F(101, 18),
    6: F(12809, 1260),
}


def det(a):
    a = [row[:] for row in a]
    n = len(a)
    out = F(1)
    sign = 1
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            sign *= -1
        p = a[j][j]
        out *= p
        for i in range(j + 1, n):
            q = a[i][j] / p
            for k in range(j, n):
                a[i][k] -= q * a[j][k]
    return sign * out


def solve(a, b):
    n = len(a)
    aug = [a[i][:] + [b[i]] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        p = aug[j][j]
        aug[j] = [x / p for x in aug[j]]
        for i in range(n):
            if i == j:
                continue
            q = aug[i][j]
            if q:
                aug[i] = [aug[i][k] - q * aug[j][k] for k in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def polymul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def main():
    # Top-left 3x3 block of the shifted Hankel matrix.
    a = [[M[i + j + 1] for j in range(3)] for i in range(3)]
    v = [M[4], M[5], M[6]]

    # Sylvester criterion: a is positive definite.
    minors = [det([row[:k] for row in a[:k]]) for k in range(1, 4)]
    assert minors == [F(1), F(2, 9), F(23, 1296)]

    # Schur-complement minimizer.
    c = solve(a, v)
    assert c == [F(13891, 9660), F(-517, 115), F(3142, 805)]

    lower = sum(v[i] * c[i] for i in range(3))
    assert lower == F(25866469, 1352400)

    # r(x) = x^3 - c0 - c1*x - c2*x^2, ascending coefficients.
    r = [-c[0], -c[1], -c[2], F(1)]
    r2 = polymul(r, r)

    # Integral of x*r(x)^2.  The m7 coefficient is exactly one.
    assert r2[6] == 1
    known = sum(r2[k] * M[k + 1] for k in range(6))
    assert known == -lower

    print("shifted-Hankel leading minors =", minors)
    print("Schur coefficients =", c)
    print("witness r(x) = x^3 - (3142/805)x^2 + (517/115)x - 13891/9660")
    print("m7_lower =", lower, "=", float(lower))
    print("identity: integral x*r(x)^2 dnu = m7 -", lower)
    print("RESULT: WP80_EXACT_M7_MOMENT_CONE_PASS")


if __name__ == "__main__":
    main()
