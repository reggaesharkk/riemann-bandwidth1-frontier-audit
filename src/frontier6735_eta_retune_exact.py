#!/usr/bin/env python3
"""
Exact eta retune of the public VeriLoop-E2 q=8 scalar assembly.

Scope
-----
This script does NOT replay the imported 190,375,830-node local certificates.
It takes the three published certified local inequalities as premises and
recomputes the finite pressure envelope, a rigorous rational lower bound for R,
and the final scalar coefficient C.

All acceptance decisions use fractions.Fraction / integer arithmetic only.
"""

from decimal import Decimal, getcontext
from fractions import Fraction as F
from math import isqrt

q = 8
d = 16
m = 531
n = m - q
T = F(9, 8)

H = F(672167187145431, 10**15)
B = F(93, 23000)

SLOPES = (F(1, 2), F(19, 20), F(1, 1))
EPS = (
    F(526, 78125),
    F(9879, 1250000),
    F(20033, 2500000),
)

# Near the exact scalar switch point between E=0 and E=5753/5000.
ETA = F(99988220836693, 100000000000000)

PUBLISHED = F(
    722547711262091300265625000000000,
    1072825050442925667061714615173641,
)

# Clean fixed headline intentionally below our rigorous rational lower bound.
HEADLINE = F(6735000520898147, 10**16)


def sqrt_lower(x: F, digits: int = 120) -> F:
    """Return a rational L with L^2 <= x, using exact integer square root."""
    scale = 10**digits
    floor_scaled_square = (x.numerator * scale * scale) // x.denominator
    return F(isqrt(floor_scaled_square), scale)


def h_lower(E: F) -> F:
    """Rigorous rational lower bound for the q=8 spectral profile h(E)."""
    if E <= T:
        return E
    root_lo = sqrt_lower(E * T)
    # h(E) = E/(d+1) + 2d/(d+1)*sqrt(E*T) - d/(d+1)*T.
    return (
        E / (d + 1)
        + F(2 * d, d + 1) * root_lo
        - F(d, d + 1) * T
    )


def pressure(E: F) -> F:
    return max(
        (F(0),)
        + tuple(F(n) * eps - slope * E for slope, eps in zip(SLOPES, EPS))
    )


# On every linear piece of p(E), h(E)+eta*p(E) is concave.  Hence its
# infimum occurs at an endpoint.  A safe finite superset of all endpoints is
# {0,T}, the zero of each pressure line, and every pairwise pressure-line
# intersection.  Extra candidates can only make R_LOWER smaller, which is safe.
candidates = {F(0), T}

for slope, eps in zip(SLOPES, EPS):
    candidates.add(F(n) * eps / slope)

for i in range(len(SLOPES)):
    for j in range(i + 1, len(SLOPES)):
        E = F(n) * (EPS[i] - EPS[j]) / (SLOPES[i] - SLOPES[j])
        if E >= 0:
            candidates.add(E)

evaluated = [
    (h_lower(E) + ETA * pressure(E), E)
    for E in candidates
]

R_LOWER, E_MIN = min(evaluated)

numerator = F(m) * H - ETA * B * n
assert numerator > 0
assert F(m) > R_LOWER

# Because R_LOWER <= true R and the denominator is m-R, replacing R by the
# lower bound gives a conservative lower bound for C.
C_LOWER = numerator / (F(m) - R_LOWER)

# Load-bearing exact checks.
assert E_MIN == F(5753, 5000)
assert C_LOWER > PUBLISHED
assert C_LOWER > HEADLINE

getcontext().prec = 100


def dec(x: F) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


print("q =", q)
print("m =", m)
print("n =", n)
print("eta =", ETA)
print("eta_decimal =", dec(ETA))
print("minimizing_candidate_E =", E_MIN)
print("R_lower_exact =", R_LOWER)
print("R_lower_decimal =", dec(R_LOWER))
print("C_lower_exact =", C_LOWER)
print("C_lower_decimal =", dec(C_LOWER))
print("percent_lower_decimal =", dec(C_LOWER) * 100)
print("published_C_decimal =", dec(PUBLISHED))
print("gain_over_published =", dec(C_LOWER - PUBLISHED))
print("headline =", dec(HEADLINE))
print("headline_margin =", dec(C_LOWER - HEADLINE))
print("RESULT: EXACT_ETA_RETUNE_PASS")
