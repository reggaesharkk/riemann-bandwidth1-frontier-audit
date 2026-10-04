# WP82 — exact well-spacing lemma for the dilated spectral frame

Date: 2026-10-04
Status: **FINITE GRID / GEOMETRIC WELL-SPACING CLOSED; HYBRID SIZE BUDGET STILL OPEN**

The public `face_arcs.py` mixes two logically different claims:

1. a deterministic well-spacing statement for images of major arcs;
2. an analytic hybrid large-sieve/minor-supremum size estimate.

Only the first is closed here.

## 1. Grid setup

On an analysis grid of period N, let the two dilated frequencies be

    gamma_m(j)=b2*j/N mod 1,
    gamma_n(j)=b1*j/N mod 1.

Fix one m-side major center a/Q and a half-width w/Q, with Q<=P. The admissible FFT bins satisfy

    || b2*j/N - a/Q || <= w/Q.

Since Q>=1, they lie inside a circular interval of undilated width at most 2w.

## 2. At most b2 image arms

Partition admissible bins by the residue class

    j mod b2.

There are trivially at most b2 classes. These are exactly the image arms used by the public face.

Within a fixed arm, two consecutive bins have

    j'-j = t*b2

for a positive integer t. Therefore their n-side images differ by

    gamma_n(j')-gamma_n(j)
      = t*b1*b2/N   (mod 1).

So the fundamental image spacing is exactly

    boxed: b1*b2/N.

The n-side/m-side roles interchange symmetrically.

## 3. Bin-count bound

A circular interval of length at most 2w contains at most `2wN` grid spacings, plus endpoint/residue rounding. A conservative exact integer form is

    #bins <= 2*w*N + b2 + 1,

the same envelope used in `face_arcs.py`.

No prime number theorem, Vaughan estimate, or large sieve is involved.

## 4. Independent checker

`src/wp82_well_spacing_exact.py` checks the exact integer statements over many unrelated grids, dilation pairs, major denominators and rational widths. It uses `fractions.Fraction`; no floating tolerance is involved.

## 5. Evidence boundary

This closes only the geometric/well-spacing half of the public mixed/minor leaf.

The still-open analytic statement is the **hybrid size budget**: after stratifying all major image arms, prove that the union large-sieve branch or the minor-supremum branch gives a total logarithmic saving uniformly across every stratum.

The public `face_arcs.py` compares such a budget with measured mixed spectral mass and accepts ratios around 24--31x. That is a useful falsifier, not the asymptotic proof.
