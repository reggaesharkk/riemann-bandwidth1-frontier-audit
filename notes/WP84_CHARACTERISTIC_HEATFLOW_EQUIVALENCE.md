# Characteristic / additive heat-flow equivalence and the actual-prime tail gate

Date: 2026-10-07. Parent: 67f240fdf15b55ecbd2f0828e82bca0126c5d693.
Decision: **C. ROUTES EQUIVALENT BUT TAIL BLOCKED.** No push or percentage promotion.
No search for a finite M_s is made.

## 1. Characteristic identity, including the error boundary

Use tau=tr/d, real background scalar s=s0(T), terminal point
z1=(4/5)(1+i), and z_t=s+t(z1-s). Let R_t(z)=(H_t-zI)^-1.
Write B(t,z)=E tau[R_t V(R_t) R_t], where V(X)=E W X W for
the chosen Gaussian noise, or sum G_p X G_p for the real Bernoulli
comparison. B is a D2 coefficient, not its primitive Xi:

    Xi(t,z)=E sum_j tau((E_j R_t(z))^2),  W=sum_j g_j E_j,
    B=Xi_z/2.

For the scalar Gaussian bridge H_t=sI+tP+sqrt(t(1-t))W,
Gaussian integration by parts gives EXACTLY

    t m_t+m+(z-s)m_z=-t B(t,z).

Therefore the chain rule gives EXACTLY, for 0<t<=1,

    d[t m(t,z_t)]/dt=-t B(t,z_t).                         (1)

No spectral derivative tower is used. For Bernoulli states the corresponding
identity has the Taylor remainder from the parent note. An o(1) proved on
fixed nonreal strips cannot be called uniform along Im z_t=(4/5)t.
For t>=delta>0 it remains o(1); growing-range bounds are discussed below.
For H0=sI+E0, the right side of the PDE acquires E tau(R E0 R).
This term cannot be integrated to t=0 using only ||E0||_1/d=o(1).

## 2. Exact rescaling and orientation

Set u=(1-t)/t, t=1/(1+u), du/dt=-1/t^2. Then

    H_t-z_t I=t[P+sqrt(u)W-(z1-s)I],
    t R_t(z_t)=[P+sqrt(u)W-(z1-s)I]^-1.                  (2)

Increasing t from 0+ to 1 runs u from +infinity DOWN to 0.
Define A=sI+P and R_u=(A+sqrt(u)W-z1 I)^-1.
Equation (2) says R_t(z_t)=t^-1 R_u, sample by sample.
For fixed spectral variables, Xi_t(z_t)=t^-2 Xi_u(z1).
Since partial_z=t^-1 partial_z1 under the rescaling,

    B(t,z_t)=t^-3 B_u(z1),
    B_u=E tau[R_u V(R_u) R_u]=Xi_u,z1/2.

Thus (1) reads -t^-2 B_u=(du/dt) partial_u m_u, and
partial_u m_u=B_u, exactly the additive Gaussian heat equation.
The noise covariance must be the SAME on both sides.

The real Gaussian series sum g_p G_p obtained from Bernoulli replacement
is not exactly the artificial circular quadrature series. They have
different finite-T covariance maps. Each Gaussian series separately obeys
(1)-(2); covariance comparison, not rescaling, relates the two series.

## 3. Moving consumer and its exact curvature

Let f=p_s be the shifted consumer with the exact coefficients in the parent
note and define f_t(x)=f(s+(x-s)/t). Functional calculus gives

    f_t(H_t)=f(A+sqrt(u)W),
    F(t)=E tau f_t(H_t)=Phi(u).

Its poles are z_t and conjugate z_t, still of order three. Explicitly

    f_t(x)=Einf+2 Re[A_s t/(x-z_t)
                    +B_s t^2/(x-z_t)^2+2C_s t^3/(x-z_t)^3].

At fixed x, t partial_t f_t+(x-s)partial_x f_t=0.
Combining this with the exact drift-free Gaussian functional generator yields

    F'(t)=-Q_(f_t)(t)/2
         =-t^-2 K(u),
    K(u)=Phi'(u)=Re E[A_s Xi_u,z+B_s Xi_u,zz+C_s Xi_u,zzz]. (3)

Here Q_g=E sum_j D^2[tau g(H_t)][E_j,E_j]. The equality
Q_(f_t)=t^-2 Q_f(A+sqrt(u)W) follows directly by differentiating
g(H+lambda E_j); Q_f/2=K. All coefficients stay grouped.
For cutoff U and delta=1/(1+U),

    F(1)-F(delta)=-integral_0^U K(u)du.                  (4)

This verifies both the Jacobian and the orientation, including the factor
1/2 in the Xi primitive. No independent (1-2t) cancellation survives:
v'(t)-2v(t)/t=-1. Gaussian integration by parts accounts for the apparent
skew factor, while the moving test accounts for the dilation.

## 4. Endpoints and the precise meaning of SAME THEOREM OBJECT

For circular finite-prime quadrature noise, W is invertible almost surely
at every fixed finite section. The corrected argument in
WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW section 10 is valid: one positive
shift A_s=G_s D_s has positive definite restricted Fourier Gram G_s;
the determinant of e^(i theta)A_s+e^(-i theta)A_s* has nonzero extreme
Fourier coefficients. Some real quadrature combination is invertible.
The Gaussian determinant polynomial is therefore nonzero. Finite-d
dominated convergence for bounded f gives

    lim_(t->0+) F(t)=lim_(u->infinity) Phi(u)=Einf,
    Einf=122310623232/120599925625.

This is NOT f(s), although H_t->sI at fixed d. The moving test is singular
at t=0; the limits of its state and its test cannot be separated.
For other Gaussian noises invertibility must be checked independently.
If W has a kernel, no general Einf boundary follows; its null-space
compression can retain finite spectral values. The zero-noise example
W=0 gives F(t)=tau f(A), showing the need for an endpoint hypothesis.

For the original actual-background bridge H_t=sI+E0+tP+sqrt(v)W,
rescaling instead gives

    f_t(H_t)=f(sI+P+E0/t+sqrt(u)W).

This is not the heat bridge with baseline sI+P+E0. Its fixed-d boundary
requires a separate argument; scalarization only gives an error bounded
by C_f ||E0||_1/(dt), inadequate uniformly near zero. If E0 is invertible
the 1/t term dominates and gives Einf; if E0=0 the preceding W argument
applies. No blanket boundary claim is made for arbitrary singular E0.

A clean exact workaround is to use the co-moving background bridge

    Htilde_t=sI+t(P+E0)+sqrt(v)W.

It has the same endpoints as the original bridge, and rescaling yields
the additive baseline A_actual=sI+P+E0 EXACTLY. Alternatively scalarize
the additive baseline first: |Phi_actual(u)-Phi_scalar(u)|
<=C_f ||E0||_1/d uniformly for ALL u by fixed-pole resolvent identities.
Endpoint differences then bound differences of signed curvature integrals;
one need not integrate a local background o(1)/t.

**SAME THEOREM OBJECT**, for a matched Gaussian noise and co-moving
background: (4) is exactly the shifted additive Loewner heat identity in
WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW, with A_s,B_s,C_s,Einf substituted.
Retire the characteristic Gaussian attack as a separate route; the canonical
representation is Phi(u) and grouped K(u). The Bernoulli path is only
asymptotically compared on controlled ranges, not an exact Gaussian path.

The scalar-shift bridge W=xi I in
WP84_SCALAR_HEAT_TAIL_AND_TWO_SIDED_SMALL_BALL_AUDIT_2026_10_06 is a
**DIFFERENT covariance/curvature object** with the same u=0 endpoint. Its
uniform tail does not transfer the prime-quadrature curvature theorem.

## 5. Weakest sufficient averaged endpoint requirement and tradeoff

Let g=f-Einf and use the certified source constant

    C_F=112913213256073216/87917345780625,
    |g(x)|<=C_F/|x| for |x|>=2.

A fully rational (not optimized) bound B_* on sup|g| is

    B_*=2[(|Re A_s|+|Im A_s|)/eta
       +( |Re B_s|+|Im B_s|)/eta^2
       +2(|Re C_s|+|Im C_s|)/eta^3], eta=4/5.

For M=||A_d||op, Weyl gives the source inequality

    |Phi_d(U)-Einf|<=B_* rho_d((K+M)/sqrt(U))+C_F/K.        (5)

Here rho is EXPECTED empirical spectral mass, not a probability that W is
invertible and not a single-coordinate conditional variance.
For chosen tail budget delta_tail, sufficient conditions are K>=2,
C_F/K<=delta_tail/2 and
rho_d((K+M)/sqrt U)<=delta_tail/(2B_*).
This single-scale condition is weaker than any uniform power law.
For rho_d(eps)<=C_d eps^beta, a sufficient quantitative tradeoff is

    K>=max(2,2C_F/delta_tail),
    U>=(K+M)^2(2B_* C_d/delta_tail)^(2/beta),              (6)

provided the argument is in the stated small-ball range. C_d may grow,
but U must also satisfy the covariance/curvature error conditions below.
For convergence to Einf rather than one fixed budget, choose K->infinity
and require C_d (K+M)^beta U^-beta/2->0.

Large baseline operator norm is avoidable. Split A=A_good+A_bad at
eigenvalue magnitude M0. rank(A_bad)/d=nu_A(|x|>M0). Rank interlacing
changes mass in an interval by at most twice this fraction. Thus

    |Phi_d(U)-Einf|<=B_*[rho_d((K+M0)/sqrt U)
                   +2 nu_A(|x|>M0)]+C_F/K.               (7)

If tau A^2<=J uniformly, use nu_A<=J/M0^2. A lower-moment gate,
not a full operator norm, can supply this input. This is an additional
proved reduction; it does not assume the numerical value of J.

## 6. Covariance audit: continuum window versus actual finite primes

The listed symbols s/(2a_phi^2) and 2s(1-s)^2/a_phi^2 are
positive-frequency quadrature contributions. They are not, individually,
the periodic spectral densities of REAL stationary a and h fields.
Real covariances require reflection s->1-s. Starting from circular Z with
E Z_k conjugate Z_l=a_phi^-2 integral s exp(2pi i(k-l)s)ds gives

    f_a(s)=[s+(1-s)]/(4a_phi^2)=1/(4a_phi^2),
    f_h(s)=[s(1-s)^2+(1-s)s^2]/a_phi^2=s(1-s)/a_phi^2,
    C_ha=0.

The cross sine integral vanishes because s(1-s) is reflection symmetric.
Hence in the continuum Gaussian ensemble a and h are independent,
a is white, and h has covariance diag 1/(6a_phi^2), offdiag
-1/(2pi^2 a_phi^2 r^2). The script checks these moments exactly.

For a CONTINUUM window of length d, the h Toeplitz covariance Sigma_d is
positive definite. For polynomial q(s)=sum_(k<d) c_k exp(2pi i k s),
||c||2=1, Parseval gives integral|q|^2=1 and |q|^2<=d. Delete two
endpoint intervals of length delta=1/(4d): their mass is at most 1/2.
On the remainder f_h>=delta/(2a_phi^2). Therefore

    lambda_min(Sigma_d)>=1/(16 a_phi^2 d),
    lambda_max(Sigma_d)<=1/(4a_phi^2),
    (Sigma_d^-1)_ii<=16 a_phi^2 d,
    Var(h_i | all other h in this window)>=1/(16 a_phi^2 d). (8)

Finite-window variances are also <=1/(6a_phi^2), with exact values
1/(Sigma_d^-1)_ii. Adding conditioning decreases variance. In a centered
growing two-sided window these decrease to zero, consistently with
integral 1/f_h=infinity and the prior audit. There is NO dimension-free
two-sided lower bound. For one-sided prediction, Jensen applied to a
prediction polynomial with constant coefficient one gives

    residual variance >= exp(integral log f_h)=e^-2/a_phi^2.

This is a one-sided bound only. It cannot be inserted after conditioning
on both halves of the matrix. No assertion about an exact finite-window
innovation equality is needed here.

There is nevertheless a dimension-dependent continuum-window Wegner bound.
Condition on a and all h_j except h_i. Independence of a and h ensures
the only remaining random matrix direction is h_i E_ii. Its density is
at most 1/(sqrt(2pi) sigma_i), where (8) gives sigma_i>=1/(4a_phi sqrt d).
Rank-one spectral averaging gives
E <e_i,1_[-eps,eps](W)e_i> <=2eps/(sqrt(2pi) sigma_i).
Sum over i and divide by d:

    rho_cont,d(eps)<=min(1,8 a_phi sqrt(d) eps/sqrt(2pi)).   (9)

For completeness, spectral averaging follows from the Schur complement
R_ii(z)=(h_i-b(z))^-1: integrating its positive imaginary part over h_i
against a density bounded by q gives <=pi q. Integrate in real z over
the interval and let Im z decrease to zero. Thus all hypotheses of (9)
are explicit; no generic random-matrix local law is imported.

The ACTUAL finite-prime quadrature field is different. If n=pi(N), it
uses only 2n independent real Gaussian coordinates. Its a and h sample
covariances each have rank <=2n, and their joint covariance rank <=2n.
In the current scale N=exp(L-sqrt L+o(1)), d asymp exp(L)L,

    2n/d = O(exp(-sqrt L)/L^2)->0.

Thus for the full actual section their smallest covariance eigenvalues
are EXACTLY ZERO. Their full inverse covariance is undefined. Distinct
Fourier nodes exp(+/-2pi i log p/L), when nonaliased and observed in at
least 2n consecutive rows, determine all quadrature coefficients by a
Vandermonde system. Consequently conditioning on the full a field then
determines h: the residual variance used in (9) is zero. Exceptional
coincident nodes require separate rank bookkeeping, not a uniform positive
variance assertion. The rank deficit alone already rules out (8) for
actual full-section covariances. Real Bernoulli Gaussian noise has even
fewer coordinates, at most n.

For small actual windows, covariance matrices are explicit finite prime
sums and can be inverted when nonsingular, but no lower bound uniform
over growing windows follows from fixed-lag PNT convergence. One-sided
finite-prime innovations also eventually vanish once sufficiently many
observations recover the finite field. The continuum innovation is not
a uniform-in-T finite-prime innovation theorem. A singular sample-field
covariance does NOT imply a singular W matrix: finite-d invertibility
above is compatible with this low-dimensional coefficient family.

## 7. Growing-U compatibility, with explicit sufficient ranges

Exact finite-d identities (2)-(4), Gaussian integration by parts, the
Hadamard covariance map, rank displacement identities and (5)-(7) hold
at any u. The actual finite-prime Xi needs no covariance replacement.
The resonant continuum substitution has a state-dependent error, not an
automatic uniform law for arbitrarily large u.

Here is a conservative quantitative extension of the existing BV proof,
with hypotheses stated: fixed terminal strip eta, sharp scalarized mean
with ||a_P||2/sqrt d=O(1), bounded square-prime mass, retained-range
discrepancy O(1/L), and endpoint width sqrt L/L. Gaussian second moments
give E||a_(P+sqrt u W)||2/sqrt d=O(1+sqrt u). The source proof's
commutator trace-norm and BV bound therefore become O_eta(1+sqrt u).
The endpoint loss instead uses |g_R|<=eta^-2, independent of u.
Cauchy on a fixed terminal pole circle handles Xi derivatives up to three.
Thus the EXPECTED grouped curvature substitution error is bounded by

    C_eta[(1+sqrt u)/L+L^-1/2].                            (10)

This is not a full-dimensional Gaussian-law coupling; it is only a
current-covariance contraction against the actual state. Its integrated
error through U is

    O_eta[(U+U^(3/2))/L+U/sqrt L].                         (11)

Consequently U=o(sqrt L) is a sufficient growing range for this
substitution, under those source bounds. No maximum admissible rate is
proved: (11) is sufficient, and a sharper endpoint treatment could improve
it. If the unspecified endpoint o(1) in a source is used WITHOUT the
working sqrt L cutoff rate, only fixed U and a nonexplicit diagonal
sequence are justified, not a prescribed polynomial growth.

Bernoulli-to-real-Gaussian comparison for f_t has third derivative bound
O(t^-3); hence error <=C kappa_T(1+U)^3. The block estimate gives
kappa_T=O(L^-3), since sum_(n>=2) (log n)^3/n^(3/2)<infinity (with a
constant for grouping powers). This is also small for U=o(sqrt L).
This comparison does not turn the real series into circular noise exactly.
The fast covariance contraction, if used for that extra comparison, must
be charged separately; the source rate includes O(L^-2/3) and its
integrated fixed-strip contribution U O(L^-2/3) is small on this range.
No moving-strip bound is obtained by merely renaming a fixed-strip error.

The continuum bound (9) requires U at least of order d for a fixed
tail budget and bounded/truncated baseline. Since d grows exponentially
in L, it is OUTSIDE (11)'s certified substitution range. Moreover (9)
was never a bound for the actual finite-prime field in the first place.
For C_d=O((log d)^gamma) and exponent beta, (6) would require
U of order L^(2gamma/beta) for a fixed budget. It fits the sufficient
range only if gamma<beta/4, with room for growing K if convergence rather
than a fixed budget is desired. Polynomial growth C_d=d^gamma, gamma>0,
cannot be paid by this range. Exact finite-prime curvature identities could
still be used beyond it, but no continuum curvature approximation there
has been proved by this audit.

## 8. Single missing tail lemma and consumer budget

Choose delta_tail=(8711/2778200)/4. The weakest presently useful tail
lemma would prove, for the ACTUAL finite-prime quadrature W_T, a sequence
U(T) in a justified curvature range and K(T)>=2 such that

    limsup B_* rho_T((K+M0)/sqrt U)
       +2B_* nu_(A_T)(|x|>M0)+C_F/K < delta_tail.          (12)

An arbitrarily slowly growing U with a uniform qualitative spectral
small-ball modulus and tight baseline tails would suffice; a universal
power-law exponent is not necessary. None is established here for the
actual prime ensemble. Finite-d determinant nonvanishing, one-sided
innovations, continuum (9), and rank-two Loewner structure do not prove
(12). This is the single narrow missing TAIL theorem. The independent
one-sided integrated CURVATURE inequality remains open as well.

At finite d, with the proved quadrature invertibility,

    tau f(A_T)=Einf-integral_0^infinity K_T(u)du.

If tail loss is <=delta_tail and approximation loss is <=delta_app, strict
>79 requires a finite-range lower bound

    integral_0^U K_model/state(u)du
       > Einf-21/200+delta_tail+delta_app.

The model-relative total loss must be <8711/2778200. This audit spends
none of that cushion by a proved actual tail estimate or curvature estimate.
The exact identities merge two descriptions; they do not improve the
numerical consumer bound. Decision C, not A or B: the available continuum
finite-dimensional lemma neither applies to actual noise nor fits the
known range, and an adequate actual spectral small-ball theorem is absent.

## Sources and verification

Read in full: WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW,
WP84_SHIFTED_UNIFORM_HEAT_TAIL_CRITERION,
WP84_SCALAR_HEAT_TAIL_AND_TWO_SIDED_SMALL_BALL_AUDIT_2026_10_06,
WP84_CIRCULAR_GAUSSIAN_Q_FIELD, WP84_GAUSSIAN_DRIFT_ELIMINATION,
WP84_GAUSSIAN_QUADRATURE_BRIDGE. Relevant proofs also inspected in
WP84_RESONANT_D2_UNIFORM_BV_CLOSURE, WP84_D2_FAST_CHANNEL_VK_CLOSURE,
WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE, WP84_PRIME_FRAME_GAUSSIAN_CONCENTRATION,
and corrected finite-d invertibility section of WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.
All source paths are notes/<name>.md. Parent audit supplies exact f coefficients.

Run src/wp84_characteristic_heatflow_equivalence.py. Exact scalar/matrix
algebra checks rescaling, moving consumer, Jacobian and covariance moments.
Optional Toeplitz numerical diagnostics are labeled numerical; (8)-(9)
are analytic inequalities, not numerical promotions. No Monte Carlo used.
