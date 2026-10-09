# WP84 Decision D — endpoint admissibility inside the adaptive trim

**Primary result: D2 — QUANTITATIVELY SUFFICIENT ADMISSIBLE DENSITY PROVED for the direct first-strike endpoint-score consumer.** The old endpoint estimate was stated on a wider window using the coarse range (N\le T^2). Reapplying its already-uniform short-interval mean-value and sampling inequalities with the actual natural cutoff proves a bounded mean score on Decision B's smaller window. Markov gives at least half of each endpoint window good; their product has at least one-quarter of the exact Decision B pair weight. Restricting the nonnegative boundary-energy average to that product set costs at most a factor four. No independence between scores and boundary energy is used.

This result is deliberately scoped. It covers the finite generic endpoint-feature scores in `WP84_GOOD_ENDPOINT_TRIMMING.md` used by the direct bounded first-strike construction. It does **not** transfer those scores to the separate hidden-prime determinant iterator requiring `source_mask(fid,slots,lag,T,section,alias)`. The prior `WP84_GOOD_ENDPOINT_DETERMINANT_COMPATIBILITY_AUDIT.md` identifies the missing score-to-masked-atom identity. That auxiliary route remains source-incomplete.

The result does not prove any of the strict (>79\%) theorem's independent arithmetic, raw-moment, or zero-side obligations.

## 1. Exact windows and weights

Use the frozen Decision B definitions

\[
X=T/(2\pi),\quad L=\log X,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,
\quad d=\lfloor TL/(2\pi)\rfloor,\quad h=2\pi/L,
\]

\[
M=\lceil d e^{-\sqrt L/2}\rceil,\quad
I_{u,v}=[b+u,b+d-1-v],\quad 0\le u,v\le M.
\]

Decision B's averaging measure is exactly uniform on
\(\mathcal W_T=\{0,\ldots,M\}^2\), with mass (1/(M+1)^2) per pair. The lower endpoint window consists of indices (b+u); the upper endpoint window consists of indices (b+d-1-v). Both have exactly (M+1) equally weighted points. The sampled physical parameter is the original
\(\tau_k=T+hk\); the endpoint theorem's mean-value bound is uniform in the location of the physical interval, so both the lower and upper windows are covered.

The physical length of either window, up to the harmless endpoint-cell enlargement in the sampling inequality, is

\[
U_T=hM=(1+o(1))T e^{-\sqrt L/2}.
\]

The earlier endpoint note used (r_0=\lfloor dL^{-1/2}\rfloor), whose physical width is (\asymp T L^{-1/2}). Thus (M/r_0\sim \sqrt L e^{-\sqrt L/2}\to0): the old statement's displayed window is wider. Its proof, however, states the mean-value estimate for **any** interval of length (U). The old coarse substitution (N\le T^2) was used only to report a large-window bound; it is not needed in the localized estimate below.

## 2. Local endpoint-score mean on the smaller window

For each of the finitely many fixed-(R) endpoint feature families in the direct consumer, write

\[
S_\theta(t)=\sum_{n\le N}a_n(\theta)e^{it\log n}.
\]

The existing endpoint proof supplies, after summing/integrating its finite feature parameters and adding the adjacent-index terms,

\[
\int \sum_{n\le N}|a_n(\theta)|^2\,d\theta\le C_R.
\]

This is the recorded balanced-product second-mass input. It retains the complete source pool (n=p^v\le N); the note bounds the proper-power correction in the same mass by (o(1)), rather than deleting those terms from the endpoint score. At fixed (R=6000), all path and feature multiplicities are finite and absorbed in (C_R).

For an interval (J) of length (U_T+O(h)), Montgomery--Vaughan applied to (S_\theta) and its derivative, followed by the same disjoint-cell sampling inequality as in the existing endpoint proof, gives

\[
\sum_{k:\,\tau_k\in J}\int |S_\theta(\tau_k)|^2d\theta
\le C_R L(U_T+N).
\]

Indeed the derivative multiplies coefficients by \(\log n\le\log N\le L\), and (h=2\pi/L), so both sampled terms have this scale. There are (M+1\asymp U_T L/(2\pi)) grid points. Dividing by their **actual uniform counting weight** yields for the combined nonnegative lower or upper endpoint score (\mathcal S_\pm\)

\[
\frac1{M+1}\sum_{u=0}^M\mathcal S_-(b+u)
\le C_R\left(1+\frac{N}{U_T}\right),\qquad
\frac1{M+1}\sum_{v=0}^M\mathcal S_+(b+d-1-v)
\le C_R\left(1+\frac{N}{U_T}\right).
\tag{1}
\]

Now use the actual cutoff, not (N\le T^2):

\[
\frac{N}{U_T}
\le(1+o(1))\frac{Xe^{-\sqrt L}}{T e^{-\sqrt L/2}}
=(1+o(1))\frac{e^{-\sqrt L/2}}{2\pi}\longrightarrow0.
\tag{2}
\]

Thus both endpoint-score means are (O_R(1)) on the Decision B windows. The estimate includes all retained prime powers and the original height/carrier phases. It is uniform in the integer location of each window.

## 3. Positive weighted density and joint selection

Set (B_\pm(T)=C_R(1+N/U_T)), enlarging (C_R) if needed to cover both score families. Define

\[
G_- =\{u:\mathcal S_-(b+u)\le2B_-(T)\},\quad
G_+ =\{v:\mathcal S_+(b+d-1-v)\le2B_+(T)\}.
\]

Markov's inequality for the equal finite endpoint weights in (1) gives

\[
\frac{|G_-|}{M+1}\ge\frac12,\qquad
\frac{|G_+|}{M+1}\ge\frac12.
\]

The consumer endpoint conditions are separate lower- and upper-endpoint score bounds in the cited endpoint theorem. Hence its jointly admissible set is the Cartesian product (G=G_-\times G_+\), and its **Decision B weighted density** is

\[
\gamma_T=\frac{|G|}{(M+1)^2}
=\frac{|G_-|}{M+1}\frac{|G_+|}{M+1}\ge\frac14.
\tag{3}
\]

The chosen score thresholds are (O_R(1)), as required by the direct bounded first-strike endpoint construction. No factorization or independence of the boundary-energy values is assumed.

**Route A (automatic for every pair) is not claimed.** The endpoint theorem is an average estimate, not a pointwise estimate for every endpoint. Local (L^2) hypotheses alone do not give automatic admissibility. Route B succeeds by a positive-density argument. Route C is the restriction inequality (4); it is valid under arbitrary score/energy dependence because the admissible set has positive mass and (E\ge0\).

Decision B proves the separate uniform-weight bound

\[
\frac1{(M+1)^2}\sum_{(u,v)\in\mathcal W_T}E(I_{u,v})\le C_B\log d,
\quad E(I)=\|P_I V(1-P_I)\|_{HS}^2\ge0.
\]

For the admissible set (G), nonnegativity alone implies

\[
\frac1{|G|}\sum_{(u,v)\in G}E(I_{u,v})
\le\frac{C_B\log d}{\gamma_T}
\le4C_B\log d.
\tag{4}
\]

Therefore at least one pair is simultaneously endpoint-admissible and has (E(I_{u,v})\le4C_B\log d). This proves a direct joint selection inequality and remains valid under arbitrary anticorrelation between endpoint score and crossing energy. It uses the same equal finite weights in both estimates; there is no conversion from an unweighted count to a different measure.

For a general nonuniform pair weight \(\omega_{uv}\), the valid statement is instead (\sum_G\omega_{uv}E_{uv}\le\sum_{\mathcal W}\omega_{uv}E_{uv}\), so the density in (4) must be \(\sum_G\omega_{uv}\). An unweighted density cannot replace that weighted mass. The certificate/replay includes an exact weighted counterexample to this invalid substitution.

## 4. Propagated cubic boundary estimate and density threshold

The exact block identity is

\[
\Delta_I=3s_0(T)E(I)+R_I,\qquad |R_I|\le3\|V\|_{op}E(I),
\quad \|V\|_{op}\le4S,
\]

where the complete prime-power mass and normalization are

\[
S=\sum_{p^v\le N}|c_{p^v}|
=\frac1{|a_\phi(T)|L}\sum_{p^v\le N}\frac{\Lambda(p^v)}{\sqrt{p^v}}
=O(\sqrt N/L).
\]

For any admissible weighted density \(\gamma_T\) for which the averaging argument yields (E(I)\le C_B\log d/\gamma_T),

\[
\frac{|\Delta_I|}{d'}
\le\frac{3C_B\log d}{\gamma_Td'}\bigl(|s_0(T)|+4S\bigr),\qquad d'=d-u-v\ge d-2M\sim TL/(2\pi).
\tag{5}
\]

Thus the weakest sufficient density condition supplied by this **bound** is

\[
\frac{\gamma_Td'}{(1+S)\log d}\longrightarrow\infty.
\tag{6}
\]

The (1) includes the scalar-background term and (s_0\to1). At the frozen natural cutoff,

\[
\frac{(1+S)\log d}{d'}
=O\!\left(\frac{\log d}{TL}+\frac{\sqrt N\log d}{TL^2}\right)
=O\!\left(\frac1T+\frac{e^{-\sqrt L/2}}{\sqrt{2\pi T}\,L}\right).
\tag{7}
\]

Here (log d\sim L), (N\sim Xe^{-\sqrt L}), and (d'\sim TL/(2\pi)). The second term dominates the sufficient rate for large (T), but both are displayed. A fixed positive density such as (3) satisfies (6), and (5) is (o(1)). This is a sufficient scale for the absolute estimate, not a necessary condition on the actual signed boundary correction.

The inherited analytic estimates state (C_R,C_B) as (O_R(1)) constants rather than explicit numerical values. Accordingly, the density (1/4) and all scale rates here are explicit; the final absolute boundary error remains an asymptotic (O_R(\cdot)) bound with those source constants.

## 5. Source scope, masks, and obligations left open

The direct first-strike section requirement is an existential common contiguous section with bounded finite endpoint feature scores; inequality (12) is a separate signed arithmetic gate on that same section. Its direct formulation has no external `source_mask` callback. The source-matched arithmetic reduction also states that no unique historical selector or determinant row tuple is a premise.

The hidden-prime/block-determinant auxiliary has different semantics: its full-pool (R=6000) iterator requires the exact callback `source_mask(fid,slots,lag,T,section,alias)` and source-selected rows. The good-endpoint theorem gives no identity from its generic (a_n(\theta)) features to those masked atoms, their root sums, height/alias data, or normalization. The existing determinant-compatibility audit correctly fails that transfer. **This D2 result must not be cited as a density theorem for that masked determinant consumer.**

The following remain open: actual uniform sixth Schatten moment and raw-cubic deletion stability; signed fifth/sixth gate; prime-to-Weil identification; zero-side block/tail-Weyl transfer; (m_3=2); actual conditioned Cayley energy below (0.105); and strict (>79\%\).

## 6. Replay scope

Run:

```powershell
python src/wp84_decision_d_endpoint_admissibility.py
python src/wp84_decision_d_endpoint_admissibility_replay.py
```

The deterministic tests include boundary mass concentrated entirely on
admissible pairs, shrinking-density saturation, score/energy anticorrelation,
nonuniform-weight mismatch, and a coupled-pair gate whose good marginals do
not imply a positive pair density. These are abstract arithmetic stress
tests, not prime-field configurations. The source conclusion comes from
(1)--(7) and the stated source score hypotheses, not from those finite tests.
