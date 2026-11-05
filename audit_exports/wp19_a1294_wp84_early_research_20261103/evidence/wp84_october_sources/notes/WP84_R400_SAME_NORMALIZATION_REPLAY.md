# WP84 — R=400 same-normalization replay

Date: 2026-10-06

Status: **FINAL R=400 ASSEMBLY AUDIT; ALL ORDER-FOUR CLASSES ARE NOW PLACED IN ONE NORMALIZATION, WITH TWO EXPLICIT o(1) PRINCIPAL-SECTION LEMMAS**

This note does not alter the bounded-consumer firewall.  It records the exact
order in which the already-proved reductions must be consumed and prevents
the endpoint row selection from being silently moved across an unbounded
polynomial step.

## 1. Canonical order of operations

Let f_match be the bounded matched consumer and let H be the full theorem
matrix.  Let H_400 be the hard displacement-band truncation, and let I be the
contiguous good-endpoint principal section chosen only after H_400 has been
formed.

The legal order is

    f_match(H)
      -> f_match(H_400)
      -> f_match((H_400)_I)
      -> P4((H_400)_I).

The first arrow pays the already-certified fixed-pole band cost

    C_match/400,

with

    C_match = 2.1728342265....

The second arrow is a bounded rank perturbation.  If r rows are deleted,
embed (H_400)_I back into d dimensions by adding r zero coordinates.  The
matrix difference has rank at most 2r.  Hence the bounded spectral statistic
changes by O(r/d); converting from the d-normalized padded trace to the
|I|-normalized trace adds only another O(r/d) term because f_match is bounded.

Choose

    epsilon_L = L^(-1/2),
    r = O(epsilon_L d).

Therefore this step costs o(1).

Only after this bounded step is complete is the global polynomial inequality

    g_match(x) <= P4(x)

used on the selected finite-band section.  No raw quartic polynomial is ever
applied to the original full matrix.

## 2. Good-endpoint sampling is genuinely discrete

For each endpoint feature family

    S_theta(t)=sum_{m<=N} a_m(theta)m^(it),
    N<=T^2,

the candidate endpoint window has physical length

    U asymp epsilon_L T

and contains

    r asymp U L

Fourier grid points.

For grid spacing h=2 pi/L, the local Sobolev sampling inequality gives

    sum_k |S_theta(t_k)|^2
      <= C[
           h^(-1) int |S_theta|^2
           +h int |S_theta'|^2
         ]

on a harmless O(h)-enlargement of the window.

Montgomery--Vaughan applied to S_theta and S_theta' yields

    int |S_theta|^2
      <= C(U+N) sum_m |a_m(theta)|^2,

    int |S_theta'|^2
      <= C(U+N)
         sum_m (log m)^2 |a_m(theta)|^2.

Because log N=O(L), both sampled terms are

    <= C L(U+N) sum_m |a_m(theta)|^2.

The balanced product second-mass theorem gives O(1) after integrating the
finite feature parameters.  Dividing by r asymp UL therefore gives the
average endpoint score

    O(1+N/U)
      = O(T/epsilon_L).

Thus good lower and upper endpoints exist simultaneously after summing all
finitely many required feature scores into one nonnegative score.

The rank-two endpoint commutator contributes 1/|I|, so Cauchy--Schwarz gives

    endpoint debt
      <= C T/(epsilon_L |I|)
      = O(1/(epsilon_L L))
      = O(L^(-1/2))
      = o(1).

This is the balanced nonclosed positive-leakage budget.

## 3. Fixed-R pair layer survives the principal-section choice

At fixed R, every degree-four band word has total Fourier displacement at
most 4R.  Replacing the full band by a contiguous principal section therefore
changes the normalized trace of a translation-invariant bulk word only
through O(R) rows at the two newly selected boundaries.

Consequently the finite-section boundary correction is

    O(R/|I|)=o(1)

for R=400.

The source-closed second-covariance substitution used in the exact pair
formula is uniform for carrier heights comparable with T.  The selected
lower and upper carriers differ from the original ones by only
O(epsilon_L T), so the corresponding continuum covariance changes by o(1).

Hence

    boxed:
    Pair_400(I)
      =
      Pair_400
      +o(1)

and the exact certificate remains

    boxed:
    Pair_400(I)
      < 0.266329+o(1).

No endpoint selection is allowed to change the pair normalization.

## 4. Complete order-four class replay

Use the exact six-word / connected normalization

    C24=4 C6=C8.

The fixed-band centered fourth trace on I is partitioned as follows.

1. Pair-pair 2+2 sector.
   The exact R=400 pair certificate gives

       Pair_400(I)<0.266329+o(1).

2. Nonclosed 3-vs-1 sign sector.
   Adaptive endpoint quarantine has N/T->0.  The sign-balance spacing gate
   therefore gives o(1) uniformly.  The O(epsilon_L) carrier displacement of
   the selected section does not change N/T->0.

3. Same-sign V-sum sector.
   Exact prime-base valuation forces every order-four resonance into proper
   prime powers with |b-c|=2.  Its total normalized contribution is o(1).

4. Proper-prime-power corrections.
   Their coefficient squared mass is O(L^-2), hence every mixed occurrence is
   o(1) against the O(1) ordinary-prime product mass.

5. Balanced exact/equal-scale connected bulk.
   The connected overlap kernel is nonpositive.  It may be discarded only in
   an upper bound, with no positive charge.

6. Balanced unequal-scale / nonclosed connected sector.
   The sharp detuning decomposition writes this as a nonpositive Brownian
   reference plus a residual with

       -dist(s-t,Z) <= E <= 0.

   The residual is converted by the exact rank-two endpoint commutator into
   the finite threshold-feature endpoint families treated in Section 2.
   Its total positive contribution on I is o(1).

These classes include the mixed and four-distinct histories after the exact
pair layer is removed; the latest-block A1/A2 bookkeeping is not used to
delete them.  Their contribution is retained inside the connected kernel
until the sign/detuning reduction is applied.

Therefore

    boxed:
    w_400(I)
      = tau_I(P_400^4)
      <= 0.266329+o(1).

## 5. Centered quartic assembly

The centered polynomial identity is

    tau_I P4(H_400)
      =
      1/2000
      +(213/1000) v_400(I)
      +(593/2000) w_400(I)
      +o(1).

The fixed-band variance satisfies

    v_400(I)<=1/3+o(1),

because the same fixed-range bulk argument changes it by O(R/|I|)+o(1).

Hence

    tau_I P4(H_400)
      <=
      1/2000
      +213/3000
      +(593/2000)(0.266329)
      +o(1)

      =
      0.1504665485
      +o(1).

Restoring the bounded full-to-band comparison gives

    defect
      <=
      0.1504665485
      +2.1728342265/400
      +o(1)

      =
      boxed:
      0.15589863406625
      +o(1).

Against the conservative record ceiling

    E_rec=0.163249981456072,

the strict asymptotic margin is

    boxed:
    0.007351347389822.

The induced simple-zero coefficient is

    boxed:
    1-2(0.15589863406625)
      =
      0.6882027318675.

Thus the replay supports the asymptotic first-strike coefficient

    boxed:
    68.82027318675 percent,

subject only to the source lemmas already cited by the component notes.

## 6. Claim firewall

This replay does not transfer any sixth-moment or 79-percent model statement.
It closes only the R=400 degree-four path.

The 79.627-percent programme remains a bounded-functional problem and must
not be inferred from this quartic argument.

References:

    notes/WP84_GOOD_ENDPOINT_TRIMMING.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
    notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md
    notes/WP84_BALANCED_PRODUCT_SECOND_MASS.md
    notes/WP84_SIGN_BALANCE_NEAR_RESONANCE_GATE.md
    notes/WP84_ORDER4_VSUM_PRIME_RESONANCE.md
    notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md
    notes/WP84_CROSS_SCALE_SHARP_DETUNING.md
    notes/WP84_DETUNING_COMMUTATOR_ENDPOINT.md
    notes/WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION.md
    notes/WP84_CENTERED_M4_SCALAR_GATE.md
    notes/WP84_MATCHED_QUARTIC_MAJORANT.md
