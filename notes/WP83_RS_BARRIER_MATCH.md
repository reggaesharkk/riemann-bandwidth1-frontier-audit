# WP83 — exact match between Proposition R and the Rudnick–Sarnak range

Date: 2026-10-04
Status: **STRUCTURAL BARRIER IDENTITY DERIVED**

The Proposition-R exponent and the classical higher-moment range meet at exactly the same threshold.

## 1. Moment-order notation

Let the even trace moment have order

    k = 2m.

Take bandwidth

    X = T^(lambda+o(1)).

Conditional on the missing Proposition-R globalization lemma, a finite normalized k-th moment upper bound gives

    |beta-1/2| <= 1/(k*lambda) + o(1).

This is the same exponent previously written as 1/(2m lambda).

## 2. When does this say anything beyond the trivial critical strip?

Every nontrivial zero already satisfies

    |beta-1/2| < 1/2.

So the moment consequence is genuinely stronger than the trivial strip exactly when

    1/(k*lambda) < 1/2,

equivalently

    boxed: k*lambda > 2.

At the boundary k*lambda=2 the inferred strip is only the original critical strip.

## 3. C26's classical prime-side range

C26 Section 7.5 states that the diagonal evaluation of the prime-side k-th trace moment is available in the Rudnick–Sarnak range

    boxed: k*lambda < 2.

For lambda in (1/2,1), this permits at most k=3; C26 explicitly remarks that the odd third moment does not improve the positive-index bound.

Thus the classical unconditional moment technology stops **exactly before** the point where a finite even moment bound would begin to imply a nontrivial zero-free strip.

## 4. Barrier match

The two conditions are complementary:

    classical diagonal moment range:      k*lambda < 2,
    nontrivial Proposition-R consequence: k*lambda > 2.

The threshold is the same number 2.

This explains why the successor higher-even-moment program was qualitatively harder than a long bookkeeping extension. Crossing its claimed fourth-moment tier at lambda=1 means moving from k*lambda=4, far beyond the classical boundary, into a regime where the moment bound itself carries zero-free information.

## 5. Concrete examples

- k=4, lambda=1: delta<=1/4; fixed strip [1/4,3/4].
- k=4, lambda=3/4: delta<=1/3; fixed strip [1/6,5/6].
- k=4, lambda=1/2: delta<=1/2; no improvement over the trivial strip.
- k=6, lambda=1: delta<=1/6; strip [1/3,2/3].
- k=8, lambda=1: delta<=1/8; strip [3/8,5/8].

## 6. Strategic consequence

A proof of the higher-even-moment transport for k*lambda>2 using only the declared classical inputs should be treated as suspect until it explains where the corresponding zero-free strength enters.

This does not invalidate exact model constants or consumer certificates. It identifies the missing analytic power they would need to become unconditional zeta theorems.

For the >79% program, the exact k<=8 model work remains useful, but an unconditional analytic bridge must now be evaluated against this k*lambda=2 barrier at every rung.
