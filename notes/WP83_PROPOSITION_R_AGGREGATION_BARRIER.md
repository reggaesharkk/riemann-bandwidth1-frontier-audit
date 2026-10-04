# WP83 — aggregation/isolation barrier for Proposition R

Date: 2026-10-04
Status: **ALGEBRAIC NECESSITY OF A GLOBALIZATION LEMMA PROVED**

The successor retraction says a reviewer Proposition R converts finite unconditional higher-even moments into power-law zero-free information. We do not yet possess the archived proof.

Before attempting to reconstruct it, one tempting shortcut must be ruled out.

## 1. A large off-line self-pair is not by itself a lower bound for the full even trace

C26 proves that an off-line pair contributes a hyperbolic signature-(1,1) block under the zero-side pullback, and notes that its self-pair term grows like

    X^(|2 beta-1|).

But C26 also explicitly warns that the zero-side expansion has cancelling cross terms and cannot be bounded termwise.

The algebraic obstruction is absolute. Let

    H1 = [[0,M],[M,0]],
    H2 = [[0,-M],[-M,0]].

Both are real symmetric signature-(1,1) hyperbolic blocks. Individually

    tr(H1^4)=tr(H2^4)=2 M^4.

Yet

    H1+H2=0,

so

    tr((H1+H2)^4)=0.

Thus even arbitrarily large positive individual fourth-power traces can disappear completely after summing indefinite pair blocks.

`src/wp83_hyperbolic_aggregation_falsifier.py` verifies this in exact rational arithmetic.

## 2. Consequence

No proof of Proposition R can use only:

- the existence of a deep off-line zero;
- the size of its individual evaluation/self-pair term;
- the fact that each off-line pair has signature (1,1);
- positivity of the final even spectral power.

A valid proof must use additional structure of the **actual evaluation vectors / frequency localization** to show that the near-extremal pair cannot be cancelled by the aggregate background.

Call that missing statement the **globalization/isolation lemma**.

## 3. Exact reconstruction target

For a zero

    rho=1/2+delta+i gamma

in the active height window, C26 gives evaluation vectors

    u_rho=(phi_hat(gamma_rho-tau_k))_k

with Paley--Wiener growth controlled by `exp(delta L/2)` and a self-pair scale of order `X^(2 delta)` in the second-moment expansion.

To recover Proposition R independently, we need a lower bound of the schematic form

    tr(G_tilde^(2m))
      >= X^(c_m delta) / (log T)^C

or an equivalent operator/eigenvalue bound, **for the full aggregated matrix**, not for an isolated block.

The proof must survive arbitrarily close ordinates, horizontal near-collisions and multiplicities; otherwise it does not justify a global zero-free region.

## 4. Current status

- local off-line growth: SOURCE-CLOSED in C26;
- cancellation of indefinite blocks: EXACT COUNTEREXAMPLE to the naive monotonicity step;
- globalization/isolation for the actual Gabor evaluation family: OPEN;
- successor retraction: says this interface was resolved in the private forward archive, but the proof is not released.

This is now the precise Proposition-R reconstruction gate.
