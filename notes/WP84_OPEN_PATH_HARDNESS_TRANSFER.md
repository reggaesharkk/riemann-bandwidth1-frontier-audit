# Open-path hardness transfer: resolved projection versus scalar quotient

Parent cb3c859958ce9ae75d976ec911193465a39a03be. Isolated branch
codex/c5-c6-attack-20261006; no push. Decision F and earlier falsifiers stay
frozen. No new consumer, actual mu7/mu8 integration, order-ten work or new
literature search is undertaken.

**Decision E: INCONCLUSIVE.** First missing estimate: a mask-extraction bound
on the actual carrier-aggregated, oriented discrepancy functional (or a complete
signed cancellation identity on its physically constrained prime amplitudes).
A labelled projection is constructed exactly, and a rational quotient-dual
certificate proves that this projection does NOT descend to the scalar/carrier
observable on the free resolved space. This is not an impossibility theorem on
the actual constrained arithmetic vector. No full-block hardness transfer is
claimed. No exact cancellation of the embedded arithmetic cell is established.

## 1. Frozen complete signed residual and hard mask

Keep L=log(T/(2pi)), N=floor(exp(L-sqrt L)), h=2pi/L,
I=[k_-,k_+], d'=|I|~floor(TL/(2pi)), R=6000 and a_phi->1.
At order n=7,8 every index alpha consists of all prime-power leaves
n_j=p_j^v_j<=N, signs eps_j, closed lags l_j in [-R,R], sum l_j=0,
root i in I, all partial sums u_j, all intermediate masks 1_I(i+u_j),
ordinary-prime deletion mark (s,t), its defect Delta=-(l_s+l_t),
carrier lambda=sum eps_j log n_j, section/endpoints and filter labels.

Use c_n=-log(base prime)/(a_phi L sqrt n), alpha_j=log n_j/L and the exact
filters f0=1-alpha, f_l^+=(1-exp(2pi i l alpha))/(2pi i l), f_l^-=conjugate f_l^+.
Reserve the canonical final ordinary zero-lag pair subset once. For other
words let D be the number of ordinary opposite-sign same-prime pairs; use
1/D for each open deletion mark. If D=0 there is no pair contribution.

For each resolved ROOT and open mark define
w_alpha=(gamma_n/D) prod_j c_nj f_lj^epsj(alpha_j)
 exp(2pi i sum_j eps_j u_(j-1)alpha_j)
 prod_j 1_I(i+u_j),
where gamma_7=c7 and gamma_8=c8 are the consumer coefficients, distinct
from the leaf coefficients c_nj.
The observable is F_alpha=d'^-1 exp(i(T+h i)lambda).
Thus the complete consumer open residual is

 R_open=sum_(n=7,8) sum_(all retained nonexact nonalias ordinary alpha)
               w_alpha F_alpha,

with the conditional proper-power gate and exact main terms kept as the
separate statuses from the parent. Equivalently ordinary
R_open=c7 O7^res+c8 O8^res. Restoring nonexact power-containing words is
required unless the complete bounded-eighth signed gate reduction is used
BEFORE masking. Every root/insertion/filter/path restriction is present.
No new cumulant subtraction or continuum replacement is introduced.

The hard mask M at order seven selects: distinct lower ordinary prime labels
with signs 2:3 and exponent windows around (.6,.6;.4,.4,.4), their frozen
central/dyadic product cell, fixed lower slot ordering and original zero lags;
a new pair prime in J=[1/8,1/6], disjoint from lower windows; pair slots first,
pair lags (1,1), both sign orientations; altered lower lags (-1,0,-1,0,0).
The sole deletion pair is new and has Delta=-2; reserve-canonical exclusion
never applies. The order-eight mask has lower 2:4 or 3:3 distinct-prime cells
and altered lags (-1,0,-1,0,0,0). These are specific masks, not the entire old
hard sector. Include adjoint masks when requiring a real scalar.

## 2. An exact labelled projection, with its actual norm

Let X_res be the vector space of fully labelled residual amplitudes BEFORE
carrier/path aggregation. Pi_M is its coordinate mask. It has operator norm
<=1 in resolved total variation (and in a counting l2 norm). With all label
conditions above, non-M populations surviving Pi_M are NONE, by definition.
Both pair orientations are in M. Repeated prime/power populations are excluded
by explicit labels, not by an unproved analytic estimate.

Sum the selected pair prime first. Its exact factor is
C_T,J=2 sum_(alpha_p in J) c_p^2 |f1(alpha_p)|^2 cos(2pi alpha_p).
PNT after same-prime reduction gives C_T,J->C_J>0, with
C_J>=343/8921088. Pair roots/carrier cancel, and disjoint windows make this
factor independent of every lower prime label without deletion multiplicity
corrections. The remaining multiplier is

M(alpha,eps)=f_-1^eps1(alpha1)/(1-alpha1)
            *f_-1^eps3(alpha3)/(1-alpha3)
            *exp(2pi i[2 eps1 alpha1+eps2 alpha2+eps3 alpha3]).

The root interval is exactly I with its last two points removed. No sampled
kernel quotient is formed at a zero of D. Define H_old^trim as the old ordered
zero-lag masked hard correlation on those roots, with its exact prime windows
and carrier phases. Multiply each labelled lower contribution by M^-1 and
sum the selected pair labels, then divide by C_T,J (and c7 if operating on the
consumer-scaled vector). This defines an EXACT linear map at each fixed T:

 Pi_hard(X_res)=H_old^trim.

Alternatively before division by C_T,J its value is C_T,J H_old^trim. The
projection kernel uses finite filter data and actual prime/window labels; it
is not a scalar multiplication on R_open. T dependence of C_T,J is explicit.

On alpha1 in [11/20,13/20], alpha3 in [7/20,9/20], sin(pi alpha)>=
2 min(alpha,1-alpha) and pi<22/7 give
|f_-1(alpha1)/(1-alpha1)|>=49/99,
|f_-1(alpha3)/(1-alpha3)|>=49/143,
so |M|>=2401/14157. Eventually C_T,J>=343/(2*8921088).
A valid resolved-TV inverse bound, BEFORE consumer-coefficient division, is

 C_TV=2*(14157/2401)*(8921088/343).

This exact rational is recorded in JSON. For consumer-scaled order-seven
coordinates multiply C_TV by 1/|c7|, which is finite but large for the frozen
witness. Therefore a theorem supplying a RESOLVED-TV discrepancy eps would
imply a bound C_TV eps for this trimmed hard mask. This is a true conditional
transfer in a stronger norm. The available theorem target controls a signed
scalar/primitive, not resolved TV. No resolved-TV theorem is available at the
natural product length.

Recovering the FULL frozen H_old needs more: other lag/order masks and the two
removed root contributions. The inherited unmasked good-endpoint compression
bound is not automatically an absolute bound for a prime-product-window masked
root sum. Masking can destroy cancellations that bounded the original local
field. No o(1) masked endpoint remainder is invented. Even a resolved transfer
for H_old^trim would not by itself prove the requested full H_old theorem.

## 3. Exact criterion for a projection on the complete observable

Let S:X_res->Y be the aggregation actually controlled: scalar trace, or the
carrier-bearing primitive after summing all amplitudes at each carrier/root.
For Pi to factor as Pi=B S, it is NECESSARY and (algebraically on ran S)
SUFFICIENT that ker S subset ker Pi. Boundedness additionally requires
||Pi x||<=C||Sx|| in the specified norm.

This test is exact. A label mask on X_res is not automatically a functional
on the scalar R_open. On C every linear map is multiplication by a constant;
it cannot recover an independently labelled masked contribution from its sum.
Frequency/carrier data are richer than one scalar, but still forget path data.

The rational dual certificate uses two admissible repaired-open ROOT states
with the SAME carrier and root:
M: pair (+5,1),(-5,1), remaining
 (+379,-1),(+401,0),(-47,-1),(-53,0),(-61,0);
B: pair (+5,-1),(-5,-1), remaining
 (+379,1),(+401,0),(-47,1),(-53,0),(-61,0).
At root 5 and section [0,30] both closed paths stay inside the section, have
unique ordinary cancelling pair and open deletion. Their defects are -2,+2.
Their reduced carrier is exactly (379*401)/(47*53*61). These are exact labels,
not a numerical model kernel. On any sufficiently long selected section use
an interior root; the illustrated [0,30] does not certify a natural-height
good-section choice. Filter factors and normalizations are incorporated into
the amplitude coordinate, leaving the common carrier/root atom unchanged.

On their two-dimensional free contribution space,
 S=[1,1], Pi_M=[1,0], z=(1,-1).
Then S z=0 but Pi_M z=1. Thus Pi_M does not factor through S, and there is NO
finite C satisfying |Pi_M x|<=C|Sx| on that free space. For the carrier measure,
both atoms occupy identical lambda/root, so the aggregated primitive E is zero
and its oriented Abel functional Phi is zero, while the masked measure is
nonzero. Adding adjoint states gives the same obstruction in a real
adjoint-invariant space. Any attempt to isolate them by carrier support alone
retains B as potential cancellation. The exact integer/rational check is
independently replayed, including corruption rejection.

SCOPE: z is an arbitrary variation of resolved contribution amplitudes, not a
claim that actual prime coefficients at one height equal (1,-1). The free-space
countercertificate falsifies automatic boundedness/inherited mask extraction.
It does NOT rule out an arithmetic theorem imposing additional structure on
actual coefficients, nor does it prove that their B contribution cancels M.
A physical-vector extraction inequality is the first missing estimate.

## 4. Who enters a coarse projection? Complete sign/multiplicity ledger

A FULL label mask Pi_M keeps no unwanted populations. A COARSE carrier/prime-cell
projection keeps every closed repaired path and insertion arrangement with that
same carrier. Its additional populations are **POTENTIAL CANCELLATION**, with
no estimate yet showing they are controlled or have smaller hardness. Exact
ordinary diagonal and aliases have already been removed and are not counted
as new competitors in the nonexact hard cell. The unique new pair and distinct
lower primes make multiplicity exactly one per higher word in this family.

For b distinct lower labels/signs and a separately labelled pair +/- leaf,
let a_b(R)=[z^0](sum_(l=-R)^R z^l)^b. There are (b+2)! leaf arrangements.
For any fixed pair positions/orientation the closed higher lag count is
 a_(b+2)(R),
closed deletion lag count (2R+1)a_b(R),
open deletion lag count a_(b+2)(R)-(2R+1)a_b(R).
All labelled pair leaves are distinct as signed labels; (b+2)! already includes
both orientations and all insertion positions and b! lower permutations.
Do not multiply by a second 2 binomial(b+2,2).

At b5,R1: a7=393, closed-delete=153, open-delete=240;
there are 5040 arrangements and 1,209,600 open channels before root masks.
At b6,R1: a8=1107, closed-delete=423, open-delete=684;
40320 arrangements give 27,578,880 open channels. R0/R2 counts are in JSON.
They are checked independently by Cartesian-product counts, not the producer's
coefficient recurrence. Repeated labels require D-weighting and are handled by
the full formula; these counts explicitly describe the distinct-label family.

Every term's exact ledger is:
- multiplicity: 1 for this family, or open mark weight 1/D in the full residual;
- raw cumulant coefficient: 1, because the consumer is a raw polynomial;
- leaf coefficient sign: (-1)^7 at seventh order, (-1)^8 at eighth;
- consumer sign for the frozen witness: c7<0, c8>0;
- filter/path factor: prod f times exp(2pi i sum eps u alpha), retained exactly;
- carrier factor: exp(i(T+hi)lambda), retained exactly;
- endpoint/root factor: product of section masks, or its exact admissible sum.
The coefficient after multiplying leaf and consumer signs is positive in both
orders, but the remaining factor is COMPLEX and need not have a positive real
part. A sign table or channel count does not prove leading cancellation or
noncancellation. All competitor populations sharing the carrier are summed by
this explicit finite ledger; their total is not replaced by the selected factor
C_T,J. No full leading coefficient for that entire hard family is certified.

## 5. Cancellation mechanisms tested

Pair sign symmetry: in M it produces 2|f1|^2 cos(2pi alpha_p), positive on J,
so it does NOT cancel this mask. Other pair positions have other factors.

Carrier conjugacy: adjoint/reversal combines A(lambda), A(-lambda) to a real
2 Re[exp(iT lambda) A(lambda)]. It is not an identity saying that real part
vanishes for all T. It does not supply a mask-extraction inequality.

Displacement reversal: B has the same carrier and opposite defect, but its
filters and moved phases are different. It provides potential same-atom
cancellation, not a proof of exact negatives at actual alpha.

Cumulant Mobius: no such subtraction occurs in the raw c7/c8 polynomial.
Introducing it would require restoring all disconnected terms. The previous
complete R1 scalar diagonal kappa8 is nonzero, so no general Gaussian-leaf
argument supplies the desired cancellation identity.

Insertion telescope: the marked incidence relation is a finite sum, not an
established telescoping divergence. The complete path factors and section
restrictions prevent treating slots as equal copies of the canonical lift.
No identity proving its full hard-cell coefficient zero was found.

Endpoint cancellation: M and B can occur at interior roots; zero endpoint
support is falsified. No weighted boundary theorem proves that their masked
scalar is an endpoint remainder.

The complete signed hard-cell amplitude therefore remains the explicit finite
sum. Neither 'total coefficient zero' nor 'total coefficient nonzero and all
remainder controlled' is certified. The kernel-dual theorem explains why a
label-based extraction cannot be promoted without additional arithmetic input.

## 6. General fixed-R diagonal: reused exact covariance certificate

The preceding full ordinary exact-diagonal reduction is retained. Odd ordinary
order-seven diagonal is exactly zero; balanced power-containing exact-diagonal
groups are o(1). Order-eight leading groups have four distinct opposite-sign
prime pairs; higher ordinary collisions are o(1). PNT may be applied AFTER
that equality reduction, with measure alpha d alpha.

For x=-1/(4pi^2), pair covariance is
 C(0,0,0)=1/6;
 C(0,0,d)=2x/d^2 (d!=0);
 C(l,0,d)=C(0,m,d)=0 when exactly one lag is nonzero;
 C(l,m,d)=-x/(lm)[delta_d0-delta_(d+l)0-delta_(d-m)0+delta_(d+l-m)0]
   when l,m!=0.
For all closed l in [-R,R]^8 and all 105 pairings pi, let q count the pairs
with lag sum nonzero and r indicate the reserved last-zero-lag pair. Then

 D8_open(R)=sum_l sum_pi (1-r)(q/4) prod_(j,k in pi)
                         C(l_j,l_k,u_(j-1)-u_(k-1)).

This is the COMPLETE finite covariance sum for arbitrary fixed R and the
established asymptotic main term. It has exact rational coefficients as a
polynomial in x, degree <=4. It is not claimed to be a positive Gram functional:
the open mask, canonical reservation and complex Fourier covariances do not
preserve positivity term by term. A Gaussian Gram representation for the FULL
unmasked moment does not certify the open subset's sign.

The exact regression, independently replayed here, is
 D8_open(1)=(373/36)x^2-(1293/4)x^3+(36130/9)x^4>0.
At R0 it is zero. The sign of D8_open(6000) is NOT evaluated and not inferred
from R1. No brute-force R6000 run is launched; the sparse delta constraints
are available for a future efficient summation theorem. The diagonal does
not currently rule out the degree-eight witness. Its numeric main term would
also need the complete paid scalar ledger to support Decision D.

## 7. Norm needed for a full-block hardness theorem

A valid resolved-TV transfer has been obtained for ONE trimmed/masked hard
correlation, with explicit constant above. The requested ACTUAL theorem would
need an inequality such as

 |H_old - H_comparison| <= C * N_actual(R_open - R_comparison)+o(1),

where N_actual is the signed/oriented primitive functional used by the frozen
consumer gate, with all path/order weights and no new absolute TV requirement.
It would have to control the competing same-carrier populations and masked
root/lower-word extension errors. The kernel test shows that no such inequality
can follow solely from free labelled algebra or a scalar estimate of R_open.
It could still follow from a NEW arithmetic extraction theorem on physical
prime coefficients. No such theorem or exact complete cancellation identity
is currently proved. This is the first missing estimate, not a numerical
uncertainty in the already-selected nonzero C_T,J.

A dual phi that tests labelled coordinates is legitimate in X_res^*, but it
is not automatically in the dual of the quotient observable norm. The same
kernel criterion forbids this descent without extra hypotheses. This prevents
an artificial 'weak dual' from silently importing the stronger TV theorem.

## 8. Budget, restrictions and final decision

Model/arithmetic intersection remains UNCERTIFIED. Accordingly no new paid
allowance is computed, and the uncharged relaxed 79.5891590 coefficient is
not used as a theorem margin. No actual mu7/mu8 computation, new consumer or
order-ten work is performed. Scalar spectral zero-side consumers remain the
existing class; path-dependent zero-side weights require a new theorem.

No new literature search: the residual is unchanged, and the unresolved gate
here is mask extraction/full cancellation, not a newly shorter shifted object.
The prior restricted-prime correlation audit remains the literature boundary.

Requested verdicts:
- Labelled projection exists and is bounded in resolved TV.
- Complete scalar/carrier projection does NOT factor on the free space.
- Coarse projection competitors: potential cancellation, uncontrolled.
- Full signed leading hard-cell coefficient: not certified zero or nonzero.
- Actual full-block hardness transfer: NOT PROVED.
- Exact complete cancellation: NOT PROVED.
- General-R diagonal: exact finite covariance main-term formula; R1 PASS;
  R6000 sign/value unevaluated.
- Paid budget UNCERTIFIED; mu7/mu8 deferred; strict >79 OPEN.
- **Decision E. First missing estimate is physical-vector mask extraction or
  a complete cancellation theorem in the actual aggregate functional.**

Artifacts:
src/wp84_open_path_hardness_transfer.py: exact projection factorization/dual
certificate, same-carrier states, full population ledger, rational constants
and pinned source blobs.
src/wp84_open_path_hardness_transfer_replay.py: independent UF, complete counts,
constant and quotient-kernel replay; three deliberate corruptions rejected.
Reused src/wp84_repaired_open_diagonal.py and
src/wp84_repaired_open_signed_replay.py: arbitrary-R covariance construction and
independent R1 full signed diagonal regression. Their source blobs are pinned
in WP84_OPEN_PATH_HARDNESS_TRANSFER_CERTIFICATE.json. No duplicated integration
engine is introduced. Both replays PASS.

The local commit hash is reported in the final response. Earlier audit commits
and notebooklm_packet remain preserved. No push.
