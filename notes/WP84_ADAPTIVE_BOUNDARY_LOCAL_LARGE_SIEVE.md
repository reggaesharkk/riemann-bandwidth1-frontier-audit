# WP84 — local large sieve and adaptive finite-section boundary transfer

**Decision B.** An existential contiguous section obtained by trimming (o(d)) rows from the two ends has complete finite-section cubic boundary correction (o(1)), with the original prime-power cutoff and phases. This does not prove a uniform estimate over all sections, transfer the original full-section cubic, or close the zero-side/conditioned-energy consumer.

This note builds on the exact block identity in `WP84_FINITE_SECTION_CUBIC_BOUNDARY_ARITHMETIC.md`. It does not redo the infinite-lattice no-wrap argument or replace the prime field by random phases.

## 1. Frozen source and the discrete local large sieve

Use
\[
X=T/(2\pi),\quad L=\log X,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,
\quad d=\lfloor TL/(2\pi)\rfloor,
\]
and every prime power (n=p^v\le N), with
\[
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
z_n=c_ne^{iT\log n},\quad \alpha_n=\frac{\log n}{L},\quad
F_k=\sum_{p^v\le N}z_{p^v}e^{2\pi i k\alpha_{p^v}},\quad A_k=\Im F_k.
\]
The source gates are (a_\phi(T)\to1) and (s_0(T)\to1). The starting trace section is any source interval (I_0=[b,b+d-1]\); the construction below only takes contiguous subintervals of (I_0).

All (alpha_n) lie in ((0,1-1/\sqrt L]), since (log N\le L-\sqrt L). Distinct prime powers are distinct integers. If (m<n\le N),
\[
\log n-\log m\ge\log(1+1/N)\ge 1/(N+1).
\]
Thus neighboring frequencies in increasing order are separated by at least (1/((N+1)L)). The wraparound gap on (mathbb R/mathbb Z) is at least (1/\sqrt L), because (1-\alpha_{N_*}\ge1/\sqrt L) and the smallest frequency is positive. Consequently the circular separation satisfies, for all sufficiently large (T),
\[
\delta_T\ge\min\!\left(\frac1{(N+1)L},\frac1{\sqrt L}\right)
=\frac1{(N+1)L}.
\]
There are no duplicate frequencies: (n\mapsto\log n) is injective on the prime-power pool. The discrete large sieve for (delta_T)-separated points on the circle gives the precise bound
\[
\sum_{k=b}^{b+M-1}|F_k|^2
\le (M-1+\delta_T^{-1})\sum_{p^v\le N}|c_{p^v}|^2,
\]
for every integer (b); changing (b) only changes the coefficients by unit phases. Since (|A_k|\le|F_k|), the same upper bound holds for (A_k). The imaginary part therefore creates no need to prove separation for a union of positive and negative frequencies.

The coefficient square mass is
\[
\sum_{p^v\le N}|c_{p^v}|^2
=\frac1{|a_\phi|^2L^2}\sum_{p^v\le N}\frac{(\log p)^2}{p^v}=O(1).
\]
For (v=1), dyadic summation using the Chebyshev bound (θ(x)=\sum_{p\le x}\log p=O(x)) gives (∑_{p\le N}(\log p)^2/p=O((\log N)^2)=O(L^2)). For (v\ge2),
\[
\sum_p(\log p)^2\sum_{v\ge2}p^{-v}
\le2\sum_p\frac{(\log p)^2}{p^2}<\infty,
\]
so the proper-power square mass is (O(L^{-2})) after normalization. These estimates include every (p^v\le N), not only ordinary primes.

Therefore, uniformly in (b),
\[
\sum_{k=b}^{b+M-1}|A_k|^2\le C(M+NL).
\tag{1}
\]
The (NL) term is the reciprocal circular spacing; it is not replaced by a pointwise bound.

## 2. The proposed trim lies in the large-sieve regime

Set
\[
M=\left\lceil d e^{-\sqrt L/2}\right\rceil.
\]
Since (d\sim TL/(2\pi)=XL) and (N\sim Xe^{-\sqrt L}),
\[
\frac Md=e^{-\sqrt L/2}+o(1)\longrightarrow0,
\qquad
\frac M{NL}=e^{\sqrt L/2}(1+o(1))\longrightarrow\infty.
\tag{2}
\]
In particular (M\to\infty), and (1) implies that every length-((M+1)) translated window has (∑ |A_k|^2\le C_1M) for large (T), with (C_1) independent of its start.

## 3. Endpoint averaging, including the infinite exterior

For (u,v\in\{0,1,\ldots,M\}), let
\[
I_{u,v}=[b+u,b+d-1-v],\qquad d_{u,v}=d-u-v\ge d-2M.
\]
For a contiguous interval (I=[\ell,r]), write
\[
E(I)=\|P_I V(I-P_I)\|_{HS}^2
=\frac1{\pi^2}\sum_{i\in I,j\notin I}\frac{(A_i-A_j)^2}{(j-i)^2}.
\]
Using ((x-y)^2\le2x^2+2y^2), it suffices to average the vertex weights
\[
w_I(x)=\sum_{y\text{ on the other side of }\partial I}\frac1{(x-y)^2}.
\]
If (x=\ell+t-1\) is inside, its left and right weights are at most (2/t) and (2/(d_{u,v}-t+1)), respectively, by (∑_{q\ge t}q^{-2}\le2/t). If (x=\ell-t) is outside to the left, then
\[
w_I(x)=\sum_{q=t}^{t+d_{u,v}-1}q^{-2}\le
\begin{cases}2/t,&t\le d,\\ d/t^2,&t>d.
\end{cases}
\tag{3}
\]
The same estimates hold at the right endpoint. Formula (3) sums over the entire complement, including all sites arbitrarily far from (I).

Average (E(I_{u,v})) over the ((M+1)^2) endpoint pairs. For each fixed offset (t), (1) bounds the sum of (A_{b+u+t}^2), or (A_{b+u-t}^2), over (u=0,\ldots,M) by (C_1M), uniformly in (t); averaging over the unused endpoint contributes no extra factor. Thus each boundary-distance shell with (1\le t\le d) costs at most a constant per dyadic shell: the shell (2^q\le t<2^{q+1}) has (O(2^q)) offsets, each with weight (O(2^{-q})), and its averaged (A^2) mass is (O(1)) per offset. There are (O(\log d)) such shells. For the exterior tail, the shell (2^qd<t<2^{q+1}d) has weight at most (O(1/(2^{2q}d))) per offset by (3); its total average is (O(2^{-q})), summable in (q\ge0). Consequently
\[
\frac1{(M+1)^2}\sum_{u,v=0}^{M}E(I_{u,v})\le C_2\log d.
\tag{4}
\]
At least one pair ((u_T,v_T)) therefore has (E(I_{u_T,v_T})\le C_2\log d). Its interval is source-admissible as a contiguous subinterval of (I_0), and by (2),
\[
d'=d-u_T-v_T=d-o(d),\qquad d'/d\to1.
\tag{5}
\]
This is an existence proof. It does not imply (E(I)=O(\log d)) for every section.

## 4. Complete finite-section cubic boundary payment on that interval

For the exact block decomposition,
\[
\Delta_I=3s_0\|P_I VQ_I\|_{HS}^2+R_I,
\quad
R_I=2\operatorname{Tr}(V_{PP}BB^*)+\operatorname{Tr}(BV_{QQ}B^*),
\quad B=P_I VQ_I.
\]
The scalar term is (O(\log d/d')=o(1)) by (4)–(5). The source-valid operator bound is
\[
\|V\|_{op}\le\|\operatorname{diag}(\beta)\|+\|[\operatorname{diag}(A),J]\|
\le2S+2S=4S,
\quad S=\sum_{p^v\le N}|c_{p^v}|=O(\sqrt N/L).
\]
Since each trace in (R_I) is bounded by the corresponding block operator norm times (|B|_{HS}^2),
\[
\frac{|R_I|}{d'}\le\frac{3\|V\|_{op}E(I)}{d'}
=O\!\left(\frac{S\log d}{d'}\right)
=O\!\left(\frac{\sqrt N}{TL}\right)
=O\!\left(\frac{e^{-\sqrt L/2}}{\sqrt T\,L}\right)=o(1).
\tag{6}
\]
No sign cancellation is used. The coefficients, full cutoff, carrier phases, prime powers, and original operator are unchanged. Equations (4)–(6) establish complete boundary transfer for at least one trimmed section inside the original length-(d) interval.

## 5. Quantifiers, section stability, and limits of the result

**Existential section.** Yes: (4) gives one section (I_T\subset I_0) for each (T) with (d'/d\to1) and complete boundary correction (o(1)). It can be used wherever the theorem asks only for an admissible common contiguous section and all other gates are established on that same selected section.

**Uniform section.** Not proved. Local large-sieve energy alone cannot give it. For the abstract sequence (A_0=\sqrt M), (A_k=0) for (k\ne0), every length-(M) window has square mass at most (M), yet an interval with the spike at an endpoint has (E(I)\ge M/\pi^2). This is a counterexample to the implication “uniform local (L^2) control (Rightarrow) uniform (O(\log d)) boundary energy.” It is not a counterexample from the prime source.

**Transfer to the original zero-side consumer.** The condition (d'/d\to1) is the stated size condition for the existing first/second prime-moment sampling arguments, which are uniform in contiguous endpoints in their recorded scope. It does not itself prove a same-section prime-to-Weil identification, a zero-side block/tail estimate, or any required endpoint-score condition. Those must hold on this very (I_T), or be shown stable under the trim.

For a bounded-variation scalar spectral function (f), Cauchy interlacing for a principal submatrix deleting (r) rows gives an empirical-CDF discrepancy at most (2r/d); hence
\[
\left|\frac1d\operatorname{Tr}f(Y)-\frac1{d-r}\operatorname{Tr}f(Y_I)\right|
\le 2\operatorname{TV}(f)\frac rd,
\]
under the corresponding probability-measure normalization. This applies to bounded rational consumers with finite total variation, once the same-matrix source identification is available.

The raw cubic is different: rank deletion alone does not control it. For (Y=\operatorname{diag}(d^{1/3},0,\ldots,0)), deleting the first coordinate changes the normalized cubic trace by (1), although (r/d=1/d\to0). If instead (\|Y\|_{6,d}\le C), embed the principal submatrix (Z) in dimension (d) by zero-padding. Then (\operatorname{rank}(Y-Z)\le2r), (\|Y-Z\|_{6,d}\le2\|Y\|_{6,d}), and Schatten Hölder gives
\[
|\tau_d(Y^3-Z^3)|\le3\|Y-Z\|_{3/2,d}\|Y\|_{6,d}^2
\le6\|Y\|_{6,d}^3(2r/d)^{1/2}.
\]
The first inequality follows by telescoping the three factors and applying normalized Schatten Hölder; the second uses rank interpolation (\|E\|_{3/2,d}\le(\operatorname{rank}E/d)^{1/2}\|E\|_{6,d}). Thus a uniform sixth-moment bound supplies the needed uniform integrability. Without it, the selected-section boundary result does not transfer a cubic moment from the original full interval.

Accordingly this note proves the finite-section block-boundary transfer only. It does not prove (m_3=2), the conditioned (0.105) energy inequality, the zero-side theorem, or strict (>79\%\). No Gaussian or model moment is used.

## Reproducibility

```powershell
python src/wp84_adaptive_boundary_large_sieve.py
python src/wp84_adaptive_boundary_large_sieve_replay.py
```

The independent replay checks prime-power separation/square-mass bookkeeping, the exact crossing-pair count, dyadic exterior-kernel sums, finite endpoint averaging, a finite deterministic Hermitian block-trace identity, and the spike falsifier. Those finite checks are diagnostics; the uniform discrete large-sieve inequality, Chebyshev bound, and endpoint-shell proof above are the analytic asymptotic argument.
