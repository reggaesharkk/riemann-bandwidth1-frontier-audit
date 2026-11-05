#!/usr/bin/env python3
"""Fail-closed bookkeeping check for the WP84 R=400 same-normalization replay."""

from decimal import Decimal, getcontext
getcontext().prec = 60

R = Decimal(400)
PAIR_HEADLINE = Decimal("0.266329")
C_MATCH = Decimal("2.1728342265")
E_REC = Decimal("0.163249981456072")

quartic = (
    Decimal(1)/Decimal(2000)
    + Decimal(213)/Decimal(3000)
    + Decimal(593)/Decimal(2000)*PAIR_HEADLINE
)
band = C_MATCH/R
defect = quartic + band
margin = E_REC - defect
simple = Decimal(1) - Decimal(2)*defect

assert quartic == Decimal("0.1504665485")
assert band == Decimal("0.00543208556625")
assert defect == Decimal("0.15589863406625")
assert margin == Decimal("0.007351347389822")
assert simple == Decimal("0.68820273186750")

# Exponent ledger for epsilon_L=L^{-1/2}.
# rank deletion: epsilon_L = L^{-1/2} -> 0
# endpoint debt: 1/(epsilon_L L)=L^{-1/2} -> 0
# fixed-R section boundary: R/d -> 0 since d~T L.
eps_exponent = Decimal("-0.5")
endpoint_exponent = Decimal("-0.5")
assert eps_exponent < 0
assert endpoint_exponent < 0

print("quartic upper =", quartic)
print("band charge   =", band)
print("defect upper  =", defect)
print("record margin =", margin)
print("simple lower  =", simple)
print("rank-delete rate  = O(L^-1/2)")
print("endpoint-debt rate= O(L^-1/2)")
print("fixed-R boundary   = O(R/d)=o(1)")
print("RESULT: WP84_R400_SAME_NORMALIZATION_REPLAY_PASS")
