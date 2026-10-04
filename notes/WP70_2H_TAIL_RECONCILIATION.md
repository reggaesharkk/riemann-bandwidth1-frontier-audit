# WP70-2H — tail reconciliation: crude falsifier vs actual E3 route

Date: 2026-10-04  
Status: **DISCREPANCY RECONCILED AT DIAGNOSTIC LEVEL; THEOREM-GRADE TAIL STILL OPEN**

## Forward record

WP70-2E recorded a genuine firing of the public helper
\`scripts/tail_bound.py env\`:

\[
0.98700\quad(T=2400),\qquad
0.95217\quad(T=4800),
\]

against that helper's own \(0.02\) closure threshold.

That observation is retained.  It was not fabricated and should not be
deleted.

What changes is its interpretation.

## The source paper does not consume that crude F-E3c envelope

The paper's actual finite-\(J\) tail lemma is the signed
\(\gamma\)-resummation

\[
\sum_{j\le J}\operatorname{tail}_P(j)\operatorname{row}_j(\theta)
=
\sum_{d\ge1}\gamma_d^{>P}
S_0(d\theta;\lfloor J/d\rfloor),
\]

followed by

\[
|S_0(x;K)|\le C_{\rm saw}=2.10.
\]

Thus the consumed uniform bound is

\[
\left|
\sum_{j\le J}\operatorname{tail}_P(j)\operatorname{row}_j(\theta)
\right|
\le
2.10\sum_d|\gamma_d^{>P}|,
\]

not the much larger Abel/total-variation envelope used by F-E3c.

This is exactly the kind of distinction our own research program treats as
load-bearing: preserving signed/algebraic structure before applying absolute
values can change the budget by orders of magnitude.

## Independent pinned reconstruction

Run \`37183856136\` reconstructed the paper's actual E3 normalization from
the public source at
\`d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8\`.

Using the public finite-\(d\) machinery and its own convergence proxy gave

\[
\varepsilon_{\rm tail}^{\rm E3}(2400)
=
0.01046701265783602,
\]

\[
\varepsilon_{\rm tail}^{\rm E3}(4800)
=
0.010060475988303966.
\]

These lie below the paper's quoted conservative charges

\[
0.0115,\qquad0.0111
\]

in the correct factor-one convention.

Therefore the quoted numbers are no longer a provenance mystery.

## Independent omitted-\(d\) Rankin closure

A second route bounds the uncomputed \(d>D\) part by multiplicativity.

Writing

\[
\gamma_d=\prod_p f_p(v_p(d)),
\qquad
f_p(v)=\beta_p(v)-\beta_p(v+1),
\]

for \(0<\sigma<1\),

\[
\sum_{d>D}|\gamma_d|
\le
D^{-\sigma}
\prod_p
\left(
\sum_{v\ge0}|f_p(v)|p^{\sigma v}
\right).
\]

Run \`37184311986\` used

\[
\sigma=\frac23,\qquad D=10^5,
\]

plus an explicit finite correction for the special-prime class subtraction
in \(\gamma^{\rm free}\).  Its conservative-shape outputs were

\[
\boxed{
\varepsilon_{\rm tail}(2400)
\le 0.01060950134965304
}
\]

and

\[
\boxed{
\varepsilon_{\rm tail}(4800)
\le 0.010211894360575683.
}
\]

Both are below the public charges, with margins approximately

\[
8.90\times10^{-4}
\quad\text{and}\quad
8.88\times10^{-4}.
\]

The worst pairwise omitted \(\ell^1\) tails were also explicitly reported,
including the finite special-prime correction.

## Evidence grade

This is not yet a final proof certificate because the current implementation
still uses floating evaluation for

1. the finite \(d\le10^5\) coefficient sum;
2. the \(\theta\)-quadrature;
3. the finite approximation to the generic Euler product before applying its
   analytic remainder bound.

The *shape* of the omitted-\(d\) proof is conservative, and the observed
margins are substantial enough to justify exactification.

## Corrected interpretation of WP70-2E

The accurate statement is now:

> The public F-E3c absolute/variation falsifier fires badly, but that
> falsifier is not the tail inequality actually consumed by the paper.
> The signed E3/\(\gamma\)-resummed route independently reproduces and,
> with a Rankin-style omitted-\(d\) closure, remains below the quoted
> \(0.0115/0.0111\) charges.  The remaining task is exact/interval
> certification, not discovery of the missing normalization.

So there is currently **no tail-based refutation** of the public one-sided
route.

## Next gate

Exactify the successful route rather than repairing the failed crude one:

- rational local \(\gamma\) factors;
- directed interval Euler product;
- certified tail after the prime cutoff;
- directed interval or exact cellwise integration of the nonnegative geometry.

Only after that should \(0.0115/0.0111\) be promoted from reproduced
finite-height charges to independently certified inputs.
