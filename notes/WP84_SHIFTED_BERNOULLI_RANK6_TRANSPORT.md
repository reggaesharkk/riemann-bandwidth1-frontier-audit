# Shifted Bernoulli rank-six transport: exact drift elimination, infinite jet obstruction

Date: 2026-10-07. Parent: f9158e19daf4d3ae44d00beca1173f0c98280c94.

Status: STOP at the requested finite-state closure gate. No >79 theorem.
The bounded consumer remains valid. Its displacement rank does not imply a
finite-dimensional dilation-invariant rational state. No raw-moment,
fixed-band B-to-C, or connected quartic norm argument is used.

## 1. Normalization and exact finite-t generator

Set z=(4/5)(1+i), s=s0(T) real, and

    P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3,
    f(x)=p_s(x)=(32/25)^3 P(x)^2/(((x-4/5)^2+16/25)^3).

The subscript on p_s denotes the shifted consumer, not the background s.
Use normalized trace tau=tr/d, H_t=H0+sum xi_p(t)G_p,
H0=sI+E0, and independent Bernoulli(t) variables. Define F_f(H)=tau f(H),
Q_f(t)=E sum_p D^2 F_f(H_t)[G_p,G_p], and
C_f(t)=E DF_f(H_t)[H_t-H0]. Fréchet derivatives are matrix derivatives.

For forced-absent/present states H^-_p,H^+_p, put
Delta_p F=F(H^+_p)-F(H^-_p) and
Delta_p DF=DF(H^+_p)[G_p]-DF(H^-_p)[G_p]. Then EXACTLY,

    E_f'(t)=sum_p E Delta_p F_f,
    C_f(t)=t E DF_f(H_t)[Pfull]
             +t(1-t)sum_p E Delta_p DF_f,
    Pfull=sum_p G_p.

The latter identity is Bernoulli self-consistency, not an approximation.
Taylor expansion at fixed nonreal poles, with kappa_T=sum ||G_p||^3,
gives E_f'=A_f+(1-2t)Q_f/2+O_f(kappa_T) and
C_f=t A_f+t(1-t)Q_f+O_f(t kappa_T).
Hence the independent prime drift A_f disappears:

    t E_f'(t)=E tau[(H_t-sI)f'(H_t)]-t Q_f(t)/2
               -E DF_f(H_t)[E0]+epsilon_f(t),                 (1)
    |epsilon_f(t)| <= C_f t kappa_T.

One may define epsilon exactly as t E_f'-C_f+t Q_f/2; the displayed
estimate is the second-order consequence, not an exact zero remainder.
Background error is bounded by C_f ||E0||_1/d. Neither division of that
uniform bound by t nor integration of an unspecified o(1)/t is justified.
This distinction matters at the small-t endpoint.

## 2. Independent one-point derivation and grouped forcing

Write R=(H-zI)^-1, m=E tau R, Xi_T=E sum_p tau((G_p R)^2).
Then B=E sum tau(R G_p R G_p R)=partial_z Xi_T/2.
For scalar background the exact state identity is
C_R=m+(z-s)m_z. Applying Bernoulli self-consistency gives

    t m_t+m+(z-s)m_z = -t Xi_T,z/2 + O(t kappa_T).

For actual H0 add +E tau(R E0 R) to the right. Differentiating q times
in z is valid on a fixed strip. In particular q=0,1,2 gives deterministic
terms (q+1)m^(q)+(z-s)m^(q+1).

The exact coefficients are

    Einf=122310623232/120599925625,
    A=-183845781504/120599925625+i112029847146/602999628125,
    Bc=297763801992/602999628125-i623773801728/602999628125,
    C=1589960358912/15074990703125+i2139153937184/15074990703125.

For each real x the rational identity is
f(x)=Einf+2 Re[A/(x-z)+Bc/(x-z)^2+2C/(x-z)^3]. Consequently
E_f=Einf+2 Re[A m+Bc m_z+C m_zz]. Its deterministic term is

    -2 Re[A(m+(z-s)m_z)
           +Bc(2m_z+(z-s)m_zz)
           +C(3m_zz+(z-s)m_zzz)].                            (2)

Its complete covariance forcing in (1) is the SINGLE object

    -t Re[A Xi_T,z+Bc Xi_T,zz+C Xi_T,zzz].                   (3)

Equivalently Q_f/2=Re[A Xi_T,z+Bc Xi_T,zz+C Xi_T,zzz].
No channelwise absolute values are taken. Equations (1) and (2)-(3) agree
by rational functional calculus; the matching script checks the scalar
identity exactly. The m_zzz term in (2) is essential, not an independent
prime drift and not removable by relabeling Xi.

The explicit resonant Xi is the PRIMITIVE in
WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL: the D2 coefficient is Xi_z/2.
WP84_BERNOULLI_DRIFT_ELIMINATION section 6 calls the displayed primitive
Xi the coefficient itself; using it that way misses a derivative and 1/2.
Here Xi_T is exact finite-T; replacement by resonant Xi and its derivatives
requires the separate uniform covariance and carrier closure hypotheses.

## 3. Small channels do not close the spectral jet

For the sharp real Loewner state, J_ij=1/[pi(j-i)], D=diag(k),
u=R1, v=Ra, r=diag R, h=diag(JR), q=diag(JRJ),

    [D,R]=(v u^T-u v^T)/pi,
    Xi_res= sum r_i^2/(6 a_phi^2 d)
       -sum_(i!=j) R_ij^2/[2 a_phi^2 pi^2 d(i-j)^2]
       +(sum h_i^2-sum r_i q_i)/(2 a_phi^2 d).

Substitute R_ij=(v_i u_j-u_i v_j)/[pi(i-j)]. The only two-index
term is a rank-two generator contraction with kernel (i-j)^-4.
Its Fourier kernel is

    S4(theta)=pi^4/45-pi^2 theta^2/6+pi theta^3/6-theta^4/24,
    0<=theta<=2pi.

S2(theta)=pi^2/3-pi theta+theta^2/2 handles the rank-three BR channel.
Exactly [D,BR]=[1 w^T+(Bv-alpha)u^T-(Bu)v^T]/pi,
w=R alpha. Thus a primitive uses 2x2 or 3x3 Fourier matrices and O(d)
vectors, not a dense d-by-d theorem interface. The cubic Cayley factor
has six displacement columns. z differentiation gives derivatives of
these vectors; finite displacement rank does NOT bound the number of
spectral derivatives in the time evolution.

The general real-Gaussian Hadamard map, with covariance matrices
A0=E aa^T,Hc=E beta beta^T,C0=E beta a^T, is exactly

    V(X)=Hc o X+(C0 o X)J-C0 o(XJ)
       +C0^T o(JX)-J(C0^T o X)
       +(A0 o(JX))J-A0 o(JXJ)-J(A0 o X)J+J(A0 o(XJ)).

Use covariances of the actual real Bernoulli-to-Gaussian directions.
The circular artificial field in the Hadamard source is not automatically
the same covariance ensemble. The resonant specialization yields the
primitive above under its substitution gates; no circular variance factor
is silently imported.

## 4. Exact obstruction to the requested finite coefficient matrix

Let L_s=(x-s)partial_x, with real s. On e_j=(x-z)^-j,

    L_s e_j=-j e_j-j(z-s)e_(j+1).                           (4)

Since Im z=4/5, z-s is nonzero. There is no finite rational basis with
fixed poles containing f and invariant under L_s. Indeed f has an actual
order-three pole at z, since

    P(z)=(-273989+90672i)/347275 !=0,
    leading Laurent coefficient f at z = 2C !=0.

The leading pole coefficient of L_s^n f at order 3+n is

    2C (-1)^n [(n+2)!/2!] (z-s)^n !=0.                     (5)

Distinct pole orders imply linear independence. This is an all-n theorem,
not a truncation diagnostic. Adding f' or f'' only enlarges the same
infinite hierarchy. In resolvent notation the smallest invariant span
generated by the consumer is countably infinite; a convenient containing
basis is 1,(x-z)^-j,(x-conjugate z)^-j for j>=1.
The real cyclic basis {L_s^n f:n>=0} is already linearly independent.
The constant component has eigenvalue zero. A proposed 3-complex/6-real
fixed-pole state is not invariant and has no exact M_s.

For a truncation at order J, the missing equation contains
-J(z-s)e_(J+1); discarding it is a new approximation requiring a budget.
Neither Gram positivity nor a covariance sign repairs this deterministic
failure. The exact infinite upper-shift coefficient system is (4), together
with the conjugate block; finite triangular truncations are not the flow.

Moving poles would avoid this particular jet expansion but are a different
interface. Adjoint test transport requires z_t=s+t(z-s), whose imaginary
part is (4/5)t. This collapses the strip at t=0 and is precisely the
characteristic shortcut the user forbids. Rank-six spatial displacement
and finite fixed-pole temporal closure are distinct statements.

## 5. Gaussian comparison and endpoint evidence boundary

Lindeberg replacement is valid for this fixed rational f and m derivatives
through order two: bounded Fréchet third derivatives at pole gap 4/5 give
uniform error O(kappa_T). Higher fixed spectral derivatives similarly work
on compact strips. This does not supply an infinite-jet estimate or a
small-t moving-pole estimate. No conditional-variance Wegner claim is used.

Background scalarization gives E_f(0)=f(s0(T))+o(1), s0(T)->1. Exactly

    f(1)=73041477632/948011895353
        =0.07704700541210235245996346... .

This is not the model value w0=1415/13891. At finite T, bounded rational
functional calculus makes E_f continuous at t=0; exact Bernoulli generator
integration is unproblematic. For any delta>0, drift-free (1) gives

    E_f(1)=E_f(delta)+integral_delta^1
       [E tau L_s f(H_t)/t-Q_f(t)/2
        -E DF_f(H_t)[E0]/t+epsilon_f(t)/t] dt.              (6)

At fixed finite T the delta->0 limit of the grouped expression exists by
the exact generator identity. Separating its background error or replacing
it by a uniform asymptotic o(1) before this limit is not justified. Thus (6)
is an exact finite-T endpoint identity with defined remainder, not the
requested source-closed uniform endpoint theorem.

The nominal increase allowed above the background is
21/200-f(1)=5299954276013/189602379070600, approximately 0.027953.
The MODEL-relative cushion remains exactly 8711/2778200.
Neither number bounds the integrated forcing. No theorem loss has been
certified and no simple-zero coefficient is promoted.

## 6. Stop decision and provenance

The requested stop condition is met: shifted transport does not close on
the requested finite fixed rational/resolvent state. Stop here before
searching a covariance sign or Monte Carlo surrogate for a nonexistent
finite M_s. This is not a proof that every bounded rank-six route is false.
An infinite hierarchy, a controlled functional PDE, or a moving-pole method
with a separately proved uniform endpoint layer would be a different route.
No long-product law reappeared. No covariance sign counterexample is claimed.
Strict >79 remains OPEN; this finite-state implementation is BLOCKED.

Full requested sources read: WP84_BERNOULLI_COMMON_STATE_GENERATOR,
WP84_BERNOULLI_DRIFT_ELIMINATION, WP84_BERNOULLI_GAUSSIAN_INVARIANCE,
WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL, WP84_GAUSSIAN_COVARIANCE_HADAMARD,
WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION,
WP84_D1_D2_SMALL_CHANNEL_CLOSURE, WP84_SHIFTED_EXACT_FRONTIER_RANK6.
Additional sources: WP84_BACKGROUND_SCALARIZATION,
WP84_BR_RANK3_SCALAR_D1, WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.
All are notes/*.md. Earlier audits and the NotebookLM packet are unchanged.

Verifier: python src/wp84_shifted_bernoulli_rank6_transport.py.
It checks exact partial fractions, dilation, leading-pole recurrence,
background and cushions. The infinite-dimensional conclusion follows from
(5) for every n, not just the finitely many regression checks.
