# WP84 — exact orientation normalization of the fixed-scale balanced ledger

Date: 2026-10-06

Status: **EXACT NORMALIZATION CHECK — THE SIX SIGN-PATTERN KERNEL AND THE EIGHT-ALTERNATING-WORD BROWNIAN KERNEL ARE THE SAME LEDGER IN DIFFERENT NORMALIZATIONS**

No unconditional zero-density percentage is claimed here.

Two exact fixed-scale notes used different normalizations:

1. the six balanced sign patterns with a fixed internal ordering of the two
   positive and two negative labels;
2. the average over the eight labelled alternating words.

The companion exact-rational checker reconciles them.

For a fixed scale s and factor splits

    (x,s-x),
    (y,s-y),

let

    C6

be the sum over the six choices of positive positions, with the positive
labels kept in the order (0,1) and negative labels in the order (2,3).

Let

    C24

be the sum over all 24 labelled permutations.

Let

    C8

be the sum over the eight labelled alternating permutations.

Then exactly

    boxed:

    C24 = 4 C6,

because the ordered product convolution already contains the two
same-sign label permutations on each side.

The four nonalternating sign patterns vanish, so

    boxed:

    C24 = C8.

Therefore

    boxed:

    C6/2 = C8/8.

The common normalized Brownian kernel is

    boxed:

    C8/8
      =
      -(s-1)
      min(
        d_s(x),
        d_s(y)
      ),

where

    d_s(u)
      =
      min(
        u-s+1,
        1-u
      ).

Equivalently,

    boxed:

    C6
      =
      -2(s-1)
      min(
        d_s(x),
        d_s(y)
      ).

Thus the factor-of-two difference between the two fixed-scale formulas is
pure normalization, not a missing orientation.

This closes the orientation-factor check needed by the product-convolution
ledger.

See:

    notes/WP84_PHI4_EQUAL_SCALE_BROWNIAN_KERNEL.md
    notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md
    src/wp84_phi4_equal_scale_brownian_kernel.py
