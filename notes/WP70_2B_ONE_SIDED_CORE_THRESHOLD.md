# WP70-2B — one-sided fourth-moment route: exact 70% threshold

Date: 2026-10-04  
Status: **EXACT REDUCTION; CONTINUUM-CORE CERTIFICATION STILL OPEN**

## A shorter route to 70%

The public 79.62 candidate contains an earlier, logically independent,
one-sided fourth-moment route.  It writes

\[
m_4=\frac{197}{60}+R+o(1)
\]

and currently freezes the conservative upper bound \(R\le0.0066\), producing
about 69.16%.

For \(m_1=1,m_2=4/3,m_3=2\), the exact degree-two moment certificate crosses
70% precisely when

\[
m_4<\frac{59}{18}.
\]

Therefore the exact condition on the difficult class is simply

\[
\boxed{R<-\frac1{180}=-0.005555\ldots}.
\]

This is much weaker than proving the full two-sided identity
\(R\to-1/30\) needed for \(m_4\to13/4\).

## Public continuum-core decomposition

The public one-sided chain uses

\[
R\le C_{\rm core}^{UB}+0.0111+o(1).
\]

Hence 70% follows if

\[
C_{\rm core}^{UB}
<
-\frac1{180}-\frac{111}{10000}
=
\boxed{-\frac{1499}{90000}}
=
-0.016655555\ldots
\]

This is our new certification target.

The source project's numerical continuum estimates are centered near

\[
C_{\rm core}\approx-0.0208\text{ to }-0.0209.
\]

Its script defines

\[
C_{\rm core}^{UB}=C_{\rm core}+B_{\rm total}
\]

and pre-registers only \(B_{\rm total}\le0.0045\).

At the diagnostic center \(-0.0209\), 70% requires the stronger exact budget

\[
\boxed{
B_{\rm total}<\frac{191}{45000}
=0.004244444\ldots
}
\]

so the published pre-registered cap \(0.0045\) is *close but not by itself
sufficient* for 70%.

The worst-case difference is only

\[
0.0045-0.004244444\ldots
=
2.55555\ldots\times10^{-4}.
\]

Thus this is a realistic kill-shot target: tighten the rigorous continuum
quadrature error budget by about \(2.6\times10^{-4}\), or prove the core is
slightly more negative, and the one-sided route alone crosses 70%.

## Why this route is preferable to full Lemma D

To establish 70% we do not need:

- the exact fourth moment \(13/4\);
- the full unrestricted shifted-convolution problem;
- fifth or sixth moments;
- the 79.62 consumption layer.

We need only the one-sided inequality

\[
R<-\frac1{180}.
\]

That isolates the problem to the continuum-core certification and its explicit
error budget.

## Public reproducibility issue

The public reproduction package gives numerical/face scripts for the core and
a \`quadrature_cert.py\` budget, but the paper also invokes archived certified
bridge/glue/consumer-interface lemmas.  Those archive memos are not present in
the public repository under the names cited by the paper.

This is **not a disproof**.  It is a reproducibility blocker: before using the
one-sided chain as our theorem, we must independently reconstruct those
normalization identities or obtain the missing archived derivations.

## Next gate

1. Recompute every component of \(B_{\rm total}\) independently.
2. Replace Richardson/grid heuristics by directed interval or exact rational
   enclosures where possible.
3. Target
   \[
   C_{\rm core}^{UB}<-\frac{1499}{90000}.
   \]
4. Independently reconstruct the bridge from this core quantity to \(R\).

If all four close, we get an unconditional-candidate \(>70\%\) result without
needing the public paper's stronger exact-fourth-moment theorem.
