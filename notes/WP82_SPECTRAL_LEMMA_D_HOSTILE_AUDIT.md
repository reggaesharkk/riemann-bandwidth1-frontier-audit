# WP82 — hostile audit of the public spectral Lemma-D route

Date: 2026-10-04
Status: **ALTERNATE ROUTE AUDITED; it does NOT currently bypass the G9 glue obligation**

The public candidate contains a potentially shorter route to the fourth, fifth and sixth moments: truncate to polylogarithmic moduli, convert the lock-variance to a spectral frame, and close major/minor frequency leaves with classical prime-sum estimates.

Because a theorem-grade m4/m5/m6 chain would immediately feed the exact 79.627% consumer, this route is worth auditing independently.

The conclusion is important: the spectral route is promising, but in its present write-out it explicitly imports the same bridge/glue normalization from Section fm:R. Therefore it is **not an independent escape from G9**. Either G9 must close, or the spectral proof must be rederived with a new self-contained consumer interface.

## S0 — finite algebraic frame

For a b-cycle, if two chains have the same lock vector then they differ by one common translation t. Therefore

    sum_j N_f(j) N_g(j) = sum_t product_i C_i(t),
    C_i(t)=sum_x f_i(x) g_i(x+t).

This is a finite Fubini/bijection identity. At b=4, finite Fourier orthogonality and Parseval give the spectral L2 identity. The public face_parseval.py is numerical corroboration, not the proof.

**Grade S0: CLOSED IN MATHEMATICS.**

## S1 — polylogarithmic cell truncation

The candidate claims cells beyond P=(log X)^B have two-sided consumed tail of size Y^2(log Y)^c P^{-(k-2)+epsilon}. The exponent bookkeeping is plausible, but the cell-mass normalization is compressed into a paragraph and should be independently expanded.

**Grade S1: RECONSTRUCTABLE, NOT YET INDEPENDENTLY CLOSED HERE.**

## S2 — local coincidence law and model comb locals

The local formula N(j)=P0*(p-D(j))/p follows directly because each affine position excludes one residue of the base variable, with duplicates counted only once. The mean-one law follows from uniform independent lock increments.

**Grade S2: STRONG / INDEPENDENTLY RECONSTRUCTABLE.**

## S3 — all-major spectral bins

For logarithmic denominators, the paper invokes Siegel--Walfisz on windowed single-prime exponential sums plus partial summation. This is a standard classical input in the stated logarithmic-modulus range. Constants are ineffective and must remain graded that way. The public face_sw.py is a finite-height diagnostic, not proof.

**Grade S3: STANDARD INPUT, WRITE-OUT CHECK NEEDED.**

## S4 — mixed and minor spectral bins

This is the most vulnerable spectral leaf. The paper says Vaughan gives a pointwise minor-arc saving and that well-spacing plus a hybrid large-sieve/minor-supremum budget converts it into the required spectral L2 bound.

However face_arcs.py does not prove this asymptotically. Its second half assembles a finite-height budget against measured mixed spectral mass and accepts a <=100x tightness ratio. That is a falsifier/diagnostic, not a theorem.

The proof still needs an explicit uniform sum over all major-image strata, including arc widths, arm count and spacing, the large-sieve inequality, minor supremum, all powers of Y,N,b1,b2,P*, and the final logarithmic exponent.

**Grade S4: OPEN WRITE-OUT / HIGH PRIORITY if pursuing this route.**

## S5 — spectral comb equals the singular-series model

The CRT support statement is exact: t=0 mod b2 and t=tau mod b1. The local factors should match the coincidence-counting law prime by prime. But face_dispersion.py only measures finite-height profile tracking. It cannot replace exact CRT/local-factor algebra or the singular-series truncation tail.

**Grade S5: EXACT CORE + ANALYTIC TAIL; INDEPENDENT WRITE-OUT NEEDED.**

## S6 — critical dependency: bridge/glue normalization

The candidate proof of truncated Lemma D explicitly states that the (k,j)-aggregation constants of the bridge and glue layer are archived/certified and that the normalization match to K J V^2 is the consumer interface there.

That layer is Section fm:R — precisely the area whose middle-band welding claim we are rebuilding as G9.

Therefore the public spectral Lemma-D route is **not currently an independent bypass of G9**.

**Grade S6: BLOCKED BY THE SAME GLUE INTERFACE.**

## S7 — higher-cycle transport

The finite product identity extends to every cycle length. What does not follow automatically is that every analytic major/minor/comb bound remains uniform with the stronger cycle bookkeeping. The public phrase 'applies verbatim' must be expanded into per-factor arc classification, a k-factor size budget, higher-dimensional comb, consumed truncation exponent, and exact normalization to m5/m6. W1/W3 finite faces are diagnostics, not analytic proofs.

**Grade S7: OPEN UNTIL S4--S6 ARE CLOSED UNIFORMLY.**

## Strategic conclusion

Two routes remain:

1. **Route A — finish G9 directly.** Close the moving-endpoint MRT estimate and exact R-unit normalization. This also repairs the dependency imported by the public spectral proof.
2. **Route B — rebuild the spectral consumer interface from scratch.** Avoid Section fm:R by deriving a new exact identity from the spectral L2 object directly to the consumed moment-cell normalization.

Route B could in principle bypass G9, but that new identity has not yet been written. Until it exists, Route A is shorter.

Therefore **G9 remains the current fastest theorem-grade bottleneck**.

In parallel, exact {5,2}/C7 computations remain useful because they feed the post-79 model side without depending on how the analytic transport is ultimately closed.

## S5 update — local coupling closed

The local arithmetic portion of the comb identification has now been strengthened independently:

- the pointwise p-local four-point factor K4_p(k,j) is explicit;
- its j-marginal is exactly the product of the two twin local factors;
- its k-marginal is exactly the squared two-point lock factor with the common-density normalization;
- finite-prime Euler products assemble by CRT with no inter-prime constraint.

This removes the ambiguity about hidden pointwise j-k congruences. They exist, but are exactly the local four-point coincidence loci and are already inside K4_p.

What remains in S5 is the analytic/spectral identification of the truncated Euler object with the MM frequency comb in the exact window convention, plus the singular-series tail. Therefore S5 is upgraded from 'exact core not written' to **LOCAL/FINITE-EULER CORE CLOSED; SPECTRAL IDENTIFICATION + TAIL OPEN**.
