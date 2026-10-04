# WP71 G9-C — MRT already contains the needed maximal/truncation machinery

Date: 2026-10-04
Status: **SOURCE MECHANISM IDENTIFIED; Stage-A short-window substitution still open**

A closer read of the published MRT paper improves the G9-C situation.

## Published ingredients

MRT Lemma 2.2 defines the maximal subinterval norm

[
left|sum_{Xle nle X_0} g(n)ight|^*
=
sup_{Xle X_1le X_2le X_0}
left|sum_{X_1le nle X_2}g(n)ight|
]

and proves a summation-by-parts inequality in that maximal norm.

MRT Corollary 2.5 then gives, uniformly for **any** interval
([X_1,X_2]), a pointwise bound for the truncated Dirichlet series

[
D[f1_{[X_1,X_2]}](1/2+it)
]

in terms of a logarithmically weighted integral of the untruncated
(D[f](1/2+i(t+u))), plus a controlled truncation error.

This is not merely background: in the proof of Proposition 5.4 MRT explicitly
invokes Corollary 2.5 to remove the support truncation before applying the
Dirichlet-polynomial mean-value estimates.

## Consequence for our strategy

We do **not** need to invent a new ad hoc maximal-prefix framework.

The moving endpoint family from G9-B should be inserted into MRT through the
same two devices they already use:

1. Lemma 2.2 for maximal/summation-by-parts control;
2. Corollary 2.5 for arbitrary interval truncation at the Dirichlet-series
   level.

The arbitrary logarithmic saving in Proposition 5.4 means the logarithmic
losses introduced by Corollary 2.5 are, in principle, absorbable by requesting
a stronger source exponent.

## What is still not automatic

This source observation does **not** yet close G9-C.

Our moving intervals have their own short length (Y), whereas the ambient
prime scale is (M).  The proof still has to verify that the transformed
parameters remain inside MRT's actual ranges:

[
H=M^{8/33+arepsilon},
qquad
Q=(log M)^B,
]

[
M^{-1/6-arepsilon}lelambdale 1/(qQ).
]

The Stage-A argument must also show that the resulting bound scales with the
moving-window length (Y), not merely with the ambient (M).

That short-window scaling is where Proposition 5.5 / the Appendix-A
mean-value input may be needed in addition to Proposition 5.4.

## Correct citation map

- Lemma 2.2: maximal summation by parts.
- Corollary 2.5: arbitrary interval truncation of Dirichlet series.
- Proposition 5.4: main long-shift mean-value estimate; proved in Sections
  6--7.
- Proposition 5.5: complementary mean-value estimate associated with
  short-interval control; its proof is in Appendix A.

Thus the public shorthand "Prop. 5.4, App. A" should be replaced by this
four-piece citation chain.

## Current G9-C target

The remaining task is now sharply formulated:

> carry the exact G9 moving endpoint family through Lemma 2.2 and Corollary
> 2.5, use Propositions 5.4/5.5 in their stated ranges, and derive the
> structured-shift bound at the actual window scale (Y).

No percentage claim is promoted until that substitution is written in full.
