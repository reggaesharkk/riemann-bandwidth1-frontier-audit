#!/usr/bin/env python3
"""Exact rational record for the Jensen-sharpened bounded consumer ladder."""

from fractions import Fraction as F

W0 = F(1415, 13891)
FRONTIER = 1 - 2 * W0

def cap(delta: int) -> F:
    d = F(delta)
    return (d + 1) * W0 / (d + W0)

def score(delta: int) -> F:
    return 1 - 2 * cap(delta)

def threshold(target: F) -> F:
    """Real delta threshold for score(delta) > target."""
    c = (1 - target) / 2
    if c <= W0:
        raise ValueError("target must lie below the limiting frontier")
    return W0 * (1 - c) / (c - W0)

def first_integer(target: F, minimum: int = 61) -> int:
    t = threshold(target)
    d = max(minimum, t.numerator // t.denominator + 1)
    while score(d) <= target:
        d += 1
    assert d == minimum or score(d - 1) <= target
    return d

def main() -> None:
    assert FRONTIER == F(11061, 13891)
    assert score(61) == F(336653, 424383)

    targets = (
        (F(159, 200), 144),   # 79.5%
        (F(199, 250), 676),   # 79.6%
        (F(3981, 5000), 2579) # 79.62%
    )
    for target, expected in targets:
        t = threshold(target)
        d = first_integer(target)
        assert d == expected
        assert F(d) > t and F(d - 1) <= t
        assert score(d) > target >= score(d - 1)
        print(
            f"target={100*float(target):.2f}% "
            f"threshold={t} first_delta={d} "
            f"score={score(d)} ({100*float(score(d)):.12f}%)"
        )

    for d in (61, 144, 676, 2579, 2871, 9717, 18577, 1_000_000):
        print(f"delta={d} score={score(d)} ({100*float(score(d)):.12f}%)")
    print(f"frontier={FRONTIER} ({100*float(FRONTIER):.12f}%)")
    print("RESULT: WP84_JENSEN_THRESHOLD_RECORD_PASS")

if __name__ == "__main__":
    main()
