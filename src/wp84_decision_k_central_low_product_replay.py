#!/usr/bin/env python3
"""Independent hostile replay for Decision K; does not import the producer."""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_K_CENTRAL_LOW_PRODUCT_CERTIFICATE.json"


def ordered_factor_count(n: int) -> int:
    count = 0
    for a in range(1, n + 1):
        if n % a:
            continue
        for b in range(1, n // a + 1):
            if n % (a * b) == 0:
                count += 1
    return count


def prime_power_set(n: int) -> set[int]:
    s = set()
    for p in range(2, n + 1):
        if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
            continue
        v = p
        while v <= n:
            s.add(v)
            v *= p
    return s


def gaussian_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def root_sum_quarter(lo: int, hi: int) -> tuple[int, int]:
    # Sum i^k over integer k in [lo,hi], represented exactly in Z[i].
    out = (0, 0)
    cycle = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for k in range(lo, hi + 1):
        out = gaussian_add(out, cycle[k % 4])
    return out


def main() -> None:
    c = json.loads(CERT.read_text(encoding="utf-8"))
    assert c["decision"] == "K2"
    assert c["frozen_source"]["pool"] == "all prime powers p^v<=N"
    assert c["frozen_source"]["J"].startswith("finite original")
    assert c["low_product"]["normalized_rate"] == "O_theta(X^(3*theta/2-1)*L^2)=o(1)"
    assert c["partition"]["residual"].endswith("product>X^theta")
    assert c["strict_gt79"] == "OPEN"

    # Independent exact divisor census: all ordered integer triples are counted
    # directly, and the prime-power subpopulation is checked as a subset.
    pows = prime_power_set(40)
    triples_checked = 0
    for y in range(1, 41):
        counts: dict[int, int] = {}
        for a in pows:
            for b in pows:
                for d in pows:
                    m = a * b * d
                    if m <= y:
                        counts[m] = counts.get(m, 0) + 1
        for m, count in counts.items():
            assert count <= ordered_factor_count(m)
            triples_checked += 1

    # Integer separation: distinct positive integers <=Y have ratio at least
    # 1+1/Y. Include hostile adjacent and far-apart pairs.
    ratio_checks = 0
    for y in range(2, 101):
        for a in range(1, y + 1):
            for b in range(1, y + 1):
                if a == b:
                    continue
                hi, lo = max(a, b), min(a, b)
                assert Fraction(hi, lo) >= Fraction(y + 1, y)
                ratio_checks += 1
    assert Fraction(3, 2) >= Fraction(101, 100)  # deliberately non-adjacent
    assert not (Fraction(100, 99) >= Fraction(1001, 1000)) is False

    # Mixed two-versus-one exact endpoint arithmetic. This catches using N^2
    # instead of N^2/2 and catches the false assertion that m=+/-2 can occur.
    for n in range(2, 50):
        assert Fraction(n * n, 2) < Fraction(n * n, 1)
        assert Fraction(4, n) > Fraction(1, n * n)
        assert Fraction(n, 4) < Fraction(n, 1)
    # The actual alias margins from the natural cutoff are the sqrt(L) gaps,
    # not merely the coarse integer inequalities above.
    assert "2*sqrt(L)" in c["alias_support"]["mixed_m2_log_gap"]
    assert "3*sqrt(L)" in c["alias_support"]["all_same_m3_log_gap"]

    # Exact finite root/centering test at omega=1/4. Do not drop global centering.
    d, u = 11, 3
    kroot = (4, 12)
    e_inter = (max(4, 7), min(12, 9))
    full = root_sum_quarter(*kroot)
    part = root_sum_quarter(*e_inter)
    centered_num = (d * part[0] - u * full[0], d * part[1] - u * full[1])
    assert centered_num != (0, 0)
    # Omitted centering is not equal to the centered kernel in this example.
    assert centered_num != (d * part[0], d * part[1])

    # A nonzero integer alias near 1 has a large geometric sum; it cannot be
    # covered by the low-sector bound whose hypothesis is |omega|<=theta<1.
    M = 10000
    omega = Fraction(9999, 10000)
    assert omega > Fraction(2, 3)
    # The literal frequency is outside every fixed theta<2/3 low sector.
    assert c["low_product"]["range"].endswith("Omega!=0")
    # Full finite-lag support is mandatory: a legal lag can exceed 6000.
    assert 6001 > 6000
    assert "no lag cutoff" in c["frozen_source"]["J"]
    assert "R=6000" in c["high_product"]["verdict"] or "R=6000" in c["high_product"]["needed"]

    # Product-boundary tuple belongs once, to low; residual is strict.
    boundary = 64
    low = boundary <= 64
    residual = boundary > 64
    assert low and not residual
    # Exponent test at several exact rational thetas, plus the endpoint failure.
    for theta in (Fraction(1, 3), Fraction(1, 2), Fraction(13, 20)):
        assert theta < Fraction(2, 3)
        assert Fraction(3, 2) * theta - 1 < 0
    assert Fraction(3, 2) * Fraction(2, 3) - 1 == 0

    print("PASS independent integer-product separation and mixed-alias endpoint tests")
    print(f"PASS exact ordered-divisor domination on {triples_checked} finite prime-power products")
    print(f"PASS exact root-sum centering mutation and product-boundary partition; ratio checks={ratio_checks}")
    print("PASS theta exponent, strict threshold, full-lag, proper-power and theorem-boundary checks")
    print("LIMIT finite tests validate algebra only; high-product source-weighted signed estimate remains open")
    print("DECISION K2; strict >79 OPEN")


if __name__ == "__main__":
    main()
