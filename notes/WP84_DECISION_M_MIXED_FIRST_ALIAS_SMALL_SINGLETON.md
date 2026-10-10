# WP84 Decision M â€” mixed first-alias small-singleton discharge

**Decision M2.** Both proposed mixed-sign removals follow from the original full prime-power finite-section source by absolute estimates. For every fixed (0\leq\eta<1/2), the mixed-sign first-alias unit-log neighborhood with singleton prime power (B\leq X^\eta) contributes (o(d)). For every fixed (0\leq\eta<1/4), the entire mixed-sign first-alias bin with (B\leq X^\eta) contributes (o(d)). The endpoint cases (\eta=1/2) and (\eta=1/4), respectively, are not established by these bounds. This is a sector removal only: the residual signed high-product estimate, complete cubic deletion, and strict (>79\%) theorem remain open.

Starting state was branch `codex/c5-c6-attack-20261006`, HEAD `e502bf1ab5fa9b1dd75e8c9de3ccbb9e01186f8d`; the pre-existing untracked `notebooklm_packet/` was left untouched. No fixed-(R) ordinary-prime consumer estimate is used below.

## 1. Source and exact mixed expression

Use the Decision I/J source, with (X=T/(2\pi)), (L=\log X),
\[
N=\lfloor Xe^{-\sqrt L}\rfloor,\qquad d=\lfloor XL\rfloor,
\qquad M=\lceil d e^{-\sqrt L/2}\rceil,
\]
all prime powers (n=p^v\leq N), and
\[
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\qquad \alpha_n=\log(n)/L,
\quad a_\phi(T)\longrightarrow1.
\]
The finite matrix uses the original compressed (J_{ij}=1/(\pi(j-i))) for (i\ne j), not an infinite-lattice replacement. Decision J gives, for every ordered closed path,
\[
\ell_1+\ell_2+\ell_3=0,\quad q_0=0,\ q_1=\ell_1,\ q_2=\ell_1+\ell_2,
\]
\[
K_\ell=\{k:k+q_0,k+q_1,k+q_2\in[b,b+d-1]\},
\quad
K_\mathrm{center}(E,\ell,\Omega)=\sum_{k\in E\cap K_\ell}e^{2\pi i k\Omega/L}
-\frac{|E|}{d}\sum_{k\in K_\ell}e^{2\pi i k\Omega/L}.
\]
The source path coefficient also includes every (f_{\ell_j}^{\sigma_j}(\alpha_{n_j})), the exact displacement phase
\[
\exp\!\left(2\pi i(\sigma_2q_1\alpha_{n_2}+\sigma_3q_2\alpha_{n_3})\right),
\]
and carrier (e^{iT\Omega}). The finite root restrictions, all lags, centering, and endpoint positions are retained. Absolute-value bounds below use only
\[
|f_0^\sigma|\leq1,\quad |f_\ell^\sigma|\leq(\pi|\ell|)^{-1},\quad
W_3:=\sum_{\ell_1+\ell_2+\ell_3=0}\prod_jw_{\ell_j}
\leq\left(1+\frac{2\zeta(3/2)}{\pi^{3/2}}\right)^2<\infty,
\]
and discard root/path restrictions only after writing this exact expression. No carrier cancellation is assumed.

For two plus signs and one minus sign, write (A=n_1n_2), (B=n_3), so (\Omega=\log(A/B)); the other orientation is its reciprocal, with (A=n_1), (B=n_2n_3). The (m=+1) first-alias bin is
\[
X^{1/2}\leq A/B\leq X^{3/2},\qquad
\delta=\log\frac{A}{XB},\qquad |\delta|\leq L/2.
\]
The reversed sign word gives the reflected (m=-1) bin. For fixed ordered slots, lag triple, and endpoint, the exact summand is
\[
c_{n_1}c_{n_2}c_{n_3}e^{iT\log(A/B)}
\prod_{j=1}^3 f_{\ell_j}^{\sigma_j}(\alpha_{n_j})
e^{2\pi i(\sigma_2q_1\alpha_{n_2}+\sigma_3q_2\alpha_{n_3})}
K_\mathrm{center}(E,\ell,\log(A/B)).
\]
Summing this expression over every prime-power factorization (n_1n_2=A), the singleton (B), all six mixed sign placements, and the complete finite path set is the source object estimated here. In particular, (A=XB) is not deleted or replaced by a prime correlation; if it occurs, its kernel is charged by (2M).

## 2. Exact finite-section kernel bounds

For any integer interval, its geometric sum at frequency (\omega=\Omega/L\) has modulus at most
\[
\min\left(r,\frac1{|\sin(\pi\omega)|}\right),
\]
where (r) is the interval length. The two terms defining (K_\mathrm{center}) therefore give, for endpoint length at most (M\leq d),
\[
|K_\mathrm{center}|\leq2\min\left(M,\frac1{|\sin(\pi\Omega/L)|}\right),
\]
with the (2M) bound at an exact integer sampling frequency. This follows for the centered full-root term because
\((|E|/d)\min(d,1/|\sin|)\leq\min(M,1/|\sin|)\). It keeps the original global centering; it is not an uncentered partial sum.

On the first-alias bin,
\(|\sin(\pi\Omega/L)|=|\sin(\pi\delta/L)|\). For
\(|\delta|\leq L/2\), this is at least (2|\delta|/L). In the unit-log region
\(|\delta|\leq1), (C=XB>0) and (A\in[C/e,eC]). The mean-value theorem gives
\[
|\log(A/C)|\geq |A-C|/(eC),
\]
so
\[
|K_\mathrm{center}|\leq
C_0\min\left(M,\frac{LC}{|A-C|}\right)\quad(A\ne C),
\qquad |K_\mathrm{center}|\leq2M\quad(A=C),
\tag{M.1}
\]
for an absolute constant (C_0) (for example (C_0=e) after a harmless enlargement). This is uniform as real (C=XB) approaches an integer. If (C) is an integer, exactly (A=C) receives the capped bound. If (C) is noninteger, at most two integers satisfy (|A-C|<1), and those are capped by (2M); no lower bound on their distance is used.

For completeness, for (C\geq2) integer shell counting proves
\[
\sum_{A\in\mathbb Z\cap[C/e,eC]}
\begin{cases}
M,&A=C,\\
\min(M,LC/|A-C|),&A\ne C
\end{cases}
\leq C_1\{M+LC\log(C+2)\}.
\tag{M.2}
\]
There are at most three integers with (|A-C|<1) when the center is allowed to be an integer; charge each by (M). Each shell (j\leq|A-C|<j+1), (j\geq1), contains at most two integers and contributes at most (2LC/j). There are (O(C)) occupied shells, and their harmonic sum is (O(\log(C+2))). This proves (M.2), including the exact-center convention.

## 3. Prime-power source weights and the near estimate

All source coefficients are retained. Since (n\leq N<X),
\(\Lambda(n)\leq\log n<L\), and (a_\phi(T)\to1), for sufficiently large (T)
\[
|c_{n_1}c_{n_2}c_B|
\leq C\,(AB)^{-1/2}.
\]
For a fixed integer product (A), the number of ordered positive-integer pairs ((n_1,n_2)) with product (A) is exactly (d_2(A)). The allowed prime-power pairs are a subset, so this upper bound includes repeated bases and proper powers without dropping any source term. Use the standard elementary divisor bound
\[
d_2(A)\leq C_\varepsilon A^\varepsilon,\quad\varepsilon>0.
\tag{M.3}
\]
Its constant is uniform in (A): writing (A=\prod p^a), (d_2(A)=\prod(a+1)). For all sufficiently large primes (p\geq2^{1/\varepsilon}), (a+1\leq2^a\leq p^{\varepsilon a}). The finitely many smaller primes contribute a finite product of suprema
\(\sup_{a\geq0}(a+1)p^{-\varepsilon a}\), which is absorbed into (C_\varepsilon).

For fixed singleton (B\leq Z), put (C=XB). Combining (M.1)â€“(M.3) and the ordered-factorization bound, the coefficient-weighted near sum is at most
\[
C_\varepsilon\frac{(XB)^\varepsilon}{\sqrt X\,B}
\{M+LXB\log(XB+2)\}.
\]
Here and below (C_\varepsilon) also absorbs the finite lag mass, six mixed sign placements, both endpoint sides, and the eventual bound on (a_\phi^{-3}). Summing over actual singleton prime powers and enlarging to all integers (2\leq B\leq Z),
\[
|Y_{\mathrm{near}}(Z)|
\leq C_\varepsilon\left(
X^{\varepsilon-1/2}MZ^\varepsilon
+X^{\varepsilon+1/2}L^2Z^{1+\varepsilon}\right),
\tag{M.4}
\]
where
\(\sum_{B\leq Z}B^{\varepsilon-1}=O_\varepsilon(Z^\varepsilon)),
\(\sum_{B\leq Z}B^\varepsilon=O_\varepsilon(Z^{1+\varepsilon})), and
\(\log(XB+2)=O(L)) for (Z=X^\eta) and fixed (\eta<1/2).

Since (d\asymp XL), (M\ll XL e^{-\sqrt L/2}), and (Z=X^\eta), (M.4) gives
\[
\frac{|Y_{\mathrm{near}}(X^\eta)|}{d}
\leq C_{\varepsilon,\eta}\left(
X^{-1/2+\varepsilon\eta}e^{-\sqrt L/2}
+X^{-1/2+\eta+\varepsilon(1+\eta)}L\right).
\tag{M.5}
\]
For (0\leq\eta<1/2), choose
\[
0<\varepsilon<\frac{1/2-\eta}{1+\eta}.
\tag{M.6}
\]
Both terms in (M.5) tend to zero. This proves candidate A for every fixed (\eta<1/2). At (\eta=1/2), (M.6) has no positive solution and the second estimate has no decaying power even as (\varepsilon\downarrow0); this argument does not establish that endpoint. For (\eta=0), (Z=1) contains no prime power and the assertion is vacuous; the displayed majorant also tends to zero.

## 4. Far region and the complete small-singleton first bin

In (1<|\delta|\leq L/2), the sine lower bound gives
\(|K_\mathrm{center}|\leq L). Keep the entire alias bin
\[
X^{1/2}B\leq A\leq X^{3/2}B
\]
and all original prime-power constraints; for an upper bound it is valid to extend (A\) to all positive integers up to (X^{3/2}B). The elementary summatory divisor bound
\[
\sum_{A\leq Y}d_2(A)=\sum_{ab\leq Y}1
\leq Y(1+\log Y)
\]
and partial summation yield, uniformly for (Y\geq2),
\[
\sum_{A\leq Y}\frac{d_2(A)}{\sqrt A}
\leq C\sqrt Y\log(Y+2).
\tag{M.7}
\]
Consequently, for each (B\leq Z),
\[
\sum_{A\leq X^{3/2}B}\frac{d_2(A)}{\sqrt{AB}}
\leq C X^{3/4}\log(X^{3/2}B+2).
\]
There are at most (Z) possible positive integer singleton values. Multiplying by the (O(L)) centered kernel and dividing by (d\asymp XL) gives the sharper, no-epsilon estimate
\[
\frac{|Y_{\mathrm{far}}(Z)|}{d}
\leq C X^{-1/4}Z\log(X^{3/2}Z+2)
=O_\eta(X^{-1/4}ZL).
\tag{M.8}
\]
This is stronger than the requested (O(X^{-1/4+\epsilon}Z^{1+\epsilon}L^C)) form; one may take any (\epsilon>0), (C=1), and enlarge the right side. With (Z=X^\eta), (M.8) is (o(1)) for every fixed (\eta<1/4). At (\eta=1/4) it is (O(L)), so the endpoint is not proved.

Combining (M.5) and (M.8), both orientations of the complete mixed-sign first-alias bin with singleton prime power (B\leq X^\eta) are (o(d)) for every fixed (0\leq\eta<1/4). This proves candidate B. It neither assumes favorable signs nor proves any negative signed constant.

## 5. Disjoint population ledger and genuine new range

For a transparent non-overlapping accounting, fix the Decision L low-product cutoff (X^{1/3}), and fix (0\leq\eta<1/4). Assign tuples in this order:

1. **Z:** (\Omega=0), the exact zero-carrier population handled by Decision I.
2. **LOW:** (\Omega\ne0) and (n_1n_2n_3\leq X^{1/3}), handled by Decision L/K.
3. **SAME1:** all signs equal and (X^{1/2}\leq n_1n_2n_3\leq X^{3/2}), handled by Decision L. (There is no overlap with LOW for large (X); the ordering still assigns any boundary overlap to LOW.)
4. **MIX1-small:** mixed signs, first-alias bin, singleton (B\leq X^\eta), handled by M; split disjointly into near (|\delta|\leq1) and far (1<|\delta|\leq L/2).
5. **RESIDUAL:** every tuple not assigned above: mixed first aliases with larger singleton, mixed first-alias tails outside the removed singleton range, other mixed aliases/fringes and far frequencies, same-sign higher aliases/fringes and complements.

The new class lies beyond the previously removed LOW population: in the full first bin,
\[
n_1n_2n_3=AB=(A/B)B^2\geq4X^{1/2}>X^{1/3}
\]
for large (X), since (B\geq2). In the unit-log core, (A/B=Xe^\delta), so (AB=Xe^\delta B^2\geq4X/e>X^{1/3}). Thus M removes genuinely higher total products. It is also disjoint from SAME1 by sign pattern. Exact zero carriers are outside the first alias for (X>1).

The partition uses the full finite-(J) source, not the fixed-(R=6000) ordinary-prime consumer. Earlier ordinary-prime high-product and signed near-alias reports retain their own masks, only ordinary primes, fixed (R), and consumer normalization; they provide no estimate for this full prime-power cubic endpoint sum. Conversely M does not improve or discharge those separate ordinary-prime obligations.

## 6. What remains and stop decision

For the untouched full-source populations, the inherited absolute envelopes remain insufficient:

| Untouched class | Inherited normalized absolute envelope | Status |
|---|---:|---|
| Global endpoint full-mass bound | (O(X^{3/2}e^{-2\sqrt L}/L^3)) | grows |
| Fixed-gap complement | (O_\delta(X^{1/2}e^{-3\sqrt L/2}/L^4)) | grows |
| Mixed (m=\pm1) coherence core and central fringe | (O(X^{3/2}e^{-2\sqrt L}/L^3)) | grows |
| Mixed inaccessible-center (m=\pm2) fringe | (O(X^{1/2}e^{-3\sqrt L/2}/L^{7/2})) | grows |
| Same-sign (m=\pm2) near core | (O_\varepsilon(X^{2\varepsilon}L)) | insufficient |
| Same-sign (m=\pm2) off-neighborhood in the enlarged product range | (O(X^{1/4}L^2)) | insufficient |
| Same-sign (m=\pm3) cutoff fringe | (O(X^{1/2}e^{-3\sqrt L/2}L^{3/2})) | grows |

These are the Decision L bounds and are not improved by M. In particular, at fixed singleton exponent (\eta<1/4), the first untouched (m=\pm1) core has (B>X^\eta); the existing global envelopes still grow for that residual. The older [ordinary-prime high-product signed feasibility audit](WP84_HIGH_PRODUCT_SIGNED_FEASIBILITY.md), [fixed-\(R\) near-alias audit](WP84_SIGNED_NEAR_ALIAS_ATTACK.md), and [fixed-\(R\) first-alias Type-II audit](WP84_CUBIC_FIRST_ALIAS_TYPEII_FEASIBILITY.md) examine a different masked consumer with ordinary-prime leaves and finite (R=6000). Their estimates do not transfer to this full prime-power finite-\(J\) score, and M does not improve those separate fixed-\(R\) claims.

The first theorem needed to advance the remaining full cubic deletion is still a **source-weighted signed multilinear estimate** for the residual dyadic prime-power products, with the actual carrier (e^{iT\log(A/B)}), all original filters and displacement phases, exact finite roots and centering, and uniform endpoint control. It must combine the remaining singleton range, all shrinking alias fringes, and the far complement to (o(d)). Divisor counting plus the geometric kernel leave the growing bounds in the table, while the inherited local large-sieve/operator estimates do not control this coupled cubic correlation at the required endpoint scale. No prime-source counterexample is proved.

The finite-(R=6000) ordinary-prime high-product estimate is not transferable because its source object and normalization differ. No signed constant saving is earned. **Decision M2** is not full deletion or a theorem-level (>79\%) advance.

Still OPEN: (m_3=2), conditioned Cayley energy (<0.105), signed fifth/sixth gate, prime-to-Weil identification, zero-side transfer, determinant compatibility, and strict (>79\%\).

## Reproduction and evidence boundary

Run the deterministic producer and independent replay identified in the certificate, plus the I/J/K/L prerequisite producer/replay suites. The scripts check finite integer factorizations, exact rational near-integer edge cases, exact finite-root centering, formulas, and hostile mutations. They do not sample asymptotically many source primes and do not replace the analytic proofs above.
