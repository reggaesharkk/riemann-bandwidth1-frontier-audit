# WP84 Decision J — full-frequency finite-section cubic paths

**Decision J2.** Relative-lag coordinates give an exact full-frequency formula for every finite-section cubic path. On the complete sector a fixed positive distance from integer aliases, the endpoint geometric kernel is (O_δ(1)), yielding a source-valid absolute bound (O_δ(S(T)^3/d)). This improves Decision H's global endpoint envelope by (e^{-√ L/2}/L^3), but still grows at the natural cutoff. Near aliases and full transfer remain open. The cubic lag kernel is absolutely summable with an explicit (R^{-1/3}) tail, but that tail also fails after the prime coefficient mass is included. No signed constant saving is established.

Starting state verified: branch `codex/c5-c6-attack-20261006`, HEAD `fd5dc616f0780dc33e40278647d1826ec5bc85f2`; only the pre-existing untracked `notebooklm_packet/` remains. It was not modified. No push or merge was performed.

## 1. Source and finite section

Keep the full prime-power pool
\[
\mathcal P(N)=\{p^v\le N:p\text{ prime},\ v\ge1\},\quad
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
\alpha_n=\frac{\log n}{L},
\]
with (X=T/(2\pi)), (L=\log X), (N=\lfloor Xe^{-\sqrt L}\rfloor), and the original finite contiguous section (I_0=[b,b+d-1]). No R=6000 lag truncation is imposed on this full matrix.

For (D_{n,\sigma}(i)=e^{2\pi i\sigma i\alpha_n}) and (J_{ij}=1/(\pi(j-i))) for (i\ne j), the Decision I operator is
\[
U_{n,\sigma}=(1-\alpha_n)D_{n,\sigma}
+\frac{\sigma}{2i}[D_{n,\sigma},J].
\]
For ℓ=(j-i\ne0),
\[
[D_{n,\sigma},J]_{ij}
=\frac{e^{2\pi i\sigma i\alpha_n}-e^{2\pi i\sigma j\alpha_n}}
{\pi(j-i)}
=e^{2\pi i\sigma i\alpha_n}
\frac{1-e^{2\pi i\sigma\ell\alpha_n}}{\pi\ell}.
\]
The diagonal commutator is zero. Therefore
\[
\boxed{U_{n,\sigma}(i,j)
=e^{2\pi i\sigma i\alpha_n}f_{j-i}^{\sigma}(\alpha_n),}
\]
where
\[
f_0^{\sigma}(\alpha)=1-\alpha,\qquad
f_{\ell}^{\sigma}(\alpha)
=\frac{\sigma(1-e^{2\pi i\sigma\ell\alpha})}{2\pi i\ell}
\quad(\ell\ne0).
\]
This fixes the finite-(J) orientation (j-i), both signs, and the diagonal. Direct conjugation gives (U_{n,\sigma}^*=U_{n,-\sigma}). The estimate (|f_0|\le1), (|f_\ell|\le1/(\pi|\ell|)) follows immediately. The finite (J) remains the original compression; no infinite-operator equality is substituted.

## 2. Relative lags and exact root conditions

In a closed path for ((V^3)_{kk}), write the three indices
\[
i_0=k,\qquad i_1=k+q_1,\qquad i_2=k+q_2,
\]
and the signed edge lags
\[
\ell_1=q_1,\qquad \ell_2=q_2-q_1,\qquad \ell_3=-q_2,
\qquad \ell_1+\ell_2+\ell_3=0.
\]
Set (q_0=0), (q_1=\ell_1), (q_2=\ell_1+\ell_2), and
\[
K_{\ell}=\{k\in\mathbb Z:k+q_0,k+q_1,k+q_2\in I_0\}.
\]
If (q_{\min}=\min(q_0,q_1,q_2)) and (q_{\max}=\max(q_0,q_1,q_2)), then
\[
K_{\ell}=\bigl[b-q_{\min},\ b+d-1-q_{\max}\bigr]\cap\mathbb Z,
\quad |K_{\ell}|=\max(0,d-(q_{\max}-q_{\min})).
\]
Thus it is a contiguous integer interval or empty. Its intersection with either contiguous endpoint interval (E_u=[b,b+u-1]) or (E_v=[b+d-v,b+d-1]) is also contiguous or empty. These conditions retain every finite-section intermediate root; they do not count paths that leave the section and re-enter.

For (n_j\in\mathcal P(N)), signs (\sigma_j\in\{-1,1\}), and
\[
\Omega=\sum_{j=1}^3\sigma_j\log n_j,
\]
the product of the three entries has phase
\[
\boxed{e^{2\pi i k\Omega/L}
e^{2\pi i(\sigma_2q_1\alpha_{n_2}+\sigma_3q_2\alpha_{n_3})}.}
\]
Indeed the three row coordinates are (k,k+q_1,k+q_2); collecting their (k)-parts gives the **full** frequency (Ω/L), while the remaining terms are exactly the displayed displacement phase. There is no assumption that the displacement phase is one.

Let (E) be either endpoint interval and (u_E=|E|). For this fixed lag triple and source triple, define
\[
K_{\rm center}(E,\ell,\Omega)
=\sum_{k\in E\cap K_\ell}e^{2\pi i k\Omega/L}
-\frac{u_E}{d}\sum_{k\in K_\ell}e^{2\pi i k\Omega/L}.
\]
The exact nonzero-carrier endpoint sum is
\[
\boxed{
\begin{aligned}
Y_E^{\ne0}={}&
\sum_{n_1,n_2,n_3\in\mathcal P(N)}
\sum_{\substack{\sigma_1,\sigma_2,\sigma_3=\pm1\\\Omega\ne0}}
\sum_{\substack{\ell_1+\ell_2+\ell_3=0\\\ell_j\in\mathbb Z}}
\left(\prod_{j=1}^3c_{n_j}\right)e^{iT\Omega}
\left(\prod_{j=1}^3f_{\ell_j}^{\sigma_j}(\alpha_{n_j})\right)
e^{2\pi i(\sigma_2q_1\alpha_{n_2}+\sigma_3q_2\alpha_{n_3})}
K_{\rm center}(E,\ell,\Omega).
\end{aligned}}
\]
The summand is zero when (K_\ell) is empty. The coefficient, carrier, filters, proper powers, path restrictions and the full global centering term are all present. The formula follows by expanding (V^3), parameterizing its two intermediate matrix indices by ((\ell_1,\ell_2)), and then summing the common root (k). For (E=E_u) it reconstructs the left endpoint sum; for (E=E_v), replace (u_E) by (v). The geometric kernel on any interval of length (r) is exactly (r) at integer frequency and otherwise has modulus (|\sin(\pi r\omega)|/|\sin(\pi\omega)|).

## 3. Exact representation versus earlier path formulas

Decision G/H wrote the cubic diagonal with fixed endpoint (k) and then expanded its neighboring indices. In that arrangement, a factor may be evaluated at (k) or at (k+q_j), so the endpoint frequencies look like signed subsets. Reindexing the complete closed path by relative lags proves that all three indices translate together with (k); their common phase is exactly the full (Ω/L). This resolves that bookkeeping ambiguity without equating Ω to a frequency before the indices have been reparameterized.

The earlier infinite no-wrap audit already had a full displacement frequency with a continuum partial-translation overlap weight. It is not this finite-(J) identity: its root weight is a continuum overlap/infinite-lattice object. The finite formula above has the exact discrete root set (K_\ell), endpoint intersection, and centered subtraction. Thus the new result is the exact finite-root organization and centered endpoint kernel for the compressed matrix. It is an algebraic representation, not a new asymptotic estimate.

## 4. Lag summability and its coefficient-weighted limitation

Set (w_0=1) and (w_\ell=1/(\pi|\ell|)) for ℓ(≠0). Then
\[
\|w\|_{3/2}
=\left(1+\frac{2\zeta(3/2)}{\pi^{3/2}}\right)^{2/3}.
\]
For the full zero-sum path mass, discrete Young's inequality and Hölder give
\[
\begin{aligned}
\sum_{\ell_1+\ell_2+\ell_3=0}\prod_jw_{\ell_j}
&=\sum_{\ell_3}w_{\ell_3}(w*w)_{-\ell_3}\\
&\le\|w\|_{3/2}\|w*w\|_3
\le\|w\|_{3/2}^3
=\left(1+\frac{2\zeta(3/2)}{\pi^{3/2}}\right)^2.
\end{aligned}
\]
For (R\ge1), a union bound on which coordinate exceeds (R), followed by the same inequalities, gives
\[
\begin{aligned}
\sum_{\substack{\ell_1+\ell_2+\ell_3=0\\\max_j|\ell_j|>R}}\prod_jw_{\ell_j}
&\le3\|w\mathbf1_{|\ell|>R}\|_{3/2}\|w\|_{3/2}^2\\
&\le \frac{3\,4^{2/3}}{\pi}
\left(1+\frac{2\zeta(3/2)}{\pi^{3/2}}\right)^{4/3}R^{-1/3}.
\end{aligned}
\tag{J.1}
\]
Here Σ(_{m>R}m^{-3/2}\le2R^{-1/2}) supplies the last line. This is a valid lag-only tail estimate.

It cannot be declared negligible after summing over the source triples. Let (S(T)=\sum_{n\in\mathcal P(N)}|c_n|=O(\sqrt N/L)). The absolute triple coefficient mass is (S(T)^3), and the eight sign triples are already represented by the three independent sign sums. For any endpoint interval of length at most (M),
\[
|K_{\rm center}|\le |E\cap K_\ell|+
\frac{|E|}{d}|K_\ell|\le2M.
\]
Therefore the two-endpoint absolute bound for the part with (max|\ell_j|>R) is at most
\[
32M S(T)^3\cdot \frac{3\,4^{2/3}}{\pi}
\left(1+\frac{2\zeta(3/2)}{\pi^{3/2}}\right)^{4/3}R^{-1/3}.
\]
After division by (d), the natural-scale envelope is
\[
O\!\left(\frac{M}{d}\frac{N^{3/2}}{L^3}R^{-1/3}\right)
=O\!\left(\frac{e^{3L/2-2\sqrt L}}{L^3}R^{-1/3}\right).
\]
For fixed (R) this grows. It is not a lower bound: it says this absolute tail payment is inadequate. All long lags remain in the exact formula unless separately estimated. The fixed-(R=6000) moment consumer is not a legal cutoff for these full-matrix paths.

## 5. Arithmetic classes and quantitative stop

For a triple define the full products
\[
P_+=\prod_{\sigma_j=+1}n_j,\quad
P_-=\prod_{\sigma_j=-1}n_j,\quad
\Omega=\log(P_+/P_-).
\]
Decision I has already bounded the exact equality (P_+=P_-) (the same-prime exponent-addition class). The remaining total-frequency classes are:

- nonzero central: (0<|\Omega|\le L/M);
- nonzero integer aliases (m=\pm1,\pm2): (|\Omega-mL|\le L/M);
- far frequencies: all other Ω, where the exact geometric kernel can be bounded using (|\sin(\pi\Omega/L)|^{-1}), while the carrier (e^{iT\Omega}) and the source coefficients remain.

These are full-frequency classes in relative-lag coordinates. They include both exact prime and proper-prime-power inputs. The coherence windows have width (1/M); exact nonzero zero-alias products remain distinct from Decision I's (P_+=P_-) class. Integer-product spacing for a distinct mixed product only gives (|\Omega|\ge1/(N^2+1)), which is much smaller than (L/M) at this cutoff. It does not rule out central near aliases. Near-nonzero-integer aliases likewise require estimates around the noninteger centers (X^m), not UFD equality. No phase randomness or independence is assumed.

For a complete fixed-gap far-frequency sector 
\[
\operatorname{dist}(\Omega/L,\mathbb Z)\ge\delta,\qquad 0<\delta<1/2,
\]
each of the two geometric sums in (K_{\rm center}) is at most (1/\sin(\pi\delta)), so (|K_{\rm center}|\le2/\sin(\pi\delta)). Summing all source triples, all eight signs and the full lag kernel gives
\[
\mathbb E_u|Y_{L,\rm far}|+\mathbb E_v|Y_{R,\rm far}|
\le \frac{32\|w\|_{3/2}^3}{\sin(\pi\delta)}S(T)^3.
\]
After normalization by (d\asymp TL), this is
\[
O_\delta\!\left(\frac{N^{3/2}}{T L^4}\right)
=O_\delta\!\left(\frac{e^{L/2-3\sqrt L/2}}{L^4}\right).
\]
The inherited whole-score absolute envelope is (O(K_TM/d)=O(e^{L/2-\sqrt L}/L)). Thus the far-sector upper envelope is smaller by (O_\delta(e^{-\sqrt L/2}/L^3)), a genuine source-valid quantitative sector improvement. It nevertheless diverges, so it pays none of the required (o(d)) full-score target. It is an absolute upper bound, not a negative signed saving.

The complementary alias neighborhoods around (m=0,\pm1,\pm2) retain an (O(M)) coherent geometric bound. Decision I controls only the exact carrier equality in the (m=0) class; its nonzero near aliases, as well as near-nonzero-integer aliases, remain. The lag-tail L1 payment also grows after including the full coefficient mass. The new far-sector estimate therefore improves one complete frequency sector but does not close the endpoint discrepancy.

The single remaining theorem needed for this route is a source-weighted estimate of the displayed (Y_E^{\ne0}) pair, summing the complete (P_+,P_-) populations with the actual carrier, displacement factors and (K_{\rm center}), strong enough to give
\[
\mathbb E_u|Y_{E_u}^{\ne0}|+\mathbb E_v|Y_{E_v}^{\ne0}|=o(d).
\]
No such estimate is proved here. There is no prime-source counterexample either.

**Decision J2:** exact full-frequency finite-path representation and an improved but insufficient far-sector bound proved; near aliases and quantitative transfer remain open. (m_3=2), conditioned Cayley energy (<0.105), signed fifth/sixth gate, prime-to-Weil identification, zero-side transfer, determinant compatibility, and strict (>79\%\) remain **OPEN**.

## Reproduction

```powershell
python src/wp84_decision_j_full_frequency_cubic_paths.py
python src/wp84_decision_j_full_frequency_cubic_paths_replay.py
```

The small regression uses a finite subset of the source prime-power coefficient formula to compare direct matrix multiplication with the independently summed root-restricted paths. It checks identities and hostile mutations only, not a complete natural-cutoff asymptotic.
