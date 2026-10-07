# Joint signed deficit: endpoint telescope and projected covariance transfer

Date: 2026-10-07. Parent: `ab70f368e66ccb04f15e65e59223ebf9eee0832b`.
Branch: `codex/c5-c6-attack-20261006`, isolated Codex worktree `0498`.
Previous commits and the untracked NotebookLM packet are preserved. No push.

**Decision C — REDUCED TO ONE SUBSTITUTION EXTENSION LEMMA.**
The extension is stated in section 8 for an explicit two-copy, finite-order
Price contraction. It is a transfer lemma, not a consumer inequality.
The joint signed form telescopes EXACTLY to an endpoint projected-energy
difference. Consequently backward-adjoint amplification is absent from the
correct comparison. The earlier scalar substitution theorem does not already
prove this comparison. No actual/reference consumer value or >79 claim is
certified. Reference-state evaluation remains conditional on the extension;
noise replacement alone does not replace the deterministic arithmetic mean.

## 1. First kill gate: what the earlier sufficient range means

The complete ten requested notes were read before the new derivation, together
with the directly load-bearing covariance, BV/PNT, Loewner, Gram, co-moving
and verifier sources listed in section 13. Later corrections take precedence
over the early notes' larger closure claims.

`WP84_CHARACTERISTIC_HEATFLOW_EQUIVALENCE`, section 7, equations (10)-(11),
states, under its listed source bounds,

    expected grouped curvature substitution error
       <= C_eta[(1+sqrt(u))/L + L^(-1/2)],
    integrated error through U
       = O_eta[(U+U^(3/2))/L + U/sqrt(L)].                 (1)

Thus `U=o(sqrt(L))` is a SUFFICIENT range, not a maximal admissible rate.
For a source endpoint described only as `o(1)`, without the working
`sqrt(L)` quarantine, the source guarantees fixed U, not that specified rate.

The actual object is the ordinary-prime circular quadrature covariance
inserted into the current sharp Loewner resolvent. The baseline includes the
deterministic retained prime powers. With real independent standard normals,

    W_T = sum_p [g_pc C_p + g_ps S_p]/sqrt(2),
    V_T(X) = sum_p [A_p X A_p* + A_p* X A_p],
    Xi_T(R) = sum_j tau(B_j R B_j R), tau=tr/d.

The reference in this theorem is `Xi_res(R)` AT THE SAME CURRENT STATE R,
and its fixed-pole z derivatives through three. It is not an expectation
under a new Gaussian law. The basic BV test in
`WP84_RESONANT_D2_UNIFORM_BV_CLOSURE` is

    g_R(s)=tau(R U_s^+ R U_s^-),
    ||g_R||infinity <= eta^-2,
    Var(g_R) <= C_eta[1+||a_state||2/sqrt(d)].           (2)

Differentiation gives one displacement commutator and two rank-one endpoint
terms. `||[D,R]||1/d` is bounded using the normalized scalar-field l2 norm;
no factor d is charged. For the Gaussian heat state its expected field norm
is `O(1+sqrt(u))`. A fixed pole circle handles the finitely many z derivatives;
constants depend on derivative order and pole distance, not on d. The
endpoint uses the amplitude bound, not the variation bound. PNT upgrading
the retained cumulative measure discrepancy to `O(L^-2)` also gives
`O(log(d)/L^2)` for the specific K2 bilinear class.

**Scope:** current-covariance resolvent contractions and their specified
spectral derivatives are closed under the stated sharp/section and field
bounds. Arbitrary bounded covariance-contracted Frechet functionals,
multiple paired derivatives in two independently randomized states, and
Hermite-projection law comparisons were not proved there. Fixed-lag
convergence of the field covariance is a separate weaker statement. The
real Bernoulli Gaussian series is not the circular series exactly; its
same-sign/fast comparison is separate and is unnecessary for the chosen
artificial circular noise. No inverse covariance, innovation or small-ball
hypothesis is involved in (1)-(2).

Every fixed finite U is in the sufficient range. This removes the old
growing-U conflict. It does NOT change the test-functional scope of (2).

The working sharp reconstruction uses

    L=log(T/(2*pi)), N=floor(exp(L-sqrt(L))),
    d=floor(T L/(2*pi)), s_p=log(p)/L,
    c_p=-log(p)/(a_phi L sqrt(p)).

The underlying proofs use `log N/L -> 1`, `N/T -> 0`, an endpoint quarantine,
`log d=L+O(log L)`, and bounded square-prime mass. A selected principal
section retains its actual integer labels. Smooth taper equivalence and
section-dependent consumer transfers are not asserted by this reconstruction.
The field normalization `a_phi` is distinct from the pole height below.

## 2. Freeze the consumer and telescope the WHOLE signed form

Keep EXACTLY

    c=3142/2415, a=131/200, z=c+i a, eta=(c^2+a^2)^(3/2),
    P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3,
    Q(H)=eta P(H)(H-zI)^-3,
    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000,
    w0=1415/13891, epsilon=8711/2778200.                 (3)

Let `f(u)` be the orthonormal probabilists' Hermite coefficients of
`Q(H_T+sqrt(u)W_T)`, `x=Pi_K f`, and retain the earlier definitions of
`A_K`, `Phi`, `Y=Phi*Phi`, `X=Y-I`, `J`, and the TWO boundary residuals.
Their exact evolution implies

    d/du <x,Yx> = 2 Re <Yx,r_(K+1)+r_(K+2)>.

Since `Y(U)=I`, integration gives

    Phi_(K+1)+Phi_(K+2)
       = ||x(U)||^2-<x(delta),Y(delta)x(delta)>.

Add `J=<x(delta),(Y(delta)-I)x(delta)>`, BEFORE bounding anything:

    BOXED: J+Phi_(K+1)+Phi_(K+2)
             = L_K(C_T,U)-L_K(C_T,delta),
    L_K(C,u):=||Pi_K Q(H_T+sqrt(u)W_C)||^2.             (4)

This also follows by subtracting the two tail energies from the earlier
whole-chain identity. It has no propagator or backward weight. Each term
in the old decomposition may be badly amplified; that amplification is
exactly canceled in their sum. This is a direct endpoint evaluation, not a
generic norm-tail improvement. The signed deficit becomes

    D_T(K,U)=E_inf-w0-L_K(C_T,U)+L_K(C_T,delta).         (5)

The verifier's nonzero odd/even witness at K=3 independently gives

    J=57987/112,
    Phi_(K+1)=47907/196, Phi_(K+2)=18175/4,
    J+both fluxes=4159837/784=retained endpoint difference.

These numbers are algebra witnesses only. Dropping the second flux fails.
No positive sign for the joint value is implied by (4).

## 3. Same-space PSD covariances, including the finite-prime singularity

Use the fixed REAL field coordinate space `xi=(a_i,h_i)` for the chosen
finite section. Define the linear map

    W(xi)=M_h+[M_a,J_hilb],
    (J_hilb)_ij=1/[pi(j-i)], i!=j, diagonal zero.

Fixed coordinate directions are `E_i^h=E_ii` and
`E_i^a=[E_ii,J_hilb]`; the latter have one redundant constant-a direction.
Let `C_T=Cov(xi_T)`. At finite T, for r=i-j,

    A_T(r)=(1/2)sum_p c_p^2 cos(2*pi*r*s_p),
    H_T^cov(r)=2sum_p c_p^2(1-s_p)^2 cos(2*pi*r*s_p),
    C_ha,T(r)=-sum_p c_p^2(1-s_p) sin(2*pi*r*s_p),
    C_T=[[A_T,C_ha,T^T],[C_ha,T,H_T^cov]].              (6)

The sign in the cross block follows from `a=Im Z`, `h=2(1-s)Re Z` and
`Cov(Re Z_i,Im Z_j)=-Im E(Z_i conjugate Z_j)/2`.
Carrier phases rotate the two prime quadratures and cancel in (6).

On the SAME integer-labeled section set

    A_ref=I/(4 a_phi^2), C_ha,ref=0,
    H_ref,ii=1/(6 a_phi^2),
    H_ref,ij=-1/[2*pi^2 a_phi^2(i-j)^2], i!=j,
    C_ref,T=diag(A_ref,H_ref),
    C_theta=(1-theta)C_T+theta C_ref,T.                (7)

Both endpoints and every C_theta are PSD. Gaussian integration is well
defined even at theta=0 and singular C_T; use positive regularization and
dominated differentiation if desired, with no inverse covariance. The
mean remains the SAME deterministic matrix H_T throughout.

For the full section, `rank A_T <= m=2*pi(N)` and `m/d -> 0`. Thus there is
an actual null vector with reference a variance `1/(4 a_phi^2)`. A global
field covariance norm does not tend to zero. In fact `tr A_T/d -> 1/(4
a_phi^2)` and its nonzero rank is at most m, so its largest eigenvalue is
at least `tr A_T/m`; for large T this exceeds `1/(4 a_phi^2)`. Therefore
`A_ref-A_T` has BOTH positive and negative directions on the full section.
This is an obstruction to global norm/Loewner shortcuts, NOT to projected
Gaussian comparison. It does not establish a sign on the actually consumed
Hessian range. The covariance norm depends on the coordinate metric; it
must not be confused with the normalized-HS prime frame norm.

## 4. The frozen functional necessarily carries projection dependence

Index fixed field coordinates by i=1,...,q (q=2d). Put

    Q_n(X)_{i1...in}=D_H^n Q(X)[E_i1,...,E_in],
    M_n(C,u)=E_C Q_n(H_T+sqrt(u)W_C).

For tensors use the normalized matrix inner product `tau(A*B)` and contract
the two ordered coordinate lists through `C^tensor n`. Gaussian integration
by parts and normalized Hermite coefficients give EXACTLY

    E_n(C,u)=u^n/n! <M_n(C,u),C^tensor n M_n(C,u)>,
    L_K(C,u)=sum_(n=0..K) E_n(C,u).                    (8)

The n! compensates the ordered tensor enumeration: an unordered multi-index
of total n appears n!/alpha! times. Formula (8) is basis independent and
valid for a singular covariance. Its factors M_n depend on C.

One single-realization functional for each frozen C is

    F_(K,U,T;C)(W)=sum_(n=0..K) [
      U^n/n! Re<M_n(C,U),C^tensor n Q_n(H_T+sqrt(U)W)>
      -delta^n/n! Re<M_n(C,delta),
                         C^tensor n Q_n(H_T+sqrt(delta)W)>]. (9)

Its expectation equals (4). The same W at both endpoints is allowed;
expectations, not path independence, are used. This is NOT a covariance-
independent functional usable unchanged along theta. It explicitly depends
on C in its projector and its means. Freezing (9) at C_T would compare a
different target at C_ref.

The smallest useful covariance-aware alternative has two independent copies:

    G_K(C,u;W1,W2)=sum_(n=0..K) u^n/n!
      Re<Q_n(H_T+sqrt(u)W1),C^tensor n
                                      Q_n(H_T+sqrt(u)W2)>.

Use `G_K(C,U)-G_K(C,delta)` as ONE signed functional. This formula removes
unknown mean coefficients from the definition, but still has explicit C
factors. Two copies are required by squared mean Hermite coefficients.

## 5. Exact Price identity, factors and maximum derivative order

For a covariance-independent real functional F of real W coordinates,

    d/dtheta E_(C_theta) F
       = (1/2) DeltaC : E_(C_theta) D_W^2 F,
    DeltaC=C_ref,T-C_T.                                (10)

Apply to real and imaginary parts of matrix observables. For two independent
copies use the block covariance `diag(C_theta,C_theta)` and BOTH Hessians.
For the above covariance-dependent G there is also `E partial_theta G`.
These are the standard-real factors; using a circular complex coefficient
without its `1/sqrt(2)` real quadratures would produce the wrong normalization.

Define

    N_(n+2)(C,u)=DeltaC : M_(n+2)(C,u),
    dM_n/dtheta=(u/2) N_(n+2).

The comparison integrand for an endpoint projected energy is EXACTLY

    P_T(theta,u)=sum_(n=1..K) u^n/(n-1)!
       <M_n, (DeltaC tensor C_theta^tensor(n-1)) M_n>
      +sum_(n=0..K) u^(n+1)/n!
       Re<M_n,C_theta^tensor n N_(n+2)>.                (11)

Tensor symmetry permits choosing the first covariance leg for the n explicit
derivatives of `C^tensor n`. In the second sum the two mean derivatives
supply 2, canceling the Price 1/2. The first sum is real by the real symmetric
covariance and Hermitian inner product. The exact comparison is

    Fdual_ref,T-Fdual_T
       = integral_0^1 [P_T(theta,U)-P_T(theta,delta)]dtheta,
    D_T-D_ref,T = same integral.                       (12)

The functional family, its explicit covariance derivative, both endpoints
and all signs are now frozen. No separate J or flux estimates occur.

Maximum Frechet derivative of Q in a SINGLE factor is **K+2**; the other
factor has at most K. Maximum TOTAL order is **2K+2**. The first sum has
orders n,n; the second has n,n+2. There are finitely many orders for fixed K,
although their coordinate tensors grow with d. At K=0 there is already a
two-copy pairing of E Q and E D^2Q, rather than the old same-state energy
curvature. Cauchy z differentiation of a scalar resolvent is not a theorem
about all these inserted-direction tensors.

The verifier independently calculates Hermite masses by four-variable
Mehler/Wick integration and by (8), then compares their derivatives with
(11), including a rank-deficient covariance endpoint. A deliberate omission
of the explicit projector covariance derivative is rejected.

## 6. Contract DeltaC through the spatial covariance channels FIRST

Linearity gives the exact signed difference map, for every matrix X,

    DeltaV(X)=DeltaH o X
      +(DeltaC_ha o X)J_hilb-DeltaC_ha o(X J_hilb)
      +DeltaC_ha^T o(J_hilb X)-J_hilb(DeltaC_ha^T o X)
      +(DeltaA o(J_hilb X))J_hilb-DeltaA o(J_hilb X J_hilb)
      -J_hilb(DeltaA o X)J_hilb+J_hilb(DeltaA o(X J_hilb)). (13)

This is the nine-term Hadamard identity, with differences of ACTUAL and
reference covariances. It applies also to a two-copy cross pairing after
cyclically ordering the trace. In each ordered resolvent word in (11), the
single exposed DeltaC pair becomes a contraction

    Gamma_Delta(M,N)=tau(M DeltaV(N)).                 (14)

Other covariance legs stay paired through C_theta. The first sum in (11)
has its exposed leg across the two copies; the second has the exposed pair
inside the n+2 derivative in one copy. These are distinct contraction
geometries; neither is discarded. Normalization remains `tr/d` throughout.

For each sample, `rank[D,R]<=2`, `rank[D,Q]<=6`, and the three-wedge
factorization and K2 Gram identity apply. The latter is

    G_kl/(pi^2 d)=tau((R^k)*R^l)
                   -d^-1 sum_i conjugate(R^k_ii)R^l_ii.

Using both resolvent displacements in T12 introduces `1/(i-j)^4` and the
S4 kernel; differentiated T12 stays grouped as in the earlier stencil.
J_hilb is used through its l2 norm, not an absolute harmonic sum.

These identities evaluate the statewise terms in (14); they do not license
rank six for every higher derivative or averaged tensor. A resolvent-power
word with n inserted directions has displacement terms from every factor,
including `[D,B_j]`. An individual ordered term has a crude finite ceiling
`6+4n` for the nonconstant part of Q_n, from `2(k+n)+2n`, k<=3. Its sum or
Gaussian average need not retain that rank. Mixed poles retain BOTH generator
families. There is no fixed six-dimensional chaos/Hessian state reduction.

The previous covariance-contracted Malliavin estimates DO apply to the
conditioning of these terms: for C_theta, the full-sharp a_phi=1 constants
can be chosen eventually as `kappa_* =1/2`, `beta_*=5/2`; the reference has
the same limiting mass bound and the interpolation is convex. Ordered
derivative tensors have `u^r kappa beta^(r-1) C_r^2` bounds. Contract an
internal pair first through V, as in the previous Z_Q hierarchy. Splitting
DeltaV as V_ref-V_T supplies finite dimension-independent conditioning
bounds. It supplies `O_(K,U,a)(1)`, NOT a vanishing discrepancy. These
bounds remove a raw coordinate-count factor but contain no small PNT error.

## 7. Exact projected discrepancy: what can and cannot be charged

Let `nu_T=sum_p (log p)^2/(L^2 p) delta_(s_p)` and `nu_ref(ds)=s ds`.
Factor `a_phi^-2` explicitly. Let U_s^+ be the actual finite-section sharp
partial translation and put

    B_c(s)=(U_s^+ + U_s^-)/sqrt(2),
    B_s(s)=i(U_s^+ - U_s^-)/sqrt(2).

A carrier phase is an orthogonal rotation of these quadratures, so it has
no effect on their paired sum. The two copies of the heat state are
independent under C_theta. Denote their Frechet tensors by Q_n^1,Q_n^2.
Resolve the remaining C_theta legs by any real Gaussian direction family
`B_j(theta)` (a continuous family is equally admissible). Define the exact
current-shift amplitude

    h_T(theta,u;s)=a_phi^-2 {
      sum_(n=1..K) u^n/(n-1)! sum_(j1...j(n-1), q=c,s)
        Re E tau[ Q_n^1(B_q(s),B_j1,...)*
                  Q_n^2(B_q(s),B_j1,...) ]
      +sum_(n=0..K) u^(n+1)/n! sum_(j1...jn, q=c,s)
        Re E tau[ Q_n^1(B_j1,...)*
                  Q_(n+2)^2(B_j1,...,B_q(s),B_q(s)) ] }.

The expectation is over the TWO independent states, and every listed
direction sum is a covariance contraction, not a sum of individual norms.
For n=0 the direction list is empty. Thus EXACTLY

    P_T(theta,u)=integral h_T(theta,u;s) d(nu_ref-nu_T)(s).
    h_joint,T(theta;s)=h_T(theta,U;s)-h_T(theta,delta;s). (15)

This is the projected covariance discrepancy the route needs. Assemble
(13)-(14), K2/Gram and all signed channels before estimating h_joint.
The known norm bounds give bounded amplitudes for fixed K,U; the missing
step is a growing-section BV estimate for this TWO-COPY, higher-response
class. The old proof (2) establishes it for its listed scalar test, not
for the additional insertions and pairings in (15). In particular its
commutator calculation does not contain the `[D,B_j]` terms introduced
by the differentiated direction words. Claiming that finite K alone pays
their covariance-contracted sums would skip the required extension proof.

Fixed-lag covariance convergence, a global field operator norm, or a
spatial rank ceiling does not fill this gap. No actual-prime counterexample
to the projected discrepancy (15) has been established here.

## 8. The ONE substitution extension lemma, with a quantitative sufficient form

Choose fixed `0<delta<U<infinity`, integer K>=0, before T tends to infinity.
On the frozen actual section and SAME baseline H_T, prove

    BOXED PROJECTED TWO-COPY SUBSTITUTION LEMMA:
    integral_0^1 | integral h_joint,T(theta;s)
                           d(nu_ref-nu_T)(s) | dtheta -> 0. (16)

This estimate is on the explicit finite list of covariance-contracted
derivatives (15), with at most K+2 in a single Q factor and 2K+2 total.
It is not a general Gaussian-law coupling or a generic Hermite-tail bound.
Absolute value is taken only AFTER assembling the endpoint difference and
all n/covariance channels. The even weaker signed integral converging to
zero is sufficient for (12); (16) is a convenient robust formulation.

A concrete sufficient extension of the existing PNT/BV argument is

    integral_0^1 [ ||h_joint,T(theta;.)||infinity
                  + Var(h_joint,T(theta;.)) ]dtheta
       <= C_(K,U,delta,a,a_phi) [1+log d],              (17)

with the amplitude alone bounded independently of d to handle the deleted
endpoint layer. This gives, using the retained O(L^-2) discrepancy,

    |D_T-D_ref,T|
       <= C_(K,U,delta,a,a_phi)
            [ (1+log d)/L^2 + (1-log N/L) ]
       = O_(K,U,delta,a,a_phi)(L^-1+L^-1/2)=o(1).      (18)

A uniform BV bound is stronger than needed. Equation (17) allows the
logarithmic growth already tolerated by the source K2 theorem. Both
(16) and (17) remain OPEN here; (18) is conditional, not an error already
paid. The precise unproved derivative estimate is (16), or the sufficient
BV realization (17), for the contracted Hessian of the covariance-aware
functional (9). The new algebra and old derivative bounds expose this
estimate without backward factors `(U/delta)^K` or Gaussian dimension m.

The old `U=o(sqrt L)` theorem therefore answers possibility B in the user's
scope test: it controls the old resolvent contractions, but has not proved
the needed finite derivative extension. Possibility C about surviving
backward amplification is rejected by (4). Rank deficiency is irrelevant
to the derivation of (10)-(12). Changing to t is unnecessary once (4) is
used; no new contractive-forward assertion is made.

## 9. Continuum Fourier/Hermite representation and its actual boundary

The original circular complex field symbol is `kappa_Z(s)=s/a_phi^2`,
with zero pseudocovariance. The original positive-frequency contributions
`s/(2a_phi^2)` and `2s(1-s)^2/a_phi^2` are NOT separate real stationary
spectral densities. Reflection produces

    f_a(s)=[s+(1-s)]/(4a_phi^2)=1/(4a_phi^2),
    f_h(s)=[s(1-s)^2+(1-s)s^2]/a_phi^2=s(1-s)/a_phi^2,
    f_ha(s)=0.                                        (19)

The field normalization a_phi has no identity with the consumer pole
`a=131/200`. Real a and h are independent in this Gaussian reference.
Fourier diagonalization is exact on the infinite stationary lattice.
A finite Toeplitz compression is NOT a circulant matrix diagonalized
exactly by a finite DFT; the verifier rejects that conflation.

An exact spectral construction on the same finite integer-labeled section
uses, for lambda=a,h, four real white-noise direction families

    v_c(s)_k=cos(2*pi*k*s), v_s(s)_k=sin(2*pi*k*s),
    B_(a,q)(s)=sqrt(f_a(s))[M_(v_q(s)),J_hilb],
    B_(h,q)(s)=sqrt(f_h(s)) M_(v_q(s)), q=c,s.

Their covariance integral is exactly (7). The n-th reference chaos energy is

    E_n,ref,T(u)=u^n/n! sum_(chi1...chin)
      integral_[0,1]^n || E D^n Q(H_T+sqrt(u)W_ref,T)
                   [B_chi1(s1),...,B_chin(sn)] ||_(2,tau)^2 ds. (20)

This is a finite-order torus integral of positive response Grams. It is
not just a finite convolution of the covariance symbol: the response still
contains the nonlinear Gaussian matrix functional. The joint flux value is
the DIFFERENCE of the sums (20) at U and delta, not two separately certified
boundary fluxes. Polynomial observables would give finite Wick reductions;
the rational resolvent has infinitely many chaos levels, even though only
the selected finitely many levels are used here.

Crucially `D_ref,T` still depends on H_T and the selected section. A theorem
`D_ref,T -> D_ref` or a uniform reference bound must control that arithmetic
mean. No source read identifies it with a finite stationary Gaussian model
or the four-node Christoffel quadrature. No limit in dimension or removal
of that mean has been performed. This distinction is an additional boundary
of the proposed continuum certificate, not a noise substitution error.

## 10. Exact model identities and the ledger

The exact simplification found is the telescope (4). Parseval gives (8) and
the Mehler coefficients; Cayley unitarity controls conditioning and spatial
Grams. None supplies `L_K(C_ref,U)-L_K(C_ref,delta)=E_inf-w0`.
Christoffel saturation `E_model p=w0` uses the discrete four-node measure
at the roots of P, whereas this Gaussian state is centered at H_T. Those
are different expectations. Taking K to infinity in (4), when justified at
fixed T, returns `E(U)-E(delta)`, retaining the unknown endpoint law.
No exact model-value identification or Ward cancellation of that unknown
is found. The scalar Hessian sign checks below also preclude a universal
monotonicity proof for every baseline from the covariance alone.

Retain the frozen initial costs exactly:

    c_initial=delta kappa_* sqrt(E_inf) K2,
    c_initial_chaos=delta kappa_* K1^2/(K+1).

There is NO new Malliavin residual cost after the exact telescope. The
initial chaos cost already pays the initial discarded tail in the earlier
sufficient gate; it must not be charged twice. The terminal chaos tail is
nonnegative and was discarded for a lower bound. Physical heat tail is
closed by the cap, with zero extra loss. Substitution is not yet paid.

For the illustrative INITIAL-only tuple
`delta=1/100000, K=16, kappa_*=1/2`, using the proved rational enclosures
`sqrt(E_inf)<43/20`, `K1<10`, `K2<74`,

    c_initial+c_initial_chaos < 28047/34000000,
    epsilon - that upper cost =1091269123/472294000000.

| Ledger entry | Certified status/value |
|---|---|
| Model cushion | 8711/2778200 |
| Initial layer plus initial chaos | strictly below 28047/34000000 for the illustrative tuple |
| Additional Malliavin/adjoint residual | 0, exact identity |
| Physical large-u tail loss | 0 for the frozen cap-safe consumer |
| Covariance substitution error | OPEN; conditionally o_T(1) by (16) |
| Signed reference deficit | UNKNOWN; no certified or promoted diagnostic K,U |
| Available initial-only budget | 1091269123/472294000000 |
| Final consumer margin | UNCERTIFIED |

For a certified reference bound `d_ref` and a paid asymptotic substitution
loss `e_sub`, the complete strict ledger would be

    margin=8711/2778200 - d_ref - e_sub
            -delta kappa_*[sqrt(E_inf)K2+K1^2/(K+1)] > 0. (21)

No tuple U=1,2,4,8,16 is called promising. Task 10 is conditional on a
successful comparison; that kill gate has not passed. Computing a surrogate
baseline or sampling a finite Gaussian window would not certify D_ref for
the actual baseline. The new exact K=3,U=2 polynomial witness is only an
algebra check and cannot be entered into (21). Zero-side block/tail,
normalization and taper transfers are not promoted by this note.

## 11. Hostile tests: distinguish amplification, wrong metric and missing uniformity

First, the exact polynomial witness verifies cancellation of the old Y
amplification in the grouped value. For a FIXED-dimensional bounded rational
Q with poles separated from R, finite K,U, covariance convergence in a
fixed coordinate space gives convergence of (8), by Gaussian expectation
continuity and bounded derivatives. There is no residual backward factor
that could defeat that conclusion. A hostile counterexample must violate
the discrepancy metric, the dimension/Hessian uniformity, or the functional
scope, rather than retaining a canceled propagator.

Here is an analytic bounded example with growing coordinate dimension and
operator-norm covariance difference tending to zero. It deliberately lacks
the actual fixed-Q derivative hypothesis. Let

    C_m=I_m, C_ref,m=(1+m^-1/2)I_m,
    psi_m(x)=[1+exp(i(||x||^2-m)/sqrt(m))]/2,
    F_(m,u)(g)=psi_m(sqrt(u)g), K=0, delta=1/4, U=1.

This is bounded by one. It can be embedded as `psi_m(diag(x)) I_m`, with
spatial displacement rank zero and diagonal Gaussian noise whose CP beta
is bounded. Its mean at variance c is EXACTLY

    M_m(u,c)=[1+exp(-i sqrt(m))
                        (1-2i u c/sqrt(m))^(-m/2)]/2. (22)

Take `m_j` to be the nearest integer to `(2*pi*j/(1-delta))^2`. Then
`(delta-1)sqrt(m_j)` tends to `-2*pi*j` modulo a vanishing error. Expanding
the logarithm in (22) proves, at u=delta and u=1,

    M_actual ->(1+exp(-u^2))/2,
    M_reference ->(1+exp(-u^2)exp(iu))/2.

Consequently the REFERENCE minus ACTUAL grouped K=0 endpoint energy
difference tends to

    [e^-1(cos(1)-1)-e^(-1/16)(cos(1/4)-1)]/2
       in [-0.069954626844386241724,
           -0.069954626844386241723].                  (23)

Yet `||C_ref,m-C_m||op=m^-1/2 -> 0`. The corresponding covariance-contracted
Hessian is not uniformly bounded in the dimension: the radial score has
sqrt(m) sensitivity. Thus boundedness, fixed K,U, small operator-norm
covariance difference and spatial rank zero are insufficient by themselves.
This is NOT the actual-prime/current-Q state and not a route-D falsifier.
The actual CP derivative hierarchy rules out importing this arbitrary
functional's sensitivity bound, but still needs the projected discrepancy
estimate (16) because the actual field covariance is not globally small.

For global covariance Loewner order, section 3 already finds both signs.
No order restricted to the actual Hessian responses is proved. Even for a
positive scalar covariance change the consumer Hessian has both signs:

    p''(0)=-29031754442553015119001839616/
              75639853533581807903139390121 < 0,
    p''(1/20)>0 (exact rational regression).

This discards a universal covariance-order/convex-Hessian shortcut. It does
not exclude a signed inequality special to the actual arithmetic state.

The optional `--recon` tests the ACTUAL full-sharp prime means at T=128
(d=61,N=3) and T=256 (d=151,N=5), u=0. It forms the six-response difference
Gram `tau[S_r* DeltaV(S_l* S_m) S_n]` without replacing DeltaV by its norm.
Floating eigenvalue ranges are respectively about `[.0292822,3.2235185]`
and `[.0370033,2.7828540]`, positive in those diagnostics. These are NOT
interval sign certificates, do not test all theta,u, and do not include a
favorable sign for the ten signed cross contractions. They establish no
asymptotic projected order and cannot be used as a consumer payment.

## 12. Decision and exact evidence boundary

**C — REDUCED TO ONE SUBSTITUTION EXTENSION LEMMA**, namely (16), with
the explicit sufficient derivative/BV estimate (17). The earlier range
is sufficient for fixed U but its proven test class is narrower. Rank
deficiency does not obstruct Price interpolation. Backward amplification
vanishes when the initial dual and both boundary fluxes stay together.
The actual-to-reference error is (12), not a global covariance norm estimate;
it is not yet o(1) by a source-closed theorem.

Closed here: joint endpoint telescope; covariance-aware functional;
standard-real Price identity including the explicit projection derivative;
maximum finite derivative orders; exact projected discrepancy formula;
same-space PSD reference covariance and real spectral symbols; exact
regressions and hostile scope distinctions.

Open: (16); subsequently a reference-state bound strong enough for (21),
including retention/control of the deterministic arithmetic mean. Decision
C does not claim one substitution lemma alone proves the >79 bound. A
would require a certified reference margin; B would require closed transfer
and a genuine finite certificate; D would require a counterexample to this
actual projected class. None is established. **Strict >79 remains OPEN.**

## 13. Source reads, replay and preservation

Read in full for this derivation (all notes below are under `notes/`):

- WP84_CHARACTERISTIC_HEATFLOW_EQUIVALENCE.md
- WP84_GAUSSIAN_QUADRATURE_BRIDGE.md
- WP84_GAUSSIAN_DRIFT_ELIMINATION.md
- WP84_CIRCULAR_GAUSSIAN_Q_FIELD.md
- WP84_SHIFTED_UNIFORM_HEAT_TAIL_CRITERION.md
- WP84_SCALAR_HEAT_TAIL_AND_TWO_SIDED_SMALL_BALL_AUDIT_2026_10_06.md
- WP84_TAIL_CAPPED_EXACT_FRONTIER_CONSUMER.md
- WP84_INTEGRATED_CROSS_ERROR_STEIN_CHAOS.md
- WP84_CROSS_REPOSITORY_PROOF_TRANSPLANT_AUDIT.md
- WP84_ACTUAL_STATE_SIGNED_DUAL_FLUX.md
- WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md
- WP84_GAUSSIAN_COVARIANCE_HADAMARD.md
- WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md
- WP84_D2_FAST_CHANNEL_VK_CLOSURE.md
- WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md
- WP84_TAIL_CAPPED_FINITE_U_CURVATURE.md
- WP84_PRIME_FRAME_GAUSSIAN_CONCENTRATION.md
- WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
- WP84_BERNOULLI_GAUSSIAN_INVARIANCE.md
- WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.md
- WP84_SHIFTED_K2_GRAM_CANCELLATION.md
- WP84_SHIFTED_THREE_CHANNEL_GRAM.md
- WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.md
- WP84_BR_RANK3_SCALAR_D1.md
- WP84_FOUR_POLE_INEQUALITY_KILL_GATE.md
- WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md
- WP84_RESONANT_SCALAR_COVARIANCE.md

Backing programs read in full, under `src/`:

- wp84_characteristic_heatflow_equivalence.py
- wp84_integrated_cross_error_stein_chaos.py
- wp84_actual_state_signed_dual_flux.py
- wp84_cross_repository_hermite_adjoint.py
- wp84_tail_capped_exact_frontier_consumer.py
- wp84_tail_capped_finite_u_curvature.py
- wp84_gaussian_quadrature_bridge_gate.py
- wp84_gaussian_covariance_hadamard_gate.py
- wp84_resonant_d2_bv_derivative_gate.py
- wp84_shifted_heat_tail_polynomial_gate.py
- wp84_resonant_d2_explicit_gate.py
- wp84_bernoulli_gaussian_invariance_gate.py
- wp84_r2_comoving_heat_flow_gate.py
- wp84_shifted_resolvent_wedge_gate.py
- wp84_resonant_scalar_covariance.py

The earlier cross-repository audit is used for its local exact derivation,
not to import any external NS/LRSC proof or missing producer arrays. Historical
linked sources irrelevant to this covariance extension are not claimed as
newly reread. The new replay requires no network or external theorem import.

Run `python src/wp84_joint_signed_deficit_covariance_transfer.py --recon --output
notes/WP84_JOINT_SIGNED_DEFICIT_COVARIANCE_TRANSFER_REPLAY.json`.
All identity/mutation checks are exact rational symbolic calculations;
only (23)'s enclosure uses outward interval arithmetic at 40 decimal digits.
The optional six-response eigenvalues are explicitly floating diagnostics;
no Gaussian sampling or floating acceptance gate is used. The replay records
`consumer_certified=false`, no certified K,U and no final margin. The source
coverage manifest records parent Git blobs and SHA-256 hashes; it is
provenance, not an analytic proof certificate. All changes are additive.
