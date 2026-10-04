#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

# Fine rational lower bound used for high-precision diagnostic arithmetic.
# This is kept separate from the publication headline gate below, which uses
# the coarser Lean-certified HD_one_decimal lower endpoint.
HD_FINE_LOWER = F(
    1345001407358823291468759581606590377186806057252528157859,
    2000000000000000000000000000000000000000000000000000000000,
)

# Lean-certified lower endpoint from HD_one_decimal.1.
HD_LEAN_LOWER = F(672500703679, 10**12)

# Mathlib Real.pi_lt_d20:
#   pi < 3.14159265358979323847
# IMPORTANT: the previous v0.2 gate accidentally used the *lower* d20
# endpoint.  Because pi enters with a negative coefficient, the rigorous
# lower bound requires an UPPER bound on pi.
PI_UPPER_D20 = F(314159265358979323847, 10**20)

B = F(1094977, 5000000000)
A1293 = F(1293, 100000)
A1294 = F(1294, 100000)

def feedback_lower(HD_lower: F, A: F) -> F:
    return (6 * HD_lower - 10 * PI_UPPER_D20 * B) / (6 - A)

fine1293 = feedback_lower(HD_FINE_LOWER, A1293)
fine1294 = feedback_lower(HD_FINE_LOWER, A1294)
lean1293 = feedback_lower(HD_LEAN_LOWER, A1293)
lean1294 = feedback_lower(HD_LEAN_LOWER, A1294)

# Publication-safe fixed headline proved from the Lean-certified HD lower
# endpoint and Mathlib's certified pi upper endpoint.
HEADLINE = F(67280506, 10**8)

getcontext().prec = 100
D = lambda x: Decimal(x.numerator) / Decimal(x.denominator)

print("A1293 fine diagnostic lower", D(fine1293))
print("A1294 fine diagnostic lower", D(fine1294))
print("fine diagnostic gain", D(fine1294 - fine1293))
print("A1293 Lean-directed lower", D(lean1293))
print("A1294 Lean-directed lower", D(lean1294))
print("Lean-directed A1294 exact", lean1294)
print("headline", D(HEADLINE))
print("headline margin", D(lean1294 - HEADLINE))

assert PI_UPPER_D20 > F(314159265358979323846, 10**20)
assert fine1294 > fine1293
assert lean1294 > lean1293
assert lean1294 > HEADLINE
