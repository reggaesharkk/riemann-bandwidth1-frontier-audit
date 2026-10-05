# WP84 resolvent kill gate -- 2026-10-05

Current status:

1. The bounded beta family is the preferred positive-index consumer family.
2. **Conditioning correction:** b10 is model-strong but is not the preferred theorem target under a raw fixed-circle Cauchy transfer. At rho=0.9 it requires resolvent accuracy about 5.1e-8, while b3 already clears 79% and requires only about 3.6e-5. Therefore b3 is the present theorem consumer unless a sharper Stieltjes-to-beta transfer is proved.
3. Cubic-and-higher single-block Lindeberg remainders are negligible on a fixed non-real circle.
4. A pure multiplication/covariance Dyson closure is false: it predicts centered m4=7/30 instead of 1/4.
5. Exact model anchors resolve the missing correction as t_opp + Phi4 = 1/30 - 1/60 = 1/60.
6. Non-cyclic partial-translation word traces reproduce exactly the overlap geometry O_b=(1-spread(partial walk))_+.
7. The correct state space is therefore the compressed translation (finite Wiener-Hopf) algebra, not a single multiplication symbol.
8. A second exact interface is now available: the fixed-circle resolvent is the exponentially weighted Laplace transform of the bounded unitary trace phi_H(t)=tau(exp(-itH)). On a fixed circle, only a finite time interval is needed up to an explicit exponential tail, and one-block Duhamel cubic remainders are O(T_*^3 sum ||B_j||^3)=o(1).

Next theorem gate:

Prove either

(A) a fixed-circle normalized resolvent trace law directly in the compressed translation algebra, with the full consumer error ledger C_m(rho)*epsilon(rho), or

(B) the equivalent bounded-time unitary-flow law for the translation coefficients and two-time correlations, then Laplace-transform it to the fixed circle.

Before any positive-index claim, the candidate law must reproduce the exact first four model moments, including the fourth-order crossing/connected correction.

Fail-closed rules:

- any closure returning only the two adjacent/noncrossing pairings is rejected;
- any >79 claim must include the fixed-circle consumer conditioning constant, not only the raw resolvent error;
- b10 may not be called easier than b3 unless a transfer theorem beats the raw Cauchy conditioning bound.
