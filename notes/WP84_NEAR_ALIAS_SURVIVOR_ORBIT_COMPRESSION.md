# Exact near-alias orbit compression: formal structure and unresolved functional rank

Parent dc71147aab7f7a3609fc2d0ca0a09cf0dfb32bf9; isolated branch
codex/c5-c6-attack-20261006. No push. No analytic theorem search,
Central/LongTail attack, H optimization or consumer change.

**Decision F.** The first uncertified structural step is identifying the
actual path-weighted correlations that have the same reduced phase
pattern. The reduced-factor catalogue is not a proven functional basis.
An incidence rank is not an analytic independence theorem.

## Frozen source and exact exported records

The source has 8,740 sign/equality classes (1,132 fifth, 7,608 sixth),
21,588 class/alias incidences, 105 reduced oriented phase-factor patterns,
and 336 alias-retaining phase types. The canonical ledger JSON contains
one record per pattern, all original sign words and equality partitions,
all admissible alias integers, exact consumer coefficient, raw cumulant
coefficient 1, original prime restrictions, symbolic Fourier/path weights,
sampled kernel, conjugate identifier and arithmetic classification.
No cumulant subtraction is invented: these are the frozen raw trace terms.

For a record (b,a,c), a and c are the positive and negative prime exponent
multisets. Its original slots remain in the origins list. Assign distinct
ordinary primes q_B to exact equality blocks, p_j=q_[j], with
q_B<=floor(exp(L-sqrt(L))), L=log X, X=T/(2*pi). Block windows are
intersections of original slot windows. The record is a finite symbolic
family over all closed paths l in [-6000,6000]^b. Put

    u_0=0, u_j=sum_(i<=j)l_i, alpha_j=log p_j/L,
    imin=k_- -min u_j,
    M=max(0,d'-max u_j+min u_j), d'=k_+-k_-+1,
    lambda=sum_j epsilon_j log p_j,
    f_0^epsilon(alpha)=1-alpha,
    f_l^+(alpha)=(1-exp(2*pi*i*l*alpha))/(2*pi*i*l),
    f_l^-=conj(f_l^+),
    W=chi prod_j[-log p_j/(a_phi L sqrt p_j)*f_l_j^epsilon_j(alpha_j)]
                exp(2*pi*i*sum_j epsilon_j*u_(j-1)*alpha_j),
    K=exp(i*T*lambda+2*pi*i*imin*lambda/L)/d'
                sum_(k=0..M-1)exp(2*pi*i*k*lambda/L).

Each atom is W K times the original near-alias indicator
0<|lambda-mL|<=H/T, with nearest residual cell [-L/2,L/2).
This formula and the origin list specify the FULL functional, rather than
just its reduced ratio. Balanced blocks cancel phase but retain their
prime sums, coefficient powers and path weights. Different origins can
therefore have the same reduced phase but different analytic weights.

## Certified symmetry and rejected identifications

One certified action is C2:

    epsilon -> -epsilon, lambda -> -lambda,
    (a,c,m) -> (c,a,-m), W -> conj(W), K -> conj(K).

The path l, prime assignment, principal section, M, imin and d' are
unchanged. All prime bounds and real window indicators are unchanged;
f_l^- is the conjugate of f_l^+, the path phase conjugates, and every
carrier/kernel exponential conjugates. The rational omega_b and raw
cumulant coefficient 1 are unchanged. This proves the involution of
complete correlations. Nonzero m ensures alias-type pairs have no fixed
points. At the phase-pattern level equal a=c can be a fixed point.

Dummy prime-label relabellings are legal when all block origins, windows,
nu and e are relabelled together; they change no sum. Permutations of
identical-role blocks are legal only under the same full-data condition.
The exponent multiset is already quotiented by those label changes.
Equal exponents ALONE do not establish identical roles: multiplicities,
original slots and Fourier weights may differ. Equality-block automorphisms
with identical full data are dummy-label actions, not extra cancellations.

Numerator/denominator exchange alone changes lambda and carrier. It is
accepted only as simultaneous conjugation. m negation alone changes the
window and is rejected. Fourier displacement negation alone changes u,
imin and path weights and is rejected alone.

Two additional FULL-PATH-SUM symmetries are certified. A cyclic rotation
by s slots rotates signs, prime slots, equality origins and lags together.
The new prefix list is u'_j=u_(s+j)-u_s, wrapping the closed path; its
root start is imin'=imin+u_s and M'=M. The W phase gains
exp(-2*pi*i*u_s*lambda/L), exactly compensated by the K root phase.
All leaf factors and real prime bounds are merely reordered. Path sets,
normalization and coefficients are unchanged.

Reversing slots and replacing the reversed lags by their negatives yields
u'_j=u_(b-j), with unchanged min/max and root kernel. For nonzero l,

    f_(-l)^epsilon(alpha)=exp(-2*pi*i*epsilon*l*alpha) f_l^epsilon(alpha).

The reversed slot starts at its old terminal vertex u_j instead of
u_(j-1), adding exp(2*pi*i*epsilon*l*alpha) to its path phase. These
cancel slot by slot; the l=0 identity is immediate. Thus W'=W, K'=K.
The reversal is a bijection of all closed paths with their original prime
assignments. It is not an identification of individual untransformed
path atoms. Both transformations preserve the actual identical natural
leaf cutoff and selected root section. Any additional nonidentical
window decoration must rotate/reverse with its origin; it cannot be
silently dropped. This audit uses the original full natural leaf ranges.

The resulting raw-class group is D_b times C2 (possibly nonfaithful on
individual classes), with canonical dummy prime-label relabelling.
No arbitrary slot permutation is inferred. The additional dihedral
actions do not change reduced exponent patterns or m, so the phase-orbit
counts below are unchanged. Scaling q by X^m does not preserve integer
primes, cutoff and weights. Different |m| cannot be identified this way.

## Exact orbit catalogue and coefficient aggregation

The certificate lists every lexicographically canonical orbit representative
and its size for the 105 phase patterns and 336 alias types. Each phase
orbit is generated by (a,c)->(c,a); each alias orbit by
(a,c,m)->(c,a,-m). These are certified orbits of the phase projection,
not assertions that a single unweighted kernel represents every origin.
The raw origin is paired with its sign-negated origin, preserving its
partition and full path sum. Adding the certified dihedral actions gives 453 explicit actual real
functionals, exported with their definitions and alias lists:

    C_j(T)=Re sum_(all ordinary prime assignments, closed paths,
                   listed admissible m) W_j K_j 1_near,
    NearAlias_surv(T)=sum_(j=0..452) alpha_j C_j(T),
    alpha_j=|O_j|*omega_b,
    omega_5=-11501/12500, omega_6=137641/250000.

Every dihedral/conjugate orbit O_j has the same raw coefficient; its
complete sum is |O_j| times the real part of its representative. If
conjugation fixes a dihedral orbit, that representative is already real. Imaginary combinations cancel; real combinations do not
cancel coefficient-wise. There are no zero coefficients in this retained
list. Within each degree the coefficients are proportional (indeed equal),
which is NOT a proof of proportional functionals. Raw class counts per
phase orbit, and the exact scalar totals omega_b times those counts, can
be reconstructed from the exported incidence rows. They are formal totals
only: different original path-weight functions cannot be merged by adding
those scalars. Every original class is counted once here; multiple m
values are inside that class functional, not duplicate raw coefficients.

## Incidence matrices, exact rank and limitations

The CSV has one row per raw class, mapping it to phase-pattern, phase-orbit
and full-data dihedral/conjugate-orbit identifiers. Three sparse 0/1 incidence
matrices are thereby completely specified. Every column has nonempty
support, supports are disjoint, and each row has a single 1. Consequently
their ranks over Q equal their numbers of columns, with no tolerance.
The certificate supplies row bases (one first row per column), all column
bases, and complete left-null bases e_r-e_first for each remaining row.
Right nullities are zero. These relations are relations between projected
incidence ROWS; they are not equations between differently weighted raw
prime correlations. The independent replay proves disjoint support
instead of invoking a floating matrix rank routine.

The raw-to-pattern incidence rank is 105, left nullity 8,635. The
raw-to-full-data-orbit incidence rank is 453, left nullity 8,287.
The phase-orbit incidence rank is 54, left nullity 8,686.
There are 51 size-two phase orbits and three singleton phase orbits;
all 168 alias orbits have size two.
Pattern-orbit rank/nullity and both orbit counts are in the certificate.
The minimal analytic rank and nullity are UNKNOWN. Even a rank-105
incidence projection does not prove analytic rank 105; conversely, 453
formal directions do not prove analytic independence. Therefore decision
B or C with an exact functional-basis dimension would be unsupported.

## Fifth/sixth and alias compression boundary

For every block e_B is congruent nu_B modulo 2, hence
sum |e_B| is congruent b modulo 2. Conjugation and prime relabelling
preserve this parity, so no fifth pattern and sixth pattern share a
certified phase orbit or conjugate-pair functional. The incidence matrix
remains block diagonal by degree. This proves no cross-degree merging
under the CERTIFIED group; it does not rule out deeper identities between
sums with different phase supports. No such identity is proved here.

Aliases are compressed only by simultaneous reciprocal/conjugation.
The alias-representative list in the certificate is the complete
irreducible list UNDER THIS GROUP, not a claim of universal irreducibility.
Distinct |m| have distinct centers X^m and disjoint residual cells when
H/T<L/2. Disjoint support is not proof of functional independence as T
varies, nor proof of identical distributions. No further support/scaling
equivalence is established.

Arithmetic types in the ledger use exact distinct exponent multisets and
multiplicity counts, not a free divisor-function replacement. All-one
2:3 and 3:3 are labelled restricted d2-d3 and restricted d3-d3;
1:2 is prime x semiprime, 2:2 semiprime x semiprime; larger products
are higher multilinear; repeated exponents are restricted prime-power
factor correlations; empty sides are one-sided higher-alias products.
These are shape labels, not applicability assertions for unrestricted
divisor theorems. Prime ranges, distinctness and weights stay attached.

## Budget, theorem package and symmetry-only falsifier

For the explicit 453 retained real functionals, a common bound
|C_j(T)|<=E(T) suffices by the triangle inequality with exact coefficient
mass S=sum_j|alpha_j|=163444421/31250. The certificate records S and the exact sufficient
full-allocation threshold E<=Delta_rel/S (approximately 1.76705785868357e-8), where
Delta_rel=52897896569489/572357731837500000. For share s it is
s*Delta_rel/S. This is the largest sufficient common bound using ONLY
these absolute constraints: synthetic C_j=sign(alpha_j)E attains S E.
No such common bound is achieved, and full allocation leaves no reserve.
It is not called the weakest arithmetic theorem or a minimal basis bound.

The genuinely weaker sufficient theorem is the single joint one-sided
inequality limsup sum_j alpha_j C_j(T)<=q_alias, with its original
ranges, fixed R, declared H and selected section, and an explicitly
allocated q_alias leaving reserve. This is a restatement of the survivor
obligation, not a collapse to one universal canonical correlation shape.
The smallest proven theorem PACKAGE or functional basis is unresolved.

For each retained formal direction set its real C_j to a nonzero t,
all others zero, and assign its conjugate the conjugate value. These
synthetic functionals obey the certified involution and any sufficiently
small individual norm cap. The response alpha_j*t is nonzero for every
j. Setting all C_j=sign(alpha_j)t yields S*t. This falsifies cancellation
from the certified symmetry and coefficient data ALONE. These abstract
values are not prime correlations, and need not satisfy an unknown
functional identity. Thus they do not prove arithmetic input necessary
on EACH analytically independent direction, because those directions
have not been determined. No actual budget obstruction follows.

Charge UNKNOWN; paid remaining allowance UNKNOWN. Strict >79 OPEN.
First unpaid STRUCTURAL step: prove or disprove the full-weight identities
needed to pass from phase orbits to a smallest correlation basis, beyond the certified
dihedral path transformations. No general near-alias estimate was launched.

Artifacts: src/wp84_near_alias_orbit_compression.py exports exact records,
incidence matrices, orbit representatives, coefficient and budget data;
src/wp84_near_alias_orbit_replay.py independently verifies these finite
certificates and the scope of the synthetic falsifier. Parent source
hashes are pinned. All prior audit commits and notebooklm_packet survive.
Verification: independent replay checks 72,960 exact rotation/reversal
path-phase and root-index compensation cases, and independently generates
the raw orbits by breadth-first closure. These finite checks accompany
the general symbolic proof above; they are not an analytic estimate.
Formal coefficient aggregation is separately exported in
WP84_NEAR_ALIAS_COEFFICIENT_AGGREGATION.csv.
