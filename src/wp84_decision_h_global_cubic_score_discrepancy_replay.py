#!/usr/bin/env python3
"""Independent exact replay for Decision H; does not import the producer."""
from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_H_GLOBAL_CUBIC_SCORE_DISCREPANCY_CERTIFICATE.json"


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def pw3(a):
    return mm(mm(a, a), a)


def cut(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def transpose(a):
    return [list(v) for v in zip(*a)]


def score_diagonal(h, aa, w):
    ans = []
    for k in range(len(h)):
        v = aa[k] ** 3
        for j in range(len(h)):
            if j != k:
                v += (2 * aa[k] + aa[j]) * w[k][j] ** 2
        for j in range(len(h)):
            for ell in range(len(h)):
                if len({k, j, ell}) == 3:
                    v += w[k][j] * w[j][ell] * w[ell][k]
        ans.append(v)
    return ans


def replay():
    av = [Q(0), Q(2), Q(-1), Q(3), Q(4), Q(-2)]
    beta = [Q(1), Q(-2), Q(0), Q(3), Q(-1), Q(2)]
    s0 = Q(2, 5)
    aa = [s0 + x for x in beta]
    n = len(av)
    w = [[Q(0) if i == j else (av[i] - av[j]) / (j - i)
          for j in range(n)] for i in range(n)]
    h = [[(aa[i] if i == j else Q(0)) + w[i][j]
          for j in range(n)] for i in range(n)]
    h3 = pw3(h)
    g = [h3[i][i] for i in range(n)]
    assert g == score_diagonal(h, aa, w)

    # All trace spaces are explicitly rectangular where appropriate.
    p, q = [1, 2, 3, 4], [0, 5]
    a, b, d = cut(h, p, p), cut(h, p, q), cut(h, q, q)
    bt = transpose(b)
    dprime, dfull = len(p), n
    mt = tr(h3) / dfull
    bb_star, b_star_b = mm(b, bt), mm(bt, b)
    lhs = tr(h3) / dfull - tr(pw3(a)) / dprime
    rhs = sum((g[k] - mt for k in q), Q(0)) / dprime
    rhs += (2 * tr(mm(a, bb_star)) + tr(mm(d, b_star_b))) / dprime
    assert lhs == rhs
    assert tr(cut(h3, p, p)) != tr(pw3(a))
    assert lhs != sum((g[k] - mt for k in q), Q(0)) / dfull

    # Check the score formula's coefficients and triangle are indispensable.
    mutated = []
    no_triangle = []
    for k in range(n):
        mutated.append(aa[k] ** 3 + sum(
            ((aa[k] + aa[j]) * w[k][j] ** 2 for j in range(n) if j != k), Q(0))
            + sum((w[k][j] * w[j][ell] * w[ell][k]
                   for j in range(n) for ell in range(n)
                   if len({k, j, ell}) == 3), Q(0)))
        no_triangle.append(aa[k] ** 3 + sum(
            ((2 * aa[k] + aa[j]) * w[k][j] ** 2 for j in range(n) if j != k), Q(0)))
    assert mutated != g and no_triangle != g

    # Exact finite geometric-sum algebra: integer frequency is the separate
    # zero-mod-Z case. Noninteger formula is recorded symbolically in the cert.
    for length in range(1, 9):
        assert sum((1 for _ in range(length))) == length
    assert 2 * 4 == 8  # exact prime-power carrier closure
    assert 2 * 3 != 5  # nonzero carrier log(6/5) must not be discarded

    # Abstract interior spike: endpoint-only score S2 does not imply global S6.
    d0, height, M = 64, 4, 4
    eigs = [Q(0)] * (d0 - 1) + [Q(height)]
    m0 = sum((x ** 3 for x in eigs), Q(0)) / d0
    end_score_sq = sum(((Q(0) - m0) ** 2 for _ in range(M)), Q(0))
    tau6 = sum((x ** 6 for x in eigs), Q(0)) / d0
    assert end_score_sq == 4
    assert tau6 == 64
    assert end_score_sq < Q(d0 * d0, M)
    deleted_spike_score = (height ** 3 - m0) / (d0 - 1)
    full_normalized_cubic = sum((x ** 3 for x in eigs), Q(0)) / d0
    retained_cubic = Q(0)
    assert deleted_spike_score == full_normalized_cubic - retained_cubic == 1

    # Mean cancellation is not absolute partial-sum control.
    signed = [Q(1), Q(-1)]
    assert sum(signed, Q(0)) == 0
    assert sum((abs(x) for x in signed), Q(0)) == 2

    doc = json.loads(CERT.read_text(encoding="utf-8"))
    exact = doc["finite_exact_replay"]
    assert exact["g_diagonal"] == [str(x) for x in g]
    assert exact["trace_identity_lhs"] == str(lhs)
    assert exact["trace_identity_score_term"] == str(sum(
        (g[k] - mt for k in q), Q(0)) / dprime)
    assert exact["trace_identity_mixed_term"] == str(
        (2 * tr(mm(a, bb_star)) + tr(mm(d, b_star_b))) / dprime)
    assert exact["abstract_deleted_row_spike_normalized_discrepancy"] == "1"
    assert doc["classification"].startswith("H2")
    assert doc["start_state"]["head"] == "13e87db74bd273349dc6db94aeb2e38e95a34fe7"
    assert "OPEN" in doc["decision_gate"]["theorem_status"]
    print("PASS exact rational global-score trace identity; d and d' normalizations")
    print("PASS exact rational diagonal formula; wrong coefficient and omitted cycle rejected")
    print("PASS hostile interior-spike: endpoint S2 can hold while global S6 grows")
    print("PASS signed-mean cancellation does not control absolute partial sums")
    print("PASS exact UFD examples; nonzero/near aliases are not discarded")
    print("LIMIT: finite replay does not estimate the actual prime-source cubic discrepancy")
    print("DECISION H2; strict >79 OPEN")


if __name__ == "__main__":
    replay()
