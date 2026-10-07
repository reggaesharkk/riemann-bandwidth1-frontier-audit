# WP84 joint Gaussian Mehler master law

Decision **D â€” the drift-free master equation does not determine the prime-dependent characteristic boundary**. Two-copy drift elimination succeeds exactly. Gaussian layers can be merged after the already-established covariance substitutions. A finite consumer-parameter transport identity exists. But it is a homogeneous scaling identity with a singular t=0 boundary, not a closed state law determined by the scalar initial value. Exact finite Loewner counterexamples give identical scalar/noisy t=0 data and different terminal values while satisfying the same master equation.

Parent: 25694f1db77b95e2f47060dda48e806b70b36815. Branch: codex/c5-c6-attack-20261006. No raw-moment expansion, generic baseline comparison, individual-prime estimate, or universal Hermite norm bound is used. All earlier frozen results remain at their established scope. No >79 theorem or positive actual margin is claimed.

## 1. Master state and exact dictionary

Use a fixed real symmetric Loewner covariance C on field coordinates, and V(B)=E[W B W]. Let G1,G2 be centered jointly Gaussian Loewner matrices with covariance Sigma tensor C, where

    Sigma=[[v1,c],[c,v2]], v1>=0, v2>=0, c^2<=v1 v2.

Here v_i=sigma_i^2 are VARIANCES. Define

    X=s0 I+tP+G1, Y=s0 I+tP+G2,
    Phi_theta(X,Y)=Re tau(Q_theta(X)^* Q_theta(Y)),
    M_C(t,Sigma;theta)=E Phi_theta(X,Y), tau=tr/d.

The physical consumer is Q=eta P_cons(H)(H-zI)^(-3), with the frozen z=3142/2415+i(131/200), eta=|z|^3 and

    P_cons(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3.

The deterministic prime operator is denoted P and is not the polynomial P_cons. The finite parameter extension theta is specified below.

Exact dictionary at the scalarized terminal baseline:

    E_u=M_C(1,u[[1,1],[1,1]];theta),
    A_u(rho)=M_C(1,u[[1,rho],[rho,1]];theta),
    F_T(H_T)=lambda0 E_U+sum_j lambda_j A_U(rho_j)-E_delta+o_T(1)_background.

For the EXACT nonscalar background replace s0I by S throughout and retain the background error only when scalarizing. The singular rho=1 covariance means identical Gaussian copies, not independent copies with equal variances. The exact K=32 lower coefficients and upper witness I are copied into the certificate. None is reoptimized or replaced by synthetic data.

## 2. The two finite-T covariance maps are not identical

Bernoulli replacement uses prime-base groups B_p and

    V_B,T(B)=sum_p B_p B B_p.

Mehler quadrature uses ordinary-prime cosine/sine directions C_p/sqrt(2),S_p/sqrt(2) and

    V_Q,T(B)=(1/2)sum_p[C_p B C_p+S_p B S_p].

These are NOT exactly the same finite-T map. For one real scalar positive branch A=1, C=A+A*=2,S=i(A-A*)=0, giving V_B(1)=4 versus V_Q(1)=2. Their difference on ordinary primes is the same-sign/fast channel. Prime-base grouping also contributes the already-controlled proper-power square correction. The exact finite-map identity is

    C_p B C_p - (1/2)(C_p B C_p+S_p B S_p)
       = A_p B A_p+A_p^* B A_p^*.

Thus initially use the exact TWO-MAP covariance

    K_copy=v(t) [[1,1],[1,1]] tensor C_B,T
              +u [[1,rho],[rho,1]] tensor C_Q,T,
    v(t)=t(1-t).

The Bernoulli/Gaussian replacement fluctuation is shared across both copies because F(A_t) uses one baseline A_t. Independent replacement fluctuations in the two copies would change the observable. The two Gaussian layers are independent of each other; addition of their covariance is exact. If their maps differ, covariance addition does not justify replacing them by one scalar copy matrix times one map.

After the established resonant substitution, fast disposal and proper-power correction, both maps may be replaced by C_ref inside these fixed-word observables, with o_T(1) error. The merged reference copy covariance is then

    Sigma(t,u,rho)=[[v+u,v+u rho],[v+u rho,v+u]].

This is exact for the substituted reference ensemble, asymptotic for the original two-map ensemble. It has effective heat u_eff=v+u and correlation rho_eff=(v+u rho)/(v+u) when u_eff>0. Earlier uniform covariance transfer applies to this compact family for fixed U, using u_eff<=U+1/4.

No derivative of an o_T(1) value comparison is taken. In particular uniform Bernoulli/Gaussian value agreement does not by itself imply agreement of t derivatives, and the frozen order-two covariance comparison does not automatically compare covariance-Hessian observables, whose comparison would require higher derivatives. The master identity is derived independently in each named ensemble; only the observable values are transferred. Integrated transport may use endpoint identities without replacing individual derivative terms.

The extension of Bernoulli invariance to the COMPILED observable is direct: condition on its Mehler noises, replace the shared centered scalar coefficient of each B_p, and match its first two moments. The uniform third directional bound from WP84_COMPILED_MEHLER_PRIME_LINDEBERG yields error at most

    (5/4) C_F sum_p||B_p||op^3=o(1),

using E|xi_p-t|^3<=1 and E|sqrt(v)g|^3<=1/4. This is one replacement proof; it does not assume matrix entries become independent.

## 3. Exact covariance and mean derivatives

For a real field basis E_i, write H_XX=sum C_ij D_XX^2[E_i,E_j], H_YY analogously, H_XY=sum C_ij D_XD_Y[E_i,E_j]. Gaussian Price differentiation gives

    M_t=D_P=E[D_X Phi[P]+D_Y Phi[P]],
    M_v1=(1/2)E H_XX Phi,
    M_v2=(1/2)E H_YY Phi,
    M_c=E H_XY Phi.

The cross derivative has coefficient ONE because both symmetric off-diagonal covariance blocks vary. There is no extra rho in M_c. At the physical consumer these contractions are

    H_XX Phi=Re tau(Z_Q(X)^*Q(Y)),
    H_YY Phi=Re tau(Q(X)^*Z_Q(Y)),
    H_XY Phi=Re sum C_ij tau(DQ(X)[E_i]^*DQ(Y)[E_j]),
    Z_Q=sum C_ij D2Q[E_i,E_j].

These identities hold in the covariance interior and extend to singular boundaries through the corresponding Gaussian interpolation limits. Boundary derivatives are understood through covariance paths in the PSD cone; no inverse covariance is required.

## 4. Two-copy drift elimination

Define the centered radial response

    G_rad=E[D_X Phi[X-s0I]+D_Y Phi[Y-s0I]].

Since X-s0I=tP+G1 and Y-s0I=tP+G2, joint Gaussian integration by parts gives exactly

    G_rad=t D_P+v1 E H_XX Phi+v2 E H_YY Phi+2c E H_XY Phi
         =t M_t+2(v1 M_v1+v2 M_v2+c M_c).

Therefore, for t>0,

    D_P=[G_rad-2(v1 M_v1+v2 M_v2+c M_c)]/t.

The two-copy deterministic drift has been eliminated algebraically. The factor 2c is essential. An exact bounded Fourier-Gaussian probe verifies the Price factors and the radial identity; dropping one cross block fails.

For two named maps, the exact radial identity instead contains the sum of covariance Euler operators for Sigma_B and Sigma_Q. It reduces to the displayed one-map formula only after covariance substitution. No finite-T map equality is presumed.

## 5. Finite rational consumer dilation generator

Center the pole at s0 and write

    z=s0+zeta,
    Q_theta(H)=q0 I+sum_(k=1)^3 q_k(H-s0I-zeta I)^(-k).

At the physical parameter point, q_k=eta b_k, with b0=p3, b1=p2+3zp3, b2=p1+2zp2+3z^2p3, b3=P_cons(z). Keep q0,q1,q2,q3,zeta as independent finite complex consumer parameters during differentiation, then evaluate at the physical point. Their conjugates vary consistently. This extension keeps rational degree three; it is not an infinite pole-derivative hierarchy.

For R=(H-s0I-zeta I)^(-1),

    D_H R^k[H-s0I]=-k R^k-k zeta R^(k+1).

Define the REAL dilation vector field, expressed compactly in Wirtinger coordinates,

    D_cons=zeta partial_zeta+conj(zeta)partial_conj(zeta)
          +sum_(k=1)^3 k(q_k partial_q_k+conj(q_k)partial_conj(q_k)).

Then G_rad=-D_cons M. Equivalently, for r>0,

    theta_r=(r zeta,q0,r q1,r^2 q2,r^3 q3),
    Q_(theta_r)(s0I+r(H-s0I))=Q_theta(H).

The verifier checks the resolvent rescaling on a noncommuting rational 2x2 matrix, and the numerical actual-consumer check independently compares this finite parameter generator against the radial derivative.

## 6. Master equation

The exact drift-free identity is

    [t partial_t+2(v1 partial_v1+v2 partial_v2+c partial_c)+D_cons]M=0.   (M1)

For the exact two-map ensemble, replace the covariance Euler term by 2(Euler_SigmaB+Euler_SigmaQ). This is still a finite parameter identity.

On any differentiable covariance path Sigma(t),

    [d/dt+D_cons/t]M_path
       =(v1'-2v1/t)M_v1+(v2'-2v2/t)M_v2+(c'-2c/t)M_c.              (M2)

For the merged Bernoulli/Mehler path,

    [d/dt+D_cons/t]M(t,Sigma(t,u,rho))
      =-(M_v1+M_v2+M_c)
       -(2u/t)(M_v1+M_v2+rho M_c).                                 (M3)

There is no separate P contraction in (M1)-(M3). The right side of (M3) is the explicit same-copy plus mixed-copy covariance response, not an assigned numerical value. At u=0 this is the two-copy version of the historical bridge coefficient v'-2v/t=-1.

Parameter domain: 0<=t<=1, Sigma PSD with bounded entries for fixed U, fixed nonreal pole strip |Im zeta|>=a_min>0 around the physical point, and bounded consumer coefficients. Equation (M1) is regular for t>0 in this domain but characteristic access to t=0 does NOT stay in that pole strip. This distinction is decisive below.

## 7. Scalar and noisy boundary, and covariance evolution

The true zero-covariance boundary at t=0 is

    M(0,0;theta)=|Q_theta(s0)|^2.

At the limiting s0=1 physical consumer its exact value is

    17299960054265282494173877728425088361 /
    22001664087015817976445407410953228409.

It is not w0=1415/13891. No model-value identification is made.

For nonzero Sigma,

    M(0,Sigma;theta)=E Re tau(Q_theta(s0I+G1)^*Q_theta(s0I+G2)),

which is a Gaussian matrix expectation, not the scalar value above. Covariance interpolation from zero gives exactly

    M(0,Sigma)-M(0,0)
       =int_0^1[v1 M_v1(0,s Sigma)+v2 M_v2(0,s Sigma)
                                    +c M_c(0,s Sigma)]ds.

This generates the noisy scalar starting functional IF its covariance responses are controlled. It is not an autonomous scalar ODE giving those response values. The covariance map is explicit but the nonlinear resolvents inside its contractions remain random.

At general t the zero-covariance boundary is

    M(t,0;theta)=tau|Q_theta(s0I+tP)|^2.

Its values for t>0 are NOT supplied by the scalar t=0 boundary or by covariance interpolation.

## 8. Copy-space common and difference modes

For general Sigma, the eigenvalues are

    lambda_+/-=(v1+v2 +/- sqrt((v1-v2)^2+4c^2))/2.

For the merged equal-variance path the orthonormal transform (G1+G2)/sqrt(2),(G1-G2)/sqrt(2) diagonalizes it with

    lambda_+=2v+u(1+rho), lambda_-=u(1-rho).

Only the common mode contains Bernoulli replacement noise. Treating replacement noises as independent would wrongly add v to lambda_-.

The state-space heat generator in these modes is

    (1/4)[lambda_+(H_XX+H_YY+2H_XY)
                 +lambda_-(H_XX+H_YY-2H_XY)].

Equivalently partial_lambda+=(partial_v1+partial_v2+partial_c)/2 and partial_lambda-=(partial_v1+partial_v2-partial_c)/2. The variance derivatives have the previously displayed Price normalization.

## 9. Exact covariance insertion and finite-channel responses

The frozen reference field has

    C_aa=I/(4a_phi^2), C_ab=C_ba=0,
    C_bb=I/(6a_phi^2)-K2/(2a_phi^2 pi^2).

The project taper a_phi is distinct from the consumer pole height. The Hadamard covariance map is therefore, with A=C_aa,H=C_bb,

    V(B)=H odot B+(A odot JB)J-A odot(JBJ)
                 -J(A odot B)J+J(A odot BJ).

The generic finite-T formula also has the named mixed C_ab/C_ba terms; those vanish only in the substituted reference map. Current-prime arithmetic is not reopened.

Expand the covariance responses into the fixed resolvent words already derived in WP84_COMPILED_MEHLER_PRIME_LINDEBERG. Every response is a finite signed sum of tau(B X B Y) contractions. For arbitrary two words X,Y, the exact reference contraction is

    H_res(X,Y)=1/(6a_phi^2 d)sum X_iiY_ii
      -1/(2a_phi^2 pi^2 d)sum_(i!=j)X_ijY_ji/(i-j)^2
      +1/(4a_phi^2 d)sum {
          (JX)_ii(JY)_ii+(XJ)_ii(YJ)_ii
          -(JXJ)_iiY_ii-X_ii(JYJ)_ii}.

Consequently the exposed state is a finite collection of diagonal word/J-word pairings and propagated rank-two generator channels, with the single BR rank-three sharpening where applicable. The mixed-copy words require both resolvents. They cannot be identified with one-state Stieltjes derivatives.

Keep the exact three-channel Gram contraction for the consumer powers. K2-weighted displacement Grams cancel to off-diagonal Hilbert products with their diagonal subtraction. D2 beta terms already containing a K2 weight yield an S4 generator contraction; no second cancellation removes that weight. Elementary Fourier channels remain 2x2, and individual BR primitives 3x3. A concatenated whole mixed word can have more generator columns. It is not correct to call the entire response vector a single 3x3 matrix.

This is finite ALGEBRAIC channel structure. The channel entries still depend on lattice position, Fourier argument, Gaussian realization and growing section size. Finite displacement rank does not give a fixed-dimensional closed ODE for their averages. Differentiating their evolution exposes additional resolvent/J/Hadamard word responses. Neither rank identities nor Gram compression express those averages as functions of a few already-certified numbers.

## 10. Compiled dual: no exact master cancellation

Apply (M2) or (M3) linearly to

    L(t)=lambda0 M_path(t,U,1)+sum_j lambda_j M_path(t,U,rho_j)
                    -M_path(t,delta,1).

The covariance derivatives are evaluated at DIFFERENT Sigma(t,U,rho_j). Their coefficients cannot be summed as though they had a common argument. All signed terms remain grouped before estimates.

The exact certificate records q_lower(0),q_lower(1),q_lower(2), q0-1 and q0-q1. The first two are near one, but q0-1 and q0-q1 are nonzero rational numbers. At zero noise the compiled observable is (q0-1)tau|Q(s0I+tP)|^2, whose dilation and baseline derivatives do not vanish identically. Small-noise drift/diagonal/cross responses are weighted by these distinct chaos multipliers; there is no exact all-state elimination of a common or difference covariance mode. No exact resonant, endpoint, or K2 cancellation beyond the frozen cutoff inequality is found.

For scale, q0-q1 is approximately -7.94e-14 and q0-1 approximately -1.00e-8. This is strong matching on those low chaos multipliers, but not a uniform suppression theorem for covariance modes evaluated at different arguments. A small residual at a regression state is not a paid uniform bound. A purported exact cancellation based on rounded dual coefficients would fail the rational checks.

## 11. Why the master PDE does not close the state law

Equation (M1) follows from the exact scaling identity

    M(r t,r^2 Sigma;theta_r)=M(t,Sigma;theta).

It is a homogeneous Euler identity, valid for EVERY deterministic P. Along its characteristics, the invariants include

    Sigma/t^2, zeta/t, q_k/t^k.

Following a physical characteristic to t=0 scales zeta to zero and leaves the fixed nonreal pole domain. Although q_k also tends to zero, the ratio q_k R^k need not tend to zero because R diverges on the same scale. Thus the characteristic limit is not the continuous scalar boundary |Q_theta(s0)|^2 at a fixed regular theta.

Explicitly, for fixed Sigma_*,theta_*,

    X_t=s0I+t[P+G_*],
    Q_(theta_t)(X_t)=Q_(theta_*)(s0I+P+G_*),
    theta_t=(t zeta_*,q0,t q1,t^2 q2,t^3 q3).

The entire unknown terminal response survives unchanged as t tends to zero along this singular characteristic. Drift elimination removed an exposed contraction, but did not erase the deterministic prime direction. The exact first nonclosing object is this prime-dependent characteristic boundary value (equivalently the zero-covariance response M(t,0;theta) for t>0), together with the covariance evolution of its channel responses. It is not provided by scalar initial data.

Exact nonuniqueness test: with d=1,s0=1, the physical consumer and the same covariance map V (reference scalar variance 1/6), choose synthetic Loewner directions P=0 and P=1. For ALL Sigma and ALL regular consumer parameters their t=0 master functions agree, because P is absent there. Both satisfy (M1). At t=1,Sigma=0 they equal |Q(1)|^2 and |Q(2)|^2, respectively, and these differ exactly. The certificate gives both rational values.

A strengthened d=2 test uses P=diag(1,-1) versus diag(2,-2). Both have trace zero, the same scalar/noisy t=0 boundary with the same project covariance, and displacement rank zero. Their zero-covariance terminal energies also differ exactly. These are counterexamples to uniqueness of the proposed PDE/boundary mechanism in the Loewner class, not counterexamples to a prime-specific theorem. The frozen large-heat tail cap does not distinguish these examples: for nondegenerate Gaussian noise at fixed dimension their large-variance consumer limit is the same constant-tail value. It therefore does not repair the finite-covariance characteristic boundary. Adding prime-specific characteristic response information could select the actual solution; that is the unproved law, not a consequence of the master identity.

## 12. Semigroup, sign tests and adjoint boundary

For a fixed mean A, the exact Gaussian state-space semigroup is

    M=e^[(v1 H_XX+v2 H_YY+2c H_XY)/2] Phi_theta |_(X,Y)=(A,A),
    A=s0I+tP.

It is a Gaussian Markov heat semigroup on the field/state coordinates. Positivity preservation and sup-norm contractivity hold for nonnegative/bounded initial functions on that FULL space. They do not imply monotonicity of this consumer in covariance, or determine its value along an unknown mean direction.

Hostile scalar test: for f(x)=|Q(x)|^2, the exact f''(1) is negative while f''(2) is positive. Hence heat-energy growth is not universally monotone or convex. The certificate records exact curvatures at several points. Complete positivity of V and Gram positivity control contraction/norm structure, not the needed signed consumer deficit. Mehler positivity for equal marginal variances remains frozen; it does not make the signed weak-dual combination a positive operator.

A target-aware adjoint of (M1) would retain a boundary pairing at the singular characteristic. Lyapunov or LRSC weak-duality methods cannot discard that unknown term. The finite consumer parameter set does not turn the growing random Fourier/channel state into a closed finite state. No compact finite certificate domain with fully supplied boundary conditions has been obtained.

## 13. Regression evidence

The exact verifier checks Price factors, radial IBP, rational degree-three rescaling, copy-space diagonalization, and the characteristic-boundary counterexamples. It independently rejects omission of a cross covariance block. Existing Gaussian invariance, quadrature covariance, Hadamard covariance and characteristic-rescaling gates passed.

Direct Gauss-Hermite quadrature uses the ACTUAL rational consumer on scalar and noncommuting 2x2 Loewner regression states, at orders 48 and 96. At order 96 the radial master residual is below 7e-17, covariance finite-difference discrepancies below 7e-10, and consumer-dilation discrepancies below 6e-11. These are numerical regressions, not interval enclosures or a certified master solution generated from t=0.

The +0.000429209 synthetic geometric benchmark is retained exactly as an OU weak-dual regression. Its two abstract endpoint chaos sequences have no established realization as this same rational consumer, deterministic P and project Gaussian covariance. Therefore there is no valid master-PDE regression on that benchmark without an additional embedding theorem. It is not silently supplied as boundary data.

## 14. Complete margin ledger and final gate

The frozen ledger remains

    epsilon=8711/2778200,
    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000,
    w0=1415/13891,
    initial payment <=53503/66000000 for K=32,delta=1/100000.

Background scalarization is o(1), charged once. Compiled Bernoulli-to-Gaussian replacement is bounded by (5/4)C_F times the block cube mass and is o(1). The prior Taylor/common-state route has its own cube remainder; it is an alternative representation, not an additional copy of the same invariance loss. Resonant and proper-power covariance substitutions, fast disposal and Mehler covariance transfer are o(1) for fixed U and fixed dual. The all-n weak-dual inequality is exact; cutoff slack remains implicit in the target. Initial layer and initial chaos costs remain paid once. Frozen adjoint residual and physical tail payment add zero.

None of those vanishing errors pays the missing characteristic-boundary response. If a future theorem supplies the grouped lower value l and any nonvanishing certified response error e, the margin is

    8711/2778200-[E_inf-w0-l]-53503/66000000-e.

Equivalently l-e must exceed

    83446820694177651440799215197979 /
    18482819123692026401760000000000.

There is no certified l, chosen actual U, or positive actual margin. The exact master identity alone cannot certify this threshold because it admits the distinct terminal responses above from identical regular scalar t=0 data.

Final decision D: the first nonclosing variable is the prime-dependent singular characteristic boundary of the master response. H_T is no longer an unexplained external argument in the formulas: its deterministic prime direction is explicitly encoded in that boundary. Removing its exposed drift did not determine the boundary. Strict >79 remains OPEN.

## Replay and provenance

    python src/wp84_joint_gaussian_mehler_master_law.py
    python src/wp84_mehler_weak_dual_certificate.py notes/WP84_JOINT_GAUSSIAN_MEHLER_MASTER_LAW_CERTIFICATE.json

The source coverage contains paths and SHA256 hashes for the requested historical Gaussian/current-covariance notes, the three frozen Mehler/reference/compiled audits, the characteristic note, and associated verifiers. Their full derivations and verifier code were used at the scope stated above. The new certificate contains exact dual witnesses, rational counterexamples, copy-mode formulas, diagnostic residuals and the explicit false consumer-certification flag.
