# Tail-capped exact-frontier consumer: small-ball obligation eliminated

Date: 2026-10-07. Parent: f7089e2197b2490a0d70bb7c42ae4cfd98f9ffa3.
Decision **D. BETTER TAIL-CAPPED CONSUMER FOUND**, with the tail-elimination
conclusion of A. Strict >79 curvature theorem remains OPEN. No push.

## 1. Exact family and frozen model

Let P(x)=1-Ax+Bx^2-Cx^3 with

    A=43428/13891, B=37704/13891, C=9660/13891,
    c=B/(3C)=3142/2415,
    a>0 rational, r2=c^2+a^2,
    f_a(x)=r2^3 P(x)^2/(((x-c)^2+a^2)^3),
    Einf(a)=r2^3 C^2.

The denominator is positive on R, f_a(0)=1, and f_a(x_j)=0 at the
three positive Christoffel nodes P(x_j)=0. Thus the frozen four-node
quadrature from WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY has

    E_model f_a=w0=1415/13891,
    1-2w0=11061/13891,
    21/200-w0=8711/2778200=0.003135483406522208624289... .

This statement uses the frozen MODEL measure, not the unknown actual
prime spectral law. Changing Einf does not change model saturation or
the model-relative cushion.

## 2. Support certificate, including the whole a>0 family

For b=a^2 define

    L_b(y)=(c^2+b)^3(1+Ay+By^2+Cy^3)^2-((y+c)^2+b)^3.

The constant coefficient is zero. Each of its six other coefficients is
a polynomial in b with nonnegative rational coefficients and strictly
positive constant term. The exact script expands and checks every one.
Thus all six coefficients are strictly positive for EVERY b>=0.
This proves f_a(x)>=1 for x<=0 for all a>0, and hence

    1-f_a(x)<=1_(x>0).

For the requested a=2/3 the ascending coefficients of y^1 through y^6 are

    3330373521107111880027904/131225134660629062484375,
    1164738199599453031625511136576/12759938418995588148793171875,
    4771098545407574796801097984/37200986644302006264703125,
    41414016734042023573138469624/472590311814651412918265625,
    153450531794259105396041236/5283618392958835672378125,
    24419244397558737332279/6563501109265634375625.

These are exact positive rationals; no floating-point sign test is used.

## 3. Global upper cap and independent Sturm replay

For any center c0, set
U_(c0,a)(x)=C^2(((x-c0)^2+a^2)^3)-P(x)^2.
The x^6 coefficient cancels and the x^5 coefficient is

    2C(B-3c0 C).

At c0=c it is zero, leaving a quartic. For a=2/3 that quartic is

    (233119584/192959881)x^4
    -(586555741960/93199622523)x^3
    +(310531081320512/25008565377005)x^2
    -(9955777537241639624/905935280782006125)x
    +24419244397558737332279/6563501109265634375625.

Its leading and constant coefficients are positive. The exact Sturm chain
has degrees 4,3,2,1,0 and signs

    -infinity: +,-,-,-,+   (2 variations),
    +infinity: +,+,-,+,+   (2 variations).

Therefore it has zero real roots and is strictly positive everywhere.
The verifier checks this both with SymPy's exact rational root count and
an independently implemented polynomial-remainder Sturm algorithm using
only standard-library Fraction arithmetic. Positive rescaling of each
Sturm polynomial preserves endpoint signs. This independently reproduces
the certificate rather than calling the same root counter twice.

Consequently

    0<=f_(2/3)(x)<Einf(2/3) for finite real x,
    Einf(2/3)=30982745506824371707904/6563501109265634375625
             =4.720460161587588332381... .

The limit at either infinity equals Einf, so the non-strict global upper
cap is valid. Identical exact certificates hold for 131/200 and 451/1000.
For 131/200 the Sturm endpoint signs are the same as above. For 451/1000
they are +,-,+,+,+ and +,+,+,-,+, again two variations each.

Moreover cap safety is monotone in a: if a>=a0>0,

    U_a-U_a0=C^2[( (x-c)^2+a^2)^3-((x-c)^2+a0^2)^3]>=0.

Since a0=451/1000 has strict positivity, the ENTIRE half-line
a>=451/1000 is cap-safe. Together with section 2 this certifies every
rational candidate searched on this half-line. This is a sufficient
cap-safe family, not a claim that 451/1000 is the exact minimum admissible a.

## 4. Structural uniqueness of the center

At both signed infinities,

    f_(c0,a)(x)/Einf(c0,a)
       =1+(6c0-2B/C)/x+O(x^-2).

If the 1/x coefficient were nonzero, one of the two tails would exceed
one. Hence a global cap at Einf FORCES c0=B/(3C), independently of a.
Equivalently a globally nonnegative U cannot have an odd-degree leading
term. This is a necessary center uniqueness theorem inside this particular
repeated-pole family, not uniqueness among all rational consumers.

## 5. Tail-sign theorem and the stronger finite-U observation

Let A_T=H_1 be any deterministic Hermitian endpoint and W_T any centered
Gaussian Hermitian series at finite dimension, with its actual covariance.
Define Phi_T(u)=E tau f_a(A_T+sqrt(u)W_T). Functional calculus gives

    0<=Phi_T(u)<=Einf(a) for EVERY u>=0.

For the actual finite-prime circular quadrature noise, the corrected
invertibility proof in WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW section 10
gives W_T invertible almost surely. Bounded dominated convergence then
gives Phi_T(u)->Einf(a) at fixed dimension. Therefore the improper SIGNED
tail integral exists and satisfies

    integral_U^infinity Phi_T'(u)du=Einf(a)-Phi_T(U)>=0.

No assertion of absolute curvature integrability or pointwise positive
curvature follows. The tail need not be monotone in U.

The crucial finite-U truncation is EVEN STRONGER than this argument:

    Phi_T(0)=Phi_T(U)-integral_0^U Phi_T'(u)du
             <=Einf(a)-integral_0^U Phi_T'(u)du.            (1)

It uses only the cap and the finite heat identity. It does not require
invertibility, a large-u limit, or any spectral small-ball bound at all.
It even holds for singular or zero Gaussian noise. A cap-safe consumer
therefore eliminates the entire large-u endpoint obligation for this
one-sided theorem. No actual-prime averaged small-ball theorem is used.

## 6. Exact quantifiers and what finite-U theorem is still required

Write J_T(U)=integral_0^U Phi_T'(u)du. For each fixed U assume a
SOURCE-CLOSED deterministic lower bound

    liminf_(T->infinity) J_T(U)>=I(U).

Equation (1) implies

    limsup_T tau f_a(H_T)<=Einf(a)-I(U)

for each such fixed U. Thus if there exists a fixed U with
I(U)>Einf(a)-21/200, strict >79 follows after the separate zero-side
consumer transfers. It is also sufficient that

    limsup_(U->infinity) I(U)>Einf(a)-21/200.

The strict gap then selects ONE finite U with a strict inequality; only
after selecting that U is T taken to infinity. No U(T), uniform-u limit,
or interchange of T with u=infinity is needed. A limiting lower bound
equal to the threshold gives no strict >79 conclusion.

Fixed-U covariance substitution errors can now tend to zero at fixed
terminal pole distance a. Background trace-norm scalarization can also be
paid at fixed poles as in the parent audit. Remaining covariance,
curvature and zero-side source obligations are not promoted by the cap.

## 7. Conditioning search and a better rational candidate

Two different diagnostics are required:

    N0(a)=|A_a|+|B_a|+|C_a|,
    Neta(a)=|A_a|/a+|B_a|/a^2+2|C_a|/a^3.

The preferred conditioning-tuned rational choice is

    a=131/200=0.655, c=3142/2415,
    Einf=7761139416076220170204368647089/1680256283972002400160000000000
        =4.619021211293706239000... .

Independent reconnaissance places the weighted proxy minimum near 0.6553.
On the EXACT certified family, a grid a=k/1000 for 451<=k<=3000 has
its numerical weighted minimum at 655/1000=131/200. The selected value
is a simple rational near the continuous diagnostic optimum, not a proved
global optimum over all real a or all cap-safe rationals. Interval arithmetic
CERTIFIES that its weighted proxy improves upon 2/3; numerical search
claims are kept separate from theorem certificates.

| Consumer | N0 | Neta |
|---|---:|---:|
| tail-cap a=2/3 | 7.74923421026719 | 16.41682468145197 |
| tail-cap a=131/200 | 7.50329211085384 | 16.40856280931999 |
| tail-cap a=451/1000 | 4.43066422432219 | 20.53727196071647 |
| old shifted c=a=4/5 | 2.85877982508708 | 4.40132042226141 |
| canonical c=0, a^3=13891/9660 | about 13.0089 | about 11.4935 |

The first four rows have 45-digit outward interval computations in the
verifier. The canonical row is independently evaluated from its algebraic
pole and the general formulas below, as a numerical conditioning diagnostic.
The smaller-a candidate improves the raw norm but worsens the weighted
proxy: there is no single optimum until an actual theorem norm is chosen.
Large proxies prove neither failure of the grouped curvature inequality
nor a necessary loss exceeding 8711/2778200. No rigorous conditioning
obstruction is found, so decision B is not justified.

## 8. Exact one-point coefficients and rank-six Cayley architecture

The following formulas specify the coefficients EXACTLY for every certified
rational candidate without enormous expanded integers. Put

    z=c+i a, delta=2i a, r3=(c^2+a^2)^(3/2),
    p=P(z), p1=P'(z), p2=P''(z), r6=(c^2+a^2)^3.

Then

    A_a=r6[(p1^2+p p2)/delta^3-6p p1/delta^4+6p^2/delta^5],
    B_a=r6[2p p1/delta^3-3p^2/delta^4],
    C_a=r6 p^2/(2delta^3).

All three lie in Q(i) for rational c,a. The exact representation is

    f_a(x)=Einf+2 Re[A_a/(x-z)+B_a/(x-z)^2+2C_a/(x-z)^3],
    tau f_a(H)=Einf+2 Re[A_a m+B_a m_z+C_a m_zz].

In particular Re A_a=0 at the forced center, independently checked in
the script. Exact expanded coefficients for each candidate are emitted
by the verifier. Partial-fraction identities are checked as rational
identities, not fits to sample points.

Define U=(H-conjugate z I)(H-zI)^-1 and Q=r3 P(H)(H-zI)^-3.
Then Q*Q=f_a(H) and Q=q(U), where with v=z u-conjugate z,

    q(u)=r3/delta^3[(u-1)^3-A v(u-1)^2+B v^2(u-1)-C v^3].

It has degree at most three, with coefficients in Q(sqrt(c^2+a^2),i).
For real symmetric H, U^T=U, Q^T=Q, and [D,Q]^T=-[D,Q].
If rank[D,H]<=2, then rank[D,U]<=2. Write [D,U]=g h^T-h g^T.
With q=q0+q1u+q2u^2+q3u^3, let

    G=[g,h,Ug,Uh,U^2g,U^2h],
    J2=[[0,1],[-1,0]],
    K3=[[q1,q2,q3],[q2,q3,0],[q3,0,0]].

The exact polynomial commutator identity gives

    [D,Q]=G (K3 tensor J2) G^T, rank[D,Q]<=6.

The middle matrix is skew and det K3=-q3^3. Its skew bilinear form has
at most three wedge pairs. This preserves the three-wedge/six-column
architecture; the positive factor itself need not have matrix rank six.
The symmetry statements require the actual real symmetric sharp Loewner
state (or scalar background). A generic non-symmetric Hermitian matrix
retains the energy identity but does not imply Q^T=Q. Actual taper and
background transfer remain separate obligations.

## 9. Grouped curvature and the new finite-U target

For W=sum_j g_j E_j with independent standard REAL Gaussian coordinates,
V(X)=sum_j E_j X E_j. In the quadrature bridge E_j are the cosine and
sine directions divided by sqrt2. Let

    R_u(z)=(H_1+sqrt(u)W-zI)^-1,
    Xi_u(z)=E sum_j tau((E_j R_u(z))^2).

Gaussian differentiation gives partial_u m=Xi_z/2. Therefore exactly at
finite dimension

    Phi_T'(u)=Re[A_a Xi_z+B_a Xi_zz+C_a Xi_zzz].            (2)

This is the SAME grouped stencil as before, at the new pole. No extra
factor 2 or variance factor is imported. The exact finite-prime primitive
can be used; replacing it by the explicit resonant primitive is a fixed-U
source substitution. Preserve (2) as one grouped object, not three
absolute-value debts.

For the selected candidate, the new strict >79 requirement is simply

    liminf_T integral_0^U Phi_T'(u)du
      > 7761139416076220170204368647089/1680256283972002400160000000000
        -21/200

for SOME FIXED finite U, or the limiting lower-bound condition in section 6.
The model total integral would be Einf-w0 if its own heat boundary holds;
the gap between that benchmark and this threshold is still 8711/2778200.
No such one-sided actual-state finite-U curvature lower bound is proved
here. The tail gate is CLOSED by global scalar algebra. The >79 route
is closer in the precise sense that its small-ball and growing-U debts
have disappeared; its curvature and zero-side transfer debts remain OPEN.

## Verification and preserved evidence boundary

Run python src/wp84_tail_capped_exact_frontier_consumer.py --search.
Exact Fraction/SymPy support and dual Sturm certificates, exact coefficient
and Cayley identities, and interval improvement comparisons pass. Grid
optimization and canonical proxy decimals are diagnostics. No Monte Carlo.
Python -O is rejected. Earlier local commits and the NotebookLM packet
remain unchanged. No raw-moment, B-to-C, finite M_s, or small-ball attack
is reopened.
