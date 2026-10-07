# Theorem-aware degree-six consumer design: exact obstructions and certificate boundary

Parent 195928861e6227d6b7cd824fd35b7eccda7d139c; 2026-10-07.
Branch codex/c5-c6-attack-20261006. Additive LOCAL audit; no push.

**Decision D: INCONCLUSIVE for the actual arithmetic-safe degree-six program.**
The first uncertified step is the existence of the proposed common joint
kernel with a positive arithmetic measure on which continuum sign implies
an upper bound. This precedes optimizer certification. We prove an exact
obstruction for the naturally defined DISJOINT sharp-kernel proxy, and an
independent universal model obstruction for the c5=0 fallback. Neither is
mislabelled as an impossibility theorem for an unidentified actual kernel.
No stronger number theory, power-H strategy or translation saving is invented.

## 1. Variables, SOS coefficients and the support certificate

The source uses centered X and physical x=X+1. Its physical support x<=0
is X<=-1, NOT X<=0. The frozen moments are moments of X. Accordingly write

 P(X)=v(X)^T G v(X), v=(1,X,X^2,X^3), G PSD,
 p_physical(x)=P(x-1).

Physical support is p_physical>=1 for x<=0; equivalently P>=1 for X<=-1.
The correct moment objective is sum c_j mu_j(X). Translating the Gram
matrix is a congruence and preserves PSD, but translating coefficients
changes which fourth-order coefficient vanishes. We impose c4=0 in the
CENTERED variable, because that is the coefficient multiplying the frozen
fourth-moment debt. Setting the physical fourth coefficient to zero instead
would not accomplish the requested debt cancellation.

With symmetric indices 0,...,3,

 c0=G00, c1=2G01, c2=G11+2G02, c3=2G03+2G12,
 c4=G22+2G13, c5=2G23, c6=G33.                                  (1)

These identities are exact. G PSD proves global nonnegativity. For discovery
we enforce a half-line support certificate

 P(-1-y)-1 = z3(y)^T H z3(y) + y z2(y)^T Q z2(y),
 H PSD (4 by 4), Q PSD (3 by 3), y>=0.                            (2)

This is a genuine sufficient support condition; no sampling is used. Floating
PSD/equality residuals do not certify it. The exact candidates below use
rational outer-product Grams and directly nonnegative support coefficients.

Normalization falsifier: if one literally imposes P(X)>=1 for X<=0 while
still using centered frozen moments, a different problem results. Its moment
matrix M minus (1/2)e0 e0^T is positive definite (exact leading minors
1/2,1/6,1/216,19/120960). Therefore E_model>=G00/2>=1/2, already excluding
>79. This is not applied to the intended translated support problem.

The old actual bounded consumer is

 p_dag(x)=a_pole^6 q(x-1)^2/(x^2+a_pole^2)^3, a_pole=221/200.

It is bounded, globally nonnegative and a support majorant, and p_dag<=
q(x-1)^2. General unbounded SOS majorants do NOT inherit its curvature or
full-to-band transfer. A candidate requires its own bounded realization and
paid curvature/section ledger. In particular a quadratic numerator over
this same sixth-degree denominator decays to zero at negative infinity and
fails support. No old band charge is automatically reused for new candidates.

## 2. Actual arithmetic object and the proposed safe-region condition

Keep the covered/uncovered sets from the accepted audits. Covered means
support-empty cells and fixed-gap product exponent sum <2, together with
the previously CLOSED reductions. U includes supercritical ordinary central
2-vs-3, 2-vs-4, 3-vs-3 cells, repeated-label populations, long FAR,
TRANSITION and near aliases; the power window also retains the old
one-vs-many populations. Proper-power complete signed-gate removal and
exact nonzero aliases remain permanently CLOSED. No U population is dropped
because its sharp geometric density has small or zero mass.

Finite arithmetic is

 sum_{b=5,6} c_b sum_{resolved tuples alpha of degree b}
     (product prime/filter coefficients and lag phases)
     exp(i tau0 lambda_alpha) D_d'(lambda_alpha/L).                (3)

The fifth tuple has five labels and four free balanced model coordinates;
sixth has six labels and five free coordinates, plus lower-dimensional
pair/{4,2} closure sectors. There is no established pointwise pairing that
identifies these different domains with one alpha. This is the same
coupling boundary recorded in the accepted power-window audit.

The legitimate sharp proxy is a signed measure on their DISJOINT UNION:

 J_proxy|Omega5=c5 F5, F5=O5 C5,
 J_proxy|Omega6=c6 F6, F6=O6 C6,

with separate measures for the sixth closure strata. On fifth F5>=0 and
its total is 1/36. Sixth F6 takes both signs; total -1/126. This proxy is
fully defined, but it is not identified with the complex measure in (3).

CRITICAL SIGN FALSIFIER: sharp negativity does not imply arithmetic
favorability. The carrier-bearing measure in (3) is complex. Already the
sampled kernel D3 at argument 3/10 has real part (2-sqrt(5))/6<0. A negative
geometric multiplier times that real part is POSITIVE. Likewise complex
carrier phases can reverse a sign. This is not claimed as an actual prime
counterexample; it disproves the algebraic inference from geometric sign
alone, unless a positive-measure representation is first proved.

Therefore 'J<=0 on U needs no arithmetic theorem' is valid only for a
PROVED representation integral_U J dmu with dmu positive, or for directly
certified nonpositivity of every actual real residual. Neither representation
is supplied by PNT measure normalization or by the continuum C5/C6 formulas.
An interval proof of a sharp sign does not bridge that gap.

## 3. Exact global obstruction for the disjoint sharp proxy

The prior exact sign certificate supplies a positive sixth box in U, with
three positive/three negative slots, balanced product exponent about 1.8.
Its root is near (-.7,.8,-.7,.6,-.4,.4). Exact perturbed center, radius,
C6 and O6 are copied into the region certificate from the accepted parent:

 C6=39971/100000, O6=199997/1000000,
 radius=1/200000 in five free coordinates,
 integral_box F6=7994080087/10^36 >0.                             (4)

All arrangement walls are excluded, so this is an open nonzero-mass region,
not one isolated zero-mass dyadic point. It is supercritical and not covered
by the short-product estimate. There is also a certified negative 2-vs-4
box; no global nonpositivity of C6 is assumed.

For the DISJOINT proxy, safety everywhere on U implies c6 F6<=0 on (4).
Since G PSD implies c6=G33>=0, necessarily G33=0. Every two-by-two principal
minor then forces Gi3=0. Thus c5=0 and G13=0. Imposing c4=0 now gives
G22=0, and PSD forces row/column 2 to vanish. The consumer is QUADRATIC:

 P(X)=G00+2G01 X+G11 X^2.                                       (5)

This implication applies to every SOS rank, not just a square. No interval
sampling or optimizer output is involved. No global c5/c6 ratio helps:
on the sixth domain K5 is zero and the dangerous value is c6 F6 alone.

For the remaining two-by-two Gram H, let v_minus=(1,-1)^T,

 M2=diag(1,1/3),
 M2-(1/4)v_minus v_minus^T
    =[[3/4,1/4],[1/4,1/12]] PSD, determinant zero.                (6)

Hence E_model=tr(H M2)>=P(-1)/4>=1/4. Equality is attained by

 q_lin(X)=-1/4+(3/4)X, P_lin=q_lin^2,
 c=(1/16,-3/8,9/16,0,0,0,0).

For y>=0, P_lin(-1-y)-1=3y/2+9y^2/16>=0. Exact PSD Gram has rank one.
Thus the OPTIMAL disjoint safe-proxy model coefficient is 1-2E=1/2.
Adding nonnegative theorem charges cannot raise it above 50%, let alone79.
This is a complete exact dual obstruction for THIS proxy program.

Scope boundary: it is not a dual obstruction for every possible coupled
finite-band arithmetic representation. Such a representation has not been
specified or proved. Finite-R signs cannot silently be replaced by sharp
signs, and a coupling might combine domains differently. Decision C for the
actual program would require an obstruction in that actual valid cone.

## 4. Kernel-ratio map and single-square/SOS comparison

The ratio -K5/K6 is not defined on a common actual exponent domain by the
existing results. On the disjoint proxy, extending the other kernel by zero
makes rho=0 wherever K6!=0, with K6 of both signs; rho is undefined on
fifth positive mass, where K6=0. There is no genuine inf/sup of a shared
local cancellation ratio. Reporting a finite admissible c5/c6 interval
would invent a coupling. Safety instead forces c6=0, after which the ratio
itself is undefined and c5 also vanishes by PSD.

For a single cubic q, c4=a2^2+2a1a3=0, c5/c6=2a2/a3 when a3!=0.
The same sixth positive-box obstruction forces a3=0, then a2=0. The optimal
square is exactly q_lin above. Full SOS mixing cannot improve the proxy:
(6) proves the same bound for every rank. Minimum number of squares for
the attainable proxy optimum is one. This is a GLOBAL sign implication
using the full U requirement; it is not a claim that one box accounts for
the full fifth continuum mass.

## 5. c5=0 hostile check: universal exact positive quadrature

This second obstruction does not depend on the proposed safe sign map.
For EVERY globally nonnegative polynomial with centered c4=c5=0 and
P(X)>=1 on X<=-1, use the positive quadrature nodes

 (-1,-1/2,0,1/2,1)

and weights

 (1151/9450, 848/4725, 626/1575, 848/4725, 1151/9450).

Their moments of orders 0,1,2,3,6 match exactly

 (1,0,1/3,0,157/630).

Fourth moments need not match because c4=0. Fifth moments need not match
because c5=0. Therefore E_model=sum weights*P(nodes). Positivity at every
node and P(-1)>=1 give

 E_model>=1151/9450,
 1-2E_model<=3574/4725 =0.756402116402116... <79/100.               (7)

This excludes >79 from the c5=0 model benchmark before ANY band, variance
or section payment. It is a rigorous upper bound, not a claimed exact
optimum of the full fallback cone. The numerical fallback search does not
supply an exact optimum, and no uncertified optimum is reported.

A simple exact feasible c5=0 square is

 q_cub(X)=157/787-(630/787)X^3,
 c=(24649/619369,0,0,-197820/619369,0,0,396900/619369),
 E_model=157/787, model coefficient=473/787.

q_cub(-1-y)=1+(1890/787)y+(1890/787)y^2+(630/787)y^3>=1.
It remains sixth-dependent and is not arithmetic-safe or a >79 candidate.

## 6. Numerical discovery: saved, unpromoted, and not theorem-aware yet

The discovery script uses scipy SLSQP over symmetric G,H,Q, with coefficient
identities (1),(2), PSD eigenvalue inequalities and c4=0; a second run adds
c5=0. It starts from the frozen rational square, whose centered support is
exact. It saves every matrix and rational entry approximant separately in
WP84_DEGREE6_CONSUMER_NUMERICAL_DISCOVERY.json.

Both runs reached the iteration limit. The unrestricted model run has
objective about .102051576 and negative minimum eigenvalue about -5.5e-8;
the c5-zero run has objective about .151877354 and negative eigenvalue about
-6.3e-8. These are NOT feasible certificates and NOT optimum statements.
Approximate equality residuals near machine epsilon cannot repair negative
eigenvalues. Entrywise rational rounding can break PSD and c4=0; none is
promoted. There is no promising theorem-aware candidate to reconstruct
until the actual kernel constraint is defined. The exact rational candidates
in this audit are the preserved square and the two explicit analytic
squares above, not those floating matrices.

## 7. Model values and the separated theorem ledger

Frozen moments are mu0=1, mu1=mu3=0, mu2=1/3, mu4=1/4, mu5=1/36,
mu6=157/630. The preserved rational square has

 q=(-19101/185500)+(961/3710)X+(31/50)X^2-(371/500)X^3,
 c=(364848201/34410250000,-18356061/344102500,
    -26060119/430128125,21981971/46375000,0,
    -11501/12500,137641/250000),
 c5/c6=-1240/371,
 E_model=35116876419/344102500000.

Its uncharged model simple-zero coefficient is 1-2E_model, not a certified
actual-zero result. Support is checked exactly by the coefficients of
q(-1-y)^2-1, all nonnegative; G=aa^T is exactly PSD. This existing consumer
retains the entire arithmetic debt; it is not a new safe consumer.

For each exact candidate the verifier separately records

 lower=c0+c2/3 (c1,c3 vanish only under inherited lower gates),
 fourth=0,
 fifth=c5/36,
 sixth pairs=c6*131/420,
 sixth {4,2}=-c6*23/420,
 sixth {6}=-c6/126.

These are MODEL sector values. Exact filtered ordinary-pair reduction is
CLOSED with its filtered value; it is not automatically equal to the sharp
131/420 at fixed R. Fifth, sixth nonexact and any sharp/filter replacement
remain arithmetic/model-identification debts.

|consumer|model defect|uncharged model coefficient|actual theorem coefficient|
|---|---|---|---|
|frozen cubic square|35116876419/344102500000|1-2 times that rational|OPEN arithmetic closure|
|safe disjoint proxy quadratic|1/4|1/2|no >79 possible; bounded transfer unbuilt|
|c5-zero cubic example|157/787|473/787|OPEN sixth/bounded transfer, below79 already|

For the frozen square ONLY, the inherited band payment is
128952763/92407500000 and variance payment 26060119/12734908593750.
Its ideal paid-model slack is 27704610381502/17886179119921875 and relaxed
slack 52897896569489/572357731837500000. The ideal conditional paid-model
coefficient is 56741962902005141/71544716479687500, about79.3098%.
These payments are not actual closure of the inaccessible arithmetic.
Selected-section/weighted reprojection has the previously proved limiting
o(1) under its inherited hypotheses and is counted separately.

New candidates cannot reuse the old curvature payment. The general formula
for a valid bounded realization f is 3||f''||infinity/(pi^2 R) for that
inherited band interface; a finite certified bound must be supplied anew.
The sufficient lower-variance charge -2c2/(pi^2 R) applies when c2<0;
if c2>0 the known LOWER variance gate does not bound c2*mu2 from above, so
an upper gate is needed. The quadratic/cubic examples are model examples,
not fully paid theorem consumers. Their extra charge is recorded as UNKNOWN,
not zero. No c4!=0 experiment is performed because no usable newly CLOSED
fourth theorem with a payable bound is supplied.

## 8. Exact Pareto outer bound, not an invented frontier

The same positive quadrature gives for ANY centered c4=0 polynomial

 E_model=Q[P]+c5/36 >=1151/9450+c5/36.                            (8)

It matches the sixth moment exactly and is valid regardless of c6. Thus
model >79 necessarily requires c5<-127/210 even BEFORE theorem charges.
This is an exact outer bound quantifying unavoidable fifth dependence in
this model normalization. It does not say that the bound is attained.
The c6=0 boundary under PSD/c4=0 is degree two and has exact optimum E=1/4.
The c5=0 slice is excluded by (7). These are rigorous boundary/outer-frontier
certificates, not a complete optimized Pareto curve for c5/c6 and paid
percentage. The latter requires the actual region-coupling constraint and
new-candidate transfer costs. Its first undefined step is recorded explicitly.

## 9. Covered-region coefficients and weak-dual test

Every prior o(1) estimate at fixed R for support-empty/short-product cells
remains o(1) for any FIXED finite consumer coefficients: multiply its
normalized error by |c5| or c6, respectively. The constants change linearly;
they are not inherited with the old numerical value. The covered geometry
does not expand simply because a coefficient changes. At c5=0 the fifth
sector disappears but (7) excludes model >79. At c6=0 PSD forces c5=0 and
then the quadratic limit applies. At nonzero c6 the certified positive sixth
region persists in the disjoint proxy; in the actual object long alias,
FAR/TRANSITION and signed correlations cannot be removed by sharp signs.
Proper-power and exact nonzero alias closures remain fixed-coefficient o(1).
For a T-dependent consumer, new uniformity would be needed; none is used.

An integral weak-dual condition with a CHOSEN positive continuum measure can
certainly be negative for the old consumer: its integrated fifth/sixth model
net is favorable. This is already the model gain. It does not bound (3),
whose arithmetic measure is neither that chosen measure nor known positive.
A valid weak-dual witness must dominate the actual residual functional with
proved normalization and endpoint/filter errors. No LRSC dual witness for
that actual measure is supplied by the quadrature above: the quadrature
certifies only polynomial model objectives, with its exact stated scope.

## 10. Decision, residual theorem and density ladder

A is not justified: no exact arithmetic-safe consumer and fully paid margin
exists here. B is not justified: no strictly smaller actual residual region
is certified. C is proved ONLY for the stated disjoint sharp proxy, not for
an unidentified common actual kernel. Therefore the actual decision is D.

For the best preserved exact >79 MODEL consumer, residual status is C in
the user's debt taxonomy: SAME FULL RESTRICTED CORRELATION REMAINS. It still
requires the same selected-section signed inequality with coefficients
-A=-11501/12500 and B=137641/250000, together with every noncentral/alias
population and model-replacement charge. The exact safe proxy instead has
zero fifth/sixth debt but cannot reach the target. No intermediate U' with a
paid >79 certificate has been found.

The first mathematical prerequisite for the redesigned program is an exact
finite-band joint representation or a valid signed functional dual. It must
preserve the carrier, distinct/repeated prime restrictions, every closed lag
path, endpoint section and K_T(n,h), and prove that the proposed sign/payment
condition bounds the actual arithmetic sum. If positivity is the route,
the positive measure and common-domain coupling must be explicitly proved.
Absent that prerequisite, numerical region optimization cannot answer the
actual safe-consumer question, regardless of how accurately it is solved.

The methodology 'choose order; identify inaccessible spectrum; optimize to
annihilate it; certify the remainder' remains a possible research architecture.
This run shows why an actual positive/dual representation is required before
its region sign step. No convergence to density one or RH is claimed.

## 11. Files and reproducibility

Run:

 python src/wp84_theorem_aware_degree6_discovery.py
 python src/wp84_theorem_aware_degree6_verify.py

The numerical JSON is discovery-only, including failed solver statuses,
negative eigenvalues and unpromoted rational entry approximants. The exact
verifier checks all 15 principal minors of each rational Gram, all support
coefficients, every coefficient vector and model sector, the support-variable
translation falsifier, the rank-collapse dual, five-node fallback quadrature,
Pareto necessary c5 bound and sampled sign-transfer falsifier. It imports
the already certified open sixth boxes from the preserved parent certificate.

Outputs include EXACT_CERTIFICATE.json, REGION_SIGN_CERTIFICATE.json and
DUAL_OBSTRUCTION_CERTIFICATE.json. The dual scope is explicitly conditional
on the disjoint sharp proxy, except the independent c5=0 model bound. All
prior audit commits and notebooklm_packet are preserved. No push occurs.
