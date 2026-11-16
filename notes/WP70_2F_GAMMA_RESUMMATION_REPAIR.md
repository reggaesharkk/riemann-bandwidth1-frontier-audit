# WP70-2F — gamma-resummation local-factor repair

Date: 2026-10-04  
Status: **ALGEBRAIC BUG IDENTIFIED; REPAIR UNDER REPLAY**

## Why this matters

The public absolute-value tail helper fired by almost an order of magnitude,
while the public revised gamma-resummation helper produced much smaller global
envelopes.  However its own representative identity checks failed badly for
several modulus pairs.

That means the revised helper cannot yet be consumed as proof-grade evidence.

## Exact local identity

The public code defines

\[
\gamma_d=\sum_e\mu(e)\beta_{de}.
\]

Since \(\beta\) is multiplicative and \(\mu(e)\) restricts each local exponent
of \(e\) to 0 or 1,

\[
\boxed{
\gamma_d
=
\prod_p
\left(
\beta_p(v_p(d))-\beta_p(v_p(d)+1)
\right).
}
\]

This gives a direct way to audit the implementation prime by prime.

## Bug in the public helper

The helper starts from the generic odd-prime product \(C_2\).  For a special
odd prime \(p\mid 2b_1b_2\) that also divides \(d\), it inserts the special
local difference but **does not divide out the generic \(C_2\) factor for that
same prime**.  The prime is therefore double-booked.

There is a second bookkeeping requirement at \(p=2\): \(C_2\) contains only
odd primes, so the \(p=2\) local factor must always be inserted explicitly.
For odd \(b_1,b_2\) and odd \(d\), that factor is zero, which forces

\[
\gamma_d=0.
\]

The public helper does not impose that factor in the fully generic odd case.

These two issues explain the pattern in the public failed identity checks:
\((2,2)\) behaves much better, while pairs containing special odd primes can
show large discrepancies.

## Repair

Use

\[
\gamma_d
=
C_2\,
\gamma_2(v_2(d);v_2(b_1),v_2(b_2))
\prod_{\substack{p>2\\p\mid d b_1 b_2}}
\frac{
\beta_p(v_p(d))-\beta_p(v_p(d)+1)
}{
1-(p-1)^{-2}
}.
\]

This replaces, rather than multiplies on top of, the generic odd-prime local
factor.

## Portfolio-method transfer

This repair follows the same principle that repeatedly mattered in our earlier
finite audits:

- do not collapse signed/local structure before the identity is matched;
- replace global envelopes by exact local factors;
- make every local contribution have a single bookkeeping owner;
- replay the repaired identity independently before consuming the smaller
  bound.

That is methodological transfer only; it does not transfer any theorem from
the other projects into the zeta problem.

## Gate

The companion script compares the old and repaired formulas against both:

1. direct finite Möbius convolution spot checks; and
2. the public full finite-\(j\) kernel at representative modulus pairs.

A smaller global envelope is not enough.  The local identity itself must pass
before the gamma-resummed tail can enter the 70% theorem ledger.
