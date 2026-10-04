#!/usr/bin/env python3
"""Exact directed arithmetic for the six-translate frontier constants."""

from decimal import Decimal, getcontext
from fractions import Fraction as F

B6 = F(1094977, 5000000000)
C0_LOWER = F("0.6725007036794116457343797908032951885934030286262640789295")
PI_UPPER = F(314159265358979323846, 10**20)

A1290 = F(129, 10000)
A1293 = F(1293, 100000)
A1295 = F(259, 20000)


def coefficient_lower(A: F) -> F:
    return (6 * C0_LOWER - 10 * PI_UPPER * B6) / (6 - A)


def decimal(x: F, digits: int = 60) -> str:
    getcontext().prec = digits + 20
    d = Decimal(x.numerator) / Decimal(x.denominator)
    return f"{d:.{digits}f}"


if __name__ == "__main__":
    for name, A in (("A1290", A1290), ("A1293", A1293), ("A1295", A1295)):
        c = coefficient_lower(A)
        print(f"{name}: A={A}")
        print(f"  exact lower = {c}")
        print(f"  decimal     = {decimal(c)}")
