#!/usr/bin/env python3
"""Independent exact hostile replay for WP84 Decision D.

No imports from the producer. Arrays below are explicitly abstract tests;
the source theorem is the localized MV/Sobolev derivation in the note.
"""
from fractions import Fraction


def avg(xs):
    return sum(xs, Fraction(0)) / len(xs)


def main() -> None:
    # The pair density from two half-dense endpoint sets is exactly >= 1/4.
    lower_good = [True, True, False, False]
    upper_good = [True, False, True, False]
    G = [(u, v) for u, a in enumerate(lower_good)
         for v, b in enumerate(upper_good) if a and b]
    assert Fraction(len(G), 16) == Fraction(1, 4)

    # Finite Markov regressions: a nonnegative endpoint score with mean m has
    # at least half its equally weighted points at score <= 2m.
    for n in range(1, 7):
        for code in range(1 << n):
            vals = [Fraction((code >> j) & 1) * (j + 1) for j in range(n)]
            m = avg(vals)
            good = n if m == 0 else sum(x <= 2 * m for x in vals)
            assert Fraction(good, n) >= Fraction(1, 2)

    # Hostile score-energy anticorrelation: concentrate all crossing energy on
    # admissible pairs. Restriction costs precisely 1/gamma, no independence.
    gamma = Fraction(len(G), 16)
    energies = [Fraction(0) for _ in range(16)]
    for u, v in G:
        energies[4 * u + v] = Fraction(64, 1)  # global mean 16; G mean 64
    assert avg(energies) == 16
    assert avg([energies[4 * u + v] for u, v in G]) == 64
    assert avg([energies[4 * u + v] for u, v in G]) == avg(energies) / gamma

    # Shrinking-density stress test saturates C/gamma exactly.
    for n in (2, 5, 20, 100):
        vals = [Fraction(0) for _ in range(n)]
        vals[-1] = Fraction(n)  # global average 1
        g = [n - 1]  # density 1/n
        assert avg(vals) == 1
        assert avg([vals[i] for i in g]) == Fraction(1, 1) / Fraction(1, n)

    # Weighted-measure mutation: unweighted density is 1/2, but actual mass
    # is 1/100. An unweighted density argument would understate the cost.
    weights = [Fraction(99, 100), Fraction(1, 100)]
    E = [Fraction(0), Fraction(100)]
    G_weighted = [1]
    weighted_mean = sum((w * e for w, e in zip(weights, E)), Fraction(0))
    good_mass = sum((weights[i] for i in G_weighted), Fraction(0))
    conditional = sum((weights[i] * E[i] for i in G_weighted), Fraction(0)) / good_mass
    assert weighted_mean == 1 and good_mass == Fraction(1, 100)
    assert conditional == weighted_mean / good_mass == 100
    assert Fraction(len(G_weighted), len(weights)) == Fraction(1, 2)

    # Coupled-pair counterexample: each marginal projection is full, but the
    # admissible pair set has density 1/n. Thus separate endpoint marginals
    # imply pair density only when the actual constraints factor by endpoint.
    for n in (3, 7, 25):
        diagonal = {(i, i) for i in range(n)}
        assert {u for u, _ in diagonal} == set(range(n))
        assert {v for _, v in diagonal} == set(range(n))
        assert Fraction(len(diagonal), n * n) == Fraction(1, n)

    # Exact inherited rational consumer checks, kept as checks rather than
    # promoted conclusions.
    target = Fraction(21,  200)
    witness = Fraction(48861622601, 195312500000)
    excess = witness - target
    assert excess == Fraction(28353810101, 195312500000)
    assert Fraction(52897896569489, 572357731837500000) > 0

    print("PASS product endpoint set density 1/4")
    print("PASS boundary concentration and score-energy anticorrelation: exact C/gamma loss")
    print("PASS shrinking-density saturation for gamma=1/n")
    print("PASS weighted-average mismatch: weighted gamma=1/100, not unweighted 1/2")
    print("PASS coupled-pair hostile example: full marginals do not force pair density")
    print("PASS exact inherited conditioned-energy threshold excess", excess)
    print("SCOPE: hostile arrays are abstract; none is claimed to be prime-field data")
    print("STRICT >79: OPEN")


if __name__ == "__main__":
    main()
