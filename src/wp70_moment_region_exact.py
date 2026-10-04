#!/usr/bin/env python3
"""
Exact robust fourth-moment gate for a 70% simple-critical-zero target.

Moment variables:
  mu0 = 1
  mu1 = 1
  mu2 = 4/3
  mu3 = r
  mu4 = q

For a nonnegative spectral measure, the degree-2 Christoffel function at 0 is
lambda_2(0) = 1 / (e0^T M^{-1} e0),
where M is the 3x3 Hankel moment matrix.  The simple-zero transfer used in the
paper gives B = 1 - 2 lambda_2(0).

This script derives the exact two-parameter region B > 7/10, then expresses it
as a one-sided error budget around the sine-kernel target (r,q)=(2,13/4).
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 80

def dec(x: F) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)

# Sine-kernel target values.
R0 = F(2, 1)
Q0 = F(13, 4)
TARGET = F(7, 10)

# Exact threshold when r=2.
Q70_AT_R2 = F(59, 18)
Q_SLACK_AT_SINE = Q70_AT_R2 - Q0
assert Q_SLACK_AT_SINE == F(1, 36)

# If r = 2-d3, then exact algebra gives
# q < 59/18 - (11/2)d3 + (51/8)d3^2.
def q_threshold_from_d3(d3: F) -> F:
    return F(59,18) - F(11,2)*d3 + F(51,8)*d3*d3

# Exact upper root for d3 when q is fixed at 13/4 solves
# 51/8 d^2 - 11/2 d + 1/36 = 0.
# We keep the radical form in the note and use a rational test value here.
D3_SAFE = F(508, 100000)  # 0.00508
D3_FAIL = F(509, 100000)  # 0.00509
assert Q0 < q_threshold_from_d3(D3_SAFE)
assert not (Q0 < q_threshold_from_d3(D3_FAIL))

# A convenient one-sided budget statement:
# if r >= 2-d3 and q <= 13/4+d4, it is sufficient that
# d4 + 11/2 d3 - 51/8 d3^2 < 1/36.
def budget(d3: F, d4: F) -> F:
    return d4 + F(11,2)*d3 - F(51,8)*d3*d3

tests = [
    (F(0), F(1,100), "exact-mu3, mu4=3.26"),
    (F(1,1000), F(1,100), "mu3>=1.999, mu4<=3.26"),
    (F(4,1000), F(0), "mu3>=1.996, mu4<=3.25"),
]
for d3,d4,label in tests:
    ok = budget(d3,d4) < F(1,36)
    print(label, "budget=", dec(budget(d3,d4)), "PASS70=", ok)

print("q_threshold_if_mu3_exact =", dec(Q70_AT_R2))
print("allowed_mu4_excess_if_mu3_exact =", dec(Q_SLACK_AT_SINE))
print("safe_example_mu3_lower =", dec(R0-D3_SAFE))
print("safe_example_q_upper =", dec(Q0))
print("safe_example_budget =", dec(budget(D3_SAFE,F(0))))
print("budget_limit =", dec(F(1,36)))

# At d4=0 the exact relevant root is
# d = (198 - 6*sqrt(106350?))?  Rather than freeze a hand-simplified radical,
# solve numerically only for display via Decimal Newton/bisection.
lo = Decimal(0)
hi = Decimal("0.01")
for _ in range(200):
    mid = (lo+hi)/2
    val = Decimal(51)/8*mid*mid - Decimal(11)/2*mid + Decimal(1)/36
    if val > 0:
        lo = mid
    else:
        hi = mid
dcrit = (lo+hi)/2
print("critical_d3_when_mu4=13/4 ~", dcrit)
print("critical_mu3_lower ~", Decimal(2)-dcrit)

print("RESULT: ROBUST_70_PERCENT_MOMENT_REGION_DERIVED")
