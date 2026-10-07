# Actual-state signed dual flux: shells, contracted Malliavin hierarchy and the remaining weighted gate

Date: 2026-10-07. Parent `68ced0e1d8e9efd9ff5423cb28044385be13aa21`.
Branch `codex/c5-c6-attack-20261006`. No push. The consumer, physical tail
theorem, prior audits and untracked NotebookLM packet are preserved.

**Decision C — REDUCED TO ONE COVARIANCE-CONTRACTED MALLIAVIN BOUND.**
The remaining bound is the JOINT, DUAL-PROJECTED deficit (24), including its
initial dual form. It is not an unweighted Sobolev-energy bound. Dimension-free
derivative constants are proved below, but do not certify (24), the finite
interior, or a consumer margin. No best certified flux tuple is obtained.
In particular this decision does NOT say that only an ordinary bound on
E||D^r F||² remains: such a claim would omit an unpaid initial form and an
unbounded backward weight. Strict >79 remains OPEN.

## 1. Freeze equation (13), exactly

Use c=3142/2415, a=131/200, z=c+ia, R=(H_u-zI)^(-1), tau=tr/d,

    P(x)=1-(43428/13891)x+(37704/13891)x²-(9660/13891)x³,
    Q(H)=(c²+a²)^(3/2) P(H) R³,
    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000,
    w0=1415/13891,
    epsilon_model=8711/2778200=21/200-w0.                (1)

W=sum_j g_j B_j, g_j independent STANDARD REAL Gaussian, actual prime
cosine/sine B_j=C_p/sqrt(2),S_p/sqrt(2). No fresh-noise radial substitution.
Every Hilbert norm below is Gaussian L2 with normalized matrix HS inner
product E tau(A*B), unless an operator or tensor norm is specified.

Let f=(f_alpha) be orthonormal probabilists' Hermite coefficients of
F_u=Q(H+sqrt(u)W). N_alpha=|alpha| and

    L_alpha,beta=sum_j 1_(beta=alpha+2e_j) sqrt(beta_j(beta_j-1)),
    A(u)=(N+L)/(2u), f'=A f,
    x=Pi_K f, A_K=Pi_K A Pi_K,
    Phi(v,u)'_v=A_K(v)Phi(v,u), Phi(u,u)=I,
    Y_K(u)=Phi(U,u)*Phi(U,u), X_K=Y_K-I.                (2)

The evolution A_K is triangular, NOT the symmetric cross Jacobi matrix
(L_K+L_K*)/2. Define the named costs and forms

    J_T=<x(delta),X_K(delta)x(delta)>,
    r_+=P_(K-1) L P_(K+1)f/(2u),
    r_++=P_K L P_(K+2)f/(2u),
    Phi_+,T=2Re integral_delta^U <Y_K x,r_+>du,
    Phi_++,T=2Re integral_delta^U <Y_K x,r_++>du,
    Fdual_T=J_T+Phi_+,T+Phi_++,T,
    c_initial=delta kappa_* sqrt(E_inf) K2,
    c_chaos=delta kappa_* K1²/(K+1), c0=c_initial+c_chaos,
    K1=(2/a)sum_(j=1..3)j|q_j|,
    K2=(4/a²)sum_(j=1..3)j²|q_j|,                       (3)

where Q=q(U_C), U_C=I+2iaR, and q_j are its EXACT current Cayley coefficients.
P_-1 and the corresponding flux mean zero when K=0.

The frozen equation (13) is exactly

    EXISTS fixed delta>0, finite U>delta, integer K>=0, and kappa_*
    with kappa_T=sum_j tau(B_j²)<=kappa_* eventually, SUCH THAT
    liminf_(T->infinity) Fdual_T(delta,U,K)
      > E_inf-21/200
        +delta kappa_*[sqrt(E_inf)K2+K1²/(K+1)].        (13 frozen)

delta,U,K are chosen BEFORE the limit in T. No K(T), U(T), exchanged limit,
altered pole, changed consumer or replaced covariance is implicit.
Replacing kappa_* by a proved sharper bound changes a cost parameter, not
the target formula. For a reference Fdual=E_inf-w0, the total deficit and
initial costs must obey STRICTLY

    limsup_T [E_inf-w0-Fdual_T]+c0 <8711/2778200.        (4)

Thus “small boundary flux” alone is insufficient: J_T also needs a lower
bound. No sign or model value for J_T is assumed.

## 2. Exact shell localization and telescoping

Put E_n=||P_n f||², E_>K=sum_(n>K)E_n, I_T(delta)=E(delta)-E(0).
The two boundary residuals in (3) are ALL of Pi_K L(I-Pi_K)f/(2u).
Indeed lowering changes degree by exactly two. Internal lower-chain terms
remain in A_K; the upper chain has no feedback from the lower chain.

    r_(K+1)=r_+, r_(K+2)=r_++,
    E'= <x,(A_K*+A_K)x>
           +2Re<x,r_(K+1)+r_(K+2)>+E_>K',
    -X_K'=A_K*X_K+X_K A_K+(A_K*+A_K), X_K(U)=0.

The exact integrated identity is

    I_T(U)=I_T(delta)+J_T+Phi_+,T+Phi_++,T
                         +E_>K(U)-E_>K(delta).         (5)

Equivalently the finite interior integral equals
J_T+2Re integral<X_K x,r_(K+1)+r_(K+2)>, with the same sum of the TWO named
residuals, and the boundary in E' supplies the remaining I part of Y=I+X.
These are alternative decompositions, not independent charges.
There is no additional “finite interior” term to add again to (5).
Upper INTERNAL transfers telescope to the two tail energies. The terminal
tail is nonnegative and may be discarded for a lower bound. Zero terminal
X prevents an unpaid endpoint term. The explicit initial cost pays I(delta)
and the initial chaos tail separately.

The exact verifier uses nonzero odd AND even chaos witnesses at K=3.
It obtains Phi_(K+1)=47907/196 and Phi_(K+2)=18175/4, and proves that
no third boundary term survives. These numbers belong only to its algebra
witness, never to the prime-state consumer. No correction to (13) is needed.

The NS transplant is precise: new Fourier shells couple to low output only
through an old boundary annulus; here L couples a cut only through two
neighboring levels. NS viscous shell summability is not imported: Hermite
dilation is not viscous dissipation. The signed pairing is kept intact.

## 3. Malliavin-Hermite identity in the current Hilbert space

Let D_g^r be the ORDERED tensor of all r Gaussian-coordinate derivatives,
with squared norm sum_(j1,...,jr) E tau((partial_j1...jr F)*partial_j1...jr F).
No r! division is used. For a multi-index alpha,
partial_j h_alpha=sqrt(alpha_j)h_(alpha-e_j). Orthogonality followed by
the multinomial falling-factorial identity gives exactly

    M_r(u):=E||D_g^r F_u||²
       =sum_(n>=r)(n)_r E_n(u),
    (n)_r=n(n-1)...(n-r+1).                            (6)

The tensor entries are u^(r/2) D_H^r Q[B_j1,...,B_jr]. Neither d nor the
Gaussian coordinate count multiplies (6); matrix normalization is tau=tr/d.
For n>=r and K+1>=r,

    E_n<=M_r/(n)_r,
    E_>K<=M_r/(K+1)_r,
    sum_(n>K)(n)_p E_n<=M_r/(K+1-p)_(r-p), 0<=p<=r.   (7)

Square roots give shell norm bounds. These are actual-state derivative
bounds, not the failed universal |C|<=D+(m/2)E inequality.
The verifier independently Gaussian-integrates polynomial derivatives and
reconstructs Hermite coefficients for every r=1,...,8, including all ordered
tensor multiplicities. That verifies normalization; the general proof is (6).

## 4. Resolve directions by covariance BEFORE norms

Use the exact self-adjoint CP covariance map

    V(X)=sum_j B_j X B_j, kappa=tau V(I), beta=||V(I)||op. (8)

Its Hadamard/Schur realization is the full nine-term map in
`WP84_GAUSSIAN_COVARIANCE_HADAMARD.md`, sections1–5. A,H,C are the ACTUAL
finite-prime covariance matrices, not continuum replacements. The CP map
has operator and Schatten2 norm <=beta (self-adjointness gives the same
Schatten1 bound, followed by interpolation). Also
V(X)*V(X)<=beta V(X*X), by the CP Schwarz inequality for V/beta.

For one ordered word T=M0 B_j1 M1 ... B_jr Mr, covariance summation in
sum tau(T*T) nests V maps between the deterministic resolvent factors.
Peel the outer paired index using positivity and M*M<=||M||op² I;
iterate before taking norms. The final trace contains tau V(I)=kappa:

    sum_(j1,...,jr)||M0 B_j1 ... B_jr Mr||_(2,tau)²
       <=kappa beta^(r-1) prod_l ||M_l||op².           (9)

For cross words keep the bilinear CP contraction until the final tensor
triangle/Cauchy inequality. No sum of individual ||B_j||op is used.
Pairings within a word first form V(M); the same estimate follows using
CP Schwarz at that interior contraction and then peeling the remaining
external indices. This observation is used for Z_Q below.

For the full-sharp a_phi=1 construction, W=M_h+[M_a,J], ||J||op<=1:
the full lattice Hilbert multiplier has magnitude<=1, and restriction is
an orthogonal compression. Writing T_a=[M_a,J],

    E W²<=2E M_h²+2E T_a*T_a,
    E T_a*T_a<=2J*E M_a² J+2E M_a J*J M_a,
    beta<=2 Var(h_i)+8 Var(a_i).                        (10)

Actual prime quadratures give Var(a_i)=(1/2)sum c_p² and
Var(h_i)=2sum c_p²(1-s_p)², s_p=log p/L. PNT/BV transfer for these bounded
polynomials gives beta<=7/3+o(1). It is independent of d and of selection
of a principal section, by compression. For kappa, fixed nonzero lattice
lag r has Var(a_i-a_(i+r))->1/2, since integral_0^1 s cos(2pi r s)ds=0;
Var h_i->1/6. Dominated summation over 1/r² then gives

    limsup kappa_T<=1/6+(1/(2pi²))sum_(r!=0)1/r²=1/3.  (11)

For arbitrary principal subsections, each row has a subset of those
differences; use the fixed-lag limits and an endpoint-independent 1/r²
tail bound first. Eventually kappa_*=1/2 and beta_*=5/2 are valid in THIS
normalization. A taper or fixed a_phi rescales these quantities and must
be charged explicitly. This does not identify sharp and filtered overlaps.
Sources: `WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md`, actual quadrature
construction in `wp84_integrated_cross_error_stein_chaos.py`, and the exact
Hadamard covariance map. Only ordinary primes enter W; proper powers remain
in H and do not invalidate its Hermitian resolvent norm bound.

## 5. Ordered nonreal-resolvent hierarchy, through every needed order

Exactly

    D_H^r R[B1,...,Br]=(-1)^r sum_(sigma in S_r)
       R B_sigma1 R ... B_sigmar R, ||R||op<=1/a,
    D_H^r R^k=(-1)^r sum_sigma sum_(n0+...+nr=k+r, ni>=1)
       R^n0 B_sigma1 R^n1 ... B_sigmar R^nr.            (12)

There are r! binom(k+r-1,r) terms including multiplicity. For Q=eta
sum_(k=0..3)b_k R^k, eta=(c²+a²)^(3/2),
b0=p3,b1=p2+3zp3,b2=p1+2zp2+3z²p3,b3=P(z). These formulas preserve
all word order and the one pole; Q* has the conjugate pole and conjugate
coefficients. The squared Malliavin tensor contracts the two words through
V as in (9), not through separately bounded Gaussian directions.

A sharper practical conditioning constant follows from Q=sum q_j U_C^j.
Distribute r derivatives among ell of the j factors. Differentiating an
individual Cayley factor s times gives s! ordered resolvent words with
factor 2ia, whose norm budget is 2/a^s. Therefore set

    C_r=(r!/a^r)sum_(j=1..3)|q_j|
            sum_(ell=1..min(j,r)) binom(j,ell)
                                      binom(r-1,ell-1)2^ell.
    M_r(u)<=u^r kappa beta^(r-1) C_r².                 (14)

C1=K1 and C2=K2 exactly. Rational radical upper enclosures, not rounded
decimals, are in the replay for orders1–8. This is valid for all r; the
contracted Z hierarchy below uses C_(r+2) through order10 as needed.
Ward identities R-R*=2iaR*R and U_C*U_C=I enter the bound. They allow
commuting resolvent powers with each other, NEVER with B_j or V(R).

The actual contracted Hessian is

    Z_Q=sum_j D_H²Q[B_j,B_j]
       =eta sum_(k=1..3)b_k 2
           sum_(n0+n1+n2=k+2,ni>=1) R^n0 V(R^n1) R^n2. (15)

Equivalently it is the six-plus-four grouped Cayley contractions in
`WP84_TAIL_CAPPED_FINITE_U_CURVATURE.md`, section2. Differentiating (15)
keeps V static and differentiates its argument and both outside words.
CP Schwarz for the INTERNAL paired index followed by (9) gives

    ||Z_Q||_(2,tau)<=beta C2,
    E||D_g^r Z_Q(H_u)||²
          <=u^r kappa beta^(r+1) C_(r+2)², r>=1.       (16)

This bound is a conditioning bound, not a signed lower bound. The large
factorial constants in (14),(16) are exposed, never hidden in O(1).
For n>=r, the projected contracted estimate is

    ||P_n Z_Q(H_u)||²<=u^r kappa beta^(r+1)C_(r+2)²/(n)_r. (17)

Thus one can bound ONLY the output projections needed by the boundary,
without estimating all lower chaoses. The raw m appears nowhere in these
actual-state derivative constants. It does reappear if one replaces the
contracted Hessian by the coordinate trace of an arbitrary tensor using
||sum_j T_jj||<=sqrt(m)||T||; that forbidden step is unnecessary here.

## 6. Exact projected flux: the contraction that still needs a theorem

Since Delta_g F_u=u Z_Q(H_u), the two named fluxes are precisely

    Psi_n=P_n Y_K x,
    Phi_+,T=Re integral_delta^U <Psi_(K-1),P_(K-1)Z_Q>du,
    Phi_++,T=Re integral_delta^U <Psi_K,P_K Z_Q>du.      (18)

The lowering weights and both factors2 have canceled in this ACTUAL
contracted representation. No approximation is involved. This is the
fixed-output transplant that succeeds: the outputs are K-1,K. It does
NOT say those outputs have dimension<=6 or favorable sign.
If ||Psi_n|| had a uniform paid bound A_n(u), then (17) would give the
explicit sufficient absolute estimate

    |Phi_(n+2)|<=sqrt(kappa_* beta_*^(r+1)) C_(r+2)
       /sqrt((n)_r) integral_delta^U A_n(u)u^(r/2)du.   (19)

No such paid uniform A_n is proved. Taking the worst-case norm of Y_K
is not acceptable: it grows with the Gaussian dimension even at K=2.
Actual signed pairing (18), rather than (19), is the live target.

## 7. Mehler alternative, compared quantitatively

For independent g,g', g_rho=rho g+sqrt(1-rho²)g', 0<=rho<=1,

    A_u(rho)=E tau(Q(H_u(g))*Q(H_u(g_rho)))
            =sum_n rho^n E_n(u),
    A_u^(r)(1)=M_r(u).                                 (20)

For 0<=rho<1 its rth derivative is the correlated-copy contraction
E<D_g^r F_u(g),D_g^r F_u(g_rho)> with matched ordered indices; all weights
(n)_r rho^(n-r) are nonnegative. Cauchy bounds it by (14). Replace Q by
Z_Q for (17). Two-copy resolvent products retain the conjugate pole in
the first factor and the current pole in the second. Resolvent difference
R1-R2=R1(H2-H1)R2 and the two Ward identities are exact.

Gram/Schur positivity proves positivity of these generating coefficients,
not of their pairing with Psi. Applying the same derivative envelope to
Mehler gives the SAME bound (7)/(17); it supplies no quantitatively smaller
certified constant without evaluating an actual two-copy expectation.
Malliavin is selected for the present rigorous constants; Mehler remains
an exact potential source interface. The verifier independently integrates
the two copies at rho=0,3/5,1 and verifies orders1–8.

There is no real Gaussian representation for rho>1. Analytically continuing
to complex correlated copies removes Hermitian H, so ||R||<=1/a is no
longer supplied. Rational nonreal poles do not imply exponential chaos
decay. For example, the normalized Hermite coefficient of (g-ia)^(-1) is

    f_n=i(-i)^n/sqrt(n!) integral_0^infinity t^n exp(-at-t²/2)dt. (21)

A window near t=sqrt(n), together with Stirling's formula, proves
lim_n log|f_n|/n=0 (the Gaussian L2 norm supplies the upper bound).
The usual saddle estimate has decay exp(-a sqrt(n)) times a power,
not exp(-const n). Higher pole powers multiply the integral by powers
of t; the current scalar Q(c+sigma sqrt(u)g) has nonzero b3 and the same
root-exponential rate, since the third-pole term dominates the lower powers
at the saddle. This is a structural hostile test, not a prime-state limit.

## 8. Backward weighting defeats a norm-tail-only certificate

In normalized Hermites, for t=v/u and beta-alpha=2k coordinatewise,

    Phi_alpha,beta(v,u)=sqrt(beta!/alpha!)
        t^(|alpha|/2)(t-1)^|k|/(2^|k| k!).             (22)

Other entries are zero. It follows from direct scaling h_beta(sqrt(t)g),
not a fitted Jacobi model. The diagonal is t^(n/2), so ||Y_K||>=t^K.
For the bounded rational witness (21), the TOP coefficient of
Phi(U,u)Pi_K f has norm squared at least t^K |f_K|², which tends to infinity
for every t>1. Nevertheless the actual F_u(sqrt(t)g) remains bounded by
1/a. Thus partial Hermite sums need not converge in the wider-variance
norm required by this backward propagator. All finite identities remain
valid; extrapolating a forward tail bound through Phi is invalid.

This counterexample uses a nonreal resolvent, not an arbitrary rough F.
For actual current Q the same scalar high-pole obstruction applies. It
blocks the proposed general K^-alpha absolute-flux argument from the
unweighted hierarchy alone. It is NOT a falsification of (13) on the
growing prime state: a signed, actual-state cancellation may still save it.
No actual-state hypothesis proving that cancellation is yet source-closed.

## 9. Rank and Lyapunov structure: exact obstructions to automatic signs

L maps chaos n onto chaos n-2 (harmonic/radial decomposition, or the
triangular monomial inverse of Delta). Its rank is binom(m+n-3,n-2),
not six. Spatial displacement rank controls rational matrix generators
at a state, not this chaos-output dimension. Even the actual prime diagonal
response family has growing dimension: its distinct frequencies are
exp(plus/minus 2pi i log(p)/L). For integer T with L=log(T/(2pi)), opposite
frequency aliases would require pq=T/(2pi) or p/q=T/(2pi), impossible.
Vandermonde evaluations give rank2*pi(N) when d>=2*pi(N). At a scalar
Hermitian base, DQ[B]=Q'(h)B, so nonzero Q'(h) retains these independent
diagonal channels. No fixed-rank implication follows from displacement.
This is a structural response test, not a claim that the arithmetic H_T
is scalar or that its actual signed flux is negative.

Use the exact statewise K2/three-wedge/S4/T12 formulas from the preceding
audit INSIDE (15),(18). They reduce matrix entry evaluation and preserve
phase cancellations. They do not factor Phi or chaos coefficients through
six scalar outputs. Nor may one average rank-six generators as if their
rank ceiling survived averaging; the prior exact rank2+rank2=rank4 witness
still applies. Mixed poles may need both generator families.

The time-dependent finite Lyapunov matrix is exactly X=Phi*Phi-I,
with recurrence (22). It is parity-block structured, generally dense and
full rank, with a positive Gram factorization for Y=X+I. It is not a
positive X: on normalized scalar levels0,2,

    Phi=[[1,(t-1)/sqrt(2)],[0,t]],
    det(X)=-(t-1)²/2<0.                               (23)

The replay checks det=-1/2 at t=2. Therefore a signed finite interior does
not follow automatically. The algebraic Lyapunov equation with positive
forcing also fails on positive eigenvalues of A; use the derived time-
dependent equation instead. NS terminal-gradient compatibility is retained.
Physics positivity-certificate discipline is used to check identity and
sign separately; a Hopf Lyapunov coefficient is not imported as an energy.
LRSC interval/weak-duality certification cannot yet begin: no fixed compact
actual-state core or source-closed signed matrix inequalities are supplied.

## 10. Initial/bulk budgets and the exact remaining constant

The frozen initial-layer bound is retained, not double counted:
I(delta)>=-c_initial and E_>K(delta)<=c_chaos. Higher-order (7) can improve
the tail cost, but replacing that cost would strengthen a DIFFERENT sufficient
inequality; (13) itself is left unchanged. For the proved full-sharp constants
kappa_*=1/2, K1<10,K2<74,sqrt(E_inf)<43/20, an illustrative INITIAL-only
choice delta=1/100000,K=16 pays at most

    c0<28047/34000000,
    epsilon_model-c0>1091269123/472294000000.

These are rigorous cost bounds, not surviving theorem margins. U=1 does
not make the bulk paid; (U/delta)^K is then at least10^80 in Y's norm.
No certified delta,K,U optimizer is obtained.

For norm tails ONLY, exact rational comparison of all r=1,...,8 at U=1
selects r=1 for K=16,64; r=4 for K=256; r=8 for K=1024. This is a
comparison of rigorous bounds (14)/(7), not a numerical proxy. It is NOT
an optimal flux order. Repeated resolvents and factorials make larger r
worse at small K. The complete rational constants and contracted Z bounds
are in the replay; no useful best flux tuple is asserted from that table.

Define the joint covariance-contracted Malliavin deficit

    Ddual_T=E_inf-w0-J_T
       -Re integral_delta^U [<Psi_(K-1),P_(K-1)Z_Q>
                             +<Psi_K,P_K Z_Q>]du.

The ONE remaining exact bound for decision C is

    EXISTS fixed delta,U,K, with the normalizations/quantifiers of (13),
    limsup_T Ddual_T
       <8711/2778200
          -delta kappa_*[sqrt(E_inf)K2+K1²/(K+1)].     (24)

This is exactly equivalent to the frozen equation (13), now expressed using
the actual covariance-contracted second Malliavin derivative and just its
two needed output projections. The required constant is explicit. It is a
SIGNED JOINT bound, including the initial form; removing J_T from it or
claiming it follows from (14)/(16) would be false. It remains asymptotic/
operator-theoretic, not a moderate finite LRSC certificate. The actual
prime-state hypothesis that would save the backward-weighted cancellation
is still the content of (24), not something proved by displacement rank.

## 11. Verification, limitations and preservation

Run `python src/wp84_actual_state_signed_dual_flux.py --output
notes/WP84_ACTUAL_STATE_SIGNED_DUAL_FLUX_REPLAY.json`.
Exact checks pass for both separated parity fluxes, the whole-chain identity,
Malliavin orders1–8, independent Mehler copies, ordered resolvent coefficients,
current K1/K2 normalization, and the indefinite finite dual witness.
An independent nested CP calculation agrees exactly with direct noncommuting
word sums through order3 at the current pole; the ordered Fréchet tensor
bounds also pass. A seven-output diagonal covariance witness has displacement
rank zero and covariance output rank seven, rejecting structural rank-six
scalarization. Omitting the nonzero K+2 flux is deliberately rejected.
The prior verifier's seven deliberate-error checks are retained in the local
history. New checks reject missing nonzero parity flux and inconsistent
radical enclosures. The generated result explicitly records
`consumer_certified=false`, `certified_flux_tuple=null`.

Analytic results: (5)–(22), subject to their stated actual covariance
normalization. Computer-assisted part: finite polynomial algebra and exact
rational order comparisons. OPEN: the signed actual-state bound (24).
No new physical tail theorem, pointwise positivity assertion, raw moment
law, finite-state limit, or unconditional simple-zero percentage is promoted.
The exact remaining consumer margin is UNCERTIFIED, rather than the
initial-budget-only number above. All previous local commits are preserved.
