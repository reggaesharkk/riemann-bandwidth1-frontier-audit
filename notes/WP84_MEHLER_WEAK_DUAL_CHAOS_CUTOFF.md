# WP84 Mehler weak-dual chaos cutoff

Decision **B**: the two-copy noise-covariance transfer closes under the frozen sharp-state PNT/BV and field bounds. Exact all-integer cutoff witnesses also close. What remains is a certified finite list of reference Mehler measurements, including the actual deterministic background H_T, strong enough to pay the consumer deficit. No actual consumer margin or strict >79 conclusion is certified.

## Evidence boundary and frozen consumer

Parent: 0b4dbdca63dca5dcba1f6c1f1548181301542e8c, branch codex/c5-c6-attack-20261006. This is an additive local audit. The previous direct projected-energy substitution required derivatives through 2K+2. We do not prove that lemma; this representation replaces its observable.

Keep the exact previous telescope:

    J + Phi_(K+1) + Phi_(K+2) = S_K(U) - S_K(delta).

Here tau=tr/d, f_u=Q(H_T+sqrt(u)W), with standard REAL Gaussian coordinates, and

    c=3142/2415, a=131/200, z=c+ia, eta=(c^2+a^2)^(3/2),
    P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3,
    Q(H)=eta P(H)(H-zI)^(-3).

The frozen constants are

    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000,
    w0=1415/13891,
    epsilon=8711/2778200.

For a certified lower difference l, the remaining test is

    D_up=E_inf-w0-l,
    D_up + delta*kappa_*[sqrt(E_inf) K2 + K1^2/(K+1)] < epsilon.

This is the grouped full remaining ledger from the parent audit. Earlier frozen costs are already represented in epsilon, not waived. There is no separate flux payment after using the exact telescope. Eventually kappa_*<=1/2; the certified caps sqrt(E_inf)<43/20, K1<10, K2<74 give the convenient rational initial-layer payment

    c0_up=delta/2[(43/20)74+100/(K+1)].

The physical large-u tail cap remains frozen. This note makes no independent filtered-to-sharp substitution and does not replace the deterministic mean by a continuum mean.

## 1. Exact Mehler representation and Abel inequalities

In the matrix-valued Gaussian L2 space, orthogonal Hermite projection gives

    f_u=sum_(n>=0) f_(u,n),
    a_n(u)=E tau(f_(u,n)^* f_(u,n))>=0,
    E_u=sum_n a_n(u), S_K(u)=sum_(n<=K) a_n(u).

For g,g' independent standard real Gaussians, conditional expectation under rho g+sqrt(1-rho^2)g' multiplies every homogeneous Hermite chaos of degree n by rho^n. Orthogonality and L2 convergence therefore give exactly

    A_u(rho)=Re E tau(Q(H1)^* Q(H2))=sum_n rho^n a_n(u).

The expectation is real and nonnegative. Its endpoints are A_u(1)=E_u and A_u(0)=tau((E Q)^*(E Q)); the latter is not |E tau Q|^2. Singular covariance causes no issue: use any square root on its support, or redundant standard coordinates.

Since rho^n<=1 below K and <=rho^(K+1) above K,

    A_u(rho)<=S_K(u)+rho^(K+1)[E_u-S_K(u)],
    S_K(u)>=[A_u(rho)-rho^(K+1)E_u]/[1-rho^(K+1)].

Since rho^n>=rho^K for n<=K,

    S_K(u)<=A_u(rho)/rho^K.

Subtracting the upper bound at delta from the lower bound at U gives the requested one-rho difference bound. The verifier tests atoms at K, K+1 and very large n, geometric tails, and two-point masses.

## 2. Exact low-order covariance interpolation

Use common field coordinates xi=(a_i,h_i), not different unrelated Gaussian parameterizations. Put

    W(xi)=M_h+[M_a,J], J_ij=1/[pi(j-i)] for i!=j, J_ii=0,
    C_theta=(1-theta)C_T+theta C_ref,
    Cov(X,Y)=[[C_theta,rho C_theta],[rho C_theta,C_theta]],
    Delta C=C_ref-C_T.

The block covariance is positive semidefinite for 0<=rho<=1 and every theta; no covariance inverse is used. Both copies keep the same H_T, including proper powers and all deterministic background terms. Let H1=H_T+sqrt(u)W(X), H2=H_T+sqrt(u)W(Y), and F=Re tau(Q(H1)^*Q(H2)). Real Gaussian Price interpolation is

    d_theta E F = (1/2)sum_ij Delta C_ij
                    E[F_XX,ij+F_YY,ij+2rho F_XY,ij].

For E_i=W(e_i), these derivatives are

    F_XX,ij=u Re tau(D2Q(H1)[E_i,E_j]^*Q(H2)),
    F_YY,ij=u Re tau(Q(H1)^*D2Q(H2)[E_i,E_j]),
    F_XY,ij=u Re tau(DQ(H1)[E_i]^*DQ(H2)[E_j]).

Exchange of copies combines the first two terms. Writing Z_Delta Q=sum Delta C_ij D2Q[E_i,E_j],

    d_theta A=u Re E tau(Q(H1)^* Z_Delta Q(H2))
                +u rho Re sum_ij Delta C_ij
                            E tau(DQ(H1)[E_i]^*DQ(H2)[E_j]).

Maximum derivative order is **2 per Q factor**, and total order is actually 2: (2,0), (0,2), or (1,1). K is absent. The rho=1 endpoint is the one-copy energy comparison. The symbolic replay independently checks the real 1/2 factor, the rho cross block, a noncommuting complex matrix polynomial, and a singular covariance endpoint. Removing the cross block is rejected.

## 3. The contracted order-two PNT/BV proof

The new ingredient is a two-word variation bound, allowing words from either correlated state. Define

    B(X)=||X||op, Dc(X)=||[D,X]||_1/d,
    g_s^+(M,N)=tau(M U_s^+ N U_s^-),
    g_s^-(M,N)=g_s^+(N,M).

The Fourier displacement compressions are contractions. Their exact derivatives are

    (U_s^+)'=2pi i D U_s^+ - e(s)1^T,
    (U_s^-)'=-2pi i U_s^- D - 1 e(s)^*,
    ||e(s)||=||1||=sqrt(d).

Cyclicity collapses the two D terms BEFORE taking norms:

    (g_s^+)'=2pi i tau(U_s^- M U_s^+ [D,N])
              -tau(M e(s)1^T N U_s^-)
              -tau(M U_s^+ N1 e(s)^*).

Consequently

    sup_s |g_s^++g_s^-| <= 2 B(M)B(N),
    Var_s(g_s^++g_s^-) <=
      2pi[B(M)Dc(N)+B(N)Dc(M)]+4 B(M)B(N).

There is no d loss. This identity holds for arbitrary noncommuting complex M,N; the replay checks it exactly on a noncommuting 3x3 example and checks the reverse branch by cyclic swap. The proof itself follows by the displayed derivative identities in every dimension.

Dc(XY)<=B(X)Dc(Y)+Dc(X)B(Y). For R_i=(H_i-zI)^(-1),

    B(R_i^r)<=a^(-r),
    Dc(R_i^r)<=r a^(-r-1)Dc(H_i),
    B(Q_i)<=sqrt(E_inf), Dc(Q_i)<=K1 Dc(H_i),
    Dc(H_i)<=(2/pi)||a_state,i||_2/sqrt(d).

The rank identities rank[D,R_i]<=2 and rank[D,Q_i]<=6 are statewise and give three wedge pairs. They remain valid separately for both copies; averaging is not claimed to preserve rank. The two-word bound also works for products containing both copies.

Let p_j be the coefficients of P and expand

    Q=eta sum_(k=0)^3 b_k R^k,
    b0=p3,
    b1=p2+3zp3,
    b2=p1+2zp2+3z^2p3,
    b3=P(z).

Keep the exposed covariance pair contracted. With Bc=(U+ + U-)/sqrt(2), Bs=i(U+ - U-)/sqrt(2),

    Bc X Bc+Bs X Bs=U+ X U-+U- X U+=V_s(X).

Carrier rotation cancels at this stage. There is no derivative of an uncancelled 2T carrier. The contracted same-copy Hessian is

    Z_s Q2=2eta sum_(k=1)^3 b_k
              sum_(p+q+r=k+2; p,q,r>=1) R2^p V_s(R2^q) R2^r.

After multiplying by Q1^* and cycling, every scalar kernel is g_s^++g_s^- with

    M=R2^r Q1^* R2^p, N=R2^q.

For the mixed DQ1^*DQ2 term, the words are

    M=R2^t (R1^*)^q, N=(R1^*)^p R2^r,
    p+q=k+1, r+t=l+1, k,l=1,2,3; all indices positive.

No other Gaussian direction matrices remain inside these words. This is precisely the difference from direct chaos-projector differentiation. Applying the displayed BV bound to this finite list establishes the required contraction without any K-dependent hierarchy.

The existing r=1,2 contracted bounds are sufficient:

    M1<=u kappa_* K1^2,
    M2<=u^2 kappa_* beta_* K2^2,
    ||Z||<=beta_* K2,

with eventual kappa_*<=1/2, beta_*<=5/2. The K2 Gram cancellation, T12/S4 grouping and Hadamard/Schur structure are retained in these contracted constants; no global operator norm of Delta C is asserted. Orders 3 through 8 are unnecessary here.

For the sharp reference field,

    Cov(a)=I/(4 a_phi^2), Cov(a,h)=0,
    Cov(h_i,h_i)=1/(6 a_phi^2),
    Cov(h_i,h_j)=-1/[2pi^2 a_phi^2(i-j)^2] for i!=j.

The same-space deterministic mean stays H_T. Under the frozen field bound, E sigma_state<=B_H+sqrt(u)sigma_a, with bounded B_H and eventually sigma_a<=1. Convex covariance interpolation preserves this estimate.

Write nu_T=L^(-2)sum_p (log p)^2/p delta_(log p/L), nu_ref=s ds. The frozen retained-interval discrepancy is <=C_nu/L^2 and the omitted endpoint width is 1-s_N=O(L^(-1/2)). The covariance comparison is

    d_theta A=a_phi^(-2) int h_(theta,u,rho)(s) d(nu_ref-nu_T)(s).

The finite word list gives rational constants alpha,beta,gamma with

    ||h||inf<=u alpha,
    E Var(h)<=u[beta+gamma(B_H+sqrt(u)sigma_a)].

They are machine-generated in the replay, using 2pi<44/7, 2/pi<1, Qcap=43/20, K1cap=10, and rational upper enclosures of eta|b_k|:

    alpha=241292924755566961111513247030054089/
          27103188584064450312500000000000,
    beta =241292924755566961111513247030054089/
          13551594292032225156250000000000,
    gamma=4364298378552974428644715979676712179/
          15533514957241938085351562500000.

Thus uniformly for delta<=u<=U and 0<=rho<=1,

    |A_(u,T)(rho)-A_(u,ref,T)(rho)| <= e_T(U),
    e_T(U)=a_phi^(-2) U {
      (C_nu/L^2)[alpha+beta+gamma(B_H+sqrt(U)sigma_a)]
      +alpha(1-s_N)} -> 0.

The endpoint rho=1 proves the same bound for E_u. These large constants condition a vanishing substitution error; they are not added as fixed consumer costs. Fixed U before T suffices. The old U=o(sqrt(L)) range is compatible: the displayed bound is O(U(1+sqrt(U))/L^2+U/sqrt(L)); even a coarser discrepancy O(1/L) would suffice in that range. This comparison is conditional on the frozen SHARP-state assumptions and does not silently transport a filtered covariance to this sharp reference.

## 4. Infinite moment problem and independently certified weak duals

At either endpoint the primal has a_n>=0 and constraints sum a_n=E, sum rho_j^n a_n=A_j. For a lower witness q_lambda(n)=lambda0+sum lambda_j rho_j^n <=1_(n<=K), weak duality gives

    lambda0 E+sum lambda_j A_j<=S_K.

The upper witness reverses this inequality. Integrability follows from finite E and bounded q. Without an additional certified linear relation between endpoint chaos masses, the joint two-sequence feasible set is a Cartesian product. Its minimum difference is exactly the separate lower problem minus the separate upper problem. Heat evolution of f_u alone supplies no extra linear mass relation used here.

The pool of rational points is

    1/4, 1/2, 3/4, 7/8, 15/16, 31/32, 63/64, 127/128.

The producer tries the first six, seven and eight points for each K=4,6,8,12,16,24,32. Floating LP output is only a proposal. Every coefficient is rationalized, shifted outward, repaired by exact checking, and then replayed by the separate Fraction-only program.

The all-n certificate consists of exact inequalities for n=0,...,N and an analytic tail. Let rmax=max rho_j and N>=K. For a lower witness,

    q_lambda(n)<=lambda0+sum_(lambda_j>0)lambda_j rmax^n.

Checking this upper envelope <=0 at N+1 proves the entire tail, since its positive part decreases thereafter. For an upper witness,

    q_mu(n)>=mu0-sum_(mu_j<0)|mu_j|rmax^n.

Checking the lower envelope >=0 at N+1 proves every later n. This is an integer-infinite certificate, not a finite floating scan. Constant mass-cap witnesses require no rho points.

For interval measurements the verifier selects each interval endpoint according to the coefficient sign. A fixed witness amplifies covariance substitution by the sum of absolute coefficients times e_T(U), still o_T(1). There is no differentiation of the cutoff and hence no return of 2K+2.

The exact witnesses, finite coverage endpoints and repairs are in WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json. The replay records all fourteen acceptances. Hostile tests include the requested atoms, geometric tails, two-point masses, near-zero/near-one rho and the noncommuting/singular algebra. Corrupt rho, corrupt coefficient and an uncertified positive lower tail are rejected.

There is no intrinsic impossibility of arbitrarily accurate finite weak-dual cutoff approximation. For rational q in (0,1), t_n=q^n, choose the continuous ramp equal to zero below q^(K+1), one above q^K, linear between. Its Lipschitz constant is 1/g with g=q^K-q^(K+1). Its Bernstein polynomial of degree M has rational coefficients and uniform error <=1/(2g sqrt(M)), by the binomial variance bound and Cauchy-Schwarz. Choose rational gamma above that error; polynomial plus/minus gamma gives all-n upper/lower witnesses. Monomials correspond to rho_j=q^j. This existence construction may be numerically expensive; it does not certify the required reference measurements.

## 5. Exact benchmark ledger versus actual reference measurements

The certificate searches a SYNTHETIC diagnostic, not an actual Gaussian heat trajectory:

    a_n(U)=E_inf(1-3/4)(3/4)^n,
    a_n(delta)=w0(1-1/100)(1/100)^n,
    delta=1/100000.

Its E and A measurements are exact geometric sums, A/E=(1-t)/(1-t rho). The producer records every rational lower/upper bound, deficit, initial payment, amplification and margin. The best benchmark is K=32 using eight points; its lower terminal unit bound is about 0.9995896051, upper initial bound is 1, and its full illustrative margin is about 0.000429209. The exact initial payment there is 53503/66000000. The witness has measurement amplification about 31364.158. These numbers prove feasibility on those positive sequences only. They do not give an actual best K,delta,U or a theorem-side positive margin.

The independently certified K=32 lower witness has N=256 and coefficients, in pool order:

    lambda0=-177474003807058873909/55887390900000000,
    lambda1=-16820385/938417306,
    lambda2=150292891/874129933,
    lambda3=-458723607/134099951,
    lambda4=50678184278/828307931,
    lambda5=-634564925781/913638178,
    lambda6=414028352447/98018322,
    lambda7=-9148412858571/774794887,
    lambda8=4252112992579/373099229.

The upper witness is mu0=1, with no rho coefficients. The JSON is the authoritative exact numerical witness if platform LP proposals change; the independent verifier, not these decimal diagnostics, establishes validity.

Only after the transfer proof, the script evaluates finite-reference diagnostics at T=128 (d=61,N=3), delta=1e-5, U=1,2,4,8,16. It uses the explicit reference covariance above and keeps the actual prime mean returned by prime_state. Mehler observables are computed directly by paired eigendecompositions; no individual Hermite reconstruction is used in this stage. The 128 seeded samples are NOT rigorous enclosures, and a finite reference with H_T is NOT a proven limiting reference state. Every diagnostic carries usable_as_a_bound=false; apparent cap violations are checked and flagged. Large signed dual weights amplify sampling error.

## 6. Direct two-copy resolvent reduction and remaining obstruction

Expand Q into R^0,...,R^3. The Mehler observable is a finite linear combination of one-copy means and mixed moments

    M_kl=E tau((R1^*)^k R2^l), 1<=k,l<=3.

A resolvent identity gives

    R1^*-R2=R1^*(H2-H1-2iaI)R2.

Gaussian integration by parts, with V(X)=sum C_ij E_i X E_j, yields

    2ia M11 = m-conj(m)
      +u(1-rho) E tau[
          R1^* V(R1^*) R2 - R1^* V(R2) R2],
    m=E tau(R2).

Indeed Cov(W2-W1,W1)=(rho-1)C and Cov(W2-W1,W2)=(1-rho)C. At rho=1 the additional term vanishes and M11=Im(m)/a, the Ward endpoint. Away from that endpoint the mixed V terms are not determined by m and M11. No finite closed scalar system has been proved. Gram positivity, Toeplitz covariance and Cayley unitarity do not by themselves identify these mixed resolvent expectations or remove H_T.

The narrow remaining obligation is a rigorously enclosed finite reference measurement vector

    (E_(U,ref,T), A_(U,ref,T)(rho_j),
     E_(delta,ref,T), A_(delta,ref,T)(rho_j))

uniformly in the theorem limit with its actual H_T, whose sign-correct dual evaluation satisfies the frozen exact ledger. A rigorously established background limit or uniform reference inequality could supply it. Monte Carlo does not.

## Replay

    python src/wp84_mehler_weak_dual_chaos_cutoff.py --recon --certificate notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json --output notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_REPLAY.json
    python src/wp84_mehler_weak_dual_certificate.py notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json

The producer uses SymPy for exact algebra and SciPy only for proposals. The standalone certificate verifier uses standard-library Fraction arithmetic. Dependencies carrying the frozen constants and state assumptions are the parent WP84_JOINT_SIGNED_DEFICIT_COVARIANCE_TRANSFER audit and script, WP84_ACTUAL_STATE_SIGNED_DUAL_FLUX and script, WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE, WP84_GOOD_ENDPOINT_TRIMMING, and the previous integrated/cross-repository Hermite audit scripts imported by the producer. Their earlier obligations remain frozen at their established scope.

Final gate: **B**, with the finite reference measurement certificate still OPEN. No actual positive margin, actual best tuple, or strict >79 conclusion is asserted.

## Moderate-K diagnostic table

All entries below refer only to the exact geometric benchmark above. The JSON contains exact rational entries; decimals are display values.

| K | certified terminal prefix / E_inf | initial prefix upper / w0 | full benchmark margin lower |
|---|---:|---:|---:|
|4|0.651809423576|1|-1.606059674667|
|6|0.778513427235|1|-1.020782622782|
|8|0.847175545006|1|-0.703614971373|
|12|0.941581392973|1|-0.267535263123|
|16|0.978230763649|1|-0.098241992818|
|24|0.996764588489|1|-0.012624450990|
|32|0.999589605107|1|0.000429209178|

The K=32 exact illustrative margin is

    1939150689002692291975282055154320449187120336298337560823715234499173313925824774560673798529347302779552006063733737 /
    4517961845055676110694372160903595755068596513383240544406098304843348968726715330221618653003539948272000000000000000000.

This equals epsilon minus the recorded synthetic deficit minus 53503/66000000. For actual measurement intervals replace the synthetic difference by the sign-correct certified lower difference. If additional, newly introduced nonvanishing costs occur, they must be subtracted as well. No such intervals have been established here.
