# WP84 — scalar Gaussian tail bypass and two-sided small-ball correction (2026-10-06)

Status: **UNIFORM LARGE-u TAIL CLOSED FOR A SCALAR-SHIFT BRIDGE; CURVATURE/ARITHMETIC INEQUALITY STILL OPEN**

This note records one valid simplification for the shifted exact-frontier
consumer and corrects a conditional-variance shortcut suggested during the
attack. It does not prove the WP84 consumer bound or an unconditional
zero-proportion theorem.

## 1. Scalar Gaussian bridge

Let
\[
p_s(x)=\frac{r^6P(x)^2}{((x-4/5)^2+(4/5)^2)^3},\qquad
E_\infty=\frac{122310623232}{120599925625},
\]
and set \(g=p_s-E_\infty\). The exact tail calculation in
WP84_SHIFTED_UNIFORM_HEAT_TAIL_CRITERION.md gives
\[
|g(x)|\le C_F/|x|\quad (|x|\ge2),\qquad
C_F=\frac{112913213256073216}{87917345780625}.
\]
Let \(B_F=\sup_{x\in\mathbb R}|g(x)|<\infty\).

For any deterministic Hermitian \(A_d\), let \(\xi\sim N(0,1)\), independent
of \(A_d\), and define
\[
\Phi_d(u)=\mathbb E\,\tau_d p_s(A_d+\sqrt u\,\xi I).
\]
For every \(K\ge2\) and \(u>0\),
\[
\left|\Phi_d(u)-E_\infty\right|
\le B_F\min\!\left(1,\sqrt{\frac2\pi}\frac K{\sqrt u}\right)
       +\frac{C_F}{K}.                                      \tag{1}
\]

**Proof.** Diagonalize \(A_d\), with eigenvalues \(\lambda_j\). For each \(j\),
\[
\mathbb P(|\lambda_j+\sqrt u\xi|\le K)
\le \frac{2K}{\sqrt{2\pi u}},
\]
uniformly in \(\lambda_j\). On this event use \(|g|\le B_F\); outside it
use \(|g(x)|\le C_F/K\). Average over \(j\) and then over any randomness in
\(A_d\). This proves (1), with no dimension, operator-norm, or moment
assumption.

Taking \(K=u^{1/4}\ge2\) for \(u\ge16\) gives the uniform bound
\[
\sup_d\left|\Phi_d(u)-E_\infty\right|
\le \left(B_F\sqrt{2/\pi}+C_F\right)u^{-1/4}.             \tag{2}
\]
The same argument works conditionally when \(A_d\) is random and independent
of \(\xi\).

The scalar heat equation gives the exact finite-dimensional identity
\[
\Phi_d'(u)=\frac12\mathbb E\,\tau_d
p_s''(A_d+\sqrt u\xi I),
\qquad
\tau_d p_s(A_d)
=E_\infty-\int_0^\infty\Phi_d'(u)\,du.                  \tag{3}
\]
Equation (2) makes the signed tail of the integral uniform in \(d\).

## 2. What this does and does not buy

The choice \(W=\xi I\) is a valid independent centered Gaussian direction
for the finite-dimensional heat identity. It removes the need for a
small-eigenvalue estimate on the matrix-valued Loewner noise and removes the
baseline operator-norm hypothesis from the large-\(u\) endpoint argument.

It does **not** bound the right side of (3). The integral is exactly the
unknown endpoint statistic rewritten as scalar Gaussian curvature. The
unresolved theorem-grade step remains a one-sided estimate strong enough to
show
\[
\limsup_{T\to\infty}\tau p_s(H_T)<0.105
\]
(or, for the full model frontier, at most \(1415/13891\)). The scalar bridge
does not inherit the useful grouped prime-curvature formula for the Loewner
bridge, so it is not by itself a closure of that arithmetic estimate.

## 3. Correction: two-sided conditional variance of the diagonal field

The continuum covariance recorded in
WP84_BERNOULLI_GAUSSIAN_INVARIANCE.md for the diagonal quadrature field
\(h_k\) has spectral density
\[
f(s)=\frac{s(1-s)}{a_\phi^2},\qquad 0<s<1,
\]
with covariance coefficients
\[
\operatorname{Cov}(h_0,h_0)=\frac1{6a_\phi^2},\qquad
\operatorname{Cov}(h_0,h_n)=-\frac1{2\pi^2a_\phi^2n^2}\quad(n\ne0).
\]
For a stationary Gaussian sequence with this density, the residual variance
after conditioning \(h_0\) on **all** other coordinates is
\[
\left(\int_0^1\frac{ds}{f(s)}\right)^{-1}=0,
\qquad
\int_0^1\frac{ds}{f(s)}
=a_\phi^2\int_0^1\frac{ds}{s(1-s)}=\infty.              \tag{4}
\]
Equivalently, the finite-neighborhood conditional variances decrease to zero
as the conditioned window grows. Numerically, the centered windows of radius
\(m=2,4,8,16,32,64,128\) give approximately
\(0.11973,0.10632,0.09434,0.08417,0.07570,0.06865,0.06275\), before the
common \(a_\phi^{-2}\) factor.

Thus the previously suggested \(e^{-2}/a_\phi^2\) value is not the
two-sided conditional variance; it is the one-sided innovation variance.
There can be no uniform positive conditional-variance lower bound for a
single \(h_i\) after conditioning on all other \(h_j\) in the continuum
limit. Since \(W_{ii}=h_i\), this rules out a Wegner proof that specifically
requires such a lower bound for the diagonal coordinates.

This is only an obstruction to that particular conditional-variance method.
It does not rule out a direct averaged eigenvalue small-ball theorem for the
full matrix \(W_d\), nor does it show that such a theorem is false.



## 4. Exact falsifier for pointwise transfer from the F61 route

The shifted consumer and the active bounded consumer
\[
F_{61}(x)=\frac{62P(x)^2}{P(x)^2+61}
\]
are distinct. In particular, \(p_s\le F_{61}\) is false. At the rational
point \(x=4/5\),
\[
P(4/5)=-\frac{41669}{347275},\qquad
P(4/5)^2=\frac{1736305561}{120599925625},
\]
and the shifted denominator is \(16/25\). Hence
\[
p_s(4/5)=\frac{13890444488}{120599925625}
       \approx0.1151778860,
\]
whereas
\[
F_{61}(4/5)=\frac{53825472391}{3679165884343}
       \approx0.0146298031.
\]
Thus the fixed-pole \(F_{61}\) arithmetic gate cannot imply the shifted
\(p_s\) gate by pointwise consumer domination. Any transfer between those
routes would need a different, proved relation on the actual spectral law.

## 5. Evidence boundary and next kill gate

The exact scalar-shift tail lemma is unconditional as a finite-dimensional
inequality, uniform in \(A_d\) and \(d\). The continuum covariance conclusion
uses the stated fixed-lag limiting Gaussian field. Neither result controls
the actual prime-side endpoint consumer.

The next decisive task remains to prove a one-sided arithmetic bound for the
actual zeta-side matrix \(H_T\), through the shifted one-point curvature
formula or the fixed-pole Bernoulli/Lindeberg route. No unconditional
simple-zero percentage follows from this note.
