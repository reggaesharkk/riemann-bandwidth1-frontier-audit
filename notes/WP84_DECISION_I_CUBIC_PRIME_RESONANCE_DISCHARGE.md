# WP84 Decision I — exact cubic prime resonance and the remaining endpoint aliases

**Decision I2.** The exact zero-carrier part of the full prime-power cubic operator has a source-valid (O(L^{-3})) operator bound. Its centered contribution to the two length-(M) endpoint score windows is (O(M L^{-3})=o(d)). This is a genuinely controlled arithmetic sector. The complete cubic endpoint discrepancy remains open because nonzero and near sampled aliases, including the finite-(J) path terms, have not been bounded by (o(d)).

The audit starts from branch `codex/c5-c6-attack-20261006`, HEAD `f58316f8ad14442427328f208a49f1aeef98470b`; the pre-existing untracked `notebooklm_packet/` was not touched. No push or merge was performed.

## 1. Scope and prior-work boundary

The original full source matrix uses

\[
X=T/(2\pi),\qquad L=\log X,\qquad N=\lfloor Xe^{-\sqrt L}\rfloor,
\qquad d=\lfloor TL/(2\pi)\rfloor,
\qquad M=\lceil d e^{-\sqrt L/2}\rceil.
\]

Its complete coefficient pool is \(\mathcal P(N)=\{p^v\le N:v\ge1\}\), including proper prime powers, with

\[
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n}\in\mathbb R,
\qquad \alpha_n=\frac{\log n}{L},
\]
\[
A_k=\sum_{n\in\mathcal P(N)}\Im(c_ne^{iT\log n+2\pi i k\alpha_n}),\quad
\beta_k=\sum_{n\in\mathcal P(N)}2(1-\alpha_n)\Re(c_ne^{iT\log n+2\pi i k\alpha_n}),
\]
\[
H=s_0I+V,\qquad V=\operatorname{diag}(\beta)+[\operatorname{diag}(A),J],\qquad
J_{ij}=\frac1{\pi(j-i)}\ (i\ne j),\quad J_{ii}=0.
\]

The relevant H conclusion is H2: existing local large-sieve/operator bounds give a source-valid cubic-score square bound, but its natural-cutoff majorant does not prove the required endpoint discrepancy. The four earlier high-product, signed-near-alias, direct-correlation and infinite-no-wrap notes concern different scopes. In particular, the first three analyze the fixed-(R=6000) **ordinary-prime moment consumer**; their removals do not transfer to the full prime-power matrix above. Infinite no-wrap identities remove certain exact integer displacements in a different infinite partial-shift operator at fixed cutoff; they do not bound finite-section endpoint scores uniformly at the natural growing cutoff.

## 2. Exact signed reconstruction and finite-(J) norm

For \(\sigma\in\{-1,+1\}\), put
\[
D_{n,\sigma}=\operatorname{diag}(e^{2\pi i\sigma k\alpha_n}),\qquad
U_{n,\sigma}=(1-\alpha_n)D_{n,\sigma}+\frac{\sigma}{2i}[D_{n,\sigma},J].
\]
Writing \(w_n(k)=c_ne^{iT\log n}e^{2\pi i k\alpha_n}\), the identities
\[
\Im w_n(k)=\frac{w_n(k)-\overline{w_n(k)}}{2i},\qquad
2(1-\alpha_n)\Re w_n(k)=(1-\alpha_n)(w_n(k)+\overline{w_n(k)})
\]
give, term by term,
\[
\boxed{V=\sum_{n\in\mathcal P(N)}\sum_{\sigma=\pm1}
c_n e^{i\sigma T\log n}U_{n,\sigma}.}
\]
Here the leading coefficient is (c_n), so the displayed formula means
\(\sum c_n e^{i\sigma T\log n}U_{n,\sigma}\); the minus sign is already in the real coefficient (c_n). The commutator term has the sign \(\sigma/(2i)\), matching the imaginary part in \(A_k\).

The bilateral convolution with kernel \(1/(\pi r)\), \(r\ne0\), has Fourier multiplier \(i(1-2x)\) on \(0<x<1\), hence operator norm one. A vector supported on a finite section can be extended by zero, acted on by the bilateral operator, and compressed back. Therefore the actual finite matrix is a compression and
\[
\|J_{I_0}\|_{op}\le1.
\]
No equality claim for every finite section is needed (for a one-site section (J_{I_0}=0)). Since \(\|D_{n,\sigma}\|=1\),
\[
\|U_{n,\sigma}\|\le 1-\alpha_n+\tfrac12\|[D_{n,\sigma},J]\|
\le 1-\alpha_n+\|J\|\le2-\alpha_n<2.
\]
The last strict inequality uses (0<\alpha_n<1), which follows from (n\le N<X\).

## 3. Exact zero-carrier population

Expand \(V^3\) using the signed reconstruction. Its carrier at an ordered triple is
\[
e^{iT\Omega},\qquad \Omega=\sigma_1\log n_1+\sigma_2\log n_2+\sigma_3\log n_3.
\]
The zero-carrier operator \(R_0\) is the sum over exactly those ordered triples with \(\Omega=0\). Equivalently, the product of the prime powers on the plus-sign side equals the product on the minus-sign side. All signs equal is impossible because an empty side has product one while every (n_i\ge2). Thus there is a 2-versus-1 split. Unique factorization forces the three prime-power bases to be the same prime (p), and the singleton exponent to equal the sum of the other two:
\[
p^a p^b=p^{a+b}.
\]
The reverse sign orientation is included.

There are exactly six labelled sign vectors: three choices for the singleton slot in each orientation. For each fixed sign vector, summation over the two pair slots is over **ordered** (a,b\ge1). If (a\ne b), the swapped assignment is another labelled tuple; if (a=b), the single assignment is still present. No extra two is placed in the (a=b) case and no ordered assignment is discarded. The coefficient product is
\[
|c_{p^a}c_{p^b}c_{p^{a+b}}|
=\frac{(\log p)^3}{|a_\phi(T)|^3L^3p^{a+b}}.
\]
For each triple, submultiplicativity gives \(\|U_1U_2U_3\|\le 2^3=8\). Also
\[
\sum_{a,b\ge1}p^{-(a+b)}=(p-1)^{-2}.
\]
Consequently the proposed factor is valid for the **original finite-section** operators:
\[
\boxed{\|R_0\|_{op}\le
\frac{48}{|a_\phi(T)|^3L^3}
\sum_p\frac{(\log p)^3}{(p-1)^2}.}
\tag{I.1}
\]
The factor is exactly (6\cdot8=48). The prime sum converges, since
\[
\sum_p\frac{(\log p)^3}{(p-1)^2}
\le4\sum_{n\ge2}\frac{(\log n)^3}{n^2}<\infty.
\]

The natural finite cutoff gives a sharper bound without an additional theorem. Define \(\alpha_{p^a}=a\log p/L\). Retaining each of the three actual (U)-norm factors yields
\[
\boxed{\|R_0\|_{op}\le\frac6{|a_\phi(T)|^3L^3}
\sum_p(\log p)^3\sum_{\substack{a,b\ge1\\p^{a+b}\le N}}
\frac{(2-\alpha_{p^a})(2-\alpha_{p^b})(2-\alpha_{p^{a+b}})}{p^{a+b}}.}
\tag{I.2}
\]
This is no larger than (I.1), and preserves the exact cutoff and all proper powers.

The set defining (R_0) is closed under taking adjoints and reversing the ordered triple, so (R_0) is Hermitian. For any Hermitian (R),
\[
|(R)_{kk}-\tau_d(R)|\le |(R)_{kk}|+|\tau_d(R)|\le2\|R\|_{op}.
\]
Thus either endpoint partial sum of length at most (M) has absolute value at most (2M\|R_0\|), and the sum of the two endpoint expectations is bounded by
\[
\boxed{\frac{192M}{|a_\phi(T)|^3L^3}
\sum_p\frac{(\log p)^3}{(p-1)^2}.}
\tag{I.3}
\]
Because (a_\phi(T)\to1), (M/d\sim e^{-\sqrt L/2}), and the displayed prime sum is a fixed finite constant, (I.3) is (O(M/L^3)=o(d)). This proves a centered endpoint-score estimate for the exact zero-carrier cubic sector, not for all of (V^3).

## 4. What remains after this discharge

Let \(R_{\ne0}=V^3-R_0\), retaining every nonzero carrier triple and every ordered finite-section matrix path. The score identity is
\[
(H^3)_{kk}-\tau_d(H^3)
=3s_0^2(\beta_k-\tau_d V)
+3s_0((V^2)_{kk}-\tau_d(V^2))
+((R_0)_{kk}-\tau_dR_0)
+((R_{\ne0})_{kk}-\tau_dR_{\ne0}).
\]
The inherited local large-sieve consequences control the first two endpoint pieces in total absolute partial-sum average by (O(M+NL)=O(M)=o(d)): the linear term follows by Cauchy from the local \(\beta^2\) estimate and bounded global first moment; the nonnegative diagonal (h_k=(V^2)_{kk}\) has local mass (O(M+NL)), and its centering contributes (O(M)) using the bounded global second trace. Together with (I.3), the sole unclosed endpoint expression is
\[
\boxed{
\mathbb E_u\left|\sum_{k=b}^{b+u-1}
((R_{\ne0})_{kk}-\tau_dR_{\ne0})\right|
+\mathbb E_v\left|\sum_{k=b+d-v}^{b+d-1}
((R_{\ne0})_{kk}-\tau_dR_{\ne0})\right|=o(d).}
\tag{I.4}
\]

For a source triple, set
\[
A=\prod_{\sigma_i=+1}n_i,\quad B=\prod_{\sigma_i=-1}n_i,
\quad \Omega=\log(A/B).
\]
This full carrier is distinct from the endpoint sampling frequency. In the \(\beta_k^3\) term, (\omega=\Omega/L). In finite-(J) path terms, (\omega) is only the signed sum of the \(\alpha_{n_i}\) whose factors are evaluated at the moving endpoint (k); factors at other matrix indices contribute to the carrier but not to this endpoint frequency. With (q) consecutive endpoint samples,
\[
\left|\sum_{k=k_0}^{k_0+q-1}e^{2\pi i k\omega}\right|
=\begin{cases}q,&\omega\in\mathbb Z,\\
\displaystyle\frac{|\sin(\pi q\omega)|}{|\sin(\pi\omega)|}
\le\min(q,|\sin(\pi\omega)|^{-1}),&\omega\notin\mathbb Z.
\end{cases}
\]
The (T)-carrier \(e^{iT\Omega}\) remains present. A near alias is a condition \(|\omega-m|\lesssim1/M\), not the exact product equation for (R_0).

For a mixed product with distinct positive integers (A\ne B\), (A,B\le N^2),
\[
|\Omega|=|\log(A/B)|\ge\log(1+1/\max(A,B))\ge\frac1{N^2+1}.
\]
The resulting endpoint-frequency spacing is only (1/(L(N^2+1))). At the natural cutoff,
\[
\frac{M}{L(N^2+1)}\ll \frac{e^{-L+3\sqrt L/2}}{1}\longrightarrow0.
\]
Thus integer-product separation is much finer than the (1/M) coherence window and does not exclude nonzero near-zero aliases. It also does not prove that a particular near-alias family occurs. Nonzero integer aliases must be retained separately: total-frequency aliases satisfy (A/B\approx X^m), and the finite-path endpoint alias uses its own subset product ratio. Since (0<\alpha_n<1), nearest aliases (m=\pm1,\pm2) can occur for three factors; (m=\pm3) cannot.

## 5. Quantitative status and stopping point

Decision H's strongest inherited direct estimate is
\[
\mathbb E_u|Y_L(u)|+\mathbb E_v|Y_R(v)|=O(K_T(M+NL)),
\quad K_T=|s_0|+4\sum_{n\in\mathcal P(N)}|c_n|.
\]
When (M\gg NL), division by (d\) gives the available envelope (O(K_TM/d)=O(e^{L/2-\sqrt L}/L)), which diverges. The endpoint-local square majorant in Decision H also fails its sufficient (o(d^2/M)) threshold. These are insufficient upper bounds, not lower bounds, and do not show that the actual prime-source inequality fails. The exact zero-carrier removal does not by itself improve either estimate for the nonzero remainder.

The single first missing analytic estimate is (I.4), a source-matched centered partial-sum bound for the full finite-(J), nonzero-carrier prime-power cubic score, with the natural (N(T)), all carrier phases, and the original endpoint sampling. No deterministic trilinear/large-sieve estimate with the required coefficients and aliases is established here. The route stops at this precise point.

The finite producer and independent replay test the exact factor, finite UFD classifications, repeated exponents, compression-norm scope, and hostile mutations. They do not numerically sample primes or claim the asymptotic estimate (I.4).

**Still OPEN:** (m_3=2); conditioned Cayley energy (<0.105); signed fifth/sixth gate; prime-to-Weil identification; zero-side transfer; determinant-consumer compatibility; strict (>79\%\).

## Reproduction

```powershell
python src/wp84_decision_i_cubic_prime_resonance.py
python src/wp84_decision_i_cubic_prime_resonance_replay.py
```

The producer writes `certificates/WP84_DECISION_I_CUBIC_PRIME_RESONANCE_CERTIFICATE.json`. The replay independently reconstructs the small UFD census and exact rational prefactors and does not import the producer.
