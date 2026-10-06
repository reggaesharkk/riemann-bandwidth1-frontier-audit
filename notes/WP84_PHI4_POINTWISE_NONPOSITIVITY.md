# WP84 — pointwise nonpositivity of the connected fourth-order kernel

Date: 2026-10-05

Status: **EXACT FINITE ARRANGEMENT CERTIFICATE: THE CLOSED-CYCLE CONNECTED FOURTH-ORDER KERNEL IS POINTWISE NONPOSITIVE**

No unconditional zero-density percentage is claimed here.

The existing support theorem proved

    C4(v)=0

whenever the balanced product scale

    s=(|v0|+|v1|+|v2|+|v3|)/2

satisfies s<=1, and that the total connected integral is -1/60.

A stronger property is true:

    boxed:
    C4(v)<=0

for every real closed four-step vector

    v0+v1+v2+v3=0.

This note gives a finite exact certificate.

## 1. Factor out the common walk overlap

For a closed four-step cycle write

    v3=-(v0+v1+v2).

The first overlap factor is common to all 26 connected ordered-partition
terms:

    O_A(v)
      =
      (1-spread{0,v0,v0+v1,v0+v1+v2})_+.

Hence

    C4(v)
      =
      O_A(v) B4(v),

where

    B4(v)
      =
      sum_terms sign(term)
        (1-spread_B(term;v))_+.

Since O_A>=0, it is enough to prove

    B4(v)<=0

on the support polytope

    spread_A<=1.

## 2. B4 is piecewise affine

Every position in every second overlap is an integer-coefficient linear form
in

    x=(v0,v1,v2).

For one overlap, max/min branches can change only when two such positions are
equal:

    ell_i(x)-ell_j(x)=0.

The positive-part cutoff can change only when the spread reaches one, i.e.

    ell_i(x)-ell_j(x)=+/-1.

Therefore all kinks of every term lie in the finite hyperplane family

    ell_i-ell_j in { -1,0,+1 }.

The common support boundary has the same form.

After removing scalar duplicates, the complete arrangement contains only

    boxed:
    21 hyperplanes.

## 3. Exact vertex principle

These hyperplanes, together with the bounded support cube, partition the
support region into convex polyhedral cells.

On each cell every max/min choice and every cutoff status is fixed, so B4 is
one affine rational function.

An affine function reaches its maximum on a bounded polytope at a vertex.

Thus it suffices to inspect every arrangement vertex lying in

    spread_A<=1.

Every such vertex is an intersection of three independent hyperplanes from
the complete arrangement.

The companion checker enumerates all such intersections using exact
fractions.

## 4. Exact enumeration result

The complete arrangement has

    21 unique hyperplanes.

Their independent triple intersections produce

    35 rational vertices inside the ambient cube.

Exactly

    21

lie in the closed common-support polytope

    spread_A<=1.

At every one of those support vertices,

    boxed:
    B4(v)<=0.

The largest exact value is

    boxed:
    0.

No floating arithmetic enters the acceptance decision.

Therefore B4<=0 on every support cell, and hence globally

    boxed:
    C4(v)<=0.

## 5. Relation to the previous support theorem

For s<=1 the earlier untruncated-cancellation theorem gave

    C4(v)=0.

The present result shows that once the connected kernel turns on beyond the
classical wall, it can only move downward:

    boxed:
    s<=1  => C4=0,

    boxed:
    s>1   => C4<=0.

The inequality may be strict on a nonempty open set.

This is consistent with the exact integral

    integral C4=-1/60.

## 6. Consequence for the fourth-moment strategy

At the limiting closed-cycle/model level, the connected sector can never
increase the centered fourth moment above the complete pair layer

    4/15.

Thus a theorem-side upper bound does not need to recover the exact
connected constant -1/60.

It is enough to show that finite-compression nonclosed/near-resonant leakage
does not create a positive error larger than the available record budget.

This is a weaker arithmetic target than proving the full connected
asymptotic.

Important boundary:

    the pointwise sign theorem is for the exact closed-cycle kernel.

It does not by itself sign-control finite-T nonclosed words carrying a
Dirichlet kernel and carrier phase.

Those near-resonant terms remain the arithmetic error to bound.

## 7. Current numerical slack

The quartic fixed-band route is best written in terms of the centered fourth
moment

    w_R=tau(P_R^4).

For the matched quartic majorant,

    tau P4(I+P_R)
      =
      1/2000
      +(213/1000) v_R
      +(593/2000) w_R
      +o(1),

with

    v_R=tau(P_R^2)<=1/3+o(1).

Therefore the variance deficit from band truncation does not cost positive
error when the theorem is parameterized by w_R.

For R=400 the sufficient centered-fourth ceiling is approximately

    boxed:
    w_R < 0.2911227517.

The full pair layer is

    4/15
      =0.2666666667...,

leaving

    boxed:
    about 0.0244560851

of positive room above the complete pair contribution.

Because the closed connected kernel is nonpositive, this entire amount may
be spent on finite-compression / weighted-correlation error.

See:

    notes/WP84_MATCHED_QUARTIC_MAJORANT.md
    notes/WP84_PHI4_SUPERCRITICAL_SUPPORT_THEOREM.md
    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
