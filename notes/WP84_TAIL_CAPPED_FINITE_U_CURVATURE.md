# Tail-capped finite-U curvature: direct positive-energy Hessian and its signed error

Date: 2026-10-07. Parent: 76cfd635924073219411dfe4bd3e984f8faf8332.
Decision **B: curvature algebra reduced to one signed positive-energy cross
error**, not a certified inequality. Pointwise sign and universal absorption
are FALSE. No useful Lyapunov corrector is certified. Strict >79 remains OPEN.

Use precisely c=3142/2415, a=131/200, z=c+ia, delta=2ia, normalized
tau=tr/d, and the preferred tail-capped p and cubic P from the parent note.
Einf=7761139416076220170204368647089/1680256283972002400160000000000.
All earlier local audits and the NotebookLM packet are preserved. No push.

## 1. Direct Fréchet formulas, with independent covariance direction

Let H be real symmetric, R=(H-zI)^-1, U=I+delta R, Q=q(U), where
q=q0+q1u+q2u^2+q3u^3 is the exact Cayley polynomial of the parent note.
For Hermitian direction B, set

    X=DU[B]=-delta R B R,
    Y=D2U[B,B]=2delta R B R B R.

Exactly, without commutativity assumptions on B,

    DQ[B]=sum_(n=1..3) qn sum_(i=0..n-1) U^i X U^(n-1-i),
    D2Q[B,B]=sum_(n=1..3) qn [sum_(i=0..n-1) U^i Y U^(n-1-i)
        +2sum_(0<=i<j<n) U^i X U^(j-i-1) X U^(n-1-j)].

For W=sum_j gamma_j E_j, with independent standard REAL Gaussians,
H_u=H_1+sqrt(u)W, use the EXACT covariance V(Z)=sum E_j Z E_j.
Differentiate the energy, rather than only its analytic partial fractions:

    D2[tau Q*Q][B,B]=2tau(DQ[B]* DQ[B])+2Re tau(Q* D2Q[B,B]),
    E_u'=E Gamma1(H_u)+E Gamma2(H_u),
    Gamma1(H)=sum_j tau(DQ[E_j]* DQ[E_j])>=0,
    Gamma2(H)=Re tau[Q* sum_j D2Q[E_j,E_j]].              (1)

Equivalently covariance-average ||DQ[Wfresh]||_(2,tau)^2, where Wfresh
is INDEPENDENT of H_u. Using the same W that generated H_u in this
conditional average would generally be wrong. Unnormalized HS squares
must be divided by d. Gaussian differentiation supplies the Hessian factor
1/2, which cancels the two factors in the displayed Hessian.

## 2. Six-channel positive Gram and ten cross contractions

Set S_l=U^l R (l=0,1,2), T_j=U^j R^2 (j=0,1). Then

    DQ[B]=-delta sum_(l+r<=2) q_(l+r+1) S_l B S_r.

The six index pairs (l,r) form a positive covariance Gram matrix

    M_(lr,mn)=tau[S_r* V(S_l* S_m) S_n],
    Gamma1=|delta|^2 sum conj(q_(l+r+1)) q_(m+n+1) M_(lr,mn).

Positivity follows from the covariance-average squared norm itself;
no entrywise positivity of resolvents or Toeplitz kernels is assumed.
The EXACT averaged second derivative is

    Z_Q:=sum_j D2Q[E_j,E_j]
       =2delta sum_(l+r<=2) q_(l+r+1) S_l V(R) S_r
        +2delta^2 sum_(i+j+k<=1) q_(i+j+k+2) S_i V(T_j) S_k,
    Gamma2=Re tau Q* Z_Q.                                (2)

There are six contractions in the first sum and four in the second.
Keep them grouped before taking real parts or absolute values. This is
the requested positive square plus signed error: E_u'=E Gamma1-E Error,
Error=-Re tau Q*Z_Q. Error is SIGNED, not assumed nonnegative.

Use the actual quadrature E_(p,c)=C_p/sqrt2, E_(p,s)=S_p/sqrt2 or
the actual Gaussian covariance of the chosen bridge. The exact Hadamard
map, with A0=E aa^T, H0c=E hh^T, C0=E ha^T, is

    V(Z)=H0c o Z+(C0 o Z)J-C0 o(ZJ)
      +C0^T o(JZ)-J(C0^T o Z)
      +(A0 o(JZ))J-A0 o(JZJ)-J(A0 o Z)J+J(A0 o(ZJ)).

This retains every Toeplitz/cross covariance. Replacing these matrices by
continuum kernels is a SEPARATE fixed-U substitution. The continuum real
field has A0=I/(4a_phi^2), C0=0, and H0c with diagonal 1/(6a_phi^2)
and off-diagonal -1/(2pi^2 a_phi^2 r^2). Do not silently use those
matrices as exact finite-prime covariances.

## 3. Ward identities and agreement with the Xi stencil

For the convention R=(H-zI)^-1,

    R-R*=2ia R*R,
    R*R=Im(R)/a>=0,
    R*R=(2I-U-U*)/(4a^2).

All powers of R,R*,U commute WITH EACH OTHER, not with E_j. Thus
(R*)^k R^l=(R*R)^min(k,l) times the remaining analytic or conjugate
power. For example (R*)^k R^k=(Im R/a)^k is positive. Wirtinger
differentiation gives partial_z(R*R)=R*R^2 and
partial_conjugate_z(R*R)=(R*)^2 R. Differentiation in a or c must move
BOTH poles; these identities prevent a wrong sign or a lost conjugate.
They make the six-channel Gram manifestly positive but impose no sign
on (2).

Define Xi(z)=E sum_j tau((E_j R(z))^2). At finite dimension,

    partial_u m=Xi_z/2,
    E_u'=Re E[A Xi_z+B Xi_zz+C Xi_zzz].                   (3)

A,B,C are the exact coefficients of the preferred consumer. To replay
derivatives without numerical differencing,

    Xi^(n)=n! E sum_j sum_(k=0..n)
             tau(E_j R^(k+1) E_j R^(n-k+1)), n=1,2,3.

Equations (1)-(3) agree by the exact energy/partial-fraction identity.
The verifier checks equality EXACTLY in scalar arithmetic and independently
on noncommuting structured matrices using the displayed Fréchet formulas.
Matrix floating-point agreement is a regression check, not a theorem estimate.

## 4. Complementary gap factorization

Let U_a(x)=C_P^2(((x-c)^2+a^2)^3)-P(x)^2, C_P=9660/13891,
and kappa=22880295987/19295988100 its positive leading coefficient.
The parent dual Sturm certificate proves it has no real roots. Let
zeta1,zeta2 be its two roots in the upper half-plane, specified EXACTLY
as algebraic roots of that rational quartic, and h(x)=(x-zeta1)(x-zeta2).
Then the exact factorization is

    U_a(x)=kappa h(x) conjugate(h(conjugate x)),
    g(x)=Einf-p(x)=r6 kappa |h(x)|^2/(((x-c)^2+a^2)^3),
    G=r3 sqrt(kappa) h(H) R^3, G*G=g(H).

This root-selection definition specifies exact algebraic coefficients;
the following decimals are diagnostic labels only:

    zeta1 ~=1.04156512682146+0.329021339123144i,
    zeta2 ~=1.56315817538499+0.338557828162849i.

Factoring into the two REAL positive quadratic factors is equivalently
kappa product_j[(x-Re zeta_j)^2+(Im zeta_j)^2]. The complex spectral
factor h is a quadratic, so G has numerator degree two rather than three.
Its Cayley polynomial is

    q_g(u)=r3 sqrt(kappa)/delta^3 (u-1)
       product_j[z u-conjugate z-zeta_j(u-1)].

It has degree at most three, q_g(1)=0, and displacement rank <=6.
For real symmetric H, G^T=G and [D,G]^T=-[D,G]. Thus the gap factor
does NOT lower the pole order or the six-column rank ceiling.

Let Gamma1_g,Gamma2_g be (1) applied to G. Then

    -E_u'=E Gamma1_g+E Gamma2_g,
    Gamma1_p+Gamma2_p+Gamma1_g+Gamma2_g=0

after covariance averaging. The desired positive p curvature gets a
NEGATIVE squared term in the gap representation. Positive g alone does
not give a quantitative lower bound g(H_1)>Einf-.105.
The p representation is preferred for a curvature lower bound because
it retains the positive Gamma1 term; the gap representation remains useful
for endpoints and possible cross-term identities.

## 5. Minimal exact hostile counterexamples

For d=1, any H is a sharp-Loewner state: its displacement commutator is
zero and J=0. The resonant covariance is V(X)=X/6 (a_phi=1).
Any nonzero actual finite-prime diagonal covariance merely multiplies
the following Hessian signs by a positive scalar.

At H=0,

    p''(0)=-29031754442553015119001839616/75639853533581807903139390121<0,
    Gamma1=0.41890632974375163326...,
    Gamma2=-0.45089096161693009594...,
    E'_0=-0.031984631873178462680... .

At H=1,

    p''(1)=-15731665700929963637973033158719170092145560702992562147472
           /517346125793081273080748757851155002435291847975196127769<0,
    Gamma1=1.8835562830314175942...,
    Gamma2=-4.4175892570572103639...,
    E'_0=-2.5340329740257927696...,
    -Gamma2/Gamma1=2.3453449715595917062... .

The displayed Gamma decimals label exact rational quantities computed by
the verifier; the signs and ratio>1 are checked exactly. These falsify
E'_u>=0, Gamma2>=0, and Error<=theta Gamma1 for every theta<=1,
as universal structured-state claims. d=1 is the smallest possible example.
At u=0 the state is deterministic, so covariance averaging does not hide
the counterexample; continuity also gives negative expected curvature for
sufficiently small positive u.

The d=4 actual-quadrature surrogate regression also finds negative curvature
at H=I. None of these is a counterexample to the asymptotic ACTUAL prime
endpoint inequality, which has additional arithmetic/state restrictions.

## 6. Completion of squares and bounded Lyapunov correctors

Ward and covariance positivity prove Gamma1>=0; universal absorption of
Gamma2 into it is impossible by section 5. Completing squares with a
discarded remainder cannot establish the falsified inequality.

A useful bounded corrector is not proved here. There is an exact obstruction
to a universal scalar corrector with nonnegative corrected curvature:
if l(x) is bounded C2 and (p+l)''>=0 on all R, then p+l is bounded
convex and hence constant. Thus l=constant-p is the only such scalar
corrector, and it yields zero rather than useful positive forcing. This
applies to bounded finite Cayley/resolvent/Ward combinations on the scalar
subclass. The complementary gap l=g is precisely this vacuous corrector:
E_u'+(E tau g(H_u))'=0, with its u=0 endpoint equal to the unknown
gap being sought. Counting that endpoint as a known benefit is circular.

The obstruction does not rule out an actual-state corrector with signed
forcing, a t/u-weighted inequality, or additional source constraints.
No such corrector with paid endpoints is certified, and no integrated
counterexample to the actual WP84 theorem is claimed.

## 7. Spatial channel reduction and conditioning boundary

[D,R] has rank two, [D,Q] has the three-wedge six-column factorization
of the parent note, and [D,BR] has the improved rank-three factorization.
The six-by-six Gram here is an INDEX matrix of directional response
channels; DQ itself need not have matrix rank six.
For functions F(H), their displacement follows from the rational resolvent
identity or the polynomial Cayley commutator. Off-diagonal entries are
reconstructed from displacement generators divided by i-j. Mixed poles
can require BOTH conjugate generator families; Ward identities do not
license dropping one. Degrees <=3 at each pole give at most twelve
generator columns for a general mixed product. All these are O(d) vector
data; they are not six scalar temporal states or a dense matrix state law.

Insert these generators in Hadamard trace contractions in (2). Products
of two off-diagonal reconstructions have denominator (i-j)^2; an exposed
K2 resolvent weighting gives (i-j)^4 and the exact Fourier kernel

    S4(theta)=pi^4/45-pi^2 theta^2/6+pi theta^3/6-theta^4/24.

The ordinary displacement pairing uses S2=pi^2/3-pi theta+theta^2/2.
Finite-prime Toeplitz covariance weights remain in the corresponding
Fourier convolutions. Diagonal vectors, Hilbert-transform responses and
small generator Fourier matrices suffice to EVALUATE the interface;
this algebra supplies no distributional lower bound for their state averages.

For comparison only, unitary U gives directional conditioning envelopes

    ||DQ[B]||_(2,tau)<=K1 ||B||_(2,tau),
    ||D2Q[B,B]||_(1,tau)<=K2 ||B||_(2,tau)^2,
    K1=(2/a)sum_(j=1..3)j|qj|,
    K2=(4/a^2)sum_(j=1..3)j^2|qj|.

Both p and g factors have ||factor||op<=sqrt(Einf); their ranks and
channel counts are the same ceilings. The verifier reports conditioning
diagnostics for both. These generic upper envelopes are NOT used as an
adequate consumer theorem or a necessary-loss obstruction.

| Interface | p energy | complementary gap energy |
|---|---|---|
| displacement ceiling | six columns / three wedges | six columns / three wedges |
| direct response channels | six Gram indices, ten cross contractions | same ceilings |
| desired p-curvature square | positive Gamma1_p | negative Gamma1_g |
| diagnostic K1 | 9.84751281119 | 7.84523551670 |
| diagnostic K2 | 73.73595477662 | 47.45109198578 |
| endpoint information | p(H1) unknown; p(HU)<=Einf | gap(H1) is the desired unknown; gap(HU)>=0 |

The gap's smaller conditioning diagnostics do not compensate for its
reversed square sign by any proved inequality here.

## 8. Fixed-U reconnaissance and honest limit of the diagnostics

The script constructs actual sharp partial-translation quadrature matrices
for primes 2,3,5,7 in a finite SURROGATE L=5,d=4, carrier=1,
mean H1=I+sum C_p. It checks deterministic sharp states, random scalar
Loewner fields, and covariance Hessians. With 4096 seeded Gaussian samples,
E0 is about .39336. Sample integral diagnostics E_U-E0 are

| U | diagnostic accumulated integral |
|---|---:|
| 1 | -.01762 |
| 2 | -.02355 |
| 4 | .01886 |
| 8 | .17530 |
| 16 | .48132 |
| 32 | .91564 |
| 64 | 1.42334 |
| 128 | 1.94234 |
| 256 | 2.42796 |

The target is always Einf-.105=4.514021211293706... . No tested U
reaches it. This surrogate is NOT the frozen model or the actual growing-T
prime endpoint and cannot select a theorem U. In fact any starting state
with E0>.105 cannot reach the target under the global cap; searching larger
U in such a surrogate would be uninformative. Scalar H=1 gives an exact
example of this universal-state obstruction. No Monte Carlo datum is
promoted and no best certified finite U is obtained.

## 9. Exact remaining inequality and decision

For actual H_(T,u) and actual covariance, define

    P_T(U)=integral_0^U E Gamma1(H_(T,u))du,
    Err_T(U)=-integral_0^U Re E tau[Q_(T,u)* Z_Q(H_(T,u))]du.

The single reduced positive-energy error target is, for SOME FIXED finite U,

    liminf_T [P_T(U)-Err_T(U)] > Einf-21/200.             (4)

Equivalently the integrated cross error must be smaller than the actual
positive Gram contribution minus the target, with a strict uniform gap.
This is an EXPLICIT algebraic theorem interface, not a proved quantitative
bound: positivity of P alone supplies no useful numerical lower bound.
No separate absolute-value estimates of Xi_z, Xi_zz, Xi_zzz are required.
The model-relative deficit must still be <8711/2778200.

Decision B means only this direct-energy algebraic reduction. It does not
claim that the original inequality is essentially solved. Universal
pointwise sign mechanisms are blocked; actual-state integrated (4) remains
open. Decision A is unsupported, C would require a useful paid corrector
which is absent, and D would overstate the scalar counterexample as a
falsification of the actual integrated route. Tail cap remains CLOSED;
no small-ball, growing-U or raw-moment route is reopened.

Run python src/wp84_tail_capped_finite_u_curvature.py --recon. Exact scalar
certificates and structured Hessian/Ward/stencil regressions pass. Gap root
decimals, matrix tests and Gaussian samples are labeled diagnostics.
