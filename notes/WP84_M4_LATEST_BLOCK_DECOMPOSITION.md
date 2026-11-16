# WP84 — latest-block decomposition of the order-4 generator

Date: 2026-10-05

Status: **EXACT COMBINATORIAL DECOMPOSITION CLOSED; PAIR LAYER ASSIGNED TO A2; FOUR-DISTINCT MEMORY ASSIGNED TO A1**

This note refines `WP84_M4_LINDEBERG_WORD_ATTACK.md` by locating the
order-four word sectors inside the exact one-block Lindeberg expansion.

## 1. Coupling setup

Put a real coupling theta on the retained prime part:

    H(theta)=s0 I + theta * sum_j B_j.

For a permutation pi define

    X_k = sum_{a<k} B_{pi(a)},
    B   = B_{pi(k)},
    R_k(theta,z)=(s0 I + theta X_k-zI)^(-1).

The quadratic one-block contribution is

    - R_k (theta B) R_k
    + R_k (theta B) R_k (theta B) R_k.

Near theta=0,

    R_k
      = sum_{n>=0} (-theta)^n (s0-z)^(-n-1) X_k^n.

At coefficient theta^4, the first-order term contains

    sum_{a+b=3} tr(X_k^a B X_k^b),

while the second-order term contains

    sum_{a+b+c=2} tr(X_k^a B X_k^b B X_k^c).

## 2. Latest-label theorem

Fix one length-four block word and one permutation of its distinct labels.
Let B be the label that was inserted latest among the labels appearing in the
word.

Then:

- if B occurs once, the word appears exactly in the first-order term A1;
- if B occurs twice, the word appears exactly in the second-order term A2;
- if B occurs three or four times, it belongs to the cubic-remainder sector.

This is an exact word identity, not an asymptotic statement.

Companion checker:

    src/wp84_lindeberg_latest_block_m4.py

## 3. Immediate order-4 consequences

### Pair-pair sector 2+2

For every A^2 B^2 word, whichever of A or B is latest occurs twice.

Therefore

    boxed:
    the entire 2+2 pair layer lives in A2.

This includes both cyclic trace classes:

    adjacent/nested -> t_adj,
    alternating/crossing -> t_opp.

Thus G4-P is specifically a **second-order conditional variance/state** gate:

    A2 must reproduce
        2*t_adj + t_opp
      = 4/15.

### Four-distinct sector 1+1+1+1

The latest label occurs exactly once.

Therefore

    boxed:
    every four-distinct word lives in A1.

So killing the accumulated first-order term merely because its trace vanishes
inside the scalar multiplication ansatz destroys the whole four-distinct
sector before it has been audited.

This identifies a concrete reason the old multiplication closure could not
possibly recover the connected four-point geometry.

### Mixed sector 2+1+1

Averaging over permutations of its three distinct labels gives the exact split

    A1 : 2/3,
    A2 : 1/3.

So the non-pair sector is not purely a drift object; state-dependent variance
can also carry mixed connected information.

### 3+1 and 4

For multiplicity 3+1, permutation averaging splits

    A1 : 1/2,
    cubic remainder : 1/2.

The all-equal sector lies entirely in the cubic remainder.

The existing o(1) cubic resolvent bound controls the latter sector at fixed
nonreal z, but no raw-moment conclusion is inferred from it.

## 4. Correct interpretation of the connected -1/60

The pair layer is now cleanly located:

    A2(pair-pair) -> 4/15.

The target centered fourth coefficient is

    1/4 = 4/15 - 1/60.

Therefore the remaining connected correction

    Phi4 = -1/60

must be produced by the **non-pair conditional-state sector** after all
2+1+1 and four-distinct contributions are assembled and the cubic remainder
is controlled.

No stronger attribution is made without the arithmetic calculation.

This is narrower than the previous statement "the generator must recover an
extra 1/60": the generator must first recover the full crossing pair
`+1/30`, then recover a separate connected correction `-1/60`.

## 5. New fail-closed rules

A theorem candidate fails immediately if it does either of the following:

1. scalarizes A2 so that the alternating A B A B trace class disappears;
2. proves A1=o(1) by using an argument valid only when the intermediate
   resolvent is already a multiplication operator.

The second rule is important because the multiplication-algebra hypothesis
has already been falsified at order four.

## 6. Next analytic object

Define the bounded-resolvent connected defect at fixed nonreal z by

    C4_T(z)
      := [theta^4](
           full conditional A1+A2 contribution
           - pair-pair A2 contribution
         ).

The model consistency target is the coefficient corresponding to

    Phi4 = -1/60

after scalar-background normalization.

The next proof should derive C4_T(z) directly from the translation-word
geometry and identify the exact arithmetic input needed for its limit.

This is now the sharpest theorem frontier.
