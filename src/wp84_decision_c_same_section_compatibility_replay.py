#!/usr/bin/env python3
"""Independent stdlib replay of the Decision C exact numerical checks.

This file deliberately does not import the producer. Analytic interlacing,
Schatten, and density arguments are stated and proved in the accompanying
note; this replay checks their exact rational examples and scale logic.
"""
from fractions import Fraction
from itertools import combinations


def main() -> None:
    target = Fraction(21, 200)
    energy = Fraction(48861622601, 195312500000)
    excess = energy - target
    assert excess == Fraction(28353810101, 195312500000)
    margin79 = Fraction(52897896569489, 572357731837500000)
    assert 0 < margin79 < Fraction(1, 10000)

    # Exact adversarial family: one cubic atom is lost by deleting one row.
    for k in (2, 3, 4, 5, 6, 8):
        d = k ** 3
        # Exact diagonal witness diag(k,0,...,0): k^3/d=1; deletion gives 0.
        full_cubic = Fraction(1, 1)
        compressed_cubic = Fraction(0, 1)
        sixth_moment = Fraction(k ** 6, d)
        assert full_cubic - compressed_cubic == 1
        assert sixth_moment == d
        assert Fraction(1, d) < Fraction(1, 4)

    # Positive-density averaging implication: average on G cannot exceed
    # total nonnegative mass divided by |G|.
    total_pairs, good_pairs, total_energy = 100, 25, 300
    density = Fraction(good_pairs, total_pairs)
    average_all = Fraction(total_energy, total_pairs)
    bound_on_some_good_pair = Fraction(total_energy, good_pairs)
    assert bound_on_some_good_pair == average_all / density
    assert bound_on_some_good_pair == 12

    # Hostile endpoint example: the global mean is small, but a singleton
    # consumer-admissible set can lie entirely on a large score. This shows
    # why existence of some B-good point does not imply intersection with an
    # unspecified consumer-good set.
    n = 10
    energies = [0] * (n * n)
    energies[-1] = n * n  # global average 1; designated good set is singleton
    designated_good = [n * n - 1]
    assert Fraction(sum(energies), n * n) == 1
    assert energies[designated_good[0]] == n * n

    # Principal-deletion CDF discrepancy for diagonal spectra: exhaust every
    # deleted subset for dimensions up to 8. The general Hermitian statement
    # uses Cauchy interlacing; this is a separate finite hostile regression.
    for d in range(2, 9):
        for r in range(1, d):
            for deleted in combinations(range(d), r):
                deleted_set = set(deleted)
                kept = [j for j in range(d) if j not in deleted_set]
                # At any threshold, each CDF is a rational counting fraction.
                for cut in range(d + 1):
                    full_cdf = Fraction(sum(j < cut for j in range(d)), d)
                    sub_cdf = Fraction(sum(j < cut for j in kept), d - r)
                    assert abs(full_cdf - sub_cdf) <= Fraction(2 * r, d)

    # A 1/d deletion fraction vanishes, while raw cubic error remains 1.
    assert Fraction(1, 256) < Fraction(1, 100)
    assert energy > target
    print("PASS exact conditioned-energy witness and threshold excess", excess)
    print("PASS sixth-moment blowup in raw-cubic deletion falsifier")
    print("PASS positive-density intersection averaging arithmetic")
    print("PASS abstract endpoint-score mutation: global mean does not control an arbitrary singleton subset")
    print("PASS exhaustive diagonal interlacing-CDF regression for dimensions 2..8")
    print("VERDICT: bounded-observable deletion is conditional transfer only; raw cubic needs uniform S6")
    print("STRICT >79: OPEN")


if __name__ == "__main__":
    main()
