# Integrated grouped cross error: Stein identities, chaos shift, and the actual-state gate

Date: 2026-10-07. Parent: 353d51290ad43c66190ca80e9d9705583e58a25e.
Decision **B: one actual-coefficient integrated chaos inequality remains**.
This is a change of analytic interface, not a quantitative closure.
The universal Hardy estimate below is sharp but insufficient. No paid
Loewner-specific corrector is found. Strict >79 remains OPEN.
Consumer c=3142/2415, a=131/200 and all previous certificates are unchanged.
No push, new consumer, pointwise p-sign search, or tail theorem attack.

## 1. Exact radial Stein normalization

Let W=sum_(j=1..m) g_j B_j with independent STANDARD REAL Gaussians.
For actual quadrature B_j=C_p/sqrt2,S_p/sqrt2; m=2 pi(N).
Use inner product <A,B>=tau(A*B), tau=tr/d, H_u=H+sqrt(u)W,
F_u(g)=Q(H_u). Define E(u)=E||F_u||2^2, and Z_Q=sum_j D2Q[B_j,B_j].
For u>0, direct differentiation gives exactly

    E'(u)=1/sqrt(u) Re E<Q,DQ[W]>.                       (1)

There is NO extra 1/2: differentiating sqrt(u) supplies 1/(2sqrt u),
and differentiating the squared energy supplies 2. This uses the SAME W
as the state. By Gaussian integration by parts, each term obeys

    E g_j <Q,DQ[B_j]>
       =sqrt(u) E[<DQ[B_j],DQ[B_j]>+<Q,D2Q[B_j,B_j]>].

Taking real parts and summing gives exactly E'=G+Gamma2, where
G=E sum_j||DQ[B_j]||2^2 and Gamma2=Re E<Q,Z_Q>.
These are the Hessian definitions of the parent audit. Its Xi stencil
is the same identity, with Xi primitive normalization B=Xi_z/2.
No fresh-noise Hessian average is confused with the radial W in (1).

A second compressed exact form, using the Gaussian score, is

    E'(u)=1/(2u) E[(|g|^2-m)||F_u||2^2].                 (2)

This is a SIGNED score, not a positive quantity. The verifier compares
radial, Hessian, analytic-stencil and direct numerical-difference
regressions; the parent exact scalar stencil certificate is retained.

## 2. Mean, variance and sharp Poincaré constant

Put M(u)=E F_u, mu(u)=||M(u)||2^2,
V(u)=E||F_u-M(u)||2^2=E(u)-mu(u). Exactly

    M'= (1/2) E Z_Q,
    mu'=Re <M,E Z_Q>,
    V'=G+Re E<F_u-M,Z_Q>,
    Gamma2=mu'+V'-G,
    E'=mu'+V'.                                          (3)

At u=0, V(0)=0 and mu(0)=E(0). In the exact Hilbert space of complex
d-by-d matrices with normalized HS norm, Gaussian Poincaré is

    V(u)<=E sum_j||partial_(g_j)F_u||2^2=u G(u).          (4)

The constant is EXACTLY 1. One can apply the real scalar inequality to
real and imaginary coordinates, or prove (4) directly by the chaos
expansion below. It is sharp on first chaos. It bounds variance at an
endpoint, not its derivative; differentiating this inequality is invalid.

## 3. OU generator and number-operator naming

Use precisely the requested notation Nrad=g dot grad_g,
L_OU=Delta_g-Nrad. Introduce separately the CHAOS number operator
Nchaos=-L_OU; Nrad and Nchaos are NOT the same operator.

    Delta_g F_u=u Z_Q,
    Nrad F_u=2u partial_u F_u,
    Re E<F_u,L_OU F_u>=-u G(u).

Thus

    Gamma2=-G+(1/u) Re E<F_u,Nrad F_u>,
    J(u):=Re E<F_u,Nrad F_u>=u E'(u).                   (5)

The negative Dirichlet term cancels the positive Hessian square when
the radial term is substituted. This is an exact cancellation, not a
gain in the theorem budget. Calling Nrad positive would lose the
Laplacian shift and would contradict the parent's scalar falsifier.

## 4. Hermite coupling matrix and exact evolution

Use orthonormal probabilists' Hermites h_alpha(g)=prod H_(alpha_j)(g_j)
/sqrt(alpha_j!). Expand F_u=sum_alpha f_alpha(u)h_alpha in the matrix
Hilbert space. Finite d and a fixed nonreal pole give Gaussian Sobolev
regularity needed for the following forms. M=f_0 and

    E=sum_alpha||f_alpha||2^2,
    V=sum_(alpha!=0)||f_alpha||2^2,
    D(u):=uG=sum_alpha |alpha| ||f_alpha||2^2,
    Cchaos(u):=u Gamma2
      =Re sum_(alpha,j) sqrt((alpha_j+1)(alpha_j+2))
          <f_alpha,f_(alpha+2e_j)> .                     (6)

The Laplacian couples ONLY levels differing by two. This includes
the level-0/2 mean coupling; discarding it is not legitimate.
The exact infinite weighted-shift matrix has entries

    L_(alpha,beta)=sum_j 1_(beta=alpha+2e_j)
                     sqrt(beta_j(beta_j-1)),
    Jcross=(L+L*)/2, Nchaos_(alpha,beta)=|alpha| delta_(alpha,beta).

Gamma1=D/u, Gamma2=<f,Jcross f>/u, and E'=(D+Cchaos)/u.
Taking coefficients in the radial identity gives

    2u f_alpha'=|alpha| f_alpha
       +sum_j sqrt((alpha_j+1)(alpha_j+2)) f_(alpha+2e_j). (7)

Consequently the evolution is an infinite coupled system; no finite
state closure is assumed. In rotation-harmonic sectors of degree ell,
the ladder indexed by k>=0 has degree n=ell+2k and lowering coefficient

    b_(k,ell)=sqrt(2k(2k+2ell+m-2)).

Its symmetric Jacobi matrix has off-diagonals b_(k,ell)/2 and zero
diagonal; Nchaos has diagonal ell+2k. Degenerate absent sectors (e.g.
nonexistent higher spherical harmonics in dimension one) are omitted.
The scalar verifier checks normalized Hermite lowering and the radial
identity exactly and reports a truncated consumer-chaos diagnostic.

## 5. Sharp whole-chain Hardy inequality and its limitation

For any Hilbert-valued Gaussian Sobolev F, let
D=E||grad F||2^2, C=Re E<F,Delta F>, e=E||F||2^2.
Integration by parts gives

    C=(1/2)E[(|g|^2-m)||F||2^2]-D.

The whole-chain completion of squares is

    E||grad F-gF/2||2^2
       =D-(1/4)E[|g|^2||F||2^2]+(m/2)e>=0.

Together with |g|^2>=0 this proves the rigorous sharp form envelope

    -D-(m/2)e <= C <= D+(m/2)e,
    |C|<=D+(m/2)e.                                      (8)

This is not level-by-level Cauchy-Schwarz. The coefficient 1 in front
of D cannot be decreased with any finite additive e constant: normalized
F=exp(t|g|^2), t<1/4, has D/e=4t^2m/(1-4t) and C-D=2tm e;
as t->1/4, C/D->1. With that coefficient 1, the additive m/2 is optimal
on the upper side by the same sequence. On the lower side, concentration
near g=0 gives C+D approaching -m e/2. Smooth bounded truncations of
these witnesses give the same limiting form ratios, so mere boundedness
of a functional does not remove the obstruction.

There is NO pure relative bound by D on the full space: a constant
component coupled to level two makes the ratio arbitrarily large.
Even after removing the mean, a dimension-free bound fails. In the radial
level-2/4 sector, the coupling is 2sqrt(m+2), while the number energies
are 2||f2||^2+4||f4||^2. Its optimal two-level ratio is

    sup |C|/D=sqrt((m+2)/8).                             (9)

For m=8 it already exceeds 1; it grows like sqrt(m). This is a lower
bound for the full mean-free relative norm, not a claim that the two-level
constant is the sharp norm of every infinite sector.

Applying (8) to F_u yields only
|Gamma2|<=G+m E/(2u). Its dimension factor m=2pi(N) grows and the
1/u term is singular at zero. It cannot be charged to the fixed
8711/2778200 cushion. This rigorously blocks the UNIVERSAL Hardy
estimate as a sufficient budget argument. It does not falsify a special
inequality on the actual coefficients f_(T,alpha)(u).

## 6. Integrate first: all telescoping terms exposed

For any 0<epsilon<U, integrate (3) or (7) BEFORE bounding a channel:

    integral_epsilon^U Gamma2 du
       =mu(U)-mu(epsilon)+V(U)-V(epsilon)
          -integral_epsilon^U G du.

All quantities are smooth at u=0 in the original heat functional, and
V(0)=0, so the exact endpoint identity is

    integral_0^U Gamma2 du
       =mu(U)+V(U)-E(0)-P(U), P(U)=integral_0^U G du.     (10)

Equivalently, in the compressed Stein form the integrand is
(J-D)/u. Termwise coefficient integrals must be understood via Sobolev
truncation; arbitrary rearrangements of a conditionally convergent sum
are not needed for (10). Equation (10) is the maximal unconditional
telescoping identity here. It is exactly E(U)-E(0)-P(U), not an independent
lower bound: estimating its endpoint E(0) by the desired conclusion would
be circular. The integration does not turn the shift form into a positive
number form for free.

## 7. Corrector audit, including the H=1 test

Let D=uG and J=uE'. Candidate correctors are rational linear
combinations alpha V+beta D+gamma J+delta mu. Exactly,

    E'+C'=(1+alpha)V'+(1+delta)mu'+beta D'+gamma J'.

At zero, V=D=J=0, mu=E(0); at U the cap gives
0<=V<=Einf, 0<=mu<=Einf, and D>=V. Using the parent's fixed-pole
directional envelopes gives D<=U K1^2 sum_j tau(B_j^2) and an analogous
finite bound for |J|. These endpoint bounds are explicit but are not
small enough, or of a favorable sign, to pay the model cushion.

For scalar H=1 and covariance X/6 the EXACT initial derivatives are

    E'=-2.53403297402579277...,
    V'=D'=1.88355628303141759...,
    mu'=-4.41758925705721036...,
    J'=E'.

Thus E'+V'=E'+D'=-.650476690994375175...; -V and -D expose the
negative cross term. Adding J doubles the negative initial derivative.
The mean corrector -mu gives E'-mu'=V', which is positive initially
but not universally positive: for the scalar consumer V starts at zero,
is nonzero, and tends to zero in the elementary fixed-scalar large-noise
limit, so V' must change sign. This uses no new uniform-tail theorem.
The variance corrector -V gives mu', also negative at H=1.
The combination -mu-V=-E gives zero identically and has unknown E(0)
in its endpoint. It is vacuous, not a discovered Lyapunov inequality.

The identity obtained from -mu is integrably nonnegative since
integral V'=V(U)>=0, but its endpoint mu(0)=E(0) is precisely the
unknown endpoint defect. It supplies no numerical model comparison.
No rational combination with a proved positive forcing and PAID endpoints
is obtained. The derivative inequalities for arbitrary combinations are
not inferred from V<=D. A state-specific corrector remains possible.

## 8. Insert Loewner structure only after this Gaussian algebra

Use the same B_j directions as the parent finite-energy audit: rank[D,R]
<=2, rank[D,Q]<=6, rank[D,BR]<=3, three skew wedge pairs, exact
Toeplitz/Hadamard covariance, and the S4 reconstruction of exposed
K2-weighted off-diagonal products. The six-response Gram and grouped
ten-contraction cross term remain valid. Stein keeps their B_j sum
contracted until after the Gaussian cancellations, rather than taking
separate absolute values of covariance channels.

These facts make each coefficient or response evaluation a structured
finite-channel problem. They do NOT project the Gaussian chaos chain onto
a finite-dimensional subspace: rational Q has infinitely many Hermite
coefficients. Nor do they bound m by the spatial displacement rank.
The direction count m in (8)-(9) is the independent Gaussian coordinate
dimension, not rank[D,Q]. Replacing m by six has no justification.

## 9. Finite-T diagnostic protocol and evidence limits

The verifier uses increasing feasible T=128,256 with
L=log(T/(2pi)), N=floor(exp(L-sqrt L)), full sharp grid
d=floor(T L/(2pi)), actual carrier T, coefficients
-Lambda(n)/(L sqrt n), all retained prime powers in the mean,
and ordinary-prime cosine/sine directions divided by sqrt2 in W.
It uses s0=a_phi=1 (sharp normalization), NOT an asserted exact smooth
taper/background equality. There is no adaptive good-section selection.
This is substantially more faithful than the prior arbitrary L=5 carrier=1
surrogate, but still not a promoted asymptotic WP84 state theorem.

For U=1,2,4,8,16 it reports P_T, Err_T, their difference, maximum
quadrature-node ratio, integrated ratio, V(U), mu(U), U G(U), and the
independent sample endpoint difference E(U)-E(0). Gaussian sampling and
Legendre quadrature are diagnostic, with NO interval error certification.
Sampling makes the Hessian-integral and path-endpoint estimates differ;
that discrepancy must not be presented as a violation of Stein.
Initial defects near .4 exceed .105 in these small sections, so these
states cannot certify the target even by indefinitely increasing fixed U.
No best theorem U is inferred from them. Consumer a is not reoptimized.

Results with 64 seeded samples and 12 Legendre nodes (all numerical):

| T / d | U | P | Err | P-Err | max node Err/G | Err/P | V(U) | mu(U) | U G(U) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 128 / 61 | 1 | .810708 | .833850 | -.023142 | 1.11844 | 1.02855 | .184405 | .210754 | .747172 |
| 128 / 61 | 2 | 1.506543 | 1.513888 | -.007345 | 1.11426 | 1.00488 | .221222 | .186251 | 1.301473 |
| 128 / 61 | 4 | 2.678372 | 2.619698 | .058674 | 1.10577 | .97809 | .291934 | .179303 | 2.128402 |
| 128 / 61 | 8 | 4.525711 | 4.292882 | .232829 | 1.09059 | .94855 | .445425 | .206191 | 3.250265 |
| 128 / 61 | 16 | 7.247538 | 6.727373 | .520164 | 1.06797 | .92823 | .684217 | .291409 | 4.648927 |
| 256 / 151 | 1 | .880755 | .899687 | -.018932 | 1.04669 | 1.02150 | .194403 | .221505 | .809118 |
| 256 / 151 | 2 | 1.636551 | 1.648870 | -.012319 | 1.04307 | 1.00753 | .237929 | .204040 | 1.416183 |
| 256 / 151 | 4 | 2.909721 | 2.850286 | .059435 | 1.03716 | .97957 | .316532 | .209590 | 2.309403 |
| 256 / 151 | 8 | 4.917700 | 4.642331 | .275369 | 1.02874 | .94400 | .483396 | .243894 | 3.541798 |
| 256 / 151 | 16 | 7.889487 | 7.219511 | .669976 | 1.02161 | .91508 | .755937 | .335610 | 5.077126 |

V(0)=0 in both states; mu(0)=.42200845 and .40589639 respectively.
The maximum above is over quadrature-node EXPECTED estimates, not the
supremum of pointwise sample ratios. At U=16 the independent endpoint
integrals are .553617 and .685651, versus Hessian-integral estimates
.520164 and .669976. These discrepancies illustrate why sampling is not
a certified integrated bound. The target remains 4.514021211293706... .

## 10. One precise actual-coefficient inequality and decision

Let f_(T,alpha)(u) be the actual normalized-HS Hermite coefficients and
D_T,C_T the exact forms (6). The remaining sharp-chain theorem is

    THERE EXISTS A FIXED FINITE U SUCH THAT
    liminf_(T->infinity) integral_0^U [D_T(u)+C_T(u)]/u du
      > 7761139416076220170204368647089/1680256283972002400160000000000
          -21/200.                                      (11)

The original integrated cross-error condition is equivalently
liminf[P_T(U)+integral C_T/u]>Einf-.105. A source-closed inequality
on THIS actual chain, with paid mean/variance endpoints, is required;
generic Gaussian form inequality (8) is insufficient. The exact identities
do not reduce (11) to a bound independent of the actual endpoint law.
Model-relative total deficit must remain <8711/2778200.

Decision B is ONLY a precise chaos-interface reduction. The universal
Stein/Hardy budget mechanism is obstructed, but declaring the entire
actual Loewner route blocked (D) would require an obstruction on its
special coefficients, which is not established. A is not proved and C
would require a useful corrector, which is absent. >79 remains OPEN;
tail elimination remains CLOSED. The next theorem is (11), not a
small-ball estimate, finite M_s, raw moment law or new consumer.

Verification: python src/wp84_integrated_cross_error_stein_chaos.py --recon.
The parent exact Hessian/Xi regression remains unchanged. New exact Hermite
and sharp-form witnesses pass; radial quadrature and prime diagnostics are
explicitly numerical. All previous audit commits remain ancestors.
