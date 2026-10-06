#!/usr/bin/env python3
"""Exact rational audit of the delta=144 strict 79.5% consumer rung.

This checks only the Jensen/model arithmetic. It does not assert an arithmetic
resolvent bound or an unconditional zero-proportion theorem.
"""
from fractions import Fraction as F

W0 = F(1415, 13891)
TARGET = F(159, 200)       # 79.5%
TARGET_CAP = (1 - TARGET) / 2  # 41/400


def cap(delta: int) -> F:
    d = F(delta)
    return (d + 1) * W0 / (d + W0)


def score(delta: int) -> F:
    return 1 - 2 * cap(delta)


def threshold(target: F) -> F:
    c = (1 - target) / 2
    if c <= W0:
        raise ValueError("target must lie below the limiting frontier")
    return W0 * (1 - c) / (c - W0)


def main() -> None:
    d = 144
    c144 = cap(d)
    s144 = score(d)
    gap = TARGET_CAP - c144

    assert c144 == F(205175, 2001719)
    assert s144 == F(1591369, 2001719)
    assert threshold(TARGET) == F(507985, 3531)
    assert F(143) <= threshold(TARGET) < F(144)
    assert score(143) <= TARGET < score(144)
    assert gap == F(479, 800687600)
    assert gap > 0

    print("w0 =", W0)
    print("79.5% real delta threshold =", threshold(TARGET))
    print("first integer delta =", d)
    print("model Jensen cap at delta=144 =", c144)
    print("model score at delta=144 =", s144)
    print("strict 79.5% cap threshold =", TARGET_CAP)
    print("cap headroom =", gap)
    print("cap headroom decimal =", f"{float(gap):.15g}")
    print("score =", f"{100*float(s144):.12f}%")
    print("score headroom =", f"{100*float(s144-TARGET):.12f} percentage points")
    print("RESULT: DELTA144_EXACT_MODEL_MARGIN_PASS")
    print("ARITHMETIC_GATE: OPEN")


if __name__ == "__main__":
    main()
