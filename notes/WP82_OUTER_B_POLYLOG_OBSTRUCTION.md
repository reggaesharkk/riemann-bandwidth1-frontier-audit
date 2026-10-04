# WP82 — a polylog cutoff cannot literally mean the outer prime-power legs

Date: 2026-10-04
Status: **EXCLUSION LEMMA FOR THE TRUNCATION REPAIR**

The undefined truncation variable in the public Lemma-D route cannot safely be repaired by simply declaring it to be `b1`, `b2`, `max(b1,b2)`, or any comparable size of the Stage-A outer prime-power legs.

## Mertens-mass obstruction

The outer prime-power measure used by the fourth-moment bridge has one-leg mass

    M(X)=sum_{n<=X} Lambda(n)/n = log X + O(1).

For any fixed B and

    P=(log X)^B,

Mertens gives

    M(P)=log P+O(1)
        = B log log X + O(1).

Therefore

    boxed:
    M(P)/M(X)
      = B log log X / log X + o(1)
      -> 0.

For two independent outer legs the retained normalized product mass is

    (M(P)/M(X))^2 -> 0.

So a literal restriction

    b1,b2 <= (log X)^B

on the same outer prime-power variables would retain asymptotically **zero**, not `1-o(1)`, of their normalized Mertens mass.

This agrees with our exact continuum-core work: large prime powers collapse to the universal continuum measure and carry leading mass; they are not an absolutely negligible polylog tail.

## Consequence

The mysterious `ell_cell` in the public truncation section, if a valid object exists, must be a different arithmetic parameter whose large values carry an additional `ell_cell^{-k}` decay. It cannot be identified by guesswork with the physical outer legs `b1,b2`.

Likewise, the statement in public Lemma D that its spectral cell has `b1,b2 <= (log X)^B` needs an explicit map from the full moment cell to these truncated spectral moduli. The current source does not display that map.

## Finite diagnostic

`src/wp82_outer_b_polylog_mass.py` prints the retained one-leg and two-leg Mertens mass fractions at several finite X. The theorem-level argument is the standard asymptotic above, not the finite data.

## Repair requirement

A successful repair must introduce a distinct `ell_cell`, prove the claimed decay in that variable, and then derive the logarithmic spectral moduli from it without discarding the leading outer prime-power Mertens measure.
