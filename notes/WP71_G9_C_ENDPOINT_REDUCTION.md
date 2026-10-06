# WP71 G9-C — endpoint reduction audit

Date: 2026-10-04
Status: **EXACT ENDPOINT IDENTITY RETAINED; POINTWISE SHORT-WINDOW THEOREM ROUTE FALSIFIED**

The exact moving-interval identity remains:

    e_k(n) = E_{rk}(U_k(n)) - E_{rk}(L_k(n)-1)

if one chooses to subtract a prime-pair main inside the interval.

However the Stage-A scale audit shows that the hard interval I_k(n) has at most 13 integer m-values. Therefore using this identity as a theorem route would require prime-pair asymptotics on O(1)-length intervals. MRT long-shift estimates do not supply that.

Consequently the formerly proposed target

    sum_k Emax(rk;M,Y)^2 << K*Y^2*(log M)^(-A)

with Y the actual moving-window length, is **not** the right G9 target when Y=O(1).

## What remains useful

- the endpoint formulas L_k(n), U_k(n);
- same-j invariance under welding;
- the one-puncture characterization;
- monotonicity/source-switch bookkeeping;
- MRT Lemma 2.2 and Corollary 2.5 for later averaged/spectral truncations.

## Correct analytic target

The prime correlation estimate must be applied only after restoring a long averaging variable. We must control the full averaged object

    sum_{k,n} G_{k,n} Lambda(n)Lambda(n-qk) w_k(n)

or an exactly equivalent Fourier/spectral representation, with the signed main preserved globally.

This is now the G9-C target. Pointwise w_k(n) approximation is retired.
