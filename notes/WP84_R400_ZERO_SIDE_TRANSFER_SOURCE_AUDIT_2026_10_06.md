# WP84 — R=400 zero-side source and normalization audit (2026-10-06)

Status: **PUBLISHED ZERO-SIDE TRANSFER VERIFIED; PROJECT GRAM NORMALIZATION CORRECTED; PRIME-SIDE R=400 ESTIMATE REMAINS CONDITIONAL**

Audit basis: PR #5, branch `research/frontier-7962-hostile-audit-v0.1`, source head `a295c0fc5daa1b847b9feb89c354c3bee6a626e3`.

## 1. Correction to the prior audit

The previous version of this note said the audited sources did not supply the
zero-side block and tail-Weyl arguments. That conclusion was too broad.
Alpöge–Furman, arXiv:2608.13637v2, Sections 3–4, proves these ingredients for
the finite Weil/Gabor matrix used as the project’s zero-side model.

The source is available at
https://arxiv.org/html/2608.13637v2.

## 2. Zero-side statements established in the source

In the paper’s notation, Propositions 4.1–4.3 establish:

- the on-line contribution (P\succeq0), with
  (operatorname{rank}P\le N_0^*(I')) and
  (operatorname{tr}P\le N_0(I'));
- each off-line reflection pair is a pullback of
  (operatorname{diag}(1,-1)), so
  (n_+(Q)\le \#\mathrm{off}/2);
- the omitted zero tail satisfies
  (|\widetilde E\|_1\ll_\chi T^{-1/2}), hence its operator norm is
  (o(1)).

The pair statement follows from writing a zero vector as (v=x+iy):
the pair contributes (2m(xx^{\mathsf T}-yy^{\mathsf T})), a pullback of a
form with one positive and one negative direction. Positive-index
subadditivity then gives
[
n_+(\widetilde G)\le N_0^*(I')+\#\mathrm{off}/2
=s_1+s_2+p.
]
The multiplicity count (N(I')\ge s_1+2s_2+2p) follows directly from the
definitions. Proposition 4.5 transfers the enlarged zero interval (I') to
the target interval (I) with (O(\sqrt T\log T)) endpoint error, and
Lemma 3.4 gives the stated tail-Weyl comparison.

Thus the integer implication
[
s_1\ge2n_+(\widetilde G)-N(I')
]
has the required source-side ingredients for this matrix construction. The
companion script checks only this final integer implication; the analytic
source is the paper above.

## 3. Exact normalization correction

The paper defines
[
\widetilde G_{kl}
=\frac{1}{a_\phi L^2}
\int \widehat\phi(\tau-\tau_k)
\widehat\phi(\tau-\tau_l)\nu_X(\tau)\,d\tau,
\qquad a_\phi=\|\phi\|_2^2/L.
]

Therefore, in the project’s representation
(\widetilde G=\int v(\tau)v(\tau)^{\mathsf T}\nu_X(\tau)d\tau), the
feature must be
[
v_k(\tau)=\frac{\widehat\phi(\tau-\tau_k)}
{\sqrt{a_\phi}\,L}.
]
The earlier (L^{-1/2}\widehat\phi) definition made the represented matrix
larger by the factor (a_\phi L). The corresponding prime-block overlap
coefficient was off by the same factor.

Both formulas are corrected in
`notes/WP84_BOUNDED_RESOLVENT_CONSUMER.md`:
[
C(y)_{kl}=\frac{2\pi}{a_\phi L^2}
A_{k-l}(y)\cos\!\left(\frac{\tau_k+\tau_l}{2}y\right).
]
This is the normalization in the prime-side Gram blocks as well as the
zero-side Weil matrix.

## 4. What this does and does not close

The cited paper supplies the zero-side block, multiplicity, interval, and
tail-Weyl arguments for its exact Weil/Gabor matrix. The R=400 construction
uses the same bounded full matrix before its band comparison and endpoint
section are applied. The principal-section deletion is on the prime-side
polynomial calculation; the zero-side count remains attached to the full
matrix.

The correction closes the explicit feature normalization in the bounded
consumer note. The R=400 percentage is still conditional on the prime-side
full-to-band constant, fixed-(R) covariance substitution, complete
degree-four word estimates, and their common normalization. The previously
recorded endpoint scale calculation is consistent, but it does not prove
those separate analytic inputs.

The R=400 notes give the conditional defect
`D <= 0.15589863406625 + o(1)`, which algebraically yields
`1-2D >= 0.6882027318675 - o(1)`. This is not an unconditional
simple-zero bound until the prime-side estimates are established in the
corrected matrix normalization.

No unconditional R=400 or >79% theorem is claimed here.
