# Repaired open-path signed arithmetic

Parent def80b674410ff58361f506f1922cc2e952c646d; isolated branch
codex/c5-c6-attack-20261006. No push. Earlier falsifiers and Decision F are
preserved. No actual mu7/mu8 integration or consumer optimization is performed.

**Decision F: INCONCLUSIVE.** The exact residual is frozen below. First
uncertified analytic step: a signed oriented near-product/near-alias estimate
for the complete repaired open block in the selected-section normalization.
There is an exact masked embedding retaining old product/shift geometry, but
no projection theorem extracting that cell from a bound for the entire signed
block. Therefore equivalence/harder/impossible verdicts C/D/E are not proved.
The 79.5891590 relaxed witness still has no complete degree-eight paid ledger.

New CLOSED results: explicit full finite-R exact-diagonal asymptotic main-term
formula; its ordinary order-seven main term is zero; higher prime multiplicities
and proper-power EXACT-DIAGONAL groups are o(1); exact nonzero alias disposal
extends to order eight. A full R=1 replay gives a strictly positive signed
open diagonal and a nonzero scalar eighth cumulant. Neither numeric value is
promoted to the frozen R6000 calculation or to an arithmetic moment theorem.

## 1. The complete scalar, including powers and every root constraint

Fix L=log(T/(2pi)), X=exp L=T/(2pi), N=floor(exp(L-sqrt L)),
h=2pi/L, selected I=[k_-,k_+], d'=|I|~floor(TL/(2pi)), fixed R=6000,
a_phi->1. Leaf n_j=p_j^v_j<=N has coefficient
c_n=-log(p)/(a_phi L sqrt(n)), alpha_j=log(n_j)/L, sign eps_j.
Use the exact filters
f0=1-alpha, f_l^+=(1-exp(2pi i l alpha))/(2pi i l), f_l^-=conjugate f_l^+.

A higher word zeta at n=7 or 8 retains all leaves/signs, l_j in [-R,R],
sum l_j=0, u0=0, uj=sum_(k<=j)l_k. Define
lambda=sum eps_j log(n_j),
i_min=k_- - min u, m_u=max(0,d'-(max u-min u)),
W(zeta)=prod_j c_nj f_lj^epsj(alpha_j)
 exp(2pi i sum_j eps_j u_(j-1)alpha_j),
K_u(lambda)=exp(iT lambda)(m_u/d')exp(2pi i i_min lambda/L)D_(m_u)(lambda/L),
D_m(z)=m^-1 sum_(k=0)^(m-1)exp(2pi i k z).
Set K=0 when m_u=0. These are the true sampled/principal-section factors.

Deletion marks M(zeta) consist ONLY of ordinary-prime pairs: v_s=v_t=1,
p_s=p_t, eps_s=-eps_t, s<t. For each mark its defect is
Delta_st=-(l_s+l_t). The marks retain insertion positions, orientation,
lags, intermediate paths and every projection; their higher root interval
above enforces the entire selected-section mask. Proper-power leaves in the
remaining word are retained until a justified reduction is made.

Reserve the frozen canonical subset FIRST: final leaves are opposite signs
of the same ordinary prime and both lags zero. Its contribution is outside O.
For every remaining word with nonempty M use the unmarked average
 theta_open(zeta)=# {marks with Delta_st!=0}/|M(zeta)|.
For a reserved canonical word or M empty set theta_open=0. This allocation
is exact and fixed; another allocation would define a different open scalar.

 O_n(T,R)=sum_(all closed higher zeta) theta_open(zeta) W(zeta)K_u(lambda),
 n=7,8.

Equivalently sum each open mark with weight 1/|M|, retaining its Delta and
insertion labels. This is the complete signed object in this convention;
no continuum proxy is used. It is real after including all adjoints. A single
marked or windowed piece may be complex. The constructor accepts prime-power
leaves, uses Lambda(n)=log(base prime), and marks ordinary pairs only.

## 2. Disjoint arithmetic partition

For nearest bin m=floor(lambda/L+1/2), xi=lambda-mL, take 0<H<=Lambda<TL/2
and the same central/transition/far partition parameters as the frozen notes.
Split power-containing words first from all-ordinary words; within EACH split:
- exact diagonal: lambda=0;
- exact nonzero alias: xi=0, m!=0;
- central nonexact: m=0, 0<|xi|<=H/T;
- near alias nonexact: m!=0, 0<|xi|<=H/T;
- transition: H/T<|xi|<=Lambda/T in every bin;
- far: Lambda/T<|xi|<=L/2 in every bin.
Thus proper powers are not counted again as an eighth overlapping category.
All pieces carry the same theta_open, W, K and 1/d' normalization. No
absolute-value splitting of O7/O8 is performed in the target consumer.

## 3. COMPLETE exact-diagonal main term at every fixed R

Unique factorization implies every ordinary exact-diagonal prime occurs with
balanced plus/minus multiplicity. Odd length is impossible: O7^diag,ordinary=0
EXACTLY. At order eight the leading groups are four distinct primes, each
occurring twice, once with each sign. Any group occurring four or more times
has vanishing total mass: sum_p |c_p|^4=O(L^-4), while sum_p |c_p|^2=O(1).
There are finitely many lag/sign/partition patterns at fixed R, every filter
has modulus <=1 and |K|<=1. Thus all other ordinary diagonal collision types
are o(1) without any nonexact correlation estimate.

If a balanced prime group contains a proper-power leaf, its total exponent
on both sides is at least two, so its absolute product denominator is at
least p^2. Summing all exponent compositions for fixed leaf count costs only
a convergent geometric/polynomial series. Its prime sum is O(L^-r) for that
group's r>=2 leaves; other ordinary paired groups have bounded square mass.
Consequently EXACT-DIAGONAL proper-power populations at either order are
O_R(L^-2)=o(1). This does not remove masked nonexact powers.

Let pi range over the 105 pairings of eight slots and let l range over
[-R,R]^8 with sum l=0. Put d_jk=u_(j-1)-u_(k-1). For a pair of lags l,m and
integer d define the orientation-summed covariance

 C(l,m,d)=sum_(eps=+,-) integral_0^1 alpha f_l^eps(alpha)
              f_m^-eps(alpha) exp(2pi i eps d alpha) d alpha.

This is an exact PNT reduction AFTER prime equality is justified. Independent
pair primes have the product measure alpha d alpha; coincident pair labels
are already disposed above. Endpoints contribute (d'-spread u)/d'->1 for
these diagonal terms. Here no growing unsigned prime mass occurs, so this
fixed-R endpoint convergence is justified independently of a high-moment gate.

Write x=(2pi i)^-2=-1/(4pi^2). Direct exponential integration gives

 C(0,0,0)=1/6;
 C(0,0,d)=2x/d^2 for d!=0;
 C(l,0,d)=C(0,m,d)=0 if exactly one lag is nonzero;
 C(l,m,d)= -x/(lm)[1_(d=0)-1_(d+l=0)-1_(d-m=0)+1_(d+l-m=0)]
              for l,m!=0.

For example use J_n(k)=integral_0^1 alpha^n exp(2pi i k alpha)d alpha,
J_n(0)=1/(n+1), J0(k)=0 if k!=0,
J_n(k)=h/k-n h J_(n-1)(k)/k with h=(2pi i)^-1.
Expand both filter factors, then add the conjugate h->-h. This yields the
above formulas; an independent replay verifies them by integration recurrence.

For each pairing and lag tuple define q(pi,l)=number of pairs with l_j+l_k!=0.
Let r(pi,l)=1 if the pairing contains the last two slots as a pair AND those
two lags are zero, otherwise 0. Then the COMPLETE signed diagonal main term is

 D8_open(R)=sum_(l closed) sum_(pi pairing)
              (1-r(pi,l)) [q(pi,l)/4]
              prod_((j,k) in pi) C(l_j,l_k,d_jk).

This includes EVERY insertion mark, orientation, multiplicity, coefficient
sign and reserved-canonical subtraction. It is a finite polynomial in x of
degree <=4 with rational coefficients, not a guessed rational sharp moment.
The exact asymptotic theorem is

 O7^diag(T,R)=o(1),
 O8^diag(T,R)=D8_open(R)+o(1),

at every fixed R, including the exact-diagonal power/collision terms just bounded.
Thus diagonal MAIN-TERM REPRESENTATION is CLOSED. Its numeric/sign evaluation
at R6000 has NOT been completed. The literal enumeration upper workload is
105(12001)^7 before support reduction; do not launch an unbounded brute-force
job or promote R1 to R6000. The Kronecker constraints provide an exact sparse
summation problem for further optimization if a paid consumer region warrants it.

The full R1 calculation, independently enumerating all 105 pairings and all
closed lag words, is

 D8_open(1)=(373/36)x^2-(1293/4)x^3+(36130/9)x^4
            =0.01355423586769687... >0.

Every displayed term is positive because x<0. This proves the earlier positive
population survives the ENTIRE signed open diagonal at R1 in the fixed reserved
allocation. It does not prove positivity at R6000. At R0 the open term is zero.
The certificate preserves both scopes explicitly.

## 4. Cumulants: what actually cancels, and what is not in the consumer

The scalar consumer p(X)=sum c_j X^j uses RAW traces. There are NO automatic
connected-cumulant subtractions in O7/O8. Introducing them changes the expression
unless every accompanying disconnected product is also restored. Filtering and
matrix-path multiplication do not supply scalar independence.

On exact-diagonal leading prime labels, only pairings survive (four distinct
balanced prime pairs at eight); higher leaf multiplicities are o(1) as above.
This is a Gaussian LEAF pairing rule, not the assertion that the limiting
spectral random variable is a scalar Gaussian. Different pair placements have
different path weights. The connected-cycle operator cumulant is also different
from a scalar trace-distribution cumulant; no identification is made.

An explicit class check uses the full R1 diagonal moments, in x:
 M2=1/6-4x;
 M4=1/12-(8/3)x+32x^2;
 M6=5/72-(7/3)x+42x^2-414x^3;
 M8=35/432-(8/3)x+(164/3)x^2-(2708/3)x^3+(65336/9)x^4.

Odd diagonal moments vanish. The scalar inverse partition expansion is
kappa8=M8-28 M6 M2-35 M4^2+420 M4 M2^2-630 M2^4.
Its exact result here is
 kappa8=4x/9-824x^2/9+8240x^3/3-190696x^4/9 <0.
It is NONZERO. The classes {8},{6,2},{4,4},{4,2,2},{2,2,2,2}
and their inverse coefficients are tracked by that identity, not assumed
to have equal geometric integrals. At R0 these moments are scalar Gaussian
and kappa8=0, an exact special cancellation that does not extend by analogy.
No theorem says this scalar kappa8 is the connected O8 sector, or that its
subtraction removes the open block in the polynomial. No additional cumulant
cancellation is removed from the raw residual.

## 5. What can actually be subtracted

Exact nonzero aliases extend the previous absolute proof to b<=8. If X^m is
irrational the exact population is empty. Otherwise X^|m|=a/b in lowest terms;
exact products are ak,bk. Bounded filter factors, theta<=1 and fixed-degree
prime/power factorizations give
 O_R((1+L)^9 X^-1/2)=o(1)
uniformly in heights tuned to exact aliases. This requires no useful carrier
oscillation and includes power-containing alias populations.

On ordinary open words subtract exact diagonal D_n(R), D7=0,D8=D8_open(R),
and exact nonzero aliases. The canonical 1/6 closed block was already excluded
by definition; subtracting it AGAIN would double count. Define precisely

 O_n^res,ordinary(T,R)=O_n^ordinary(T,R)
        -O_n^exactdiag,ordinary(T,R)-O_n^exactalias,ordinary(T,R).

This is the exact sum of central nonexact, near-alias, transition and far
ordinary populations. The full scalar satisfies
 O_n^ordinary=D_n(R)+O_n^res,ordinary+o(1).
Short-product restricted cells admit their inherited estimates below. No
uncertified closed-diagonal NUMBER is booked into a paid R6000 ledger.

The original sixth-degree proper-power theorem is a COMPLETE bounded signed
gate equivalence, not unconditional masked o(1). For this degree-eight witness
c8>0, a finite upper bound for its full polynomial trace forces bounded eighth
Schatten norm by coercivity; proper powers then have normalized eighth norm
O_R(L^-1/4) and Holder yields o(1) in the whole polynomial. That conditional
gate reduction can be used BEFORE partitioning, not as o(1) of O7/O8 separately.
Outside such a gate, nonexact power-containing open pieces remain explicit debt.
The only unconditional power pieces removed here are exact diagonal and exact
nonzero aliases. This is a scope correction to the requested 'remove closed
proper powers' shorthand, not a reopening of the frozen sixth-degree theorem.

## 6. Exact old-to-new masked map and the Delta phase

Restrict an old distinct-prime closed b-word, b=5 or 6, to all lags zero and
the actual hard prime/sign windows: fifth 2:3 around .6,.6 versus .4,.4,.4;
sixth 2:4 or 3:3 in a retained supercritical cell. Choose a new pair prime
with alpha_p in J=[1/8,1/6], disjoint from all these lower windows. For sixth
cells whose windows intersect J, choose another disjoint compact pair window
with a nonzero covariance; no universal window is assumed.

Insert the new pair first with lags (1,1), both sign orientations. Change the
first and third lower lags from 0 to -1. The higher word has total lag zero,
spread 2 and only the new cancelling prime pair, so theta_open=1. It is outside
the reserved canonical subset. Its deletion has Delta=-2. The carrier is
EXACTLY the original lower carrier, for each finite T and each prime tuple.
The map is injective on this masked old population: remove the first pair,
restore those two lags and retain the lower prime/sign labels.

The higher lower-leaf root offsets before the slots are (2,1,1,0,0) at five,
(2,1,1,0,0,0) at six. The pair's two orientations sum EXACTLY to

 C_T,J=2 sum_(alpha_p in J) c_p^2 |f1(alpha_p)|^2 cos(2pi alpha_p).

By PNT after this same-prime reduction it tends to
2 integral_J alpha |f1(alpha)|^2 cos(2pi alpha) d alpha.
On J this is positive and bounded below by
(49/7744)(7/1152)=343/8921088.
It is bounded above by 2 sum c_p^2=O(1). The disjoint windows ensure there
are no repeated-label corrections or prime-dependent deletion multiplicities.
The exact finite expression factors C_T,J out of the remaining prime sum.

The remaining old-weight multiplier is

 M(alpha,eps)= [f_-1^eps1(alpha1)/(1-alpha1)]
              [f_-1^eps3(alpha3)/(1-alpha3)]
       exp(2pi i[2 eps1 alpha1+eps2 alpha2+eps3 alpha3]).

On compact hard windows away from alpha=0,1 it is bounded and bounded away
from zero in modulus. It has no T-growing frequency. The root kernel is the
same carrier-bearing sampled kernel on the exact shortened common interval
of d'-2 roots; endpoints are not silently erased. Thus the embedded cell is
exactly a FILTER-WEIGHTED OLD restricted-prime correlation with a bounded,
nonzero smooth multiplier and the same lambda. It is category A/B at the
MASKED level (bounded multiplier with extra bounded Fourier phase), not a
shorter-shift category C. The constructor checks the closed lift, preserved
carrier, unique mark and defect at both orders. It does not replace a weighted
correlation by an unweighted one.

Original product n~X^(6/5) in the fifth cell still obeys the exact central
condition n exp(-H/T)<=B<=n exp(H/T); shift is nH/T~n^(1/6)H.
The new prime cancels in lambda and does not shorten this product or shift.
The extra average is C_T,J, a nonzero O(1) coefficient, not a vanishing factor.
Trace index still carries exp(i(T+hi)lambda). Insertion positions and lags
form finite sums at fixed R; no growing averaging parameter appears. The
pair phase cos(2pi alpha) is positive in this window, not a saving.

IMPORTANT LIMITATION: an embedding of a masked correlation in a signed sum
does not imply that every bound for the COMPLETE signed open sum bounds that
masked correlation. Other masks can cancel it. Extraction needs a bounded
projection/dual on the actual oriented discrepancy functional, which is not
supplied. Nor does this single zero-lag mask represent the entire old hard
vector. Therefore the user's proposed embedding-to-universal-hardness
inference needs an additional theorem. No equivalence/inferiority verdict is
claimed from this masked construction alone.

## 7. Estimates against the frozen residual

The first method whose hypotheses match the full arithmetic OBJECT is oriented
summation by parts. On every signed cell/bin let nu carry theta W exp(i tau0 xi)
(and its alias phase), and let E(x) be its difference from a justified comparison
primitive. Abel gives the exact sufficient bound
 Phi(E;a,b)=|D(b)E(b)|+|D(a)E(a)|+integral_a^b |E(x)| |D'(x)|dx,
 D(x)=D_d'(x/L), with the actual path root interval when required.
It transfers an ESTIMATE for the unknown primitive; it does not establish one.
There is no proved uniform residual discrepancy to put into Phi at long length.

Hilbert/Montgomery-Vaughan/large-sieve tests use the actual tuple-product
coefficients after retaining the finite filter paths and root masks. Fixed
R yields bounded coefficient square masses for a fixed product degree; the
ordinary short-cell absolute row bound has error of shape
 O_R((1+L)^C[sqrt(UV)/T+X^-1/2]).
The masked multiplier and theta<=1 cannot improve that absolute estimate.
It closes fixed-gap product cells with log U/L+log V/L<2, but in the old
balanced cell U,V~X^(6/5), sqrt(UV)/T~X^(1/5), not o(1). Grouping the
cancelled pair first returns the same old length, not a new saving.

Fejer majorization can yield positive-kernel coefficient norm bounds but
loses the carrier-bearing signed main term; no small norm at the required
length is supplied. Discrete Fourier duality is an exact reformulation of
the sampled kernel; no orthogonality separates deletion Delta after repair.
A divisor-shift estimate would have to accept restricted prime factors,
ordered filter weights, n,h dependent carrier phase and this oriented average.
A weak LRSC dual would require an actual bounded functional isolating the hard
masked cell or paying the signed primitive. The sharp commutator rank identity
does not construct it. None of these tests presently supplies the long residual
o(1) or a paid numeric bound. The best applicable estimate closes only the
already-short region and exact cases above.

## 8. Primary literature audit, after freezing the exact residual

[Topacogullari, The Shifted Convolution of Divisor Functions](https://arxiv.org/pdf/1506.02608),
Theorems 1.1/1.2, treats unrestricted d3(n)d2(n+h) with h<<n^(2/3).
That shift range includes the numerical old n^(1/6) scale, but the theorem's
coefficients and smooth weights do not include the resolved restricted-prime
factor weights and carrier-bearing n,h kernel here. A nonnegative unrestricted
majorant is not the required normalized signed asymptotic.

[Baier--Browning--Marasingha--Zhao, Averages of shifted convolutions of d3](https://arxiv.org/pdf/1101.5464)
studies first/second averages of unrestricted ternary divisor correlations.
It does not establish the oriented prime-factor-restricted primitive of this
residual. Extra pair averaging here has already reduced to C_T,J; it does
not supply the missing unweighted shift average by itself.

[Matomaki--Radziwill--Tao, Divisor correlations in short ranges](https://arxiv.org/abs/1712.08840)
gives almost-all-shift results for specified divisor/divisor and Mangoldt/divisor
coefficient sequences. Almost-all-shift control does not automatically bound
this weighted oriented sum, including exceptional shifts and factor windows.
[Topacogullari's generalized divisor paper](https://arxiv.org/abs/1605.02364)
and [Lau's smoothed generalized-divisor paper](https://arxiv.org/abs/2509.07556)
also concern stated unrestricted divisor sequences; no extension to this exact
filter/prime restriction is inferred. These are bounded hypothesis mismatches,
not a theorem that all current or future number theory fails. No nonprimary
search result is used as proof. No result found here closes the exact residual.

## 9. Complete signed consumer and exact ledger boundary

Recover the exact witness from the frozen JSON. Its q coefficients are
(-708647100/6882128371, 3565290899/13764256742,
 137641000/222004141, -5106481100/6882128371,
 137641/13764256742).
G=aa^t is exactly PSD, c4=0, and all coefficients of q(-1-y)-1 are
nonnegative, as certified in the preceding audit. The certificate copies
EVERY c0,...,c8 fraction without rounding. In particular

 c5=-87154293740347770741/94727381829846227282,
 c6=26076736521048521000/47363690914923113641,
 c7=-702861165085100/47363690914923113641,
 c8=18945044881/189454763659692454564.

Keep the signed target as the COMPLETE polynomial sum with its lower terms:
 c0+c1 tau X+c2 tau X^2+c3 tau X^3
 +c5 tau X^5+c6 tau X^6+c7 tau X^7+c8 tau X^8.
The signed open residual is c7 O7^res+c8 O8^res, together with c8 D8_open(R)
and all other closed/new sectors; do not separately absolute-value it as a
new target. Canonical lower amplitudes have coefficients c5+k_T c7 and
c6+k_T c8. This witness has tiny positive ratios c7/c5 and c8/c6, not -6;
these coefficients do NOT cancel even the canonical component. No missing
pair-lift payment is treated as zero.

Its relaxed completion gives E=0.10205420488978459 and uncharged coefficient
0.7958915902204308. Those completion mu7/mu8 are NOT actual model moments.
The exact hypothetical uncharged defect allowance is
8528806512359665159693267/2895247698247420090647048000.
The known inherited variance upper payment alone is
32242676406427306183391/15756336965594727445610547000,
leaving partial allowance
105010427619399283011381545483/35672346890106462936862278408000.
These values and the support/SOS certificate are copied in the new JSON.

There is NO true fully paid allowance before mu7/mu8: the degree-eight band
curvature/functional comparison and selected-section order-seven/eight transfer
are not certified by the old cubic constants. Canonical remainder and closed
pair terms are not numerically paid. D8_open(6000) is an explicit known formula
but not evaluated here; model/geometry substitution and actual seventh/eighth
law are still unproved. Support and c4 produce zero algebraic deficit; known
lower o(1) gates remain separate from finite band/variance/geometry costs.
The user-requested 'true budget' therefore cannot be assigned a positive number
without inventing theorem inputs. Record fully paid budget UNCERTIFIED.

## 10. Requested conclusions

1. Full O7/O8 formulas: Section 1, all ordinary and power leaves retained.
2. Exact diagonal: O7=o(1), O8=D8_open(R)+o(1); full finite covariance sum.
   Full signed R1 diagonal positive; R6000 sign/number not evaluated.
3. Cumulants: raw consumer has none to delete; scalar R1 kappa8 is nonzero.
4. Closed removals: exact diagonal/power-diagonal and exact nonzero aliases;
   canonical excluded once; nonexact power masking not unconditionally removed.
5. Residual: central nonexact, near alias, transition, far, plus nonexact
   powers unless complete bounded-eighth gate reduction is made first.
6. Old relation: exact nonzero bounded-multiplier masked lift retains lambda,
   old shift and product restrictions; full aggregate equivalence unproved.
7. Delta saving: none established; no new T-frequency or growing average.
8. Best matching method: oriented Abel reduction; generic short-length MV
   closes only fixed-gap short cells, not the hard residual.
9. Exact witness: all coefficients/support/Gram copied, with c5..c8 above.
10. Paid budget: UNCERTIFIED; only relaxed uncharged/partial-variance ceiling.
11. Hardness: no proven strict gain; not an equivalence or hardness theorem.
12. mu7/mu8 NO-GO: arithmetic feasible region and easier debt not certified.
13. Strict >79 OPEN; path-dependent weights still require a new zero-side theorem.
14. Local commit is reported in final response, retaining parent source hashes.

Artifacts: src/wp84_repaired_open_signed_arithmetic.py (constructor, normalized
residual inventory, masked lift, signed ledger); src/wp84_repaired_open_diagonal.py
(complete fixed-R pairing/covariance enumerator); src/wp84_repaired_open_signed_replay.py
(independent all-permutation pairing and exponential-integral replay);
notes/WP84_REPAIRED_OPEN_PATH_SIGNED_CERTIFICATE.json (exact outputs/scopes).
The scripts intentionally do not label R1 as R6000 or a relaxed completion as
actual mu7/mu8. Independent 105-pairing replay and two corruption tests PASS.
All previous local commits and NotebookLM packet preserved. No push.
