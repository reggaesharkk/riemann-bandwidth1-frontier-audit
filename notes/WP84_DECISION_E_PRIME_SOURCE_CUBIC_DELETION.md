# WP84 Decision E — prime-source cubic deletion stability

**Classification: E3 — conditional theorem; the source-specific deleted-block cubic estimate is missing.** The Decision B/D2 endpoint is boundary-good and consumer-admissible for the direct first-strike consumer, but the boundary estimate does not control the cubic trace carried by the deleted rows. No prime-source counterexample or uniform sixth Schatten bound is established.

## 1. Starting state and source matrix

Audit base: branch `codex/c5-c6-attack-20261006`, start commit
`aba8d321270332829d5c8f21fc6c111f449081a1`. The only pre-existing
untracked path is `notebooklm_packet/`; it is preserved.

The exact finite prime-source matrix is specified in
`WP84_INFINITE_NO_WRAP_CUBIC_AUDIT.md` and
`WP84_FINITE_SECTION_CUBIC_BOUNDARY_ARITHMETIC.md`. Put
\(X=T/(2\pi), L=\log X, N=\lfloor Xe^{-\sqrt L}\rfloor\),
\(d=\lfloor TL/(2\pi)\rfloor\), and
\(\tau_k=T+2\pi k/L\), for the original consecutive (d)-point index
set. Every prime power (n=p^v\le N) occurs, with
\[
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
z_n=c_ne^{iT\log n},\quad \alpha_n=\frac{\log n}{L},\quad
w_n(k)=z_ne^{2\pi i k\alpha_n}.
\]
Its real fields are
\[
A_k=\sum_n\Im w_n(k),\qquad
\beta_k=\sum_n2(1-\alpha_n)\Re w_n(k),
\]
and, with (J_{ij}=1/(\pi(j-i))) for (i\ne j), (J_{ii}=0),
\[
H=s_0(T)I+V,\qquad V=\operatorname{diag}(\beta)+[\operatorname{diag}(A),J].
\]
Thus (v_{ij}=\delta_{ij}\beta_i+(1-\delta_{ij})(A_i-A_j)/(\pi(j-i))).
The commutator is Hermitian since (J^*=-J). The exact infinite-lattice
Fourier multiplier is (j(x)=i(1-2x)) on (0<x<1), with the symmetric
half-value convention at its jump. Each prime-power summand is the partial
translation (z_nS^+_{\alpha_n}+\bar z_nS^-_{\alpha_n}); paths do not wrap.
The natural cutoff gives (0<\alpha_n\le1-1/\sqrt L+o(L^{-1/2})).
The no-wrap identity is exact at fixed (T,N), but its Cesàro limit is not
uniform in the growing natural prime pool and does not control the deleted
finite rows.

Known source bounds include (a_\phi(T)\to1), (s_0(T)\to1),
\(S=\sum_{p^v\le N}|c_{p^v}|=O(\sqrt N/L)\) with powers retained, and
\(\|V\|_{op}\le4S\). The fixed-section local large-sieve/endpoint theorem
and Decision D2 give a direct-consumer-admissible section (I) with
\(r=d-d'=u+v\le2M=o(d)),
\[
M=\lceil d e^{-\sqrt L/2}\rceil,\quad r/d=O(e^{-\sqrt L/2}),\quad
E=\|PHQ\|_{HS}^2=O(\log d),
\]
where (P=P_I,Q=1-P). The D2 density is at least (1/4) under the
Decision B pair weights; it is already used in this selected section.

## 2. Exact deletion identity and the boundary term already paid

Write (A=PHP|_{P}, B=PHQ:Q\to P, D=QHQ|_Q), so (C=QHP=B^*).
Block multiplication and cyclicity give the exact full-trace identity
\[
\operatorname{Tr}H^3-\operatorname{Tr}A^3
=\operatorname{Tr}D^3
+3\operatorname{Tr}_{P}(A BB^*)
+3\operatorname{Tr}_{Q}(D B^*B).                         \tag{1}
\]
The two mixed terms are not assumed positive. Since
\(\|A\|_{op},\|D\|_{op}\le |s_0|+4S=:K_T\), the actual same-section
crossing-energy bound implies
\[
\left|3\operatorname{Tr}_{P}(A BB^*)
+3\operatorname{Tr}_{Q}(D B^*B)\right|
\le 6K_TE=O((1+S)\log d).                               \tag{2}
\]
After division by (d\asymp TL),
\[
\frac{(1+S)\log d}{d}
=O\!\left(T^{-1}
+\frac{e^{-\sqrt L/2}}{\sqrt{2\pi T}\,L}\right)=o(1). \tag{3}
\]
The exact decision-B boundary identity instead compares
\(\operatorname{Tr}(PH^3P)) with \(\operatorname{Tr}(A^3)\). It also has
an (O(K_TE)) error. Neither identity bounds \(\operatorname{Tr}D^3\):
the deleted (Q)-block cubic is a separate term in (1). This is the key
distinction between compression-of-the-cubic and cubic-of-the-compression.

Normalization is exact as well:
\[
\tau_d(H^3)-\tau_{d'}(A^3)
=\frac{\operatorname{Tr}D^3}{d}
+\frac{3\operatorname{Tr}_{P}(A BB^*)+3\operatorname{Tr}_{Q}(D B^*B)}d
-\frac rd\,\tau_{d'}(A^3).                              \tag{4}
\]
By (3)--(4), the single exact remaining signed condition is
\[
\frac{1}{d}\operatorname{Tr}(D^3)
-\frac rd\,\tau_{d'}(A^3)=o(1).                        \tag{5}
\]
No cancellation between these terms is presumed. A transparent stronger
sufficient pair is \(d^{-1}|\operatorname{Tr}(D^3)|\to0\) and
\((r/d)|\tau_{d'}(A^3)|\to0\); bounded \(\tau_{d'}(A^3)\) reduces
that pair to the deleted-block estimate alone. The stronger source-specific
condition \(d^{-1}\|D\|_{S_3}^3\to0\) implies its first condition. None
of these deleted-block cubic bounds is in the checked-in source gates.

There is a source-specific but insufficient boundary-localized estimate
available from the existing local large sieve. The deleted coordinates
form two intervals of length at most (M). Uniformly on either interval,
the weighted version of the same prime-power sieve gives
\[
\sum_{k\in Q}|A_k|^2+\sum_{k\in Q}|\beta_k|^2=O(M+NL).
\]
Indeed the coefficients for (A) are (c_n), and those for (beta)
are (2(1-\alpha_n)c_n), whose square mass is at most four times the
original; the sieve spacing is at least (1/((N+1)L)). Writing
\(W=QVQ|_Q\), compression of (J) and
\(\|[\operatorname{diag}(A_Q),J_Q]\|_{HS}\le2\|A_Q\|_2\)
then imply
\[
\|W\|_{HS}^2=O(M+NL),\qquad \|W\|_{op}\le4S.
\]
Since (D=s_0Q+W), exact scalar expansion and trace inequalities yield
\[
\frac{|\operatorname{Tr}D^3|}{d}
=O\!\left(\frac rd+\frac{\sqrt{r(M+NL)}}d
+\frac{M+NL}{d}+\frac{S(M+NL)}d\right).
\]
For (M\gg NL), (r\le2M), this is
\[
O\!\left(\frac Md+\frac{SM}{d}\right),\qquad
\frac{SM}{d}=O\!\left(\frac{\sqrt T e^{-\sqrt L}}{L}\right).
\]
The first part vanishes, but the available upper majorant for the second
grows (its logarithm is \(L/2-\sqrt L-O(\log L)\)). This is a sharper
source-localized Hilbert--Schmidt estimate than applying only the global
operator bound to every deleted row, but it still does not prove
\(\operatorname{Tr}D^3=o(d)\). A growing upper bound is not a lower bound
or a prime-source counterexample.

## 3. What a uniform sixth moment would prove; weaker alternatives

The already audited rank/Schatten argument is valid: if the *actual*
prime-source matrices obey
\(\sup_T\tau_d(|H|^6)\le C_6^6\), zero-padding (A) to dimension (d)
and using rank at most (2r) gives
\[
|\tau_d(H^3)-\tau_{d'}(A^3)|
\le6C_6^3\sqrt{2r/d}
+C_6^3(r/d)(d/d')^{1/2}=o(1).                         \tag{6}
\]
This is sufficient, not proved for this source.

Full S6 is stronger than necessary. Uniform integrability of the cubic
spectral observable for both (H) and its principal compressions suffices:
truncate (x^3) to a bounded-variation function on ([-R,R]), apply
interlacing for fixed (R) as (r/d\to0), then send (R\to\infty) using
the two uniform tail bounds. In particular, a source theorem
\(\sup_T\tau_d(|H|^4)<\infty\) suffices: Schatten compression gives
\(\tau_{d'}(|A|^4)\le(d/d')\tau_d(|H|^4)\), and each cubic tail is at
most its fourth moment divided by (R). No uniform fourth-moment theorem
for this natural-cutoff prime matrix is certified here either; the
repository's higher-moment source audits explicitly prohibit importing the
model values (m_4,m_5,m_6\).

The exact block compression identity (1) and a boundary-localized S2
estimate have therefore been used as far as their hypotheses reach. A
bounded-resolvent comparison can control bounded spectral tests, but raw
cubic recovery from it also needs a source-uniform large-eigenvalue tail
estimate (equivalently a suitable weighted resolvent integral); no such
estimate is recorded for this natural-cutoff matrix. No independent signed
prime cancellation for Tr(D^3) is proved.

The unconditional information currently recorded for this source consists
of the matrix identity, first/second-moment and local mean-square gates in
their stated scopes, the growing operator bound, the no-wrap operator
identity, and the selected-section crossing energy. A fourth-moment result
from a different model or a bounded consumer cannot be transferred to the
raw cubic tail.

## 4. Sixth-moment expansion and first unestimated arithmetic sum

For each (n=p^v\le N), let (V_n) be the exact real matrix whose entries
are
\[
(V_n)_{ij}=\delta_{ij}2(1-\alpha_n)\Re w_n(i)
+(1-\delta_{ij})\frac{\Im w_n(i)-\Im w_n(j)}{\pi(j-i)}.
\]
Then (V=\sum_nV_n). The complete sixth moment is the exact finite identity
\[
\tau_d(|H|^6)=\tau_d(H^6)
=\sum_{j=0}^6{6\choose j}s_0^{6-j}\frac1d
  \sum_{n_1,\ldots,n_j\in\mathcal P(N)}
       \operatorname{Tr}(V_{n_1}\cdots V_{n_j}),          \tag{7}
\]
where the (j=0) inner trace is (d), and
\(\mathcal P(N)=\{p^v:p\text{ prime},v\ge1,p^v\le N\}\).
Equivalently each word trace is the explicit cyclic index sum
\(\sum_{i_1,\ldots,i_j}\prod_{a=1}^j(V_{n_a})_{i_a i_{a+1}}\),
with (i_{j+1}=i_1). Its entries retain every carrier (e^{iT\log n}),
real/imaginary sign, diagonal multiplier, full (J), exact aliases and
proper powers.

The equality-pattern partition of the (n_a)'s (all distinct, repeated
ordinary-prime bases, and proper powers) is a legal finite bookkeeping
partition. No estimate here makes any class negligible. Nor does the
diagonal/off-diagonal split of the matrix entries make the corresponding
six-cycle sums positive separately. The first missing estimate for E1 is
therefore an upper bound uniform in (T) on the *total signed sixfold
source correlation* in (7), or a different source theorem implying
\(\sup_T d^{-1}\operatorname{Tr}|H|^6<\infty\). The elementary bound
\(\tau_d(H^6)\le\|H\|_{op}^4\tau_d(H^2)), even with bounded source
second moment, costs (O((1+S)^4)) and diverges at the natural cutoff.
Fourth-moment information alone cannot control the sixth moment.

## 5. Hostile test and evidence boundary

The exact abstract family (Y_d=\operatorname{diag}(d^{1/3},0,\ldots,0))
with one deleted row has (r/d=1/d\to0), full normalized cubic (1),
compressed cubic (0), and \(\tau_d(|Y_d|^6)=d\). It falsifies the
rank-only implication. It is **not** a prime-source matrix and is not a
counterexample to the actual prime theorem. No source-legal asymptotic spike
or source-specific exclusion of one is obtained. Finite rational matrix
replays verify identities only; absence of a spike in a finite diagnostic
would prove no uniform source bound.

Decision B/D2 still proves the same direct-consumer section has the
endpoint-score and crossing-energy properties. Equations (1)--(3) prove its
mixed block terms are negligible. They leave precisely (5), or a usable
uniform-integrability substitute, unproved. The source-masked determinant
consumer remains separate and is not covered by D2.

## 6. Decision and remaining theorem obligations

**E3.** Conditional on (5), or on actual-source uniform integrability of
the cubic spectral tails, normalized raw cubic deletion is stable on the
Decision D2-selected interval. A uniform source S6 theorem would imply the
stronger quantitative estimate (6), while a uniform source fourth moment
would be another sufficient route. No such theorem is currently present.

The sixth Schatten bound, raw cubic deletion stability, signed fifth/sixth
gate, prime-to-Weil identification, zero-side block/tail-Weyl transfer,
\(m_3=2\), conditioned Cayley energy below (0.105), source-masked
determinant compatibility, and strict (>79\%\) remain OPEN. No positive
consumer saving is claimed.

## Reproduction

```powershell
python src/wp84_decision_e_prime_source_cubic_deletion.py
python src/wp84_decision_e_prime_source_cubic_deletion_replay.py
```

The producer writes the exact-constant certificate. The independent replay
uses only the standard library and does not import the producer.
