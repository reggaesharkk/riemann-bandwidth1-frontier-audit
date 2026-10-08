# Full-weight evaluation map: exact normal form and unresolved kernel

Parent f7391edb664b5cf695778970face063faadd3ad4; isolated branch
codex/c5-c6-attack-20261006. Decision **F**. First unresolved step:
characterize the kernel of actual prime/path evaluation on the retained
453-dimensional formal span, or produce legal exact evaluation minors.
No gauge/symmetry or analytic-estimation route is reopened here.

## Actual map and input space

Let V0 be the Q-vector space with 453 formal generators F_j, one for
each exported real full-weight representative. Calling V0 a formal space
avoids presupposing independence of its evaluated generators. The input
space X consists of actual heights T in the construction's regime, with
L=log(T/(2*pi)), X0=T/(2*pi), N=floor(exp(L-sqrt(L))), actual prescribed
a_phi(T), fixed R=6000 and the ONE declared admissible H, together with
the selected principal section I=[k_-,k_+] satisfying the frozen endpoint
requirements. Prime sets, leaf weights and window masks are determined
by those inputs. They are NOT freely chosen coordinate probes.

If the construction fixes a particular endpoint selector, restrict X to
its graph. Allowing all good endpoint choices defines a larger domain:
a rank witness on that larger domain need not apply to a particular
selector. Likewise varying a_phi freely would change the map. No claimed
rank result depends on those unproved enlargements. This audit does not
invent a finite-height good-endpoint certificate.

Define E:V0->Functions(X,R) by Q-linear arithmetic evaluation. Every F_j
is the REAL part of the complete sum below with its representative
b,epsilon,pi and original admissible alias list. The external frozen
consumer coefficient alpha_j=|raw orbit_j| omega_b is recorded separately;
it does not change the definition of F_j. Use omega_5=-11501/12500 and
omega_6=137641/250000 in the full consumer.

For each exact block B of pi choose distinct ordinary primes q_B<=N.
Set p_j=q_[j], nu_B=|B|, e_B=sum_(j in B)epsilon_j,
alpha_p=log p/L, lambda=sum_j epsilon_j log p_j. Retain the original
slot-window intersections chi. No Möbius factor occurs in the original
ordinary-prime sum. If an exact Vaughan/HB expansion is used it introduces
Möbius factors and compensators algebraically; none is inserted into this
original map or assumed to vanish.

For all |l_j|<=R with sum l_j=0, set u_0=0, u_j=sum_(i<=j)l_i,
imin=k_- -min u, M=max(0,d'-range u), d'=k_+-k_-+1. Define

    c_p=-log p/(a_phi L sqrt p),
    f_0^epsilon(alpha)=1-alpha,
    f_l^epsilon(alpha)=(1-exp(2*pi*i*epsilon*l*alpha))
                         /(2*pi*i*epsilon*l), l!=0,
    W=chi prod_j c_(p_j) f_l_j^epsilon_j(alpha_(p_j))
             exp(2*pi*i*sum_j epsilon_j*u_(j-1)*alpha_(p_j)),
    K=exp(i*T*lambda+2*pi*i*imin*lambda/L)/d'
             sum_(k=0..M-1)exp(2*pi*i*k*lambda/L).

Then F_j=Re sum_(distinct q_B) sum_(closed l) sum_(m in its alias list)
W K 1_(0<|lambda-mL|<=H/T), with the frozen nearest residual cell
[-L/2,L/2). Empty M is zero. Exact delta=0 is excluded. The prime
multiplicities, equality mask, Fourier displacements, carrier, normalization,
selected section and conjugate pairing all remain. Raw cumulant coefficient
is 1; there is no new connected-cumulant subtraction.

The constructor JSON contains every representative and EVERY raw orbit
origin, so the symbolic formula is not restricted to a phase exponent
catalogue. All 453 original definitions are pinned by source SHA256 and
individual canonical descriptor fingerprints.

## Exact Fourier numerator normal form

For a block let z_B=exp(2*pi*i*log q_B/L), h=(pi*i)^(-1), and
alpha_B=log q_B/L. Before actual evaluation, filter products expand in

    Q[h, alpha_B, z_B, z_B^-1].

For nonzero l the two terms have rational coefficients
+1/(2*epsilon*l), -1/(2*epsilon*l), h-degree one, and z-degrees
0, epsilon*l. For l=0 use 1-alpha_B. The executable constructor multiplies
these terms, combines exactly equal exponent vectors after imposing pi,
and removes zero rational coefficients. At most 2^b terms arise before
combination for an individual path. The independent replay expands by
subset choices instead of iterative multiplication.

The remaining factors belong to an extension containing log q_B,
sqrt(q_B), a_phi, L, carrier exponentials and actual window/endpoint
indicators. These are not independent algebraic indeterminates under E.
One may work in a formal extension ring to retain expressions, but cannot
call its monomials a faithful Q-basis of evaluated functions. Real-part
projection can introduce additional relations. Different q choices,
paths or origins may also coalesce after evaluation. These are the
unresolved kernel questions, not a numerical tolerance issue.

The actual arithmetic atom set depends on T (prime cutoff, alias windows,
endpoint counts). Over the full input domain an exact coefficient object
is a symbolic family indexed by all possible prime/path/root assignments,
with parameter-dependent masks. A finite 453-by-453 integer matrix does
NOT result merely from labelling that family. No complete faithful finite
atom coefficient matrix A has been constructed in this audit.

The exported sparse matrix is explicitly the FORMAL TAGGED incidence
minor I_453. Its rank over Q is 453, kernel zero, fifth/sixth labelled
blocks 72 and 381, formal intersection zero. It records source identity
and reconstruction only. It is not substituted for the requested
arithmetic matrix A, and no analytic conclusion follows from its
nonzero determinant. Computing it modulo any prime would repeat this
formal result, not certify actual independence.

## Exact specialization tests and the obstruction

A legal rank witness must specify actual inputs in X and certify exact
values or certified enclosures of a nonzero minor. Selecting a prime
assignment, deleting all but one Fourier path, changing prime windows,
introducing independent atom amplitudes, or setting carrier variables
freely are not evaluations in X. They would probe a different map.
Distinct labelled prime atoms alone therefore do not supply triangular
evaluation witnesses.

As an exact filter diagnostic, X0=121, q=11 gives alpha=1/2 and z=-1,
so f_2^-=0, proved directly in the expanded Laurent form. The ordinary
prime is within the natural cutoff: log(121)=2 log(11), and
log(11)>2 implies L-sqrt(L)>log(11). This diagnostic identifies an
actual evaluation relation in a formal filter ring. It does not claim
that a full F_j vanishes at that height, that the endpoints are selected
good endpoints there, or that a vector in V0 is a GLOBAL kernel vector.
A zero at one input is insufficient to disprove injectivity into Functions(X).
Thus it does not justify decision D about the map restricted to the
453-span. It does rule out treating all formal filter variables as freely
independent numerical probes at that height.

No exact nonzero specialization minor is obtained. The best certified
analytic bounds here remain 0<=rank(E)<=453. This lower bound is the
trivial bound and is not presented as decision C or as substantive
independence progress. The carrier exp(i*T*log ratio) is generally
transcendental at simple rational X0; requiring exact rational evaluations
by replacing it with a rational would alter the map. Rigorous interval
minors are possible in principle, but would require full fixed-R sums,
actual endpoint eligibility, and certified evaluation error. The existing
floating zero-lag diagnostic is none of those, so is not reused as a rank
witness. Bareiss/modular reconstruction has no actual integer evaluation
matrix to operate on yet.

## Kernel and fifth/sixth structure

No nonzero global vector c with sum c_j E(F_j)=0 is proved. Absence of a
found vector is not proof ker E=0. Analytic nullity is UNKNOWN, with the
formal-domain relation dim ker E=453-rank E and hence range [0,453].
There is no kernel basis to classify as fifth, sixth, mixed, alias, path
or endpoint.

The formal 72/381 block decomposition is exact. Analytic ranks obey
0<=r5<=72 and 0<=r6<=381. The actual intersection dimension is UNKNOWN;
it obeys the general identity rank(E)=r5+r6-dim(V5 intersect V6).
Parity of net prime exponents is preserved by the frozen definitions,
but distinct exponent labels are not a proved faithful function-space
basis. Therefore neither a nonzero intersection nor zero intersection
is promoted from those labels. No fifth/sixth identity is added.

## Reconstruction, corruption checks and budget

All 453 definitions are checked against their source records, including
raw origins, multiplicities, signs, aliases and full formulas. The replay
compares 1,359 exact path-filter expansions (zero lag and two nonzero
closed paths per representative) by two independent expansion algorithms.
This validates the finite expansion machinery; the general formula, not
finite sampling, covers all R6000 paths.

The producer changes separately the coefficient, alias, equality labels,
multiplicity and Fourier-displacement constraint in every descriptor:
2,265 deliberate corruptions are detected. These are provenance/constructor
integrity tests. They do NOT prove that every such edit produces unequal
arithmetic functions. A change can be annihilated by a genuine evaluation
identity, which is exactly why hashes are not a rank theorem. Matrix
scope and all unknown analytic-rank fields are independently checked.

No r<453 is certified and no reconstruction into a smaller analytic basis
is available. No new common arithmetic threshold follows. The previous
sufficient bound 1.7670578586835696e-8 and its exact l1 mass remain
unchanged and unproved. No cost is paid by a formal matrix rank or a
single-height vanishing filter. Strict >79 remains OPEN, charge UNKNOWN.

**F. INCONCLUSIVE:** the first unsolved step is faithfulness/kernel
characterization of actual prime/path evaluation on V0, or a legal exact
specialization minor providing an analytic lower bound. No injectivity,
nontrivial kernel, intersection identity or consumer obstruction is claimed.

Artifacts: src/wp84_full_weight_evaluation_map.py and independent
src/wp84_full_weight_evaluation_replay.py; full constructor JSON, explicitly
formal coefficient matrix CSV, kernel/rank-status certificate, and
corruption-test JSON. No new analogy, literature search or number-theoretic
bound was attempted. Prior audit commits and notebooklm_packet are preserved.
