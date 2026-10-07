# WP84 prime characteristic boundary law: circularity stop gate

Decision **D — master route provably circular at the first requested stop gate**.

The characteristic boundary is classification **A: literally the original compiled signed target under a reparameterization**. Its exact consumer factors, covariance, matrix dimension and prime cutoff survive unchanged. The scalar prime-field representation exposes its source, but is the already-established representation; it does not turn this characteristic boundary into a finite-lag cylinder or a new arithmetic object.

User stop condition 16.A is therefore applied. Localization, finite-dimensional CLT, literature/public-candidate applicability and passage R to infinity are not pursued in this audit. No assertion that any of those independent arithmetic approaches fails is made. The Mehler/weak-dual architecture remains intact; the master characteristic adds no simplification to its active arithmetic target.

Parent: 00f5f8f67b9c03d399c90650d0811cf01e6c7464. Branch: codex/c5-c6-attack-20261006. No push; all earlier local audit commits are preserved.

## 1. Complete characteristic flow and invariants

Use the master consumer family

    Q_theta(H)=q0 I+sum_(k=1)^3 q_k(H-s0I-zeta I)^(-k),

where the physical point has zeta=z-s0, q_k=eta b_k, z=3142/2415+i(131/200), eta=|z|^3. Keep the finite complex parameters and their conjugates consistent. The master vector field is

    t partial_t+2(v1 partial_v1+v2 partial_v2+c partial_c)
      +zeta partial_zeta+conj(zeta)partial_conj(zeta)
      +sum_(k=1)^3 k(q_k partial_q_k+conj(q_k)partial_conj(q_k)).

Let ell be characteristic time and r=exp(ell-ell_*). Its exact flow is

    t=r t_*, v1=r^2 v1_*, v2=r^2 v2_*, c=r^2 c_*,
    zeta=r zeta_*, q0=q0_*, q_k=r^k q_(k,*).

A complete independent REAL invariant system for t>0 is

    v1/t^2, v2/t^2, c/t^2,
    Re(zeta)/t, Im(zeta)/t,
    Re(q0), Im(q0),
    Re(q1)/t, Im(q1)/t,
    Re(q2)/t^2, Im(q2)/t^2,
    Re(q3)/t^3, Im(q3)/t^3.

There are thirteen independent invariants in the fourteen-real-parameter extension. Every differentiable characteristic invariant is locally a function of these thirteen. Derived invariants include the copy correlation c/sqrt(v1 v2), variance ratio v1/v2 when defined, and q_k/zeta^k when zeta!=0. They supply no additional independent data. The fixed s0, T,L,d, covariance map, retained prime coefficients, K and dual weights are static parameters, also unchanged by the flow.

For two separately named covariance maps, each of the six copy-covariance entries divided by t^2 is invariant; the other ten consumer/pole invariants are unchanged. This yields sixteen independent invariants for that seventeen-real-parameter extension. The finite-T distinction between the Bernoulli and quadrature maps does not repair the circularity.

## 2. Exact boundary matrix and function

Take terminal t_*=1 and any correlated Gaussian Loewner pair G1,G2 with copy covariance Sigma_*. Couple the characteristic states by

    X_r=s0I+r[P_sharp,T+G1],
    Y_r=s0I+r[P_sharp,T+G2],
    z_r=s0+r(z-s0), theta_r=(r zeta,q0,r q1,r^2 q2,r^3 q3).

Then, for EVERY realization and r>0,

    X_r-z_r I=r[s0I+P_sharp,T+G1-zI],
    r^k(X_r-z_r I)^(-k)
            =(s0I+P_sharp,T+G1-zI)^(-k),
    Q_(theta_r)(X_r)=Q_theta(s0I+P_sharp,T+G1),

and the same identities hold in the second copy. Consequently

    lim_(r down to 0) M(r,r^2 Sigma_*;theta_r)
       =E Re tau[Q_theta(s0I+P_sharp,T+G1)^*
                         Q_theta(s0I+P_sharp,T+G2)].

This is an equality for every r>0 before taking a limit, not an asymptotic approximation. It requires no interchange of limits or dominated-convergence theorem. The right side is the original terminal master observable. Im(z_r)=r Im(z) tends to zero, so the characteristic never reaches the regular fixed-pole scalar boundary while preserving the consumer. Setting r=0 first would discard the inverse factors that diverge as r^(-k) and change the object.

For the actual compiled witness, set terminal covariance U[[1,1],[1,1]] for the lambda0 term, U[[1,rho_j],[rho_j,1]] for each lambda_j term, and delta[[1,1],[1,1]] for the negative upper term. Along their characteristics the heat values become r^2 U and r^2 delta and the correlations remain unchanged. All consumer factors still equal their terminal factors. Thus the COMPLETE signed boundary is exactly

    B_T=lambda0 E_(U,T)+sum_j lambda_j A_(U,T)(rho_j)-E_(delta,T).

This is F_T(s0I+P_sharp,T) from the previous audits. Its relation to the nonscalar-background original target uses only the already-paid o_T(1) scalarization error; its relation to actual noise uses the previously closed covariance transfer. No new error or new boundary value is obtained from the characteristic.

## 3. Prime-field-only representation of the boundary

Distinguish the prime polynomial Q_T from the rational consumer Q_theta. On the retained grid,

    tau_k=T+2pi k/L,
    Q_T(tau)=sum_(n=p^a<=N, retained) c_n exp(i tau log n),
    c_n=-Lambda(n)/(a_phi L sqrt(n)),
    Q_T'(tau)/L=i sum_n c_n (log n/L) exp(i tau log n).

The prime-base grouping changes neither this sum nor the matrix. Proper powers remain in the deterministic mean; they are not silently removed by their disposal from covariance-square errors. The normalization is the sharp hat-unit convention used in WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION and the retained prime-block construction.

Write xi_k=Q_T(tau_k), chi_k=Q_T'(tau_k)/L. For a Gaussian field realization a_k,h_k define the explicit matrix ONLY through samples and the fixed kernel:

    H_T[xi,chi;a,h]_ii=s0+2 Re(xi_i)-2 Im(chi_i)+h_i,
    H_T[xi,chi;a,h]_ij=
      [Im(xi_i)+a_i-Im(xi_j)-a_j]/[pi(j-i)], i!=j.

The deterministic part is exactly M_(2Re xi-2Im chi)+[M_(Im xi),J], J_ij=1/[pi(j-i)]. The Gaussian part is M_h+[M_a,J]. No generic external prime-matrix data are needed in this representation.

Define the response directly from this explicit sampled matrix:

    C_theta[xi,chi;a,h]
      =q0 I+sum_(k=1)^3 q_k
                (H_T[xi,chi;a,h]-(s0+zeta)I)^(-k).

For two reference Gaussian fields (a1,h1),(a2,h2) with copy covariance u[[1,rho],[rho,1]] tensor C_ref, let

    B_(u,rho,T)[xi,chi]
      =Re E tau(C_theta[xi,chi;a1,h1]^*
                              C_theta[xi,chi;a2,h2]).

The full characteristic boundary, with no unexplained H_T or prime-operator argument, is

    lambda0 B_(U,1,T)[{Q_T(tau_k)},{Q_T'(tau_k)/L}]
      +sum_j lambda_j B_(U,rho_j,T)[{Q_T(tau_k)},{Q_T'(tau_k)/L}]
      -B_(delta,1,T)[{Q_T(tau_k)},{Q_T'(tau_k)/L}].

This uses all d samples and the inverse of their Loewner/Cauchy matrix. It is precisely the previously load-bearing rational functional, not a new finite collection of known scalar prime statistics. Its boundedness is unchanged. Its Gaussian smoothing is also unchanged.

The reference Gaussian field kernels remain the frozen

    Cov(a_i,a_j)=delta_ij/(4a_phi^2), Cov(a,h)=0,
    Cov(h_i,h_j)=delta_ij/(6a_phi^2)
                 -1_(i!=j)/(2a_phi^2 pi^2(i-j)^2),

with the stated copy correlation. These specify the ADDED Gaussian component; they are not proof that the deterministic sampled prime vector itself has this law.

## 4. Why the exact rewrite is not a localization theorem

The scalar representation eliminates independent d^2 source data, but retains a nonlinear nonlocal inverse. Rank[D,R]<=2 and rank[D,Q]<=6 constrain displacement generators; they do not make a diagonal entry of the inverse a function of a fixed neighborhood of xi,chi. Likewise K2/Gram cancellation reorganizes energy into diagonal and off-diagonal resolvent data. It does not by itself localize the dependence of those data on the prime-field samples.

No raw truncation of J or claim that a summable exposed covariance kernel supplies a cylinder functional is made. In particular no bound

    sup_T |B_T-B_(T,R)|<=epsilon(R), epsilon(R)->0

has been established here. The lag-tail error is UNKNOWN, not zero. This audit stops before attempting that independent theorem, as directed by stop condition 16.A.

For clarity, the PROPOSED future finite vector is still

    X_(T,R)={Q_T(tau_(K_T+r)),Q_T'(tau_(K_T+r))/L}_{|r|<=R},

with a uniformly sampled trace index and a separately specified edge convention. It is not yet the argument of a certified Phi_R representing the boundary. No random-index/finite-cylinder theorem is inferred from the exact full-grid rewrite. A future direct field route would need that new localization theorem before the CLT would determine this consumer.

## 5. Requested later gates: not reached

|Requested item|Status after the explicit first stop condition|
|---|---|
|Finite-lag localization / Phi_R|Not established; not pursued after stop 16.A|
|Finite prime-field covariance/CLT|No convergence theorem proved or falsified here|
|Literature applicability table|Not performed because the conditional downstream target was not reached|
|Public pinned 0.7947 machinery|Not imported or assessed for a new CLT at this stop gate|
|Long-product hostile test|No new proof requiring those products proposed|
|Gaussian smoothing improvement|Original smoothing remains; no lowered arithmetic requirement proved|
|T then R limit passage|Not justified without localization and a field-limit theorem|
|Reconstructed numerical boundary value|Unknown; exact identity supplies the original unknown value|

This does not say no applicable literature exists, that the public candidate cannot help, or that fixed-R Gaussianization is false. It records the user-required stopping point. No covariance-only or PDE-only closure is pursued after this result.

## 6. Consumer ledger preserved

The exact consumer budget and initial-payment upper bound remain

    epsilon=8711/2778200,
    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000,
    w0=1415/13891,
    c_initial+c_initial_chaos<=53503/66000000
        for the frozen K=32,delta=1/100000 witness pair.

For a future certified lower boundary value l and any additional nonvanishing error e,

    margin=8711/2778200-[E_inf-w0-l]-53503/66000000-e.

The required l-e threshold is exactly

    83446820694177651440799215197979 /
    18482819123692026401760000000000.

The characteristic identity gives no value for l. Its equality error is zero, but this is not an arithmetic comparison error of zero. Earlier background/covariance/invariance/cube errors retain their previously established o(1) scope, and frozen adjoint/tail payments remain unchanged. No cost is counted twice or waived. The +0.000429209 synthetic benchmark remains a regression only. There is no reconstructed actual boundary value, positive actual margin, or certified actual U. Strict >79 remains OPEN.

## 7. Exact verification and provenance

    python src/wp84_prime_characteristic_boundary_law.py
    python src/wp84_mehler_weak_dual_certificate.py notes/WP84_PRIME_CHARACTERISTIC_BOUNDARY_LAW_CERTIFICATE.json

The new verifier checks the complete characteristic scaling, covariance/pole/coefficient invariants and unchanged degree-three consumer factors on a noncommuting rational matrix. It rejects an incorrect power of the scaling factor. A separate exact prime-power regression uses n=2,4, L=4log2,T=2pi/log2 to reconstruct the sharp matrix from Q_T and Q_T'/L with actual pi and exact roots of unity. It checks the rank-two source law. That convenient finite regression is not asserted to be the asymptotic cutoff scale.

The exact winning dual witnesses are preserved and independently replayable. The certificate contains explicit stop/decision flags, null fields for unproved lag-tail/boundary/margin values, and hashes of the load-bearing existing source notes. The existing sharp-Loewner verifier was read; no downstream arithmetic theorem is claimed from finite algebra.

Final classification: boundary A; decision D. The master route is circular, while the original prime-field arithmetic obligation remains open for a direct noncircular attack.
