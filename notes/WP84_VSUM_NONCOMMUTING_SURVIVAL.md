# WP84 — V-sum does not vanish for a noncommuting intermediate state

Date: 2026-10-05

Status: **EXACT FINITE-SECTION FALSIFIER OF AUTOMATIC V-SUM CANCELLATION**

The sharp multiplication model makes the same-sign variance branches vanish
because two equal-direction shifts have no diagonal kernel after sandwiching
by a multiplication operator.

That conclusion does **not** survive an arbitrary noncommuting intermediate
state.

## 1. Exact lattice witness

Let S_r be the N by N non-cyclic shift and choose

    A = I + S_1 + S_1^*.

This is a simple symmetric Toeplitz state with one off-diagonal band.

At r=1, exact integer matrix multiplication gives

    Tr[
      A S_1 A S_1 A
      + A S_1^* A S_1^* A
    ]
      = 6N-8,

whereas the mixed branch is

    Tr[
      A S_1 A S_1^* A
      + A S_1^* A S_1 A
    ]
      = 14N-24.

Therefore

    boxed:
    normalized V-sum -> 6,
    normalized V-diff -> 14.

The same-sign contribution is not merely nonzero; it remains macroscopic.

Companion exact checker:

    src/wp84_vsum_noncommuting_survival.py

## 2. Consequence

No proof may remove V-sum solely because the elementary block is a nonzero
translation.

V-sum vanishes only after proving enough structure about the intermediate
state.

This independently confirms the order-four warning:

    multiplication-algebra closure
      -> V-sum disappears,
      -> crossing/connected sectors are lost,
      -> wrong fourth-order calibration.

## 3. Relation to the connected -1/60 sector

This witness does not identify Phi4=-1/60.

It proves something narrower and important:

    the exact first/second-order flow has an O(1) same-sign channel available
    to carry noncommutative state memory.

So the remaining provenance theorem should evaluate V-sum and V-diff together
on the actual permutation-averaged retained-range state rather than trying to
kill V-sum first.

## 4. Updated branch strategy

The retained-range theorem should be organized around the full four-branch
functional

    V_full(A)
      = V_diff(A)+V_sum(A),

with only the endpoint layer and cubic single-block remainder quarantined.

The target is not

    prove V_sum=o(1),

but rather

    identify the combined bounded trace functional and verify that its
    order-four expansion reproduces

        2*t_adj+t_opp+Phi4 = 1/4.

Only after that calibration may any asymptotic cancellation be promoted.

No unconditional >79 theorem is claimed.
