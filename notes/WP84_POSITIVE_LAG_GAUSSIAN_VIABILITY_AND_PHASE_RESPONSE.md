# Positive-lag Gaussian viability: an all-radius obstruction

Parent: c3fbdd74a1a75ceb8d77ab1066b311bf28f481be.
Branch: codex/c5-c6-attack-20261006. No push. Earlier commits preserved.

**Decision A — GAUSSIAN REFERENCE ITSELF CANNOT WIN.**

For the EXACT localized Gaussian scalar-field consumer, at the frozen
delta=1/100000, for EVERY integer R>=0 and EVERY finite terminal U>=delta,

    E_inf - F_R^G(U,delta) >=109/1000>21/200.             (A)

The full Gaussian-side margin is at most -317503/66000000, even with ZERO
localization cost and ZERO arithmetic comparison error. Thus improving the
tail or proving a full prime CLT cannot make this particular Gaussian
reference close the frozen >79 ledger. This does not disprove strict >79 or
exclude a non-Gaussian arithmetic reference. No arithmetic attack is started.

The user explicitly required stopping if the Gaussian reference is provably
above 0.105 at every radius. That gate is met by a universal spectral
minorant, not by an unfavorable finite numerical search. Later conditional
arithmetic/public-source tasks are therefore not pursued.

## 1. Observable orientation and exact covariance

The compiled signed lower quantity is F_R, whose required value is about
E_inf-0.105, not 0.105. To use the requested upper-consumer convention define

    GaussianValue_R(U)=V_R(U)=E_inf-F_R^G(U,delta).

The viability test is V_R + c_initial + C_loc(R) <21/200. Equivalently,
with w0=1415/13891 and epsilon=8711/2778200,

    epsilon-[E_inf-w0-F_R^G]-c_initial-C_loc(R)>0.

Do not compare the signed F_R itself with 0.105, or subtract the R=0
LOWER BOUND 2813/25750 as though it were an actual measured value.

Keep c=3142/2415, a=131/200, z=c+ia, eta=(c^2+a^2)^(3/2),

    P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3,
    Q_cons(A)=eta P(A)(A-zI)^(-3),
    f(x)=eta^2 P(x)^2/((x-c)^2+a^2)^3,
    E_inf=7761139416076220170204368647089/
          1680256283972002400160000000000.

Let m=R+1. The previous translated-block cylinder, averaged over its central
offsets and the stationary Gaussian baseline, equals the SAME m-site
normalized-trace compiled observable. Every translated m-site window has
the same Gaussian marginal; summing its m central columns recovers trace/m.
This is not the R=0 surrogate for R>0.

The full complex covariance is, for r=i-j,

    E xi_i conj(xi_j)=I1(r), E chi_i conj(xi_j)=i I2(r),
    E xi_i conj(chi_j)=-i I2(r), E chi_i conj(chi_j)=I3(r),
    Ij(r)=int_0^1 s^j exp(i2pi r s) ds,

with zero pseudocovariance. At zero lag I1=1/2,I2=1/3,I3=1/4.
At nonzero lag, t_r=2pi r,

    I1=-i/t_r, I2=-i/t_r+2/t_r^2,
    I3=-i/t_r+3/t_r^2+6i/t_r^3.

The EXACT linear projection alpha=Im xi, beta=2Re xi-2Im chi gives

    Cov(alpha_i,alpha_j)=delta_ij/4,
    Cov(alpha_i,beta_j)=0,
    Cov(beta_i,beta_j)=delta_ij/6
                       -1_(i!=j)/(2pi^2(i-j)^2).       (B)

Consequently the Gaussian source sample is

    W_m=diag(beta)+[diag(alpha),J_m],
    (J_m)_ij=1/(pi(j-i)), i!=j; diagonal zero.

Alpha and beta are independent Gaussian families, by the zero cross block.
This projection retains ALL derivative and cross-lag covariances relevant to
the consumer. Unused scalar coordinates can be integrated out exactly.
It does not replace beta by iid diagonals or alter the K2 signs.

Take independent copies W0,W1,W2 of this field, with the usual shared-noise
Mehler construction. The baseline is I+W0. Define

    B_(u,rho,m)=Re E tau_m Q_cons(I+W0+sqrt(u)Z1)^*
                                     Q_cons(I+W0+sqrt(u)Z2),
    Cov(Z1,Z2)=rho C_ref,
    F_m^G=lambda0 B_(U,1,m)+sum_j lambda_j B_(U,rho_j,m)-B_(delta,1,m).

Conditional on W0, the exact all-n lower witness is bounded above by the
identity OU operator. The scalar cap also gives B_(U,1,m)<=E_inf. Hence

    F_m^G<=E_inf-I_m(delta),
    V_R(U)>=I_m(delta),
    I_m(delta)=E tau_m f(I+sqrt(1+delta)W_m).            (C)

This bounds the COMPLETE signed observable for ALL U, keeping every weak-dual
coefficient and common/difference-copy correlation. It does not estimate
individual signed pieces by absolute values to obtain the Gaussian obstruction.

## 2. Frozen localization constant, without big-O placeholders

Let H_m=sum_(r=1)^m 1/r and

    h_m=8(H_m+1)/(pi^2 m), m=R+1,
    Lambda_U=sum_(j=0)^8 |lambda_j|,
    C0=43/20, C1=10, 2C0 C1=43.

The exact weak-dual coefficients are:

    lambda0=-177474003807058873909/55887390900000000,
    lambda1=-16820385/938417306,
    lambda2=150292891/874129933,
    lambda3=-458723607/134099951,
    lambda4=50678184278/828307931,
    lambda5=-634564925781/913638178,
    lambda6=414028352447/98018322,
    lambda7=-9148412858571/774794887,
    lambda8=4252112992579/373099229.

The rho values are 1/4,1/2,3/4,7/8,15/16,31/32,63/64,127/128.
The upper initial witness is I. Exactly

    Lambda_U=505188015348196189693235774226141659495879806382496275807827042414664568918197834015309/
             16107689666801183743028326831779334846580946960663900516250658618048401530900000000
             =31363.1579573708... .

The inherited eventual scalar second-mass enclosure is C_mass=2; the
uniform taper bound a_phi>=1/2 gives noise alpha mass <=u. Thus the
edge-aware translated-block theorem gives the explicit conservative bound

    |F_T-F_(T,R)|<=C_loc(R;U),
    C_loc(R;U)=43 sqrt(h_m)
                  [Lambda_U sqrt(2+U)+sqrt(2+delta)].  (L)

At a_phi=1 the stronger noise expression uses U/4 and delta/4; (L) freezes
the inherited uniform a_phi>=1/2 enclosure. A height T0 exists for these
eventual bounds; no effective numeric T0 was supplied in the parent.

The scalar cut estimate uses (a_i-a_j)^2<=2a_i^2+2a_j^2 (factor 4 after
summation), both signs of the displacement (factor 2), and

    average_cut ||offblock[diag(a),J]||_(2,tau)^2
          <=h_m C_mass.

K2 is exactly 1/r^2. S2 and S4 have coefficients 1/r^2 and 1/r^4. Their
rank-six/three-wedge contributions have already recombined into the
completed trace: they carry NO extra factor three, six, pi^2, or a separate
error payment in (L). The nonconstant consumer coefficients are the exact
polynomial-division b1,b2,b3 from the parent; their certified aggregate
C0,C1 is used here rather than adding the same word bounds twice.

For R>=2 one completely explicit big-O-free simplification is

    C_loc(R;U)<=C_star(U) sqrt(log R/R),
    C_star(U)=43 sqrt(40)/pi
                    [Lambda_U sqrt(2+U)+sqrt(2+delta)].

It follows from H_m<=1+log m and log(R+1)+2<=5log R.
The exact h_m expression, not this weaker logarithmic envelope, is used
for every minimum-radius computation.

Replacing short physical edge blocks by the T-independent cylinder adds

    |e_edge|<=4(Lambda_U+1) E_inf R/d, d>2R,

and the paid fixed-R parameter freezing contributes o_T(1). These are not
part of the uniform edge-aware bound (L). All radii below are fixed before
T->infinity. An additional Gaussian-side lag payment is required only when
comparing a finite Gaussian value to a FULL Gaussian reference, not when
directly consuming a certified finite-R value as here. No such extra error
is silently counted in the table.

## 3. Exact localization-budget gate

There is no winning U. For ANY permitted U>=delta, (L) is minimized at
U=delta. The following optimistic minima are therefore necessary for this
inherited certificate at every possible fixed terminal U. They do NOT
select a useful U. Monotonicity of (H_m+1)/m proves integer minimality.

| Allocation of epsilon=8711/2778200 | Smallest R at U=delta | Smallest R at illustrative U=1 |
|---|---:|---:|
| Full cushion | 13688829784425016685 | 20719374183222330228 |
| Half cushion | 56455152967537037424 | 85426706689276493190 |
| Quarter cushion | 232615502991921489879 | 351897120001789214516 |
| One tenth cushion | 1509946782718904278568 | 2283490988116224814276 |

These radii are astronomical. For example, the optimistic bound is about
674316.735 at R=32, compared with cushion 0.0031354834065... .
The certificate contains outward rational intervals for the cost at each
minimum and the previous integer. Strict < is verified at the minimum and
fails at its predecessor. For U=delta the squared coefficient is exactly

    C_loc^2=1849 (Lambda_U+1)^2 (2+delta)
                         *8(H_m+1)/(pi^2 m).

Harmonic numbers at huge m are enclosed by

    log m+gamma+1/(2m)-1/(12m^2)<H_m<log m+gamma+1/(2m).

The signed first-omitted-term remainder for positive real arguments is
given in [NIST DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii). Directed
100-digit interval arithmetic is used; no approximate root is rounded into
an integer certificate. These are minima of the STATED certified envelope,
not lower bounds on the true block error.

## 4. Global symmetrized-consumer certificates

Set g(x)=[f(1+x)+f(1-x)]/2. Two exact global inequalities are

    g(x)>=q4(x)=-3/250+(27/50)x^2-(1/50)x^4,           (D4)
    g(x)>=q6(x)=1265/10000-(8561/10000)x^2
                    +(25977/10000)x^4-(13633/10000)x^6. (D6)

Let D_+(x)=((1+x-c)^2+a^2)^3 and D_-(x)=((1-x-c)^2+a^2)^3.
After multiplying by the POSITIVE denominator 2D_+D_-, the difference is

    eta^2[P(1+x)^2 D_-+P(1-x)^2 D_+]
                           -2q_j(x)D_+D_-.

It is an even polynomial in x. In y=x^2 it has degree 8 for q4 and degree
9 for q6. Both have positive value at zero and zero positive-half-line
roots. The producer uses exact SymPy rational root counts; the independent
replay reconstructs the numerator and its Fraction-only Sturm chain from
the consumer coefficients and finds the same zero root counts. Coefficients
are recorded in full in the certificate. No numerical sign grid is accepted
as a proof of either global inequality.

The reconnaissance that proposed q6 was deterministic moment-dual linear
programming, followed by rational downward coefficient repair. High-precision
evaluation of the resulting exact expressions predicts the gaps below.
Only the independently replayed global inequalities and rational moment
bounds are theorem evidence; LP output itself is not a certificate.

## 5. Every block of size m>=3 is excluded by fourth order

The centered Gaussian matrix satisfies W_m equal in law to -W_m. Hence for
t=1+delta,

    I_m(delta)=E tau_m g(sqrt(t)W_m).

Write mu_j=E tau_m W_m^j. From (B),

    mu2=1/6+(1/(pi^2 m))sum_(r=1)^(m-1) (m-r)/r^2.

This increases with m. For m>=3,

    1/6+3/(4pi^2)<=mu2<=1/3.                          (M2)

For any real Gaussian matrix series W=sum g_a E_a, let V=sum E_a^2.
Wick's identity gives

    E tr W^4=2tr V^2+sum_(a,b)tr(E_a E_b E_a E_b)
             <=3tr V^2.

The inequality follows from |tr A^2|<=tr A* A with A=E_a E_b;
cyclicity gives tr A* A=tr E_a^2 E_b^2. For THIS covariance,

    V=(1/6)I+(1/4)[J_m^T J_m+diag(rowmass)],
    rowmass_i=sum_j (J_m)_ij^2<=1/3.

The discrete Hilbert kernel is the compression of the Fourier multiplier
i(theta/pi-1), of norm at most one. Thus ||J_m||op<=1 and

    0<=V<=(1/2)I, tau V=mu2<=1/3,
    mu4<=3tau V^2<=(3/2)mu2<=1/2.                    (M4)

This proof retains Gaussian covariance signs; it does not assume iid matrix
entries, scalar Gaussian eigenvalues, or an independent matrix ensemble.
Using (D4), (M2), and (M4),

    I_m(delta)>=-3/250+(27/50)t[1/6+3/(4pi^2)]-t^2/100
                  =0.1090361897249405489...>109/1000.

A purely rational independent lower certificate replaces pi by 355/113:

    I_m(delta)>=549651397272959/5041000000000000
                  >109/1000, m>=3.                   (E3)

Machin's alternating arctangent series verifies pi<355/113 in the independent
replay. No transcendental decimal enters this rational acceptance gate.

## 6. The two-site block is excluded by sixth order

For m=2 write W_2=[[beta1,c12],[c12,beta2]]. Its eigenvalues are

    v0 +/- sqrt(v1^2+v2^2),

where the three variables are independent centered real Gaussians. For the
scaled INITIAL sample sqrt(t)W_2, their variances, with u=1/pi^2, are

    A=t(1/12-u/4), B=t(1/12+u/4), C=t u/2.

Put r2=B+C, r4=3B^2+2BC+3C^2,
r6=15B^3+9B^2 C+9BC^2+15C^3. The exact trace moments are

    M2=A+r2,
    M4=3A^2+6A r2+r4,
    M6=15A^3+45A^2 r2+15A r4+r6.

Therefore (D6) gives I_2(delta)>=sum_j q6_j M_(2j), which evaluates to
0.110580273577951486768682947292... . Its exact polynomial in u has coefficients

    15209008993027326367/144000000000000000000,
    9653266062152204569/240000000000000000000,
    11054812102925659101/80000000000000000000,
    -40900226982269740899/80000000000000000000.

Machin's bounds give 1/10<u<103/1000. Substituting 1/10 in the positive
terms and 103/1000 in the negative cubic yields the exact, independent bound

    I_2(delta)>=79533722832078710520319925843/
                 720000000000000000000000000000
                  >109/1000.                         (E2)

The preserved one-site certificate gives
I_1(delta)>=2813/25750>109/1000. Together (E2), (E3), and that certificate
prove (A) for EVERY R. This is the first all-positive-lag obstruction;
it is not an extrapolation of the scalar diagnostic.

## 7. Values by radius and gain accounting

The following are CERTIFIED LOWER BOUNDS on the COMPLETE upper-consumer
V_R(U), uniform in U. Decimals are rounded downward; exact outward rational
endpoints are in the certificate. They are not quadrature point estimates.

| R | Lower bound on GaussianValue_R(U), all U |
|---:|---:|
| 0 | 0.109242 |
| 1 | 0.110580 |
| 2 | 0.109036 |
| 3 | 0.117395 |
| 4 | 0.123094 |
| 6 | 0.130450 |
| 8 | 0.135049 |
| 12 | 0.140566 |
| 16 | 0.143805 |
| 24 | 0.147504 |
| 32 | 0.149589 |

For every row the complete signed consumer has the rigorous enclosure

    V_R(U) in [L_R, E_inf(2-sum_(lambda_j<0)lambda_j)].  (V)

The upper endpoint is broad. The lower endpoints alone decide viability,
so a costly complete high-dimensional quadrature search is not needed
after the user's universal-obstruction stop condition has been proved.
There is no favorable radius to certify. No Monte Carlo is used.

The actual gain G_R(U)=V_R(U)-V_0(U) is NOT measured by the difference of
two lower bounds in the table. An immediate rigorous, but broad, enclosure
is [L_R-U_cap,U_cap-L_0] using (V). No sign of G_R or monotonicity of the
actual sequence is claimed. The lower bound is increasing for R>=2;
this is a property of the bound, not a monotonicity theorem for f.
What IS proved is that no decrease can cross 0.105.

The geometry can nevertheless be separated exactly at the moment level:

    mu2=1/6+(1/(pi^2 m))sum_(r<m)(m-r)/r^2,
    first-lag contribution=(m-1)/(pi^2 m).

Let S_j=sum_(r<m)(m-r)/r^j and v_i=sum_j J_ij^2. The exact fourth-order
decomposition is

    mu4 = 1/12
          +2S2/(3pi^2 m)
          -S4/(pi^4 m)
          +[tr J^4+4sum_i v_i^2+sum_(i,j)J_ij^4]/(8m). (W)

These terms are respectively diagonal Gaussian energy, adjacent
diagonal/off-diagonal pair words, the negative diagonal-covariance correction,
and the coupled alpha-commutator Wick contribution. Direct four-index Wick
summation independently checks (W) symbolically at m=2,3,4 with 1/pi left
as a formal variable. In the large-section limit the four terms tend to
1/12,1/9,-1/90,1/12; thus mu4->4/15. In particular, the Gaussian centered
fourth moment differs from the frozen connected arithmetic/model value 1/4
by 1/60. That is not imported as an arithmetic moment claim.

Derivative coordinates are quantitatively essential: at one site the
variance contributions to beta=2Re xi-2Im chi are 1, 1/2, and -4/3,
summing to 1/6. Omitting chi or its cross covariance gives a different
reference. The off-diagonal K2 energy and three-wedge Gram are two exact
representations of the SAME consumer term, not two additive improvements.
For the nonlinear rational observable there is no canonical additive split
of G_R into all the requested overlapping labels. A telescope of altered
models would depend on the chosen order. No such artificial gain ledger is
substituted for the complete signed observable. Mehler cross-copy coupling
is preserved in (C); its exact weak-dual inequality makes it unable to
overcome the certified initial-energy obstruction, regardless of U.

## 8. Full Gaussian-side ledger and localization's first loss

The upper payment charged by the frozen certified ledger is

    c_initial,up=53503/66000000.

Even granting zero arithmetic and quadrature errors, zero physical edge
loss, and zero localization cost, the certified complete margin obeys

    margin<=epsilon-[V_R-w0]-53503/66000000
           <=21/200-109/1000-53503/66000000
            =-317503/66000000<0.                     (LEDGER)

This negative margin is a Gaussian-reference obstruction. It is not a
negative actual-prime margin. Adding the explicit nonnegative (L) can only
worsen it. The previously paid covariance/background/zero-side costs and
physical tail cap remain in their frozen scopes; no cost is waived or paid
twice. The synthetic benchmark is never used.

The first square-root loss in the old localization proof is

    average_cut ||Delta||_(2,tau)
                <=sqrt(average_cut ||Delta||_(2,tau)^2),

after the first-order consumer Lipschitz estimate. Absolute dual coefficients
add amplification Lambda_U=31363.1579... . These identify where a signed
boundary-flux or second-order pinching improvement would have to enter.
However, the user permitted that optimization only on a viable Gaussian
route and explicitly required stopping upon an all-R obstruction. No new
tail optimization is undertaken. Even an exact zero-error localization
theorem would leave (LEDGER) negative. Decision D (localization dominant)
is therefore weaker than, and superseded by, decision A.

## 9. Frozen phase-response equations, without starting an arithmetic attack

For completeness, the two equations from the parent remain explicit.
Let x_p(k) be the REAL vector whose complex coordinate pair at lag r is

    c_p exp(i(T+2pi k/L)log p)
                      (exp(i2pi r log p/L),
                       i(log p/L)exp(i2pi r log p/L)).

Include retained powers in the same prime-base group if not using the
already justified Lipschitz proper-power disposal. For any ordering of
primes, let

    Y_p(k,g)=sum_(q preceding p) g_q
                        +sum_(q following p) x_q(k),

with independent matching Gaussian contributions g_q, and Sigma_p their
independent-circle covariance. The current prime is excluded exactly.
The two response terms are

    A1_(T,R)=sum_p (1/d)sum_(k=0)^(d-1)
                   E_g sum_a partial_a Phi_R(Y_p(k,g)) x_(p,a)(k),
    A2_(T,R)=(1/(2d))sum_p sum_(k=0)^(d-1)
                   E_g sum_(a,b) partial_ab Phi_R(Y_p(k,g))
                         [x_(p,a)(k)x_(p,b)(k)-(Sigma_p)_ab].

The remainder is bounded by the parent's uniform third derivative envelope
times the prime-base cube mass O_R(L^-3). Neither response is certified
o(1). Their explicit leave-one-prime states and Fourier/alias obligations
are frozen, not attacked in this audit. Closing either or both cannot cure
the Gaussian-side contradiction to the desired ledger.

No favorable fixed R is selected, and no new arithmetic theorem is proposed
as the active next debt. The public 0.7947 candidate machinery is not reopened:
its previous DIRECT/ADAPTABLE/INCOMPATIBLE classification remains recorded in
WP84_DIRECT_PRIME_FIELD_STATE_LAW. The present stop gate precedes the user's
conditional response-spectrum, Fourier-degree, block-translation and public
dictionary tasks. No independence, spectral gap, cancellation or transfer
claim is invented to bypass that ordering.

## 10. Verification, provenance, and scope

Run:

    python src/wp84_positive_lag_gaussian_viability.py
    python src/wp84_positive_lag_gaussian_viability_replay.py
    python src/wp84_direct_prime_field_scalar_gaussian_replay.py

The producer checks exact global consumer minorants, symbolically checks
the finite Gaussian Wick geometry, creates the rational/interval radius
table, and copies the frozen weak-dual witnesses. The independent replay
uses only standard-library Fraction arithmetic and the existing independent
all-n dual checker. It reconstructs both minorant polynomials from P,c,a,
implements Sturm remainders without SymPy, derives the two-site moments by
independent polynomial convolution, verifies Machin bounds and the rational
all-R negative ledger. No producer import, interval engine, approximate
eigenvalue, sampled Gaussian value, or Monte Carlo is used in its acceptance.

The minimum-radius table additionally uses directed mpmath interval arithmetic
and the cited positive-real digamma remainder. The certificate supplies full
rational polynomial coefficients, source hashes and all predecessor/minimum
cost intervals. Independent Gaussian proof replay does not claim an independent
implementation of the interval radius search.

Preserved sources: the parent scalar-field state law and its certificate;
the tail-capped exact-frontier consumer; K2/displacement identities and the
all-n weak-dual certificate. No historical local commit is amended. Strict
>79 is still OPEN, and this Gaussian-reference route is now excluded for
the frozen consumer, witness pair and delta. Changing that tuple would be a
different viability problem; no such replacement is made here.
