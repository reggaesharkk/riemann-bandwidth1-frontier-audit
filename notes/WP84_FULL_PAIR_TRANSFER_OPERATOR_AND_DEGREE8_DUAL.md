# Full pair-transfer operator and degree-eight dual audit

Parent bca3752131d40648472337914815cb2a108a3bb5; isolated branch
codex/c5-c6-attack-20261006. No push. Decision C of the preceding audit is
permanent. The failed rational quartic is not reopened and its mu7/mu8 are
not computed.

**Decision F: INCONCLUSIVE.** First uncertified step: a complete pair-transfer
identification between the augmented open-path input tensors and the ACTUAL
closed fifth/sixth hard measures, with a bound in the oriented primitive
functional needed by the theorem. An exact cross-order insertion map is given
below; it is not an endomorphism of the closed lower-order space. Neither
an arithmetic eigenchannel nor a universal scalar obstruction has been proved.

A separate exact certificate proves the degree-eight SOS family is NOT killed
by moments through six and extended moment positivity alone: a strict-degree-eight
member and a positive-definite relaxed moment completion give 79.5891590%
before charges. This is feasibility in the requested positivity relaxation,
not the value of the actual continuum model and not an arithmetic rescue.

## 1. Frozen scale and basis

Use L=log(T/(2pi)), N=floor(exp(L-sqrt(L))), h=2pi/L,
d=floor(TL/(2pi)), selected I=[k_-,k_+], d'=|I|~d, R=6000,
c_p=-log(p)/(a_phi L sqrt(p)), a_phi->1. No scale change.

A closed resolved state gamma=(I,T,L,a_phi,i; (p_j,eps_j,l_j)_(j=1)^b)
retains every prime, sign, Fourier lag, intermediate displacement u_j,
projection 1_I(i+u_j), orientation and root i. Here |l_j|<=R,
u_j=sum_(k<=j)l_k and u_b=0. The filter f_l^eps(alpha) is exactly
f_0^eps=1-alpha, f_l^+=(1-exp(2pi i l alpha))/(2pi i l),
f_l^-=conjugate f_l^+, alpha=log(p)/L.
Its carrier is the integer prime-exponent vector e, lambda=sum eps log(p).
Its normalized carrier-free root weight is

 F_b(gamma)=(1/d') prod_j c_pj f_lj^epsj(alpha_j)
     exp(2pi i sum_j eps_j(i+u_(j-1))alpha_j)
     prod_(j=0)^b 1_I(i+u_j).

Restoring exp(iT lambda) and summing roots/states gives the actual trace.
All intermediate projections and selected-section restrictions are retained.
The weight is complex; reversal/adjoint must be retained as well.

## 2. Complete exact insertion matrix, and why its domain must be augmented

Let V_b^closed be the free resolved closed-state space above. Let V_b^open
also retain rooted lag skeletons of total displacement d0 in [-2R,2R],
without imposing intermediate endpoint projections on the skeleton after pair
deletion. Root i stays in I. The old leaf factors, lag labels and phase data
remain. Skeleton nodes may leave I; the HIGHER word is always fully projected.
This augmentation is necessary, not permission to replace the actual hard vector.

For slots s<t in {1,...,b+2}, p<=N, eps=+/- and pair lags v,w in [-R,R],
insert (p,eps,v),(p,-eps,w) into skeleton eta, preserving its other labels.
Retain the channel iff d0+v+w=0 and every higher node lies in I.
The exact symbolic multiplicative channel coefficient is

 c_p^2 f_v^eps(alpha_p) f_w^-eps(alpha_p)
 exp(2pi i [sum_higher eps_j(i+u_(j-1))alpha_j
              -sum_skeleton eps_j(i+u_(j-1))alpha_j])
 prod_(j=0)^(b+2) 1_I(i+u_j).

The common 1/d' normalization is not duplicated. Remaining leaf filters
are unchanged. This formula uses no division by zero lower amplitudes.
Use the unprojected skeleton weight in the input; a skeleton projection of
zero would otherwise destroy a nonzero higher state. The carrier phase
exp(iT lambda) is unchanged. Root and section masks are part of each matrix
entry, not an asymptotic replacement.

For each higher word zeta let D(zeta) be the number of its opposite-sign
equal-prime slot pairs. The marked insertion map counts D copies. Define the
unmarked full map by dividing each marked contribution by D(zeta); equivalently
use lexicographically first cancellable pair deletion. Then every higher
same-carrier word with |e|_1<=b is counted exactly once. This is the complete
linear channel representation P_b^aug:V_b^open -> V_(b+2)^closed.
The builder enumerates every marked channel; the unmarking convention is
specified separately to avoid silently counting marked and unmarked sectors
as the same quantity.

Unique factorization gives |e|_1=b+2-2 sum min(r_p,s_p), hence D>0 for every
higher carrier shared with order b. Thus the augmented map is surjective on
resolved carrier words. It is not surjective from V_b^closed.

Exact R=1 example in the certificate:
(+2,1),(-2,1),(+3,-1),(+5,0),(-7,-1),(-11,0),(-13,0),
where each displayed pair is signed prime and lag. Root 0 and section [0,2]
admit the closed seven-word. Its unique cancelling pair has lags 1,1.
Deleting it gives a five-skeleton with total displacement -2. The builder
recovers the higher word from this open skeleton, and checks that closed
lower deletion cannot recover it. A further distinct prime at lag zero gives
an eight/six analogue. This preserves the frozen path-deletion obstruction.

## 3. Exact block structure and spectral scope

P5 and P6 have the same channel form, at different graded orders. They are
rectangular, finite-dimensional at fixed T,R,I,N and sparse in resolved
coordinates. Exact invariant block labels are carrier e and retained root i,
as well as fixed external parameters I,T,L,R. Each channel is labelled by
slots s,t, pair prime, orientation eps and pair lags. Input displacement d0
connects only to channels v+w=-d0; output displacement is zero. Input and
output order are different; intermediate path ordering is changed. There is
no scalar/diagonal displacement action, no uniform low-rank theorem, and no
universal Toeplitz or positive Gram identification for the insertion map.
Further special decompositions can depend on the particular finite alphabet;
no mathematically canonical 'finest' spectral decomposition follows from labels.

An eigenvalue is defined for an ENDOMORPHISM. P_b^aug is not one. The expression
P_b v=lambda v requires an additional map J_b back to an agreed common space.
Carrier aggregation J loses paths and is not invertible; deletion J is convention
dependent and can leave open skeletons. J_b P_b can be studied after J_b is
specified, but its spectrum is then the spectrum of that chosen composition.
No exact spectral conclusion for the actual arithmetic hard vector follows
from the old scalar Laurent counterexamples or toy finite-matrix ratios.
The spectral verifier therefore fails closed on claims that this rectangular
map has the requested hard eigenspaces.

## 4. Actual hard vectors, not continuum proxy vectors

The exact v5 is the atomic root/state measure F5(gamma) exp(iT lambda_gamma),
restricted to the signed 2-versus-3 hard cell and its adjoint, with exponent
windows around (3/5,3/5;-2/5,-2/5,-2/5), central |lambda|<=H/T and the
product/dyadic windows in WP84_SIGNED_NEAR_PRODUCT_CELL_DECOMPOSITION and
WP84_POWER_SCALE_CENTRAL_WINDOW_AND_DENSITY_BRIDGE. The window endpoints
are parameters; no fictitious numerical prime list or unproved density is inserted.
Its root weights are the actual 1/d' weights above. The hard-mask function in
the builder applies specified finite-T prime and product windows. Its log
comparisons require exact or certified-real caller inputs, not a floating
sign decision promoted to a theorem.

v6 is the same atomic definition at order six, with the unresolved 2:4 and
3:3 cells, collision masks and adjoints from the finite-T decomposition. There
is not one repository-certified universal sixth hard eigenvector. Each retained
cell is a vector/mask, not a scalar continuum kernel.

Applying P to the CLOSED vectors yields the admissible insertion channels
originating from those vectors; it omits higher words whose deletion needs
open skeletons or different lower cell labels. Completing P requires additional
open-sector inputs. Their size is not inferred from v5,v6. Thus a computed
P v5 alone would not equal the full same-carrier seventh hard measure.

The canonical append component has both new lags zero in the final two slots,
both sign orders and the same prime. On aggregated lower amplitudes its exact
multiplier is k_T=2S0,T ->1/6. It is one component, not an invariant eigenspace
of the complete rectangular operator. No other insertion coefficient is declared
1/6. Finite-T unmarking must keep this chosen subset disjoint: remove it first,
then allocate remaining higher words using a deletion rule. Dividing ALL marked
pairs by D without reserving this subset would change the canonical contribution.

## 5. Norm and scalar cancellation: exact criterion, no invented lower bound

The actual sufficient analytic functional in the power-window note is
Phi(E;a,b)=|D(b)E(b)|+|D(a)E(a)|+integral_a^b |E(x)| |D'(x)| dx,
D(x)=D_d'(x/L), with signed/oriented primitive discrepancy E on each branch.
The consumer coefficients are included exactly once. The direct signed trace
can also benefit from cancellations lost by this sufficient absolute functional.
Phi is not a Hilbert norm on resolved paths and is not spectrally equivalent
to counting l2. The exact-zero population and each alias/transition/far branch
must retain their existing status; the new operator does not reopen closed exact
nonzero-alias disposal. Near-alias transfer is not automatically closed.

After specifying a common projection J and Hilbert weights, a diagnostic
real scalar a minimizing ||v+a w||, w=J P v, is
 a_*=-Re<v,w>/||w||^2,
 residual^2=||v||^2-(Re<v,w>)^2/||w||^2.
For complex a replace Re squared by |<v,w>|^2. Polynomial ratios are REAL.
A rigorous arithmetic ratio region requires estimates for the ACTUAL Phi/trace
of the discrepancy, not these formulas on an arbitrary toy l2 space.

A dual lower bound in a normed common space would require a bounded functional
ell with ell(w)=0, |ell(v)|>0 and ||ell||_dual<=1; then inf_a||v+a w||>=|ell(v)|.
No such functional or nonzero asymptotic Delta in the required arithmetic
functional has been certified. Nonconstant operator channels alone do not prove
that the actual v has quantitatively nonnegligible mass in incompatible channels.
Consequently optimal c7/c5, c8/c6 and residual lower bounds remain UNCERTIFIED.
This explicitly prevents the tempting but invalid upgrade to Decision C.

## 6. Entire SOS coefficient family and exact support parameterization

Let z=(1,X,X^2,X^3,X^4), p=z^t G z, G real symmetric PSD. Then
c_k=sum_(i+j=k)G_ij,
c4=2G04+2G13+G22=0,
c5=2G14+2G23, c6=2G24+G33, c7=2G34, c8=G44.
The ratios are these exact rational expressions wherever denominators are nonzero;
zero denominators are separate strata, not infinite ratios silently discarded.

The exact half-line support condition is p(-1-y)-1>=0 for y>=0. In one variable
it admits an SOS half-line representation
 p(-1-y)-1=z4(y)^t U z4(y)+y z3(y)^t V z3(y), U,V PSD,
where z4=(1,y,...,y^4), z3=(1,y,...,y^3). Match all coefficients through eight.
This is a parameterization of the full support/SOS family, not merely squares
with nonnegative translated coefficients. No failed 1/6 identities are imposed.

For moment completion choose z=mu7, t=mu8, H=(mu_(i+j))_(0<=i,j<=3),
h=(mu4,mu5,mu6,z). Since H>0, positivity is exactly t>=h^t H^-1 h.
For each fixed G the objective is L0(G)+c7 z+c8 t. For c8>0 its best-case
completion is at
 z_*=-(c7+c8 B)/(2 c8 A),
 where h^t H^-1 h=A z^2+B z+C;
 inf_completion E[p]=L0+c8 C-(c7+c8 B)^2/(4c8 A).
This is an exact fixed-consumer moment-positivity optimizer. For c8=0,
PSD forces G's final row zero, hence c7=0 and the objective is the lower-order
one. Joint optimization over G and completion is NOT a convex SDP merely
because its two slices are convex: c7 z+c8 t is bilinear. No numerical local
optimization is promoted to a global rational dual optimum.

The globally best-case uncharged coefficient over this relaxation is rigorously
bracketed by 79.58915902204308% <= optimum <=100%. The upper bound is only
the trivial nonnegativity bound, not a solved optimum. No <=79 universal dual
certificate exists for this relaxation, because the following exact witness
violates such a bound. Additional support constraints on the model law could
change the relaxation; none are invented. The zero-count support X<=-1 is
an event to majorize, not support of the entire model measure.

## 7. Rational strict-degree-eight witness in the positivity relaxation

Start with a0=-19101/185500, a2=31/50, a3=-371/500,
a4=1/100000 and set a1=-(a2^2+2a0 a4)/(2a3).
Normalize q by q(-1). G=aa^t is exactly PSD and c4=0. The certificate
records every normalized coefficient. The translated q(-1-y) is

1+(44141630265/13764256742)y
 +(19586727223/6882128371)y^2
 +(5106756382/6882128371)y^3
 +(137641/13764256742)y^4.

All coefficients are nonnegative, so q(-1-y)>=1 and p=q^2>=1 there.
Use the RELAXED completion mu7=0,
mu8=984591917/748818000=h^t H^-1 h+1.
The extended moment matrix is strictly positive definite, with leading minors
1,1/3,5/108,283/108864,283/108864. These are completion values, NOT actual
continuum moment evaluations. They satisfy the stated Hamburger positivity
relaxation; no extra finite-support bound has been certified for the true model.

E[p]=295472201803619444358246773/2895247698247420090647048000
 =0.10205420488978459,
1-2E[p]=1152151647320090600965277227/1447623849123710045323524000
 =0.7958915902204308.

Its ratios are
c7/c5=10212962200/633200091109101,
c8/c6=1/5505764000.
They are tiny positive ratios, not -6. This is a certified point in the
relaxed model-feasible region and a counterexample to a universal <=79
positivity assertion. It does not satisfy any established arithmetic pair
cancellation condition, and no degree-six curvature/band charge is copied to it.
Strict inequalities and positive definiteness give continuity of model
feasibility for nearby exact support-certified squares; this is not a quantified
arithmetic-feasible interval.

The preceding dead quartic's lower-bound dual remains intact and is not a dual
for this family. The new witness is a primal countercertificate to the requested
universal model obstruction. There is no fabricated universal rational dual.
Independent Fraction replay checks convolution, support binomial expansion,
LDL positivity, objective and the path obstruction, and rejects three deliberate
corruptions. The initial independent support expansion had an extra (-1)^k;
it was corrected before the passing replay and local commit.

## 8. Model/arithmetic intersection and zero-side admissibility

The relaxed model region is nonempty, explicitly above. The arithmetic ratio
region for the complete actual hard measure is UNCERTIFIED. Their intersection
is therefore UNRESOLVED, not empty or established nonempty. Conditions A and B
for actual mu7/mu8 integration are not both met; DO NOT compute those moments.
No fully paid new degree-eight margin is available. A->B reprojection, filtered
arithmetic, geometry, endpoint and zero-transfer charges stay separate.

The existing zero-side mechanism bounds a spectral indicator by a scalar
polynomial or bounded scalar functional calculus of the Hermitian Weil matrix.
The scalar pointwise inequality is what transfers to every eigenvalue. The
R400 zero-side source audit keeps the count attached to the FULL matrix even
when a selected section is used for prime-side calculations. Bounded resolvent
consumers also use a scalar spectral function; they do not authorize independent
word/path coefficients.

An arbitrary channel-weighted sum of prime words need not be positive, need
not be a function of that matrix and has no established eigenvalue majorant.
Hence path-dependent consumers **REQUIRE A NEW ZERO-SIDE THEOREM**. They are
not already admissible. Stop that consumer route here; no invented theorem or
path-dependent zero percentage is claimed.

## 9. Structural progression and required report

Degree six: fifth information is necessary in the previously certified scoped
model obstruction; fifth/sixth carrier cancellation is forbidden by parity.
Degree eight: same-parity carrier overlap exists, but the canonical scalar
lift is incomplete and full insertion depends on paths. One specific quartic
is dead by positivity; the entire scalar family is not thereby dead.

1. P5: rectangular carrier/root-block sparse channel map on augmented skeletons.
2. P6: same form; no universal scalar or endomorphism spectrum.
3. v5/v6: actual finite-T projected atomic measures and hard-cell masks above.
4. 1/6: only canonical appended zero-lag component, not full invariant subspace.
5. Optimal arithmetic scalar ratios: UNCERTIFIED; generic Hilbert formula only.
6. Actual arithmetic residual lower bounds: UNCERTIFIED; no positive Delta.
7. Degree-eight model-feasible region: nonempty, exact witness and SOS equations.
8. Universal positivity optimum: not solved; rigorous bracket 79.5891590%-100%.
   In particular positivity alone cannot supply a <=79 dual for this family.
9. Model/arithmetic intersection: UNRESOLVED.
10. Actual mu7/mu8: not worth integrating until an arithmetic-feasible region exists.
11. Path-dependent consumer: requires a new zero-side theorem; route stopped.
12. Remaining theorem: complete closed/open path identification plus the signed
    carrier-bearing primitive discrepancy estimate on the selected section,
    quantitatively within a support-certified scalar consumer's paid budget.
13. Strict >79: OPEN. No arithmetic or unconditional zero theorem is promoted.
14. Local commit is reported in the final response. Inputs remain pinned to parent.

Artifacts:
- src/wp84_full_pair_transfer_degree8.py: all-position marked channel builder,
  carrier/deletion and hard-mask projector, positivity witness/calculator.
- src/wp84_full_pair_transfer_degree8_replay.py: independent rational replay.
- notes/WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json:
  all rational witness coefficients, completion, principal minors and path counterexample.

The missing spectral/eigenspace certificate is explicitly a type/analytic gate,
not a numerical job silently omitted. A rectangular map cannot have a hard-vector
eigenvalue until an identification is supplied and validated in the actual norm.
The old-counterexample and toy spectral scopes are not used to claim a universal
scalar impossibility theorem.
