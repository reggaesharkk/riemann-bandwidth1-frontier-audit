# WP70-2G — asymptotic tail escape and the exact payoff ladder

Date: 2026-10-04  
Status: **THEOREM-SHAPED REDUCTION; ANALYTIC BRIDGE STILL OPEN**

## Why the fixed \(0.0111\) charge is not the final target

The public one-sided route freezes the singular-series cutoff at \(P=40\) for
its finite-height certification pass.  That is useful for a numerical
certificate, but it is not the natural asymptotic choice.

The same public source states the mean-square singular-series truncation

\[
\sum_{|j|\le H}
\left|\mathfrak S(j)-\mathfrak S^{(P)}(j)\right|^2
\ll
H(\log X)^{-B+O(1)},
\qquad
P=(\log X)^B,
\]

uniformly for the logarithmic-modulus range consumed by the proof.

The row kernel satisfies

\[
\sum_{j\le H}|\operatorname{row}_j(\theta)|^2
\ll \theta,
\]

and in the relevant zone \(H\asymp \theta^{-1}\).  Therefore a single
Cauchy--Schwarz in the **shift variable** gives

\[
\left|
\sum_{j\le H}
(\mathfrak S-\mathfrak S^{(P)})(j)
\,\operatorname{row}_j(\theta)
\right|
\ll
(\log X)^{-B/2+O(1)}
\]

uniformly in the scaled zone.  The factor \(H^{1/2}\) from the singular-series
tail cancels the factor \(\theta^{1/2}\) from the row norm.

Because the remaining consumed modulus families are only polylogarithmic, an
arbitrarily large fixed \(B\) can absorb those losses.  Thus the correct
asymptotic target is

\[
\boxed{\varepsilon_{\rm tail}(T)=o(1)}
\]

rather than a permanent \(+0.0111\) penalty, **provided the public
truncation/bridge normalization is independently reconstructed exactly in this
convention**.

This is also consistent with the program's own forward-recorded rule that
finite-height envelopes are not to be transported blindly to limits.

## Exact consequence of our continuum geometry

Our independent rational-polytope audit established

\[
C_{\rm core}=-\frac1{48}.
\]

If the bridge/glue reduction is valid and all singular-series, band, collar and
finite-height errors are shown to be \(o(1)\), then

\[
\limsup R(1)\le-\frac1{48}.
\]

The degree-two Christoffel consumer then has

\[
\Delta=R+\frac1{30}
=
\frac1{80},
\]

\[
\Lambda_2(0)
=
\frac{5/108+\Delta/3}{1/3+4\Delta/3}
=
\frac{109}{756}.
\]

Hence the exact asymptotic payoff is

\[
\boxed{
\liminf\frac{N_0^s}{N}
\ge
1-2\frac{109}{756}
=
\frac{269}{378}
=
0.711640211640\ldots
}
\]

and

\[
\boxed{
\liminf\frac{N_d}{N}
\ge
\frac{647}{756}
=
0.855820105820\ldots
}
\]

This is **71.1640%**, not 70.3054%.  The difference is precisely that the
finite \(P=40\) tail charge is replaced by a genuine asymptotic \(o(1)\)
argument.

## Natural ladder beyond this

### Stage A — exact continuum core + vanishing analytic errors

\[
\boxed{269/378=71.1640\%}
\]

Load-bearing work: independent tail/truncation, bridge/glue, and continuum
transfer.

### Stage B — exact fourth moment

If the stronger Lemma-D route establishes

\[
m_4=\frac{13}{4},
\qquad
R=-\frac1{30},
\]

then

\[
\boxed{
\frac{N_0^s}{N}\ge\frac{13}{18}=72.2222\%
}
\]

and

\[
\boxed{
\frac{N_d}{N}\ge\frac{31}{36}=86.1111\%.
}
\]

This is the next analytic target after Stage A.

### Stage C — exact moments through six

For

\[
(m_1,\ldots,m_6)
=
\left(
1,\frac43,2,\frac{13}{4},\frac{101}{18},
\frac{12809}{1260}
\right),
\]

our independent exact degree-three consumer gives

\[
\boxed{
\frac{N_0^s}{N}
\ge
\frac{11061}{13891}
=
79.6270966813\ldots\%.
}
\]

This is still conditional on independently proving the imported higher-moment
analytic premises.

## How our existing research helps

No Navier--Stokes or LRSC theorem is imported into analytic number theory.

What *does* transfer is the certification architecture already developed in
the portfolio:

1. separate semantic identities from numerical bounds;
2. preserve signed/cancellation structure before applying absolute envelopes;
3. convert continuum geometry to exact rational polytopes whenever possible;
4. use independent generator/verifier paths;
5. use dyadic/branch-and-bound only after the analytic interface is frozen;
6. treat any fired falsifier as information, not as something to hide;
7. freeze each rung before climbing to the next.

The fixed-\(P\) tail discrepancy is an example: the crude absolute F-E3c
envelope fires, while the signed \(\gamma\)-resummation and the actual
sawtooth lemma are much tighter.  The correct next move is to certify the
signed structure, not to enlarge the crude absolute budget.

## Kill gates before a public 71.16% claim

We still require a complete written proof that:

1. the singular-series tail with \(P=(\log X)^B\) is \(o(1)\) after the exact
   consumer normalization;
2. the high-modulus cells discarded by the reduction are \(o(1)\), not merely
   small in a finite-height face;
3. the bridge and glue identities feed the same \(R\)-normalization used by
   the exact \(-1/48\) calculation;
4. the Mertens scaling/universality passage to the rational-polytope integral
   is justified with dominated convergence or an equivalent explicit
   truncation argument;
5. all remaining covered-zone, collar and low-zone terms are \(o(1)\).

Until those are closed, \(269/378\) is a theorem target, not a theorem claim.
