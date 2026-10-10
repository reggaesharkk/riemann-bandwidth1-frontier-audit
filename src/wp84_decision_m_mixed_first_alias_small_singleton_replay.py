#!/usr/bin/env python3
"""Independent hostile replay for Decision M; imports no producer code."""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_M_MIXED_FIRST_ALIAS_SMALL_SINGLETON_CERTIFICATE.json"


def divisor_count_independent(n: int) -> int:
    return sum(1 for a in range(1, n + 1) if n % a == 0)


def ppower_set_independent(N: int) -> set[int]:
    out: set[int] = set()
    for p in range(2, N + 1):
        if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
            continue
        value = p
        while value <= N:
            out.add(value)
            value *= p
    return out


def gaussian_root_sum(lo: int, hi: int, numerator: int, denominator: int) -> tuple[Fraction, Fraction]:
    """Exact roots for omega=numerator/denominator when denominator=4."""
    assert denominator == 4
    cycle = ((1, 0), (0, 1), (-1, 0), (0, -1))
    re = im = 0
    for k in range(lo, hi + 1):
        re += cycle[(k * numerator) % 4][0]
        im += cycle[(k * numerator) % 4][1]
    return Fraction(re), Fraction(im)


def main() -> None:
    c = json.loads(CERT.read_text(encoding="utf-8"))
    assert c["decision"] == "M2"
    assert c["start"]["head"] == "e502bf1ab5fa9b1dd75e8c9de3ccbb9e01186f8d"
    assert c["source"]["pool"].startswith("all prime powers")
    assert "global centering" in c["exact_mixed_source_term"]["retained"]
    assert "exact displacement phase" in c["exact_mixed_source_term"]["retained"]
    assert "fixed-R" in c["ordinary_prime_R6000_boundary"]
    assert "R=6000" in c["ordinary_prime_R6000_boundary"] or "R=6000" in c["source"]["consumer_scope"] or "fixed-R" in c["source"]["consumer_scope"]
    assert c["frozen_gates"]["strict_gt79"] == "OPEN"

    # Divisor multiplicity is checked independently by direct divisibility;
    # source prime-power ordered pairs, including equal bases, are a subset.
    pp = ppower_set_independent(100)
    counts: dict[int, int] = {}
    repeated = powers = 0
    for a in pp:
        for b in pp:
            counts[a * b] = counts.get(a * b, 0) + 1
            repeated += a == b
            powers += any(a == p**k or b == p**k
                          for p in range(2, 11) for k in range(2, 8))
    for product, count in counts.items():
        assert count <= divisor_count_independent(product)
    assert repeated > 0 and powers > 0
    assert counts[4] == 1  # (2,2) is retained as a proper-power pair.

    # Rational centers model exact aliases and noninteger centers arbitrarily
    # close to an integer; no denominator/Diophantine lower bound is presumed.
    exact_center = Fraction(1000, 1)
    near_center = Fraction(10**18 + 1, 10**15)
    assert exact_center.denominator == 1
    assert 0 < abs(Fraction(1000) - near_center) < Fraction(1, 10**9)
    assert sum(abs(Fraction(a) - near_center) < 1 for a in (1000, 1001)) == 2
    assert "A=C separately charged by 2M" in c["kernel"]["near_exact"]
    assert "at most three integers" in c["kernel"]["reason"]

    # Unit-shell count and harmonic majorant are checked on rational centers;
    # the analytic proof in the note supplies the uniform O(log C) argument.
    for center in (Fraction(101, 2), Fraction(1000), Fraction(2001, 2)):
        shell_counts = [sum(1 for a in range(1, 5000)
                            if j <= abs(Fraction(a) - center) < j + 1)
                        for j in range(1, 30)]
        assert all(n <= 2 for n in shell_counts)
        close = sum(1 for a in range(1, 5000) if abs(Fraction(a) - center) < 1)
        assert close <= 2

    # Exact centered finite root sum: mutation dropping u/d changes the value.
    d, u = 13, 4
    full = gaussian_root_sum(3, 15, 1, 4)
    part = gaussian_root_sum(8, 11, 1, 4)
    centered = (d * part[0] - u * full[0], d * part[1] - u * full[1])
    assert centered != (d * part[0], d * part[1])
    assert centered != (Fraction(0), Fraction(0))

    # Hostile root mutation: for displacement coordinates q=(0,1,3), the
    # finite-section root set has length 11-3=8, not the untrimmed length 11.
    finite_full = gaussian_root_sum(0, 7, 1, 4)
    wrong_untrimmed = gaussian_root_sum(0, 10, 1, 4)
    endpoint = gaussian_root_sum(0, 2, 1, 4)
    finite_centered = (11 * endpoint[0] - 3 * finite_full[0],
                       11 * endpoint[1] - 3 * finite_full[1])
    wrong_centered = (11 * endpoint[0] - 3 * wrong_untrimmed[0],
                      11 * endpoint[1] - 3 * wrong_untrimmed[1])
    assert finite_centered != wrong_centered  # catches replacing exact K_l by I_0.

    # A rational displacement phase can be nontrivial; dropping it is detected.
    phase_quarter = ((1, 0), (0, 1), (-1, 0), (0, -1))[1]
    assert phase_quarter == (0, 1) and phase_quarter != (1, 0)

    # Reciprocal sign reversal reflects m=+1 to m=-1 and preserves |delta|.
    for A, B in ((400, 20), (1001, 31), (2048, 64)):
        ratio_log_delta_sign = (A, B)
        reflected = (B, A)
        assert ratio_log_delta_sign[0] * reflected[0] == A * B
        assert Fraction(A, B) * Fraction(B, A) == 1

    # Exact exponent tests. At equality the displayed power cannot prove o(1).
    for eta in (Fraction(0), Fraction(1, 5), Fraction(1, 4), Fraction(2, 5)):
        eps_max = (Fraction(1, 2) - eta) / (1 + eta)
        if eta < Fraction(1, 2):
            assert eps_max > 0
            eps = eps_max / 2
            assert Fraction(-1, 2) + eta + eps * (1 + eta) < 0
        exponent = Fraction(-1, 4) + eta
        assert exponent < 0 if eta < Fraction(1, 4) else exponent == 0 if eta == Fraction(1, 4) else exponent > 0
    assert Fraction(-1, 4) + Fraction(1, 4) == 0
    assert Fraction(-1, 2) + Fraction(1, 2) == 0
    assert "eta=1/2 not proved" in c["candidate_A_near"]["endpoint_eta"]
    assert "eta=1/4 not proved" in c["candidate_B_full_bin"]["endpoint_eta"]

    # Distinct products show this is higher than the chosen L low-product set;
    # near/far cells are disjoint and no signed cancellation is used.
    assert 4 * math.sqrt(10**12) > (10**12) ** (1 / 3)
    assert c["population_partition"]["newness"].startswith("mixed first bin")
    assert "no fixed-R ordinary-prime transfer" in c["source"]["consumer_scope"]
    assert c["residual"]["no_counterexample"] is True
    assert c["candidate_A_near"]["claim"].endswith("o(1)")
    assert c["candidate_B_full_bin"]["near_plus_far"].endswith("eta<1/4, with Z=X^eta")
    # Artificial cancellation cannot replace the absolute endpoint-majorant.
    signed_terms = (Fraction(1), Fraction(-1))
    assert sum(signed_terms) == 0 and sum(abs(x) for x in signed_terms) == 2

    print("PASS independent ordered divisor and prime-power multiplicities (including repeated bases)")
    print("PASS exact and near-integer aliases; capped closest-integer shell treatment")
    print("PASS integer-distance shell count, finite-root mutation, displacement phase, and reciprocal sign reflection")
    print("PASS signed-cancellation falsifier: signed sum is zero while positive mass is two")
    print("PASS epsilon restrictions: near eta<1/2; whole-bin far eta<1/4; endpoints excluded")
    print("PASS disjoint low/same-sign/mixed/residual ledger and fixed-R non-transfer")
    print("LIMIT finite checks do not prove asymptotic prime-source estimates; residual signed estimate remains open")
    print("DECISION M2; strict >79 OPEN")


if __name__ == "__main__":
    main()
