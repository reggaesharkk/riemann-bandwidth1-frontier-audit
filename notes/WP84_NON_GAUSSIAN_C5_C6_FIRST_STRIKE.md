# Non-Gaussian C5/C6 first strike: one signed arithmetic theorem

Date: 2026-10-07. Parent: adbaef99d4aa6fd16119135a349facc127a8ca54.
Branch: codex/c5-c6-attack-20261006. All earlier local commits preserved.

**Decision B — REDUCED TO ONE SIGNED NEAR-PRODUCT THEOREM.**
The exact sufficient theorem is (12) below. It consumes the actual filtered
fifth/sixth sum, including every unresolved population and alias, rather
than assuming a finite-band equality with sharp continuum cumulants.
The theorem remains OPEN. Strict >79 remains CONDITIONAL on that theorem
and the inherited lower-moment, matrix-normalization, functional-band and
zero-side hypotheses. No prime inequality is proved by the finite replays.

The Gaussian obstruction is permanent. This audit does not improve a CLT,
Gaussian localization, a Gaussian master law, or the prime cutoff. It does
not reoptimize the consumer around an unproved arithmetic interface.

## 1. Freeze the old Gaussian obstruction and identify the new consumer

For the previous physical resolvent/Mehler consumer, every R_lag and finite U
has Gaussian defect at least 109/1000. Thus a favorable limiting arithmetic
gain must exceed

    Gain_arith > 109/1000 - 21/200 = 1/250 = 0.004

before payments. With its frozen initial upper payment,

    Gain_arith > 1/250 + 53503/66000000
               = 317503/66000000 = 0.00481065151515... .       (1)

Any additional new paid cost e raises this threshold by e. Its physical
edge and parameter costs are o_T(1) at a fixed radius; its tail cap and exact
telescope carry no extra limiting payment. The old localization cost is
nonnegative and would also have to be added if that route were consumed.
We do not choose or optimize R_lag or U. These are necessary gain lower
bounds from a Gaussian lower bound, not an evaluation of the true gain.

The new route uses a DIFFERENT bounded consumer. Do not carry the old
Mehler initial payment or localization cost into it a second time. Freeze

    R_band = 6000, a_pole = 221/200,
    q(X) = -19101/185500 + (961/3710)X
           + (31/50)X^2 - (371/500)X^3,
    P_dag(x)=q(x-1),
    p_dag(x)=a_pole^6 P_dag(x)^2/(x^2+a_pole^2)^3.

The inherited exact support certificate gives p_dag>=1 on x<=0,
p_dag>=0 globally and p_dag<=P_dag^2. The polynomial square is consumed
only on the fixed-band selected section. The bounded consumer handles
full-to-band comparison and principal deletion.

Independently convolving the four rational coefficients gives

| order | coefficient in q(X)^2 |
| --- | --- |
| 0 | 364848201/34410250000 |
| 1 | -18356061/344102500 |
| 2 | -26060119/430128125 |
| 3 | 21981971/46375000 |
| 4 | **0** |
| 5 | -11501/12500 |
| 6 | 137641/250000 |

Write A=11501/12500 and B=137641/250000 throughout. A,B here are consumer
weights, not the transport objects A_b,T,R and B_b,T,R.

## 2. Exact joint consumer gate; positive deficits versus signed deficits

Freeze the lower-moment directions used by the robust note:

    mu1^c=o(1), mu3^c=o(1),
    mu2^c >= 1/3 - 2/(pi^2 R_band) + o(1).

Their application must be on the SAME selected section and in the SAME
centered Weil/prime normalization. This note does not newly prove that
source interface. In particular a scalar third-moment gate is not a tensor
{3,3} cancellation theorem.

Let E_base=c0+c2/3. At mu5=1/36, mu6=34/135,

    E_rob = E_base - A/36 + B*(34/135)
          = 240421959557/2322691875000.

Using the frozen exact curvature bound 137721/5000 and pi>333/106,

    e_band = 128952763/92407500000,
    e_var  = 26060119/12734908593750,
    M = 21/200 - E_rob - e_band - e_var
      = 52897896569489/572357731837500000
      = 0.00009242103954753147... .                         (2)

The sufficient positive-deficit budget is exactly the requested

    A*(1/36-mu5)_+ + B*(mu6-34/135)_+ < M.                 (3)

Positive-part clipping makes (3) STRONGER than the single signed condition:
it throws away any compensating surplus. It is not logically equivalent
to that more permissive condition. With signed deficits, the exact gate is

    limsup_T [-A mu5^c(T) + B mu6^c(T)] < J_* ,
    J_* = -A/36+B*(34/135)+M
        = 64788151489666079/572357731837500000
        = 0.1131952062247327... .                          (4)

A strict gap eta>0 in (4) implies consumer defect <=21/200-eta+o(1),
hence the inherited simple-zero coefficient is >=79/100+2eta-o(1).
An equality or a limsup merely <=J_* does not supply strict >79.
No separate fifth or sixth asymptotic is required by (4).

## 3. Gaussian versus target: exact moment-order decomposition

There are TWO distinct covariance-only objects in the archive.

1. The actual full Gaussian Loewner reference has
   W=diag(beta)+[diag(alpha),J], Cov(alpha_i,alpha_j)=delta_ij/4,
   Cov(alpha,beta)=0, Cov(beta_i,beta_j)=delta_ij/6
   -1_(i!=j)/(2pi^2(i-j)^2). Its sharp bulk moments are
   mu2=1/3, mu4=4/15, mu5=0, mu6=131/420.
2. The multiplication-only operator-valued semicircle ansatz with
   Kf(x)=integral |x-u|f(u)du has mu4=7/30 and mu6=29/140.
   It is NOT that full Gaussian reference. The previous falsifier concerns
   this second object. Do not substitute its sixth moment for the first.

The full Gaussian sixth value is a matrix Wick value, not 3var^3 or
15var^3 of a scalar Gaussian eigenvalue. A precise derivation is as follows.
Represent the Gaussian source as a circular spectral Gaussian measure of
intensity s ds multiplying the signed partial translations U_+s,U_-s.
Its alpha/beta covariance is exactly the covariance above (the derivative
projection is retained). Wick pairs each leaf with the opposite branch
of the same spectral variable. The normalized sharp trace of the closed
translation word is its single walk overlap. Consequently

    G6_sharp = sum_(15 matchings) integral_[−1,1]^3
                    O6(v_matching) |v| |w| |u| dv dw du.

The four chord-placement classes have multiplicities 5,6,3,1 and exact
integrals 3/70,1/90,1/180,1/70. Thus G6_sharp=131/420. These are
the exact three-pair integrals, with no connected arithmetic constants
inserted. The preserved exact_t222.py defines all four walks and their
breakpoint integrations; the historical compression audit records their
provenance. Matrix Gaussian Wick contractions justify their use for this
reference. The full field is not replaced by an iid diagonal model.
The single-compression step in this reference calculation is justified,
rather than assumed: the deterministic sharp-word reprojection bound is
uniform O_b(log d/d); each Wick pair measure has finite mass, so integrating
that bound over the finitely many pair patterns gives o_d(1). The same
argument does not extend to the nonexact arithmetic coefficient measure.

For the multiplication-only ansatz the independent recurrence is
M2=K1, M4=M2^2+K(M2),
M6=M2*M4+K(M2)*M2+K(M4); exact integration gives 29/140.
Its robust square is 215654545181/2064615000000. This smaller number
does not refute the frozen Gaussian obstruction: it belongs to a different
law and a different consumer, and the ansatz is already falsified at m4.

The target sharp centered model is

    mu2=1/3, mu3=0, mu4=1/4, mu5=1/36,
    mu6=131/420-23/420-1/126=157/630.

For the robust square the exact sharp comparison is

    E_G,sharp = 334737684433/2064615000000
              = 0.162130801351826...,
    E_target  = 35116876419/344102500000
              = 0.102053534685159...,
    E_G,sharp-E_target = 901159/15000000
                       = 0.060077266666666... .

| source of favorable gain | exact square reduction | decimal |
| --- | --- | --- |
| fifth connected target | A/36 = 11501/450000 | 0.0255577777778 |
| sixth {4,2} target | B*(23/420) = 452249/15000000 | 0.0301499333333 |
| sixth {6} target | B/126 = 19663/4500000 | 0.00436955555556 |
| orders 0,1,2,3 | same sharp lower moments | 0 |
| fourth | coefficient zero despite differing moments | 0 |

Before robust payments the required reduction from this sharp pair reference
is E_G,sharp-21/200=117953109433/2064615000000
(0.0571308013518259...). After e_band it is
1488798635828159/25438121415000000 (0.0585262807555539...);
after e_var it is exactly

    G_required,sharp = 66998281104243827/1144715463675000000
                     = 0.0585283271086006... .             (5)

The target's resulting conditional margin is M+B/378,
where B/378=19663/13500000. This explains the scale of the missing
non-Gaussian gain for THIS square. It is not an equality between the
new square gain and the old nonlinear Mehler response gain in (1).
Nor is E_G,sharp a lower bound on the new bounded Gaussian consumer:
p_dag<=P_dag^2 is an UPPER domination. A large Gaussian square value
shows this polynomial upper ledger lacks the required information; it
does not prove that E p_dag(I+W) itself exceeds 0.105. The permanent
all-radius obstruction concerns the previous frozen physical consumer.
Consequently the hypothesis that its failure is EXACTLY the missing
C5/C6 gain is not established by matching these moment differences.
If the full sharp target could be inserted with no extra fixed-R loss,
the paid margin would be 27704610381502/17886179119921875 and the conditional
simple-zero coefficient 56741962902005141/71544716479687500,
approximately 0.793097879116132. Neither number is an actual-prime theorem.

At fixed R_band the Gaussian value is instead

    E_G,R = c0+c2*G2_R+B*Pair6_R,
    G2_R = 1/6 + (1/pi^2) sum_(r=1)^R 1/r^2.              (6)

Pair6_R is the explicit filtered Wick integral in Section 7. Equation (6)
is exact; no numeric Pair6_6000 enclosure has been certified in this audit.
The displayed sharp decomposition is its R->infinity reference, not an
assertion that the finite-R Gaussian sixth equals 131/420. In particular
(5) must not be promoted as the measured finite-R Gaussian gain. The direct
arithmetic gate (12) does not need a finite-R Gaussian quadrature.

## 4. How much positive fifth mass / negative sixth mass is sufficient?

The exact geometric theorem is preserved:

    0<=C5(v)<=(s(v)-1)_+, s(v)=sum |v_j|/2,
    C5(v)=0 for s(v)<=1, on closed outer support.

The sharp positive model measure O5(v)C5(v)dv has mass 1/36. There is no
absolute-value loss for this GEOMETRIC measure. If an arithmetic theorem
transports a fraction f5 of that mass with all remaining terms controlled,
and the sixth model pair and {4,2} sectors are frozen, write

    mu5 >= f5/36,
    mu6 <= 131/420-23/420-f6/126.

Then the exact sufficient JOINT condition is

    (A/36)(1-f5)+(B/126)(2/3-f6) < M.                    (7)

Hence the weakest strict fifth fractions at the two specified sixth endpoints
are

    f6=2/3: f5 > 14575293823126261/14628191719695750
                   = 0.996383838988228...,
    f6=1:   f5 > 6870822093743843/7314095859847875
                   = 0.939394591676400... .

There is no absolute 'best sixth' without specifying its admissible lower
endpoint: a stronger actual sixth bound can buy more fifth loss. These two
numbers compare the requested relaxed ceiling and the frozen model value.
If f5=1, the weakest strict connected-sixth fraction is

    f6 > 1614401374707661/2500948906915725
       = 0.645515536220453... .                          (8)

The clean two-thirds sufficient target has a margin. With all {6} dropped,
even full model fifth mass fails this frozen cubic's paid ledger.
If pair or {4,2} differ, add B times their signed excess to (7), plus
any {3,3} or singleton contribution. Calling those sectors frozen MODEL
values does not prove their actual arithmetic specialization.

The usable geometric mass is positive, but a certified ARITHMETIC lower
bound on any positive fraction of it has not been obtained. Discarding
an arithmetic complement using geometric positivity is invalid without
the additional signed reduction in Sections 6–9.

## 5. Exact phase-response expansion and the cumulant dictionary

For the old bounded cylinder Phi_Rlag, use the actual real vector x_p(k)
whose complex pair at lag r is

    c_p exp(i(T+2pi k/L)log p)
       (exp(i2pi r s_p), i s_p exp(i2pi r s_p)), s_p=log p/L.

Group retained powers at the same base if they have not been disposed of
in a justified bounded-test norm. For any prime ordering set

    Y_p(k,g)=sum_(q preceding p)g_q+sum_(q following p)x_q(k),
    A1 = sum_p E_(k,g) D Phi(Y_p)[x_p(k)],
    A2 = (1/2)sum_p E_(k,g) D^2 Phi(Y_p):
                            (x_p(k)x_p(k)^t-Sigma_p).     (9)

Here g_p are independent centered matching Gaussians. For the old bounded
Phi, its uniform third derivative times grouped cube mass gives an
O_Rlag(L^-3) remainder. These are signed dependent-phase responses, not
errors now presumed negligible.

For the degree-six polynomial F(x)=tau q(M(x))^2, with M here the
CENTERED linear prime matrix, (9) with F substituted
is NOT by itself the complete identity. The exact finite Taylor telescope is

    E F(sum_p x_p)-E F(sum_p g_p)
      = sum_(m=1)^6 R_m,
    R_m = (1/m!) sum_p E_(k,g) D^m F(Y_p):
                          [x_p(k)^tensor m-E g_p^tensor m].       (10)

Derivative coordinates and all fixed-band matrix entries are linear in the
input. For F_b=tau M(x)^b, the explicit derivative is m! times the sum over
all ways to place m ordered input generators among b matrix slots, with
the other b-m slots occupied by M(Y_p); polarize if the directions differ.
Thus (10) is an exact noncommutative word expansion, not a scalar analogy.
For odd m the Gaussian tensor is zero; for even m it is the sum of
Gaussian pairings of Sigma_p. The unbounded derivatives of F prohibit
importing the bounded cylinder's uniform remainder envelope. The small
single-base cube mass needs actual weighted hybrid moments before it can
dispose of R_3,...,R_6 here.

A precise dictionary requires keeping TWO partitions distinct:

* Prime-base occurrences in the hybrid expansion: a word is assigned to
  its earliest replaced base p and its number m of current-base slots;
  previously replaced bases contract by Gaussian Wick pairing, later bases
  remain deterministic functions of the SAME root k. This is the exact
  assignment of that word to R_m. R_1,R_2 depend on the chosen base ordering.
* Empirical connected partitions of the leaf variables Z_j(k) along a
  closed band path: for each subset S define
  kappa(S)=sum_(partitions pi of S)(-1)^(|pi|-1)(|pi|-1)!
  product_(blocks C in pi) E_k product_(j in C) Z_j(k).
  The moment is exactly sum_pi product_C kappa(C).

To map (10) to connected sectors, expand its words, then use THIS second
moment-cumulant identity. This algorithm assigns every coefficient exactly.
There is no order-independent identification R_1=C5 or R_2=C6.

| degree / connected partition | exact count | placement in response expansion |
| --- | ---: | --- |
| 5: {5} | 1 | wordwise sum of R_m under cumulant inversion; candidate C5 only after arithmetic/model identification |
| 5: {3,2} | 10 | mixed connected triple and pair; not erased by scalar mu3=o(1) |
| 5: partitions with singleton | 41 | retained; scalar centering is not local empirical centering |
| 6: {6} | 1 | all six-leaf connected coefficients, potentially spread among R_m |
| 6: {4,2} | 15 | four-leaf connected coefficient contracted with one pair |
| 6: {2,2,2} | 15 | pair products; covariance-only Gaussian contributes here |
| 6: {3,3} | 10 | two connected triples; aggregate scalar third gate insufficient |
| 6: partitions with singleton | 162 | retained unless a same-convention local theorem removes them |
| proper powers / repeated bases | not a cumulant shape | may enter any row above; exact balanced nonpair closures negligible, nonexact weighted terms OPEN |

The names C5,C6 in the sharp Ursell position-walk ledger are not definitions
of these empirical cumulants. Their equality is a missing arithmetic theorem.
The historical finite compression audit already warned about this interface.

The new exact 2x2 noncommutative hybrid replay uses pairwise independent
signs x,y,xy solely as a hostile identity test. At degree five it gives
R1=65/4, R2=0, R3=353/54, total difference=2461/108. At degree six
R1=R2=0 but R4=-21431881/270000 and
R6=-18176884117/364500000, total=-47109923467/364500000.
It rejects the universal assertion that polynomial gain is exhausted by
the first two responses. This is not a prime counterexample. A proof of
negligible higher responses for the actual prime polynomial remains needed
if that particular comparison architecture is used. The direct theorem
(12) avoids requiring any such individual response theorem.

## 6. Actual resolved-prime formula and the one-sided theorem

Retain L=log(T/(2pi)), X=e^L=T/(2pi),
N=floor(X exp(-sqrt(L))), h=2pi/L, d=floor(TL/(2pi)),
c_n=-Lambda(n)/(a_phi L sqrt(n)), a_phi->1, including n=p^v.
Let I=[k_-,k_+] be the common good selected section, d'=|I|~d,
with its absolute Fourier indices retained. All limits fix R_band FIRST.

Use the row-entry convention, independently checked by the historical
prime path verifier:

    f0^+(s)=f0^-(s)=1-s,
    f_r^+(s)=(1-exp(2pi i r s))/(2pi i r), r!=0,
    f_r^-(s)=conjugate(f_r^+(s)).

For r_j in [-R,R] with sum r_j=0 set q0=0, q_j=sum_(a<=j)r_a and define

    Gamma_b,R(epsilon,s)
      = sum_(closed r paths) product_j f_(r_j)^(epsilon_j)(s_j)
                    exp(2pi i sum_j epsilon_j q_(j-1)s_j),
    lambda = sum_j epsilon_j log n_j = log(Aprod/Bprod),
    K_I(lambda)=exp(i(T+h k_-)lambda) D_d'(lambda/L),
    D_m(z)=m^-1 sum_(k=0)^(m-1)exp(2pi i k z).

This keeps every prime variable RESOLVED. Its exact finite sum is

    B_b,T,R = sum_(epsilon in {+,-}^b) sum_(n1,...,nb<=N)
                   [product_j c_(n_j)] Gamma_b,R(epsilon,s)
                   K_I(sum_j epsilon_j log n_j).           (11)

Gamma is the finite Fourier-path realization of the individually filtered
translation overlap. It is not a sharp overlap. The complete expression
is real by adjoint/reversal conjugation; take Re when separating subsets.
No polynomial of product length N^3 or N^4 has been formed in (11).

Define E_b,T,R as the same sum restricted to EXACT lambda=0, and
N_b,T,R=B_b,T,R-E_b,T,R. The letter N_b is a residual, not the cutoff N.
Unique factorization and the exact prime-base norm reduction prove

    E5=o(1), E6=Pair6_R+o(1).

Pair6_R is the following completely specified finite-feature integral:

    Pair6_R=sum_(15 perfect matchings pi) sum_(2^3 orientations)
             integral_[0,1]^3 Gamma_6,R(epsilon_pi,s_pi)
                                      product_(a=1)^3 s_a ds_a.

Each paired leaf uses the same s_a and opposite epsilon. This retains the
actual filter before PNT/BV testing. Coincident bases and exact proper-power
closures vanish by absolute prime-base bounds. Constants may depend on R.
The quarantine adds O_R(L^-1/2), a_phi normalization adds O_R(|a_phi-1|),
and full-measure PNT discrepancy adds O_R(L^-2), all o_T(1).

**Single sufficient signed near-product theorem, actual normalization:**

    At R=6000 and the retained natural cutoff, there exist eta>0
    and an admissible common good section for which

    limsup_(T->infinity) Re[-A N5,T,6000+B N6,T,6000]
          <= J_* - B Pair6_6000 - eta.                    (12)

Equivalently the favorable arithmetic gain

    G_arith,R(T)=A B5,T,R - B*(B6,T,R-Pair6_R)

must have liminf >=B Pair6_R-J_*+eta. The pair reference is only a
subtraction convention; the theorem requires a favorable nonzero correction,
not convergence to that reference. Together with A->B=o_T(1), (12) gives
(4). It directly absorbs finite-R geometry, without claiming C_R=D.

'Near-product theorem' here includes all nonexact residual terms, not just
a thin window already localized by proof. Far terms, all sign populations,
nonexact proper powers, repeated bases, near aliases, and selected-section
carrier phases are INCLUDED. One may later remove a class only with a
proved signed or summable bound. Exact nonzero aliases alone are o_T(1)
by the existing divisor-counting bound and may be removed without changing
(12). No estimate here proves the remaining residual is supported only
near zero or that its fifth restriction is nonnegative.

## 7. Resonance scale, aliases and the invalid positivity shortcut

Near sampled resonance the windows are

    |log(Aprod/Bprod)-mL| <= O(L/d') = O(1/T),
    m in Z, |m|<=b.

On the central m=0 cell this means product tolerance of order product/T,
not a fixed additive tolerance in an individual prime. Exact ordinary-prime
degree-five equality is impossible; leading positive fifth mass, if the
sharp model is correct, is necessarily NONEXACT. The sign populations
include 2-vs-3 and its conjugate, and at sixth degree 2-vs-4,4-vs-2,3-vs-3.
The smaller and same-sign populations remain in (12) because filtered words
can wrap. Exact nonzero aliases have lambda=mL and K_I=exp(iTmL).
Near aliases are OPEN at the natural cutoff.

There is an exact obstruction to discarding a complement based solely on
C5>=0: the sampled arithmetic kernel is signed, even in the central window.
For a section with k_-/d->0, d'h~T, and lambda=pi/(2T),

    Re K_I(lambda) -> integral_1^2 cos(pi v/2)dv = -2/pi.

Even without a carrier, Re D3(3/10)=(2-sqrt(5))/6<0. These are kernel
witnesses, not assertions that primes realize a given phase with a given
total weight. They falsify the universal nonnegative-integrand inference.
Also C5's sign theorem assumes sum v=0, while an off-diagonal arithmetic
tuple has sum v=lambda/L !=0. Projecting it onto a closed tuple and
controlling the residual is itself part of the missing reduction.

Thus the geometry localizes the TARGET positive measure to s>1. It does
not yet localize the entire arithmetic signed measure, justify dropping
its complement, or certify even the 93.94% subset required in Section 4.
An arithmetic positive-measure representation, or a separate signed
complement bound, is necessary before the proposed subset architecture
can be used. The theorem (12) preserves cancellations before absolute values.

The long-scale weighted Hilbert bounds are O_R(N^(5/2)/T) and
O_R(N^3/T), with logarithmic factors for the elementary discrete/alias
estimate; they do not vanish. The largest pooled lengths are N^3 in 2-vs-3,
N^4 in 2-vs-4 and N^3 in 3-vs-3. Repeated factors do not enlarge these
supports but their nonexact contribution is not disposed of by second mass.
No oscillation slogan supplies a mean-value theorem in this normalization.
N^3/T->0 remains permanently rejected: it forces the old B5 limit to zero
or changes dimension/background/prime measure, so it cannot retain this target.

## 8. Public arithmetic engine: variable-by-variable applicability

**PUBLIC CANDIDATE SOURCE — NOT ASSUMED CORRECT.**
JoshuaHKU/zeta-0.7947-reproduction at
d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8. Read the pinned paper's
s:trunc, s:local, s:four, p:prod, W1/W2/W3 and s:five:conn, the public
frame/local/Parseval/writeouts programs, and the local full-source packet's
provenance manifest.
The claimed percentage is not an input.

| public variable / ingredient | actual variable / obstruction | classification |
| --- | --- | --- |
| prime index m in window I_m, Lambda(m) | each resolved n_j, Lambda(n_j)/(a_phi L sqrt(n_j)) | ADAPTABLE weights via Abel summation only after a matched estimate |
| position lattice b_i*m | log n_j/L and Fourier lag path q_j | INCOMPATIBLE direct lattice identification; no additive integer grid for log primes supplied |
| affine lock j_t=n_(t+1)-a_t n_t | lambda=sum epsilon_j log n_j and near mL | MISSING PROOF: exact change of variables, Jacobian, multiplicity and consumption normalization |
| common additive shift t of chains | common height root k with carrier exp(i(T+hk)lambda) | INCOMPATIBLE as a direct symmetry; multiplicative ratios are not additive chain differences |
| p:prod finite autocorrelation identity | resolved finite correlations after a valid encoding | DIRECT finite algebra for the public additive object; ADAPTABLE methodology, no direct prime inequality |
| complete multidimensional Parseval | a specified joint analysis grid and its coupled spectrum | DIRECT finite algebra; MISSING PROOF that our arithmetic measure is that density |
| SW sum Lambda(m)e(b_i m beta), small rational denominator | sum c_n exp(it log n) with derivative/lag weights | INCOMPATIBLE direct theorem application; ADAPTABLE only through a proved weighted cell transform |
| Vaughan additive minor arcs | high-product log near-resonances and aliases | MISSING PROOF of relevant arc classification, minor mass and weighted signed saving |
| local residues d_t and coincidence count D(j) | multiplicative product-ratio condition | DIRECT residue identity for affine unit chains; INCOMPATIBLE as this log-product local law |
| CRT progression per lock coordinate | exp(iTmL), |lambda-mL|<=O(1/T) | MISSING PROOF: CRT does not control the archimedean carrier/alias |
| ell1 cell/modulus cutoff <=log^B X, tail ell1^(-k) | logarithmic n_j cells and their signed tuple masses | INCOMPATIBLE direct tail import; public modulus truncation is not a log-prime cell discretization |
| W2 unrestricted free-slot Fubini/PNT | a leaf still appearing in Gamma and K_I | INCOMPATIBLE removal while coupled; DIRECT only for a genuinely unrestricted already reduced factor |
| W3 disjoint pair chains | our exact opposite-prime pair contractions | ADAPTABLE; our exact pair PNT/BV theorem already closes this part; not a near-product gain theorem |
| W1 factor-by-factor resolved comb | our complete fifth/sixth signed sum (11) | MISSING PROOF of arithmetic/frame identity and consumed norm bound; not yet one missing local lemma |
| exact connected polytope volumes | sharp C5,{4,2},{6} target constants | DIRECT model geometry, not actual filtered-prime transport |

For clarity, the exact resolved Fourier identity can be written without
any prime theorem. On Z/M with unnormalized Fourier transforms set

    N_f(j2,...,jb)=sum_x f1(x) product_(i=2)^b fi(x+ji).

Then

    hat N_f(xi2,...,xib)=hat f1(-sum_(i=2)^b xi_i)
                                      product_(i=2)^b hat fi(xi_i),
    sum_j |N_f(j)|^2=M^(-(b-1)) sum_xi
                  |hat f1(-sum xi_i)|^2 product_(i=2)^b |hat fi(xi_i)|^2.

The first factor's frequency is COUPLED to the others. Equivalently
sum_j N_f(j)N_g(j)=sum_t product_i C_i(t), with the appropriate
conjugates in the complex version. Our new independent integer replay
checks both forms at b=5,6. They are identities for complete grids, not
an estimate that the product spectrum is close to a CRT comb. Minor-factor
supremum savings must still be integrated over the coupled grid with the
right consuming norm and every coefficient. The paper's factor-by-factor
paragraph does not give that bound for (11), even for its single signed target.

The public scripts' scope is also narrower than an analytic transfer:
face_local_closure enumerates finite affine residues; face_parseval checks
a one-coordinate FFT identity; b5/b6_frame compare selected finite
autocorrelation products with models at a 5% threshold.
writeouts_verification W1 checks one-coordinate Parseval and a CRT contrast
on a small 2D window, not a complete b-1-dimensional prime asymptotic.
W2b evaluates the same factored expression on both sides; W3 is a finite
product-of-twin-sums check. None consumes (11) or certifies a 9.24e-5 loss.

There is a quantitative cell obstruction to a casual transplant. Conditional
on all other primes, a central near-product window constrains one n by a
relative width O(1/T), hence absolute width O(n/T)<1 at our cutoff.
That is not the public theorem's Y~X^theta, theta>1/2, window. Averaging
all resolved variables might overcome this, but it requires a NEW theorem.
Linearizing log n across relative cells of width u incurs carrier phase
error O(Tu^2); taking it o(1) requires u=o(T^-1/2). Public logarithmic
modulus truncation does not prove these cell errors or their signed total
mass are small. Alternatively retaining exact logarithms requires a
Mellin-phase estimate, not an automatic additive Vaughan substitution.

Therefore decision C is not justified: there are multiple unmatched
interfaces before a single local lemma could finish a public transplant.
The unified direct theorem (12), not a claimed public application, is B.

## 9. Joint kernel, dual attempts and exact structural boundaries

The complete kernel is the disjoint union of degree-five and degree-six
resolved tuple spaces with weights -A and +B multiplying (11). Do not
identify the two spaces leaf-for-leaf without a marginalization theorem.
This explicit kernel preserves the Fourier closure, orientations and carrier.

An exact useful square completion is

    B X^6 - A X^5
      = B X^4 (X-310/371 I)^2 - (961/2500) X^4.          (13)

The original fourth coefficient remains zero: (13) is an identity, not a
license to import a new raw fourth-moment theorem. For an upper bound,
the positive degree-six square in (13) still requires control. It gives
no automatic favorable gain or uniform upper certificate.

The preserved C6 witnesses have outer overlap 1/5 and kernel values
+2/5 and -1/10. A universally negative pointwise Gram representation
of C6 is falsified. The previous quartic actual-semiprime audit also
falsifies the generic uniform full-product-space norm-times-mass rescue
at every fixed R; this result is not a counterexample to the actual
Lambda-weighted expectation. We do not promote it to a sixth-order
counterexample, but neither do we use that invalid norm inference here.

Covariance facts alone cannot bound this joint functional: a symmetric
scalar law of variance 1/3 supported at 0 and +/-M has fifth zero and
sixth M^4/3, unbounded as M increases. Thus no universal covariance-only
upper witness can prove (4). This rules out a universal completion/Gram
certificate derived solely from second mass. It does not rule out a
prime-specific signed dual or finite polyhedral certificate after a
source-closed reduction. LRSC exact weak dual/replay is ADAPTABLE only
after such a reduction supplies a finite domain and paid remainder.
No finite arithmetic dual witness satisfying (12) has been obtained.

## 10. Transport diagram and complete loss ledger

Keep the two radii distinct: only R_band=6000 occurs in this ledger.

    centered normalized zeta state -> A_b,T,R -> B_b,T,R -> C_b,R -> D_b
           source interface           CLOSED       OPEN      CLOSED as R->infinity
           inherited/conditional                          fixed-R loss not certified

A->B is CLOSED on the selected section with
rho_b=4bR K_R^b/d'=o_T(1), b=5,6. It is not raw-moment stability at
the original endpoints. Rank deletion of O(d/sqrt(L)) rows is safe for
the bounded consumer and costs o_T(1); raw moments are used only on the
selected section. C->D has a uniform continuum word convergence proof
as R->infinity once a complete finite-measure ledger is specified. It
does NOT give a useful fifth/sixth loss at R=6000. Filtering merged
translations and multiplying individually filtered translations are
different at fixed R; a candidate C must specify which it means.

The direct gate (12) is deliberately formulated BEFORE that ambiguity.
It closes the desired consumer if proved without needing C or its geometry
loss separately. This does not mark B->C CLOSED: the original full-moment
arrow remains OPEN and may be stronger than necessary.

| payment or residual | exact disposition in this route |
| --- | --- |
| full-to-band bounded functional charge | e_band=128952763/92407500000, paid once |
| variance lower-bound deficit | e_var=26060119/12734908593750, paid once |
| remaining joint tolerance | M in (2); require a strict eta gap |
| repeated filtered reprojection | A rho5+B rho6=o_T(1), fixed R; not a filter/sharp charge |
| principal-section deletion | bounded-consumer rank and normalization O(L^-1/2)=o_T(1); no raw-moment rank assertion |
| good endpoint neighborhoods | fixed 12R; their grouped linear-field bound gives K_R=O_R(1); no high-product feature norm assumed |
| pair-measure endpoint quarantine | O_R(L^-1/2), included in E6-Pair6_R=o_T(1) |
| exact pair PNT/BV | O_R(L^-2)+O_R(|a_phi-1|), after exact reduction |
| exact repeated-base/proper-power closures | o_T(1) by absolutely convergent valuation sums |
| exact nonzero aliases | o_T(1) from the existing exact-alias bound |
| nonexact ordinary, repeated-base, proper-power sectors | INCLUDED in N5,N6; no separate free o(1) claim |
| near aliases and nonlocalized far terms | INCLUDED in N5,N6; OPEN signed arithmetic contribution |
| fixed-R filtering / sharp replacement | no substitution in (12), no separate payment; if one goes through C,D this loss is OPEN and must fit the same budget |
| cell truncation, local density and minor arcs | no method yet satisfying hypotheses; any eventual residual must be paid inside (12), not waived |
| scalar/ramp centered-state interface and lower moments | inherited hypotheses in the exact consumer, not newly promoted by polynomial replay |
| zero-side block/tail-Weyl transfer | inherited corrected source normalization and bounded transfer, no new proof or independent percentage claimed |
| old Mehler initial / R_lag / localization | belong to (1), not paid again in this different consumer |

No complete numerical arithmetic loss allocation is presently possible:
the unknown signed residual is the required favorable gain itself.
An approach based on separate moment losses would need
A eps5+B eps6<M; the axis limits are
52897896569489/526614901909047000 and
52897896569489/315119562271381350. Crude continuum word bounds at R=6000
do not certify these. The half-interval g6000 witness is not a fifth/sixth
aggregate error and cannot be inserted as eps5 or eps6.

## 11. Remaining theorem, frontier and verification

The narrowest high-order arithmetic debt is (12), an upper bound on ONE
actual signed resolved-prime residual. No independent positive fifth mass
theorem, exact C6 convergence, full moment CLT, or finite-R sharp identification
is required by its direct form. All nonexact proper powers and aliases
remain explicit. The theorem could be proved by a prime-specific signed
cell method, a valid marginalization/dual, or another arithmetic estimate;
none has been supplied by the sources inspected here.

The method's structural validity is not established, so the user's
reoptimization trigger is not met. Parameters stay q above, pole 221/200,
R_band6000. No new radius, cutoff or raw moment debt is introduced.

If (12) closes with eta>0 under the frozen lower/analytic inputs, strict
>79 follows with coefficient 79/100+2eta. Reaching 11061/13891 is a
different task: it needs a consumer defect <=1415/13891 with its actual
finite-band and transfer payments, rather than merely <21/200. The exact
frontier cubic has a nonzero fourth coefficient and would require its
joint fourth/fifth/sixth information, or a different fully paid bounded
consumer. Sharp model constants alone do not supply that stronger theorem.

Verification:

    python src/wp84_non_gaussian_c5_c6_first_strike.py
    python src/wp84_non_gaussian_c5_c6_first_strike_replay.py
    python src/wp84_m4_free_robust_cubic_r6000.py
    python src/wp84_fixed_r_arithmetic_filtered_moment_transfer.py

The new verifier independently reconstructs the rational cubic, joint
margin and fraction thresholds; derives the multiplication-only sixth
moment; checks the full noncommutative finite Taylor telescope; enumerates
all connected-partition counts; preserves the C6 sign witnesses; and
checks complete resolved Parseval/product identities with exact integers.
The independent replay uses Fraction-only polynomial convolution and
checks all budget identities without importing the producer.

Reading/provenance: the eleven requested notes and their companion
verifiers were inspected, including the historical compression note and
verifier at c3f38619c4d1b534c58b91e990b5a44fd220e599 via git show.
The public pin and source packet remain unchanged. Cross-repository
method boundaries and immutable source pins are retained in
WP84_CROSS_REPOSITORY_SOURCE_MANIFEST.json and its transplant audit;
no claim to have freshly rerun all eight repository archives is made.
The certificate records source hashes and marks arithmetic_theorem_proved
and strict_gt79 FALSE. Earlier Gaussian certificates are preserved and
are not rerun to search for a winning Gaussian route.

No push, merge, rebase, amendment, visibility change, modification of main,
or modification of the Downloads checkout occurs. This is an additive
local audit with decision B, not a claimed unconditional theorem.
