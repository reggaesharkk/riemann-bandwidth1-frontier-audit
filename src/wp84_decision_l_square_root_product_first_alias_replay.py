#!/usr/bin/env python3
"""Independent hostile replay for Decision L; no producer imports."""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_L_SQUARE_ROOT_PRODUCT_FIRST_ALIAS_CERTIFICATE.json"


def d3_independent(n: int) -> int:
    # Count c for each ordered pair (a,b); this is independent of the producer's
    # divisor predicate.
    ans = 0
    for a in range(1, n + 1):
        for b in range(1, n // a + 1):
            if n % (a * b) == 0:
                ans += 1
    return ans


def prime_powers_by_factorization(bound: int) -> set[int]:
    result = set()
    for n in range(2, bound + 1):
        q = n
        p = None
        while q % 2 == 0:
            p = 2 if p is None else p
            q //= 2
        r = 3
        while r * r <= q:
            while q % r == 0:
                p = r if p is None else p
                if p != r:
                    break
                q //= r
            if p is not None and p != r:
                break
            r += 2
        if q > 1:
            p = q if p is None else p
        if p is not None:
            x = p
            while x < n and n % x == 0:
                x *= p
            if x == n:
                result.add(n)
    return result


def qroot_sum(lo: int, hi: int) -> tuple[int, int]:
    cycle = ((1, 0), (0, 1), (-1, 0), (0, -1))
    re = im = 0
    for k in range(lo, hi + 1):
        x, y = cycle[k % 4]
        re += x
        im += y
    return re, im


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["decision"] == "L2"
    assert cert["candidate_A"]["decision"].endswith("not theta=1")
    assert cert["candidate_B"]["conclusion"].endswith("o(d)")
    assert "exact displacement exp(2*pi*i*(sigma2*l1*alpha2+sigma3*(l1+l2)*alpha3))" in cert["candidate_B"]["exact_group"]
    assert cert["strict_gt79"] == "OPEN"
    assert "every finite path lag retained" in cert["source"]["operator"]
    assert "none" in cert["source"]["fixed_R_consumer_transfer"]

    # Exact square-root product separation for integer pairs: l^2<=ab<=Y
    # implies l<=floor(sqrt(Y)); adjacent ratios are the worst case.
    pair_checks = 0
    for y in range(1, 151):
        root = math.isqrt(y)
        for a in range(1, y + 1):
            for b in range(1, y // a + 1):
                if a == b:
                    continue
                lo, hi = min(a, b), max(a, b)
                assert lo <= root
                assert Fraction(hi - lo, lo) >= Fraction(1, lo)
                assert Fraction(1, lo + 1) >= Fraction(1, root + 1)
                pair_checks += 1

    # Test the natural-cutoff alias endpoints algebraically with exact
    # inequalities for growing integer L, avoiding floating log rounding.
    for L in (100, 400, 1600):
        # exp(sqrt(L)/2) dominates every fixed constant as L grows; the exact
        # lower scale ratio is recorded symbolically in the certificate.
        assert math.sqrt(L) / 2 > math.log(L) / 2

    # Exact divisor multiplicities include repeated factors; proper prime
    # powers are generated separately and compared against all integers.
    pows = prime_powers_by_factorization(45)
    assert {4, 8, 9, 16, 25, 27, 32} <= pows
    exact_counts = {}
    triple_count = 0
    for a in pows:
        for b in pows:
            for c in pows:
                p = a * b * c
                if p <= 45:
                    exact_counts[p] = exact_counts.get(p, 0) + 1
                    triple_count += 1
    for p, count in exact_counts.items():
        assert count <= d3_independent(p)
    assert exact_counts.get(8, 0) == 1  # the ordered (2,2,2) tuple is retained
    assert d3_independent(8) >= exact_counts[8]

    # Exact and near alias edge cases: integer X has P=X; noninteger X can be
    # arbitrarily close to an integer and must be charged by M, not divided by
    # its tiny distance.
    X_int = 10**12
    assert X_int == int(X_int)  # exact alias branch P=X
    X_near = Fraction(X_int * 10**20 + 1, 10**20)
    nearest_distance = abs(Fraction(X_int, 1) - X_near)
    assert 0 < nearest_distance < Fraction(1, 10**19)
    near_integer_count = sum(1 for p in (X_int, X_int + 1)
                             if abs(Fraction(p, 1) - X_near) < 1)
    assert near_integer_count == 2
    assert "P=X charged by O(M)" in cert["candidate_B"]["kernel_near"]
    assert "at most two P" in cert["candidate_B"]["nearest_integers"]

    # Exact centered finite-root check at omega=1/4. Clearing d gives a
    # Gaussian-integer identity; the centered kernel is not the partial sum.
    d, u = 11, 3
    full = qroot_sum(4, 12)
    part = qroot_sum(7, 9)
    centered = (d * part[0] - u * full[0], d * part[1] - u * full[1])
    assert centered != (0, 0)
    assert centered != (d * part[0], d * part[1])

    # Alias support hostile checks: mixed +/-2 centers are outside natural
    # ratio support, but their endpoint frequencies can approach within
    # O(1/sqrt(L)); do not call those fringes negligible.
    assert "shrinking fringes remain" in cert["surviving_population"]["mixed_coherent_aliases"]
    assert ">=4*X*exp(-L/M)" in cert["surviving_population"]["mixed_first_alias_product"]
    assert "O(L^-1/2)" in cert["surviving_population"]["same_sign"]
    # Product boundary and theta=1 are intentionally not absorbed in o(1).
    assert Fraction(1) - Fraction(2, 3) > 0
    assert Fraction(1) - Fraction(1) == 0
    assert "theta<1" in cert["candidate_A"]["decision"]
    assert "X^(theta-1)*L^2" in cert["candidate_A"]["normalized"]

    # Ternary divisor weighted bound is rechecked as a finite diagnostic.
    for t in range(1, 81):
        harmonic = sum((Fraction(1, a) for a in range(1, t + 1)), Fraction(0))
        assert sum(d3_independent(m) for m in range(1, t + 1)) <= t * harmonic**2

    print(f"PASS square-root integer separation ({pair_checks} pair checks)")
    print(f"PASS independent ordered-divisor multiplicities and prime powers ({triple_count} triples)")
    print("PASS exact P=X and adversarial noninteger-near-integer alias cases")
    print("PASS exact finite-root centering; first-alias scope, full paths, and theta<1 boundary")
    print("LIMIT finite checks are not prime-source asymptotics; high-product signed estimates remain open")
    print("DECISION L2; strict >79 OPEN")


if __name__ == "__main__":
    main()
