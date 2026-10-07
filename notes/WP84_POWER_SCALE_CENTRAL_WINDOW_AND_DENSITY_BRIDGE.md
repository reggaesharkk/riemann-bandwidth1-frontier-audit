# Power-scale central window and density-to-rigidity audit

Parent: 95458d6cf49466f406fa0c8444aeef5230cd816e. Date: 2026-10-07.
Branch codex/c5-c6-attack-20261006. Local additive audit; no push.

**Decision D: EVEN AFTER POWER-SCALE H, CURRENT NUMBER THEORY STILL MISSES
THE REQUIRED WEIGHTED CORRELATION.** This is a statement about the inspected
hypotheses, not a theorem that no future method can work. Power enlargement
removes the exponent endpoint obstruction for an UNWEIGHTED unrestricted d3
average. It does not remove prime restrictions, the n,h kernel, absolute
normalization, aliases or the model-identification debt. No first feasible
eta is certified. C would overstate matters: no lower bound proves that
actual tail costs necessarily exhaust the margin.

## 1. Exact scale and admissibility audit

Keep the original construction UNCHANGED:

 L=log(T/(2pi)), X=exp(L)=T/(2pi), N_prime=floor(exp(L-sqrt(L))),
 grid step=2pi/L, d=floor(TL/(2pi)), d'/d->1, R=6000,
 tau0=T+2pi k_minus/L, c_p=-log(p)/(a_phi L sqrt(p)), a_phi->1.

Use N0=N_cell=X^(6/5) only as the balanced PRODUCT scale. Set H=N0^eta.
It is not N_prime^eta. Put z=H/T=(2pi)^(-1)X^(6eta/5-1).
The exact condition for h=A-B, n=A is

 n(1-exp(z))<=h<=n(1-exp(-z)).                                  (1)

In the dyadic balanced cell N0/4<n<=4N0, N0/8<B<=8N0. For z<=1,
necessary |h|<=4eN0z=(2e/pi)N0^(1/6+eta), and sufficient symmetric
|h|<=N0z/(4e)=N0^(1/6+eta)/(8pi e), subject to the coefficient supports.

The partition has a shrinking logarithmic resonance width iff 0<eta<5/6.
This is an admissible PARTITION interval, not a proved consumer window.
All original prime-square normalization, matrix dimension, lower gates,
principal section, endpoint reprojection and zero-count interfaces use the
same N_prime,L,T and are untouched by changing a label in the partition.
Their original theorem status is inherited, not upgraded here. Proper-power
bounded-signed-gate equivalence and exact nonzero alias disposal remain
permanently CLOSED before this partition, independently of H.

|Additional step|eta restriction|meaning|
|---|---|---|
|shrinking central window H/T->0; disjoint alias cores eventually|0<eta<5/6|exact partition compatible|
|old one-vs-many support disposal H=o(exp(sqrt(L)))|NO fixed eta>0|must withdraw this disposal|
|optional logarithm phase linearization H^2/T->0|eta<5/12|not used; summed unsigned mass still needs a bound|
|Topacogullari individual d3/d2 shift Q<<N0^(2/3)|eta<=1/2 with appropriate constants|unrestricted theorem only|
|BBMZ useful first average Q>=N0^(1/6+epsilon), Q<=N0^(1-epsilon)|epsilon<eta<5/6-epsilon|unweighted d3/d3 only|
|BBMZ second average Q>=N0^(1/3+epsilon)|eta>1/6+epsilon|unrestricted, different coefficients|

At eta=5/6 the core does not shrink; eta>5/6 eventually invalidates the
small-log expansion and may merge alias cores. These cases cannot identify
the same balanced continuum target by this argument. H does not alter the
prime cutoff; N_prime^3/T is still large and is not silently changed.

Across the full exponent simplex, n~X^gamma rather than X^(6/5).
The same global H yields shifts of size X^(gamma-1+6eta/5), or
n^(1-1/gamma+6eta/(5gamma)). Thus the balanced exponent 1/6+eta is not a
uniform statement for every cell. Larger gamma requires a separate analytic
range audit. At gamma<=1 the frozen sharp C5 kernel vanishes; this geometric
fact does not prove enlarged-core arithmetic contributions negligible.

## 2. Recomputed kernel partition and exact loss specifications

Let m=floor(lambda/L+1/2), xi=lambda-mL in [-L/2,L/2). Choose a symbolic
Lambda>=H with Lambda/T<L/2. CENTRAL is m=0, |xi|<=H/T; near ALIAS is
m!=0 with the same width; TRANSITION is H/T<|xi|<=Lambda/T in every bin;
FAR is Lambda/T<|xi|<=L/2. Exact xi=0 populations are separate. Because
H/T->0 and the natural support leaves extreme resonances separated by
sqrt(L), the prior alias core support table still holds for eta<5/6.
The one-prime gap log(T/N_prime) does NOT imply near support is empty at
this power width; retain every such ordinary population.

Use the oriented carrier-bearing primitive in each signed branch/bin/cell:

 dnu=sum_alpha w_alpha exp(i tau0 lambda_alpha) delta_xi_alpha,
 E(x)=nu((0,x])-comparison((0,x]),
 D(x)=D_d'(x/L), D_m(u)=m^(-1)sum_{k<m}exp(2pi i k u).

Negative xi is a separate branch, not a |lambda| count. Alias weights include
exp(iTmL). Define the exact sufficient functional

 Phi(E;a,b)=|D(b)E(b)|+|D(a)E(a)|
                 +integral_a^b |E(x)| |dD(x)/dx| dx.               (2)

For a=0 use E(0)=0 with exact-zero atoms removed. Abel bounds the REAL
residual by Phi, with consumer coefficients already inside w. Bounds are

 |D(x)|<=min(1,L/(2d'x)),
 |dD/dx|<=min(pi(d'-1)/L,pi/x+pi L/(4d'x^2)).                     (3)

Thus if |E|<=epsilon on [a,b], Phi<=epsilon times

 min(1,L/(2d'a))+min(1,L/(2d'b))
 +min(pi(d'-1)(b-a)/L,pi log(b/a)+pi L(1/a-1/b)/(4d')).            (4)

At a=0 the sufficient factor is 1+pi(d'-1)b/L. In particular the uniform
central primitive must be o(1/H) to prove o(1) by this crude bound. Weighted
primitive estimates using (2), rather than uniform suprema, can be sharper.

The requested rigorous loss functions can be specified conditionally as

 Loss_central(eta)=sum central Phi(E;0,H/T) + identification charges,
 Loss_transition(eta)=sum bins/branches Phi(E;H/T,Lambda/T),
 Loss_far(eta)=sum bins/branches Phi(E;Lambda/T,L/2),
 Loss_alias(eta)=sum nonzero bins/branches Phi(E;0,H/T).

These are explicit functions of the ACTUAL complex primitive, not evaluated
numerical functions of eta alone. Their certified numerical upper bounds
are OPEN for long products. No finite rigorous number is manufactured from
the kernel envelope. Comparison=0 is valid for a disposal claim; identifying
a nonzero filtered main term needs its own theorem.

A noncancelling fallback is U_region=sum_region |w| times the appropriate
kernel supremum. For FAR this is <=L T U_far/(2d'Lambda); for TRANSITION
<=L T U_transition/(2d'H); for either core <=U_core. Full tuple absolute
mass is at most C_R N_prime^(b/2) for degree b, with fixed R constants,
so even power H<N0^(5/6) does not make the resulting degree-six crude tail
bound small. This is failure of a bound, not a proved positive tail cost.
Kernel-frequency L2 relative tail <=LT/(2d'H)~pi N0^(-eta) improves, but
our measure is atomic, complex and prime restricted; it is not Lebesgue.

## 3. Mesoscopic exponent partition: exact geometry versus arithmetic

Partition the free signed coordinates v1,...,v_(b-1) in [-1,1] into half-open
intervals of maximum width delta(T); v_b=-sum free v. Intersect cells with
all support constraints and all sign sectors. Number of boxes is at most
ceil(2/delta)^(b-1): fifth O(delta^-4), sixth O(delta^-5). Empty cells are
discarded only by exact support. Assign every arithmetic tuple to exactly
one cell; the finite arithmetic partition has ZERO error even on cell faces.
No smooth prime-window replacement or discarded boundary is used.

For a closed walk let O_b(v)=(1-(max partial sums-min partial sums))_+.
Let C_b(v) be the sum over ordered connected partitions, coefficients +/-1,
of the corresponding overlap. There are 150 terms for b5 and 1082 for b6.
The free-coordinate forms have coefficients in {-1,0,1}. Across sup-norm
displacement delta, each spread changes by <=2(b-1)delta. Thus C_b has
Lipschitz bound 2(b-1)t_b delta, O_b has bound 2(b-1)delta, and |C_b|<=t_b.
The product F_b=O_b C_b therefore has global bound

 |F_b(v)-F_b(v')|<=4(b-1)t_b delta.

With domain volume <=2^(b-1), the midpoint/Riemann error is <=38400delta
for fifth and <=692480delta for connected sixth. These deliberately coarse
constants are rigorous, include zero-support regions, and prove convergence
for EVERY candidate delta->0. Positive/negative parts have the same modulus,
so favorable/dangerous connected masses admit the same enclosures. This is
a usable certified refinement procedure, not an arithmetic transference.

If a boundary strip of thickness t is explicitly removed, a hyperplane
with integer normal a!=0 inside the cube has strip volume <=2^b t/||a||inf.
Sum this over the actual support/arrangement walls and multiply the density
bound t_b. Without removal the geometric interface charge is zero. The
natural cutoff differs from alpha<=1 by thickness 1/sqrt(L); a union bound
on the b leaf faces gives geometric O_b(1/sqrt(L)). Arithmetic boundary
mass does not follow from this Lebesgue calculation.

|delta|fifth/sixth box counts|geometric total error|arithmetic uniformity|
|---|---|---|---|
|1/loglog T|O((loglog T)^4), O((loglog T)^5)|O(1/loglog T)|no growing-cell transfer proved|
|L^(-a), a>0|O(L^(4a)), O(L^(5a))|O(L^(-a))|per-cell errors must beat these counts|
|N0^(-epsilon_cell)|O(N0^(4epsilon_cell)), O(N0^(5epsilon_cell))|O(N0^(-epsilon_cell))|requires uniform power saving stronger than total count|

Coefficient bounds are uniform in cells: |log p/(a_phi L)|<=C,
|f_l^epsilon(alpha)|<=1; finite lag phases have modulus one. Each path
weight <=C_b/sqrt(AB), with R-dependent path count fixed. Hard windows add
BV jumps, and their variation grows with the partition. Smooth partitions
introduce derivatives delta^-j. Constants of a fixed smooth divisor theorem
cannot be assumed uniform as delta shrinks. A per-cell residual <=E_T yields
only O(delta^-5 E_T) in the joint ledger. This accumulated arithmetic error
is OPEN for all three meshes.

## 4. Global model simplex, sign and cumulative masses

For each sign pattern sigma, alpha_j>=0, v_j=sigma_j alpha_j, balance
sum sigma_j alpha_j=0, alpha_j<=1, and O_b(v)>0. Eliminate the last signed
leaf using this equality; use the induced free-coordinate measure d alpha_1
...d alpha_(b-1), NOT Euclidean surface measure (which differs by a constant).
The fifth connected model is

 sum_sigma integral_{Omega5,sigma} O5(sigma alpha) C5(sigma alpha) d alpha_free
       =1/36.                                                     (5)

Patterns with C5>0 require gamma=sum_positive alpha=sum_negative alpha>1.
The preserved exact pointwise theorem proves C5>=0 on the entire outer
support and C5<=max(0,gamma-1). Fifth contribution to the signed consumer
is -A F5, A=11501/12500: favorable mass exactly 1/36, dangerous mass zero,
and the zero-density part contributes zero. This states total model mass,
not actual prime transfer. The old balanced neighborhood fraction and the
zero limiting mass of a dyadic family remain unchanged; a mesoscopic cover
of the full cube converges to (5), rather than to one isolated point.

For sixth 2-vs-4 and 3-vs-3 write the SAME Omega6,sigma, with respectively
sum of two alpha equal sum of four, or sum of three equal sum of three.
The connected integrand is F6=O6 C6. Pair and {4,2} sectors live on additional
lower-dimensional closure manifolds and must use their own measures; a
single six-dimensional Lebesgue density does not include these diagonals.
Frozen sharp totals are

 {2,2,2}:131/420, {4,2}:-23/420, {6}:-1/126,
 total sixth=157/630.                                             (6)

No pointwise identification of a fifth cell and a sixth cell is established.
Consequently a scalar 'joint density' on one exponent simplex is not yet
defined. The legitimate object is a signed measure on the DISJOINT UNION of
fifth, sixth connected, and sixth closure domains, with weights -A and B=
137641/250000. Its net consumer integral is -A/36+B*157/630. To speak of
pointwise joint cancellation requires an explicit coupling theorem; (12)
of the non-Gaussian first-strike note is the actual global arithmetic gate,
not such a coupling theorem.

Connected sixth favorable region is F6<0, dangerous F6>0, negligible F6=0.
Let P6=integral(F6)_+, M6=integral(-F6)_+. Exact cumulative identity:

 M6-P6=1/126, 0<=P6+M6<=34624.                                   (7)

Unlike fifth, neither mass is inferred individually from the signed total.
The verifier certifies NONZERO regions of each sign by excluding every
ordered-partition wall and exactly integrating the affine-product kernel:

 dangerous 3-vs-3 box mass
   7994080087/1000000000000000000000000000000000000,
 favorable 2-vs-4 box absolute mass
   824753144241637/27000000000000000000000000000000000000000000.

Centers, radii, kernels and outer overlaps are machine recorded in the
certificate. Thus P6 is at least the first mass and M6 at least the second;
(7) gives P6<=(34624-1/126)/2, M6<=(34624+1/126)/2. These coarse certified
cumulative enclosures do NOT claim an exact global positive/negative split
or establish a useful consumer gain. The mesh rule above converges with an
explicit error; full fine integration and filtered identification remain
unperformed, since even perfect sharp geometry would not close the arithmetic
stop gate. Pair and {4,2} aggregate signs in (6) do not certify pointwise
signs of their placement densities.

## 5. Literature threshold: relative saving is not our absolute saving

[BBMZ, Theorems 1/2](https://arxiv.org/pdf/1101.5464) concerns unrestricted
d3(n)d3(n+h), N<n<=2N. With Delta its singular-series discrepancy,

 sum_{h<=Q}Delta <<(Q^2+Q^(1/2)N^(13/12))N^epsilon.

For Q=N0^(1/6+eta), RELATIVE to N0 Q the exponents are eta-5/6 and -eta/2;
so a fixed eta>0 indeed supplies a relative power saving. But our product
coefficients have scale 1/N0, not 1/(N0 Q). Even a hypothetical identical
prime-restricted bound, divided by N0, has exponents

 -2/3+2eta and 1/6+eta/2.                                         (8)

The latter is positive for EVERY eta>0. Therefore that theorem-scale
absolute bound does not yield o(1), much less either fixed small ledger.
This does not prove the actual signed sum large; it shows that simply
crossing the endpoint cannot be the entire repair. The theorem is for an
unweighted first mean; an arbitrary complex h-weight would need a separate
uniform partial-sum/BV argument. Its second mean requires eta>1/6 plus an
epsilon gap and gives an L2 error with a coefficient-dependent power delta;
Cauchy pays the weight's L2 norm and does not remove our n-dependent kernel.

[Topacogullari 2015, 1.1/1.2](https://arxiv.org/pdf/1506.02608) supplies
unrestricted d3/d2 asymptotics for h<<N0^(2/3): sharp error N0^(8/9+epsilon),
smooth N0^(5/6+theta/3+epsilon). Sharp absolute summation divided by N0
costs N0^(1/18+eta); theta=7/64 gives smooth N0^(7/192+eta). Both grow.
The fixed smooth cutoff constants also do not license our T-dependent
weights. Kuznetsov/Voronoi are the analytic mechanism in that paper, not a
proved restricted-coefficient identity. No theorem in this audit certifies
a joint prime-restricted d2/d3 and d2/d4 or d3/d3 weighted saving at (8).

## 6. Transference and the exact weighted average

For each closed lag path keep the arrays from the previous note. The fifth
core is EXACTLY

 A sum_l sum_h sum_n a2,l(n) conjugate(a3,l(n-h))
   1_{gcd(n,h)=1} 1_{(1)} omega_T(n,h),
 omega_T(n,h)=exp(i tau0 log(n/(n-h)))
                     D_d'(log(n/(n-h))/L).                        (9)

The sixth companions replace a2/a3 by a3/a3 or a2/a4 and A by B; all signs
and orientation/path placements are retained. Expand D if useful:

 omega_T(n,h)=d'^(-1)sum_{k<d'}[n/(n-h)]^(i(tau0+2pi k/L)).

This extra averaging is exact and must stay inside a spectral/dispersion
estimate. It is not an average over independent shifts with positive weights.
The restriction (1) depends on n, as does every carrier. No exact h-only
factorization exists.

One can use Lambda=mu*log with exact prime-power corrections, or finite
Vaughan/Heath-Brown decompositions of each individual leaf. The resulting
finite factor-type sums retain Mobius signs, coprimality (insert its exact
divisor sum if desired), slot filters, dyadic restrictions and (9). This
is an algebraic decomposition, not a proof of controlled analytic errors.
Buchstab has rough-number residuals; weighted sieve majorants lose the
negative fifth sign or complex phase. No uniform norm/derivative estimate
for ALL resulting Type I/II/III shifted sums is supplied by the inspected
divisor statements. Thus finite linear-combination syntax is possible but
a controlled one-lemma transference conclusion is NOT established. Even
coefficient transfer with the same (8) error would be insufficient.

## 7. Past-present-future bridge: exact inverse and falsifiers

On a Fourier mode e^(it lambda), U_s shifts t by s. Delta_s^2=U_s+U_-s-2I
has multiplier -4sin^2(s lambda/2). Project away the central spectrum FIRST.
For a fixed s and a noncentral set E excluding every zero 2pi j/s,

 integral_E D(lambda/L)dnu
   = integral_E [-1/(4sin^2(s lambda/2))]D(lambda/L)
                                    d(Delta_s^2 nu).              (10)

There are no boundary terms for an exact spectral projector on the full
field. If E contains multiplier zeros, add their ORIGINAL contribution
explicitly; noncentrality alone does not remove these zeros. If translations
are implemented on a finite section, extending/truncating the time interval
creates endpoint integrals: for an integrand F and interval [u,v],
 integral_u^v(F(t+s)-F(t))dt=integral_v^(v+s)F-integral_u^(u+s)F.
The -s version similarly gives the lower and upper opposite strips.
Their weighted moments must be bounded, not declared zero.

A fixed s small enough to have no other zero for |lambda|<=6L costs an
inverse growing like (L T/H)^2 near the core boundary. Choosing s~T/H
instead introduces many noncentral zeros. Falsifier: a single spectral atom
at lambda=2pi/s has bridge zero and nonzero original contribution.

A better-conditioned EXACT average is

 M_a(lambda)=a integral_0^(1/a)4sin^2(s lambda/2)ds
            =2(1-sin(lambda/a)/(lambda/a)), a=H/T.                 (11)

For |lambda|>=a, 19/60<=M_a<=4. Proof: on 1<=|u|<=2,
sin u/u<=1-u^2/6+u^4/120<=101/120; for |u|>=2 use 1/|u|<=1/2.
Hence the inverse costs at most 60/19. Applying the bridge separately to
alias residual xi needs demodulation and the alias projector; a physical
translation in lambda does not automatically operate on xi.

Equation (10) with the averaged multiplier is well conditioned away from
zero, but M_a stays bounded instead of growing with frequency. Its inverse
provides NO new asymptotic decay. The bridged primitive has not been proved
smaller than the original carrier-bearing primitive. In absolute variation,
bridging costs up to 4 and inverse recovery can pay it back. It could expose
cancellation if a NEW arithmetic estimate were proved, but it does not
supply one. Central modes remain in (9). Translations reach times T/H;
relative strip width is 1/H, but a bulk high-moment/weighted endpoint theorem
is still needed to convert that fraction into an o(1) charge.

## 8. Full ledger and exact remaining theorem

|charge|eta dependence|certified status|
|---|---|---|
|proper powers; exact nonzero aliases|o(1) independent of eta|CLOSED, paid zero in limit|
|principal weighted reprojection|inherited o(1), construction unchanged|separate from arithmetic|
|mesoscopic SHARP geometric quadrature|<=A*38400delta+B*692480delta for connected portions|CLOSED geometry only|
|finite-R filtered-to-sharp identification|not supplied by this partition|OPEN if sharp model used|
|central|equations (2),(9), H=N0^eta|OPEN|
|transition|equations (2)-(4), a=H/T|OPEN|
|far|equations (2)-(4), a=Lambda/T|OPEN|
|near aliases|dilated n versus X^m q correlation|OPEN|
|bridge finite-section endpoint strips|translation range <=T/H|OPEN additional charge if used|
|band|128952763/92407500000|already paid once|
|variance|26060119/12734908593750|already paid once|

The ideal slack is 27704610381502/17886179119921875; relaxed slack is
52897896569489/572357731837500000. Their decimal values are respectively
0.00154893955806605 and 0.00009242103954753147. All added positive residual
charges must fit STRICTLY inside the selected slack; unknowns are not zero.
No objective function with numerical finite upper costs has been established,
so no rigorous feasibility search or first feasible eta exists in this audit.
The geometric error tends to zero for slow meshes, but this does not pay
the arithmetic or filtered-model charges.

The sufficient remaining theorem is still the actual SAME-section signed
arithmetic inequality from the accepted note:

 limsup Re[-A N5,T,R+B N6,T,R]
       <=J_star-B Pair6_R-epsilon, epsilon>0,
 J_star=64788151489666079/572357731837500000, R=6000.                (12)

N5,N6 include ALL nonexact ordinary sectors. A power-window route must prove
(9) jointly with its sixth companions uniformly across a mesoscopic cover,
PLUS the oriented tail/dilated-alias bounds. A transference lemma strong
enough to imply all these estimates would already be a new arithmetic
closure theorem, not merely the existing unweighted divisor theorem with
prime restrictions inserted. Required normalized aggregate error is strictly
less than the chosen slack after all other charges. Exact assertions and
bounds above are recorded in the verifier; none are a prime theorem.

## 9. Density ladder: research architecture only

Define kappa_m as the supremum of proportions certified by a specified
family of valid consumers using connected moments through order m, with
ALL arithmetic, analytic and zero-side interfaces proved. Keep the
architecture and cost conventions explicit. If families are nested and
lower-order certificates can be embedded with identical costs, monotonicity
follows by set inclusion. Those hypotheses are not established by merely
having order-2 and order-6 formulae, so monotonicity is not assumed here.
An open >79 consumer is not a certified value of kappa_6.

Higher degree potentially changes approximation and sign control, but also
requires new joint arithmetic moments and tail/conditioning costs. No proof
shows that attainable kappa_m approaches 1. Even a proved limit 1 would give
a density-one statement about simple critical-line zeros, with the counting
normalization specified, not full RH. An infinite exceptional set with count
about sqrt(M) among M zeros has density zero; a finite exceptional set also
has density zero. RH excludes EVERY off-line nontrivial zero and does not
by itself assert simplicity of every critical-line zero.

## 10. Precise density-to-rigidity requirement

A primary criterion is [Connes--Consani, Appendix C, Proposition C.1](https://alainconnes.org/wp-content/uploads/Selecta.pdf). On smooth compactly
supported multiplicative tests g with Mellin transform vanishing at 0 and 1
(and permitted additional finite constraints), their explicit-formula sign
convention is sum_v W_v(g*conjugate(g)^7)<=0 iff RH. Define Q_W to be its
negative, so the required convention is Q_W(g)>=0. The logarithmic/unitary
change of variables converts this to the corresponding additive test form.
This criterion tests every admissible function, not an asymptotic zero density.

A sufficient completeness theorem for a finite-certificate architecture is:
for every admissible g, construct g_j in finite stages V_j, with support
contained in a fixed compact set for that g, all required Mellin constraints
preserved, g_j->g in the smooth-test topology; identify each certified matrix
quadratic form with Q_W on V_j, including a proved error tending to zero;
certify positivity for ALL complex linear combinations in V_j, not just
individual basis elements; and prove continuity of Q_W under this convergence.
Then Q_W(g)=lim Q_W(g_j)>=0, and the criterion implies RH. Uniform coercive
bounds are a possible way to control errors; strict coercivity itself is
not logically necessary if exact positivity and continuity already hold.
An L2-dense set alone is insufficient for a distributional form without
its own continuity theorem. Polarization controls cross terms. Disjoint
finite positive tests do not certify positivity of their linear span.

No map from the current moment consumers into such dense V_j is proved.
The existing matrix positivity is not already the Weil quadratic form;
trace-moment bounds and zero proportions do not imply Q_W positivity.
A separate rigidity alternative would require a theorem saying that any
single off-line zero forces a definite violation of some certified finite
stage, independent of its density. Neither completeness nor this separation
property is established. This architecture note has no role in the >79 ledger.

## 11. Verification and scope

Run python src/wp84_power_scale_central_window_verify.py.
It checks rational shift exponents, BBMZ normalization exponents, exact
averaged bridge multiplier and inverse bound constants, connected-sixth
term count, favorable/dangerous affine boxes, frozen consumer budgets,
and certificate flags. The two interrupted-run verifiers and the exact
restricted convolution replay are rerun as regressions. Prior commits and
the untracked notebooklm_packet remain preserved. Strict >79 remains OPEN.
