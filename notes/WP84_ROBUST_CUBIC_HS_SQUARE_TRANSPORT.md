# Robust cubic Hilbert–Schmidt square: exact transport audit

Date: 2026-10-07. Parent: e85002990e9fb65dc2dd1cc1aea145c7f9910b06.
Branch: codex/c5-c6-attack-20261006. Additive local audit; no push.

**Decision D — DIRECT SQUARE ROUTE BLOCKED.** The specific proposed
public common-lock transport fails at an exact finite identity, before
major/minor analysis: two matrix chains share their endpoints but not
necessarily their full relative-position lock vectors. The growing
log-product carrier also survives conjugation. This does not prove that
no prime-specific direct L2 theorem could work. It prevents promoting the
public p:prod/W1 method to such a theorem through the proposed dictionary.
Return to the already accepted signed theorem (12), restated in Section 13.
Strict >79 is not certified.

The positive square and complete finite Parseval identity ARE proved below.
Their existence alone is not an arithmetic reduction to independent
single-prime factors. All coefficients stay inside the square when the
spectral representation is formed. Expanding the polynomial once to verify
the consumer interface does not replace the primary two-chain test.

## 1. Exact square target and the lower-moment distinction

Fix R_band=6000 and a_pole=221/200. For Hermitian X on the selected
principal section I of size d', define tau_I=Tr/d'. (Thus d in the user's
HS formula means the dimension of the matrix being consumed, d' here.)

    q(X)=a0 I+a1 X+a2 X^2+a3 X^3,
    (a0,a1,a2,a3)=(-19101/185500,961/3710,31/50,-371/500).
    Q=q(X)=Q*,
    tau_I q(X)^2 = Tr(Q Q*)/d' = ||Q||_HS^2/d'.             (1)

The exact centered-moment coefficients c_b=sum_(r+s=b) a_r a_s are:

| b | c_b |
|---|---|
|0|364848201/34410250000|
|1|-18356061/344102500|
|2|-26060119/430128125|
|3|21981971/46375000|
|4|0|
|5|-11501/12500|
|6|137641/250000|

In particular a2^2+2a1a3=0, before any absolute-value estimate.
Write A=11501/12500, B=137641/250000. With the inherited bounded
consumer p_dag(x)=a_pole^6 q(x-1)^2/(x^2+a_pole^2)^3, its support and
upper-domination certificate gives the sufficient DIRECT target

    limsup_T ||q(X_T)||_HS^2/d' < K_* ,
    K_*=21/200-e_band=9573834737/92407500000
        =0.103604520596272... .                            (2)

Here e_band=128952763/92407500000 is paid once. The variance payment
is NOT added to an actual measured/proved q-square, since mu2 is already
inside it. Let E_base=c0+c2/3 and

    ell_T=c1 mu1+c3 mu3+c2(mu2-1/3).
    tau_I q^2=E_base+ell_T-A mu5+B mu6.                    (3)

The exact equivalent high-order condition is the upper bound on the
RIGHT SIDE OF (3), including ell_T. Frozen lower inputs give
mu1,mu3=o(1), mu2>=1/3-2/(pi^2 R)+o(1), hence

    ell_T <= e_var+o(1),
    e_var=26060119/12734908593750=0.00000204635304667909... .

Consequently the accepted cap J_*=K_*-E_base-e_var is SUFFICIENT for
(2), not logically necessary under these one-sided inputs. Claiming exact
logical equivalence to the worst-case signed cap would turn a variance
inequality into an equality. Exact equivalence holds if the actual ell_T
is retained; replacing it by e_var produces the robust envelope.

    J_*=64788151489666079/572357731837500000.

A strict eta gap in the robust signed envelope gives defect <=21/200-eta
and the inherited simple-zero coefficient >=79/100+2eta-o(1).
Source normalization, common-section lower moments and zero-side bounded
transfer remain inherited hypotheses; finite algebra does not prove them.

## 2. Actual long cutoff and resolved matrix entries

Retain the natural scale, unchanged:

    L=log(T/(2pi)), h=2pi/L, d=floor(T L/(2pi)),
    N=floor(exp(L-sqrt(L))), tau_i=T+h i,
    c_n=-Lambda(n)/(a_phi L sqrt(n)), a_phi -> 1,
    n=p^v<=N, v>=1, s_n=log(n)/L.

The selected section I=[k_-,k_+] has d'~d, endpoint-window size
floor(d/sqrt(L)), and the frozen good-endpoint bounds on 12R neighborhoods.
No short-cutoff substitution is made: N^3/T diverges on this scale.

Use the ROW-index convention consistently:

    f_0^+(s)=f_0^-(s)=1-s,
    f_l^+(s)=(1-exp(2pi i l s))/(2pi i l), l!=0,
    f_l^-(s)=conj(f_l^+(s)).
    X_ij=1_(i,j in I, |j-i|<=R)
          sum_(n=p^v<=N,epsilon=+/-1)
             c_n exp(i epsilon tau_i log n) f_(j-i)^epsilon(s_n). (4)

This is the centered filtered prime matrix of the frozen source interface.
Its diagonal is beta_i=2 Re sum c_n(1-s_n)e^(i tau_i log n);
its off-diagonal is (alpha_i-alpha_j)/(pi(j-i)),
alpha_i=Im sum c_n e^(i tau_i log n). Formula (4) verifies Hermiticity;
it includes proper powers, both orientations and zero displacements.

## 3. Full entrywise paths and pairs with common endpoints

For r>=1, a path gamma=(v0=i,v1,...,vr=j) has increments
l_a=v_a-v_(a-1), |l_a|<=R, all v_a in I. Let
u_a=v_a-i=sum_(t<=a) l_t, u0=0. Retain a distinct n_a=p_a^e_a
and epsilon_a on EVERY edge, even if labels coincide. Define

    F_gamma(epsilon,n)= product_(a=1..r)
       c_(n_a) f_(l_a)^epsilon_a(s_(n_a))
       exp(2pi i epsilon_a u_(a-1) s_(n_a)),
    lambda_gamma=sum_a epsilon_a log(n_a).
    P_r(i,j)=sum_(gamma:i->j) sum_(epsilon,n)
                 F_gamma exp(i tau_i lambda_gamma).
    P_0(i,j)=delta_ij.

All sums are finite. No equality or near-equality of prime products is
inserted. Entrywise,

    Q_ij=a0 delta_ij+a1 X_ij
         +a2 sum_(k in I) X_ik X_kj
         +a3 sum_(k,l in I) X_ik X_kl X_lj.              (5)
    E_T=(1/d') sum_(i,j in I) |sum_(r=0..3) a_r P_r(i,j)|^2.

The exact paired block is

    Pair_rs=(1/d') sum_(i,j) P_r(i,j) conj(P_s(i,j)).
    E_T=sum_(r,s) a_r a_s Pair_rs.                       (6)

Each pair has two independent internal-vertex strings with the SAME i,j.
Thus sum_a l_a=sum_b m_b=j-i, but no edgewise equality is imposed.
For Hermitian X, Pair_rs=tau_I X^(r+s). This cyclic identity proves
that all r+s=4 blocks cancel after their coefficients are assembled.
It does not prove equality between individual path weights or prime locks.

The effective positive-sign/negative-sign prime product pools within a
block of total degree r+s can each have length up to N^(r+s), depending
on orientation; their total degree is at most six. The natural weighted
Hilbert bounds for degree five/six carry N^(5/2)/T and N^3/T, respectively,
and do not tend to zero. A length-three path on each side does not make
all signed factors positive or reduce every product pool to N^3.

## 4. Decisive common-lock dictionary, all 16 blocks

For the public normalized additive positions x1,...,xb define the full
lock j=(x2-x1,...,xb-x1). Two configurations have this same lock iff
y_k-x_k=t for EVERY k. For unit affine chains the normalization by the
unit products A_k gives this relative-position version. Sharing endpoints
is only two equations, not that full set of equations.

| our variable | proposed public variable | exact disposition |
|---|---|---|
|i,j|root and terminal position|matrix row indices, not prime positions|
|internal v_a,w_b|remaining lattice positions|independent in (6); their relative locks need not agree|
|increments l_a,m_b|lock coordinates|only equal TOTAL increment is enforced|
|n_a=p_a^e_a, m_b=q_b^f_b|windowed prime positions|edge labels independent of matrix vertices; no affine prime-lock equations|
|s_n=log n/L|position coordinate|real logarithm; public position is b_i n on an integer lattice|
|I and all internal membership tests|prime windows|matrix-row restrictions, not independent prime windows|
|i shifted by t|common additive shift|a shift of row index; leaves log-product carrier, not a shift of all prime labels|
|tau_i=T+h i|window/analysis variable|large Mellin phase, absent from a bare additive prime-position lock|
|R=6000|modulus/cell cutoff|Fourier displacement cutoff, not a prime-power modulus or ell1 truncation|

The matrix-coordinate status of each block is explicitly:

| r\\s |0|1|2|3|
|---|---|---|---|---|
|0|constant identity; no primes|closed one-edge path; unequal lengths|closed two-edge path; unequal lengths|closed three-edge path; unequal lengths|
|1|transpose of (0,1)|same two vertices, independent prime labels|unequal lengths, free internal vertex|unequal lengths, two free internal vertices|
|2|transpose of (0,2)|transpose of (1,2)|same endpoints, one internal lock UNMATCHED|unequal lengths, independent internal vertices|
|3|transpose of (0,3)|transpose of (1,3)|transpose of (2,3)|same endpoints, two internal locks UNMATCHED|

Only (0,0) is an immediate constant identity. Matrix-coordinate equality
in (1,1) does not provide prime-position equality; every nonconstant block
still fails the proposed prime-lattice dictionary. Transposition here means
complex-conjugate polarized block, not deletion of a sector.

FIRST EXACT failed implication, already in (2,2):

    (i,v,j) and (i,w,j) have common endpoints
       DOES NOT imply common relative-position locks.

Witness (0,1,3), (0,2,3), with R>=2 and section containing 0,...,3:
the coordinate differences are (0,1,0), not a common shift. The actual
R=6000 admits this witness. The full-lock public identity cannot sum these
pairs as common-shift pairs. It therefore fails even before logarithmic
prime coordinates or an asymptotic normalization is considered.

## 5. Carrier conjugation does not remove the obstruction

With gamma length r and eta length s sharing i,j, their phase is

    exp(i tau_i lambda),
    lambda=sum_a epsilon_a log n_a-sum_b delta_b log m_b,

times the retained internal-offset factors in F_gamma conj(F_eta).
The common-root factor cancels only when lambda=0. It does not cancel
merely because the paths share endpoints. Even the (1,1) diagonal pair
n=2,m=3, epsilon=delta=+1 leaves exp(i tau_i log(2/3)); the diagonal
filter factors (1-s_2)(1-s_3) are nonzero for large T.

This is a GENUINE MULTIPLICATIVE NEAR-PRODUCT CARRIER, with fixed
endpoint-offset factors in addition. In a given path-pair the root average
is over the exact interval I intersected with all translated section tests.
For an unrestricted admissible root interval starting i0 of length m,

    (1/d') sum_i exp(i tau_i lambda)
       =(m/d') exp(i(T+h i0)lambda) D_m(lambda/L),
    D_m(z)=m^-1 sum_(k=0..m-1) exp(2pi i k z).

Zero length paths use lambda=0 for that chain, not a fictitious prime label.
The complete q-square has cancellations; an isolated (1,1) witness alone
is not a proof of a surviving coefficient in every assembled frequency.
But the leading formal degree-six component is a3^2 ||X^3||_HS^2/d',
with nonzero coefficient. On a one-vertex real field X=z+conj(z), its
sixth harmonics survive. Thus polynomial assembly does not algebraically
erase all nonzero carriers. Any extra cancellation for the actual prime
matrix would require an arithmetic theorem, not conjugation alone.

## 6. Exact polarized identities and why W2 cannot pad matrix paths

On G=Z/M, for b slots let

    N_f(j2,...,jb)=sum_x f1(x) product_(k=2..b) f_k(x+j_k).
    C_k(t)=sum_x f_k(x) conj(g_k(x+t)).
    sum_j N_f(j) conj(N_g(j))=sum_t product_k C_k(t).       (7)

Proof: write y=x+t in the second chain and set z_k=x+j_k. Summing
independently over x and every j_k sums independently over every z_k.
For integers with finite supports, the same proof holds with unrestricted
integer locks and sums; zero-extension on a sufficiently large cyclic grid
recovers it without wrap. Restrictions must be retained as weights and
cannot silently be removed. Complex conjugation is the required polarization.

Using unnormalized Fourier transforms hat f(xi)=sum_x f(x)e(-xi x/M),

    hat N_f(xi2,...,xib)
       =hat f1(-sum_(k>=2) xi_k) product_(k>=2) hat f_k(xi_k).
    sum_j N_f conj(N_g)
       =M^(-(b-1)) sum_xi hat N_f(xi) conj(hat N_g(xi)).  (8)

The first factor has the COUPLED frequency -sum xi_k. Complete Parseval
is exact; declaring all factors to have independent frequencies is not.

Different b have different lock spaces; (7) does not define their mixed
inner product without a specified embedding. A valid free spectator
satisfies sum_z H(j)u(z)=H(j)sum_z u(z), with unrestricted z and no
coupling in H. This is the exact W2/Fubini hypothesis. Matrix padding of a
shorter chain instead inserts I_uv=delta_uv. Its offset is constrained to
zero and its vertices coincide. It is NOT an unrestricted prime slot with
window mass. Replacing I by a free all-ones edge changes X I=X to X J,
which differs in the verifier. A dummy prime slot with product phase also
changes the carrier; the only identity label would be n=1, not a prime.

For ALL mixed lengths the valid generalized identity is the endpoint
polarization (6) and its spectral form (9) below. It retains constrained
padding if one chooses to use it. No factorized single-prime mixed-length
identity follows from W2 for these paths.

## 7. One complete positive spectral square, exact at finite T

Take an integer analysis period M>=d', shift indices by k_-, and
zero-extend EACH already computed matrix P_r to G^2. Define

    S_r(u,v)=sum_(i,j in I) P_r(i,j)
                 exp(-2pi i[u(i-k_-)+v(j-k_-)]/M).
    E_T=(1/(d' M^2)) sum_(u,v in G)
                 |sum_(r=0..3) a_r S_r(u,v)|^2.          (9)

Dimension: two; grid: M by M; weight: positive uniform 1/(d'M^2).
The transforms are of matrices with exact section tests, not circular
matrix products. No restriction on R relative to M is needed for this
zero-extended transform of already formed entries. A cyclic convolution
implementation of the path products would need separate padding and tests.

Proof: two finite orthogonality sums leave only equal i and equal j.
Polarization also gives Pair_rs=(d'M^2)^-1 sum S_r conj(S_s).
All a_r remain inside the amplitude in (9); c4 cancellation follows upon
polarizing and grouping r+s, not by estimating each block separately.

Substituting (5) into S_r leaves sums over roots, internal vertices, and
r independent signed prime-power labels with logarithmic phases and
filters. S_r is NOT a windowed single-prime exponential sum. The public
(b-1)-coordinate lock transform (8) and this two-coordinate endpoint
transform have different fibers. Parseval orthogonality in (9) enforces
endpoint equality, not equal prime products or full internal locks.

A positive-bin truncation E_keep<=E_T is a LOWER bound. For the desired
upper bound, one must prove E_T<=E_keep+E_omit with a certified upper bound
on E_omit. Positivity alone cannot discard dangerous positive mass, nor
turn geometrically favorable signed sectors into free upper-bound gains.
No omitted-bin bound with the required precision is currently proved.

## 8. Pinned public candidate machinery at the HS-square level

PUBLIC CANDIDATE SOURCE — NOT ASSUMED CORRECT.
JoshuaHKU/zeta-0.7947-reproduction,
commit d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8.
Read paper.tex: s:trunc, s:local, s:four, p:prod, W1/W2/W3,
s:five:conn. Source hash and verification-program hashes are preserved in
WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE_CERTIFICATE.json. The pinned texts
were reread locally, not replaced with current public head.

| component | classification for our square | reason |
|---|---|---|
|finite complete Parseval|DIRECT|finite group orthogonality proves (9)|
|p:prod polarized finite algebra|DIRECT on its stated lock object|proof (7); not an identification with (6)|
|p:prod dictionary to our square|MISMATCH|same endpoints do not fix full locks; independent edge primes|
|W2 finite Fubini|DIRECT for a truly free spectator|identity padding and prime phases violate its hypotheses|
|W2 mixed-length prime padding|MISMATCH|delta edge, not unconstrained offset/window sum|
|W3 triple-pair philosophy|ADAPTABLE after exact pair reduction|our opposite-prime pair sector already has PNT transfer; no near-product gain|
|W1 multidimensional comb transfer to (9)|MISMATCH|different fibers and amplitudes; no factorwise single-prime dictionary|
|W1 additional prime asymptotic needed here|UNPROVED|finite FFT/local enumerations do not prove our normalized L2 remainder|
|MM / Siegel–Walfisz|MISMATCH as direct application|public additive e(n gamma), ours Mellin e^(i tau log n)|
|minor/mixed / Vaughan|MISMATCH as direct application|our amplitude has multiple primes, path restrictions, natural long cutoff|
|CRT/local coincidence counts|DIRECT finite affine residue algebra; MISMATCH to ours|no affine prime-lock constraints from endpoint equality|
|comb identification|UNPROVED for ours|no model spectrum with normalized bin-mass estimates|
|truncation discharge|MISMATCH|public ell1/modulus weights not our log/filter displacement tails|

The paper's MM leaf splits Lambda(n)e(n gamma) into progressions for
denominators <=log^B X and window length Y~X^theta, theta>1/2.
Its minor leaf uses Vaughan for additive phases, and its claimed relative
mass bound also consumes spacing and stratum budgets. The comb uses
integer CRT congruences in prime POSITION lattices b2*m and b1*n.
Its truncation uses weight ell1^-k times normalized mass O(ell1) and
divisor multiplicity ell1^epsilon; none is an available bound for the
finite-R prime-path square. The public proof's factor-by-factor claim
cannot repair the failed dictionary in Section 4. No theorem grade is
inferred from percent-level finite faces or their numerical Parseval tests.

## 9. Exact logarithm/additive-lock obstruction

The public integer coordinate b*n is not a logarithmic prime cell.
An additive shift n->n+t changes log n by log(1+t/n), depending on n;
it is not a common additive shift of logarithms. Conversely a common
logarithmic shift maps n->exp(t)n and need not map primes to primes or
preserve the windows. Matrix root shifts change exp(i h i log n),
without shifting the prime labels at all. Thus no exact change of
variables satisfying the proposed prime-window/lock dictionary exists.

A conditional near-product window |log(A/B)|<=O(1/T), with other labels
fixed, gives a final-prime interval of length O(n/T)<1 at this cutoff.
That is not the public Y~X^theta window. Log linearization on relative
cells of width u leaves a T u^2 phase error; an o(1) bound needs
u=o(T^-1/2), together with a NEW aggregate remainder estimate. Public
ell1 truncation supplies neither this estimate nor its normalization.
There is more than one missing interface, so decision C is unjustified.

## 10. Alias, prime-power and section ledger

The root sampling in Section 5 retains exact aliases lambda=m L and
near aliases |lambda-m L|~1/T. At exact alias the root Dirichlet kernel
is one, leaving exp(i T m L); this need not be one. Conjugation subtracts
signed log sums but does not suppress these populations. Full endpoint
Parseval does not orthogonalize the prime labels inside an amplitude.

| population/payment | rigorous status |
|---|---|
|full-to-band bounded functional|e_band, already paid in K_*|
|actual variance in square|included exactly; e_var only if using lower envelope|
|principal-section deletion|bounded-consumer O(L^-1/2)=o(1), inherited; no raw-moment rank claim|
|repeated filtered A_b to B_b|rho_b=4b R K_R^b/d'=o(1), b=5,6, same good section|
|good-endpoint neighborhoods|frozen 12R grouped linear-field bound, not a high-product L2 theorem|
|exact ordinary-prime fifth products|no exact multiplicative closure; E5=o(1) after existing exact power analysis|
|exact leading sixth products|three opposite pairs; E6=Pair6_6000+o(1)|
|exact repeated-base/proper-power closures|existing convergent valuation sums, o(1)|
|pair PNT/BV and endpoint quarantine|O_R(L^-2+|a_phi-1|+L^-1/2) after reduction|
|exact nonzero periodic aliases|existing exact-alias divisor bound, o(1)|
|nonexact ordinary/repeated/proper powers|retained; no new o(1) bound|
|near aliases, far nonexact products|retained; OPEN signed arithmetic contribution|
|filtered-to-sharp substitution|none used in direct target or fallback; any model comparison needs a paid remainder|
|public log-cell/CRT truncation|no proved transfer charge in our normalization|

The o(1) entries inherit the exact-reduction gates documented in the
fixed-R arithmetic-transfer and first-strike notes. The new finite verifier
does not certify these asymptotic gates afresh. Keeping powers and aliases
in (5)/(9) prevents silently claiming their disposal by orthogonality.

## 11. Exact precision and complete error budget

| quantity | exact value | decimal |
|---|---|---|
|actual square threshold K_*|9573834737/92407500000|0.103604520596272|
|ideal sharp joint-model square E_ideal|35116876419/344102500000|0.102053534685159|
|relaxed-sixth square E_rel|240421959557/2322691875000|0.103510053203678|
|band charge|128952763/92407500000|0.00139547940372805|
|variance envelope charge|26060119/12734908593750|0.00000204635304667909|
|ideal PAID allowance Delta_ideal|27704610381502/17886179119921875|0.00154893955806605|
|relaxed PAID allowance M|52897896569489/572357731837500000|0.0000924210395475315|
|extra ideal room|19663/13500000|0.00145651851851852|
|arithmetic transport charge|NOT CERTIFIED|must fit the corresponding strict allowance|

If proving E_T<=E_ideal+e_var+delta+o(1), require delta<Delta_ideal.
Its exact relative ENERGY allowance delta/E_ideal is less than
886547532208064/58411129638397365=0.0151777159198318 (1.51777159198318%).
For E_rel+e_var+delta, require delta<M; relative energy allowance is
52897896569489/59244779274035940=0.000892870177215286
(0.0892870177215286%). These references are model ledger values,
not certified actual fixed-R square limits.

A direct comparison already including actual mu2 instead has allowances
K_*-E_ideal=Delta_ideal+e_var and K_*-E_rel=M+e_var. The verifier records
both exact fractions. Do not subtract e_var again in that situation.
For an amplitude norm perturbation ||S-S_model||_normalized<=epsilon,
Cauchy–Schwarz gives energy loss <=2 sqrt(E_model)epsilon+epsilon^2;
the corresponding exact relative amplitude tolerance is
sqrt(1+delta/E_model)-1, not the energy percentage itself. This is only
a conditional diagnostic until a model amplitude and norm error are proved.

Endpoint/reprojection losses are o_T(1) at fixed R, distinct from model
filter/sharp and arithmetic errors. A model-mediated attempt must charge
its finite-R geometry error inside the SAME allowance as arithmetic;
there is no certified numerical allocation that may be added for free.

## 12. Secondary six-variable lift: what is actually exact

Only after the direct common-lock test failed, test the W2 lift. A fifth
geometric zero-sum tuple (v1,...,v5) has four free coordinates; adding an
independent spectator t in [0,1] with unit mass gives five free coordinates,
equivalently six listed coordinates with sum_(1..5) v_i=0. Its exact
integral is unchanged by Fubini. A {4,2} geometric integrand with four free
coordinates can be lifted similarly; a sixth zero-sum tuple already has
five. These facts give a common DIMENSION, not the same domain or density.

More explicitly, let (Omega5,nu5),(Omega42,nu42),(Omega6,nu6) be the
frozen distinct geometric integration spaces, with original scalar
integrands H5,H42,H6 INCLUDING their overlap and density weights. The
exact joint tagged five-free-coordinate measure space is

    Omega=( {5} x Omega5 x [0,1] )
       disjoint-union ( {42} x Omega42 x [0,1] )
       disjoint-union ( {6} x Omega6 ).
    H(5,z,t)=-A H5(z), H(42,z,t)=B H42(z), H(6,z)=B H6(z).
    integral H = -A/36-B*23/420-B/126.                   (10)

This is a valid joint weighted kernel construction with exact scalar
model integrals. It is not a common arithmetic six-prime kernel. Taking
an arbitrary independent density of mass one also lifts a scalar arithmetic
sum formally, but does not make its spectator a prime cell satisfying W2.
Inserting a genuine sixth prime changes log products, filters and section
paths. Inserting an identity edge constrains its offset and supplies no
free prime mass. Those are the exact failed W2 hypotheses.

Marginal/sign tests therefore cannot be promoted from (10) to actual
arithmetic. The existing sixth connected kernel takes +2/5 and -1/10 on
closed tuples with outer overlap 1/5; a universal negative Gram certificate
for that component is false. Symmetrizing labels does not remove the
carrier depending on the full log product. A covariance-only upper
certificate is impossible: a symmetric scalar law with mass 1/(6t^2)
at each of +/-t and remaining mass at 0 has mu2=1/3, mu1=mu3=mu5=0,
mu6=t^4/3; its q-square grows as B t^4/3. The verifier checks this
exactly. This is an obstruction to universal covariance/Gram bounds,
not a counterexample to a prime-specific joint theorem.

An exact polyhedral majorant for the frozen GEOMETRIC integrals cannot
bound an unidentified arithmetic signed measure. The first required step
for a weak dual or polyhedral arithmetic witness would be a proven finite
common measure/kernel reduction with paid omitted mass. No such reduction
or dual certificate is supplied here. The secondary lift has not closed a
new arithmetic theorem and does not justify a six-prime W2 claim.

## 13. Compare routes and return to the frozen theorem

| issue | direct square via proposed public method | accepted signed fallback (12) |
|---|---|---|
|open arithmetic statement|one scalar L2 upper target (2), but no factorized reduction; dictionary fails|one explicit signed resolved-prime residual bound|
|required loss|model-based delta<Delta_ideal or M, plus all model errors; or direct K_*|strict gap below J_*; same paid envelope|
|carrier|survives inside amplitudes|retained explicitly in N5,N6|
|aliases|not erased by endpoint Parseval|included in residual theorem|
|proper powers|not erased by endpoint Parseval|nonexact sectors included, exact sectors reduced|
|sharp substitution|unnecessary for (2); needed if importing model spectrum|unnecessary in its direct form|
|public prerequisites|multiple unmatched interfaces, not one normalization lemma|no claim of public factorwise application|

There is no proved strictly stronger arithmetic route from positivity.
The direct square target is potentially weaker than the WORST-CASE lower-
moment envelope, but simply renaming it an L2 lemma gives no new estimate.
The fallback is the stronger established REDUCTION: exact closed sectors
are separated and one explicit nonexact signed theorem is specified. We
choose that substantive reduction, without claiming mathematical dominance
of its sufficient condition over the actual-square target.

Define B_b,T,R by the resolved finite paths of the fixed-R note, with
E_b their exact lambda=0 sectors and N_b=B_b-E_b. On the SAME admissible
good section E5=o(1), E6=Pair6_R+o(1), where

    Pair6_R=sum_(15 matchings) sum_(8 opposite-pair orientations)
       integral_[0,1]^3 Gamma6_R(epsilon,s) product_(a=1..3) s_a ds_a,
    Gamma_b,R=sum_(l1+...+lb=0, |l_a|<=R)
       product_a f_(l_a)^epsilon_a(s_a)
       exp(2pi i sum_a epsilon_a u_(a-1) s_a).

The exact remaining theorem is existence of eta>0 such that

    limsup_T Re[-A N5,T,6000+B N6,T,6000]
       <= J_*-B Pair6_6000-eta.                         (12)

All nonexact ordinary, repeated-prime, proper-power, far and near-alias
populations stay in N_b. Constants and section are those of the frozen
natural cutoff. No numerical sharp substitution for Pair6_6000 is used.
A proof of (12), together with frozen inherited inputs, implies strict
>79. This audit proves no such inequality. A direct prime-specific proof
of (2) would also suffice, but the pinned common-lock identity is not that
proof. Decision D is the sole NEW decision; it preserves the prior accepted
fallback Decision B rather than overwriting its evidence boundary.

## 14. Verifier, provenance and evidence boundary

Run:

    python src/wp84_robust_cubic_hs_square_transport.py --write
    python src/wp84_robust_cubic_hs_square_replay.py

The exact verifier uses Fraction and SymPy rational/complex algebra. It
checks all sixteen finite entrywise path blocks, their trace identities,
all sixteen polarized Fourier blocks, the COMPLETE coefficient-weighted
positive square on a 4x4 grid, complex public product polarization,
complete coupled-frequency multidimensional Parseval, unrestricted
free-slot Fubini, the endpoint/common-shift counterexample, constrained
identity-padding counterexample, and the covariance upper-bound obstruction.
It regenerates WP84_ROBUST_CUBIC_HS_SQUARE_CERTIFICATE.json.
An independent Fraction-only replay reconstructs all ledger constants and
checks the full weighted HS square on a separate 2x2 matrix using an exact
Walsh transform. Both new verifiers PASS. The frozen first-strike replay
also PASSes, and all six pinned public source SHA256 hashes match.

The finite matrix contains complex Hermitian off-diagonal entries and
exact boundary restrictions. It is a finite algebra verifier, not a prime
sample or asymptotic proof. No Monte Carlo, new parameter optimization,
cutoff shortening, fixed-R/sharp equality, or independent zero-count
claim is used. Polynomial c4 cancellation is retained before norms.
Pinned public source hashes are inherited and checked against the local
copies during the audit. Existing commits and notebooklm_packet remain
preserved. main and the Downloads checkout are unchanged.
