# WP84 dependent-phase prime-adic firewall

**Decision C — independent-Haar cancellation is exact, but transfer to the
actual trace grid remains open.** This is a fixed-R audit of the arithmetic
remainder, not a closure of the strict >79% theorem.

## Frozen setting and source boundary

Starting commit: 9ba9d4afad19cfdd8a9e4c2e5a386930fc16a14d on
codex/c5-c6-attack-20261006. Source hashes for the five governing notes and
the Hermite-projection certificate appear in the JSON certificate.

The test cylinder remains
\[
\Psi_R=s_{32,R,U}-s_{32,R,\delta},\qquad K=32,\quad\delta=1/100000.
\]
The comparison is
\[
 E\Psi_R(X_{T,R})-E\Psi_R(G_R)=A_{1,T,R}+A_{2,T,R}+O_R(L^{-3}),
\]
\[
A_1=\sum_p E_{K,g}[D\Psi_R(Y_p(K,g))\cdot V_p(K)],\quad
A_2=\frac12\sum_pE_{K,g}[D^2\Psi_R(Y_p(K,g)):(V_pV_p^T-\Sigma_p)].
\]
The current base p is excluded from Y_p. Group all powers as
G_p=sum_{a:p^a<=N}B_(p^a), with every power using the common base phase
z_p^a. The inherited mass bounds are max_p||G_p||=O(L^-1),
sum_p||G_p||^2=O(1), and sum_p||G_p||^3=O(L^-3). The cube mass pays the
Taylor remainder; it does not remove the first-order mean.

## Exact Haar cancellation

Fix p, a hybrid/permutation state and Gaussian realization. Lift only the
other deterministic prime-base phases to independent Haar variables z_q,
q!=p, retaining z_q^a for every power. Then Y_p and the responses
R1_p=D Psi_R(Y_p), R2_p=D^2 Psi_R(Y_p) have p-adic exponent zero.
The current block is a finite sum of nonzero characters
gamma_(p,a)z_p^a+conjugate(gamma_(p,a))z_p^-a, realified over xi/chi and lag
coordinates. Masks and lag/carrier factors alter coefficients, not exponents.

Conditioning on all other variables, integration in z_p kills every A1
term; hence A1_Haar=0 exactly. In A2, same-sign pairs have exponent
plus/minus (a+b); opposite-sign unequal powers have exponent plus/minus
(a-b). Both vanish under Haar measure. Opposite-sign equal powers are the
only survivors, and their sum equals E_(z_p)[V_p V_p^T]=Sigma_p for the
complete grouped block. Thus A2_Haar=0 after subtracting that exact
covariance. If Sigma_p is replaced by a limiting covariance, the difference
is a separate covariance-transfer payment. The equal-power term also
cancels pointwise on the actual path when the same exact grouped covariance
is subtracted.

These are identities for the lifted Haar law, not the trace-index law. The
source uses z_q(K)=exp(i(T+2 pi K/L)log q), with the same K for all bases.
No grid-to-Haar comparison is implied.

## Actual kernel, exact aliases, and response frequencies

For a contiguous source interval I,
\[
\mathcal K_I(\omega)=\frac1{d'}\sum_{k\in I}e^{i(T+2\pi k/L)\omega}.
\]
Writing lambda_nu=sum_(q!=p)nu_q log q, A1 has frequencies
lambda_nu +/- a log p. After covariance subtraction, A2 has frequencies
lambda_nu +/- (a+b)log p and lambda_nu +/- (a-b)log p for a!=b.
The residual therefore pairs exact response coefficients with
K_I(lambda_nu+r log p), with r!=0. It is the trace-grid discrepancy because
the Haar terms vanish.

Exact resonance is
\[
\lambda_\nu+r\log p=mL
\quad\Longleftrightarrow\quad
p^r\prod_{q\ne p}q^{\nu_q}=X^m,\qquad X=e^L.
\]
For m=0, unique factorization excludes resonance when r!=0. For m!=0, no
such result follows: X may be tuned to an arithmetic value. The response has
unbounded Bohr degree, so the finite alias range for fixed-degree moments
does not apply. Near aliases remain.

## L2 response coefficients and a counterexample

Fourier expansion is in L2(Haar x Gaussian); absolute summability is not
claimed. Parseval and the fixed-pole derivative bounds give, with
n_R=4(2R+1),
\[
\sum_\nu E_g||c_{1,p,\nu,g}||_2^2\le C_{1,R}^2,\qquad
\sum_\nu E_g||c_{2,p,\nu,g}||_F^2\le n_R C_{2,R}^2.
\]
The Hessian Frobenius factor follows from the dimension times its squared
operator bound. One torus derivative yields
\[
\sum_\nu\nu_q^2E_g||c_1||_2^2\le C_{2,R}^2g_q^2,\qquad
\sum_\nu\nu_q^2E_g||c_2||_F^2\le n_RC_{3,R}^2g_q^2.
\]
The exact constants and their input hashes are in the certificate.

L2 coefficient control alone cannot yield a uniform trace-grid estimate
tending to zero. Take current p=2, current exponent r=1, and p-excluded
response character z_3^253891 z_5^-173308. The exact frequency satisfies
\[
\lambda=\log 2+253891\log 3-173308\log 5
\in(1286529,1286530)\,10^{-12}.
\]
The independent replay certifies this interval with rational atanh-series
bounds. At T=7800, the natural cutoff N=floor(X exp(-sqrt(log X))) contains
2, 3, 5 and 2^2. For each source index with T<=T+2 pi k/L<=2T, the angle
is below 1/40. Since cos x>=1-x^2/2, the normalized kernel modulus is at
least 3199/3200, although this one-atom coefficient sequence has L2 norm
one. This is an adversarial L2 spectrum, not an assertion that the monomial
is an actual coefficient of D Psi_R. It falsifies the norm-only lemma, not
the desired prime arithmetic theorem.

For positive weights w_nu, the exact dual norm on weighted ell2 is
\[
\left(\sum_\nu
\frac{|\mathcal K_I(\lambda_\nu+r\log p)|^2}{w_\nu}\right)^{1/2}.
\]
Vanishing of this dual weighted-kernel mass is necessary and sufficient for
a uniform linear bound in that weighted class. First angular Sobolev
regularity is the first level penalizing this high-degree atom; existing
influence bounds do not establish the required p-summed weighted-kernel
estimate. No sufficiency claim is made.

## Status and first remaining theorem

- Haar A1: closed, exact zero.
- Haar A2: closed, exact zero after exact grouped covariance subtraction.
- Actual A1: open. Every current power remains in the first-order mean; its
  absolute prime l1 bound is O(1), not o(1).
- Actual A2: open after removing the equal-power diagonal. Unequal
  opposite-sign, same-sign, periodic and near-alias response correlations
  remain.
- A2 proper-power current correction: the certified square-mass estimate
  gives O_R(L^-1); this does not remove proper powers from A1.
- Direct degree-one/two coverage: ordinary covariance normalization and
  exact covariance diagonal; aggregate proper-power deletion only in its
  established bounded full-cylinder scope. The product with an unbounded
  degree leave-one-prime response is not covered by generic degree-one/two
  moment transfer.
- Authorized small section-start variation does not provide the O(d) phase
  averaging needed to smooth the 1/T kernel window; no useful smoothing is
  established.

The single remaining theorem is the source-matched signed limit
\[
\sum_p\Delta_{1,p,T,R}+\sum_p\Delta_{2,p,T,R}\longrightarrow0
\quad(T\to\infty),\qquad R\text{ fixed},
\]
for the exact p-excluded response, all grouped powers, common trace-index
path, natural cutoff, and every periodic and near alias. A sufficient
absolute version is the corresponding p-summed weighted-kernel dual-mass
estimate; it is not proved. No signed saving is earned. Strict >79% remains
OPEN.

## Reproduction

Run these commands from the repository root:

    python src/wp84_dependent_phase_prime_adic_firewall.py
    python src/wp84_dependent_phase_prime_adic_firewall_replay.py

The replay does not import the producer. It independently verifies the
rational frequency enclosure and cutoff/kernel bounds, checks the recorded
source SHA-256 values, and rejects 19 hostile mutations or invalid
inferences. The certificate records an open theorem, not a proof of the
trace-grid transfer.
