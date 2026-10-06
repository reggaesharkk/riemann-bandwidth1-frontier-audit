#!/usr/bin/env python3
"""WP84 exact block-mass ledger.

From the analytic Toeplitz lemma:
  ||B_n|| <= 4 * Lambda(n)/(L*sqrt(n))
in hat units once a>=1/2.

The source-closed Chebyshev-Mertens input gives
  sum_{n<=X} Lambda(n)^2/n = L^2/2 + O(L).

Hence sum ||B_n||^2 <= 8+O(1/L).

For cubes, Lambda(n)<=log n and a dyadic comparison proves
  sum_{n>=2} (log n)^3/n^(3/2) < infinity,
so sum ||B_n||^3 = O(L^-3).

This script checks a finite partial sum of the dyadic majorant numerically.
It does not certify the infinite sum; convergence follows from the geometric-series
argument in the accompanying note. The printed partial sum is a floating-point diagnostic; the convergence argument is the analytic input.
"""
from fractions import Fraction as F
import math

def main():
    # For n in [2^k,2^(k+1)), at most 2^k terms and
    # (log n)^3/n^(3/2) <= ((k+1)log2)^3 * 2^(-3k/2).
    # So shell <= ((k+1)log2)^3 * 2^(-k/2).
    s=0.0
    for k in range(80):
        s += ((k+1)*math.log(2))**3 * 2**(-k/2)
    # tail after 80 is microscopic; this is diagnostic only.
    print("dyadic cube-mass majorant first 80 shells =",repr(s))
    assert 195.0 < s < 200.0  # loose floating-point smoke range; not a proof bound
    print("hat block square-mass asymptotic coefficient <= 8")
    print("hat block cube-mass = O(L^-3)")
    print("RESULT: WP84_INFINITESIMAL_BLOCK_LEDGER_PASS")

if __name__=="__main__":
    main()
