# WP84 — principal-major-arc geometry of the balanced E2 window

Date: 2026-10-06

Status: **SOURCE-INTERFACE CORRECTION — THE ACTUAL WP84 LOCAL FREQUENCY WINDOW LIES INSIDE THE q=1 PRINCIPAL MAJOR ARC THROUGHOUT THE E2 LONG-SHIFT RANGE**

No unconditional zero-density percentage is claimed here.

The balanced product reduction and the discrete-to-local oversampling lemma
remain valid.

The source interface needs one correction: the actual WP84 sampled frequency
window is not centered on a generic minor-arc point. In the long-shift range
it sits inside the principal q=1 major arc.

## 1. Actual frequency location

On one product cell of scale M put

    H=M/T.

The additive frequencies are

    alpha_k
      =
      tau_k/(2pi M).

For the consumed height window

    T <= tau_k <= 2T+o(T),

we have

    boxed:

    1/(2pi H)
      <=
      alpha_k
      <=
      1/(pi H)+o(1/H).

Thus the local interval has width comparable to 1/H, but its location is
also O(1/H) from the origin.

## 2. Evans major-arc parameters

In Evans' E2 circle-method decomposition the major arcs have the form

    |alpha-a/q|
      <=
      1/(qQ),

with

    q<=Q_0,

and the parameter choice satisfies

    Q_0<P<Q<H

in the long-shift regime.

For q=1, the principal major arc about 0 therefore contains

    |alpha|
      <=
      1/Q.

Since

    Q<H,

we have

    1/H<1/Q.

Consequently, for all sufficiently large T,

    boxed:

    [1/(2pi H),1/(pi H)]
      subset
    [-1/Q,1/Q].

Hence the complete WP84 local frequency window lies in the q=1 principal
major arc.

## 3. Consequence for the source interface

The minor-arc estimate is not the load-bearing theorem for the main WP84
window.

The correct decomposition on the consumed window is the q=1 specialization
of the major-arc expansion

    S(alpha)
      =
      a(alpha)+b(alpha),

where the principal term is

    a(alpha)
      =
      C_P
      sum_{M<n<=2M}
        e(alpha n),

with

    C_P
      =
      sum_{P<p<=P^(1+delta)}
        1/p,

and b(alpha) is the centered E2 remainder.

The published major-arc analysis proves an L2 estimate for b over the full
major-arc family. A WP84 transfer must adapt that estimate to the exact
factor-sliced smooth coefficient and to the local q=1 window.

## 4. Why Proposition 3.5 is not enough by itself

The local minor-arc estimate has the scale

    int_{minor cap J}
      |S(alpha)|^2 d alpha
      <<
      M/log^(1+eta) M,

with |J|~1/H.

The WP84 normalized discrete average converts a local integral with a
multiplicative factor comparable to H.

Therefore a bound of the displayed size would contribute schematically

    H M/log^(1+eta) M

before the project normalization.

For polynomial H this does not automatically give o(1).

So even away from the principal arc, the local minor-arc estimate cannot be
promoted to a WP84 closure without checking the exact coefficient and
normalization savings.

## 5. Correct primary target

After the oversampling lemma, the main long-shift cell is controlled by

    H
    int_J
      |F(alpha)|^2 d alpha,

with

    J
      subset
      [-1/Q,1/Q].

The correct target is therefore:

1. transfer the WP84 factor-sliced coefficient to a q=1 principal model
   plus centered remainder;

2. identify the principal model contribution with the already-certified
   closed-cycle connected main;

3. prove that the centered q=1 remainder contributes o(1) after the exact
   WP84 normalization.

This is a major-arc error theorem, not a minor-arc theorem.

## 6. Published major-arc structure that is relevant

For the E2 weight the major-arc decomposition uses the principal-character
approximation

    C_P
    sum e(beta n)

and a centered remainder.

The published source proves that the global major-arc remainder energy

    B^2(M)

is smaller than the full scale by a power of log.

That estimate is structurally relevant, but the WP84 theorem still needs a
same-normalization transfer because multiplying a generic local L2 estimate
by H may lose the required saving.

The newer type-II major-arc machinery for divisor-bounded convolutions is
also structurally aligned with the WP84 Lambda*Lambda factorization, but no
direct import is claimed here.

## 7. Status of the previous E2 notes

Still valid:

- exact product collapse;
- H=M/T shift geometry;
- multiplicative-to-additive phase linearization;
- oversampled discrete-to-local transfer;
- shrinking transition-layer mass o(1).

Corrected:

- the main local window should not be described as a minor-arc window;
- Proposition 3.5 is a side estimate, not the primary source bridge.

## 8. Remaining arithmetic debt

The long-shift fourth-order sector now has one central source-transfer target:

    boxed:

    q=1 centered major-arc error
      =
      o(1)

in the exact WP84 normalized weighted energy.

If that closes and the principal term matches the nonpositive closed-cycle
kernel, the positive connected leakage is o(1), comfortably below the
R=400 allowance >0.0247937.

No unconditional record theorem is claimed.

See:

    notes/WP84_E2_LOCAL_WINDOW_TRANSFER.md
    notes/WP84_E2_OVERSAMPLING_TRANSFER.md
    notes/WP84_E2_TRANSITION_LAYER_MASS.md
    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
