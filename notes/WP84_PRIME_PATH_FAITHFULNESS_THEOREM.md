# Prime/path faithfulness: carrier uniqueness and partial analytic ranks

Parent 73802f59532c2eb10db8f9689c886fc8ac901b64; isolated branch
codex/c5-c6-attack-20261006. No push. Faithfulness attack only.

**Decision F**, with new symbolic lower bounds:

    19 <= rank_5 <= 72,
    35 <= rank_6 <= 381,
    35 <= rank_total <= 453.

These are analytic independence bounds for the defined full natural-cutoff
functionals, not floating ranks or ranks of label matrices. The 54 selected
representatives are listed explicitly. Independence is proved separately
by degree; a joint rank 54 of the original normalized family is NOT claimed.
The remaining same-carrier amplitude identities and fifth/sixth intersection
are unresolved. Global nullity is between 0 and 418. Strict >79 stays OPEN.

## Three kernels and the actual map

V0 is the 453-dimensional formal Q-space with the frozen real generators.
K_formal={0} on these independent labels (the certified incidence map).
K_global consists of c in Q^453 such that sum c_j F_j(T)=0 for every
admissible actual input, with the prescribed normalization and selected
principal section. K_T is the kernel of a single finite-height evaluation,
not the intersection over heights. K_global is the intersection of the
corresponding K_T across the actual domain; its value is UNKNOWN.

A complex filter atom that is zero at X=121 has no implication of a
nonzero vector in K_global on the 453-span. Nor is it automatically a
relation among full F_j at that height: a single atom may vanish while
other assignments and paths do not. The scalar Q-linear finite-height
map can have a kernel without the function-valued map having one.

Use the complete constructor from WP84_EVALUATION_MAP_CONSTRUCTORS.json:
X=T/(2*pi), L=log X, N=floor(exp(L-sqrt(L))), actual a_phi(T),
R=6000, one declared fixed H>0, selected I=[k_-,k_+], d'=|I|.
Distinct block primes q_B<=N realize the exact partition pi, p_j=q_[j],
nu_B=|B|, e_B=sum_(j in B)epsilon_j. The ordinary-prime expression has
no inserted Möbius coefficients; its raw cumulant coefficient is 1.
For closed |l_j|<=R, u_0=0,u_j=sum_(i<=j)l_i,
imin=k_- -min u, M=max(0,d'-range u), lambda=sum epsilon_j log p_j,

    W=chi prod_j[-log p_j/(a_phi L sqrt p_j)
                        *f_l_j^epsilon_j(log p_j/L)]
            exp(2*pi*i*sum_j epsilon_j*u_(j-1)*log p_j/L),
    K=exp(i*T*lambda+2*pi*i*imin*lambda/L)/d'
            sum_(k=0..M-1)exp(2*pi*i*k*lambda/L),
    F_j=Re sum_(prime assignments,closed paths,listed m)
            W K 1_(0<|lambda-mL|<=H/T).

Use f_0=1-alpha and f_l^epsilon=(1-exp(2*pi*i*epsilon*l*alpha))
/(2*pi*i*epsilon*l) for l!=0. All endpoint, prime-window and equality
restrictions remain; no zero-lag-only diagnostic replaces F_j.
The external consumer coefficients remain |raw orbit_j| omega_b.

## Reduced rational carriers and exact grouping

Unique factorization gives

    lambda=log(A/B),
    A=prod_(e_B>0)q_B^e_B, B=prod_(e_B<0)q_B^(-e_B), gcd(A,B)=1.

Since real log is strictly increasing, lambda_1=lambda_2 iff the positive
ratios A_1/B_1 and A_2/B_2 are equal. Reduced rational equality is
equivalent to equality of every prime valuation. For a finite prime set
P, the valuation vector v in Z^P determines lambda=sum v_p log p;
if sum v_p log p=0, exponentiation gives prod p^v_p=1, so v=0.
Thus distinct valuation vectors give distinct frequencies. Real-part
projection identifies the reciprocal pair lambda,-lambda, and this is
why the witness supports are unordered numerator/denominator multisets.

On a fixed-combinatorics cell the expression is a finite sum

    a_phi(T)^b F_j(T)=sum_lambda A_(j,lambda)(z) exp(i*T*lambda),
    z=1/log(T/(2*pi)),

including negative lambda after taking the real part. The amplitudes
A_(j,lambda) are entire germs in z formed from finite polynomials in z
and exponentials exp(2*pi*i*rho*z), rho a fixed integer combination of
prime logarithms. Prime weights contribute z^b times constant log and
square-root factors. The root/Dirichlet sum contributes finitely many
exp(2*pi*i*(imin+k)*lambda*z)/d'. Displacement phases and the Fourier
numerators supply other exponentials in z. Zero-lag factors contribute
polynomials 1-z log p. All discrete endpoints and counts are frozen.
The finite root sum, rather than its sine quotient, avoids removable
singularities. This is an exact amplitude description, not a constant-
coefficient Dirichlet polynomial. The common normalization is removed
within one degree only; no analyticity of a_phi is assumed.

## Fixed-combinatorics cells and selected endpoints

On a bounded sufficiently small interval about a large height there are
finitely many relevant primes, partitions, paths and root/endpoint indices.
Natural cutoff and dimension floors are locally constant off their
boundaries. Tuple alias masks can change only at zeros of finitely many
real-analytic boundary equations (including exact delta=0). On compact
subintervals these zeros are isolated unless an equation is identically
zero; the constant cases do not create boundaries. Thus an open subcell
with fixed cutoff, active alias assignments, d and path support exists.
The full natural leaf windows in this frozen family are retained. No
additional arbitrary window is introduced for the witnesses.

For any fixed endpoint pair on such a subcell, a_phi^b F_j has the
analytic representation above. The actual selected endpoint rule need
not itself be analytic: with d fixed there are only finitely many possible
pairs. We will prove the required fixed-endpoint analytic expressions
are NONZERO for every positive-length section. A finite union of their
isolated zero sets cannot cover the open subcell. Consequently the
nonvanishing/independence argument applies even to an arbitrary actual
selector among these sections. This avoids declaring an uncertified
finite-height endpoint pair to be good.

The analytic continuation used below freezes the finite cell formula,
not the physical prime cutoff or alias masks at later heights. It is
legitimate only to test whether that analytic cell expression is
identically zero. It is NOT an assertion that the continued expression
is the physical observable outside its cell.

## Restricted uniqueness lemma: actual germ amplitudes

Lemma. Let finitely many distinct real lambda_r be given and let A_r(z)
be analytic at z=0, with their compositions analytic for T>2*pi. If

    sum_r A_r(1/log(T/(2*pi))) exp(i*T*lambda_r)=0

on a nonempty open interval, then every A_r is identically zero as a
germ, provided the finite expression analytically continues on T>2*pi.
This condition holds for the finite polynomial/exponential amplitudes
constructed above.

Proof. Analytic identity continuation extends the zero expression to all
T>2*pi. If some germ is nonzero, let k be the minimum order of vanishing.
Multiply by log(T/(2*pi))^k. Uniformly on [S,2S] as S tends to infinity,
the result is

    P(T)+O(1/log S), P(T)=sum_(ord A_r=k) c_r exp(i*T*lambda_r),

with at least one nonzero c_r. Therefore the mean square of P on [S,2S]
is O(1/(log S)^2). Direct integration gives that same mean square as
sum |c_r|^2+O(1/S), because each distinct-frequency cross integral is
bounded by 2/|lambda_r-lambda_s|. Contradiction. Hence all germs vanish.
This proves the lemma without assuming algebraic independence of prime
logarithms or invoking torus density.

For unconstrained analytic amplitudes the proposed uniqueness claim is
FALSE already with two distinct carriers: take a_1(T)=1 and
 a_2(T)=-exp(i*T*(lambda_1-lambda_2)). The terms cancel identically.
The fast carrier absorbed into a_2 destroys uniqueness. Such a function
is not an analytic germ in 1/log(T/(2*pi)) at zero. The restricted germ
hypothesis is the new justified mechanism; it does not automatically
prove that several full origins sharing one lambda have independent
amplitudes.

## Zero-lag leading coefficient and partial support independence

For every path, f_l^epsilon(log p*z)=O(z) when l!=0. At l=0 it has
constant term 1. Thus after removing a_phi^-b, ONLY the all-zero path
contributes to the coefficient of z^b. Its M=d', root count cancels the
normalization, and all its extra root phases have constant term 1.
For any retained reduced carrier, the leading real-character coefficient is

    (-1)^b/2 * sum_(assignments giving lambda or -lambda as applicable)
                 prod_B (log q_B)^nu_B / q_B^(nu_B/2).

It is strictly nonzero whenever at least one such assignment is active;
all summands have the same sign. Balanced blocks remain in this positive
weight. For reciprocal self-support the contributions add, not cancel.
This uses the FULL Fourier sum: nonzero-lag paths start at higher order
and cannot cancel its z^b coefficient. It is independent of the choice
of positive-length principal section.

Different reciprocal reduced exponent patterns have disjoint rational
carrier supports by unique factorization, since all block primes are
distinct. Select ONE retained representative per reciprocal phase-pattern
orbit. There are 19 fifth and 35 sixth supports, with explicit IDs in
WP84_PRIME_PATH_CARRIER_WITNESSES.json. Their formal incidence alone is
not the proof: the germ lemma, positive leading coefficient and legal
support cells below supply the faithfulness needed for this subfamily.

Suppose a nonzero Q-combination of the selected representatives in one
degree vanished globally. Choose a nonzero coefficient and a cell on
which its representative has an active tuple. All other chosen supports
have different carriers. For EVERY fixed endpoint pair, the selected
carrier's z^b coefficient is nonzero and cannot be supplied by other
supports; the restricted uniqueness lemma shows the combination is not
identically zero on that cell. Each endpoint branch has isolated zeros.
Finitely many branches cannot vanish at every point under the actual
selector. Contradiction. Therefore these selected representatives are
independent as actual functions in EACH degree.

## Arbitrarily large legal support construction

For a representative choose any listed m. Put
ap=sum e_B^+, am=sum (-e_B)^+, so -am<m<ap, m!=0, as independently
checked in the certificate. Let t=(m+am)/(ap+am), and assign

    gamma_B=t for e_B>0,
    gamma_B=1-t for e_B<0,
    gamma_B=1/2 for e_B=0.

These rational numbers lie strictly between 0 and 1, and
sum e_B gamma_B=m. At large Y use Bertrand's prime-existence theorem
to choose q_B between C_B Y^gamma_B and 2 C_B Y^gamma_B,
C_B=3^B (integer endpoints may be rounded, adding only O(1) to logs).
Blocks of equal gamma have disjoint intervals; blocks with different
gamma have disjoint intervals eventually. Thus all primes are distinct.
Set X_Y=(prod q_B^e_B)^(1/m). Then log X_Y=log Y+O(1), and because
max gamma<1, log q_B<=log X_Y-sqrt(log X_Y) for all large Y.
So every prime belongs to the ACTUAL natural cutoff. Multiplicity is
implemented by repeating its block prime in its original slots.

At X_Y the tuple is an exact alias and is excluded. Perturb X to one
side within the nonempty open residual window
0<|log(A/B)-m log X|<H/(2*pi*X). Such a punctured interval exists for
any fixed H>0 by continuity, since m!=0. Remove the finitely many
combinatorial boundaries and choose a subcell. The same tuple remains
active and within the cutoff. This is an existence witness at arbitrarily
large actual heights, not a freely adjusted carrier or prime window.
Good selected sections exist by the frozen construction; no new endpoint
claim or arithmetic estimate is required. Every positive-length section
has the same nonzero leading coefficient, as proved above.

The independent replay reconstructs these rational exponents from signs
and partitions, verifies interior support and the identity sum e gamma=m,
and checks all 54 supports against the entire 453 catalogue. The finite
checks certify the witness data; the argument above proves cell existence
and analytic independence.

## Second normal form: residual exponential-polynomial amplitudes

For a fixed cell and fixed degree, group the full Fourier/root expansion
by (lambda,rho,h), with amplitude terms c_(lambda,rho,h) z^h
exp(2*pi*i*rho*z). rho is itself an integer combination of prime logs.
Distinct rho are distinguished by their reduced rational valuations.
For fixed lambda the exponential-polynomials z^h exp(2*pi*i*rho*z)
are linearly independent over the actual complex CONSTANT field: apply
successively the constant-coefficient differential operators
(D-2*pi*i*rho) to eliminate frequencies (or use the confluent Vandermonde
Wronskian). To spell out the operator argument, to isolate one rho_0
apply prod_(rho!=rho_0)(D-2*pi*i*rho)^(H_rho+1). It annihilates every
other polynomial times exponential. On the rho_0 polynomial, each factor
acts as D+2*pi*i*(rho_0-rho), invertible on polynomials of bounded degree
because its nonzero constant term gives a triangular matrix. Thus the
rho_0 polynomial must be zero. Repeat for all rho.

Together with the carrier-germ lemma this proves: in ONE degree on a
fixed legal cell, equality of actual functions is equivalent to zero of
all COMBINED coefficients c_(lambda,rho,h). The coefficient field is
Q(i,pi,{log p},{sqrt p}) for the fixed prime set and rational section
normalization. These are actual constants; no algebraic independence
of logarithm products or of pi is assumed. Duplicate frequencies,
polynomial powers, conjugate contributions, paths and assignments must
be combined BEFORE testing coefficients.

This is a faithful cell-level normal form theorem, stronger than the
independent-label proxy. Its full coefficient matrix for 72/381 columns
has not been enumerated: it requires all actual prime assignments and
closed R6000 paths on chosen cells, exact frequency grouping, and exact
constant-field cancellation/rank certificates. The small exported support
matrix certifies only the 19/35 selected subfamilies by the leading-sign
proof, not the full same-carrier amplitude matrix. This is now the first
symbolic obstruction to full block certification. A family of cell-level
matrices suffices globally; one fixed small cell need not contain every
functional's support.

## Free-carrier lift and prime torus

An exact lift G_j(X,t) is available by using X for N,L, masks, actual
section/taper at physical height 2*pi*X, and changing ONLY exp(i*T*lambda)
to exp(i*t*lambda). The residual window stays H/(2*pi*X). Then
F_j(T)=G_j(T/(2*pi),T). Equality on a one-dimensional diagonal does
NOT imply a two-variable identity for arbitrary analytic lifts: already
exp(i*t*lambda)-exp(i*2*pi*X*lambda) vanishes on that diagonal but is not
zero elsewhere. This is not a constructed kernel vector in the Riemann
family; it falsifies the unrestricted implication.

For a SAME-DEGREE combination of the ACTUAL cell lifts, however, the
common a_phi factor can be removed and the restricted germ lemma DOES
justify the implication: physical-cell identity forces all grouped
carrier amplitudes to be identically zero, hence the free-t combination
vanishes throughout the fixed cell. No extra density theorem is required.
It does not make distinct same-carrier origins independent; their
combined residual coefficients still have to be computed. For mixed
degrees the two different a_phi powers cannot be removed by one common
factor. No analytic-germ continuation property for that normalization
is imported from the mere assertion a_phi->1, so a mixed-degree lift
faithfulness theorem is not certified here.

For a fixed finite prime set, Q-independence of log p follows from unique
factorization as above. The continuous phase flow has no nonzero integer
annihilator, and hence its closure is the full torus. No independence
with 2*pi is needed for a CONTINUOUS flow (its annihilator condition is
sum v_p log p=0). A DISCRETE sampled orbit at unit times would instead
need exclusion of sum v_p log p in 2*pi*Z, which is not invoked or proved
here. Even continuous torus density does not freeze moving amplitudes,
cutoff or geometry on the physical diagonal. Constant finite Laurent
characters are already independent by distinct-frequency differentiation;
that result alone is insufficient for the full map. The germ argument,
not a stripped torus proxy, handles the actual cell factors.

## Rigorous numerical fallback: no fabricated minor

The installed system Python has mpmath and SymPy, but not python-flint
or Sage. Ordinary mpmath values are not used as proof. Absence of those
engines is not a mathematical impossibility: the repository's rational
log/trig enclosures or another outward-rounded implementation could be
extended. A complete legal fixed-R evaluation needs more than the old
zero-lag diagnostic: all prime assignments/paths (or a rigorously proved
matrix contraction computing the same sum), actual taper normalization,
and certified admissible endpoints, followed by outward-rounded pivots
or minors. No such numeric matrix/minor is certified in this run.

The symbolic construction above avoids fake finite-height inputs and
gives stronger independence than rank-one discovery within each block.
It does not supply an interval pivot, a rank-72 or rank-381 matrix, or a
full determinant. Endpoint-selector analyticity is not assumed. The
support-witness route cannot isolate all 453 columns, because multiple
columns share the same rational carrier pattern. Isolating a Fourier
path or prime assignment by fiat would be a different evaluation map.

## Certified output and remaining obstruction

K_formal={0} on the retained labels; K_global UNKNOWN; no global kernel
relation is produced. The new per-degree analytic ranks satisfy
19<=r5<=72 and 35<=r6<=381. The combined original rank satisfies
35<=r<=453, global nullity between 0 and 418, and fifth/sixth intersection
dimension UNKNOWN. The 54 normalized support witnesses do not prove
combined original rank 54 without controlling the mixed normalization.
The coefficient incidence of those support witnesses is diagonal, but
its analytic independence is justified by the proofs above, not its
formal determinant alone.

Algebraic compression remains OPEN. The symbolic obstruction is the
rank of the FULL combined (lambda,rho,h) amplitude matrices within shared
carrier supports, followed by mixed-degree faithfulness/intersection.
The interval obstruction is the unconstructed complete legal outward-
rounded evaluation matrix and its endpoint/taper certificates. No
quantitative NearAlias bound or new consumer is attempted, and the old
arithmetic budget is unchanged and unpaid. Strict >79 remains OPEN.

Decision **F**, with the stated partial analytic lower bounds. Neither
A/B/C/E is established, and D would incorrectly label the symbolic proof
as an interval-minor certificate. Source/certificate pins and all 54
explicit representative IDs, rational support exponents, symbolic prime
construction and independent replay are provided in the adjacent JSON,
CSV and src/wp84_prime_path_faithfulness*.py artifacts. Replay verifies
all finite witness identities; the analytic proofs are given in this note.
The executable cell_atom_terms constructor also supplies the exact
(lambda valuation vector, rho valuation vector, z power) expansion of
one admitted tuple/path, with complete sampled-root summation and real
pairing. Constant-field monomials retain log-prime powers, square-root
prime denominators and inverse powers of pi*i. Its caller must validate
actual cell admission; its small algebraic replay examples are NOT legal
rank-specialization witnesses. Replay independently checks that summing
the zero-lag leading coefficient over roots gives (-1)^b/2 on each
reciprocal carrier for different sections, as used in the proof.
