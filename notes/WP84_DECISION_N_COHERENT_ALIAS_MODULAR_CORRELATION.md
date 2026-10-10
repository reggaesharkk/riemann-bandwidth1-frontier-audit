# WP84 Decision N — coherent alias to modular correlation

**Decision N4.** The carrier in the mixed positive first-alias coherence window can be replaced by an additive character modulo the singleton prime power with a uniformly negligible, source-weighted error, including the complete prime-power pool and both endpoint choices. The resulting exact correlation is not a separable bilinear sum: its thin product window and centered finite-root kernel couple the two prime-power variables. The finite Fourier bilinear estimate therefore does not apply to the actual weight. On a representative residual block `B ~ X^(3/5)`, `n1,n2 ~ X^(4/5)`, the absolute normalized bound has exponent `1/10 + (8/5) epsilon`; a signed estimate saving more than this exponent (and any logarithmic/subpower losses) is still missing. No signed saving is earned.

This is a bounded feasibility test, not a claim that no possible theorem can estimate the sum. Decision I–M's exact source scopes and classifications remain unchanged. Strict (>79\%), the signed fifth/sixth gate, the prime-to-Weil step, zero-side transfer, (m_3=2), the conditioned Cayley energy target, and determinant compatibility remain OPEN.

## 1. Frozen source and prerequisites

The required starting branch and HEAD were `codex/c5-c6-attack-20261006` and `4edcde030b352ada0ca0bd23faeec077f10b5e1f`. The pre-existing untracked `notebooklm_packet/` was left untouched. The Decision I, J, K, L, and M independent replays all passed before this audit. Their finite replay tests verify algebra and their stated bounds; none is an asymptotic signed estimate for the present residual.

Keep
\[
 X=T/(2\pi),\quad L=\log X,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,
 \quad d=\lfloor XL\rfloor,\quad M=\lceil d e^{-\sqrt L/2}\rceil.
\]
The source leaves are every prime power (n=p^v\le N), including proper powers, with
\[
 c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\qquad \alpha_n=\frac{\log n}{L},\qquad a_\phi(T)\to1.
\]
For the mixed orientation with two plus leaves and one minus leaf, put (A=n_1n_2), (B=n_3), and
\[
 \delta=\log(A/(XB)),\quad \Omega=\log(A/B)=L+\delta.
\]
The source summand for each ordered slot assignment and closed lag path is
\[
 c_{n_1}c_{n_2}c_B e^{iT\Omega}
 \prod_{j=1}^3 f_{\ell_j}^{\sigma_j}(\alpha_{n_j})
 e^{2\pi i(\sigma_2q_1\alpha_{n_2}+\sigma_3q_2\alpha_B)}
 K_{\rm center}(E,\ell,\Omega),
\]
where ℓ₁+ℓ₂+ℓ₃=0, q₀=0, q₁=ℓ₁, q₂=ℓ₁+ℓ₂. The original finite-section root intersection and the global centering in `K_center`, all finite-J filter factors, all displacement phases, and both endpoint selections are retained. Decision J supplies the complete finite lag-mass bound `W3 < infinity`. We use only the Decision M source-safe estimates
\[
 |f_0^\sigma|\le1,\quad |f_\ell^\sigma|\le (\pi|\ell|)^{-1}\ (\ell\ne0),\quad |K_{\rm center}|\le2M.
\]
No independent-phase, Gaussian, fixed-(R), or ordinary-prime substitution is made.

## 2. Carrier linearization, with real center

On (|\delta|\le L/M), set (z=h/(XB)=e^\delta-1), where (h=A-XB\in\mathbb R); neither (XB) nor (h) is assumed integral. Since (d\sim XL) and (M\sim XL e^{-\sqrt L/2}), eventually (L/M\le2e^{\sqrt L/2}/X\to0). Thus eventually (|\delta|\le1/4), (|z|\le2|\delta|\le1/2). The convergent logarithm series gives
\[
 |\log(1+z)-z|\le z^2\quad(|z|\le1/2).
\]
Because (T=2\pi X),
\[
 |T\delta-2\pi h/B|
 =2\pi X|\log(1+z)-z|
 \le8\pi X\delta^2
 \le32\pi\,e^{\sqrt L}/X.
\]
For real (u,v), (|e^{iu}-e^{iv}|\le|u-v|); consequently
\[
 |e^{iT\delta}-e^{2\pi ih/B}|\le32\pi e^{\sqrt L}/X.
\]
The exact algebra, valid for real (X), is
\[
 e^{iT\log(A/B)}
 = e^{iTL}e^{iT\delta}
 = e^{iTL-2\pi iX}e^{2\pi iA/B}+\mathcal E_{A,B},
 \qquad |\mathcal E_{A,B}|\le32\pi e^{\sqrt L}/X.
\]
Indeed (A/B=X+h/B); the phase (e^{-2\pi iX}) is essential. Reversing the orientation uses its source-prescribed conjugate/reflection; it does not change the error bound or authorize changing any filter or displacement phase.

## 3. Aggregate source-weighted error

For sufficiently large (T), (N<X), (a_\phi(T)\) is bounded away from zero, and hence
\[
 |c_{n_1}c_{n_2}c_B|\le C(AB)^{-1/2}.
\]
The coherence window implies
\[
 |A-XB|=XB|e^\delta-1|\le2XB L/M\le4B e^{\sqrt L/2}.
\]
This bound counts integer $A$ even when the real center $XB$ is arbitrarily close to an integer. For each $A$, all ordered prime-power factorizations $A=n_1n_2$ are bounded by $d_2(A)\le C_\epsilon A^\epsilon$. Since $A\asymp XB$ in the window and there are $O(Be^{\sqrt L/2}+1)$ possible integers $A$, for each singleton $B\le N$ the sum of absolute coefficient weights is
\[
 \ll_\epsilon X^{-1/2+\epsilon}
 \left(e^{\sqrt L/2}B^\epsilon+B^{\epsilon-1}\right).
\]
Summing over actual singleton prime powers and enlarging only for this upper bound to all integers (2\le B\le N) yields
\[
 \sum_{B,n_1,n_2\atop |\delta|\le L/M}|c_{n_1}c_{n_2}c_B|
 \ll_\epsilon X^{-1/2+\epsilon}
 \left(e^{\sqrt L/2}N^{1+\epsilon}+N^\epsilon\right).
\]
The normalized kernel and path/end-point factor is at most $C W_3 M/d$, with $M/d\le e^{-\sqrt L/2}+1/d$. Multiplying by the pointwise phase error gives
\[
 \frac{|\mathrm{aggregate\ replacement\ error}|}{d}
 \ll_\epsilon \frac{e^{\sqrt L}}{X}
 \left(e^{-\sqrt L/2}+1/d\right)
 X^{-1/2+\epsilon}
 \left(e^{\sqrt L/2}N^{1+\epsilon}+N^\epsilon\right)
 =O_\epsilon\!\left(X^{-1/2+2\epsilon}e^{-\epsilon\sqrt L}\right)
 +o\!\left(X^{-1/2+2\epsilon}e^{-\epsilon\sqrt L}\right).
\]
Here $N\le Xe^{-\sqrt L}$; the displayed leading bound is $o(1)$ for any fixed $0<\epsilon<1/4$, and the ceiling contribution $1/d$ is smaller. Constants include the complete lag mass, all ordered slot placements, both orientations, and either endpoint, uniformly in endpoint position. The geometric kernel, filters, root set and centering are unchanged: only the carrier is replaced. Thus classification N3 is ruled out; this proves the reduction half of N2/N4.

## 4. Exact modular correlation and dyadic absolute bound

After the certified replacement the residual phase is
\[
 e^{2\pi i A/B}=e^{2\pi i n_1n_2/B},
\]
times the global unit scalar (e^{iTL-2\pi iX}). For a fixed (B), path, endpoint and orientation, define the exact coupled residue weight
\[
 W_B(a,b)=\sum_{\substack{n_1\equiv a\ (B),\ n_2\equiv b\ (B)\\
 n_1,n_2,B\ \mathrm{prime\ powers}\le N\\
 |n_1n_2-XB|\le4B e^{\sqrt L/2}}}
 c_{n_1}c_{n_2}c_B\,\Phi_{\ell}(n_1,n_2,B)
 K_{\rm center}(E,\ell,\log(n_1n_2/B)),
\]
where Φℓ is exactly the product of the three original filters and the displacement exponential written in Section 1. The correlation is exactly
\[
 \sum_{a,b\bmod B}W_B(a,b)e^{2\pi iab/B}.
\]
The window and (K_{\rm center}) depend on (n_1n_2), so (W_B(a,b)) is not shown to factor as (u_B(a)v_B(b)). For a genuinely separable weight, the complete DFT identity
\[
 \sum_{y\bmod B}e^{2\pi i(a-a')y/B}=B\,\mathbf1_{a=a'\bmod B}
\]
implies
\[
 \left|\sum_{a,b}u(a)v(b)e^{2\pi iab/B}\right|
 \le\sqrt B\,\|u\|_2\|v\|_2.
\]
This is valid for any integer modulus, including (p^v), but its hypothesis is not met by the actual coupled weight. For an arbitrary matrix weight the direct Frobenius Cauchy bound is only (B\|W_B\|_F), with no square-root bilinear gain. Fourier completion of the product-window indicator would require bounding its full expansion against the same prime-power weights and the endpoint-dependent kernel; no such cost-free, uniform completion is supplied by Decisions I–M.

The complete DFT identity itself is equally exact for (B=p^v). What changes in the arithmetic is the non-coprime stratum: if (s=\min(v,v_p(n_1n_2))<v), the phase has conductor (p^{v-s}); if (s\ge v), it equals (1). These repeated-base/proper-power terms are retained in (W_B), can be coherent, and are not covered by a units-only estimate. No estimate may discard them. No prime equidistribution in residue classes is assumed.

For (B\asymp X^\beta), the window contains (O(Be^{\sqrt L/2}+1)) integers (A). Applying only (d_2(A)\ll_\epsilon A^\epsilon), the exact coefficient majorant, (W_3<\infty), (|K_{\rm center}|\le2M), and the (O(B)) integer count for singleton moduli gives, uniformly for each endpoint,
\[
 \frac{|S_{B\sim X^\beta}|}{d}
 \ll_\epsilon X^{-1/2+\epsilon}(X^\beta)^{1+\epsilon}
 +O_\epsilon(X^{-1/2+\epsilon}X^{\beta\epsilon}e^{-\sqrt L/2})
 = O_\epsilon\!\left(X^{\beta-1/2+\epsilon(1+\beta)}\right).
\]
This is an absolute bound, not a signed saving. For β>1/2 it grows. A cancellation factor (X^{-\sigma}) must have
\[
 \sigma>\beta-\tfrac12+\epsilon(1+\beta)
\]
with additional room for any logarithmic/subpower losses. The limiting required power as ε decreases to zero is strictly greater than β−1/2; equality leaves no decay.

## 5. One critical residual block and one attempted method

Take (B\in[X^{3/5},2X^{3/5}]), (n_1,n_2\in[X^{4/5},2X^{4/5}]). All three variables are below (N) for large (X). Their product ranges overlap the centers (XB\asymp X^{8/5}); the *actual* sum is restricted further by (|n_1n_2-XB|\le4B e^{\sqrt L/2}). No claim that every (B) has a prime-power pair in that narrow interval is made. The required exact source estimate is
\[
 \sup_{E\ \mathrm{admissible}}\frac1d\left|
 \sum_{\substack{B\in\mathcal P\cap[X^{3/5},2X^{3/5}]}
 \sum_{\substack{n_1,n_2\in\mathcal P\cap[X^{4/5},2X^{4/5}]\\
 |n_1n_2-XB|\le4B e^{\sqrt L/2}}}
 \sum_{\ell_1+\ell_2+\ell_3=0}
 c_{n_1}c_{n_2}c_B\Phi_{\ell}(n_1,n_2,B)
 K_{\rm center}(E,\ell,\log(n_1n_2/B))
 e^{2\pi i n_1n_2/B}\right|=o(1),
\]
where ℘ denotes all prime powers through the natural cutoff. The separate carrier replacement contributes the certified (o(1)) from Section 3. The absolute baseline at β=3/5 is (O_\epsilon(X^{1/10+8\epsilon/5})). Therefore this block needs a source-matched signed saving exceeding (X^{-1/10-8\epsilon/5}) relative to that baseline (strictly more than (1/10+8\epsilon/5) powers, before logs).

We tested the complete-residue bilinear DFT inequality as the bounded analytic attempt. It is exact for separable weights; applying it to (W_B(a,b)) would require precisely the unsupported factorization/low-rank decomposition of the product-window, finite-root-centered source weight. The universal matrix Cauchy bound has no needed gain. This failure is a hypothesis mismatch, not a counterexample to the actual arithmetic inequality. We do not import a Type I/II, large-sieve, dispersion, or almost-all-modulus estimate: no checked hypothesis supplies the needed uniformity in the variable prime-power modulus, narrow moving product interval, repeated-base strata, finite-J path weights, and each admissible endpoint simultaneously. This is a bounded no-go for this attempted reduction only, not an assertion that all literature methods fail.

The absolute endpoint-pair consumer is protected: every bound above is uniform for a fixed admissible endpoint (E), hence would imply the endpoint-pair average if a signed block estimate of the displayed strength were proved uniformly. A mean over (T), (B), or endpoints alone is not enough and is not substituted here.

## 6. Classification, scope, and remaining debt

**Primary classification: N4.** The carrier reduction is proved and its aggregate source-weighted error is (o(1)) (N2's positive conclusion). The one tested standard bilinear route does not apply to the coupled source weight, and the exact missing block inequality is given above. No signed constant saving or source counterexample is proved.

Unpaid populations remain as stated in Decision M: the mixed first-alias outer fringes and larger-singleton tails, inaccessible-center alias fringes, same-sign second-alias core/tails, same-sign cutoff fringes, and the fixed-gap high-product complement. Decisions I–M still do not give full cubic deletion. No fixed-(R), ordinary-prime result transfers to this full finite-J prime-power source.

### Reproduction

Run:

```powershell
python src/wp84_decision_n_coherent_alias_modular_correlation.py
python src/wp84_decision_n_coherent_alias_modular_correlation_replay.py
```

The independent replay uses exact rational identities, exact finite DFT checks for prime and prime-power moduli, non-coprime conductor cases, strict exponent arithmetic, the coupled-weight falsifier, and mutations for the (2\pi), integer-center, sign, fixed-(R), endpoint-mean, omitted-filter, and natural-cutoff mistakes. Finite checks validate identities and scope only; they do not establish the missing signed prime-power correlation.
