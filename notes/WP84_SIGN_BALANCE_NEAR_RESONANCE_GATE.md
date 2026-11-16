# WP84 — sign-balance near-resonance barrier

Date: 2026-10-05

Status: **ELEMENTARY NONCLOSED-WORD LEAKAGE BOUND SHARPENED; FIRST GENUINE FINITE-COMPRESSION ARITHMETIC DEBT LOCALIZED TO BALANCED 2-vs-2 WORDS**

This note sharpens the near-resonance statement in
`WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md`.

The key point is that the integer-spacing lower bound is governed by the
**smaller sign population**, not by the total word length.

## 1. Setup

For a sharp translation word built from prime-power shifts write

    Y = log(A/B),

where A and B are positive integers obtained by multiplying the factors whose
translation signs are positive and negative respectively.

Assume every individual prime power retained in the word is at most N.

Let

    r_plus  = number of factors in A,
    r_minus = number of factors in B,

and put

    m = min(r_plus,r_minus).

The finite Fourier-compression trace contains the normalized Dirichlet factor

    D_d(Y/L),

and for a nonclosed word in the small-displacement regime

    |D_d(Y/L)| <= L/(2 d |Y|).

Since d = T L/(2*pi) + O(1), this is O(1/(T|Y|)).

## 2. Smaller-side integer-spacing lemma

Suppose A != B and |log(A/B)| <= 1.

The side with only m factors is at most N^m.  Because the ratio A/B lies in

    [e^(-1), e],

the other side is at most e N^m as well.  Hence

    max(A,B) <= e N^m.

By the mean-value theorem for log,

    |log A - log B|
      = |A-B|/xi

for some xi between A and B.  Since A and B are distinct integers,

    |A-B| >= 1,

and therefore

    boxed:
    |log(A/B)| >= 1/(e N^m).

Thus every such nonclosed word obeys the uniform trace bound

    boxed:
    |tau_d(word)| <= C N^m/T

apart from the already-smaller large-displacement branch.

This uses no prime cancellation and no unproved spacing hypothesis.

## 3. Consequence of adaptive endpoint deletion

The LRSC-derived endpoint quarantine permits

    N/T <= exp(-W+o(1))

with

    W -> infinity,
    W/L -> 0.

For m=1 this gives

    N/T -> 0.

Therefore every nonclosed word for which one sign occurs only once has
uniformly vanishing finite-compression leakage.

This remains true **regardless of the total word degree**.

In particular:

- all degree-1 nonclosed words vanish;
- all degree-2 nonclosed words vanish after exact pair removal;
- all degree-3 nonclosed words vanish;
- at degree 4, every 3-vs-1 sign pattern vanishes.

The first word geometry not killed by this elementary argument is therefore

    boxed:
    2 positive factors versus 2 negative factors.

## 4. First hard sector is balanced degree four

For a 2-vs-2 word,

    A = n1 n2,
    B = n3 n4,

and the spacing lemma gives only

    |log(A/B)| >= c/N^2.

At bandwidth N = T^(1-o(1)) this does not dominate 1/T.

Thus the first genuine finite-compression arithmetic debt is exactly the
near-product-collision window

    boxed:
    |log(n1 n2 / (n3 n4))| <= O(1/T).

Under prime-base grouping, exact equality is already controlled by unique
factorization and gives the known pair sectors.  The unresolved part is the
weighted population of **nonexact** 2-vs-2 near collisions.

This is precisely where the order-four crossing/connected gate first becomes
arithmetically nontrivial.

## 5. General threshold and the k*lambda=2 barrier

If the retained range is

    N = T^(lambda+o(1)),

then a sign sector with smaller population m is automatically suppressed by
integer spacing whenever

    N^m/T -> 0,

equivalently

    boxed:
    m lambda < 1.

For a balanced even word of total degree

    k = 2m,

this becomes

    boxed:
    k lambda < 2.

So the elementary finite-compression spacing threshold is **the same
k*lambda=2 boundary** already identified independently in
`WP83_RS_BARRIER_MATCH.md`.

This gives a direct operator/Dirichlet-kernel explanation for why the
classical diagonal range ends exactly where balanced near-multiplicative
collisions can enter at O(1) scale.

## 6. Consequence for the bounded-resolvent route

The LRSC transfer has now discharged:

- ramp-to-sharp boundary error;
- adaptive endpoint deletion;
- every nonclosed sector with one factor on the smaller sign side.

It does **not** discharge balanced 2-vs-2 near collisions at lambda=1.

Therefore the next arithmetic theorem should be targeted narrowly at the
bounded-resolvent-weighted 2-vs-2 product-collision sector, rather than at a
generic hierarchy of all nonclosed words.

That target is compatible with the Proposition-R firewall because the
consumer remains bounded at fixed nonreal poles; no finite-T raw fourth
moment is being asserted.

No unconditional >79% theorem is claimed.
