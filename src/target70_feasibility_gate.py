#!/usr/bin/env python3
"""
70% feasibility gate for simple critical-line zeta zeros.

This is a research-planning checker, not a theorem prover.  It freezes the
quantitative consequences of the currently audited information barriers:

  * current exact-retuned q=8 scalar headline;
  * the paper's bandwidth-one ceiling (~0.68185);
  * the flat-window support needed to reach 0.70;
  * the paper's conditional fourth-moment target 13/18.

No floating-point value is used for the exact rational comparisons.
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext

CURRENT = F(6735000520898147, 10**16)
TARGET70 = F(7, 10)
TARGET72 = F(13, 18)

# Paper-level barrier quoted in Remark 1.1.  This is a stated decimal ceiling
# for the bandwidth-one configuration-by-configuration certificate class.
BW1_CEILING_DEC = Decimal("0.68185")

# Flat-window H(lambda) = 2 - 1/lambda - lambda/3 reaches 0.70 when
# 10 lambda^2 - 39 lambda + 30 = 0.  The relevant root is
# (39 - sqrt(321))/20.
getcontext().prec = 80
D = Decimal
LAMBDA_FLAT_70 = (D(39) - D(321).sqrt()) / D(20)

def dec(x: F) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)

print("current_fixed_headline =", dec(CURRENT))
print("target_70 =", dec(TARGET70))
print("gap_current_to_70 =", dec(TARGET70 - CURRENT))
print("bandwidth1_ceiling_stated =", BW1_CEILING_DEC)
print("gap_bw1_ceiling_to_70 =", D("0.70") - BW1_CEILING_DEC)
print("flat_window_lambda_for_70 =", LAMBDA_FLAT_70)
print("paper_optimized_support_target_for_70 ~= 1.04")
print("conditional_HL4_target_13_over_18 =", dec(TARGET72))
print("HL4_margin_over_70 =", dec(TARGET72 - TARGET70))

assert CURRENT < TARGET70
assert BW1_CEILING_DEC < D("0.70")
assert LAMBDA_FLAT_70 > D(1)
assert TARGET72 > TARGET70

print("RESULT: 70_PERCENT_REQUIRES_NEW_ARITHMETIC_INFORMATION")
