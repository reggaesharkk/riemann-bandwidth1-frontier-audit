# Signed near-product cell decomposition: exact gates and uncovered region

Date: 2026-10-07. Parent: 40684faa2fc278d319b89df2550e82eb874ae0c7.
Branch: codex/c5-c6-attack-20261006. Additive local audit; no push.

**Decision D â€” CURRENT NUMBER-THEORY TECHNOLOGY AUDITED HERE DOES NOT COVER
A SPECIFIC CELL.** The interior 2-vs-3 cell in Section 10 has positive exact
fifth MODEL mass, product exponent about 6/5, and an oriented weighted product
correlation not covered by the hypotheses of the inspected results. This is
a bounded literature finding, not a proof that every conceivable method fails.
Multiple other supercritical, near-alias and long-product tail cells remain
open. No all-but-one-cell claim or optimized H is made.

New CLOSED reductions: proper powers can be removed from the bounded signed
theorem by Schatten/coercivity; exact nonzero aliases have an independent o(1)
bound in this normalization; support-empty and short-product cells close.
Power removal is a gate EQUIVALENCE, not smallness of every separately masked
power population. The frozen HS-square/common-lock/W2/carrier/Gaussian/master-PDE
routes are not reopened.

## 1. Target reconstructed independently; two separate budgets

Fix R=6000 and pole height eta_pole=221/200; reserve epsilon>0 for a strict
arithmetic gap. On the SAME principal section I=[k_-,k_+], d'=|I|,
mu_b^c=tau_I X_R,I^b, the target is

    A=11501/12500, B=137641/250000,
    limsup_T [-A mu5^c+B mu6^c] < J_*,
    J_*=64788151489666079/572357731837500000.              (1)

From a=(-19101/185500,961/3710,31/50,-371/500), independent convolution
c_b=sum_(r+s=b) a_r a_s gives

    c=(364848201/34410250000,-18356061/344102500,
       -26060119/430128125,21981971/46375000,0,-A,B).

Thus c4=0. Using the frozen SAME-section lower inputs mu1,mu3=o(1),
mu2>=1/3-2/(pi^2 R)+o(1), pi>333/106, and curvature bound 137721/5000:

    E_base=c0+c2/3,
    e_band=3*(137721/5000)*(106/333)^2/6000
          =128952763/92407500000,
    e_var=-2*c2*(106/333)^2/6000
         =26060119/12734908593750,
    J_*=21/200-E_base-e_band-e_var.

Separate paid MODEL allowances, both with mu5_model=1/36:

    Delta_ideal=27704610381502/17886179119921875
               =0.00154893955806605... (mu6_model=157/630),
    M_relaxed=52897896569489/572357731837500000
             =0.00009242103954753147... (mu6_relaxed=34/135). (2)

Their difference is 19663/13500000. Neither is a measured transport error.
Any finite-R model/geometry substitution consumes the SAME allowance; the
direct target (1) itself requires no sharp-model substitution. Source and
zero-side interfaces remain inherited, not newly proved by these replays.

Natural scale, unchanged:

    X_scale=exp(L)=T/(2pi), L=log(T/(2pi)),
    N=floor(exp(L-sqrt(L))), h=2pi/L,
    d=floor(T L/(2pi)), d'/d->1, tau0=T+h k_-, d'h/T->1,
    c_n=-Lambda(n)/(a_phi L sqrt(n)), n=p^v<=N, a_phi->1.

Good-endpoint neighborhoods have width 12R and O_R(1) LOCAL bounds.
No uniform bulk prime-matrix norm is assumed. This matters in Section 4.

## 2. Full finite-T resolved sum and exact alias partition

Row convention:

    s_n=log(n)/L,
    f_0^epsilon(s)=1-s,
    f_l^+(s)=(1-exp(2pi i l s))/(2pi i l), l!=0,
    f_l^-(s)=conj f_l^+(s).

A tuple alpha retains b=5 or 6, every p_j and v_j>=1, n_j=p_j^v_j<=N,
all epsilon_j, all |l_j|<=R with sum l_j=0, u0=0,
u_j=sum_(a<=j)l_a, section I and endpoint k_-. Define

    lambda=sum_j epsilon_j log n_j=log(P_+/P_-),
    w_alpha=omega_b product_j c_(n_j) f_(l_j)^epsilon_j(s_(n_j))
                 exp(2pi i sum_j epsilon_j u_(j-1) s_(n_j)),
    omega5=-A, omega6=B,
    S_T=sum_alpha w_alpha exp(i tau0 lambda_alpha)
                            D_d'(lambda_alpha/L),
    D_m(z)=m^-1 sum_(k=0..m-1)exp(2pi i k z).             (3)

All sums are finite. P_+,P_- are tuple product labels, not unrestricted
Dirichlet-polynomial coefficients. Sum paths to obtain Gamma_b,R only after
keeping these labels. Individual cells are complex; adjoint/reversal pairs
are conjugates, and their complete sum is real.

The actual repeated compression inserts every i+u_j in I and averages over
the resulting root interval. Passing to (3), with roots throughout I, uses
ONLY the previously CLOSED weighted boundary error
A rho5+B rho6=o(1), rho_b=4bR K_R^b/d'. It is not a raw-moment rank bound.

Set m=floor(lambda/L+1/2), xi=lambda-mL in [-L/2,L/2). For r positive and
s=b-r negative slots, the exact finite-T SUPPORT condition is

    r log2-s logN <= lambda <= r logN-s log2.            (4)

Intersect (4) with [(m-1/2)L,(m+1/2)L). Eventually all allowable nearest
bins are -s,...,r; these are support possibilities, not assertions of actual
prime resonances. For H/T=o(sqrt(L)), extreme -s,r cannot lie in a resonant
core. Empty sides also exclude central m=0.

|b|r:s|nearest bins|possible resonance cores|
|---|---|---|---|
|5|0:5|-5,...,0|-4,-3,-2,-1|
|5|1:4|-4,...,1|-3,-2,-1,0|
|5|2:3|-3,...,2|-2,-1,0,1|
|5|3:2|-2,...,3|-1,0,1,2|
|5|4:1|-1,...,4|0,1,2,3|
|5|5:0|0,...,5|1,2,3,4|
|6|0:6|-6,...,0|-5,-4,-3,-2,-1|
|6|1:5|-5,...,1|-4,-3,-2,-1,0|
|6|2:4|-4,...,2|-3,-2,-1,0,1|
|6|3:3|-3,...,3|-2,-1,0,1,2|
|6|4:2|-2,...,4|-1,0,1,2,3|
|6|5:1|-1,...,5|0,1,2,3,4|
|6|6:0|0,...,6|1,2,3,4,5|

For symbolic 0<H<=Lambda<=TL/2, partition every tuple into CENTRAL
m=0, |xi|<=H/T; ALIAS m!=0, |xi|<=H/T; TRANSITION every m with
H/T<|xi|<=Lambda/T; FAR every m with |xi|>Lambda/T. Separate exact xi=0
again. Since k_- is integer,

    exp(i tau0 lambda)D_d'(lambda/L)
       =exp(i T mL) exp(i tau0 xi)D_d'(xi/L).            (5)

Only D is periodic; the complete carrier-bearing kernel is not.

## 3. Exact kernel bounds; mean values before coefficient L1 mass

For 0<|xi|<=L/2,

    |D_d'(xi/L)|=|sin(pi d'xi/L)|/[d'|sin(pi xi/L)|]
       <=min(1,1/[d'|sin(pi xi/L)|])
       <=min(1,L/[2d'|xi|]).                            (6)

Square the envelope for a pointwise L2 bound. Complete-period Parseval gives

    (1/L) integral_(-L/2)^(L/2)|D_d'(xi/L)|^2 dxi=1/d',
    (1/L) integral_(|xi|>H/T)|D_d'(xi/L)|^2 dxi
       <=L/(2d'^2)*(T/H-2/L)<=LT/(2d'^2 H).             (7)

The uniform-frequency relative tail is at most LT/(2d'H)~pi/H. Our prime
measure is atomic and weighted, so (7) is not automatically its mean square.
For K(x)=exp(i tau0 x)D_d'(x/L),

    |K'(x)|<=tau_bar=tau0+h(d'-1)/2~3T/2.              (8)

This exact bound is used in Abel summation. FAR pointwise decay ~pi/Lambda
does not bound the total long-product prime sum: unsigned coefficient mass
can grow like N^(b/2) times logarithms and fixed-R constants.

Auxiliary grouping of equal products, solely to test estimates, has bounded
j-fold coefficient second mass for fixed j<=6 and bounded lag factors.
Weighted Montgomeryâ€“Vaughan gives sqrt(UV)/T for product supports U,V.
Discrete absolute harmonic-row bounds, with ALL alias bins accounted for,
give nonexact cell error

    O_(R,b)((1+L)^C [sqrt(UV)/T+X_scale^-1/2]).          (9)

Near central equality use 1/|log(u/v)|<=C sqrt(uv)/|u-v| and harmonic
integer row sums. Near alias X^m use nearest integers and harmonic tails
around X^m v. Exact central equalities are treated separately. Absolute
row bounds also cover restrictions to FAR/TRANSITION. Thus cells with
log U/L+log V/L<2 by a fixed amount close. Generic Hilbert, large-sieve or
mean-square norms do not give o(1) beyond this length region. Sparse mean
values replace the error with SHORT-SHIFT PRODUCT COUNTS, not a proof of
those counts. No absolute prime L1 payment is inferred from (7).

## 4. Proper powers first: a CLOSED signed-gate removal theorem

For j>=2 the exact coefficient higher mass is

    M_j^pow(N)=1/(|a_phi|^j L^j)
       sum_p (log p)^j sum_(2<=v<=logN/logp) p^(-vj/2)
       <=1/(|a_phi|^j L^j)
          sum_p (log p)^j p^-j/(1-p^(-j/2))=O_j(L^-j).  (10)

Each displayed series is absolutely convergent, including j=2. For j=1,
the p^2 piece gives M_1^pow->1/2 by PNT partial summation, and v>=3 is
O(1/L). Therefore proper-power absolute FIRST mass is not o(1). Grouped
product second mass with a proper label is O_j(L^-2); generic high-product
Hilbert error N^(b/2)/(TL) still grows. It cannot justify raw deletion.

Instead write X=Y+P on the SAME section, Y ordinary and P proper-power.
Since the band is fixed,

    ||P||_op<=2 M_1^pow(1+2 H_R/pi)=O_R(1), H_R=sum_(l<=R)1/l.

Sobolev sampling and Montgomeryâ€“Vaughan for LINEAR proper-power fields of
length N, on the actual interval of length d'h~T, give average squared
field <=C(1+N/T) M_2^pow=O(L^-2). The derivative costs at most L,
hL=2pi; finitely many row shifts enlarge the interval only by O_R(h).
Summing squared band entries yields

    ||P||_2,tau^2=||P||_HS^2/d'=O_R(L^-2),
    ||P||_6,tau^6<=||P||_op^4 ||P||_2,tau^2=O_R(L^-2),
    p_T=||P||_6,tau=O_R(L^-1/3).                       (11)

No uniform ordinary-prime bulk norm has been assumed. For Hermitian Z,
y=||Z||_6,tau and F(Z)=-A tau Z^5+B tau Z^6 satisfy

    F(Z)>=B y^6-A y^5;
    y>=2A/B implies F(Z)>=B y^6/2.

A finite upper bound on the SIGNED gate itself forces bounded y. Expanding
noncommutative words and applying normalized Schatten Holder gives, b=5,6,

    |tau X^b-tau Y^b|<=(y+p_T)^b-y^b                  (12)

if y=||Y||_6,tau is bounded, and conversely with ||X||_6,tau. Thus any
candidate ordinary-prime proof limsup F(Y)<J_* supplies exactly the bound
needed for F(X)-F(Y)=O_R(L^-1/3)=o(1). The reverse implication also holds.
If one signed limsup is +infinity, the other cannot be finite by this
reverse argument. The finite strict signed gates are EQUIVALENT.

CLOSED: proper-power gate removal, limiting loss ZERO in both budgets.
Not claimed: unconditional o(1) of every separately masked power sector.
Removal is made on the complete signed functional BEFORE the ordinary
alias/cell partition. Masking first would invalidate the word-norm argument.
This avoids adding an independent high-moment hypothesis or offending
power-pattern debt to the sufficient ordinary-prime theorem.

## 5. Exact nonzero aliases independently reproved

For exact m!=0, P_+/P_-=X_scale^m. If X^m is irrational there are no such
integer products. (Irrational X alone does not exclude rational powers.)
Otherwise write X^|m|=a/b in lowest terms, a>=b, exchange sides for m<0.
Exact pairs are P_+=a k, P_-=b k in support. Ordered fixed-degree prime
multiplicities are bounded; the looser C_b(1+L)^b bound even allows powers.
With |Lambda(n)/(a_phi L)| bounded and |f_l|<=1, summing each fixed path gives

    C_(b,R)(1+L)^b/sqrt(ab) sum_(k<=N^b)1/k
       <=C_(b,R)(1+L)^(b+1) X_scale^(-|m|/2).           (13)

Use sqrt(ab)>=sqrt(a/b); empty sides restrict k further. Sum finitely many
paths/signs and |m|<=6: O_R((1+L)^7 X_scale^-1/2)=o(1), with consumer
coefficients included. Carrier modulus is one, not presumed cancelled.
This is uniform at heights tuned to exact arithmetic aliases. CLOSED in
both ledgers. Near aliases lack the divisibility restriction and retain
the growing sqrt(UV)/T term in (9); they remain open outside short cells.

## 6. Central log cells, exact interval interpretation and coverage polytope

Partition each log p_j/L into rational intervals [a_j,b_j], intersected
with [log2/L,logN/L]. Put u=sum_+ alpha_j, v=sum_- alpha_j,
U=X_scale^(sum_+ b_j), V=X_scale^(sum_- b_j). The exact central H-polytope is

    log2/L<=alpha_j<=logN/L, |u-v|<=H/(TL).              (14)

For aliases use |u-v-m|<=H/(TL). The CSV contains ALL 9,216 quarter-log
boxes for canonical 2:3, 2:4, 3:3 sectors, with explicit support, short-length
and uncontrolled/boundary flags. Other orders have the same support, not
interchangeable filtered signs. Boundary boxes require subdivision.

For central gamma=u=v<1 by a fixed amount and H=X_scale^o(1), integer
separation gives no nonexact tuples. Ordinary prime-vs-many central sectors
also vanish when H=o(e^sqrt(L)): HN/T->0 makes the final integer window
shorter than one, and unique factorization excludes exact prime equality.
Thus central ordinary sectors left are 2:3/conjugate, 2:4/conjugate, 3:3,
including nonexact repeated-label populations. Their UNCOVERED regions for
the audited estimates are

    0<alpha_i<1 (intersect actual cutoff 1-1/sqrt(L)),
    sum_+ alpha=sum_- alpha=gamma>=1,
    (r,s)=(2,3),(2,4),(3,3).                           (15)

Nonzero-alias uncovered polytopes have u-v=m and u+v>=2. This is a coverage
boundary, not a claim that all signed tuples there are dangerous.

For a fixed P_+=a, |log(a/P_-)|<=H/T is EXACTLY

    a e^(-H/T)<=P_-<=a e^(H/T).                        (16)

The asymmetric additive widths are a(1-e^-H/T) and a(e^H/T-1). Symmetric
|P_--a|<=a(e^H/T-1) is an OUTER envelope, not equivalence. At balanced
product exponent gamma, width ~H X_scale^(gamma-1)/(2pi). The negative
product is triple prime in 2:3, semiprime in 3:2, four-prime in 2:4,
semiprime in 4:2, and triple prime in 3:3. Freezing all other labels instead
leaves a FINAL-PRIME interval of size O(H p/T)<1 under H=o(e^sqrt(L)).
Do not confuse the product-variable interval with a long single-prime window.

## 7. Joint cell functional, sign and local completion/duality tests

A joint cell is an explicit TAGGED union of degree-five and degree-six tuple
spaces assigned a common balance/alias region, not a leafwise identification:

    J_cell=Re[-A Fifth_cell+B Sixth_cell].               (17)

Pair conjugate reversal/orientation cells, separate exact sixth pairs, and
assemble Gamma/path coefficients BEFORE absolute values. Support-empty cells
are harmless; (9) closes short cells. No generic favorable arithmetic cell
sign follows from the C5 continuum sign. All-zero-lag consumer weights are
positive for BOTH degrees, while their carrier changes sign. Their full
Gamma cancellations must be proved; they cannot be ignored or presumed.

If resolved two-label and three-label arrays could be matched, the local
quadratic B||v||^2-A Re<u,v> has matrix [[0,-A/2],[-A/2,B]], determinant
-A^2/4<0. Completion gives

    B||v-A/(2B)u||^2-A^2/(4B)||u||^2.                  (18)

It supplies a LOWER bound, not the needed upper bound. Optimized CS bounds
the cross term absolutely and loses favorable gain; an upper bound still
requires positive-square mass. Schur/negative-Gram upper certificates fail
for the unrestricted form. The 2:4 array adds a different unresolved object.

Central hard restriction itself need not preserve PSD: frequencies 0,a,2a
with H/(2T)<a<H/T have difference-window matrix
[[1,1,0],[1,1,1],[0,1,1]], determinant -1. PSD of an unmasked sampled
correlation does not prove PSD after a hard near-product mask. No LRSC weak
dual or semidefinite cell upper certificate is obtained without valid mass
and remainder bounds. This does not exclude a constrained prime-specific dual.

## 8. Oriented summation by parts and explicit counting-error norm

The requested radial count sum_(0<|lambda|<=x) signed_weight is generally
INSUFFICIENT: weights are complex and K(-x)=conj K(x). Weights i at +x
and -i at -x have radial sum 0 but contribution -2 Im K(x),
already -2 sin(tau x) for a single sampled phase. Keep orientations.
For each cell, alias m and sigma=+/- set

    C_(m,+)(x)=sum_(0<xi<=x)w_alpha e^(i T mL),
    C_(m,-)(x)=sum_(0<-xi<=x)w_alpha e^(i T mL),
    K_+(x)=K(x), K_-(x)=K(-x).

These are finite complex step functions; exact xi=0 is separate. For 0<=a<b:

    sum_(a<sigma xi<=b) w_alpha e^(iTmL)K_sigma(|xi|)
      =C_sigma(b)K_sigma(b)-C_sigma(a)K_sigma(a)
          -integral_a^b C_sigma(x)K_sigma'(x)dx.        (19)

This is the concrete WEIGHTED almost-prime counting formulation. If a proved
model cumulative M_sigma is available and |C_sigma-M_sigma|<=E_sigma(x),
a sufficient transport loss is

    E_sigma(b)|K_sigma(b)|+E_sigma(a)|K_sigma(a)|
                       +integral_a^b E_sigma(x)|K_sigma'(x)|dx. (20)

A uniform epsilon_cell error on (0,H/T] bounds one branch by
epsilon_cell(1+tau_bar H/T). Sum branches/cells before comparing with (2).
The weighted norm (20) is weaker than this sufficient uniform bound. There
is no unique weakest pointwise bound: signed Abel cancellations can allow
large cumulative functions. No paid model cumulative has been identified
for the first cell. An unsigned existence theorem does not supply (19).

Illustrative RESERVED half-budget allocations, if all other cells had proofs:

    delta_cell,ideal=13852305190751/17886179119921875,
    delta_cell,relaxed=52897896569489/1144715463675000000. (21)

With two branches and uniform epsilon require
2 epsilon(1+tau_bar H/T)<delta_cell. These are explicit required constants,
not a certified allocation to the other open sectors. Spending a full global
allowance independently on every cell would double count it.

## 9. Type I/II/III and literature hypothesis audit

Only primary texts were used; this is not a proof of absence of other methods.

[Montgomeryâ€“Vaughan, Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf):
finite L2 coefficients, log frequencies, averaging interval T; length loss
sqrt(UV)/T. Actual sampling requires aliases. Quantitative cell loss: (9),
covered region u_high+v_high<2. No exceptional set. Long interior cells fail
this vanishing-error conclusion from coefficient norms alone.

[Matomakiâ€“Teravainen, Almost primes in almost all short intervals II,
Theorems 1.1/2.1, Proposition 2.2, Lemmas 3.2â€“3.4](https://arxiv.org/html/2207.05038):
E2 fixes a prime near (log z)^1.1; centers average over [z,2z], exceptional
count O(z/log^delta z). The minorant variance uses h=(log z)^2.1,
h1=z^.99 and L2 error O(log^(-2-epsilon)z). Type II uses a factor at most
z^(2/11); sparse estimates have additional support hypotheses. Our balanced
semiprime primes have fractions about 1/2 of log z, not a polylog factor,
and centers are weighted prime products. No matching error for (20) follows.
Its improved mean-value lemma leaves exactly the short-shift correlations
that need proof here; the theorem cannot be cited to assume them.

[Teravainen, Almost primes in almost all short intervals,
Theorems 4/5 and Proposition 4](https://arxiv.org/pdf/1510.06005):
normalized interval comparisons impose prescribed iterated-log/logarithmic
small prime factors and almost-all integer centers. Our interior 0.4/0.6
factors violate those ranges. Exceptional counts are not weighted bounds on
our centers. E3/E4 existence is weaker than a complex filtered correlation.
No applicable quantitative loss is supplied for this cell.

[Matomakiâ€“Radziwill, Multiplicative functions in short intervals II](https://arxiv.org/html/2007.04290):
mean/exceptional-set results concern multiplicative functions with specified
bounded/non-vanishing hypotheses. Our fixed prime-factor-count windows and
resolved path filter are not a single such multiplicative function of the
product. Methodology is adaptable after a proved reduction and weighted
exceptional-set control, neither currently available here.

[Polymath, New equidistribution estimates of Zhang type,
Theorems 2.8/2.9/7.1](https://arxiv.org/pdf/1402.0811):
Type I/II/III progression discrepancies are averaged over smooth/densely
divisible moduli. Type III uses smooth factors and prescribed length ranges.
Our prime-product interval centers, path coefficients and averaging measure
do not provide this progression reduction. Prime-restricted factors are not
the theorem's smooth factors. No exponent overlay is certified from it.

Vaughan/Heath-Brown identities alone are decompositions, not estimates.
A usable decomposition must preserve coefficient ranges, smoothness, path
phases and boundary errors. No source-closed matching Type I/II/III upper
estimate is established here. Large sieve/Halaszâ€“Montgomery/large-value
methods need actual separation, sparsity or large-value hypotheses, not
just the phrase almost-prime. The coverage overlay therefore contains the
proved short-product half-space, small-factor theorem hypotheses disjoint
from the first interior cell, and unmatched progression/smoothness regions.
It does not invent broad Type III coverage.

Trace averaging is already fully used in D_d': heights are approximately
[T,2T], not uniform independent product centers P_+. Pulling an almost-all
integer-center theorem back to our sparse weighted centers requires their
exceptional-set weight or an appropriate weighted L2 discrepancy. Similarly,
almost-all trace-position bounds require control of the high-degree sum on
exceptional positions. Lower second mass and good BOUNDARY endpoints do not
supply a bulk high-moment tail bound. A suitably weighted averaged theorem
would suffice; pointwise estimates for every tuple are not intrinsically
required. No second factor d' may be claimed after D_d' has been formed.

## 10. Exact C5 mass, sixth triage and first uncontrolled cell

C5 model mass is ZERO for gamma=sum positive alpha<=1. Hence the closed
short-product region has exact model mass 0, and the supercritical complement
has 1/36. Polylog-small-prime faces have alpha_i=0 and zero Lebesgue model
mass; directly matched model mass from the audited interval theorems is 0.
They do not supply either required fifth fraction.

An exact POSITIVE interior cell integral is computed, not sampled. Put

    x=(603/1000,-397/1000,598/1000,-406/1000),
    v5=-sum x=-398/1000, delta=49/1500,
    Q={v1..v4: |v_i-x_i|<=delta}.

All 45 breakpoint hyperplanes have distance greater than their coefficient
L1 norm times delta. Thus O5,C5 are affine throughout Q:

    C5(x)=201/1000, grad C5=(1,0,1,0),
    O5(x)=49/250, grad O5=(-1,-1,-1,0).
    m5,Q=(2delta)^4[C5(x)O5(x)+delta^2 gradC5 dot gradO5/3]
        =1505310601921/2135742187500000000>0.            (22)

Its fraction of total mass is 1505310601921/59326171875000000, far below
the required fractions. Exact COARSE distribution: subcritical 0; Q mass
(22); remaining supercritical 1/36-m5,Q. Finer quarter-box masses have exact
polytope-integral definitions but are NOT individually evaluated here. The
CSV is a coverage map, not a fabricated numerical mass table.

Required fifth fractions are exactly
6870822093743843/7314095859847875 (model sixth), and
14575293823126261/14628191719695750 (relaxed sixth). Arithmetic fifth
fraction certified by this run: ZERO. Positive model mass cannot justify
discarding an arithmetic complement without a sign/transport theorem.

Sixth exact opposite-prime pairs close at the ACTUAL filtered Pair6_6000,
with PNT/BV after unique factorization. Sharp sector model totals remain
131/420, -23/420, -1/126; none replaces a fixed-R arithmetic sector here.
{4,2}/{6} arithmetic cell identification and favorable fractions are OPEN.
With full fifth and the {4,2} correction available, the needed fraction of
the {6} correction is 1614401374707661/2500948906915725. This is not a
fraction of the entire connected sixth correction. Only a one-sided upper
bound is necessary; no new bound reaches that fraction. Per-cell C6 numerical
mass is not claimed with an unproved arithmetic/model dictionary.

FIRST UNCONTROLLED CELL: ordinary pairwise-distinct primes, signs
(+,-,+,-,-), with alpha_j=log p_j/L in

    I1=[1711/3000,1907/3000], I2=[1093/3000,1289/3000],
    I3=[848/1500,946/1500], I4=[560/1500,658/1500],
    I5=[401/1500,793/1500], p_j<=N.                    (23)

P_+=p1 p3, P_-=p2 p4 p5, 0<|log(P_+/P_-)|<=H/T.
I5 contains every fifth coordinate forced by exact closure of the first four;
the tiny finite-T O(H/(TL)) boundary correction must be retained. Balanced
gamma is in [3407/3000,3799/3000], strictly >1. The product interval has
width about H X_scale^(gamma-1)/(2pi), while fixing other factors leaves
sub-unit final-prime windows. This is a weighted semiprime/triple-prime
short-interval correlation at PRIME-PRODUCT centers.

Exact dyadic ranges are (2^j_i,2^(j_i+1)] contained in
[X_scale^a_i,X_scale^b_i] from (23), plus partial end boxes for full coverage.
The explicit interior family j1,j3=floor((3/5)log2 X_scale),
j2,j4,j5=floor((2/5)log2 X_scale) is contained for large T.

Every path weight, including the consumer coefficient, is

    w5=A/(a_phi^5 L^5 sqrt(p1 p2 p3 p4 p5))
          product_j log p_j f_(l_j)^epsilon_j(alpha_j)
          exp(2pi i sum_j epsilon_j u_(j-1)alpha_j),
    sum l_j=0, |l_j|<=6000,

multiplied by exp(i tau0 lambda)D_d'(lambda/L). This sign includes the
five negative c_p and the negative fifth consumer. No sharp C5 substitutes.

For a JOINT test tag this with degree-six 3:3 cells alpha_i in [1/3,1/2],
balanced gamma in [3407/3000,3799/3000], excluding exact lambda=0 tuples.
Their weights are B times the full six-edge coefficient/filter product.
All assigned orientations/orderings are kept; remaining 2:4/repeated-label/
other 3:3 cells stay outside explicitly. The exact required one-sided
counting theorem, with h=H/T, is

    Re sum_(sigma=+/-)[E_sigma(h)K_sigma(h)
                       -integral_0^h E_sigma(x)K_sigma'(x)dx]
        <=delta_cell,                                  (24)

where E_sigma=C_joint,sigma-M_joint,sigma and C is EXACTLY the above signed
resolved fifth plus assigned sixth weights. M must first have a proved paid
arithmetic/filter identification; geometric positivity supplies no M.
Equivalently Re J_cell<=Re J_cell,model+delta_cell. Without a model, retain
the exact C formula and compare its total with the remaining global cap (1).
The illustrative allowances are the exact half-budgets (21), the full global
allowances (2). Neither is a feasible allocated ledger yet: other long cells
remain unbounded and model identification is unpaid. (24) is the FIRST
explicit uncovered cell theorem, not the ONLY remaining theorem.

## 11. Local public candidates, Fejer and optimization gate

Only uncovered cells are tested against the public candidate pin
JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8,
NOT ASSUMED CORRECT. Finite resolved transforms are DIRECT; partial summation
and log-cell organization ADAPTABLE; required affine prime-lock equations
and CRT densities MISMATCH; W1/MM/minor quantitative transfer INSUFFICIENT.
W3 gives no new distinct-prime near-product estimate beyond exact pairs.
W2/global common-lock remain frozen, not retested. Restricting a logarithmic
cell does not create an additive prime lattice or independent free slots.

Fejer: |D_d'(z)|^2=d'^-1 F_d'(z) exactly. Near its zeros |D|/|D|^2 is
unbounded, so a fixed Fejer multiple alone cannot dominate arbitrary signed
K contributions. |D|<=epsilon+|D|^2/(4epsilon) is valid, but epsilon times
absolute coefficient mass can grow. Real-kernel pointwise majorants preserve
order only against positive measures, not arbitrary complex cell weights.
Short Fourier/Beurlingâ€“Selberg approximations need a norm against our ATOMIC
measure and paid resolved correlations; uniform Lebesgue L2 error is not
enough. The full carrier has frequencies ~T and central width H/T.
No majorant with a total certified loss below (2) is obtained; D is never
replaced by |D| in the target.

H stays symbolic with H<=Lambda<=TL/2, and H=o(e^sqrt(L)) for the stated
single-prime support elimination. Pointwise tail improves like 1/H, but no
long-product measure tail bound closes. There is therefore NO proved objective
function to optimize. No theorem-optimal H is claimed. H=1,4 below are
numerical diagnostics chosen only after the symbolic estimates were derived.

## 12. Reconnaissance, complete ledger and verification

Deterministic numerical recon uses T=100000,1000000,10000000, a_phi=1 explicitly as a
diagnostic, R=6000, distinct ordinary primes in exact dyadic 0.6/0.4 windows,
and a specified candidate section inside the endpoint quarantine windows.
The candidate is NOT theorem-certified as a good section. Complete zero-lag
subterms are enumerated without losing prime labels. Full finite-R Gamma is
computed by displacement convolution for the first eight resolved tuples per
sector, explicitly PARTIAL unless the tuple count is <=8. The JSON records
inputs, all sampled labels, phases, signs, counts and Gamma values. No finite
observation is promoted to an asymptotic theorem or rigorous error bound.
At the first two heights both distinct nonexact diagnostic cells are empty.
At T=10^7 the fifth/sixth tuple counts are 756/504 for H=1 and 5868/2520
for H=4. The complete fifth zero-lag sum changes from +6.989582008e-9
to -1.545120080e-8; full-R eight-tuple sums remain partial. These are finite
sign/scale diagnostics, not estimates of the whole arithmetic remainder.

|loss|ideal ledger|conservative ledger|status|
|---|---|---|---|
|proper-power signed-gate removal|0 limiting|0 limiting|CLOSED O_R(L^-1/3) once either gate bounded|
|exact nonzero aliases|0 limiting|0 limiting|CLOSED (13)|
|bounded principal deletion / weighted reprojection|o(1)|o(1)|inherited, separated|
|exact sixth pair PNT/BV|o(1)|o(1)|CLOSED reduced filtered sector|
|near aliases|no certified finite total|same|OPEN long cells|
|FAR|no certified finite total|same|OPEN except short cells|
|TRANSITION|no certified finite total|same|OPEN except short cells|
|covered/support-empty cells|0 limiting|0 limiting|CLOSED (9)/(14)|
|global uncontrolled-cell allowance|Delta_ideal in (2)|M_relaxed in (2)|available after ALL other costs|
|model/filter geometry remainder|not certified|not certified|must fit same allowance if model used|
|band charge|e_band|e_band|already paid once|
|variance charge|e_var|e_var|already paid once in sufficient signed envelope|

Ideal is numerically less restrictive; neither ledger is established as
reachable by inspected arithmetic estimates. Unknown signed residuals are
not assigned zero merely because they oscillate. After the proper-power
gate reduction, the accepted global remaining theorem is

    limsup_T Re[-A N5,T,6000+B N6,T,6000]
       <=J_*-B Pair6_6000-epsilon, some epsilon>0,       (25)

N_b the resolved nonexact ordinary residual including EVERY uncovered alias,
transition, far, repeated-label and central population. Exact fifth closures
vanish; exact sixth closures give Pair6_R. If proved with inherited inputs,
(25) gives strict >79. This run proves no such inequality.

Run:

    python src/wp84_signed_near_product_cell_decomposition.py --write
    python src/wp84_signed_near_product_cell_recon.py --write

Exact gates reconstruct the budget, all sign-pattern alias supports, 9,216
coverage rows, the rational positive model-box integral, all 45 wall/corner
checks, complex oriented Abel identity, coercivity identity and hostile Gram
determinants. The preserved exact 150-term C5 kernel is imported. Certificate
flags strict_gt79/arithmetic_theorem_proved remain FALSE. Recon is separately
labelled numerical only. Existing commits and notebooklm_packet are preserved;
main and Downloads are unchanged, and no push occurs.

## 13. Continuation: carrier-bearing oriented primitive (authoritative refinement)

The interrupted files above were preserved and rerun. The following refinements
supersede any interpretation of (25) as a single-cell closure claim. Decision D
means that the inspected published hypotheses do not supply the required
factor-restricted weighted correlation; it is not a nonexistence theorem about
all possible number-theory methods.

For each resolved sector define

    nu_T = sum_alpha w_alpha exp(i tau0 lambda_alpha) delta_lambda_alpha,
    N_T(x) = nu_T((-infinity,x]),
    S_T = integral D_d'(lambda/L) d nu_T(lambda).

This is a COMPLEX oriented measure. The carrier is part of the count, not an
unsigned multiplicity. Positive and negative lambda remain distinct. On an
alias bin m use xi=lambda-mL, multiply the primitive weights by exp(i tau0 mL),
and retain exp(i tau0 xi). Since tau0=T+2pi k_minus/L, the alias constant is
exp(i T mL). The periodic D kernel is D_d'(xi/L).

For either oriented branch let E(x) be the difference between its local
carrier-bearing primitive and an explicitly specified comparison primitive.
With a<x<=b, Abel gives exactly

    residual = D(b/L)E(b)-D(a/L)E(a)
                 - integral_a^b E(x) (d/dx)D(x/L) dx.                 (26)

The negative branch uses xi=-x and the corresponding derivative. Atoms on
boundaries are assigned consistently to (a,b]; exact xi=0 atoms are separate.
Thus a sufficient absolute loss is

    |D(b/L)E(b)|+|D(a/L)E(a)|+integral_a^b |E(x)| |D'(x/L)/L| dx.    (27)

Here D' in the last expression denotes the derivative of D in its own
argument, not the section length d'. For 0<x<=L/2,

    |D(x/L)| <= min(1,L/(2d' x)),
    |(d/dx)D(x/L)| <= min(pi(d'-1)/L,
                                  pi/x+pi L/(4d' x^2)).            (28)

The second bound follows by differentiating
exp(i pi(d'-1)x/L) sin(pi d' x/L)/(d' sin(pi x/L)); use
sin(pi x/L)>=2x/L. Consequently a uniform primitive error epsilon on [a,b]
costs at most

 epsilon*[min(1,L/(2d'a))+min(1,L/(2d'b))
          +min(pi(d'-1)(b-a)/L,
               pi log(b/a)+pi L(1/a-1/b)/(4d'))].                   (29)

At a=0 use the global derivative bound and one endpoint: epsilon times
[1+pi(d'-1)b/L], with E(0)=0. These are quantitative sufficient conditions,
not estimates proved for the prime-product primitives. FAR uses a=Lambda/T,
b=L/2; TRANSITION uses a=H/T,b=Lambda/T; near aliases use a=0,b=H/T.
Sum (27) over all actual orientations, lag paths, cells and aliases, with
consumer coefficients already inside w. Closing means this total fits the
remaining ledger, not merely that each primitive has some unspecified saving.
Setting the comparison primitive to zero proves disposal; a nonzero continuum
comparison requires a separately justified cell-model identification.

Status: exact nonzero aliases CLOSED by (13); proper-power signed-gate removal
CLOSED; short-product cells CLOSED; long FAR, TRANSITION and near-alias
primitive bounds OPEN. H remains unoptimized.

## 14. Exact additive shift conversion and restricted convolution

Write X=T/(2pi), N_cell=X^(6/5). Let P=2^floor((3/5)log_2 X),
Q=2^floor((2/5)log_2 X), and choose p1,p2 in (P,2P], q1,q2,q3 in (Q,2Q].
Eventually these windows are below the unchanged natural cutoff. Then

    N_cell/4 < A=p1p2 <=4 N_cell,
    N_cell/8 < B=q1q2q3 <=8 N_cell.

Put h=A-B and n=A; hence B=n-h. This convention differs by a minus sign
from writing n+h. For z=H/T the exact condition is

    n(1-exp(z)) <= h <= n(1-exp(-z)).                               (30)

It is not a symmetric interval of precisely equal radius. If 0<z<=1,
necessary |h|<=4 N_cell z exp(z), and the sufficient symmetric condition
|h|<=N_cell z/(4e) implies (30), provided the coefficient supports hold.
Since T=2pi X, necessary

    |h| <= (2e/pi) H X^(1/5) = (2e/pi) H N_cell^(1/6),              (31)

and sufficient |h|<=H N_cell^(1/6)/(8pi e). These are rigorous dyadic
constants. In a fixed logarithmic neighborhood the common product exponent
varies; for common exponent gamma the shift exponent is 1-1/gamma.
The exact 1/6 statement is for the dyadic family centered at gamma=6/5.

Fix one closed lag path l1,...,l5, |lj|<=6000, sum lj=0, uj=sum_{a<=j}la,
and orientation (+,-,+,-,-). Define for all five slots

    gj(p) = (log p)/(a_phi L sqrt(p)) f_lj^+(log p/L)
              exp(2pi i u_(j-1) log p/L) 1_{slot j window}(p).

Then restricted squarefree arrays are

    a2,l(n)=sum_{p1 p3=n, p1!=p3} g1(p1)g3(p3),
    a3,l(m)=sum_{p2 p4 p5=m, all three distinct} g2(p2)g4(p4)g5(p5).

For the all-five-distinct hard cell impose additionally gcd(n,h)=1; this is
exactly gcd(A,B)=1. Repeated-label sectors are separate and remain in the
full audit. The exact resolved contribution is

 S5,cell = A_cons sum_closed_l sum_h sum_n
       a2,l(n) conjugate(a3,l(n-h)) 1_{gcd(n,h)=1} 1_{(30)}
       exp(i tau0 log(n/(n-h))) D_d'(log(n/(n-h))/L),                (32)

where A_cons=11501/12500. Its sign is positive because five negative prime
coefficients multiply the negative fifth consumer. Slot windows and all
endpoint Fourier factors are retained. The selected section gives tau0 and
d'; replacement of the exact root-dependent lag admissibility by the section
average is solely the already separated o(1) weighted boundary charge.
No extra trace factor may be inserted: D is already normalized by d'.

IMPORTANT FALSIFIER: the exact kernel is K_T(n,h), not K_T(h). At fixed h=1,
10/9 differs from 20/19. The displayed requested h-only form cannot be exact
with the defined a2,a3. One may define C_T(h) as the whole n-dependent sum
in (32), and write sum_h C_T(h), or expand D into its d' sample phases and
absorb n^(i tau_k) into each array. Neither produces an unrestricted divisor
correlation. Linearizing the logarithm has phase error O(H^2/T), but its
aggregate multiplication by unsigned mass is an additional unproved charge.
Freezing n inside relative-width delta bins has phase cost O(H delta), also
requiring a proved summed error. No such approximation is charged as zero.

An exact noncentral alias similarly has kernel with xi=log(n/(X^m q));
near alias condition n exp(-z)<=X^m q<=n exp(z). This is a dilated affine
correlation, not n-q=h. If X^m=a/b rational, the integer shift is bn-aq;
otherwise the center is nonintegral. Exact aliases are already disposed;
near-alias correlations remain OPEN.

## 15. Fresh primary-source applicability table

The table records theorem hypotheses, not a claimed transfer. N in this table
is the product length N_cell, not the repository prime cutoff. Smooth weights
are fixed smooth functions; dependence on derivatives is material here.

|Primary source / theorem|Sequences, restrictions, cutoff|shift range / uniformity|error / averaging|complex structured weight applicability|
|---|---|---|---|---|
|[Topacogullari 2015](https://arxiv.org/pdf/1506.02608), 1.1/1.2|unrestricted d3(n)d2(n plus/minus h); sharp or fixed smooth compact [1/2,1]|h<<N^(2/3), uniform; fixed shifts|sharp N^(8/9+epsilon); smooth N^(5/6+theta/3+epsilon), constants depend on w,epsilon|no theorem for slotwise prime restrictions, coprimality mask and K(n,h); Kuznetsov is a method, not coefficient transference|
|[Baier--Browning--Marasingha--Zhao](https://arxiv.org/pdf/1101.5464), Theorems 1/2|unrestricted d3(n)d3(n+h), N<n<=2N|1<=Q<=N first mean; N^(1/3+epsilon)<=Q<=N^(1-epsilon) second mean|sum_{h<=Q}Delta <<(Q^2+Q^(1/2)N^(13/12))N^epsilon; sum |Delta|^2<<QN^(2-delta)|first is unweighted signed prefix; partial summation needs bounded variation of an h-only weight; second permits Cauchy for complex h weights with their L2 cost, not K(n,h)|
|[Topacogullari 2016](https://arxiv.org/pdf/1605.02364), 1.1/1.2|unrestricted dk(n)d2(n plus/minus h), k>=4; sharp or nonnegative fixed smooth|nonzero h<<N^(15/19), uniform|sharp N^(1-4/(15k-9)+epsilon)+N^(56/57+epsilon); smooth N^(1-1/(3k-2)+epsilon)+N^(37/38+theta/19+epsilon)|potential unweighted d4/d2 companion; no slotwise prime/filter transfer|
|[Lau 2025](https://arxiv.org/html/2509.07556), 1.1|unrestricted dk,d2 k>=4; fixed nonnegative smooth [1/2,1]|0<abs(h)<<N^(25/28-eta), 0<eta<25/28|N^(1-7eta/128+epsilon)+N^(127/128+epsilon); uniform, constants k,w,epsilon|does not give our prime arrays or growing-frequency mixed n,h kernel|

The 2015 theorem's stated theta can be taken as 7/64 in its framework,
giving smooth exponent 167/192; no claim about the latest spectral bound is
needed. All four entries are primary sources freshly inspected.

Threshold audit: Q approximately H N_cell^(1/6). For H=polylog X, BBMZ's
first-mean ASYMPTOTIC range N^(1/6+epsilon)<=Q is not met for any fixed
positive epsilon; the bound remains valid but provides no uniform power
saving at the endpoint. Its second-mean threshold N^(1/3+epsilon) is much
larger. For H=X^eta=N_cell^(5eta/6), any fixed eta>0 crosses the first
threshold (choose epsilon<5eta/6). Crossing the second requires eta>1/5.
The inherited single-prime support disposal H=o(exp(sqrt(L))) excludes any
fixed positive eta. Changing that window demands a new support audit and
all tail losses. Topacogullari's individual shift range easily contains our
polylog Q: shift SIZE is not its obstruction. Even granting a hypothetical
prime transference with its sharp exponent, absolute summation of pointwise
errors weighted at scale 1/N_cell costs Q*N_cell^(-1/9), which grows as
H*N_cell^(1/18); smooth exponent 167/192 costs H*N_cell^(7/192).
Structured average cancellation, not pointwise power saving alone, is needed.
These comparisons are diagnostic sufficient-bound failures, not lower bounds
on the actual arithmetic residual.

## 16. Prime transference and joint sixth companion

No inspected identity supplies the required transfer for free. Dyadic
partition changes supports only and leaves prime coefficients unchanged.
Mobius inversion uses Lambda=mu*log (with its sign convention) and creates
additional divisor variables and signed sums; divisor asymptotics uniform
in those variables and filter derivatives have not been provided. Vaughan
and Heath-Brown identities give exact decompositions, not small remainders:
each Type I/II/III restricted shifted sum still requires a bound, including
all cutoff and coefficient norms. Buchstab decomposition has a residual
rough-number term and local sieve/parity sensitivity. A weighted sieve
majorant can bound some positive counts but loses the complex carrier and
negative fifth term; an upper count does not give the required lower fifth
contribution. Thus all transfer remainders are UNBOUNDED here, not o(1).
No replacement of a2,a3 by d2,d3 is made.

Geometrically compatible sixth populations at product scale X^(6/5) include
3-versus-3 with all factors about X^(2/5), and 2-versus-4 with positive factors
about X^(3/5) and four negative factors about X^(3/10). Each has exact form
(32) with a3*conjugate(a3) or a2*conjugate(a4), sixth coefficient B_cons=
137641/250000, and the corresponding six-slot closed lag paths. Nonexact
all-distinct populations impose gcd(n,h)=1. Exact 3-versus-3 pair closures
are handled separately by the existing filtered diagonal reduction.
There is no proved unique cell-by-cell pairing of the fifth model with one
sixth cell. The signed 2/3 block determinant is negative; completion gives a
LOWER bound, not the upper consumer bound. The BBMZ/divisor companion methods
therefore do not certify this joint combination. No frozen global HS route
is reopened.

## 17. Exact mass: point, dyadic family, logarithmic neighborhood

At the balanced point v=(3/5,-2/5,3/5,-2/5,-2/5), C5=O5=1/5. The point
itself has mass zero. A fixed dyadic factor cell has logarithmic widths
(log 2)/L, hence its continuum contribution is O(L^-4), tending to ZERO.
The positive fixed-log box in section 10 is a different, nonshrinking region;
its mass remains 1505310601921/2135742187500000000.

For an exactly specified balanced neighborhood let all five exponent
deviations have magnitude <=delta, retaining the signed pattern above and
sum v=0. In four free deviations y1,...,y4 this is [-delta,delta]^4 with
abs(sum y)<=delta. For delta=1/100 all arrangement walls are excluded and

    C5=1/5+y1+y3, O5=1/5-y1-y2-y3.

Exact simplex inclusion-exclusion integration gives

    mass(delta)=delta^4*(69-526 delta^2)/180,
    mass(1/100)=344737/90000000000000,
    fraction of full 1/36 =344737/2500000000000.                    (33)

The verifier checks the chamber against all 45 arrangement hyperplanes and
integrates the polynomial with rational monomial simplex formulas. This
fraction is approximately 1.379e-7, far below either 0.93939459 or 0.99638384
required fifth fraction. The older larger box's fraction is about 2.537e-5,
also far below both. No unspecified 'region' is assigned a unique mass:
(33) defines the neighborhood precisely. A single shrinking dyadic family
cannot account for positive limiting fifth mass; many such cells or a
nonshrinking region with substantially larger mass must be controlled.
Neither computed geometric mass is arithmetic mass already certified.

## 18. Precise stop gate and remaining quantitative theorem

D. EXISTING NUMBER THEORY DOES NOT REACH THE REQUIRED N^(1/6)-SCALE /
FACTOR-RESTRICTED WEIGHTED CORRELATION.

This decision is scoped to the audited theorems: unrestricted d3/d2 reaches
the shift sizes, but not the actual coefficient/kernel/normalization, and
BBMZ's asymptotic average does not cover polylog enlargement of its endpoint.
B is false because FAR, TRANSITION and near aliases remain open. C is not
justified because coefficient transfer alone leaves the structured average,
normalization, sixth companion and other sectors unresolved.

The first local missing lemma is a restricted, carrier-bearing signed
convolution estimate for (32), at N_cell=X^(6/5), factor ranges as in (30),
shifts bounded by (31), with the actual 1/(a_phi^5 L^5 sqrt(n(n-h)))
normalization inside the arrays and ALL finite R=6000 paths. It must supply
an explicit comparison main term M5,cell and a proved bound on its REAL
residual, jointly with M6,cell from the specified sixth arrays if cancellation
is used. The main term is not automatically the sharp C5 cell integral;
filtered model identification must itself be proved. An acceptable cell
statement is

    limsup Re[(S5,cell+S6,companion)-(M5,cell+M6,companion)]
          <= epsilon_cell.                                      (34)

The comparison convention in (32) includes the consumer coefficients; do
not multiply A or B again. Illustrative half-slack caps are

    epsilon_cell <13852305190751/17886179119921875 (ideal),
    epsilon_cell <52897896569489/1144715463675000000 (relaxed).      (35)

They are NOT an allocation theorem. The exact GLOBAL requirement is that
sum of all positive signed residual charges, all model identification charges,
FAR/TRANSITION/alias charges and any additional endpoints not already paid
is strictly less than

    Delta_ideal=27704610381502/17886179119921875
                   approximately 0.00154893955806605,
    M_relaxed=52897896569489/572357731837500000
                   approximately 0.00009242103954753147.          (36)

For a primitive-based route, (27) summed with these same normalizations is
one explicit sufficient error specification. The fully sufficient arithmetic
lemma remains (25), not merely (34). No strict >79 theorem is proved.

Verification additions: wp84_restricted_shifted_convolution_replay.py proves
exact labeled-tuple/shift grouping with the coprimality constraint; exhibits
small-coefficient-L2 coherent samples and small normalized HS/divergent sixth
mass counterexamples; falsifies h-only kernel factorization; and reconstructs
(33). The recon verifier now independently enumerates all closed R=1 lag
paths for degrees 5/6 against its FFT implementation and retains the T=1e7
H=1/H=4 tuple counts/sign flip as assertions. All three verifiers pass.
Proper powers are permanently CLOSED as bounded-signed-gate equivalence:
||P||_(6,tau)=O_R(L^-1/3), coercivity bounds the relevant sixth norm, and
|tau(Y+P)^b-tau Y^b|<=(||Y||6+||P||6)^b-||Y||6^b for b=5,6. This does not
assert unconditional deletion of every masked proper-power sector. No
unproved high-moment bound is smuggled into the gate equivalence.
