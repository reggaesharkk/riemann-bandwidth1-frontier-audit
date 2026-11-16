# WP71 G9 — Stage-A moving-window scale correction

Date: 2026-10-04
Status: **CRITICAL CORRECTION; previous ambient/logarithmic-window bulk route is FALSIFIED**

The public Stage-A hard band does **not** have a moving m-window of ambient or polylogarithmically reduced length.

The actual band condition in `scripts/g1_ledger.py` is

    |b1*n-b2*m| * T <= 40 * min(b1*n,b2*m),

with

    m <= X = floor(T/(2*pi)).

For fixed n, every admissible m therefore satisfies

    |m - (b1/b2)n|
      = |b1*n-b2*m|/b2
      <= 40*min(N1,N2)/(T*b2)
      <= 40*m/T
      <= 40*X/T
      <= 40/(2*pi).

Hence all admissible m lie in an interval of total length at most

    40/pi = 12.732... .

Using the elementary rational bound pi>3.14 already gives 40/pi<13. Therefore:

    **for every fixed n, the Stage-A hard welding interval contains at most 13 integer m values before the j=0 deletion and any additional support cuts.**

The companion gate `src/wp71_g9_stageA_width_gate.py` brute-force checks representative finite cells, but the displayed inequality is the proof.

## Consequence

The earlier proposal to create a logarithmic collar and treat the remaining moving intervals as near-ambient-length intervals is invalid for the actual Stage-A hard kernel. The interval is structurally O(1).

Therefore a pointwise approximation

    w_k(n) = S(rk)*|I_k(n)| + small error

cannot be justified from a long-interval prime-pair theorem. It would demand control of prime pairs in intervals containing only O(1) candidate m-values.

MRT Corollary 2.5 still gives endpoint-uniform truncation machinery, but it does **not** turn an O(1)-length prime-pair window into an asymptotic singular-series law.

## Gate downgrade

The following prior route is retired as a theorem path:

- pointwise maximal short-window Emax control for w_k(n);
- the logarithmic bulk/collar argument based on |I_k(n)| being within log powers of ambient scale.

The exact moving-interval formulas remain correct and useful combinatorially.

## Required pivot

G9 must keep the averaging over n/j/k **before** invoking prime-correlation estimates. The viable objects are global/averaged four-prime or spectral quantities, not pointwise short welding windows.

Two candidate pivots remain:

1. derive a direct averaged covariance estimate for
   sum_{k,n} outer_pair(n,qk) * w_k(n),
   without approximating w_k(n) pointwise;
2. rebuild the exact spectral/Parseval consumer interface so the averaged four-point object is controlled by windowed single-prime sums and classical major/minor arc estimates, without importing the unproved glue statement.

This correction narrows the problem and prevents a false G9 closure.
