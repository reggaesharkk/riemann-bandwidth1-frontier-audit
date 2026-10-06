# WP84 — finite-band Cayley resolvent locality after alpha rank quarantine

Date: 2026-10-05

Status: **AFTER DISPLACEMENT-TAIL REDUCTION, THE ONE-POINT r2 CONSUMER IS EXPONENTIALLY LOCAL IN INDEX SPACE**

No unconditional zero-density percentage is claimed here.

After the fixed-displacement reduction, write

    H_{R,M}=D_beta+K_{R,M},

where the off-diagonal bandwidth is R and |alpha_i|<=M. Then

    |K_ij| <= 2M/[pi |i-j|],

so the off-diagonal row sum obeys

    J0(R,M) <= (4M/pi) H_R,

with H_R=sum_{r=1}^R 1/r.

For theta>0 let W_theta=diag(exp(theta i)). Since the diagonal commutes with W_theta,

    ||W_theta H W_theta^{-1}-H||
      <= J0(R,M)[exp(theta R)-1].

Choose theta by

    J0(R,M)[exp(theta R)-1]=1/2.

At z=i, ||(H-iI)^(-1)||<=1. The conjugated resolvent therefore has norm at most 2, giving the exact Combes--Thomas envelope

    boxed:
    |R(i)_{jk}| <= 2 exp(-theta |j-k|).

No bound on beta is required.

For the repeated-pole term,

    (R^2)_{jj}=sum_k R_{jk}^2,

so the contribution from |k-j|>S is bounded by

    8 exp[-2 theta(S+1)]/[1-exp(-2 theta)].

The diagonal entry R_{jj} is also locally approximable. If H_I is the principal window on I=[j-S,j+S], then the full matrix and H_I direct_sum H_{I^c} differ only on the O(R^2) hopping entries crossing the two boundaries. Resolvent identity plus the same exponential envelope gives

    |R_{jj}-(R_I)_{jj}|
      <= C(R,M) exp[-2 theta(S-R)]

for S>R, and the analogous estimate holds for (R^2)_{jj}.

Hence, for fixed R,M,

    tau r2(H_{R,M})
      = d^(-1) sum_j F_{R,M,S}(j)
        + O_{R,M}(exp(-c_{R,M}S))
        + O(S/d),

where F_{R,M,S}(j) depends only on the finite local vector

    {alpha_{j-S},...,alpha_{j+S}, beta_{j-S},...,beta_{j+S}}.

Therefore the preferred record theorem reduces, after arbitrarily small band-tail and rank-quarantine errors, to the empirical average of one bounded finite-dimensional local observable.

This is strictly weaker than proving a global long-range matrix-Dyson law.

The recommended limit order is

    T -> infinity at fixed R,M,S,
    then S -> infinity,
    M -> infinity,
    R -> infinity.

At fixed R,M,S the remaining arithmetic task is a finite local joint-distribution problem. It can be attacked either directly or by a finite polynomial approximation of the bounded local observable, requiring only finitely many translation-word correlation gates.

The a=1 r2 model margin 0.0466326939503807... can be allocated across displacement-tail, rank-quarantine, locality, and final arithmetic errors.

See:

    notes/WP84_R2_DISPLACEMENT_TAIL_TRUNCATION.md
    notes/WP84_R2_CAYLEY_DEFECT_GATE.md
    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md
