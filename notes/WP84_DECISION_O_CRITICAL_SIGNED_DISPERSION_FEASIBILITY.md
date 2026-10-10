# WP84 Decision O — critical signed dispersion feasibility

**Decision O4.** In the representative block $B\asymp X^{3/5}$, $n_1,n_2\asymp X^{4/5}$, the fixed-$(B,n_1)$ admissible $n_2$ interval has length $O(X^{-1/5}e^{\sqrt L/2})=o(1)$, so it contains at most one integer. This gives a sparse graph description, but no density of prime-power occupancy and no signed cancellation.

An exact additive Fourier completion of the sharp product interval is possible. Expanding the endpoint kernel root by root preserves its exact multiplicative separability. However, the interval completion needs period $Q\gg X^{8/5}$; combining it with the original modulus $B$ yields bilinear modulus $BQ\gg X^{11/5}$. The resulting valid DFT bound is $O(LX^{7/5}e^{-\sqrt L/2})$, much worse than the existing $X^{29/250}$ absolute bound at $\epsilon=1/100$. A source-matched Cauchy dispersion expansion has an unresolved off-diagonal prime-power correlation and its available absolute bound is only $O(X^{3/10-o(1)})$. No power saving is earned; the tested methods do not approach the required $29/250$ saving.

This is a bounded failure of these completion/dispersion estimates, not a counterexample to the arithmetic inequality and not a claim that every analytic method fails. Strict $>79\%$ and the inherited arithmetic, band, and zero-side obligations remain OPEN.

## 1. Frozen source and verified prerequisites

Starting branch and HEAD were `codex/c5-c6-attack-20261006` and `3fab3a406dcb710cbc7a085626246571c82ed570`; the pre-existing untracked `notebooklm_packet/` was preserved. Decision N's note and certificate were read, as was the prior first-alias Type-II feasibility audit. Decision N's carrier approximation is accepted here and not rederived as a theorem search.

Use
\[
X=T/(2\pi),\quad L=\log X,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,
\quad d=\lfloor XL\rfloor,\quad M=\lceil d e^{-\sqrt L/2}\rceil,
\quad H=e^{\sqrt L/2}.
\]
All leaves remain prime powers $p^v\le N$, with the original
\[
c_n=-\Lambda(n)/(a_\phi(T)L\sqrt n),\qquad \alpha_n=\log n/L.
\]
For two positive leaves and the negative singleton, $A=n_1n_2$, $B=n_3$, and the retained coherence condition is
\[
|A-XB|\le4BH.
\]
For each closed finite-J lag path, all factors $f_{\ell_j}^{\sigma_j}(\alpha_{n_j})$, the exact displacement exponential, the original finite-root intersection, the global centering, both endpoint choices, and the carrier scalar $e^{iTL-2\pi iX}$ are retained. The additive phase is exactly $e(A/B)=e(n_1n_2/B)$ after Decision N. No ordinary-prime/fixed-$R$ transfer is used.

The three dyadic ranges overlap: $n_1n_2$ ranges from $X^{8/5}$ to $4X^{8/5}$ while $XB$ ranges from $X^{8/5}$ to $2X^{8/5}$. They lie below $N$ for sufficiently large $X$, because $X^{4/5}/N\ll X^{-1/5}e^{\sqrt L}\to0$ and $X^{3/5}/N\to0$.

## 2. Thin-strip sparsity and what it does not imply

For fixed $B\in[X^{3/5},2X^{3/5}]$ and $n_1\in[X^{4/5},2X^{4/5}]$, the allowed interval for $n_2$ is
\[
\left[\frac{XB-4BH}{n_1},\frac{XB+4BH}{n_1}\right],
\]
whose length is
\[
\frac{8BH}{n_1}\le16X^{-1/5}e^{\sqrt L/2}
=16\exp(-L/5+\sqrt L/2)=o(1).
\]
It therefore contains at most one integer for all sufficiently large $X$. The same statement holds with $n_1,n_2$ interchanged. It applies to prime powers as a subset, but does not assert that the interval contains an integer, much less a prime power.

Let $\mathcal G_B$ be the resulting partial matching between the integer $n_1$ and $n_2$ sets. The number of edges is bounded using the other exact parametrization: there are $O(BH+1)$ integer products $A$, and each has at most $d_2(A)\ll_\epsilon (XB)^\epsilon$ ordered factorizations. Thus
\[
|\mathcal G_B|\ll_\epsilon (BH+1)(XB)^\epsilon.
\]
This reproduces the existing divisor-count support bound. Injectivity in each coordinate alone does not improve it: the graph could still have as many as this many edges. No prime-power occupancy density is inferred.

The coefficient scale on this block is $|c_{n_1}c_{n_2}c_B|\ll(AB)^{-1/2}\asymp X^{-1/2}B^{-1}$, and $|K_{\rm center}|/d\le2M/d\ll H^{-1}$. Counting $(B,A)$ by $O(X^{3/5}\cdot X^{3/5}H)$ and then ordered factorizations gives
\[
\frac{|S|}{d}\ll_\epsilon X^{1/10+8\epsilon/5}
\]
as in Decision N. At $\epsilon=1/100$ this is $X^{29/250}$, which grows. Thinness alone has not improved this bound.

## 3. Exact sharp-window Fourier completion

For each fixed $B$, let $I_B$ be the consecutive integer interval cut out by $|A-XB|\le4BH$; its length $m_B\le8BH+1$. On the fixed factor box, every product satisfies $1\le n_1n_2\le4X^{8/5}$. Choose a power of two $Q$ with
\[
5X^{8/5}<Q\le10X^{8/5}.
\]
There is no wrap on the products in this box, so the DFT of the interval is an exact decomposition, including its sharp boundary:
\[
\mathbf1_{I_B}(A)=\sum_{r\ ({\rm mod}\ Q)}\widehat I_B(r)e(rA/Q),\qquad
\widehat I_B(r)=Q^{-1}\sum_{a\in I_B}e(-ra/Q).
\]
The geometric-sum formula gives, for $r\ne0$,
\[
|\widehat I_B(r)|\le\min\{m_B/Q,\,[2\min(r,Q-r)]^{-1}\}.
\]
Thus the ordinary Fourier coefficient $\ell^1$ norm is $O(1+\log Q)=O(L)$, uniformly in the real center $XB$; no smoothing or transition region is introduced.

The endpoint kernel can be split exactly into its original root terms:
\[
d^{-1}K_{\rm center}(E,\ell,\log(A/B))
=d^{-1}\sum_{k\in E\cap K_\ell}e^{2\pi i k\log(A/B)/L}
-|E|d^{-2}\sum_{k\in K_\ell}e^{2\pi i k\log(A/B)/L}.
\]
For each fixed root $k$, the factor is exactly
\[
e^{2\pi i k\log(n_1n_2/B)/L}
=n_1^{it_k}n_2^{it_k}B^{-it_k},\qquad t_k=2\pi k/L,
\]
so the root term, finite-J filters, source coefficients, and displacement phases are separable in $n_1,n_2$. The sum of absolute root coefficients is at most $2M/d\ll H^{-1}$, including the full-root centering term.

Completion combines the original phase $e(A/B)$ with the Fourier mode to give
\[
e(A/B)e(rA/Q)=e((Q+rB)A/(BQ)).
\]
For odd prime-power singleton $B$, $\gcd(B,Q)=1$. Put $q=BQ$ and $c_r=Q+rB$. The exact $q\times q$ additive Fourier matrix obeys
\[
\|[e(c_rxy/q)]_{x,y\bmod q}\|_{2\to2}
=\sqrt{q\,\gcd(c_r,q)}
=\sqrt{BQ\,\gcd(r,Q)}.
\]
The identity follows by summing row inner products; it also covers non-coprime $c_r$. For the power-of-two $Q$, the interval coefficient bound above yields
\[
\sum_{r\ ({\rm mod}\ Q)}|\widehat I_B(r)|\sqrt{\gcd(r,Q)}
\ll 1+\log Q+m_B/\sqrt Q\ll L.
\]
To see the weighted estimate, group nonzero $r$ by $v_2(r)$: below $Q/m_B$ use $m_B/Q$, and above it use $1/\min(r,Q-r)$; the resulting dyadic valuation weights form a convergent geometric sum times $O(\log Q)$. The $r=0$ contribution is exactly $m_B/\sqrt Q=o(1)$.

Each prime-power coefficient array on an $X^{4/5}$ dyadic interval has squared $\ell^2$ norm at most
\[
|a_\phi(T)|^{-2}\sum_{X^{4/5}\le n\le2X^{4/5}}1/n=O(1),
\]
since $\Lambda(n)/L\le1$ and filter factors are bounded by their Decision J lag weights. The two factor lengths are less than $q$, so no interval-completion multiplicity is gained. Summing the exact DFT estimate over $r$, roots, paths, and singleton $B$ gives
\[
\frac{|S_{\rm Fourier}|}{d}
\ll W_3\frac{M}{d}L\sum_{B\asymp X^{3/5}}B^{-1/2}\sqrt{BQ}
\ll L X^{7/5}e^{-\sqrt L/2}.
\]
Here $Q\asymp X^{8/5}$, $\sqrt{BQ}\asymp X^{11/10}$, each $B^{-1/2}$ is $X^{-3/10}$, and there are at most $O(X^{3/5})$ integer moduli. This upper bound grows like $X^{7/5-o(1)}$; it is worse than the existing $X^{29/250}$ bound by $321/250-o(1)$ powers. The sharp Fourier completion is exact and controlled, but its bilinear-modulus cost overwhelms its logarithmic coefficient norm. No transition-region charge is needed because this completion does not smooth.

The exceptional singleton powers $B=2^v$ have at most two members in this dyadic block. They can be bounded directly, without dropping them: for each such $B$,
\[
|S_B|/d\ll_\epsilon X^{-1/2}(XB)^\epsilon
=O_\epsilon(X^{-1/2+8\epsilon/5}).
\]
For example $\epsilon=1/10$ gives $O(X^{-17/50})=o(1)$. This small subfamily removal does not change the odd-modulus completion exponent or establish the full block estimate.

## 4. One source-matched Cauchy dispersion attempt

Fix a lag path, endpoint, and one root term $k$ of the exactly centered kernel. Its root phase factors over $n_1,n_2,B$. For fixed $(B,n_1)$ the thin-strip result defines at most one $n_2=\nu_B(n_1)$. Absorb the original separated filter, displacement, coefficient, and root factors into $a_k(n_1)$ and $b_{k,B}(n_1)$, setting $b=0$ when there is no admissible prime-power $\nu_B(n_1)$. Then the exact root contribution has the form
\[
S_k=\sum_{n_1}a_k(n_1)\sum_{B\asymp X^{3/5}}b_{k,B}(n_1)e(n_1\nu_B(n_1)/B).
\]
Cauchy in $n_1$ gives the exact square expansion
\[
|S_k|^2\le\Big(\sum_{n_1}|a_k(n_1)|^2\Big)
\sum_{n_1}\sum_{B,B'}b_{k,B}(n_1)\overline{b_{k,B'}(n_1)}
e\!\left(\frac{n_1\nu_B(n_1)}B-
\frac{n_1\nu_{B'}(n_1)}{B'}\right).
\]
The first factor is $O(1)$. The diagonal $B=B'$ in the second factor is nonnegative and records the actual prime-power occupancy. For $B\ne B'$, put $h=n_1\nu_B(n_1)-XB$ and $h'=n_1\nu_{B'}(n_1)-XB'$. The two exact product-window intersections are
\[
|h|\le4BH,\qquad |h'|\le4B'H,
\]
and the cross phase simplifies exactly to
\[
e(h/B-h'/B'),
\]
because the common $X$ carrier cancels. The residue constraints are $n_1\nu_B(n_1)\pmod B$ and $n_1\nu_{B'}(n_1)\pmod {B'}$; their common denominator is governed by $\operatorname{lcm}(B,B')$, with all shared-prime and proper-power gcd cases retained. These off-diagonal terms can be coherent when $h/B-h'/B'$ is near an integer. No source estimate for their signed sum is available here.

Bounding the expanded off-diagonal by absolute values gives no gain. There are at most $O(X^{3/5})$ singleton integers for a fixed $n_1$ and each $|b_{k,B}(n_1)|\ll X^{-7/10}$ on these dyadic scales (the singleton and $n_2$ coefficient factors). Thus
\[
\sum_{n_1}\left(\sum_B|b_{k,B}(n_1)|\right)^2
\ll X^{4/5}(X^{3/5}X^{-7/10})^2=X^{3/5}.
\]
The Cauchy output is $O(X^{3/10})$ before the normalized root factor $M/d\ll e^{-\sqrt L/2}$, or $X^{3/10-o(1)}$ afterward. This is weaker than $X^{29/250}$, and cancellation in the displayed off-diagonal is the missing theorem, not a consequence of the Cauchy step.

## 5. Quantitative decision and scope

| Step | Certified size on the normalized block | Saving toward target |
|---|---:|---:|
| Existing divisor/absolute bound, $\epsilon=1/100$ | $O(X^{29/250})$ | none; required exponent is negative |
| Fixed-$(B,n_1)$ thinness | at most one integer $n_2$ | no occupancy density or sign information |
| Exact interval DFT completion | $O(LX^{7/5}e^{-\sqrt L/2})$ | none; worse by $321/250-o(1)$ powers |
| Cauchy dispersion, absolute off-diagonal | $O(X^{3/10-o(1)})$ | none; worse than the starting bound |
| Singleton $B=2^v$ subfamily | $O_\epsilon(X^{-1/2+8\epsilon/5})$ | this subfamily is $o(1)$ only |

The bound required for the full block is $o(1)$, with a source-matched signed saving strictly greater than $X^{-29/250}$ relative to the inherited baseline at $\epsilon=1/100$. The Fourier and Cauchy routes above do not approach it. No log, smooth-transition, endpoint, or prime-power cost was hidden. All estimates are uniform for a fixed admissible endpoint; no height, modulus, or unrelated endpoint average is substituted.

**Primary classification: O4.** The tested exact completion and one Cauchy dispersion method fail to achieve the required exponent under their available source-valid bounds. The exact unresolved term is the signed off-diagonal sum over $B\ne B'$ in the displayed square expansion, retaining the narrow product-window intersections, finite-J source factors, root terms, and endpoint. This is not a counterexample to the original signed inequality. No cubic deletion, $m_3=2$, conditioned Cayley energy, fifth/sixth gate, prime-to-Weil, zero-side, determinant, or strict $>79\%$ conclusion follows.

The exact source summand being tested, for each ordered slot assignment and closed lag path, is
\[
c_{n_1}c_{n_2}c_B e^{iT\Omega}
\prod_{j=1}^3 f_{\ell_j}^{\sigma_j}(\alpha_{n_j})
\exp\!\left(2\pi i(\sigma_2q_1\alpha_{n_2}+\sigma_3q_2\alpha_B)\right)
K_{\rm center}(E,\ell,\Omega),
\]
where $\ell_1+\ell_2+\ell_3=0$, $q_0=0$, $q_1=\ell_1$, $q_2=\ell_1+\ell_2$, and $\Omega=\log(A/B)$. The carrier replacement is the Decision N identity
\[
e^{iT\Omega}=e^{iTL-2\pi iX}e(A/B)+\mathcal E_{A,B},
\qquad |\mathcal E_{A,B}|\le32\pi e^{\sqrt L}/X.
\]
No coefficient is made positive, no proper prime power is removed, and the finite-root centering and both endpoint choices remain in $K_{\rm center}$. The estimates above are uniform in each fixed admissible endpoint; they do not exchange endpoint and height averages.

The prerequisite replay sequence was rerun: Decisions I, J, K, L, M, N and the previous first-alias Type-II feasibility replay all exited successfully; this Decision O independent replay also passed. These replays certify their stated finite algebra and exponent bookkeeping only. In particular, they do not estimate the unresolved signed off-diagonal correlation.

### Reproduction

Run:

```powershell
python src/wp84_decision_o_critical_signed_dispersion.py
python src/wp84_decision_o_critical_signed_dispersion_replay.py
```

The independent replay checks the exact exponent arithmetic, interval DFT identities and weighted gcd structure on finite powers of two, the additive DFT operator norm for coprime and non-coprime numerators, the sparse-interval implication, and hostile mutations for wraparound, integer-center assumptions, prime-power omission, zero-mode loss, separability, and endpoint averaging. Finite checks do not prove the missing asymptotic off-diagonal estimate.
