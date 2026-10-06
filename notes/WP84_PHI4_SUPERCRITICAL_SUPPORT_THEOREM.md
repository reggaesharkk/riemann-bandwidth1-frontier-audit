# WP84 — exact support theorem for the connected Phi4 correction

Date: 2026-10-05

Status: **KILL-GATE ADVANCE — THE ENTIRE CONNECTED FOURTH-ORDER CORRECTION IS SUPPORTED STRICTLY BEYOND PRODUCT SCALE T; CLASSICAL SIDE CANCELS POINTWISE**

The previous sign-balance reduction showed that balanced 2-vs-2 product
collisions are the first genuinely hard finite-compression sector.

This note sharpens that statement dramatically.

For the exact public connected four-cycle kernel, the connected integrand is
**identically zero** whenever the balanced product scale is at or below the
classical threshold.

Consequently the whole exact value

    Phi4 = -1/60

comes from the supercritical product region.

## 1. Closed four-step variables and product scale

Write the four signed normalized logarithmic shifts as

    v0,v1,v2,v3,
    v0+v1+v2+v3=0.

Define

    s
      = sum_{vj>0} vj
      = sum_{vj<0} (-vj)
      = (|v0|+|v1|+|v2|+|v3|)/2.

For a balanced multiplicative relation

    A/B = 1,

this is exactly

    s = log A / L = log B / L.

Thus:

    s<=1  <=>  product scale A,B <= exp(L)=X,
    s>1   <=>  product scale A,B > X.

At bandwidth lambda=1, X is asymptotic to T.

## 2. Every ordered-partition path has spread at most s

A connected-cumulant term is indexed by an ordered set partition.

Its overlap positions are a nested chain of subset sums

    0,
    sum_{j in S1} vj,
    sum_{j in S2} vj,
    ...,
    0,

with

    empty subset S0 subset S1 subset ... subset all labels.

Take any two positions in the chain.  Their difference is the sum of the
vj over one set difference.

The positive part of any such partial sum is at most the total positive mass
s, and its negative magnitude is at most the total negative mass s.

Because the two subsets are nested, the absolute difference of the two
positions is at most s.

Therefore every connected overlap path satisfies exactly

    boxed:
    spread <= s.

In particular, if s<=1, the positive-part cutoff never activates:

    (1-spread)_+ = 1-spread.

## 3. Exact untruncated connected cancellation

The b=4 connected kernel has 26 ordered-partition terms.

Remove the positive-part truncation from the second overlap factor.  The
signed sum is

    C4_untr(v)
      = sum_terms sign(term) * [1-spread_term(v)].

The companion exact chamber checker proves

    boxed:
    C4_untr(v) == 0

for every real closed four-step vector v.

The proof is finite and exact.

All max/min choices can change only on the seven hyperplanes

    v2=0,
    v1=0,
    v1+v2=0,
    v0=0,
    v0+v2=0,
    v0+v1=0,
    v0+v1+v2=0.

These seven central planes have 32 feasible open chambers.

On every chamber:

- the 13 positive and 13 negative constant coefficients cancel;
- every spread is one fixed integer linear form;
- the signed sum of the three linear coefficients is exactly (0,0,0).

Hence the untruncated connected kernel vanishes identically, not merely after
integration.

Companion:

    src/wp84_phi4_untruncated_cancellation.py

## 4. Pointwise support theorem

Combine Sections 2 and 3.

For s<=1 no connected term is truncated, so the actual connected kernel is
the untruncated kernel.

Therefore

    boxed:
    C4(v)=0 pointwise for every s<=1.

This is stronger than saying the integral over that region vanishes.

It says there is literally no connected fourth-order density on the
subcritical product side.

## 5. Entire -1/60 comes from s>1

The independent exact public archive certifies

    integral C4 = Phi4 = -1/60.

Since the integrand vanishes pointwise on s<=1,

    boxed:
    integral_{s>1} C4 = -1/60.

Thus the connected repair needed to move

    pair layer 4/15

to

    centered m4 = 1/4

is a purely supercritical-product phenomenon.

No part of Phi4 is hiding in the classical product range.

## 6. Exact explanation of the k*lambda=2 wall

For a balanced degree-k word with k=2m, the positive product scale is
approximately

    T^(m lambda).

Finite averaging has length T.

The first time the product Dirichlet polynomial becomes longer than the
averaging interval is

    m lambda > 1,

equivalently

    boxed:
    k lambda > 2.

The support theorem above shows, at the first nontrivial case k=4, that the
connected correction is supported **exactly on the far side of that wall**.

So three previously separate observations are the same geometry:

1. Rudnick--Sarnak classical diagonal range: k lambda < 2;
2. Proposition-R starts carrying nontrivial zero-free strength: k lambda > 2;
3. Phi4 connected density turns on only when the balanced product scale
   crosses T.

This is not numerical coincidence.

## 7. Why the Evans almost-prime theorem now matters much more

The companion product-correlation bridge identified product scale M and shift
range

    H_M ~ M/T.

For every fixed s>1,

    M=T^(s+o(1)),
    H_M=T^(s-1+o(1)),

which eventually dominates every fixed power of log M.

Therefore every fixed supercritical scale is deep inside the range of the
published average E2-correlation theorem of Natalie Evans.

The only region not automatically covered by its stated
H >= log^(19+eps) M threshold is an asymptotically shrinking layer immediately
above s=1.

The new support theorem tells us that this shrinking transition layer is the
**only** remaining interface between classical mean-value technology and the
published long-shift almost-prime machinery.

That is a much narrower theorem problem than the original fourth-moment
transport.

## 8. Consequence for the bounded six-pole route

The theorem target remains bounded:

    F_delta(H_T)

at six fixed nonreal poles.

We do not revive a finite-T raw fourth-moment theorem.

Instead Phi4 is used only as the fail-closed calibration of the bounded
D1/D2 generator.

The next analytic task is now:

    classical/subcritical side
      -> exact connected cancellation;

    fixed supercritical product scales
      -> weighted Evans L2 almost-prime correlation;

    shrinking threshold layer s=1+o(1)
      -> explicit transition estimate;

    assemble into bounded six-pole D1/D2 inequality.

No unconditional >79% theorem is claimed yet.


## 9. Quantitative turn-on bound at the threshold

The same argument gives more than support.

For one ordered-partition term with spread r,

    (1-r)_+ - (1-r) = (r-1)_+.

The complete untruncated connected sum is exactly zero, so the actual
connected bracket can be written entirely as a signed sum of truncation
defects.

There are 26 terms, and every ordered-partition spread obeys

    r <= s.

Hence pointwise

    |C4(v)|
      <= sum_terms (r_term-1)_+
      <= 26 (s-1)_+.

Including the common first overlap can only reduce the magnitude.

Therefore

    boxed:
    |connected Phi4 density|
      <= 26 (s-1)_+.

So the connected sector not only starts at s=1; it turns on at most linearly
in the excess product exponent.

For a transition layer

    1 < s <= 1+epsilon

the kernel itself is uniformly O(epsilon).

This converts the remaining short-shift patch into a domination problem for
the underlying weighted almost-prime correlation measure.  We no longer need
to discover cancellation inside the connected kernel there; the kernel has
already supplied an explicit small factor.
