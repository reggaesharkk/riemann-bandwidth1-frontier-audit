# WP84 contour-mixture and current-prime mass audit

**Decision C — a sharper, source-weighted reduction; A1 and A2 remain open.**
Probability mixtures remove the artificial (2^{|S|}) factor from the
Parseval right side, and the exact grouped source block has fourth prime mass
(O(L^{-4})). The corresponding dual masses have not been estimated, so
neither arithmetic term is closed. Strict (>79\%) remains **OPEN**.

This audit continues from local commit
`90af6336111e822e67df4eabaa534fbb78fd9360` on
`codex/c5-c6-attack-20261006`. It keeps (K=32),
\(\delta=1/100000\), (N=\lfloor X e^{-\sqrt{\log X}}\rfloor\), fixed
(R) followed by (T\to\infty), all grouped prime powers at their base,
the common trace index and carrier phases, and the current-prime exclusion
from (Y_p). It does not replace the trace-grid law by independent Haar
phases.

## 1. The contour-mixture lemma

Let (S) be a finite set of prime coordinates and let
\[
\mathcal B_S=\{s\in\mathbb R^S:\sum_{q\in S} B_q(|s_q|)\le\theta a\},
\quad \theta a=131/400,
\]
be the feasible contour body from the preceding fixed-pole certificate. For
each feasible (s), shifted-torus Parseval gives
\[
\sum_{\nu\in F}e^{2s\cdot\nu}\,\|c_\nu\|_{\mathcal H}^2\le M_{j,R}^2
\tag{1}
\]
for every finite set (F\subset\mathbb Z^S), with
\(\mathcal H=L^2(g)\) and (j=1,2). If (\mu\) is any probability measure
on (\mathcal B_S), integrate (1). The sum is finite, so interchange is
immediate and
\[
\sum_{\nu\in F}W_\mu(\nu)\|c_\nu\|_{\mathcal H}^2\le M_{j,R}^2,
\qquad W_\mu(\nu)=\int_{\mathcal B_S}e^{2s\cdot\nu}\,d\mu(s).
\tag{2}
\]
Exhaust the countable Fourier lattice by increasing finite sets and apply
monotone convergence to the nonnegative summands. This proves (2) for the
whole lattice. No factor is charged to the right side by probability
averaging.

For a fixed feasible nonnegative radius vector \(\rho\), put equal mass on
the \(2^{|S|}\) contours \(s_q=\epsilon_q\rho_q\), with independent
uniform signs. Finite product expansion gives exactly
\[
W_\rho(\nu)=\prod_{q\in S}\frac{e^{2\rho_q\nu_q}+e^{-2\rho_q\nu_q}}2
             =\prod_{q\in S}\cosh(2\rho_q\nu_q).
\tag{3}
\]
For every real (x), \(\cosh x=\frac12 e^{|x|}(1+e^{-2|x|})\), hence
\[
W_\rho(\nu)\ge 2^{-\lvert\operatorname{supp}\nu\rvert}
                  e^{2\sum_q\rho_q|\nu_q|}.
\tag{4}
\]
Thus random signs remove the sign choice from a common mixture and preserve
the Parseval bound, but the reciprocal dual weight still carries a
support-size penalty. This is a genuine limitation of the pointwise
comparison, not a reason to multiply the Parseval right side by
\(2^{|S|}\).

For a finite Fourier truncation (F), weighted Hilbert duality now gives
\[
\left|\sum_{\nu\in F}\langle c_\nu,k_\nu\rangle\right|
 \le M_{j,R}\left(\sum_{\nu\in F}
                 \frac{\|k_\nu\|^2}{W_\mu(\nu)}\right)^{1/2}.
\tag{5}
\]
For a fixed full source expression, (5) passes to its Fourier limit only when
the source pairing has been justified (for example, first by the uniformly
convergent finite-dimensional Fejer approximants and then by a finite-
section limit). The inequality itself does not assert that the full dual
sum is finite.

## 2. One common measure per finite truncation

For (F\) finite, write
\[
D_\mu(k)=\sum_{\nu\in F}\frac{\|k_\nu\|^2}{W_\mu(\nu)}.
\]
Every (W_\mu(\nu)) is affine in \(\mu\), positive, and bounded away from
zero on the compact feasible contour body for fixed (F). Since (x\mapsto
1/x) is convex on (x>0), (D_\mu(k)) is convex in \(\mu\). Compactness
gives a minimizing measure. If \(|F|=n\), the vector
\((W_\mu(\nu))_{\nu\in F}\) lies in the convex hull of the compact feature
curve \(s\mapsto(e^{2s\cdot\nu})_{\nu\in F}\subset\mathbb R^n\).
Caratheodory's theorem therefore gives an optimizer supported on at most
\(n+1\) feasible contours with the same vector and objective value.

This is an existence theorem for a **single common measure** on a finite
truncation. No measure was numerically optimized here, and no separate
pointwise optimizer is substituted for each \(\nu\). A sequence of finite
truncation optimizers need not converge to a useful optimizer for the full
infinite dual mass.

## 3. Exact grouped current-prime mass

The source block bound, with the matrix/operator and path factors included,
is
\[
\|B_{p^a}\|\le \frac{4\log p}{L p^{a/2}},\qquad p^a\le N.
\]
Group all powers at the common base phase and use the triangle inequality
only inside this finite local group. The following infinite geometric
envelope is valid:
\[
g_p:=\frac{4\log p}{L}\sum_{a\ge1}p^{-a/2}
    =\frac{4\log p}{L(\sqrt p-1)},\qquad \|V_p\|\le g_p.
\tag{6}
\]
The extension to all (a\ge1) only enlarges the retained finite sum.

The function \(x\mapsto\log x/(\sqrt{x}-1)\) decreases for (x\ge2\),
so
\[
\max_{p\le N}g_p\le\frac{4\log2}{L(\sqrt2-1)}=O(L^{-1}).
\tag{7}
\]
Also
\[
\frac1{(\sqrt p-1)^2}=\frac1p\left(1+O(p^{-1/2})\right),
\]
and PNT partial summation yields
\[
\sum_{p\le N}g_p^2
 =\frac{16}{L^2}\sum_{p\le N}\frac{(\log p)^2}{(\sqrt p-1)^2}
 =8+o(1),
\tag{8}
\]
because \(\log N=L-\sqrt L+o(1)\) and
\(\sum_{p\le N}(\log p)^2/p\sim(\log N)^2/2\). The error series
\(\sum_p(\log p)^2/p^{3/2}\) converges.

For (k=3,4), the prime series
\(\sum_p(\log p)^k/(\sqrt p-1)^k\) converges (its terms are
\(O((\log p)^k/p^{k/2})\), with exponent (k/2>1\)). Hence
\[
\sum_{p\le N}g_p^3=O(L^{-3}),\qquad
\sum_{p\le N}g_p^4=O(L^{-4}).
\tag{9}
\]
The fourth-mass claim is stronger than (O(L^{-2})). It is about the
complete grouped source block; it does not delete proper powers from A1.

## 4. Exact grouped kernels and Hilbert reductions

Write \(\Gamma_{p,a,\epsilon}(k)\) for the **actual realified source
coefficient tensor** of the current power (p^a), including lag/root/path
factors, masks, conjugate coefficient, and any source gate depending on the
sampled row. The oscillatory trace carrier is displayed separately below
and occurs exactly once. Let
\(\lambda_\nu=\sum_{q\ne p}\nu_q\log q\) and retain the actual selected
section kernel
\[
\mathcal K_I(\omega)=\frac1{d'}\sum_{k\in I}
 e^{i(T+2\pi k/L)\omega}.
\]
After contracting the source tensor with the response coordinate, the
grouped A1 kernel at ((p,\nu)) is exactly
\[
K_{1,p,\nu}=\frac1{d'}\sum_{k\in I}e^{i\tau_k\lambda_\nu}
 \sum_{a:p^a\le N}\sum_{\epsilon=\pm1}
 \Gamma_{p,a,\epsilon}(k)e^{i\tau_k\epsilon a\log p},
\tag{10}
\]
where (\tau_k=T+2\pi k/L) and every conjugate is included once. When the
coefficient is row-independent, this reduces to the original geometric
kernel (\mathcal K_I(\lambda_\nu+\epsilon a\log p)); this displayed
average also covers row-dependent source gates without silently factoring
them out. It uses the original source coefficients and does not replace
masks or root sums by scalar absolute values. It aggregates powers and signs
before taking its norm. If the source's full vector tensors are instantiated,
the pairing is
\(A_1=\sum_{p,\nu}\langle c_{1,p,\nu},K_{1,p,\nu}\rangle\), first on
finite Fejer truncations.

For A2 define before its global factor (1/2)
\[
K_{2,p,\nu}=\frac1{d'}\sum_{k\in I}e^{i\tau_k\lambda_\nu}
 \sum_{\substack{a,b:p^a,p^b\le N\\
                   (a,b,\epsilon,\epsilon')\notin\mathcal D_p}}
 [\Gamma_{p,a,\epsilon}(k)\otimes\Gamma_{p,b,\epsilon'}(k)]
 e^{i\tau_k(\epsilon a+\epsilon'b)\log p},
\tag{11}
\]
where \(\tau_k=T+2\pi k/L\) and \(\mathcal D_p\) consists **only** of the opposite-sign equal-power
terms \(a=b,\epsilon'=-\epsilon\) that are subtracted by the exact
\(\Sigma_p\). Every other same-base pair, same-sign pair, and unequal
opposite-sign pair remains. Then
\(A_2=\frac12\sum_{p,\nu}\langle c_{2,p,\nu},K_{2,p,\nu}\rangle\).

Equations (10)–(11) make explicit where the exact source masks, tensor
directions and carrier phases enter. The checked-in source descriptions
specify those as part of \(\Gamma\); they do not provide a ready finite
numeric table of all selected-section tensors. No such table is fabricated
here. The geometric kernel is retained at every frequency.

For each (p), use a feasible probability measure \(\mu_p\) on the response
contour body. Applying (5) within each (p), then Cauchy across (p),
gives the valid finite-truncation bounds
\[
|A_1|^2\le M_{1,R}^2\left(\sum_p g_p^2\right)D_{1,T},\qquad
D_{1,T}=\sum_{p,\nu}\frac{\|K_{1,p,\nu}\|^2}
                              {g_p^2 W_{p,\mu_p}(\nu)},
\tag{12}
\]
and
\[
|A_2|^2\le\frac14M_{2,R}^2\left(\sum_p g_p^4\right)D_{2,T},\qquad
D_{2,T}=\sum_{p,\nu}\frac{\|K_{2,p,\nu}\|^2}
                              {g_p^4 W_{p,\mu_p}(\nu)}.
\tag{13}
\]
The (g_p) and (g_p^2) normalizations in (12)–(13) are the exact
one-current and two-current source envelopes. The total targets are
\[
D_{1,T}=o(1),\qquad D_{2,T}=o(L^4).
\tag{14}
\]
The factor (1/4) in (13) is the square of A2's original (1/2).
Although (12)–(13) are rigorous inequalities on every finite Fourier
truncation, no estimate proving (14) is currently available.

## 5. Aliases, radius schedules, and the primorial test

At a current exponent (r\ne0), an exact (m=0) resonance would require
\(p^r\prod_{q\ne p}q^{\nu_q}=1\), impossible by the (p)-adic
valuation. For (m\ne0),
\[
\lambda_\nu+r\log p=mL
\quad\Longleftrightarrow\quad
 p^r\prod_{q\ne p}q^{\nu_q}=X^m,
\]
and the primorial family from the prior audit realizes (m=1). Near aliases
remain possible because \(\mathcal K_I\) can be order one within (O(1/T)).
For intermediate and far frequencies the pointwise geometric-kernel bound
is known, but its sum against all source coefficients is not.

For \(X_y=2\prod_{3\le q\le y,\ q\ prime}q\), take current (p=2,r=1)
and \(\nu_q=1\) on the odd primes through (y). Then
\(\lambda_\nu+\log2=L_y=\log X_y\), an exact (m=1) alias, and the
kernel factor at that label has modulus one. Let (S_y) be those odd
primes. The uniform log radius \(\rho_q=\log q/4\) is feasible once
\(32|S_y|/L_y\le131/400\), which holds eventually since
\(|S_y|/L_y\sim1/\log y\). It yields a single-contour weight
\(\exp(\frac12\sum_{q\in S_y}\log q)=(X_y/2)^{1/2}\). The random-sign
mixture instead gives exactly
\(\prod_{q\in S_y}\cosh((\log q)/2)\), at least
\(2^{-|S_y|}(X_y/2)^{1/2}\). Both suppress the reciprocal weight
exponentially in (L_y), because \(|S_y|=o(L_y)\).

For this **single** Fourier label, the optimized common measure is a point
mass at the solution \(\rho_q^*\) to the finite KKT system
\[
1=\mu B_q'(\rho_q^*)\quad(q\in S_y),\qquad
\sum_{q\in S_y}B_q(\rho_q^*)=131/400.
\tag{15}
\]
Strict convexity of each (B_q) makes the maximizing radii unique. Its
weight is \(\exp(2\sum_q\rho_q^*)\). This is an exact implicit optimizer
for that one-label truncation, not a shared optimizer for the full response
and not evidence that the corresponding response coefficient is nonzero.

Additional feasible schedules were checked at the level of contour cost:

- For \(\rho_p=c p^{-\alpha}\), \(\alpha>1/2\), the cost is
  \(O_c(L^{-1})\) from the convergent prime sum
  \(\sum_p\log p/p^{\alpha+1/2}\). The acquired height is only
  \(c\sum_p|\nu_p|\log p/p^\alpha\).
- For \(\rho_p=c/(\sqrt p\log^\beta p)\), \(\beta>1\), the cost is
  (O(c/L)\) by convergence of
  \(\sum_p1/(p\log^{\beta-1}p)\).
- For \(\rho_p=c\log p/(L\sqrt p)\), the total cost is (O(c)) by
  \(\sum_{p\le N}\log^2p/p=O(L^2)\); (c) must be fixed below a
  constant determined by the exact (B_p), not selected after dropping
  proper powers.
- On logarithmic prime shells (P_j), radii
  \(\rho_p=\eta_j\log p\) are feasible if
  \(\sum_j128\eta_j|P_j|/L\le131/400\).

These schedules show admissible ways to distribute contour cost. They do
not control the growing-support multiplicity or the actual (p)-summed
dual mass. The obstruction remains **aggregation over (p) and response
indices**, including alias concentration; it is not the validity of the
mixture lemma.

## 6. A1/A2 status and first missing theorem

- **A1:** its current-prime coefficients are aggregated over every power,
  sign, carrier and path before taking the kernel norm. The source envelope
  has divergent global \(\ell^1\) mass, so the old triangle estimate is
  unavailable. Mixture duality reduces the claim to (D_{1,T}=o(1)), which
  is open.
- **A2:** only the exact opposite-sign equal-power covariance diagonal is
  removed. The remaining same-sign and unequal-power correlations stay in
  (11). Fourth prime mass is (O(L^{-4})), so it suffices to prove
  (D_{2,T}=o(L^4)). No such bound has been established.
- **Alias strata:** (m=0) is excluded for each nonzero current exponent by
  unique factorization; nonzero periodic aliases exist; near aliases have
  order-one sampled kernel; intermediate/far pointwise kernel decay has no
  completed source-weighted summation.
- The old primorial example is only an admissible label. Its actual source
  response coefficient may vanish. No actual contribution lower bound is
  claimed.

The first unproved estimate is the pair of source-contracted dual-mass
bounds in (14), uniformly in the selected section at fixed (R), with all
actual root/mask tensors and carriers. This is a strict new reduction of
the transfer obligation but does not close either term. The fixed-R
comparison and strict (>79\%) remain OPEN.

## Reproduction

```powershell
python src/wp84_contour_mixture_prime_mass.py
python src/wp84_contour_mixture_prime_mass_replay.py
python src/wp84_analytic_response_trace_grid_transfer_replay.py
python src/wp84_dependent_phase_prime_adic_firewall_replay.py
```

The certificate stores the exact rational setup and hashes of its source
notes/scripts. The independent replay does not import the producer and
rejects hostile certificate mutations. PNT is used only for the stated
prime-mass asymptotics; it does not estimate either open dual mass.
