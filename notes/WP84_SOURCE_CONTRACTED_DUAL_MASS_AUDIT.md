# WP84 source-contracted dual-mass audit

**Decision E — source information is insufficient to instantiate the proposed dual masses.** The contour and prime-mass lemmas survive replay, but the arrays whose norms define (D_{1,T}) and (D_{2,T}) are not executable in the checked-in source. No source-legal counterexample is established. The fixed-(R) comparison and strict (>79\%) remain **OPEN**.

The audit starts at local commit `93959b4e429d7bc02aaec8fd535acf2075bd877b` on `codex/c5-c6-attack-20261006`. It preserves (K=32), (delta=10^{-5}), the natural cutoff (N=\lfloor X e^{-\sqrt{\log X}}\rfloor), fixed (R) followed by (T\to\infty), full prime-power grouping, and the common trace index. It does not modify the prior contour or firewall sources.

## What the prior replays establish

All three requested independent replays passed before this audit:

- The contour-mixture replay checked its stated rational formulas, rejected 12 mutated certificates, and verified 9 source hashes.
- The fixed-pole response replay checked its rational constants, rejected 22 mutations, verified 10 source hashes, and retained the open aggregate response mass.
- The prime-adic firewall replay checked its rational frequency/cutoff/kernel example, source hashes, and 21 hostile-inference evidence checks.

Those are finite identity, integrity, and evidence-boundary checks. They do not evaluate (D_{1,T}), (D_{2,T}), or prove a limit as (T\to\infty).

## Source-completeness findings

The prior contour note gives formal templates for
\[
K_{1,p,\nu}=\frac1{d'}\sum_{k\in I}e^{i\tau_k\lambda_\nu}
 \sum_{a,\epsilon}\Gamma_{p,a,\epsilon}(k)e^{i\tau_k\epsilon a\log p}
\]
and the corresponding double sum for (K_{2,p,\nu}), with only the exact opposite-sign (a=b) covariance diagonal removed. In the producer, these definitions are **string-valued certificate fields**; no routine constructs the contracted tensors or sums them numerically. The revised certificate therefore treats them as symbolic placeholders, not evaluated source coefficients.

The available source records the following partial definitions:

| Object | Evidence status | Boundary |
|---|---|---|
| (\mathcal K_I(\omega)=d'^{-1}\sum_{k\in I}e^{i(T+2\pi k/L)\omega}) | Closed formula, evaluable for supplied (I,d',T,L) | No executable selected-section/root-selector object is attached to the dual-mass computation. |
| Ordinary-prime (V_p(K)) | Formula in `WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md` | It is prose, and it does not instantiate every grouped proper-power coordinate or the requested source gates. |
| Proper-power blocks (B_{p^a}) | Grouped at base (p); the envelope (4\log p/(L p^{a/2})) is recorded | Full coordinate tensors, lag/root factors and row-gate values are not enumerated as executable arrays. |
| (\Gamma_{p,a,\epsilon}(k)) | Symbolic source-tensor placeholder | No checked-in constructor supplies the row-specific masks/gates and root/path contractions. |
| Response coefficients (c_{1,p,\nu},c_{2,p,\nu}) | Uniform analytic and Parseval bounds are certified | The actual full-pool Fourier arrays and a contraction against them are not generated. |
| Selected (I,d') | (I,d') appear as parameters in the kernel formula | No serialized selected rows/endpoints/order and root-count map are inputs to the dual-mass producer. |

There is a `source_mask(...)` callback required by the separate full-pool determinant atom iterator in `src/wp84_fifth_full_pool_amplitude.py`, but no implementation is checked in. That callback is not automatically the mask for the fixed-(R) Lindeberg vector; this audit does not transfer it between objects. Likewise, the carrier convention must be resolved from the actual row tensor before an implementation can guarantee that the factor (e^{iT\omega}) occurs exactly once.

## What follows from the documented bounds

The contour-mixture identity itself is sound. For each finite Fourier set, integrate shifted Parseval against one probability measure on the feasible contour body; monotone convergence extends the nonnegative sum. Independent contour signs yield
\[
W_\rho(\nu)=\prod_q\cosh(2\rho_q\nu_q)
\ge 2^{-\lvert\operatorname{supp}\nu\rvert}
 e^{2\sum_q\rho_q|\nu_q|}.
\]
The mixture does not multiply Parseval’s right-hand side by (2^{|S|}), but the reciprocal dual weight retains the support penalty. On a finite truncation (D_\mu(k)) is convex in the common measure and an optimizer can be supported on at most (|F|+1) contours. That finite result does not certify a uniform infinite-index limit.

The grouped block bound yields
\[
g_p=\frac{4\log p}{L(\sqrt p-1)},\quad
\max_pg_p=O(L^{-1}),\quad
\sum_{p\le N}g_p^2=8+o(1),\quad
\sum_pg_p^3=O(L^{-3}),\quad
\sum_pg_p^4=O(L^{-4}).
\]
The square-mass leading constant uses the stated PNT partial-summation input; the cubic and fourth prime series converge absolutely.

Consequently, **conditional on actual source-contracted kernels being constructed**, the previous Hilbert inequalities imply
\[
|A_1|\le M_{1,R}\sqrt{8+o(1)}\sqrt{D_{1,T}},\qquad
|A_2|\le \frac{M_{2,R}}2\sqrt{C_4}\,L^{-2}\sqrt{D_{2,T}},
\]
where
\[
M_{1,R}=\frac{43212226464}{16375},\quad
M_{2,R}=\frac{166449403229184}{429025},\quad
C_4=256\sum_p\frac{(\log p)^4}{(\sqrt p-1)^4}<\infty.
\]
Thus (D_{1,T}=o(1)) and (D_{2,T}=o(L^4)) are sufficient. They are still **unproved**; the replay does not turn these assumptions into estimates.

The exact (m=0) current-base resonance is excluded for nonzero residual current exponent (r) by (p)-adic valuation. Nonzero periodic aliases remain possible; the primorial (m=1) family is a frequency label, not proof of a nonzero source coefficient. Near-alias kernels can have order-one modulus in an (O(1/T)) window. Far-frequency geometric decay is pointwise only; no source-weighted sum is certified. The independent-Haar cancellations do not establish orthogonality on the shared trace-index path.

## Hostile checks and evidence boundary

For the explicit sign-mixture schedule with (s=\pi(N)-1) coordinates and (\rho_q=\eta\log q), (eta=\min(1/4,131L/(51200s))), the contour cost is feasible. As (N\to\infty), (eta\log N\to0). Therefore
\[
\sum_{\nu\in\mathbb Z^S}\frac1{W_\rho(\nu)}
=\prod_{q\in S}\sum_{n\in\mathbb Z}\operatorname{sech}(2\rho_q n)
\ge (1+2\operatorname{sech}2)^s\longrightarrow\infty.
\]
This rigorously defeats the **trivial** route that substitutes only 
\(|\mathcal K_I|\le1\) and then sums reciprocal weights for this schedule. It does not show that the actual kernel-weighted (D_1) or (D_2) diverges, and does not show that every contour measure fails.

The prior adversarial high-degree atom still falsifies an inference from unweighted (L^2) coefficient control alone. It is not an actual response coefficient and not a source-legal counterexample to (D_1) or (D_2). The primorial alias, growing-support multiplicity, actual row-mask cancellation, and a uniform majorant for optimized measures remain **UNKNOWN** where the source tensors are absent.

Finite Parseval sums pass to the all-index weighted-energy sum by monotone convergence. To pass the source pairing, its dual mass must be finite for the truncations. No estimate uniform in (T) currently permits the further exchange with (T\to\infty).

## Decision and first missing input

**Decision E.** The first missing input is an executable fixed-(R) source constructor that supplies: (1) every (p^a\le N) realified current tensor with exact normalization and one-time carrier convention; (2) row-dependent source masks/gates and root/path sums; (3) the selected-section row identities/order, (d'), and root-count/endpoint data; and (4) either the actual response Fourier coefficients or an executable contraction that avoids materializing them. Until that source object is supplied, the actual (K_{1,p,\nu}), (K_{2,p,\nu}), (D_{1,T}), and (D_{2,T}) cannot be independently instantiated. No uniform theorem over an unspecified admissible mask/section class and no source-legal counterexample is claimed.

After source recovery, the first analytic theorem is exactly to prove, for each fixed (R) and uniformly over the allowed sections,
\[
D_{1,T}=o(1),\qquad D_{2,T}=o(L^4),
\]
with nonzero periodic, near, intermediate and far frequencies retained and only the justified covariance diagonal removed. Strict (>79\%) remains **OPEN**.

## Reproduction

```powershell
python src/wp84_source_contracted_dual_mass_audit.py
python src/wp84_source_contracted_dual_mass_audit_replay.py
python src/wp84_contour_mixture_prime_mass_replay.py
python src/wp84_analytic_response_trace_grid_transfer_replay.py
python src/wp84_dependent_phase_prime_adic_firewall_replay.py
```

The new replay checks source hashes, distinguishes strings from executable
constructors, independently checks the finite reciprocal-weight failure for
the trivial schedule, and rejects hostile certificate mutations. It does
not assert an actual zeta-side counterexample or asymptotic limit.
