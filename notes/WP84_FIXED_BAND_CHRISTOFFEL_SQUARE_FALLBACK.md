# WP84 — fixed-band Christoffel-square fallback for a direct >79 theorem

Date: 2026-10-06

Status: **EXACT REDUCTION OF THE BOUNDED SIX-POLE CONSUMER TO ONE FIXED-BAND DEGREE-SIX POSITIVE SQUARE; FIXED-BAND ARITHMETIC ESTIMATE OPEN**

No unconditional zero-proportion theorem is claimed here.

The active shifted one-point heat-flow route remains the primary attack.  This
note records a separate fallback that avoids a full large-T resolvent-state
law if the fixed-band degree-six arithmetic can be closed.

The key observation is that the bounded Christoffel family can be band-truncated
*before* using the degree-six Christoffel square.  This preserves the
Proposition-R firewall: the unbounded polynomial is never applied directly to
the full arithmetic matrix.

## 1. Bounded consumer

Let

    P(x)
      =
      1-(43428/13891)x
       +(37704/13891)x^2
       -(9660/13891)x^3,

    g(x)=P(x)^2,

    w0=1415/13891.

For fixed delta>0 define

    F_delta(x)
      =
      (delta+1) g(x)/(g(x)+delta),

and

    h_delta(w)
      =
      (delta+1) w/(delta+w).

Then

    F_delta=h_delta o g,

and h_delta is increasing and concave on w>=0.

The exact Christoffel certificate gives g(x)>=1 for x<=0, hence

    F_delta(x)>=1
    for x<=0.

Therefore the usual positive-index consumer is valid.

## 2. Full-to-band comparison uses only fixed nonreal poles

Let H be the full sharp Loewner matrix and H_R its hard displacement-band
truncation.  Write

    Delta_R=H-H_R.

For a fixed nonreal pole z the already-established second-resolvent identity
gives

    |m_H(z)-m_HR(z)|
      <=
      6/(pi^2 |Im z|^3 R)
      +o(R^-1)

in the sharp normalization q_alpha=1/4+o(1).

Write the six simple poles of F_delta as z_j(delta), and their residues as

    c_j(delta)
      =
      -delta(delta+1)/
       [2 P(z_j) P'(z_j)].

Then, for every fixed delta for which the poles stay off the real axis,

    boxed:

    |tau F_delta(H)-tau F_delta(H_R)|
      <=
      C_band(delta)/R
      +o(R^-1),

where the explicit finite constant is

    boxed:

    C_band(delta)
      =
      (6/pi^2)
      sum_{j=1}^6
        |c_j(delta)|/|Im z_j(delta)|^3.

This is a bounded-consumer comparison.  No degree-six raw moment of the full
matrix is used.

## 3. Jensen collapses the banded consumer to one scalar positive square

Because h_delta is concave,

    tau F_delta(H_R)
      =
      tau h_delta(g(H_R))

      <=
      h_delta(
        tau g(H_R)
      )

exactly.

Therefore

    boxed:

    tau F_delta(H)
      <=
      h_delta(
        tau P(H_R)^2
      )
      +
      C_band(delta)/R
      +
      o(R^-1).

This is the central reduction.

The entire bounded >79 theorem can therefore be obtained from ONE fixed-band
degree-six positive observable

    boxed:

    tau P(H_R)^2.

No separate convergence theorem for m1,...,m6 is logically required.

## 4. Exact sufficient inequality

A simple-zero proportion above 79 percent follows once

    tau F_delta(H)<0.105-o(1).

Hence it is sufficient to prove, for one fixed delta and one fixed R,

    boxed:

    h_delta(
      limsup_T tau P(H_R)^2
    )
      +
      C_band(delta)/R
      <
      0.105.

Equivalently, if

    epsilon_band
      =
      0.105-C_band(delta)/R

is positive, then it suffices that

    limsup_T tau P(H_R)^2
      <
      h_delta^{-1}(epsilon_band),

where

    h_delta^{-1}(y)
      =
      delta y/(delta+1-y).

This is an exact scalar fixed-band kill gate.

At the frozen Christoffel value w0,

    h_delta(w0)

is exactly the Jensen cap already used by the bounded-consumer route.  Since
h_delta(w0)<0.105 for every sufficiently large fixed delta, and
C_band(delta)<infinity, there always exists a finite fixed R for which the
model point w0 has positive >79 margin.

Thus the remaining issue is not existence of a band radius.  It is proving
the one-sided fixed-band arithmetic inequality for the single positive square.

## 5. Numerical conditioning reconnaissance only

The companion script evaluates the explicit six-pole constant numerically.
These numbers are conditioning diagnostics, not theorem constants until the
root/residue enclosures are independently certified.

For example, at delta=101 it finds approximately

    min pole height
      1.1777492995,

    C_band(101)
      64.5778838945.

At the illustrative fixed radius

    R=40000,

the numerical band charge is

    0.00161444710.

The exact Jensen model cap is

    h_101(w0)
      ~=0.10276942707,

so the numerical model-side total is approximately

    0.10438387417,

leaving about

    0.00061612583

below the 0.105 first->79 defect ceiling.

Again, this is only a scale diagnostic.  The exact reduction in Sections 1--4
does not depend on these decimal values.

## 6. Why this route is potentially useful

The unresolved shifted heat-flow theorem controls an infinite-dimensional
state evolution at one fixed nonreal point.

The present fallback asks instead for a fixed-band limit of

    tau P(H_R)^2,

with R fixed before T->infinity.

For fixed R this is a finite-displacement degree-six word problem.  The
degree-four R=400 program already developed:

- exact pair-sector contractions;
- sign-balance / unique-factorization gates;
- fixed-scale connected-kernel negativity;
- detuning commutator reduction;
- good-endpoint trimming;
- proper-prime-power disposal.

Those mechanisms do not automatically prove the degree-six square, but they
are structurally closer to it than a full resolvent law is.

In particular, the theorem target is the complete combined Christoffel square,
not six separate raw moments.  Signed/positive cancellations inside P(H_R)^2
must be preserved before taking termwise absolute values.

## 7. Proposition-R firewall

The order of operations is essential:

1. start with the bounded consumer F_delta(H);
2. compare H to H_R using only fixed-pole resolvent identities;
3. only then invoke Jensen on the bounded banded matrix;
4. expand P(H_R)^2, if needed, inside the fixed-band arithmetic problem.

Do **not** replace Step 1 by the unbounded polynomial g(H) on the full matrix.

## 8. Evidence boundary

Closed in this note:

- exact bounded-consumer-to-band comparison formula with explicit
  C_band(delta);
- exact Jensen reduction to one scalar fixed-band positive square;
- exact inversion of the >79 threshold;
- theorem-safe Proposition-R ordering.

Open:

- a certified numerical enclosure for any selected C_band(delta), if an
  explicit finite R is to be frozen;
- the large-T fixed-band arithmetic estimate for tau P(H_R)^2;
- final insertion of the already-audited zero-count transfer.

This route is a fallback / parallel attack.  It does not replace the selected
shifted exact-frontier heat-flow route unless the degree-six fixed-band
arithmetic closes first.

See:

    notes/WP84_BOUNDED_CHRISTOFFEL_JENSEN.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
    notes/WP84_R400_COMPLETE_WORD_LEDGER_REPLAY.md
    notes/WP84_FIXED_BAND_M4_EVIDENCE_BOUNDARY.md
