# WP71 — Stage-A bridge/glue micro-gate ledger

Date: 2026-10-04  
Target: \(\displaystyle N_0^s/N\ge269/378=71.16402116\ldots\%\)  
Status: **ACTIVE; exact normalization isolated, asymptotic zone/glue remainder not yet closed**

## Why this ledger exists

The exact continuum computation \(C_{\rm core}=-1/48\) is only useful if the
prime-side quantity consumed by the fourth-moment ledger reaches that same
normalization without an uncharged leading contribution.

We therefore split the remaining interface into small fail-closed statements.
No numerical agreement is allowed to substitute for an asymptotic estimate.

## Normalization lock

The pinned public implementation \`m1_suite.py\` defines, at \(\lambda=1\),

\[
l=\log(T/2\pi),\qquad X=\lfloor T/2\pi\rfloor,\qquad
\ell_1=l+2\log2-1,
\]

and its explicit \(R\)-unit normalization is

\[
\boxed{
R_{\rm pp}
=
\frac1{\pi\,lX\,\ell_1^4}
\sum_{b_1\le b_2}
\frac{\Lambda(b_1)\Lambda(b_2)}{b_1b_2}
\,T\int
\mathcal G_{b_1,b_2}(\theta)\,
Q_{\rm sym}\,
\theta^{-2}\,d\theta .
}
\]

The exact \(-1/48\) polytope calculation was derived from this same
ordered/unordered \(Q_{\rm sym}\) convention and from the same leading
spectral-mass law.  Hence there is no free multiplicative constant left
between the geometric core and \(R\).

What remains is additive: prove that replacing the actual prime correlations
by the singular-series/continuum model changes this normalized quantity by
\(o(1)\).

## Gate decomposition

### G1 — exact algebraic swap identities — CLOSED

The independent pinned replay of \`t2_swaps.py\` gives the \(A^2\),
\(A\cdot MT\), and \(MT^2\) reorderings to machine roundoff and separately
checks the fixed-window bridge

\[
\sum_{k\ne0}T_W(qk)
=
\sum_{a\bmod q}
\left[
\psi_W(q,a)^2-
\sum_{\substack{n\in W\\n\equiv a(q)}}\Lambda(n)^2
\right].
\]

This gate is finite algebra/identity only.

### G2 — structured shifted-prime \(L^2\) input — DERIVED

From the MRT variance theorem over all shifts, split the structured multiplicity
\(\nu(h)\le\tau(h)\) at \(V=(\log Y)^C\).  On \(\nu\le V\), absorb \(V\)
by requesting a larger logarithmic saving.  On the exceptional set, combine
the divisor second moment with the standard sieve envelope.

This yields, for every \(A\),

\[
\sum_{q\in Q}\sum_{k\le K_q}|E(qk)|^2
\ll_A
HY^2(\log Y)^{-A}.
\]

No factor proportional to the number of moduli is lost.

### G3 — singular-series signed tail — CLOSED IN SHAPE; EXACTIFIED IN UNIVERSAL CLASS

The crude absolute/variation F-E3c route is rejected.

The consumed identity keeps the signed finite contribution and only bounds the
omitted \(\gamma\)-tail.  We independently reconstructed that route and proved
the universal-class coefficient tail beyond \(d=4000\) is \(<2.52\times10^{-4}\).

The general polylog-modulus Rankin argument gives \(o(1)\) after choosing the
coefficient cutoff as a sufficiently high power of \(\log X\).

### G4 — prime-power measure to continuum geometry — DERIVED FROM STANDARD INPUTS

With

\[
\mu_l=\frac1l\sum_{n\le e^l}\frac{\Lambda(n)}n
\delta_{\log n/l},
\]

Mertens/PNT gives uniform distribution-function discrepancy \(O(1/l)\).
Because \(Q_{\rm sym}\) is bounded and piecewise affine on finitely many
rational cells, the product prime-power measure transfers to the exact
polytope integral.  Fixed small primes and diagonal prime-power pairs are
lower order.

### G5 — exact geometric core — CLOSED

\[
\boxed{C_{\rm core}=-1/48}.
\]

No Richardson fit or numerical quadrature is consumed.

### G6 — deterministic finite-law correction — CLOSED AS LOWER ORDER

The public law is

\[
g_{\rm law}=-l^2(\nu-1)-l\widetilde c.
\]

After the exact \(R\)-normalization, the \(\widetilde c\) term is
\(O(1/l)\).  It cannot change the leading \(-1/48\).

### G7 — smoothing collar — OPEN WRITE-OUT

Required statement:

> Replacing the hard geometric window by the smooth Gallagher/Abel window
> changes the normalized \(R\)-quantity by \(o(1)\), uniformly over the
> polylogarithmic modulus family.

The proof must exhibit the collar width, its total prime-power measure and the
largest kernel/overlap weight.  A finite-height face is not accepted as proof.

### G8 — covered-zone error — OPEN WRITE-OUT, STANDARD INPUT AVAILABLE

Use G2 with the exact slow geometric weights.  The needed calculation is a
Cauchy--Schwarz estimate in the **shift variable only**:

\[
\left|\sum_h w_hE(h)\right|
\le
\left(\sum_h|w_h|^2\right)^{1/2}
\left(\sum_h|E(h)|^2\right)^{1/2}.
\]

The remaining task is to bound the first factor in the public \(R\)-units and
show that the arbitrary logarithmic saving in G2 dominates it.

### G9 — middle-band welding weight — OPEN / HIGHEST PRIORITY

For

\[
w_k(n)=\sum_{m\in I(n)}\Lambda(m)\Lambda(m-rk),
\]

write

\[
w_k(n)=M_k(n)+e_k(n)
\]

with \(M_k\) the singular-series main term.  Preserve the signed main term
exactly.  Only \(e_k\) is fed to Cauchy--Schwarz/dispersion.

Required output:

\[
\frac{1}{\pi lX\ell_1^4}
\sum_{k,n}
(\text{slow geometry})\,e_k(n)\,
(\text{outer prime-pair factor})
=o(1).
\]

This is the direct analogue of the signed/remainder decomposition repeatedly
used in our other audit projects: **do not absolute-value the main term.**

### G10 — low-zone remainder — OPEN / FALSIFIER RUNNING

The public finite-height helper quotes a \(0.0163\) cap.  That number cannot
simply be renamed \(o(1)\).

A dedicated scaling workflow now runs the public band/cellmean ledgers at
multiple heights.  Its purpose is not to prove the limit, but to falsify any
claimed vanishing law before we spend time proving it.

If the normalized low-zone quantity fails to decay, Stage A is blocked and the
\(71.164\%\) target is not available from this route.

### G11 — final same-convention assembly — BLOCKED BY G7--G10

Only after the four open gates above may we write

\[
R(1)\le-\frac1{48}+o(1).
\]

Then the exact degree-two consumer gives

\[
\boxed{
\frac{N_0^s}{N}\ge\frac{269}{378}
=0.711640211640\ldots
}
\]

and

\[
\frac{N_d}{N}\ge\frac{647}{756}.
\]

## Parallel higher-rung programme

While G7--G10 are being attacked, the model side is being pushed upward:

- \(C_7=-17/360\) full exact orbit certification is running;
- the public outlook prices a fully pinned \(k=8\) tower near \(0.797\)--\(0.802\);
- a successful C7 exact certificate removes one model-side uncertainty but
  does not replace the missing \(m_7/m_8\) arithmetic transport.

The policy is therefore parallel:

1. close the shortest theorem-grade route first (Stage A);
2. simultaneously certify reusable exact model constants for the higher tower;
3. never let a larger conditional percentage outrank a smaller closed theorem.

## Research-method transfer

We deliberately reuse methodology from the user's broader research programme,
not unrelated mathematical assertions:

- signed main term + interval/remainder;
- local identity before global estimate;
- exact finite object separated from continuum transfer;
- narrow semantic interfaces with fail-closed gates;
- independent replay before freeze.

These principles are portable.  Navier--Stokes/LRSC results themselves are not
inputs to the zeta proof.
