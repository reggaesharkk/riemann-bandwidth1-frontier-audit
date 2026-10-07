# Augmented open-path pair transfer

Parent 484769f9dd226ccc8a1ca2e5f335075415c727b2, branch
codex/c5-c6-attack-20261006. Local audit only; no push. All earlier decisions
and falsifiers remain frozen. The dead quartic is not reopened. Actual mu7/mu8
are not integrated.

**Decision F: INCONCLUSIVE.** First uncertified step: quantitative control of
the carrier-bearing, filter-weighted signed OPEN-DELETE block after it is
closed by pair insertion, on the actual selected section. The exact finite
incidence and observable formulas below do not supply this estimate. No
universal scalar obstruction or >79 theorem is asserted.

New exact results: all defect channels and marked insertion/deletion algebra;
trace-before-insertion versus trace-after-insertion distinction; a normalized
positive exact-diagonal order-eight population with open deletion defects,
showing that automatic trace annihilation, 1/d suppression and endpoint-only
support are false. This population is not a lower bound for the entire signed
open block and is not a proof that the hard near-product block is nonnegligible.

## 1. Exact augmented spaces for b=5 and b=6

Freeze L=log(T/(2pi)), N=floor(exp(L-sqrt(L))), h=2pi/L,
d=floor(TL/(2pi)), selected I=[k_-,k_+], d'=|I|~d, fixed R=6000,
a_phi->1, c_p=-log(p)/(a_phi L sqrt(p)). Ordinary primes only in this pair
analysis; previous proper-power gate status is inherited, not a new per-cell
absolute power estimate.

A basis state is eta=(T,L,R,I,a_phi,i; (p_j,eps_j,l_j)_(j=1)^b),
u_0=0, u_j=sum_(k<=j) l_k, initial index i, terminal index i+u_b,
Delta=u_b, |l_j|<=R. Retain every intermediate node i+u_j and its projection
mask 1_I(i+u_j), all leaf filters, signs, prime labels, carrier exponent vector
e_p=sum_(j:p_j=p)eps_j, lambda=sum eps_j log p_j, and root i in I.
The pair-deletion augmentation needs -2R<=Delta<=2R. Closed means EXACTLY
Delta=0, open means Delta!=0. These definitions apply separately at b=5,6.

The augmented space also retains deletion skeletons with intermediate nodes
outside I; store the mask rather than discarding the state. A higher fully
projected word can have such a skeleton. This is a formal resolved tensor space,
not an assertion that unprojected skeletons are terms in the original trace.
Its raw coefficient is

 F_b^raw(eta)=d'^(-1) prod_j c_pj f_lj^epsj(alpha_j)
 exp(2pi i sum_j eps_j(i+u_(j-1))alpha_j), alpha_j=log(p_j)/L,
 f_0=1-alpha,
 f_l^+=(1-exp(2pi i l alpha))/(2pi i l), f_l^-=conjugate f_l^+.

The physical word coefficient multiplies its entire projection mask and
exp(iT lambda). The augmentation is finite at fixed T,R,I,N; the dimension
grows with T. The builder records roots, terminal nodes, defects, masks and
carrier, and reuses the parent filter/channel definitions without changing
normalization.

## 2. Deletion is a marked map; unmarked allocation must be specified

For a closed higher word zeta, each pair of slots s<t with p_s=p_t,
eps_s=-eps_t is an admissible multiplicative deletion mark. Delete those
leaves and retain the remaining lags in order, with the same root. Exactly

 Delta_deleted=-(l_s+l_t).

The remaining partial sums are unchanged before s, shifted by -l_s between
s and t, and shifted by -(l_s+l_t) after t, with the obvious slot reindexing.
The remaining filter factors are retained and their root phases are recomputed.
This is a carrier-preserving deletion but need not be a projected closed word.
It lands in H_b^aug. Delta=0 iff l_s+l_t=0.

A word can have multiple cancelling pairs, possibly with BOTH zero and nonzero
deletion defects. Thus 'closed-delete plus open-delete' is not a disjoint split
of unmarked words until one specifies a convention. This is essential, not a
notational detail. On marked words the two classes are disjoint and complete.
For the unmarked pair sum we use either deterministic canonical allocation,
or weight each deletion mark by 1/D(zeta), D=number of cancelling slot pairs.
Then the closed/open fractions sum to one. They are amplitude allocation
fractions, not nonnegative mass fractions for general complex words.

To preserve the frozen canonical lift EXACTLY, reserve first the subset whose
last two leaves are opposite signs of the same prime with BOTH lags zero,
including both sign orders. Allocate all remaining words by the chosen rule.
Using a uniform 1/D over all marks without this reservation would change the
canonical subset's contribution when a prefix has other cancelling pairs.
All bounds and classifications here state which convention is used.

## 3. Exact insertion and the actual endomorphisms DI and ID

Insert at all slots s<t a prime p, sign eps, pair lags v,w in [-R,R],
retaining every lower label. The higher word is admissible iff
Delta+v+w=0 and every higher node is in I. Pair filters and phase changes
are the exact symbolic channel_factor in the parent builder; no lower
zero-mask or coefficient division is used. Its carrier is unchanged.

On the MARKED combinatorial spaces let D map each higher marked state to
its unique deletion skeleton. Let I=D^t for counting inner products. This
convention gives a complete incidence operator, and an actual graded
endomorphism DI on skeletons. If n_eta is the number of admissible insertion
channels above skeleton eta,

 DI=diag(n_eta),
 ID on each marked fiber = the n_eta by n_eta all-ones matrix.

Hence DI is diagonal, generally not scalar; ID is positive Gram-like,
rank one on each nonempty fiber, generally not a projection. ID has eigenvalues
n_eta and zero in that fiber. After normalization J=I diag(n_eta^-1/2) on
nonempty fibers, J is an isometry and JJ^t is a projection. These statements
are EXACT combinatorial algebra. They do not turn filter-weighted arithmetic
insertion into an isometry or supply a trace estimate.

The incidence-algebra unit replay checks two illustrative fibers with sizes 2
and 1; these are not claimed to be actual natural-height hard-cell blocks:
DI=diag(2,1), ID=[[1,1,0],[1,1,0],[0,0,1]].
It also enumerates actual R=1 repaired channels over an open five-skeleton.
For UNMARKED averaging, D has several nonzero entries in a higher-word
column, so DD^t need not be diagonal. With complex filter/phase weights,
the physical insertion is a weighted incidence map and is not generally the
adjoint of plain combinatorial deletion. Its compositions require those weights,
not the above n_eta eigenvalues. No hard-eigenvector claim is imported.

## 4. Every defect block and finite-R counts

All possible defects are integers -2R,...,2R. For fixed Delta, there are
exactly 2R+1-|Delta| choices of (v,w) with v+w=-Delta. Before projection masks,
per prime and per lower skeleton there are

 2 * binomial(b+2,2) * (2R+1-|Delta|)

marked channels, including both pair orientations. Multiply by the number of
allowed pair primes only if all are admitted by the chosen prime mask. At b=5
the prefactor is 42, at b=6 it is 56. Summing Delta gives
2 binomial(b+2,2)(2R+1)^2 across formal defect labels. A fixed lower
skeleton occupies only its own Delta block, not all of these at once.
The certificate independently brute-counts R=1,2.
Repeated prime labels introduce deletion-mark multiplicity D; do not confuse
these counts with distinct higher words or with coefficient-weighted sums.

For each higher path with offsets u, admissible roots are
[k_- - min u, k_+ - max u], with
m_u=max(0,d'-(max u-min u)). Thus exact endpoint-dependent counts use this
m_u, or individual root indicators if a skeleton root has already been fixed.
All pair positions and orientations are included. Fourier coefficients depend
on v,w and alpha_p, while moved lower phases depend on the entire ordered
path. No defect-only scalar reproduces these weights.

The canonical append component has v=w=0 and Delta=0. Its normalized
aggregate multiplier is EXACTLY k_T=2S0,T,
S0,T=sum_(p<=N)(log p)^2/(a_phi^2 L^2 p)(1-log p/L)^2 ->1/12.
It is a strict subset of closed-delete, not the complete closed-delete block.
Other Delta=0 channels can have v=-w!=0, interleaved insertions and different
skeleton projection masks.

## 5. Trace projection: the bare open word is zero, the repaired word is not

On physical augmented word tensors define

 L_b^trace(eta)=1_(Delta=0) exp(iT lambda) F_b^raw(eta)
                    prod_j 1_I(i+u_j),

and sum over all roots and states. This reproduces the actual trace, and
EXACTLY annihilates a bare open word. One may also define an off-diagonal
row average d'^-1 sum_i M_(i,i+Delta), but it is not a trace and should not
be used as an unproved zero-side observable.

The required observable on open skeletons is L_(b+2)^trace I_b. It is
NOT L_b^trace times a scalar and is not zero merely because L_b^trace=0.
Insertion repairs Delta and changes filters, phases and projections before
the trace is taken. For a fixed repaired higher path the root sum is exactly

 exp(iT lambda) prod_j c_pj f_lj^epsj(alpha_j)
 exp(2pi i sum_j eps_j u_(j-1)alpha_j)
 (m_u/d') exp(2pi i i_min lambda/L) D_(m_u)(lambda/L).

Here i_min=k_- - min u and D_m(z)=m^-1 sum_(k=0)^(m-1) exp(2pi i k z).
When m_u=0 the contribution is defined as zero. Delta no longer appears
as a trace Kronecker delta because the HIGHER word has total displacement zero.
The sampled kernel depends on the prime carrier lambda, not on the deletion
defect. It has no universal 1/d or 1/|Delta| factor.
At lambda=0 the root factor is m_u/d' ->1, not 1/d'.

For a single channel and Delta!=0, at least one of |v|,|w| is >=|Delta|/2.
The coefficient bounds |f_l|<=min(1,1/(pi|l|)) give a possible
2/(pi|Delta|) FILTER envelope, with the other factor <=1. This is not sampled
kernel orthogonality. At fixed R and fixed nonzero Delta it supplies no o_T(1).
The sums and arithmetic correlations still require control. Some channels
may vanish for special filter values or empty root intervals; no generic
annihilation of all open classes follows.

## 6. Exact normalized nonzero open-delete population

Take an order-eight word in this order:
(+p,1),(-p,1),(+q,-1),(-q,-1),(+r,0),(-r,0),(+s,0),(-s,0),
with four DISTINCT ordinary primes. Offsets are
(0,1,2,1,0,0,0,0,0), carrier lambda=0, and admissible roots number d'-2.
Its four deletion marks have defects (-2,+2,0,0). The displayed word ends with a zero-lag pair and is in the reserved canonical
subset. Uniform marked allocation nevertheless assigns half its marks to open
defects. For an example outside the reserved subset, rotate it cyclically to
start with the r pair, leaving the q pair last. The last two lags are then
-1,-1. This rotated word has the same trace, root count, carrier and deletion
defect multiset. The positive-population calculation uses the rotated word
when the canonical reservation convention is chosen; its open fraction is
still two of four marks.

Its normalized trace coefficient is
((d'-2)/d') c_p^2 c_q^2 c_r^2 c_s^2
 |f_1(alpha_p)|^2 |f_1(alpha_q)|^2
 (1-alpha_r)^2(1-alpha_s)^2 exp(2pi i(alpha_q-alpha_p)).
The carrier T phase is EXACTLY one. No oscillatory T averaging is needed.
One half is assigned to the two open deletion marks in uniform allocation.
The rotated version has the same trace coefficient by cyclicity (or direct
root reindexing). There is no endpoint-only support: d'-2 roots are interior.

Restrict alpha_p,alpha_q to J1=[1/8,1/6], alpha_r,alpha_s to
J2=[1/4,1/3]. Every such prime window is inside the natural cutoff eventually.
The real phase is bounded below because |alpha_q-alpha_p|<=1/24.
Using pi<22/7 and cos t>=1-t^2/2 gives cos>=3407/3528.
Using sin(pi alpha)>=2alpha for 0<=alpha<=1/2 gives
|f_1(alpha)|^2>=49/7744 on J1. On J2, (1-alpha)^2>=4/9.
The CLOSED prime-square/PNT measure theorem, applied only AFTER this exact
same-prime product reduction, gives
sum c_p^2 1_J(alpha_p) -> integral_J alpha d alpha.
Those masses are 7/1152 and 7/288. Coincident p=q or r=s have vanishing
mass because max c_p^2 in these positive exponent windows tends to zero and
total square mass is bounded; J1 and J2 are disjoint. Thus distinct-prime
restriction has the same limit.

Consequently the selected open-marked population has real liminf at least

 (1/2)(3407/3528)[(49/7744)(7/1152)]^2[(4/9)(7/288)]^2
 =400830143/4812249661301738962944 >0.

The exact rational bound is independently replayed. Its small numerical value
(~8.32937e-14) is NOT used as a budget estimate. It proves a nonzero population,
not a lower bound for the full signed open-delete block. Other populations may
cancel it. It does not prove the original hard 2:3 or sixth near-product cells
have nonzero limiting mass, and does not justify Decision D/E. It disproves
blanket per-population negligibility, trace annihilation and endpoint-only
support. Canonical dominance is not established by this example or any count.

## 7. Existing reprojection machinery: first hypothesis mismatches

WP84_FOURIER_REPROJECTION_BRIDGE_AUDIT bounds leakage across the SECTION
projection Q_I and deterministic sharp-word compression differences. A deletion
defect is not a Q_I insertion: the repaired higher path above stays in I at
d'-2 roots. Applying its leakage bound to Delta!=0 would conflate different
operators. It also does not justify weighted absolute prime aggregation.

WP84_FIXED_BAND_WEIGHTED_REPROJECTION closes selected-section compression
errors for b=5,6 using good endpoints and local linear-field mean squares.
Open skeletons produced by deleting a pair from order seven/eight are not
those compression errors. Their repaired words are bulk contributions.
The theorem's b0=6 hypotheses do not automatically certify new order-eight
consumer boundary charges at the same frozen endpoints.

WP84_TWO_SCALE_FILTERED_TO_SHARP_MOMENT_BRIDGE supplies model geometric
convergence as R grows after an arithmetic gate. Fixed-R open deletion is
neither a high-frequency filter tail nor an established arithmetic transfer.
It cannot replace the sampled kernel by a sharp overlap to dispose of the defect.

WP84_LRSC_DISPLACEMENT_RANK_CLOSURE supplies a sharp operator's rank-two
commutator with the Fourier index operator. It explicitly leaves trace-law
extraction OPEN. A path defect is not low ordinary rank, and fixed displacement
need not be endpoint-supported. The sharp rank-two relation does not assert
that a band-filtered repaired prime word has small trace. This is the first
hypothesis mismatch; no LRSC theorem is silently imported.

## 8. Fifth and sixth hard sectors: structural answer without fake fractions

v5 is the actual normalized, selected-section, closed five-word atomic measure
with prime/sign 2:3 windows near (3/5,3/5;2/5,2/5,2/5), central carrier window
|lambda|<=H/T, and the inherited dyadic product conditions. v6 comprises the
analogous unresolved 2:4 and 3:3 masks. The hard_mask routine is reused from
the parent with specified finite-T window parameters and exact/certified log
comparisons. No continuum proxy or invented prime counts are used.

Every literal insertion into a CLOSED lower hard state leaves lower Delta=0,
so closure of its higher word forces v+w=0. Such marked lifts lie entirely in
closed-delete for that particular deletion mark. This is an exact structural
answer: the old trace vector itself has no open coordinate. It does not imply
that every higher word with the same reduced carrier has a closed hard preimage.

For the same five-leaf prime/sign profile, put a new +u,-u pair first with
lags (1,1) and choose remaining five lags (-1,0,-1,0,0). This is an admissible
closed seven-path at an interior root; deletion of the new pair gives defect -2.
If all six prime labels are distinct except the inserted pair, it is the only
cancelling pair. Its lower prime/sign exponent windows can still be the hard
2:3 profile, and its carrier window is identical to that of those five primes.
This gives open-skeleton channels in the same hard prime-profile family.
It does NOT prove there exist sufficient prime near-collisions in that window,
or a positive fraction of actual asymptotic hard mass. That density is exactly
part of the unresolved arithmetic problem.

At order eight use the same pair (1,1) and remaining six lags
(-1,0,-1,0,0,0). Assign the remaining signs 2:4 or 3:3. The same assertions
hold. Repaired product sectors are 3:4 at seven, 3:5 or 4:4 at eight.
Their pair prime cancels in lambda but affects coefficient, phases and paths.
No structural fraction of signed mass is available. The canonical closed lift
covers its precisely reserved subset, not all closed-delete, and none of these
unique open-delete words.

## 9. Projected scalar ratios and the remaining arithmetic residual

For a fixed fully specified hard vector v, set x=L_b(v), y=L_(b+2)(I_b v).
For REAL scalar ratio a=c_(b+2)/c_b, if y!=0 then

 a_*=-Re(conjugate(y)*x)/|y|^2,
 inf_a |x+a y|^2=|x|^2-[Re(conjugate(y)*x)]^2/|y|^2.

For a complete adjoint-closed REAL trace, x,y are real, so a_*=-x/y cancels
that single evaluated scalar when y!=0. This is NOT a fixed asymptotic consumer
ratio theorem: x,y depend on T, cells and still-unknown arithmetic correlations.
If y=0 the residual is |x|. One ratio must serve every retained component and
a support-certified consumer, not be chosen after seeing T or unknown trace.

Under the reserved-canonical split, the COMPLETE same-carrier higher contribution
can be written k_T x+y_closed,rest+y_open. The scalar combination is
(c_b+c_(b+2) k_T)x+c_(b+2)y_closed,rest+c_(b+2)y_open.
The open term includes additional augmented inputs, not merely I applied to v
whose support is closed. This explicitly avoids omission of open sectors.
Optimal ratios in the actual theorem functional are UNCERTIFIED. No estimates
for x,y_closed,rest,y_open justify finite paid asymptotic cancellation.
The oriented primitive Phi(E;a,b) of the power-window note is a sufficient
absolute discrepancy functional; the scalar formula above is not its optimizer.

## 10. Bounds attempted in both directions

An exact finite upper bound for the open block is the sum of absolute repaired
root/path weights, with the selected open-mark allocation fractions. It can be
written without ambiguity as
sum_zeta theta_open(zeta) |prod c f| (m_u/d') |D_(m_u)(lambda/L)|,
with theta_open in [0,1], plus carrier phases of modulus one in the real sum.
This supplies no o(1) at the natural product lengths. Pure defect counting,
fixed |Delta| filter bounds and m_u/d' do not make it small.

The positive population in Section 6 obstructs automatic annihilation; it is
NOT a dual functional separating the full signed block or all scalar ratios.
No rigorous lower bound on that whole aggregate or universal cancellation
obstruction has been found. Conversely no paid small upper bound has been
found. The first uncertified step remains a signed product/phase estimate,
not a missing numerical path count.

For hard product n~X^(6/5) the old central window has additive shifts
nH/T ~ n^(1/6) H, with X=T/(2pi). Pair insertion preserves lambda but adds a
prime-square weight and path-dependent phase; it does not shorten that old
near-product geometry. This is a structural retained geometry statement, not
a reduction theorem proving equal difficulty. Therefore Decision D would
currently overstate the evidence. No smaller explicit analytic lemma is closed.

## 11. Recover the exact relaxed 79.5891590 witness and margin ceiling

The certificate copies the ENTIRE frozen coefficient vector and support/Hankel
certificate from WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json.
It is a strict degree-eight square with c4=0 and

c7/c5=10212962200/633200091109101,
c8/c6=1/5505764000.

Its relaxed completion mu7=0, mu8=984591917/748818000 is NOT the actual
model's seventh/eighth moments. Its exact relaxed expectation is
295472201803619444358246773/2895247698247420090647048000.
The relaxed uncharged coefficient is
1152151647320090600965277227/1447623849123710045323524000
 =0.7958915902204308.
The maximum uncharged defect allowance below 21/200 is

8528806512359665159693267/2895247698247420090647048000
 =0.002945795110215408,

or 0.58915902204308 percentage points in 1-2E. This is a CEILING for payments
inside this hypothetical completion, not a certified charged margin or the
actual continuum value. The coefficient vector is recorded without rounding.
The existing arithmetic feasible ratio region remains UNCERTIFIED, so the
intersection is **NOT YET CERTIFIABLE**.

Charge audit, with no double counting:
- Support: exact p>=1 on X<=-1 and p>=0 globally; zero algebraic support deficit.
- c4=0: exact, no fourth substitution charge.
- First/third lower moments: inherited o(1) gates have finite fixed coefficients;
  these carry no nonzero limiting numeric charge once their SAME-section
  hypotheses hold.
- Second lower bound: c2<0 permits the inherited variance correction
  2|c2|/(pi^2 R). With pi>333/106, its rational upper payment is
  2|c2|(106/333)^2/6000. This can be calculated from the exact vector, but
  alone is not a complete ledger.
- Normalization a_phi->1 is asymptotic; new eighth-order use still needs bounded
  relevant moments to multiply normalization errors. No invented fixed number.
- Selected section/compression: earlier b5/b6 o(1) error remains available for
  those terms only; b7/b8 boundary/consumer transfer is not automatically covered.
- Canonical pair: k_T->1/6 gives a coefficient limit; (k_T-1/6)x needs a bound
  on x. It is not automatically a free error for unresolved carriers.
- Band: the old cubic curvature constant/charge is not valid for this quartic
  by inheritance. A degree-eight functional band comparison is UNCERTIFIED.
- Geometry/model seventh/eighth substitutions and complete open arithmetic:
  UNCERTIFIED. Do not allocate a numeric zero to these debts.

Thus a fully paid pre-mu7/mu8 margin is NOT CERTIFIED. Even subtracting the known
variance payment only would produce a PARTIAL allowance under a relaxed model,
not a theorem margin. The partial variance payment is exactly
32242676406427306183391/15756336965594727445610547000.
Subtracting this alone leaves
105010427619399283011381545483/35672346890106462936862278408000
in the relaxed defect allowance. Both values are recorded separately in JSON;
neither incorporates the uncertified degree-eight band/geometry/open charges.
The earlier dead quartic lower-bound certificate stays frozen.

## 12. Go/no-go, zero side and requested final report

mu7/mu8: **NO-GO**. Neither a nonempty arithmetic/model intersection nor a
strictly easier open-defect theorem has been certified. No integration launched.

The zero-side mechanism is scalar spectral functional calculus: scalar
polynomials and certain bounded scalar functions, not necessarily polynomials
only. The pointwise eigenvalue majorant and existing tail-Weyl/block argument
are what permit zero counting. Independent path/channel-dependent coefficients
are not supported by that derivation. **NEW ZERO-SIDE THEOREM REQUIRED** for
such consumers; no path-dependent weights are introduced here.

1. H5_aug: rooted, fully labelled closed/open skeletons, Delta in [-2R,2R].
2. H6_aug: identical definition at six leaves.
3. Deletion/insertion: marked carrier-preserving incidence, repair Delta+v+w=0;
   unmarking explicitly convention dependent.
4. Canonical 1/6: reserved final zero-lag pair subset of Delta=0 only.
5. All nonzero defects: integers +/-1,...,+/-2R with triangular lag counts.
6. Bare open trace zero; repaired open trace can be bulk and nonzero.
7. Fifth hard vector is closed; full same-carrier seven-word family has extra
   open-skeleton channels, with no certified mass fraction.
8. Sixth 2:4/3:3: same structural split at eight.
9. Scalar projected optimizer formula exact; actual asymptotic ratios uncertified.
10. Positive normalized population falsifies automatic suppression; no complete
    signed-block o(1) estimate or universal scalar dual.
11. Exact 79.5891590 relaxed coefficient vector preserved in JSON.
12. Intersection NOT YET CERTIFIABLE.
13. Charged margin UNCERTIFIED; uncharged ceiling and partial variance separately.
14. mu7/mu8 NO-GO.
15. Remaining theorem: actual signed, carrier-bearing repaired-open primitive
    discrepancy bound (and closed remainder), within a separately justified
    scalar consumer's full paid ledger.
16. Strict >79 OPEN.
17. Local commit hash is reported in the final response; this note pins parent inputs.

Verification scripts: src/wp84_augmented_open_path_pair_transfer.py and
src/wp84_augmented_open_path_pair_replay.py. Exact defect counts, marked-fiber
algebra, root paths, rational positive population envelope and frozen SOS
recovery pass independent replay; three deliberate corruption tests are rejected.
The asymptotic PNT reduction is justified in Section 6, not by numerical tests.
No push; existing local commits and NotebookLM packet preserved.
