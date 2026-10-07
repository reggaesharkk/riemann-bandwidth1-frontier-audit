# WP84 degree-eight pair insertion and model audit

Decision **C. CANONICAL 1/6 CANCELLATION IS TOO SMALL / NONUNIFORM TO REMOVE THE OLD HARD DEBT.**

Base: local isolated branch codex/c5-c6-attack-20261006, commit
855a47a80f962c7d068ab5db233c36bc6f0e6852. No push. Earlier audit commits are preserved.
This is a structural audit and an exact model falsifier, not a new arithmetic transfer theorem.
Strict >79 remains OPEN for the research program. The particular rational quartic below is ruled out as a >79 consumer even before transport charges.

## First falsifier: no positive moment completion can rescue this quartic

Use the frozen centered model moments
(m0,...,m6)=(1,0,1/3,0,1/4,1/36,157/630).
Set
q(x)=(-449-1128x-12720x^2+14400x^3+144000x^4)/117559,
p=q^2.
The exact c vector, divided by 13820118481, is
(201601,1012944,12694944,15765120,0,-691200000,
-3456000000,4147200000,20736000000).
Thus c4=0, c5+c7/6=c6+c8/6=0. These identities do not imply a small expectation.

Let H=(m_(i+j))_(0<=i,j<=3), h=(m4,m5,m6,z)^t,
a=(-449,-1128,-12720,14400)^t/117559, t=144000/117559.
Every positive model completion has moment matrix
[[H,h],[h^t,m8]] positive semidefinite. H is positive definite:
its leading minors are 1, 1/3, 5/108, 283/108864.
Consequently m8 >= h^t H^-1 h and

E[p] >= a^t H a+2t a^t h+t^2 h^t H^-1 h
 = 234617453201/677185805569
   +(104509440000000/3911093530123)(z-271/5600)^2.

In particular E[p]>=0.3464594964507039. Its excess over the uncharged
79-percent threshold 21/200 is exactly
32702588723251/135437161113800 >0.
The frozen transfer coefficient 1-2E[p] is at most
207950899167/677185805569 =0.30708100709859226,
or 30.708100709859226 percent. No band/variance/endpoint payment can reverse this obstruction.
This is a lower bound, not the actual model expectation; 271/5600 is a relaxed
completion optimizer, NOT a certified mu7. No optimization of a new consumer was performed.
If a proposed formal model violates positive moment matrices, it cannot serve as
a limiting spectral measure for the positive polynomial consumer. This is an additional consistency gate.

The independent Fraction replay uses Gaussian elimination and LDL positivity,
not the producer's Sympy calculation. It rejects corruption of the lower bound,
quadratic coefficient, percentage, and Bell count. The certificate does not claim
mu7/mu8 values and therefore does not select Decision D.

## Exact resolved amplitudes and all insertion channels

Fix T, cutoff prime alphabet, R and selected section I. A resolved configuration
has ordinary primes p_j, signs eps_j, lags l_j in [-R,R], sum l_j=0,
u_0=0, u_j=sum_(k<=j)l_k. Its roots satisfy i+u_j in I for every j.
For alpha_j=log(p_j)/L and c_p=-log(p)/(a_phi L sqrt(p)), define

f_l^+(alpha)=1-alpha (l=0),
f_l^+(alpha)=(1-exp(2 pi i l alpha))/(2 pi i l) (l!=0),
f_l^-=conjugate(f_l^+).

The resolved carrier-free amplitude is
w(gamma)=prod_j[c_(p_j) f_(l_j)^(eps_j)(alpha_j)]
 exp(2 pi i sum_j eps_j u_(j-1) alpha_j)
 (1/d') sum_(i: all i+u_j in I) exp(2 pi i i lambda/L),
lambda=sum eps_j log(p_j).
A_b(lambda)=sum_(gamma with this exact carrier) w(gamma).
The trace restores exp(iT lambda). Root endpoints, every orientation, every
filter coefficient and every intermediate compression are present in this formula.

An explicit all-position insertion channel chooses slots s<t among b+2 slots,
a prime p, pair signs (+,-) or (-,+), and pair lags v,w in [-R,R].
Insert these in a lower ordered word; retain the channel exactly when the resulting
closed path and roots are admissible. If lower lags are left unchanged, closure
forces v+w=0. Its coefficient is exactly w(higher)/w(lower) when the denominator
is nonzero; use unsummed leaf/root tensors rather than division when it is zero.
The inserted partial sums shift intermediate phases and root admissibility.
Thus it is a rectangular, carrier-block-diagonal linear incidence operator on
**resolved leaf/root tensors**, with explicit channel weights. It is generally
path dependent. At fixed finite alphabet and section it is finite dimensional;
this statement is not a uniform finite-rank assertion as T grows. It maps different
orders, so a spectrum is not intrinsically defined. A chosen square composition
could have a spectrum, but is a different operator.

Marking all pairs counts a higher word multiple times. Choose a deterministic
lexicographic deletion rule, or weight each marked admissible preimage by the
reciprocal number of its preimages. These give incidence conventions, not a new
universal scalar on A_b. For an extension with no closed lower preimage, such
weights cannot supply one. A_b(lambda) has already forgotten leaf ordering,
root and displacement data needed by the channel; a complete operator
P_b:A_b->A_(b+2)^pair on those aggregated scalars is NOT established.

## Carrier surjectivity versus geometric surjectivity

Let e_p=r_p-s_p. Then |e|_1=b-2 sum_p min(r_p,s_p).
Therefore C_b={e: |e|_1<=b, |e|_1=b mod 2}. Every (b+2)-leaf configuration
whose carrier lies in C_b contains an opposite-sign equal-prime pair. Deleting
any such pair preserves its reduced carrier and gives b leaves. This proves
carrier-level surjectivity. It does not recover a prescribed lower word.

A finite R=1 counterexample has seven lags (1,1,-1,0,-1,0,0),
with partial sums (0,1,2,1,1,0,0,0). In the first two slots put +p,-p;
use five other distinct primes in the remaining slots. The only opposite-sign
equal-prime pair has lag sum 2. Its deletion leaves a five-leaf path with lag
sum -2, which is not closed. A section with at least three points admits the
higher path. The carrier has norm 5, hence is in C5. It has no deletion preimage
among unchanged-lag closed five-words. Appending a further distinct leaf with
lag zero gives the analogous eight/six example. Filters at these lags are
nonzero for ordinary interior alpha. This is an exact combinatorial obstruction,
not an asymptotic claim that its aggregate has nonzero limiting mass.

Reassigning other lags can create some new lower path, but changes its filter,
phase and endpoint weights; this requires a new transport kernel and does not
prove the requested insertion identity. Open-path tensors can encode the missing
channels (lower total displacement -v-w); they are additional data, not A_b.

## Complete finite-T decomposition without hiding the old debt

Define Q_(b+2)(lambda)=1_(e in C_b) A_(b+2)(lambda), and
N_(b+2)=1_(|e|_1=b+2) A_(b+2). This disjoint split is canonical,
complete, finite T and exact. Q includes all same-carrier extensions, including
nondeletable geometry. Define
E_b^pair=Q_(b+2)-(1/6) A_b.
Then the full fifth-through-eighth contribution is exactly
c7 E5^pair+c8 E6^pair+c7 N7+c8 N8.
There is no explicit c5 A5 or c6 A6 term. This is an algebraic rewrite;
E_b contains -(1/6) A_b and can retain all its hard arithmetic information.
Neither E5 nor E6 is CLOSED by existing estimates.

The frozen canonical component uses only the last two slots, both lag zero,
the same ordinary prime and both sign orders. It has EXACT multiplier
k_T=2 S0,T with
S0,T=sum_p (log p)^2/(a_phi^2 L^2 p)(1-log p/L)^2 ->1/12.
Write Q=k_T A_b+Q_rest. Then
E_b=(k_T-1/6)A_b+Q_rest.
The o(1) scalar times unknown carrier total variation is not automatically o(1).
Conditional bounded eighth moment can bound aggregate lower traces, but is not
an unconditional closure of their resolved correlations.

A valid crude finite-T total-variation bound is
||E_b||_TV <= Z_(b+2)+||A_b||_TV/6,
Z_j=sum_(admissible gamma) |w(gamma)|.
More specifically ||E_b||_TV <= |k_T-1/6| ||A_b||_TV+Z_rest.
These are exact bounds and give no saving in T. They must not be presented as
a closed estimate or charged as a small paid error.

For scalar one-prime Laurent field z+z^-1 (a diagnostic special case), exact
full common-carrier coefficient ratios are
5->7: e=1,3,5 gives 7/2,21/5,7;
6->8: e=0,2,4,6 gives 7/2,56/15,14/3,8.
Multiply by the squared leaf weight if it is not one. They falsify universal
full-sector scalarization, not the already-proved canonical identity.
The earlier full finite-matrix Fourier replay at base commit also found
nonconstant common-carrier ratios with all compression paths included.

## Hard-cell cancellation and normal ordering

Old fifth hard cell: two primes at exponents 3/5 versus three at 2/5.
For EVERY closed lower path the specified appended zero-lag component is
paired and asymptotically coefficient-canceled. Thus the structural answer is
**PARTIALLY CANCELED**, with exact subset: final two leaves, opposite signs,
equal prime, both displacements zero, original lower path/root unchanged.
No fraction of total mass follows: amplitudes are complex and signed, so a
counting fraction is not a mass fraction. The original hard cell remains in
E5 through other insertions and the definition above; its N^(1/6) estimate
has not improved. The identical subset statement holds for sixth-order cells
and E6. Complete cancellation is unproved and scalar cancellation is falsified.

For the canonical append operator K, K^k A_b=k_T^k A_b exactly (fixed T),
because slots are fixed and each appended pair closes at the unchanged root.
An isolated canonical ladder combination vanishes iff
sum_(j=0)^k c_(b+2j) k_T^j=0; its limit uses (1/6)^j.
This says nothing about all-position channels, overlaps, or open paths.

For an actually independent scalar Gaussian pair of variance v, Wick's exact
polynomial is
:x^n:_v=sum_(k=0)^floor(n/2) (-1)^k n!/(2^k k!(n-2k)!) v^k x^(n-2k).
The number of k disjoint marked pair contractions is that factorial ratio.
It follows from exp(tx-vt^2/2), and is not the canonical k_T^k law. The current
consumer conditions cancel only a chosen append component. They do not match
this full contraction rule. For example scalar cumulants would require
M7=kappa7+21 kappa5 kappa2 (if kappa1=kappa3=0), while canonical 1/6 supplies
no coefficient 21. No general normal-order construction removing all ordinary
prime carrier sectors is proved. The canonical recurrence is the only valid
reuse here; it is structural and makes no density claim.

N7,N8 above are NEW-CARRIER remainders, not connected cumulants. An exact
finite-T scalar cumulant can instead be defined from traces M_j by
kappa_n=sum_(set partitions pi) (-1)^(|pi|-1)(|pi|-1)! prod_(blocks B)M_|B|.
It is not N_n, and does not by itself imply factorization of matrix path kernels.
If lower disconnected insertions are subtracted, the convention must specify
this full partition kernel. No identification with the above carrier split is
available. Naming N7,N8 'connected' would hide an unproved theorem.

## Partition certificate and the still-uncertified model moments

The certificate contains EVERY block type for Bell7=877 and Bell8=4140,
with exact multiplicity n!/(prod size! prod multiplicity!) and inverse
Mobius coefficient (-1)^(k-1)(k-1)!. Independent replay checks the Mobius
convolution using a separate Stirling recurrence. Examples:
7: {7}:1, {5,2}:21, {4,3}:35, {3,2,2}:105.
8: {8}:1, {6,2}:28, {5,3}:56, {4,4}:35,
{4,2,2}:210, {3,3,2}:280, {2,2,2,2}:105.
These are scalar partition counts, not equal-valued placement integrals.

If scalar kappa1=kappa3=0, the exact scalar identities are
M7=kappa7+21 kappa5 kappa2;
M8=kappa8+28 kappa6 kappa2+35 kappa4^2
 +210 kappa4 kappa2^2+105 kappa2^4.
From the frozen moments kappa2=1/3, kappa4=-1/12,
kappa5=1/36, kappa6=139/1260. Hence
kappa7=mu7-7/36, kappa8=mu8-1349/2160.
These kappa values are NOT the repository's connected-cycle C7,C8.
For example its Phi4=-1/60 differs from scalar kappa4=-1/12.
The recurrence does not cancel all {5,2} or {6,2} classes.

mu7: UNCERTIFIED. mu8: UNCERTIFIED. No rationality theorem or counterexample
has been established. The local C7 -17/360 and SPEC52 1/8 proposals remain
incomplete certificates/numerical identifications; they cannot be substituted.
The exact moment-completion calculator above does not invent their values.

The finite model integration problem is explicit: for each set partition, impose
sum_(j in B) v_j=0; use b-|pi| independent variables; multiply its connected
block cycle kernels and the outer closed-walk overlap (1-spread partial sums)_+.
Each block kernel is the ordered-partition signed sum of (1-spread subset sums)_+.
Resolve all affine ordering/sign cells into rational polytopes and integrate the
resulting polynomial exactly with the existing rational facet engine. This is
finite, but no completed order-eight archive has been recovered here.
C7 alone has 9366 ordered terms (397 symmetry orbits in the existing driver),
SPEC52 has 450 term/placement jobs; C8 has 94586 ordered terms in dimension 7.
Additional eighth placement classes {62},{44},{422},{2222} must also be covered.
No reliable wall-time bound follows without term timings and degeneracy analysis.
A partial archive or expected sum is not certification. Because the consumer is
already falsified independently of mu7/mu8, no massive unfinished integration
was launched or theorem optimization performed.

## Machinery inventory and evidence boundary

The app lists one connected project: Downloads Riemann checkout. Its head is
908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5; it was not changed.
The available user repos directory contains reggaesharkk, with no discovered
polytope/cumulant/rational integration source. Downloads directory inventory
also found A1294/A1296 diagnostic folders, compoo, M14 parts, and OSF folders;
these names alone do not identify an LRSC repository. No LRSC connected project
was exposed. A broader file scan found local LRSC ZIP source bundles; every
archive and candidate Python/integration member is recorded with archive SHA256
in WP84_DEGREE8_LRSC_ARCHIVE_INVENTORY.json. They were inspected as archives,
without changing or extracting into Downloads. This is the discovered inventory boundary, not a claim that LRSC
cannot exist in an unavailable workspace. Thirty-five LRSC-related Python source members were examined without execution;
member hashes, function inventories and integration-keyword matches are recorded
in the archive inventory. Their spectral/rank and interval certificate machinery
does not supply a completed seventh/eighth Riemann polytope receipt. No component
was imported from LRSC.

Reused/read current sources and exact git blobs are recorded machine-generated
in WP84_DEGREE8_PAIR_INSERTION_AND_MODEL_CERTIFICATE.json, pinned to base
855a47a80f962c7d068ab5db233c36bc6f0e6852:
wp81_spec52_exact.py and verify.py; wp80_c7_full_orbit_batch.py,
aggregate.py and symmetry_reduce.py; wp84_c5_pointwise_supercritical_sign.py;
wp84_parity_graded_degree8_verify.py and recon.py.
The SPEC52 adapter requires upstream gpu/exact_connected.py and
exact_polytope.py at public commit d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8.
No missing upstream source or certificate is assumed correct. No new network
fetch was needed for the exact falsifiers.

## Old-versus-new arithmetic complexity

For signed leaves alpha_j in (0,1), closed resonant cells obey
sum_plus alpha=sum_minus alpha=s and outer spread<1.
For m versus n leaves, supremum balanced product length is X^min(m,n).
It is approached by alternating unit-sized excursions with remaining opposite
leaves split as necessary; hence the exponent alone gives no shortening.
Away from aliases, the root phase scale |log(A/B)|=O(1/T) gives additive
shift |A-B|=O(X^s/T). Since T~2pi X, this is X^(s-1).
For the old fifth cell s=6/5: products X^(6/5), shifts X^(1/5),
The previously isolated N^(1/6) obstruction is inherited from the earlier
restricted-correlation audit; it is not derived from this product-length table.

| sector | balanced product supremum | root shift supremum | status |
|---|---:|---:|---|
| old 5: 2 vs 3 | X^2 | X | OPEN restricted hard estimate |
| old 6: 2 vs 4 | X^2 | X | OPEN |
| old 6: 3 vs 3 | X^3 | X^2 | OPEN |
| E5 pair, inherited hard cell plus pair exponent a | X^(6/5+a) | X^(1/5+a) | no gain; 0<a<1 |
| E6 pair | inherits lower cell plus a | inherits shift times X^a | no gain |
| N7: 1 vs 6 / 2 vs 5 / 3 vs 4 | X / X^2 / X^3 | 1 / X / X^2 | OPEN |
| N8: 1 vs 7 / 2 vs 6 / 3 vs 5 / 4 vs 4 | X / X^2 / X^3 / X^4 | 1 / X / X^2 / X^3 | OPEN |

All-distinct primes give genuinely new carriers; ordinary exact equality cannot
close these nonempty sectors. Near-product geometry is still present. With
N=e^(L-sqrt L) these lengths acquire subpower factors, not a better limiting
exponent. Connected-cycle cancellation might reduce support, but it must be
proved cell by cell; no such theorem is supplied by the carrier split. The table
is a raw-sector envelope, not a claim that every maximum survives a Mobius sum.
Aliases satisfy log(A/B)/L near integer j, with tolerance O(1/(m_l));
these are additional channels, not disposed of by ordinary near equality.
Periodic alias estimates remain unclosed wherever their old/new signed reduction
has not been proved. New C7/C8 debt cannot be declared easier than old debt.

## Requested sixteen conclusions

1. Carrier insertion is surjective; unchanged-lag closed-path insertion is not.
2. Full resolved incidence is carrier-block diagonal and path dependent; no
   complete scalar operator on the aggregated A_b has been established.
3. 1/6 belongs precisely to the canonical appended zero-lag pair component.
4. Old fifth debt: PARTIALLY CANCELED in that exact component; no mass fraction.
5. Old sixth debt: same; E6 remains OPEN.
6. Wick identity is valid only under its scalar independence hypotheses; not here.
7. Canonical repeated multiplier k_T^k and polynomial recurrence are exact.
8. mu7 UNCERTIFIED.
9. mu8 UNCERTIFIED.
10. Scalar kappa7=mu7-7/36, kappa8=mu8-1349/2160; actual values UNCERTIFIED.
11. Actual model percentage unknown, but certified upper bound 30.70810071%.
12. Fully paid margin: not assembled; the uncharged consumer already fails.
    Keep A->B reprojection, filtered arithmetic, geometry, endpoint, variance
    and zero-transfer obligations separate. No invented charge or double count.
13. New 7/8 raw product envelopes reach X^3/X^4; connected reductions unproved.
14. New debt is not proved smaller/easier; old geometry is retained in E5/E6.
15. Decision C, with an additional exact moment-positivity consumer falsifier.
16. Local audit commit is reported in the final response; this note pins its
    inputs to the parent commit, avoiding a self-referential hash.

Verification:
python src/wp84_degree8_pair_model_audit.py
python src/wp84_degree8_pair_model_replay.py
Both PASS. The JSON contains full partition tables, exact constants, provenance,
workload and preserved falsifiers. Strict >79 remains OPEN; no push performed.
