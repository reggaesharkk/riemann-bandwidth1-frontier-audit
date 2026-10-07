# Cross-repository proof transplant: backward Hermite dual and boundary flux

Date: 2026-10-07. Starting branch `codex/c5-c6-attack-20261006`,
HEAD `6ab4622cea3833e847e005eb30f0a2e1c7bf5cf1`.
This audit was written before implementing the new candidate or running a
large computation. Previous local commits, Downloads checkout, main and the
untracked NotebookLM packet are preserved. No push.

**Decision B — TRANSPLANT REDUCES IT TO ONE NEW LEMMA.** The reduction is an
exact signed finite-level dual-flux sufficient gate, not a numerical closure.
The new lemma is asymptotic and operator-theoretic on the ACTUAL prime state.
There is not yet a fixed-dimensional certificate or a >79 theorem.

## 1. Scope and provenance

All repositories returned by the accessible public `reggaesharkk` account
inventory were inspected, including the extra Psi benchmark; the current
authorized local Riemann repository was inspected separately. External
snapshots were obtained by read-only GitHub API/commit archives, without
changing any repository checkout or remote ref. Pins:

| Repository | Commit |
|---|---|
| riemann-bandwidth1-frontier-audit (local) | 6ab4622cea3833e847e005eb30f0a2e1c7bf5cf1 |
| navier-stokes-bridge-audit | 4790a7edbabdcc8f4bdf1bde1c67b44f0ccc238f |
| lrsc-odd-ring-spectral-rank | 96cdd83ceadfff766d98ffdf2249a9de43fe74de |
| Reggae-shark-universe- | f97be3256a427214af6c47e81115fb1836b7d0f3 |
| physics-v1-dynamical-sector | d409fd30bcd7c071ef92558f3fe8c1adff3f3022 |
| self-referential-processing-designlab | cfae263ff84d3bb08d4decfbdeef2f420364e4b0 |
| intentseal | c02507e2aedfae9ea526feec5a9d195d9eb2bced |
| psi-self-modeling-benchmark | 8a309b7f9c4b5fe9558e8b8a538dc777474e69db |

For an external source below, its immutable URL is
`https://github.com/reggaesharkk/REPOSITORY/blob/PIN/PATH` using this table.
The companion source manifest records content SHA-256 and Git blob SHA-1.
This is an audit of the accessible snapshots and relevant actual text/code,
not a claim to have read inaccessible private repositories, missing producer
arrays or every historical ZIP. Public release claims are source claims;
their full expensive certificates were not rerun in this audit.

The historical Riemann search covered every available research remote ref:
`70pct-support-escape-v0.1`, `bandwidth1-v0.1`, `bandwidth1-v0.2`,
`frontier-6735-v0.1`, `frontier-7962-hostile-audit-v0.1`, both local Codex
branches, and all-ref commit history for Gram/T12/Schur/corrector failures.
Later local corrections take precedence over old reference-branch claims.
No checkout, fetch, merge or rebase was needed. Repository contents were
searched for the mathematical mechanisms, followed by proof/code reads.

## 2. Frozen consumer and exact target

Keep c=3142/2415, a=131/200, z=c+ia, r²=c²+a²,

    P(x)=1-(43428/13891)x+(37704/13891)x²-(9660/13891)x³,
    Q(H)=r³ P(H)(H-zI)^(-3), p=Q*Q,
    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000,
    w0=1415/13891, model-relative cushion=8711/2778200.

All matrix inner products use tau=tr/d. W=sum_(j=1..m) g_j B_j uses
independent STANDARD REAL Gaussians, with the actual prime cosine/sine
directions divided by sqrt(2), m=2*pi(N). H_(T,u)=H_T+sqrt(u)W_T.
The target, for some FIXED finite U, is

    liminf_T I_T(U) > E_inf-21/200,
    I_T(U)=P_T(U)-Err_T(U)=integral_0^U E'(u) du,
    E(u)=E_g tau(Q(H_(T,u))*Q(H_(T,u))).                 (1)

The physical large-u tail-cap theorem remains CLOSED. None of the following
arguments changes the consumer, identifies filtered and sharp overlaps,
reopens raw moments, or assumes pointwise curvature positivity.

## 3. Transplant table

NS denotes navier-stokes-bridge-audit; RU denotes Reggae-shark-universe-;
R denotes the local Riemann repository. All paths are relative to that repo.
DIRECT means exact reusable algebra/workflow under stated hypotheses, not
an imported percentage or a quantitatively paid analytic theorem.

| Source repository and exact file(s) | Identity/theorem and hypotheses | Mechanism, success/failure boundary | Dictionary and status |
|---|---|---|---|
| NS `notes/WP19_v0_24_HERMITE_GOAL_REMAINDER_BUDGET.md`; `notes/WP19_v0_26_SIGNED_C500_NUMERATOR_GOAL_ADJOINT.md`; `src/wp19_v0_26_signed_goal_adjoint.py` | e'=A e+r-B(e,e), -lambda'=A*lambda, lambda(T)=J'(x(T)); real Fourier L2, same projected high system | Signed full reconstruction residual is paired before taking norms. Half-step RK4/Simpson scouts matched transitions, but nonlinear and endpoint remainders remained uncertified | e becomes Hermite projection error; A becomes (N+L)/(2u). No nonlinear state remainder in the exact linear chaos evolution; a quadratic goal still has a quadratic remainder. **ADAPTABLE**, derived below |
| NS `notes/WP19_v0_6_DUAL_WEIGHTED_RESIDUAL_BRIDGE.md` | F<=G_C500 for nonzero normalizer; frozen signs and low support | Freezing 500 terms leaves 1,159 fixed modes and 1,048 pairs; favorable discrete adjoint scouts are not interval proofs | Freeze one scalar consumer and its dual, rather than full-state norms. Hermite finite LEVEL is not fixed coordinate support as m grows. **ADAPTABLE** |
| NS `src/wp19_v0_23_rk4_goal_adjoint.py` (nonlinear_vjp/adjoint_rhs); `notes/WP19_v0_28_REVERSE_TIME_SIGN_CORRECTION_2026_10_01.md`; RU `papers/navier-stokes/WP19_v0_28_REVERSE_TIME_SIGN_CORRECTION_FOLLOWUP_2026_10_01.md` | Producer r=L_t-VJP(u,L)-nu Lambda L; error e_tau=-VJP(u,e)-nu Lambda e+r | Reverse viscosity is dissipative for this convention. Earlier +22.5 necessity claim is superseded. Requires real/divergence-free/Hermitian symmetry, Galerkin-Leray commutation and valid continuous inputs | Derive adjoint from current A, not from symmetric cross J or an earlier sign label. **DIRECT** sign-audit methodology; NS dissipation itself **INCOMPATIBLE** |
| NS `notes/WP19_v0_28_LOGNORM_ADJOINT_RESIDUAL_GATE.md` | Whole cubic-Hermite segments give degree <=6 residual; frozen binary floats reconstructed exactly; logarithmic strain norm | Skew transport cancels; Bernstein suprema must cover full segments. Recurrence alone does not certify imported bounds | Preserve full signed block residual, exact reconstruction and whole-interval enclosure. Gaussian dilation has no NS skew-transport dissipation. **ADAPTABLE** |
| NS `notes/WP19_v0_27b_ENDPOINT_GRADIENT_BALL_ARB.md`; `notes/WP19_v0_28_OUTPUT_BOUND_AUDIT_2026_10_01.md` | Terminal gradient variation plus Taylor remainder; one norm convention | Coordinate boxes lose constrained directions; missing arrays prevent coefficient-level replay; arithmetic agreement is weaker than PDE proof | Zero terminal dual for integral goal; include nonzero terminal gradient only if consuming an endpoint. Initial u=0 singularity cannot be omitted. **DIRECT** endpoint discipline |
| NS `notes/WP19_v0_28_ROUTE_CONDITIONING_AUDIT_2026_10_01.md`; `notes/WP19_v0_28_STRUCTURED_UNCERTAINTY_AB_2026_10_01.md` | Three finite segments and one structured A/B Arb enclosure | ~99.4% growth arose from incoming-radius amplification; structured residual penalty fell to ~0.33485 of old value but outgoing radius improved only ~0.00778%. No full chain | Keep level/channel vectors and dual pairing. Better residual bounds cannot fix badly conditioned endpoint propagation. **ADAPTABLE**; scalar worst-case continuation rejected |
| NS `notes/WP19_v0_14_DIVERGENCE_FREE_OUTPUT_FREQUENCY_CANCELLATION.md` | k=p+q and a_p dot p=0 imply a_p dot q=a_p dot k; ||P11 B(a,b)||<=sqrt(404724)||a||||b|| | Derivative moves to fixed output using incompressibility. Fixed-output same-state closure does not control recursive state drift | Hermite lowering has no divergence-free closure. Spatial displacement rank six does not replace m by six. **INCOMPATIBLE** as a universal rank-six Hardy theorem; falsifier below |
| NS `notes/WP19_v0_19_BOUNDARY_ANNULUS_DIRECT_SHELL_THEOREM.md` | New shell couples to low output only through old boundary annulus | Direct increment O(M^-2) is summable by common energy/viscosity; recursive backreaction remains open. Corrects coarse O(M^-1) obstruction | Chaos lowering crosses a cut only from K+1,K+2; use boundary flux, not all tail levels individually. No automatic viscous summability. **ADAPTABLE** |
| RU `papers/navier-stokes/WP16_036_PHASE_UNIFORM_TAIL_AND_SIGNED_GAP_2026_09_26.md` | Fixed phase torus preserves magnitudes and M_s; conditional tail D M_s(R-|k|)^(1-2s) | High-shell envelope was numerically vacuous; 9/64 fixed-magnitude phase probes failed signed criteria; low outside groups dominated | Covariance or Gram magnitudes alone cannot certify signed cross response. Preserve actual phase/state coupling. **ANALOGY ONLY** for a Riemann inequality |
| R `notes/WP84_SHIFTED_RESOLVENT_SIX_VECTOR_WEDGE.md`; `notes/WP84_SHIFTED_THREE_CHANNEL_GRAM.md` | Rank-two [D,H], rational pole order three; [D,Q]=-r³/pi(UMV^T-VMU^T), G_kl=<Wk,Wl>_K2 PSD | Exact three-channel positive energy, not a large-T bound. Historical pole differs; recompute coefficients at current z | b0=p3, b1=p2+3zp3, b2=p1+2zp2+3z²p3, b3=P(z), M Hankel triangular. Keep b*Gb contracted before chaos dualization. **DIRECT** state algebra; finite chaos closure **INCOMPATIBLE** |
| R `notes/WP84_SHIFTED_K2_GRAM_CANCELLATION.md`; `src/wp84_shifted_resolvent_wedge_gate.py` | Wk=-pi[D,R^k]; G/(pi²d)=tau((R^k)*R^l)-d^-1 sum_i conj(R^k_ii)R^l_ii | Displacement denominator cancels exactly; full trace is a mixed Stieltjes derivative; diagonal subtraction survives | Spatial K2 acts inside the Hilbert inner product at EACH chaos level. It does not cancel Hermite level-shift weights. **DIRECT** |
| R `notes/WP84_SINE_SCALAR_K2_WEDGE.md`; `notes/WP84_SINE_WEDGE_CANONICAL_FRAME.md` | Real wedge square reduces to A^T K2 B-Re(C* K2 C)+Re(P^T K2 Q-S^T K2 S) | Entire combination positive; Fourier S2 changes sign. Separate absolute values lose cancellation. Old sine consumer cannot be substituted for current one | Reuse grouped Gram/polarization, not old constants or a sign of individual bilinears. **ADAPTABLE** |
| R `notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md`; `notes/WP84_TAIL_CAPPED_FINITE_U_CURVATURE.md` | V(X)=sum B_j X B_j, exact Toeplitz/Hadamard A,H,C formula; six directional Gram indices and ten grouped cross contractions | Finite covariance map and Ward algebra exact; continuum covariance is separate substitution | Apply V to grouped response before bounding. Spatial six-index Gram is not matrix rank(DQ)<=6, nor chaos dimension six. **DIRECT** |
| R `notes/WP84_COVARIANCE_ONLY_MOMENT_FALSIFIER.md`; `src/wp84_covariance_only_moment_falsifier.py` | Pure multiplication covariance K(x,y)=|x-y| predicts m4=97/30 versus target13/4 and centered fifth0 versus1/36 | Exact discrepancy1/60 at fourth order falsifies zero-drift scalar closure | A scalar/diagonal resolvent surrogate cannot silently replace actual coefficients in the adjoint gate. **INCOMPATIBLE** |
| R `notes/WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION.md`; `notes/WP84_DETUNING_COMMUTATOR_ENDPOINT.md` | Indicator/min feature integrals and rank-two endpoint commutator turn Schur terms into moving prefix Dirichlet sums | Exact finite-feature reduction; normalized maximal endpoint estimate still required. Filtered/sharp audit later disallows unpaid sharp substitutions | Schur/PSD is legitimate only for its actual kernel. Can organize a finite dual residual feature, cannot import the missing arithmetic bound. **ADAPTABLE** |
| R `notes/WP84_CHRISTOFFEL_SYMMETRIC_LINEARIZATION.md` | Cubic P has symmetric 3-layer pencil with determinant P(x)-z and (3,3) inverse=-1/(P(x)-z); lifted displacement rank<=6 | Exact bounded observable and goal-oriented lift; endpoint expectation remains open | Group internal channels but retain actual growing spatial state. This historical consumer is distinct from frozen tail-capped Q. **ADAPTABLE** methodology |
| R `notes/WP84_INTEGRATED_CROSS_ERROR_STEIN_CHAOS.md`; `src/wp84_integrated_cross_error_stein_chaos.py` | E'=G+Gamma2; M,V identities; exact lowering and sharp Hardy envelope | Hardy m/2 remainder cannot be paid; mean-free 2/4 ratio sqrt((m+2)/8); corrector -E vacuous; small-state sampling not asymptotic proof | Exact current generator is the sole input to the new dual. **DIRECT** algebra; pointwise absorption **INCOMPATIBLE** |
| lrsc-odd-ring-spectral-rank `odd-ring-rank-theorem/v1.2/THEOREM_v1_2.md` | Odd M>=9, reflection-even mask with inactive orbit, nonzero shedding Fourier scales; Chebyshev/Vandermonde rank=p, stencil injective on masked span | Analytic family rank theorem; locked compression threshold not universal | Need an actual invariant subspace before claiming rank reduction of chaos. No Gaussian analogue of inactive-orbit injectivity supplied. **ANALOGY ONLY** |
| RU `lrsc/structural-mechanism/v1.1/README.md`, `REPRODUCIBILITY_BOUNDARY.md`; `v1.1.1-reproducibility/source/audit_k1_to_k10.py` | Binary subset quadratic c+f*x+x^TQx; finite locked M99 | Historical branch-and-bound weak duality records K<=10 exclusion, but full dual multipliers/tree missing. Later source explicitly labels floating exhaustive search numerical | Freeze actual finite matrix; a stored successful status is not a complete dual witness. **ADAPTABLE**, not an imported proof |
| lrsc-odd-ring-spectral-rank `finite-benchmark/k001-certificate/CERTIFICATE.md`; RU `lrsc/structural-mechanism/interval-audit-candidate-v0.1/interval_certificate.py`; LRSC `finite-benchmark/theta07-rank14/verify_witness.py` | Machin/Taylor rational enclosures, outward integer coefficients, overflow/coverage checks, independent decisive traversal and direct witness | Later exact exclusion resolves fixed benchmark; candidate log check itself imports exhaustive log; theta=.07 witness differs from .08 | Analytic truncation plus frozen rational/interval finite core and independent replay. All actual-state asymptotic inputs must precede promotion. **DIRECT** certificate workflow, **ADAPTABLE** mathematics |
| physics-v1-dynamical-sector `appendix/v1.4/THEOREM.md`; `appendix/v1.4.1/PROOF_AUDIT.md`; `analysis/physics_v1_0_ode_analysis.py` | Reduced positive parameter Hopf l1=ReG21/(2omega)>0; numerator/denominator positive coefficients | Exact sign proof is local/subcritical. Coefficient positivity does not alone prove rational identity; numeric identity check is diagnostic | Derive functional from generator and separately check identity/sign. Hopf Lyapunov coefficient is NOT an energy Lyapunov functional. **ANALOGY ONLY** |
| physics-v1-dynamical-sector `exploratory/recursive_cosmology_sandbox/REPORT.md` | Positive toy ODE invariant box, concavity gives unique equilibrium; characteristic product controls local stability | No global attraction; normalized ray proximity1 does not imply fixed point | Conservation/invariance hypotheses must be proved in present variables. **ANALOGY ONLY**, toy fixed-point claim **INCOMPATIBLE** |
| self-referential-processing-designlab `research/phase7/final_release/README.md`; `research/phase7/phase7_inferential_validation_runner.py` | Frozen covariance generator/CRN, equal datasets for paired architectures, block coverage/hashes, null screens | M1 passed simulation screens, M2 failed; no analytic dynamics theorem | Preserve covariance coupling and frozen inputs for diagnostics; never promote simulation calibration to signed operator inequality. **DIRECT** provenance practice, **ANALOGY ONLY** theorem |
| intentseal `verifiable-research-kernel/VRK_v0_3_1_FINAL_2026_09_28.md`; RU `verifiable-research-kernel/src/intentseal_vrk/types.py` | Claim classes require separate proof/scope, coverage/exclusion, interval verifier roles and anchored dependencies | Finite LRSC certified under local replay; N11 checker deliberately EVIDENCE_BOUND because Arb producer not regenerated; HMAC demo not universal authority | Hash witness and consumer, reject missing/mutated entries, distinguish algebra checks from source-closed analytic theorem. **DIRECT** workflow |
| psi-self-modeling-benchmark `README.md`, `provenance/README_OSF_ARCHIVE.md` | Additive original-manifest correction and benchmark scope firewall | Diagnostic self-model benchmark, no relevant energy/adjoint theorem located | Additive provenance corrections only. **ANALOGY ONLY**; no mathematical transport claim |

Additional load-bearing historical sources:

| Source | Mechanism and boundary | Dictionary/status |
|---|---|---|
| NS `WP3_PROOF.md` | Normalized enstrophy identity, zero mean-advection cancellation, explicit lattice constant C0²=4pi²+pi⁴/45, invariant small-data region nu-C0 sqrt(G0)>0, exponential decay and integrated dissipation | Genuine cutoff-independent theorem under smallness and NS viscosity. Radial Gaussian dilation has no such dissipative coefficient or actual-state smallness hypothesis. **INCOMPATIBLE** direct coercivity transplant; **ANALOGY ONLY** invariant-region design |
| NS `notes/WP11_PR27_REVIEW_GATE_2026_09_25.md` | Signed triad symmetrization gives -(1/2)(m(k)²-m(q)²); fixed low-advector band at sigma=0,s>3/2 has explicit bound sK(1+K)^(s-1)sqrt(M_K)||u||2 X | High-advector one-sided L2/L3 bound and time integral remained OPEN; measured phase drift is not that bound. Hermite lowering lacks divergence-free triad antisymmetry. **ADAPTABLE** whole-form commutator audit, **INCOMPATIBLE** importing high-level dissipation |
| R `notes/WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md`, sections4–5; `notes/WP84_EXACT_FRONTIER_RANK6_HP_AUDIT.md`, sections5–6 | T_ab=d^-1 sum_(i!=j)(R^a)_ij(R^b)_ij/(i-j)^2; d_z T12=T22+2T13, d_z²T12=6(T23+T14). Grouped leakage -(1/pi²)Re E[A_*T12+B_*d_zT12+C_*d_z²T12]; base2x4 channel, fallback widths2x8. High-precision algebra replay is not a one-sided expectation bound | Apply differentiated pole stencil to the whole assembled form; S4 reconstructs spatial weights, not positive Hermite forcing. Historical coefficients/asymptotic boundary are not imported into current consumer. **ADAPTABLE** |
| R `notes/WP84_R400_FILTERED_SHARP_REPAIR.md`, sections9–10; `notes/WP84_FILTERED_CONNECTED_OPERATOR_NORM.md`, sections7–9 | Actual filtered connected form differs from sharp Brownian anchor; uniform actual-prime full-space norm diverges at fixed R. Auxiliary Fourier Gram eigenvalues are not the consumed semiprime quadratic form. Neither norm divergence nor failed universal sign falsifies the actual weighted expectation | Do not certify an adjoint by an auxiliary six-channel Gram or import a uniform operator norm that the actual state does not satisfy. **INCOMPATIBLE** uniform-norm rescue; **DIRECT** scope lesson |

## 4. Three strongest candidates, in attack order

1. **Hermite backward dual with exact quadratic operator lift.** Derive from
   radial dilation and keep the signed boundary pairing; no separate norms
   of off-diagonal Jacobi entries. This produces the new gate (13).
2. **Three-wedge/Gram evaluation inside that dual identity.** Exact spatial
   K2 cancellation and Hadamard covariance preserve cancellations, but do
   not produce a finite Gaussian coordinate state. Use them to evaluate
   actual finite-level coefficients/residual pairings, not as a local law.
3. **LRSC exact interval dual certificate after source-closed reduction.**
   Freeze a finite witness, branch domain and remainder budget, then replay
   independently. Currently premature: fixed K still has binomial(m+K,K)
   coefficients and m grows. A uniform source theorem is required first.

Operator Lyapunov and boundary-flux localization are part of candidate1,
not independent arbitrary combinations of V,uG and mean energy.

## 5. Derive the actual evolution, and distinguish the Jacobi observable

Use orthonormal probabilists' Hermites h_alpha and Hilbert-valued coefficients
f_alpha(u). N_alpha=|alpha|, and

    L_(alpha,beta)=sum_j 1_(beta=alpha+2e_j) sqrt(beta_j(beta_j-1)),
    J_cross=(L+L*)/2,
    A(u)=(N+L)/(2u),     f'=A(u) f.                    (2)

The symmetric Jacobi chain is the **observable**, not the evolution:
in a radial harmonic sector ell it has off-diagonal
sqrt(2k(2k+2ell+m-2))/2, whereas N has diagonal ell+2k.

    D=<f,Nf>=uG,
    C=Re<f,Lf>=<f,J_cross f>=u Gamma2,
    S(u)=(N+J_cross)/u=A*+A,
    E'=<f,Sf>.                                         (3)

A is upper triangular in increasing chaos degree, not self-adjoint.
Neither its diagonal nor J_cross gives the NS dissipative lognorm. Replacing
A by J_cross in an adjoint solves the wrong equation.

For fixed finite T, Q at a nonreal pole has the required Gaussian Sobolev
regularity. All identities below can first be proved on polynomials and
then by Sobolev projection; no rearranged conditional infinite sum is used.

## 6. Exact NS-style goal pairing, with endpoint and residual conventions

Let Pi_K retain all |alpha|<=K, x=Pi_K f, A_K=Pi_K A Pi_K, and

    r_K=Pi_K L (I-Pi_K)f/(2u),  x'=A_K x+r_K.           (4)

Only rows of degrees K-1,K receive r_K, from degrees K+1,K+2
(omit nonexistent degrees). Every internal coupling stays in A_K.
Take 0<delta<U; never silently start the singular equation at zero.

For a chosen reconstructed path h, e=x-h and
r=r_K-(h'-A_K h). For S_K=Pi_K S Pi_K solve

    -lambda'=A_K*lambda+2S_K h, lambda(U)=0.            (5)

The exact identity is

    d Re<lambda,e>/du=-2Re<S_K h,e>+Re<lambda,r>,
    integral_delta^U (<x,S_K x>-<h,S_K h>) du
      =Re<lambda(delta),e(delta)>
       +integral Re<lambda,r> du+integral <e,S_K e> du. (6)

This is the joint signed NS pairing, with the actual Riemann generator.
A nonzero residual d=lambda'+A_K*lambda+2S_K h adds -integral Re<d,e>
to the right. A nonzero lambda(U) contributes -Re<lambda(U),e(U)>.
If an endpoint goal is added, its gradient sets the terminal dual so that
this term cancels the endpoint linear term; its Taylor remainder is still
paid. Equation (6) by itself does NOT remove the quadratic remainder.
Choosing a target containing unknown x would be circular as a certificate.

## 7. Operator Lyapunov lift removes the quadratic-goal remainder exactly

Instead solve the deterministic, finite-level operator equation

    -X'=A_K* X+X A_K+S_K,       X(U)=0.                 (7)

Then

    d<x,Xx>/du=-<x,S_K x>+2Re<Xx,r_K>,
    integral_delta^U <x,S_K x> du
       =<x(delta),X(delta)x(delta)>
          +2Re integral_delta^U <Xx,r_K> du.            (8)

Thus no state-error Taylor remainder is needed for this EXACT quadratic
goal. Numerical approximations of X still need a whole-interval residual
and terminal enclosure. If X_hat is used, let
R_X=X_hat'+A_K*X_hat+X_hat A_K+S_K; subtract integral<x,R_X x>
and subtract <x(U),X_hat(U)x(U)> from the right of (8).

For the cross error alone use S_cross=J_cross,K/u in (7)-(8), retaining
P separately. For the actual total goal S_K=A_K*+A_K, the propagator
Phi(v,u) satisfies partial_v Phi=A_K(v)Phi, Phi(u,u)=I. Exactly

    Y(u)=Phi(U,u)*Phi(U,u),  X(u)=Y(u)-I.               (9)

Y>=0, while X need not be positive. Its norm/entries may grow badly as
delta decreases or K grows; no small endpoint cost is inferred.
For any positive target Y0(u), the finite-horizon solution
X(u)=integral_u^U Phi(v,u)*Y0(v)Phi(v,u)dv is positive and satisfies
the same differential Lyapunov equation with forcing Y0. This is different
from the algebraic equation A*X+XA=-Y0. The latter cannot have positive X
for positive Y0 on a positive-eigenvalue mode: evaluating on an eigenvector
of A with n/(2u)>0 gives a positive left side and negative right side.
The zero-degree mode also precludes strictly positive Y0 there.

Equation (9) re-encodes an endpoint response. It is not an independent
energy gain. Its usefulness would have to come from a source-closed bound
on the grouped actual signed pairing and initial coefficient form.

## 8. Boundary-flux identity: all upper levels eliminated except one cut

Let t=(I-Pi_K)f, E_tail=||t||². Triangular lowering implies that t evolves
by its INTERNAL upper-chain lowering: there is no feedback from x to t.
Consequently

    E'=<x,S_K x>+2Re<x,r_K>+E_tail'.

Combine this with (8)-(9), retaining the whole boundary pairing:

    I_T(U)=I_T(delta)+<x(delta),X(delta)x(delta)>
       +2Re integral_delta^U <Y(u)x(u),r_K(u)>du
       +E_tail(U)-E_tail(delta).                       (10)

This is exact for each finite T. The high-level INTERNAL signed terms
telescope to the two tail endpoints. Positive E_tail(U) may be discarded
for a LOWER bound. No absolute bound on each chaos level is required.
There is only one shared boundary flux, not a separate error per block.

Vector organization: keep f_n with matrix-valued entries, mean n=0 and
fluctuations n>=1, even/odd chains, and the three spatial wedge pairs.
The dual Y acts on Hermite indices and tensor I on the HS matrix space.
Different spatial covariance directions remain contracted until the final
real pairing. Do not identify the six directional-response indices with
the three displacement wedges. Products/mixed poles may require twelve
generator columns. No closed evolution of six scalar wedge amplitudes is
proved by these spatial factorizations.

There is a further averaging boundary: the Hermite coefficient is an
average of matrices whose displacement generators depend on g. Statewise
rank[D,R(g)]<=2 does NOT imply rank[D,E R]<=2; similarly no six-column
factorization of each f_alpha is supplied by the statewise Q factorization.
The verifier gives an exact two-state rank2+rank2=rank4 Loewner-resolvent
witness at the CURRENT pole. Use d=4, D=diag(0,1,2,3),

    H1_ii=(1,2,3,4), a1=(1,0,2,-1),
    H2_ii=(2,-1,1,0), a2=(0,1,-1,3),
    Hk_ij=(ak_j-ak_i)/(i-j) for i!=j.

Each [D,Hk]=1 ak^T-ak 1^T has rank<=2. The two individual resolvent
commutators have rank2, their sum rank4. This falsifies preservation of
the rank ceiling by averaging, not the actual Gaussian-prime inequality.
Consequently spatial compression in candidate2 must be kept inside
statewise/polarized expectations; replacing an expected wedge by the wedge
of expected generators is invalid. A fixed three-index Gram representation
of a statewise energy may still be averaged as a Gram, but that does not
close the nonlinear evolution of its entries.

The dual boundary flux itself has no universal favorable sign: the scalar
polynomial F_u=1-u*g1² with K=0 gives x=1-u, r=-1, Y=1 and flux=-5/16
on [1/4,1/2]. This is an obstruction to a NEW universal dual-flux positivity
claim, not another search for pointwise positivity of the frozen consumer.

## 9. Optional rigorous chaos tail and initial-layer budgets

These are Gaussian-level approximation estimates, distinct from the already
CLOSED physical large-u tail theorem. Define the ACTUAL covariance mass
kappa_T=sum_j tau(B_j²). For the fixed Cayley coefficients q_j of current Q,
the finite-energy audit gives the deterministic derivative bounds

    ||DQ[B]||_(2,tau)<=K1||B||_(2,tau),
    ||D²Q[B,B]||_(1,tau)<=K2||B||_(2,tau)²,
    K1=(2/a)sum_(j=1..3) j|q_j|,
    K2=(4/a²)sum_(j=1..3) j²|q_j|.

Using ||Q||op<=sqrt(E_inf),

    D_T(u)<=u K1² kappa_T,
    E_tail,T(u)<=u K1² kappa_T/(K+1),
    I_T(delta)>=-delta sqrt(E_inf) K2 kappa_T.           (11)

The second inequality is the exact number-operator estimate
sum_(n>K)||f_n||²<=(K+1)^(-1)sum n||f_n||²; no assumed chaos-tail law.
The last discards the nonnegative G and bounds only Gamma2. These bounds
hold at each finite T with its actual kappa_T. To claim a uniform paid
constant, certify a common kappa_* for the chosen actual normalization;
continuum covariance is not silently substituted. There is no new product
mean-value theorem hidden in (11), but a covariance mass source is required.
Very small delta and large K make this initial budget small while possibly
making Y enormous; their simultaneous usefulness remains OPEN.

For the full-sharp, a_phi=1 quadratures explicitly used by the current
`prime_state` reconstruction, write s_p=log(p)/L and
c_p=log(p)/(L sqrt(p)). The complex symmetric primitive has
|A_p,ii|²=c_p²(1-s_p)² and
|A_p,ij|²=c_p² sin²(pi(i-j)s_p)/(pi²(i-j)²).
The carrier phase has modulus1, and Cp=2Re A_p, Sp=-2Im A_p give

    kappa_T=(2/d)sum_p sum_(i,j)|A_p,ij|²
       <=(8/3)sum_(p<=N)c_p².                         (11a)

This row bound also holds on a principal section because its differences
are a subset of the full lattice differences. The PNT source
`notes/WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md`, sections1–3, gives
sum c_p²=(log N/L)²/2+O(L^-2). For log N/L->1, hence
limsup kappa_T<=4/3, and kappa_*=3/2 is valid eventually in THIS
normalization. A fixed a_phi factor or another taper/bridge changes the
directions and must be included explicitly; (11a) does not identify a
smooth-taper covariance with sharp covariance. Thus the ordinary-prime
mass source can pay the Gaussian truncation bound without any higher
product correlation theorem. Proper powers in H_T do not enter W_T here.

## 10. First genuine new lemma and exact sufficient target

Fix delta>0, finite U>delta, integer K>=0, all independent of T. Define

    Fdual_T(delta,U,K)=<Pi_K f_T(delta),X_K(delta)Pi_K f_T(delta)>
       +2Re integral_delta^U <Y_K(u)Pi_K f_T(u),
                            Pi_K L(I-Pi_K)f_T(u)/(2u)>du. (12)

The **uniform actual-state signed dual-flux lemma** required here is

    liminf_T Fdual_T(delta,U,K)
      > E_inf-21/200
        +delta kappa_*[sqrt(E_inf)K2+K1²/(K+1)],        (13)

with kappa_T<=kappa_* eventually, under the actual sharp prime-state
construction and all previously frozen normalization/section choices.
Equations (10)-(11) then imply (1), with no double counting of the boundary
or initial layer. Alternatively retain exact I_T(delta)-E_tail,T(delta)
instead of (11); that can sharpen the sufficient gate but must be certified.

This is a sufficient new lemma, not an asserted equivalent finite problem.
It involves only finitely many CHAOS LEVELS (through K+2), actual coefficients
at delta, and one signed dual boundary form. It remains asymptotic and
operator-theoretic, because the count of multi-indices and the HS matrix
dimension grow with T. It is not merely a finite rational matrix at fixed
dimension. An arithmetic/source theorem on these actual coefficients is
still needed before LRSC-style certification can produce decision C.
No source in the audited repositories proves (13), provides a frozen
finite witness for it, or proves a favorable uniform lower bound on its
signed flux. The new adjoint interface isolates rather than solves that debt.

## 11. Fixed-output rank-six proposal falsified as a universal implication

For any scalar Gaussian function psi(g), take F(g)=psi(g)I_d. Then
[D,F]=0, so even displacement rank ZERO coexists with all m Gaussian
coordinates. For psi=exp(t|g|²), t<1/4,

    (C-D)/||F||²=2tm -> m/2 as t increases to1/4.

Any alleged |C|<=D+3||F||² derived ONLY from displacement rank<=6
fails for m>6 and t sufficiently close to1/4. Smooth bounded cutoffs
preserve the limiting form ratios. The mean-free level2/4 witness has
|C|/D=sqrt((m+2)/8), again with zero spatial displacement. This is NOT
a counterexample to actual Q(H_T+sqrt(u)W_T); it falsifies a universal
rank implication, exactly the missing hypothesis in the NS dictionary.
Fixed Cayley degree bounds spatial poles/derivatives but does not truncate
Hermite expansion of a rational Gaussian functional. Total Hermite parity
is conserved; total level is not, because L lowers by two.

## 12. Implementation/evidence plan following this pre-computation audit

Implement `src/wp84_cross_repository_hermite_adjoint.py` with independent
exact rational polynomial reconstructions of the Hermite chain, finite
propagator, linear dual, operator Lyapunov equation, and boundary-flux
identity. Use unnormalized Hermites with Gram diag(alpha!) so square roots
cannot contaminate exact coefficients. Check the weighted adjoint rather
than Euclidean transpose. Include a nonzero boundary witness, signed channel
cross terms, rank-zero obstruction, and fail-closed mutation checks.

This finite algebra verifier does not implement an actual-state certificate
for (13). A successful algebra check is never a consumer PASS. No Gaussian
sampling, huge branch search or unvalidated ODE rollout is needed to decide
the present gate. Subsequent implementation results are recorded below.

## 13. Implemented exact replay and resulting decision

Run:

    python src/wp84_cross_repository_hermite_adjoint.py \
      --output notes/WP84_CROSS_REPOSITORY_HERMITE_ADJOINT_REPLAY.json

The replay PASSES with independent Gaussian polynomial projection and
Hermite-scaling propagator construction. All final witness values are exact
rationals. It checks K=0,1,2,3 cuts of a two-coordinate, three-Hilbert-channel
degree-four polynomial path, retaining a positive, nonorthogonal channel
Gram with signed off-diagonals. It checks both total and CROSS-only operator
Lyapunov equations, the forced linear adjoint, its quadratic goal remainder,
zero terminal costs, and the full boundary/tail telescoping identity.

For K=2, delta=1/2, U=2, the polynomial algebra witness has

    direct I=7652/15,
    early I=233/24,
    initial dual form=2004/25,
    signed dual flux=35433/200,
    initial tail=143/150, terminal tail=18304/75.

Their sum according to (10) is exactly 7652/15. Dropping the positive
terminal tail gives 6652/25. For the CROSS-only goal, the exact quadratic
remainder is 1539/200, demonstrating why linear adjoint pairing alone
cannot omit it. These numbers belong ONLY to the polynomial algebra witness,
not the prime state or the fixed consumer budget.

Seven deliberate errors are rejected: reverse-time sign, boundary factor,
Euclidean instead of weighted Hermite adjoint, nonzero terminal endpoint,
halved signed flux, discarded channel cross terms, and attempted promotion
of an algebra replay into a consumer certificate. Checks use explicit
exceptions rather than removable Python assertions.

Rational radical upper enclosures at the FROZEN consumer give

    K1<=3225060445671/327500000000 <10,
    K2<=7908641999521/107256250000 <74,
    sqrt(E_inf)<=2149190827101/10^12 <43/20.

These conditioning bounds certify the optional initial-layer budget;
they do not bound the signed dual flux. No consumer witness or favorable
margin is reported. The replay explicitly outputs
`consumer_certified=false`, `actual_prime_bound_available=false`.

**Final decision B.** The exact new object is (12), and the required strict
inequality is (13). It has one cut, only K+1/K+2 boundary coefficients, and
paid initial-layer/tail terms. Its actual-state lower bound remains OPEN;
fixed chaos level does not make growing m(T),d(T) a fixed-dimensional
certificate. Tail cap stays CLOSED, all existing local audit commits are
preserved, and no zero-side obligation or strict >79 claim is promoted.

The source manifest records 63 cited source records across all eight
repositories, with immutable pins, file hashes and historical local refs.
The table records reading/section scope and separates archive claims from
independent replay. The exact new replay is additive and has no producer
array or unverified certificate import.
