# WP84 — exact V-sum phase-cancellation falsifier

Date: 2026-10-05

Status: **AUTOMATIC SAME-SIGN CANCELLATION FALSE FOR THE TRUE INTERMEDIATE RESOLVENT**

The four-branch prime-square variance split contains mixed-sign difference branches `V_diff` and same-sign sum branches `V_sum`.

The carrier gauge already shows that the large T-phase is not an invariant source of cancellation. A remaining possibility was that transpose/branch symmetry might still force `V_sum` to disappear for the actual resolvent. It does not.

## Exact carrier-free counterexample

Let `S` be the non-cyclic one-step shift on five coordinates and put

    H = S + S^*.

At the fixed nonreal point `z=i`, set

    R=(H-iI)^(-1).

All entries of R lie in Q(i). Define

    first
      = tau(R S R)+tau(R S^* R),

    V_sum
      = tau(R S R S R)+tau(R S^* R S^* R),

    V_diff
      = tau(R S R S^* R)+tau(R S^* R S R).

Exact Gaussian-rational elimination gives

    first = 7 i / 20,
    V_sum = 17 i / 80,
    V_diff = 3 i / 80.

Hence

    |V_sum|/|V_diff| = 17/3.

So the same-sign branch is not merely nonzero in this exact finite sharp model; it is larger than the mixed branch.

## What the multiplication surrogate hides

If the resolvent is replaced by a diagonal/multiplication operator, the first-order shifted trace and same-sign variance trace vanish geometrically.

That conditional calculation is correct. But once the resolvent is the actual inverse of a translation operator, it contains off-diagonal shift words. Those words can close the net translation inside both first-order and same-sign products.

Therefore the rule

    same-sign branch is a nonzero translation
      => normalized trace is zero

is valid only while the resolvent itself stays in the multiplication algebra.

It is false for the true evolving resolvent.

## Consequence for the connected sector

The connected correction `Phi4=-1/60` cannot be obtained by first discarding `V_sum` through phase symmetry.

The full four-branch state must remain alive until the translation-word / finite-population arithmetic has been evaluated.

The retained-range bounded theorem must therefore control the combined functional

    D1 + D2_diff + D2_sum

on the actual hybrid state.

A proof may show `D2_sum=o(1)` only by a new quantitative theorem valid for that state. It cannot be removed merely by carrier oscillation, adjoint symmetry, or the diagonal sharp-model calculation.

This finite example is a structural falsifier, not an asymptotic zero-density result.
