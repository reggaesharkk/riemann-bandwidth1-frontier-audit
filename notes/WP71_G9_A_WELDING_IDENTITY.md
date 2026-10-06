# WP71 G9-A — exact welding identity

Date: 2026-10-04
Status: ALGEBRAIC REINDEXING CLOSED; analytic remainder still open

Fix b1,b2 and write

    g = gcd(b1,b2),
    r = b1/g,
    q = b2/g.

For a j-cell define

    A(j) = sum_m a_m b_n,
    n = (b2 m + j)/b1,

with the actual interval/support restrictions understood and j nonzero.

Expand

    sum_j A(j)^2.

A term is indexed by (j,m,m') with corresponding n,n'.  Equality of the two
j-values gives

    b1(n-n') = b2(m-m').

After dividing by g,

    r(n-n') = q(m-m').

Since gcd(r,q)=1 there is a unique integer k such that

    n' = n-qk,
    m' = m-rk.

The diagonal is k=0.  Every off-diagonal tuple has k!=0, and conversely every
admissible (k,n,m) reconstructs a unique original tuple with

    j = b1 n - b2 m.

Therefore, exactly,

    sum_j A(j)^2
      = diagonal
        + sum_{k!=0} sum_n b_n b_{n-qk} w_k(n),

where

    w_k(n)
      = sum_m a_m a_{m-rk}

and the m-sum carries simultaneously

- m and m-rk in the original m-window;
- 0 < |b1 n-b2 m| <= J;
- the original support restrictions for n and n-qk.

No asymptotic statement is used.

For the prime application take

    a_m = Lambda(m),
    b_n = Lambda(n).

This is the exact welding object used in G9.

The companion script

    src/wp71_g9_welding_identity.py

checks the identity in pure integer arithmetic on several unrelated finite
families with arbitrary deterministic weights.  The machine check is
corroboration of the written bijection, not a substitute for it.

## What this closes

G9-A: CLOSED.

The hard part is now strictly downstream:

    w_k(n) = M_k(n) + e_k(n),

carry M_k with sign intact, and reduce the weighted e_k contribution to the
published MRT mean-value hypotheses in the exact Stage-A normalization.

That is G9-B/C/D in notes/WP71_MRT_IMPORT_AUDIT.md.
