# WP84 — delta=79 sharp functional-band rung

Date: 2026-10-06

Status: **EXACT SHARPENING OF THE FUNCTIONAL O(1/R) FIXED-BAND FALLBACK; ARITHMETIC DEGREE-SIX GATE STILL OPEN**

No unconditional zero-proportion theorem is claimed here.

The preceding functional-calculus theorem gives, for every fixed bounded
C^2 consumer f,

    |tau f(H)-tau f(H_R)|
      <=
      3 ||f''||_infinity/(pi^2 R)
      +o(R^-1)

in the sharp prime normalization.

A small exact parameter search shows that delta=79 gives a slightly stronger
integer-curvature rung than delta=80.

## 1. Exact global curvature certificate

Let

    F_79(x)
      =
      80 P(x)^2/(P(x)^2+79).

Exact differentiation writes

    F_79''(x)=N(x)/D(x),

with D(x)>0 on the real line.

After clearing denominators, the companion gate applies exact Sturm root
counts to

    71 D+N

and

    71 D-N.

Both have zero real roots and are positive at x=0.

Therefore

    boxed:

    ||F_79''||_infinity < 71.

This is very close to the true numerical supremum
about 70.99615983, but the theorem uses only the exact integer 71.

## 2. Fully rational band constant

Using pi>333/106,

    3*71/pi^2
      <
      213 (106/333)^2

      =
      boxed:

      797756/36963

      ~=21.5825555285.

Hence

    boxed:

    |tau F_79(H)-tau F_79(H_R)|
      <
      [797756/36963]/R
      +o(R^-1).

## 3. Exact R=12000 first->79 gate

The Jensen model cap is

    boxed:

    h_79(w0)
      =
      28300/274701
      ~=0.103021102944656,

with

    w0=1415/13891.

At R=12000 the rational band charge is

    boxed:

    199439/110889000
      ~=0.00179854629404179.

Therefore

    boxed:

    h_79(w0)
      +
      band_charge

      <
      0.105

by the exact residual

    boxed:

    915620351/5076886531500
      ~=0.000180350761302021.

This slightly improves the delta=80 residual at the same band.

Inverting h_79 gives the exact banded Christoffel-square target

    boxed:

    limsup_T tau P(H_12000)^2
      <
      452034287/4429838047

      ~=0.102043072953001.

The allowed excess above the Christoffel model value is

    boxed:

    10987444212/61534880310877

      ~=0.000178556359523102.

## 4. Strategic meaning

This is currently the sharpest certified integer-curvature fixed-band rung
on the branch.

It does not change the nature of the hard theorem:

    prove the single degree-six fixed-band square estimate.

The gain over delta=80 is modest but exact.  More importantly, it confirms
that the functional-calculus full-to-band theorem is stable under nearby
consumer parameters and can be optimized without returning to six-pole
residue sums.

The selected primary attack remains the minimal-radius one-point grouped
heat-curvature route.

See:

    notes/WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md
    notes/WP84_FIXED_BAND_CHRISTOFFEL_CENTERED_LEDGER.md
