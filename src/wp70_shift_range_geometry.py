#!/usr/bin/env python3
"""Geometry of the shift range in the fourth-trace 70% attack."""

from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 40

lambdas = [F(4,5), F(9,10), F(19,20), F(49,50), F(1,1)]

print("lambda,beta where H=X^beta and beta=2-1/lambda")
for lam in lambdas:
    beta = F(2,1) - F(1,1)/lam
    print(
        f"{float(lam):.5f},"
        f"{float(beta):.12f},"
        f"exact_beta={beta}"
    )

# Existing long-shift benchmark often quoted for Lambda correlations:
MRT = F(8,33)
print("MRT_long_shift_benchmark_beta =", float(MRT), "exact", MRT)

for lam in lambdas:
    beta = F(2,1) - F(1,1)/lam
    if lam > F(1,2):
        print(
            f"lambda={float(lam):.2f}: beta-MRT = "
            f"{float(beta-MRT):.6f}"
        )

assert all(F(2)-F(1)/lam > MRT for lam in lambdas)
print("RESULT: FOURTH_TRACE_SHIFT_RANGE_IS_LONG_RELATIVE_TO_MRT_BENCHMARK")
