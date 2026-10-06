# WP84 — R=400 first-record assembly ledger

Date: 2026-10-06

Status: **NEAR-FINAL SAME-CONVENTION ASSEMBLY; IF THE GOOD-ENDPOINT PRINCIPAL-SECTION INSERTION IS ACCEPTED IN THE FIXED-BAND ORDER-FOUR LEDGER, THE CURRENT R=400 CONSTANTS ALREADY CLEAR THE RECORD THRESHOLD**

No unconditional percentage theorem is claimed in this note.

This note assembles only theorem-side quantities already present on the branch.

## 1. Bounded route and band charge

Use the matched bounded consumer and hard displacement band R=400.

The full-to-band charge is

    C_match/R,

with

    C_match = 2.1728342265... .

Thus

    C_match/400
      =
      0.00543208556625....

The quartic polynomial is applied only after the bounded full-to-band step.

## 2. Centered quartic identity

For the fixed-band centered state P_R,

    tau P4(H_R)

      =
      1/2000
      +(213/1000) v_R
      +(593/2000) w_R
      +o(1),

where

    v_R=tau(P_R^2),
    w_R=tau(P_R^4).

Since

    v_R<=1/3+o(1),

we have

    boxed:

    tau P4(H_R)

      <=
      1/2000
      +213/3000
      +(593/2000) w_R
      +o(1).

## 3. Pair plus connected ledger at R=400

The exact pair theorem gives

    boxed:

    Pair_400
      <
      0.266329.

The connected-sector reductions give:

- closed/equal-scale connected bulk is nonpositive;
- four nonalternating balanced words vanish;
- proper-prime-power sectors are o(1);
- the sharp unequal-scale residual is rank-two-endpoint reducible;
- the good-endpoint trimming note gives an o(1) endpoint budget after an
  o(d) row deletion performed at the bounded-consumer level.

Therefore the desired promotion statement is

    boxed:

    w_400
      <=
      0.266329
      +o(1).

This line is the final same-convention bookkeeping gate.  It must be replayed
against the complete order-four word ledger before theorem promotion.

## 4. Numerical consequence if the bookkeeping gate passes

Insert

    w_400<=0.266329+o(1).

Then

    tau P4(H_400)

      <=
      1/2000
      +213/3000
      +(593/2000)(0.266329)
      +o(1)

      =
      boxed:

      0.1504665485
      +o(1).

Add the full-to-band charge:

    defect
      <=
      0.1504665485
      +0.00543208556625
      +o(1)

      =
      boxed:

      0.15589863406625
      +o(1).

The conservative comparison ceiling is

    E_rec
      =
      0.163249981456072....

Hence the remaining theorem-side margin would be

    boxed:

    E_rec
      -
    0.15589863406625

      =
      0.007351347389822...
      >0.

## 5. Induced simple-zero coefficient

The consumer conversion is

    C_simple
      =
      1-2 defect.

Thus the assembled R=400 bound would give

    boxed:

    C_simple
      >=
      0.6882027318675
      +o(1)

      =
      68.82027318675...%.

This is a theorem-side assembled coefficient, not a model ledger.

It is deliberately below the 70.875% quartic model value because:

- the connected negative -1/60 is not consumed quantitatively;
- only the upper bound connected<=o(1) is used;
- the fixed R=400 band charge is paid in full.

## 6. What is still required before promotion

Do not call 68.820273... an unconditional theorem until the following final
replay passes:

1. start from the complete fixed-band order-four word ledger;
2. apply the selected principal frequency section from
   WP84_GOOD_ENDPOINT_TRIMMING;
3. verify the pair sector changes by only o(1);
4. verify every 3-vs-1, same-sign, proper-power, and boundary term is already
   covered by an existing o(1) gate in this exact normalization;
5. verify the balanced nonclosed remainder is exactly the detuning endpoint
   object closed by the good-endpoint argument;
6. assemble the bounded rank-deletion charge, band charge, quartic majorant,
   and normalization in one inequality.

If those six checks pass, no new analytic-number-theory theorem is needed for
the R=400 first strike.

See:

    notes/WP84_GOOD_ENDPOINT_TRIMMING.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
    notes/WP84_CENTERED_M4_SCALAR_GATE.md
    notes/WP84_MATCHED_QUARTIC_MAJORANT.md
    notes/WP84_SIGN_BALANCE_NEAR_RESONANCE_GATE.md
    notes/WP84_ORDER4_VSUM_PRIME_RESONANCE.md
