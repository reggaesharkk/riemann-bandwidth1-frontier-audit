# WP84 — fixed-R pair layer is stable under the good-endpoint principal section

Date: 2026-10-06

Status: **SAME-NORMALIZATION LOCALITY LEMMA — THE R=400 PAIR CERTIFICATE SURVIVES ANY CONTIGUOUS o(d)-END TRIMMING WITH ONLY o(1) NORMALIZED CHANGE**

No unconditional percentage theorem is claimed here.

The good-endpoint argument selects a contiguous principal frequency section
after deleting o(d) rows from the two ends of the full sharp matrix.  The
R=400 first-strike assembly requires the exact fixed-band pair layer to survive
that selection.

This note closes that locality check.

## 1. Fixed-band restriction commutes with taking a principal section

Let P be the centered sharp prime matrix and let

    P_R

denote its hard displacement truncation

    (P_R)_{ij}=P_{ij}  if |i-j|<=R,
                 0     otherwise.

Let I be any contiguous set of Fourier indices and let P_I be the principal
submatrix of P on I.

Then exactly

    boxed:

    (P_R)_I
      =
      (P_I)_R.

There is no extra truncation interface inside I.  Only the two new ends of I
can affect fixed-R trace paths.

## 2. Every pair contraction is finite-range

The pair-pair fourth sector is the Wick contraction of the already-closed
second covariance and contains only matrix paths whose four displacement
increments have absolute value at most R.

Therefore a starting index whose distance from both ends of I exceeds 4R
sees exactly the same local lag ledger as an index in an infinite section.

The number of potentially boundary-affected starting indices is O(R), with a
constant independent of d and of the selected endpoint positions.

After normalized trace division by

    d'=|I|,

the pure section-boundary contribution is

    boxed:

    O(R/d').

For fixed R=400 and d'->infinity this is o(1).

## 3. Bulk covariance is translation-invariant in the fixed-R limit

The source-closed resonant second covariance used in

    WP84_R400_EXACT_PAIR_LAYER

is a function only of the lattice lag i-j:

    E alpha_i alpha_j
      =
      (1/4) delta_ij,

    E alpha_i beta_j
      =
      0,

    E beta_i beta_j
      =
      1/6                         if i=j,

      -1/[2 pi^2(i-j)^2]          if i!=j.

The sum-frequency / carrier-2T covariance is o(1) uniformly in the retained
high-frequency window by the existing fast-channel closure.

Hence shifting the lower index of a contiguous principal section does not
change the limiting fixed-R bulk pair tensor.

The good-endpoint selection moves the two band edges by at most

    O(epsilon_L d),

with

    epsilon_L=L^(-1/2)->0,

and the retained carrier interval remains inside the same T-scale compact
window.  The prime-square continuum substitutions used for the fixed finite
set of lags |r|<=R are uniform there.

Therefore the bulk covariance error is o(1), uniformly over all candidate
sections allowed by the good-endpoint construction.

## 4. Pair-layer consequence

Let

    Pair_R(I)

denote the complete normalized pair-pair contribution to

    tau_I[(P_I)_R^4].

Then for every good-endpoint candidate section I,

    boxed:

    Pair_R(I)
      =
      Pair_R
      +
      O(R/|I|)
      +
      o(1).

The o(1) term is uniform over the candidate endpoint windows.

At R=400,

    Pair_400<0.266329

was certified independently.  Therefore

    boxed:

    Pair_400(I)
      <
      0.266329
      +
      o(1).

The data-dependent choice of the good lower and upper endpoints does not
change this statement because the estimate is uniform over every candidate
section.

## 5. Interaction with the bounded-consumer order of operations

The proof order remains:

    bounded full consumer
      -> fixed R band comparison
      -> choose/delete o(d) endpoint rows
      -> quartic majorant on the selected principal section.

The present lemma concerns only the fixed-R quartic pair ledger after the
bounded rank deletion.  It does not apply the quartic polynomial to the
unbanded matrix and therefore does not violate the Proposition-R firewall.

## 6. R=400 replay item closed

The six-item promotion checklist in

    WP84_R400_FIRST_RECORD_ASSEMBLY

included:

    verify the pair sector changes by only o(1).

This note supplies exactly that statement.

The remaining replay items are now the word-class bookkeeping and final
single-inequality assembly.

## Evidence boundary

Closed:

- principal-section/band-truncation commutation;
- fixed-R path locality;
- O(R/d') boundary fraction;
- uniform translation-invariant pair covariance on the candidate sections;
- Pair_400(I)<0.266329+o(1).

No new prime-correlation theorem is used.

See:

    notes/WP84_GOOD_ENDPOINT_TRIMMING.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
    notes/WP84_RESONANT_SCALAR_COVARIANCE.md
    notes/WP84_D2_FAST_CHANNEL_VK_CLOSURE.md
