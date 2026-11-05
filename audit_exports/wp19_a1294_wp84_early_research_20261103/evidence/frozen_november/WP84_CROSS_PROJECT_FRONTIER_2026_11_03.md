# WP84 cross-project mathematical frontier audit

**Date:** 2026-11-03
**Research branch:** `codex/cross-project-math-frontier-20261103`
**Audit base:** `8cac9051c8bd94568d3010f5c08a44dc975ee668`
**Frozen baseline:** `7f3394c5655238b1e9736f91233d0bcc4c49fd43` (ancestor of the audit base)
**Scope:** source lineage, one independently stated WP84 theorem, and whether the Navier–Stokes methods yield a new ordinary-prime estimate. This note changes no historical source or result.

## Decisions

| Gate | Decision | What the evidence supports |
|---|---|---|
| `NAVIER_TO_WP84_LINEAGE` | **PARTIAL** | The published/currently accessible NS bridge source and its connection to the prior WP84 audit were checked. The accessible GitHub repository is reported as public; no distinct private NS checkout was available to verify as the user's intended repository. The mathematical methods do not transfer an estimate. |
| `SMOOTH_POWER_THEOREM_SOURCE_LOCK` | **COMPLETE** | The proper-prime-power summand is source-matched under the stated taper and section hypotheses. A finite-cutoff equality in the earlier proof note is corrected here to an inequality; the asserted bounds remain valid. |
| `TRANSFERABLE_ANALYTIC_IDENTITY` | **NONE_FOUND** | The Hermite adjoint/telescoping algebra replays exactly, but its required actual-source signed-flux estimate is open. NS skew-transport cancellation has no WP84 operator identity. |
| `NEW_ORDINARY_PRIME_REDUCTION` | **NONE_FOUND** | No new source-valid cancellation or norm saving for the physical 26-term ordinary-prime connected aggregate was found. |
| `COUNTEREXAMPLE_STATUS` | **NONE_FOUND** | No source-admissible ordinary-prime aggregate counterexample was found. The preserved positive physical atom is proper-prime-power data. Abstract obstructions are not source counterexamples. |
| `NEXT_THEOREM_TARGET` | **NO_VALID_TARGET** | Freeze the cross-project route. The unresolved source inequality is recorded in §3. |

These decisions make no claim about the R400 consumer, a strict greater-than-79% theorem, or RH. Those remain open as recorded in the predecessor audits.

## 1. One selected theorem: smooth proper-power Schatten absorption

Let $L\ge1$, $X=e^L$, and $h=2\pi/L$. Let $\phi_L$ be real and even, supported on an interval of length $L$, with
\[
\|\phi_L\|_\infty\le B,\qquad a_L=L^{-1}\|\phi_L\|_2^2\ge a_0>0.
\]
For each $y\in[0,L]$, define the zero-extension, non-wrapping compressed shift
\[
B_y=P_dM_{\phi_L}U_y^+M_{\phi_L}P_d,
\]
where $P_d$ projects onto source Fourier modes $0\le k<d$, $d=\lfloor e^LL\rfloor$. For a consecutive principal section $I\subseteq\{0,\ldots,d-1\}$ of length $m\ge\eta e^LL$, $0<\eta\le1$, define $Q_I$ as the compression of the proper-prime-power part of the exact source prime-side matrix. Then, with $c_0=1-2^{-1/2}$,
\[
\tau_I(Q_I^2)\le \frac{256B^2}{a_0L^2}\left(1+\frac2\eta\right),\qquad
\|Q_I\|_{op}\le\frac{12B^2\log2}{a_0c_0}.
\]
Assume additionally $\phi_L\in C_c^2(\mathbb R)$, as in the source. This regularity is needed for the Weil-matrix identity, not for the operator estimates.

Consequently,
\[
\tau_I(Q_I^4)=O_{a_0,B,\eta}(L^{-2}),\qquad
\left|\tau_I((A_I+Q_I)^4)^{1/4}-\tau_I(A_I^4)^{1/4}\right|
=O_{a_0,B,\eta}(L^{-1/2})
\]
for every Hermitian $A_I$. The second statement is a normalized Schatten-4 fourth-root perturbation bound; it is not a raw fourth-trace difference. No bound on $\tau_I(A_I^4)$ or $\tau_I((A_I+Q_I)^4)$ is assumed.

### Source matching and normalization

Alpöge–Furman, arXiv:2608.13637v2, §§2.1–2.3, defines
\[
\phi_L(x)=\chi(L/2+x)\chi(L/2-x)\sqrt{\psi(x/L)},\quad
L=\log(T/2\pi),\quad X=e^L=T/(2\pi),\quad \alpha_k=T+2\pi k/L.
\]
The paper's two windows are $\psi_0=\mathbf1_{[-1/2,1/2]}$ and $\psi_{MT}(s)=\cos(\sqrt2s)\mathbf1_{[-1/2,1/2]}(s)$. Its exact normalization is
\[
a_L=\|\phi_L\|_2^2/L=\int_{-1/2}^{1/2}\psi(s)\,ds+O_\chi(L^{-1}).
\]
Thus $a_L\to1$ for $\psi_0$; for $\psi_{MT}$, $a_L\to\sqrt2\sin(1/\sqrt2)$, not $1$. Both have $B=1$ and an eventual source-valid lower bound $a_L\ge1/2$. No argument below replaces the source taper by a sharp box.

For the audited WP84 principal interval, $m\ge d-2q$ with $q=\lfloor d/\sqrt L\rfloor$ and $d=\lfloor e^LL\rfloor$. When $L\ge16$ and $e^LL\ge2$, this gives $m\ge e^LL/4$, so the actual selected section satisfies the theorem with $\eta=1/4$ eventually.

For $f_y(x)=\phi_L(x-y/2)\phi_L(x+y/2)$, define
\[
G_r(y)=\frac1{a_LL}\int_{\mathbb R}f_y(x)e^{ihrx}\,dx.
\]
Then
\[
|G_r(y)|\le1,\qquad \sum_{r\in\mathbb Z}|G_r(y)|^2
=\frac1{a_L^2L}\int |f_y(x)|^2dx\le\frac{B^2}{a_L}.
\]
The entry identity, for $l=k+r$, is
\[
(Q)_{k,k+r}=\sum_{p^e\le X,\ e\ge2}\lambda_{p^e}G_r(\log p^e)
\left(e^{iT\log(p^e)}e^{ih(k+r/2)\log(p^e)}+
e^{-iT\log(p^e)}e^{-ih(k+r/2)\log(p^e)}\right),
\quad \lambda_{p^e}=-\frac{\log p}{L p^{e/2}}.
\]
This is the proper-power part of the original matrix, with both carrier branches and the source normalization retained. Principal compression is literal zero-extension compression, so no boundary wrap term appears.

### Finite-cutoff correction to the earlier proof note

The earlier note wrote an equality after extending the exponent sum to infinity. At finite $X=e^L$, the exact identity is instead
\[
\sum_{p^e\le X,\ e\ge2}|\lambda_{p^e}|^2
=\frac1{L^2}\sum_{p\le\sqrt X}(\log p)^2
\sum_{e=2}^{\lfloor L/\log p\rfloor}p^{-e}
\;\le\;\frac1{L^2}\sum_p\frac{(\log p)^2}{p(p-1)}
\;\le\;\frac{64}{L^2}.
\]
An empty inner sum is zero. The first inequality is the finite geometric-series bound $\sum_{e=2}^{E}p^{-e}\le1/[p(p-1)]$. For the last inequality, $\log p\le4p^{1/4}$, $p(p-1)\ge p^2/2$, and $\sum_{n\ge2}n^{-3/2}\le2$ give $32\sum_{n\ge2}n^{-3/2}\le64$. The erroneous equality is not needed. All later constants in the second-trace, operator, fourth-trace and Schatten-root conclusions continue to follow.

### Proof dependencies and independent check

For $u_n=\log n/L$ in the proper-power set, $n\ge4$. If $m<n\le X$, then
\[
u_n-u_m=\frac{\log(n/m)}L\ge\frac1{(N+1)L},\quad N=\lfloor X\rfloor,
\]
and the complementary circular gap is
\[
1-(u_n-u_m)=\frac{\log(Xm/n)}L\ge\frac{\log4}{L}.
\]
Thus each sign branch separately is circularly $\delta$-separated with $\delta\ge((N+1)L)^{-1}$, including the endpoint alias if $X=N$ and $n=X$. Montgomery–Vaughan Theorem 1 (Mathematika 20 (1973), 119–134) applies to arbitrary complex coefficients at distinct points modulo one. Duality gives the consecutive-row bound
\[
\sum_{k\in I}\left|\sum_n b_ne^{2\pi iku_n}\right|^2\le(m+\delta^{-1})\sum_n|b_n|^2.
\]
The arbitrary start row changes $b_n$ only by unit phases. With $m\ge\eta e^LL$, $1+\delta^{-1}/m\le1+2/\eta$. The positive and negative branches are estimated separately and combined by $|S^++S^-|^2\le2|S^+|^2+2|S^-|^2$, giving factor $4$. Parseval sums all displacements, yielding $256B^2(a_LL^2)^{-1}(1+2/\eta)$. The full-operator row uses $\|B_y\|_{op}\le B^2$, coefficient absolute mass, Chebyshev's bound $\theta(x)\le4(\log2)x$, and partial summation. Finally $\tau(Q^4)\le\|Q\|_{op}^2\tau(Q^2)$ and the normalized Schatten-4 triangle inequality yield the claimed conclusions.

The accessible original source states the taper, normalization, finite Weil matrix and prime-side identity at equations (2.7), (2.10)–(2.11) and Lemma 2.1. The applicable classical inequality is the separated-point theorem, not a claim that the prime-power frequencies themselves have a special arithmetic cancellation. The proof uses fixed $a_0,B,\eta$; constants are independent of $T$, section start and endpoints. The local regression suite passed 8/8 in normal, optimized, and doubly optimized Python. The exact cross-project Hermite replay also passed in all three modes, while printing consumer_certified=false and actual_prime_bound_available=false.

## 2. Cross-project source connections and limits

The checked Navier–Stokes source has several mathematical mechanisms, but none supplies the missing ordinary-prime bound:

* **WP3 small-data energy:** the proposition assumes $\nu-C_0\sqrt{G_0}>0$, uses real divergence-free Galerkin solutions and the periodic energy identity, then proves an invariant region, decay and integrated dissipation. It is a small-data theorem and has no input matching the static prime coefficient/cumulant array.
* **WP11 commutator:** skew-adjointness of divergence-free transport yields a whole-form squared-symbol difference with factor $-1/2$; the fixed low-advector estimate is proved at $\sigma=0$, $s>3/2$. The signed high-advector/time-integrated estimate is explicitly open. WP84 has no source identity representing its 26-term physical cumulant as this transport commutator; importing that sign would be invalid.
* **WP19 cutoff shell and adjoint:** the direct same-state low-output shell couples only to a boundary annulus and has a summable $O(M^{-2})$ increment. Recursive state drift remains open. The v0.24/v0.26 Hermite-adjoint work retains nonlinear and endpoint remainders; v0.26 is a floating pre-interval gate. Those hypotheses concern a Galerkin trajectory and do not control $pq\ne rs$ prime products.
* **WP84 Hermite transplant:** the finite rational algebra is real and reproducible. The replay's rank-zero/spatial and signed-flux obstructions, including flux $-5/16$, falsify a universal implication from displacement rank alone. They are generic algebra countermodels, not counterexamples to the source prime inequality. The required uniform actual-state signed dual-flux lemma remains open.
* **Schatten/energy:** the proper-power summand has the source-matched result above. The known diagonal-matrix countermodel shows that normalized second-mass control alone cannot yield a fourth-moment bound. The proper-power operator-norm input resolves that issue only for $Q$, not for the ordinary-prime matrix $A$.
* **Physical/geometric kernels and endpoints:** prior WP84 audits preserve the positive physical atom and physical/geometric kernel mismatch. At $v=(1/5,-2/5,3/5,-2/5)$, the public nested-overlap bracket is $B_{4,nc}=0$ and $O_A=2/5$, while the physical row cumulant satisfies $\kappa_m\ge384/625>0$ for the selected sections and the R400 physical atom is $>9588/78125$. Its tuple $(p,p^2,p^3,p^2)$ has one ordinary-prime slot and three proper powers, so it is not an ordinary-prime-only counterexample. Its complete one-base family is separately $O_R(L^{-4})$. Endpoint/tensor identities are exact bookkeeping identities, but no source-weighted error estimate makes their correction small for the complete ordinary-prime array.

The accessible GitHub metadata reports `reggaesharkk/navier-stokes-bridge-audit` as **public**. I did not find a separate private NS checkout; therefore repository identity and any unexposed private changes are not verified. The NS source commit used here is `def4df60b0ebdce8b0c99cea6006eb2905e0e02f`. The relevant proof files have the same Git blob IDs as the historical pin `4790a7edbabdcc8f4bdf1bde1c67b44f0ccc238f`, so these particular files are byte-identical across those two commits. A local v0.29.1 extraction exists in another worktree but has no `.git` metadata and is treated as an archive, not a verified current checkout.

## 3. Ordinary-prime frontier: no source-valid reduction

The actual target remains the complete pair-subtracted physical row cumulant with all 26 ordered partitions, six balanced orientations, original coefficients, section-dependent averages, root corrections, near-product pairs $A=pq\ne B=rs$, and aliases. The exact $A=B$ pair layer has already been treated separately. The existing reports establish neither a signed upper bound nor a source-valid positive-part estimate for the remaining aggregate. The prior near-product norm and endpoint-correction routes do not create an arithmetic saving; the Hermite replay does not change that.

The smallest sufficient unresolved statement remains either a common admissible section $I_T$ with
\[
\Re C^{ord}_{T,I_T}<\Delta_{\max}+o(1),\qquad
\Delta_{\max}=\frac{3675673694911}{148250000000000},
\]
and every other consumer condition, or the previously recorded joint-selection sufficient estimate
\[
\limsup_{T\to\infty}\mathbb E_{I\in\mathcal G_T}
\bigl[(\Re C^{ord}_{T,I})_+\bigr]
< (1/4-\epsilon)\Delta_{\max}
\]
for one fixed $\epsilon>0$, with the source-defined admissible set and its actual measure. Signed mean, mean positive part, and an individual-section bound are distinct. No NS result provides this estimate, and no new exponent, major-arc saving or kernel cancellation was found. Thus the stronger positive-part statement remains the precise old debt, not a proved consequence of this audit.

The prior local record still controls the proper-power family and preserves the physical positive atom, while the ordinary-prime connected aggregate, complete product-frequency endpoint selection, R400 record budget, conditional 68.820273% route, strict greater-than-79% claim and RH remain open/conditional as previously labeled. The public Riemann verification repository is a separate source; its status likewise treats the historical percentage routes as conditional and the arithmetic/normalization transfers as open. No public or model benchmark was used to decide the private aggregate.

## 4. Literature and publication-priority assessment

The selected proper-power theorem is an application of the classical Montgomery–Vaughan separated-point large sieve, Cauchy–Schwarz/Parseval, Chebyshev's estimate, Schur compression, and Schatten inequalities to the actual smooth finite source matrix. Its source-matched packaging is checkable, but no new large-sieve theorem or publication novelty follows. The NS energy/commutator arguments are standard within their stated PDE hypotheses; their transport symmetry and coercive viscosity have no demonstrated WP84 counterpart. The Poisson–Gabor source identity is part of Alpöge–Furman's paper, while the finite endpoint and tensor identities in WP84 are exact finite algebra and are not claimed as novel. The physical/geometric discrepancy is an important correction/control result inside this audit chain, not by itself an ordinary-prime theorem.

Priority for independent review: (1) the corrected source-level proper-power Schatten note, as a self-contained lemma under explicit hypotheses; (2) the finite physical/geometric kernel comparison and positive atom, with their strict scope limitations; (3) endpoint/tensor identities as reproducibility aids. Publication novelty is **not established**. A literature review specifically supporting novelty has not been performed.

## 5. Reproduction and falsification instructions

From the repository root, use Python 3.12.10. The exact Hermite replay uses SymPy 1.14.0; mpmath 1.3.0 is installed but not used by these checks.

```powershell
python -B -m unittest -v tests.test_wp84_direct_smooth_power_absorption
python -O -B -m unittest -v tests.test_wp84_direct_smooth_power_absorption
python -OO -B -m unittest -v tests.test_wp84_direct_smooth_power_absorption
python -B -m unittest -v tests.test_wp84_physical_kernel_reconciliation
python -O -B -m unittest -v tests.test_wp84_physical_kernel_reconciliation
python -OO -B -m unittest -v tests.test_wp84_physical_kernel_reconciliation
python -B src/wp84_cross_repository_hermite_adjoint.py
python -O -B src/wp84_cross_repository_hermite_adjoint.py
python -OO -B src/wp84_cross_repository_hermite_adjoint.py
```

The smooth-power command family reports 8 tests passing in each mode; the physical/geometric reconciliation family reports 5 in each mode. `pytest` is not installed in the inspected Python 3.12 environment; the tests use standard `unittest`, so no test dependency is needed. The Hermite run reports exact rational algebra status `PASS`, `consumer_certified=false`, and `actual_prime_bound_available=false`. To falsify the selected theorem, check the finite (p^e\le X) sum above against the infinite geometric majorant, include the two Fourier branches separately, test a section at its minimum allowed length and arbitrary start, and check — rather than assume — the source taper normalization. A successful finite replay is not evidence for any ordinary-prime asymptotic.

## 6. Preserved failures and scope

No earlier source, certificate, audit decision, branch, or commit was edited. The only mathematical correction introduced here is the finite-cutoff equality-to-inequality correction displayed above. The original proof note remains unchanged for provenance. This audit does not certify an ordinary-prime sign, a new R400 bound, an unconditional percentage theorem, or RH.
