# WP84 reference Mehler measurement certificate

Decision **D — reference measurement route blocked by the currently available certified information**. This is an obstruction to this proof certificate, not a disproof of the arithmetic theorem. Compilation into one observable succeeds exactly. It removes independent measurement bookkeeping, but neither removes the deterministic prime baseline nor supplies the endpoint energy law needed by the consumer. There is no theorem-grade U selected and no >79 promotion.

Parent commit: d702810f6b165f2d9a1e11392d6462df940b9b37. Branch: codex/c5-c6-attack-20261006. All six user-frozen items remain CLOSED at their previously stated scope. No raw fifth/sixth moments are introduced.

## 1. Frozen witnesses and their operator meaning

The exact fourteen witnesses for K=4,6,8,12,16,24,32 are copied without alteration into the accompanying JSON, together with every exact synthetic benchmark ledger. Their all-n certificates are independently replayed. The winning benchmark uses K=32, delta=1/100000 and these rational rho points:

    1/4, 1/2, 3/4, 7/8, 15/16, 31/32, 63/64, 127/128.

Its lower coefficients in that order, preceded by lambda0, are

    -177474003807058873909/55887390900000000,
    -16820385/938417306,
    150292891/874129933,
    -458723607/134099951,
    50678184278/828307931,
    -634564925781/913638178,
    414028352447/98018322,
    -9148412858571/774794887,
    4252112992579/373099229.

The upper witness is mu0=1 with no other coefficients. The lower satisfies q_lower(n)<=1_(n<=32) for every integer n>=0; the upper satisfies the reverse. The finite exact lower check covers 0..256, followed by the analytic adverse-coefficient tail envelope starting at 257. The upper is the exact mass cap. The other witnesses' coefficients, rho sets, coverage endpoints, inequalities and synthetic contributions are fully retained in the JSON rather than recomputed as theorem data.

On Gaussian L2 with normalized matrix Hilbert inner product Re E tau(F*G), let T_rho be the self-adjoint contraction with chaos multiplier rho^n. Define

    O_lower=lambda0 I+sum lambda_j T_(rho_j),
    O_upper=mu0 I+sum mu_j T_(rho_j).

These are bounded self-adjoint operators. Orthogonal chaos decomposition proves exactly

    <f,O_lower f>=lambda0 E+sum lambda_j A(rho_j),
    O_lower <= Pi_K <= O_upper

as quadratic forms on ALL Gaussian L2, including matrix-valued functions and singular covariance representations. Indeed the quadratic-form differences are sums of nonnegative scalar multiplier differences times ||f_n||^2. There is no matrix-order claim about the pointwise values of O_lower f. The exact algebra replay checks the compiled form against its chaos multipliers on a noncommuting matrix polynomial. The all-n verifier, not that finite polynomial test, supplies the infinite-dimensional operator assertion.

## 2. One signed reference target

Keep the consumer function Q distinct from the OU operators O. It is the frozen

    Q(H)=eta P(H)(H-zI)^(-3),
    c=3142/2415, a=131/200, z=c+ia,
    eta=(c^2+a^2)^(3/2),
    P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3.

For the SAME deterministic mean H_T and reference field W_ref,T, put f_u(g)=Q(H_T+sqrt(u)W_ref,T(g)). The only signed target is

    L_T(K,U,delta)=<f_U,O_lower f_U>-<f_delta,O_upper f_delta>.

Then S_K(U)-S_K(delta)>=L_T exactly. For the winning upper witness, its second term is simply ||f_delta||^2. All subsequent statements keep this signed combination intact. The frozen covariance transfer applies to this fixed finite combination with o_T(1) error; its conditioning constants are not new nonvanishing ledger charges.

## 3. Conditional common noise and exact heat normalization

Take Z0,Z1,Z2 independent with the SAME reference field covariance C_ref,T. Set

    X=sqrt(rho)Z0+sqrt(1-rho)Z1,
    Y=sqrt(rho)Z0+sqrt(1-rho)Z2.

Then Cov(X)=Cov(Y)=C_ref,T and Cov(X,Y)=rho C_ref,T, exactly the frozen Mehler pair. Given Z0, X and Y are independent. Entrywise conditional expectation and the finite-dimensional matrix Hilbert product give

    A_u(rho)=E || E[Q(H_T+sqrt(u)X)|Z0] ||_(2,tau)^2.

This proves positivity without taking the absolute value of a signed dual sum.

Define the covariance heat semigroup, acting ENTRYWISE on matrix-valued functions of Hermitian H,

    P_t^C Q(H)=E_Z Q(H+sqrt(t)W_ref,T(Z)),
    generator=(1/2)sum_ij C_ij D_H^2[E_i,E_j].

Its time parameter is variance, not standard deviation. Consequently

    A_u(rho)=E_Z || P_(u(1-rho))^C Q(
                               H_T+sqrt(u rho)W_ref,T(Z)) ||_(2,tau)^2.

At rho=1 this is E_u; at rho=0 it is ||P_u^C Q(H_T)||_(2,tau)^2. Both identities remain true for complex matrix-valued Q and singular C. The exact verifier checks the heat formula against a correlated two-copy Wick expectation for a noncommuting 2x2 polynomial and rejects an incorrect normalization. Positivity does NOT make lambda_j all positive. The joint expectation cannot be replaced by the square of a scalar trace.

The compiled heat form is exactly lambda0 E_U plus the signed sum of these conditional squared norms, minus the initial upper form. Common Z can be used in the outer expectations, but the evaluated common states H_T+sqrt(U rho_j)W(Z) and inner heat times differ with j. Combining them as norms of one common matrix, or cancelling their heat times, would be false. The OU spectral form is the valid place where the cancellations occur.

## 4. Deterministic baseline derivative: one target-aware co-state

For a justified comparison state H_ref,T, write H_theta=H_ref,T+theta E_T, E_T=H_T-H_ref,T. Use the same reference Gaussian field throughout and define

    f_(u,theta)=Q(H_theta+sqrt(u)W),
    psi_(U,theta)=O_lower f_(U,theta),
    psi_(delta,theta)=O_upper f_(delta,theta).

Self-adjointness gives the GROUPED derivative

    d_theta L_theta=
      2 Re <DQ(H_theta+sqrt(U)W)[E_T],psi_(U,theta)>
      -2 Re <DQ(H_theta+sqrt(delta)W)[E_T],psi_(delta,theta)>.

Only first Frechet derivatives occur. The OU co-state carries the entire dual combination before any norm or triangle inequality. This is the target-aware vector-valued transplant; it is not fourteen separately differentiated measurements.

For R=(H-zI)^(-1) and Q=eta sum_(k=0)^3 b_k R^k, the exact derivative is

    DQ(H)[E]=-eta sum_(k=1)^3 b_k
                         sum_(p+q=k+1;p,q>=1) R^p E R^q,
    b0=p3, b1=p2+3zp3, b2=p1+2zp2+3z^2p3, b3=P(z).

Thus define the Hermitian matrix statistic

    G_(u,theta)(g)=-2 Herm[
       eta sum_(k=1)^3 conjugate(b_k)
              sum_(p+q=k+1) (R*)^p psi_(u,theta)(g)(R*)^q].

Then

    d_theta L_theta=E tau(E_T [G_(U,theta)-G_(delta,theta)]).

The exact scalar baseline transport statistic still needed is

    B_T=integral_0^1 E tau(E_T [G_(U,theta)-G_(delta,theta)]) dtheta,
    L_T=L_ref,T+B_T.

This is a single signed resolvent/co-state contraction, not a raw moment. A one-sided lower bound on L_ref,T+B_T above the ledger threshold would close the reference gate. Neither a certified scalar-reference value L_ref,T nor a paid signed B_T is established in the repository. Therefore decision C, which could suggest that ONLY a baseline comparison remains, would overstate the evidence; decision D records both missing pieces.

The exact replay checks the grouped baseline derivative. The winning multipliers q_lower(0) and q_lower(1) are nonzero (their exact rational values are in the JSON). The baseline derivative of the grouped polynomial example is nonzero. Thus the dual has not universally cancelled the leading baseline dependence.

## 5. What displacement structure does and does not remove

Statewise rank[D,R]<=2 and rank[D,Q]<=6 survive. They supply finite displacement-generator representations and fixed-pole bounds for each response. They do not say Q, a conditional heat average, the OU co-state psi, or G has matrix rank six. An average of rank-two displacement generators can have higher displacement rank; the exact replay gives ranks 2,2,4 for two matrices and their average. This is an algebraic obstruction to compressing a random family into six deterministic scalar numbers by rank alone.

For the grouped operator, one useful bound preserves cancellation:

    |d_theta <f,O f>|<=2 ||DQ[E_T]||_(L2,tau) ||O f||_(L2,tau).

It is stronger information than blindly summing absolute lambda_j errors, but ||O f|| is itself a target-aware statistic not yet certified. A fallback uses ||O||=sup_n|q(n)| and ||DQ[E_T]||<=K1||E_T||op. Neither proves small error for the deterministic prime contribution. The constant lower multiplier tends to lambda0<0 as n tends to infinity, so O_lower is not a positive contraction even though its low-chaos multipliers approximate one.

There is also a fixed-pole normalized trace-norm Lipschitz bound from the ordered resolvent derivative, of the form

    |L(H)-L(H')|<=C_(dual,Q) ||H-H'||_1/d.

This pays the smooth-background error E_S=o_(1,tau)(1) uniformly in fixed u. It does not pay P_T: the source theorem scalarizes S=H_mu+H_Pi, leaving the deterministic prime sum. H_T=S+P_T (with retained proper powers in the mean), whereas the frozen noise covariance contains ordinary primes only. No source proves ||P_T||_1/d=o(1).

Finite lower moment data do not identify this rational response. An exact example uses probability weights binom(5,k)/16 on even k=0,2,4 versus odd k=1,3,5. Their moments of orders 0 through 4 agree, while their exact energies int |Q(x)|^2 differ. Diagonal matrices realize both measures with displacement rank zero. This is a generic insufficiency example, not a counterexample satisfying every arithmetic hypothesis. It forbids inferring a rational-resolvent value from four moments and rank alone. Knowing tau Q*Q at u=0 would fix that one energy, but would not close the heat response or its OU co-state.

## 6. Research-library search result

The verifier scans the entire notes Markdown library for scalarization, permutation/Lindeberg, displacement channels, T12/S4, adjoint, compatibility, weak duality and Hadamard terms. It records matching paths and SHA256 hashes; this is search coverage, not a claim that every matched source proves a theorem used here.

Load-bearing scope checks:

* WP84_BACKGROUND_SCALARIZATION: scalarizes S, explicitly leaves the prime-block noncommutative evolution open.
* WP84_GAUSSIAN_DRIFT_ELIMINATION: removes an exposed drift term using Gaussian integration by parts, but the resolvent retains the deterministic arithmetic mean and a mixed covariance statistic.
* WP84_D1_D2_DISPLACEMENT_REDUCTION and WP84_PERMUTATION_LINDEBERG_RESOLVENT: reduce to diagonal and displacement-generator/permutation-average statistics; their arithmetic evaluation remains open.
* WP84_LRSC_DISPLACEMENT_RANK_CLOSURE: establishes statewise rank structure, not the values of averaged channels.
* WP84_SHIFTED_BERNOULLI_RANK6_TRANSPORT: stops at finite-state closure and does not give >79.
* WP84_CHARACTERISTIC_HEATFLOW_EQUIVALENCE: the correct co-moving rescaling retains the additive prime baseline; it only pays the already-small smooth background error.
* WP84_CROSS_REPOSITORY_HERMITE_ADJOINT_REPLAY and the corresponding imported scripts: target-aware/endpoint-compatible algebra transfers, but no actual prime bound. Navier-Stokes-inspired vector propagation does not provide the missing arithmetic response law.

K2 Gram cancellation, T12/S4 and Hadamard contraction control derivative conditioning; they do not determine the signed baseline contraction B_T. No new fifth/sixth-moment assumption is used.

## 7. Absolute monotonicity, Taylor bounds and low-rho mean

Let M_r(u)=sum_(n>=r)(n)_r a_n(u), the covariance-contracted Malliavin energy, not a raw coordinate tensor norm. Then A^(r)(1-)=M_r. With h=1-rho,

    A(rho)=sum_(k=0)^(r-1) (-h)^k M_k/k! + R_r,
    0<=(-1)^r R_r<=h^r M_r/r!, M0=E.

This follows by Taylor's integral remainder and absolute monotonicity A^(r)(t)<=M_r on [0,1]. In particular

    max(0,E-(1-rho)M1)<=A(rho)<=E.

Even and odd truncations alternate lower and upper bounds when the needed moments are known. The exact verifier tests signs and factorials through r=8 on masses including n=32 and n=100. The certified bounds are

    M_r(u)<=u^r kappa_* beta_*^(r-1) C_r^2,
    kappa_*<=1/2, beta_*<=5/2,

with the frozen rational C_r enclosures. No Gaussian-coordinate count is introduced. The accompanying JSON records caps for U=1,2,4,8,16,32. These are theorem-grade bounds, not a search selecting a winning U.

Bounds on M_r alone do not give E a lower bound. Consequently the unconditional certified intervals remain

    E_u in [0,E_inf], A_u(rho_j) in [0,E_inf].

The conditional relation E-(1-rho)M1<=A can be retained jointly, but both the zero sequence and a constant-chaos sequence satisfy every derivative upper cap. It cannot establish near-saturation of E_U or identify E_delta. Higher-order Taylor upper caps alone leave that same obstruction.

At low rho, M_u=P_u^C Q(H_T), A_u(0)=||M_u||^2, and

    partial_u M_u=(1/2)P_u^C Z_Q(H_T), M0=Q(H_T).

This is an exact matrix-valued heat equation. Z_Q contains resolvents and V(R); it is not an autonomous equation for the few mean resolvent entries. It retains H_T and the state-dependent response. Neither low-rho elimination nor a Ward identity yields its value. Low-rho points are therefore not silently treated as easy measurements.

## 8. Cost-aware robust optimization with the available intervals

The eight-point winner is frozen as a regression witness, not automatically used as a theorem optimizer. For a fixed independent interval vector, worst-case dual evaluation takes the lower endpoint for positive lower coefficients and the upper endpoint for negative lower coefficients, with reversed choices for the upper form. A cost-aware LP can introduce absolute coefficient costs to encode those radii. But assigning tighter intervals without proof would manufacture a margin.

For the ONLY unconditional intervals above, the exact robust optimum for the two-endpoint difference is

    lower difference = -E_inf,
    attained by O_lower=0, O_upper=I,
    retained rho points: none.

Proof: the permitted data include zero terminal mass and initial mass E_inf concentrated in chaos zero. Every upper witness has q_upper(0)>=1, so the worst-case difference is <=-E_inf. The displayed pair attains this value for the independent interval boxes. The same adverse pair satisfies all derivative upper caps and absolute-monotonicity relations. This is an exact optimum of the stated RELAXATION, not an assertion that those endpoints arise from one actual H_T heat trajectory. A new paid trajectory/baseline relation could shrink this relaxation; none is certified here.

Thus cost-aware removal of expensive points does not rescue the current proof data. We do not perform a nominal U search. For K=32,delta=1/100000 the full robust ledger is

    initial payment <=53503/66000000,
    D_up=E_inf-w0-(-E_inf)=2E_inf-w0,
    robust margin=8711/2778200-(2E_inf-w0)-53503/66000000,

approximately -9.1338530741. Its exact rational value is in the JSON. This is the obstruction of conservative data, not an estimated actual deficit.

## 9. Frozen benchmark regression and final boundary

The original geometric benchmark margin, exactly preserved in the JSON, remains approximately +0.00042920917783421334 at K=32,delta=1/100000. Synthetic values are never fed into reference measurement bounds. There is no certified actual K,delta,U tuple.

All ledger terms are retained: initial layer delta*kappa_*sqrt(E_inf)K2, initial chaos delta*kappa_*K1^2/(K+1), additional adjoint residual zero by the frozen telescope, physical heat-tail payment zero for the frozen cap-safe consumer, and fixed-dual covariance substitution o_T(1). No initial chaos cost is counted twice. For any future grouped lower certificate l_ref, the precise remaining test is

    epsilon-[E_inf-w0-l_ref]-c_initial-c_initial_chaos > 0

after the vanishing substitutions. If baseline comparison or finite-integral truncation adds a nonvanishing error, it must also be paid. No such value is hidden here.

The narrow target is now one signed reference scalar L_T, or equivalently a certified comparison L_ref,T+B_T. Compilation and the baseline derivative are exact. A finite continuum Gram certificate has not been obtained: conditional heat averaging still integrates a nonlinear resolvent of a growing matrix with H_T retained. Rank-six displacement does not bound the number of its Gaussian degrees of freedom.

Final decision D. No strict >79 theorem. Previous closed gates are not reopened.

## Exact replay

    python src/wp84_reference_mehler_measurement_certificate.py
    python src/wp84_mehler_weak_dual_certificate.py notes/WP84_REFERENCE_MEHLER_MEASUREMENT_CERTIFICATE.json

The certificate supplies the standalone verifier's native witnesses field as well as the frozen provenance copy. The exact output contains the complete frozen witnesses, benchmark ledgers, baseline tests, rational derivative caps, conservative intervals and robust margin.
