# WP84 Decision C — same-section consumer compatibility audit

**Primary result: C2 — CONDITIONAL.** Decision B supplies an existential
boundary-good trimmed interval. It is geometrically of the same asymptotic
size required by the bounded consumers, and bounded-variation spectral
observables are stable under this principal deletion. It does not establish
that the interval also satisfies the source endpoint-score gates, and it does
not transfer an unbounded raw cubic without a uniform sixth Schatten bound.
No conditioned-energy estimate, (m_3=2), or strict (>79\%) conclusion
follows.

Audit base: branch `codex/c5-c6-attack-20261006`, start HEAD
`ccff1757a424f07b96033c3b1b75277ea7e252bd`. The pre-existing untracked
`notebooklm_packet/` was left untouched.

## 1. Actual matrices and consumers

The frozen source operator is the prime-power field from
`WP84_FINITE_SECTION_CUBIC_BOUNDARY_ARITHMETIC.md`:

\[
H_d=s_0 I+V,\quad V=\operatorname{diag}(\beta)+[\operatorname{diag}(A),J],
\]

\[
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
z_n=c_ne^{iT\log n},\quad \alpha_n=\log(n)/L,\quad n=p^v\le N,
\]

with the full natural cutoff (N=\lfloor Xe^{-\sqrt L}\rfloor),
(X=T/(2\pi)), (L=\log X), (d=\lfloor TL/(2\pi)\rfloor),
and all prime powers retained. For a contiguous interval (I\subset I_0),
(P=P_I), (Q=1-P), and (H_I=PHP|_{P\mathcal H}), Decision B proves
for at least one (I=I_{u,v}), (0\le u,v\le M),

\[
M=\lceil d e^{-\sqrt L/2}\rceil,\quad r=u+v\le2M=o(d),
\quad E(I)=\|PHQ\|_{HS}^2=O(\log d),
\]

and the exact boundary identity and bound

\[
\Delta_I=\operatorname{Tr}(PH^3P)-\operatorname{Tr}(H_I^3),\qquad
\frac{|\Delta_I|}{|I|}=O\!\left(\frac{S\log d}{d'}\right)=o(1),
\quad S=\sum_{p^v\le N}|c_{p^v}|=O(\sqrt N/L).
\]

This is an existential interval theorem, not a statement about every
subinterval and not a source-selector identity.

Two distinct downstream objects appear in the source:

* The direct first-strike consumer uses the same selected section and
  centered prime/Weil normalization for lower moments and the signed
  fifth/sixth gate (12) in
  `WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE.md`. Its frozen residual is
  \(\limsup\Re[-A N_5+B N_6]\le J_*-B\,\mathrm{Pair6}_{6000}-\eta\),
  with (A=11501/12500), (B=137641/250000), and signed tolerance
  \(M_{79}=52897896569489/572357731837500000\approx9.24210395475\times10^{-5}\).
  The note explicitly requires the lower-moment and arithmetic gates on the
  **same** selected section. Decision B does not prove this signed gate.
* The conditioned Cayley consumer is the bounded statistic
  \(p(H)=q(U)^*q(U)\), (U=(H+iI)(H-iI)^{-1}), with target
  \(\tau p(H)<21/200=0.105\), as stated in
  `WP84_CONDITIONED_RANK6_79_CONSUMER.md`. The exact moment-only feasibility
  audit shows that the source-certified (m_1=1,m_2=4/3) plus generic
  displacement rank do not imply this target. Decision B proves no new
  estimate of this (p(H)).

The section in Decision B can be used as a bounded-consumer section **if**
the consumer's actual source identification is valid for that same
compression. Its length condition alone does not prove prime-to-Weil
identification or the zero-side block/tail-Weyl transfer.

## 2. What deletion does prove

For Hermitian (H_d) and a principal (d'=d-r) submatrix (H_I),
interlacing gives a spectral-distribution discrepancy bounded by (2r/d)
(a deliberately conservative normalization bound). Thus every real bounded
BV function (f\) satisfies

\[
|\tau_d f(H_d)-\tau_{d'} f(H_I)|
\le 2\,\mathrm{TV}(f)\,r/d.
\]

The conditioned Cayley energy (p(x)=|q((x+i)/(x-i))|^2) is a bounded
rational function with no real poles, finite total variation, and finite
limits at both infinities. Consequently its *deletion error* on the Decision B
trim is (O(\mathrm{TV}(p)e^{-\sqrt L/2})=o(1)). This only transports an
energy bound if one has already proved that bound for the trimmed actual
source matrix. The spectral feasibility counterexample remains untouched;
this stability statement does not provide the missing one-sided energy
estimate.

Likewise the documented first/second prime-moment sampling results are
uniform for contiguous sections with (d'/d\to1), within their recorded
normalization. They are compatible with the Decision B length. Any stronger
endpoint, arithmetic, or zero-side requirement remains a separate gate.

## 3. Endpoint compatibility is conditional, not automatic

Decision B averages the boundary energy over its exact candidate square
\(\mathcal W_T=\{0,\ldots,M\}^2\) and proves
\[
|\mathcal W_T|^{-1}\sum_{(u,v)\in\mathcal W_T}E(I_{u,v})\le C\log d.
\]
The source's other endpoint-score arguments establish good endpoints in
their stated candidate windows and normalization; they do not state that the
consumer-admissible pairs have positive density inside this smaller
\(M\)-window. Mere existence in a larger (r\asymp d/\sqrt L\) window does
not imply existence in Ω's (M\)-window.

There is a precise sufficient compatibility condition. If a set
\(\mathcal G_T\subset\mathcal W_T\) of consumer-admissible endpoint pairs
has density \(|\mathcal G_T|/|\mathcal W_T|\ge\gamma>0\), then nonnegativity
of (E) and the full-square average imply

\[
\min_{(u,v)\in\mathcal G_T}E(I_{u,v})\le(C/\gamma)\log d.
\]
The Decision B proof then gives the same boundary conclusion with constant
multiplied by (1/\gamma). No such lower-density theorem for all required
endpoint gates is recorded. The exact missing input is therefore either
(i) prove those gates are automatic on every Decision B interval, or
(ii) prove a fixed positive lower density of their jointly admissible pairs
inside \(\mathcal W_T\). A source-valid counterexample to this intersection
claim was not found; absence of the density statement is not a
counterexample.

The replay includes a finite abstract endpoint-score array with global
average 1 and a designated singleton consumer set whose sole score is 100.
It falsifies the inference from a global average alone to control on an
arbitrary consumer-selected subset. It is only a logical counterexample to
that inference, not a score array realized by the prime source.

## 4. Raw cubic deletion: exact sufficient estimate and failure without it

Let (Z=H_I\oplus0_r\) in dimension (d). Then
\(\operatorname{rank}(H-Z)\le2r\). If the actual source additionally
satisfies a uniform normalized sixth Schatten bound
\(\|H\|_{6,d}=(\tau_d|H|^6)^{1/6}\le C_6\), normalized
Schatten-Hölder and rank interpolation give

\[
|\tau_d(H^3)-\tau_{d'}(H_I^3)|
\le 6C_6^3\sqrt{2r/d}
 + C_6^3(r/d)(d/d')^{1/2}.
\]

The first term follows by telescoping (H^3-Z^3), using
\(\|H-Z\|_{3/2,d}\le(2r/d)^{1/2}\|H-Z\|_{6,d}\) and
\(\|H-Z\|_{6,d}\le2C_6\); the final term is the difference between
zero-padded dimension-(d) and dimension-(d') normalizations; the factor
\((d/d')^{1/2}\) is the normalized Schatten scaling for the principal
compression. With
Decision B's (r/d=O(e^{-\sqrt L/2})), this would be
\(O(C_6^3e^{-\sqrt L/4})\). It is a sufficient estimate, not an available
source theorem.

The existing source input gives (m_1,m_2), the local prime-field
large-sieve bound, and a global operator bound growing like (S=O(\sqrt
N/L)). None supplies a uniform (C_6) for the actual sharp (H_d).
Interpolation from (m_2) and a growing operator norm is not enough. The
finite Decision B boundary identity controls
\(\operatorname{Tr}(PH^3P)-\operatorname{Tr}(H_I^3)\) on its selected
interval; it does not bound the contribution of the deleted rows to
\(\operatorname{Tr}(H^3)\).

The obstruction to inferring raw cubic stability from rank deletion alone is
exact. For
\(Y_d=\operatorname{diag}(d^{1/3},0,\ldots,0)\), delete its first row:
\(r/d=1/d\to0\), but
\(\tau_d(Y_d^3)=1\) and the compressed cubic is zero. This family has
\(\tau_d|Y_d|^6=d\), so it violates precisely the missing uniform
integrability condition. It is an abstract matrix falsifier, not a
prime-source example.

## 5. Margin and verdict

No positive consumer margin is consumed by the bounded-variation deletion
itself: its error tends to zero. But no numerical saving toward (0.105) is
earned, because the required actual-source upper bound on the trimmed
\(\tau p(H_I)\) is absent. The moment-only witness has energy
\(48861622601/195312500000\approx0.2501715077>0.105\), a gap
\(28353810101/195312500000\approx0.1451715077\); Decision B does not remove
that witness from the certified first-two-moment class.

For the first-strike route, its exact (M_{79}) allowance remains as above;
the signed high-product theorem and same-section endpoint gates remain
unproved. The cubic boundary (o(1)) is a distinct payment and cannot be
counted as a signed fifth/sixth saving.

**Classification: C2 — CONDITIONAL.** The bounded Cayley energy transfers
across the trim with the stated BV error, conditional on proving it on that
same actual-source trim and on the inherited prime-to-Weil/zero-side
identification. To combine Decision B with consumer endpoint constraints,
one needs the positive-density intersection condition in Section 3 (or an
automatic-gate proof). To transfer a raw cubic from the full original
interval, one needs the actual-source uniform sixth Schatten bound above.
Neither is certified here. Strict (>79\%\) remains OPEN.

## Reproduction

```powershell
python src/wp84_decision_c_same_section_compatibility.py
python src/wp84_decision_c_same_section_compatibility_replay.py
```

The producer and independent replay check exact rational consumer margins,
the deletion scale, the positive-density averaging implication, and the
raw-cubic spike. Prerequisite replays are listed in the certificate.
