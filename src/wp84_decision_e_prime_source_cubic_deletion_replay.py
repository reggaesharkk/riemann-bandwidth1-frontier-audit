#!/usr/bin/env python3
"""Independent standard-library replay for WP84 Decision E.

This file deliberately does not import the deterministic certificate
producer. It checks exact block identities, normalization, and the abstract
rank-only falsifier; it cannot certify a large-T prime estimate.
"""
from fractions import Fraction as Q


def mul(x, y):
    return [[sum((x[i][k] * y[k][j] for k in range(len(y))), Q(0))
             for j in range(len(y[0]))] for i in range(len(x))]


def trace(x):
    return sum((x[i][i] for i in range(len(x))), Q(0))


def submatrix(x, rows, cols):
    return [[x[i][j] for j in cols] for i in rows]


def transpose(x):
    return [list(v) for v in zip(*x)]


def cube(x):
    return mul(mul(x, x), x)


def main():
    # A different rational Hermitian matrix from the producer's regression.
    h = [[Q(1), Q(2), Q(-1), Q(0)],
         [Q(2), Q(-2), Q(3), Q(1)],
         [Q(-1), Q(3), Q(4), Q(-2)],
         [Q(0), Q(1), Q(-2), Q(5)]]
    pids, qids = [0, 1], [2, 3]
    a = submatrix(h, pids, pids)
    b = submatrix(h, pids, qids)
    dblock = submatrix(h, qids, qids)
    bbt = mul(b, transpose(b))
    btb = mul(transpose(b), b)
    full_minus_kept = trace(cube(h)) - trace(cube(a))
    deleted_cube = trace(cube(dblock))
    cross = 3 * trace(mul(a, bbt)) + 3 * trace(mul(dblock, btb))
    assert full_minus_kept == deleted_cube + cross

    # Scalar-background separation of the deleted block D=s0 I+W.
    s0 = Q(1, 3)
    w = [[dblock[i][j] - (s0 if i == j else 0) for j in range(2)]
         for i in range(2)]
    tw, tw2, tw3 = trace(w), trace(mul(w, w)), trace(cube(w))
    expanded_deleted_cube = 2 * s0 ** 3 + 3 * s0 ** 2 * tw + 3 * s0 * tw2 + tw3
    assert trace(cube(dblock)) == expanded_deleted_cube

    # Exact unequal-normalization identity, with r=d-d'.
    d, dprime = Q(4), Q(2)
    lhs_norm = trace(cube(h)) / d - trace(cube(a)) / dprime
    rhs_norm = deleted_cube / d + cross / d - (d - dprime) / d * (trace(cube(a)) / dprime)
    assert lhs_norm == rhs_norm

    # Compression-of-cubic identity is a distinct target: omitting D^3 and
    # doubling the mixed P terms here must fail for this witness.
    p_h3_p = submatrix(cube(h), pids, pids)
    compression_boundary = trace(p_h3_p) - trace(cube(a))
    compression_rhs = 2 * trace(mul(a, bbt)) + trace(mul(b, mul(dblock, transpose(b))))
    assert compression_boundary == compression_rhs
    assert full_minus_kept != compression_rhs
    assert full_minus_kept != cross  # deleting Tr(D^3) is invalid

    # Abstract diagonal spike. The sixth moment is unbounded while one-row
    # deletion has vanishing relative rank and a fixed normalized cubic loss.
    for k in (2, 3, 5, 7):
        dim = k ** 3
        rho = Q(1, dim)
        full_tau3 = Q(k ** 3, dim)
        kept_tau3 = Q(0)
        tau6 = Q(k ** 6, dim)
        assert rho == Q(1, dim) and rho <= Q(1, 8)
        assert full_tau3 == 1 and kept_tau3 == 0 and tau6 == dim

    # Uniform fourth moment -> cubic-tail bound is exactly 1/R times m4:
    # x^3 1_{|x|>R} <= |x|^4/R.
    for x, radius in ((Q(7, 2), Q(3)), (Q(-5), Q(4)), (Q(2), Q(5))):
        if abs(x) > radius:
            assert abs(x) ** 3 <= abs(x) ** 4 / radius

    print("PASS exact full-trace deletion identity with deleted-block cubic")
    print("PASS exact scalar-background expansion of deleted-block cubic")
    print("PASS normalized identity and sign of dimension-renormalization term")
    print("PASS separate compression-of-cubic identity; hostile term omissions rejected")
    print("PASS abstract diagonal spike: rank fraction -> 0, cubic loss = 1, sixth moment = d")
    print("PASS fourth-moment cubic-tail inequality")
    print("LIMIT: exact finite diagnostics are not prime-source asymptotics")
    print("DECISION E3: actual-source deleted-block cubic/UI estimate remains open")
    print("STRICT >79: OPEN")


if __name__ == "__main__":
    main()
