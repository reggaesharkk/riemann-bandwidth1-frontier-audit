# Shared-carrier jet ranks and mixed-degree intersection

Parent 9d637dafa2bcedcf81ba6aad700903de0654041e. Isolated branch
codex/c5-c6-attack-20261006. No push. Decision **F**.

The fifth result is frozen first: 19 shared-support blocks, rank bounds
19..72. Sixth: 35 blocks, bounds 35..381. The smallest unresolved fifth
block has two columns, IDs 5 and 7. Its FULL carrier amplitudes have
identical jets through u^8, rank 1, truncated null vector (1,-1).
No global functional kernel is inferred. Its first possible separating
jet is at order >=9 and has not been certified. Mixed physical-span
intersection remains unknown; total rank bounds remain 35..453.

## Correct carrier blocks and normalization

Every exported representative retains all prime assignments, equality
masks, multiplicities, Fourier paths, root/endpoint restrictions and
aliases. The partition is by reciprocal reduced exponent multiset,
not one rational carrier value. Each such block contains MANY values
lambda=log(A/B). Consequently one cannot write an entire support block
as a single common exponential times A_j(u). The correct cell form is

    F_j(T)=a_phi(T)^(-b) sum_lambda
                  A_(j,lambda)(u) exp(i*T*lambda),
    u=1/log(T/(2*pi)).

Both positive and negative carriers are included after the real-part
projection. For a FIXED lambda its exponential and degree normalization
can be factored. The cell jet matrix must have rows (lambda,k), or the
faithful residual-frequency/power indices from the parent theorem. A
support-key incidence row alone is not that matrix.

On each cell the exact amplitude is a finite sum of
c*u^h*exp(2*pi*i*rho*u). The builder retains rho prime-valuation vectors,
log-prime powers, square-root-prime denominators and inverse powers of
pi*i, with exact rational coefficients. Taylor coefficient at k>=h is
c*(2*pi*i*rho)^(k-h)/(k-h)!, combined BEFORE rank testing. The constant
field is Q(i,pi,log p,sqrt p), consisting of actual constants; its formal
symbols are not assumed algebraically independent. The independent
builder expands the linear rho polynomial by repeated multiplication,
while the producer uses multinomial compositions. These exact builders
operate on admitted tuple/path expansions; a full cell matrix requires
summing all actual admitted tuples/paths, not selecting a proxy subset.

## Exact block inventory and proved ranks

Fifth block-size distribution (size: number of blocks):

    1:4, 2:6, 3:2, 4:3, 6:1, 8:2, 16:1.

These sum to 19 blocks and 72 columns. Four singleton blocks have exact
analytic rank 1. Every remaining block has analytic rank between 1 and
its size; its nullity is between 0 and size-1. The nonzero carrier/leading
minor is justified by the parent's zero-lag positivity and legal-cell
existence theorem, with lowest u-order 5. Full higher-jet ranks of those
blocks are UNKNOWN. No deficient finite jet matrix is treated as a
global kernel certificate. The fifth JSON records every support, ID,
size, leading order and exact lower/upper rank and nullity.

The fifth certificate is written and frozen before the sixth inventory.
Sixth block-size distribution:

    1:4, 3:9, 6:8, 8:2, 9:2, 11:2, 12:1,
    13:2, 28:1, 32:1, 38:2, 72:1.

These sum to 35 blocks and 381 columns. Again four singleton blocks have
exact analytic rank 1; every other block has bounds 1..size, lowest
u-order 6. This preserves rank_6>=35 but supplies no new strict bound.
All 54 blockwise certificates are exported; they are not hidden inside
one coarse global interval.

No leading-order triangular proof separates the columns within a block:
each original same-degree column starts at u^b, with positive weighted
zero-lag carrier coefficients. In the smallest block even the next three
orders coincide, as proved below. A surviving leading/truncated null
vector is not a relation at all orders.

## Smallest unresolved block: complete jets through order eight

IDs 5 and 7 have signs +++++, equality layouts 00123 and 01023,
reduced factor multiset (2,1,1,1), and aliases 2,3,4. For a fixed admitted
carrier p^2*q*r*s with four distinct primes, each column has exactly six
assignments of its singleton primes. Let a_i=log p_i for the five slots,
with the doubled prime repeated in its two original slots. Let

    S1=sum_i a_i=lambda,
    e2=sum_(i<j)a_i*a_j, e3=sum_(i<j<k)a_i*a_j*a_k,
    mu_h=(1/d') sum_(k in I)k^h,
    K0=min(R,d'-1),
    S2=2*K0-K0*(K0+1)/d',
    S3=K0*(K0-1)*(3-2*(K0+1)/d').

The common nonzero factor for the positive real-part carrier amplitude is

    C=6*(-1)^5/2 * prod_i a_i/sqrt(prod_i p_i).

After factoring C and u^5, BOTH columns have the same four coefficient
rows (orders u^5,u^6,u^7,u^8):

    1,
    -S1+2*pi*i*lambda*mu1,
    (1+S2)*e2-2*pi*i*lambda*mu1*S1-2*pi^2*lambda^2*mu2,
    -(1+3*S2+S3)*e3
      +(1+S2)*e2*2*pi*i*lambda*mu1
      +2*pi^2*lambda^2*mu2*S1
      +(2*pi*i*lambda)^3*mu3/6.

For the negative carrier use the conjugate. These formulas retain the
FULL sampled section and FULL fixed-R path sum; no zero-lag proxy is
substituted for the other paths.

Proof of the complete low jets. A nonzero-lag filter has expansion
f_l^+(a*u)=-a*u-pi*i*l*a^2*u^2+O(u^3). Closed paths cannot have just
one nonzero lag. Through relative order 3, the possible paths therefore
have zero, two or three nonzero lags only.

The all-zero path is exactly
prod_i(1-a_i*u) times the normalized root exponential sum. Its first
four Taylor rows give the zero-path contributions displayed above,
independently of slot order.

For a pair of positions and lags r,-r, root count is (d'-|r|)_+,
regardless of their separation. Summing leading two-filter coefficients
gives S2*a_i*a_j. At the next order the other zero-lag factors contribute
-S2*a_i*a_j*(S1-a_i-a_j); summing pairs gives -3*S2*e3.
The filter's terms odd in r cancel between r and -r. The intermediate-
vertex phase is also odd in r and cancels. The two root intervals have
opposite shifts, and their average absolute root position is the full
section mean mu1. Thus the remaining pair contribution is
S2*e2*2*pi*i*lambda*mu1. This is independent of the repeated-prime
positions and proves the pair part of the fourth row.

For three nonzero lags r,s,t=-r-s, the path range is
max(|r|,|s|,|t|), and its leading coefficient is -a_i*a_j*a_k.
Among triples with maximum absolute lag n there are exactly 6*(n-1)
ordered choices. Summing (d'-n)_+/d' for n=2,...,K0 gives exactly S3.
Every chosen triple of slots therefore contributes the same S3 factor;
its total is -S3*e3. No path with four or more nonzero lags contributes
through relative order 3. This exhausts the full sum and proves the rows.

The normalized 4-by-2 jet matrix has rank exactly 1, nonzero 1-by-1 minor
1, and kernel span_Q{(1,-1)}. C is nonzero because all primes exceed one.
This proves only that the difference vanishes through u^8 per carrier.
It does NOT prove that the two full amplitudes are identical. Higher
jets introduce additional filter terms, intermediate root moments and
multi-lag interactions; their complete order-sensitive sums have not
been reduced into a separating minor or all-orders identity. Hence this
is the explicit smallest unresolved rank-2 question, rather than a
claim that a null vector is a global arithmetic relation.

The independent replay checks the general row data, exact S2 and S3
sums at multiple integer sections/cutoffs, opposite-lag root means and
coefficient-builder expansions. The finite checks accompany the general
exhaustion proof above. Corrupting one normalized coefficient breaks
the claimed truncated null relation; it does not prove independence of
the genuine uncorrupted columns.

## Mixed degree: exact carrier exclusion versus physical intersection

For any reduced rational carrier the sum of absolute prime valuations
has parity b, since e_B congruent nu_B modulo 2 and sum nu_B=b.
The parity is unchanged by reciprocal real-part pairing. Thus the exact
ordinary-prime fifth and sixth rational-carrier sets have EMPTY
intersection: common carrier count zero, at every admissible cell.
There are no [J5(lambda)|J6(lambda)] matrices at a shared exact lambda.
This is a statement about phase support, not yet about the physical
function spaces with differing normalization.

Put both degrees into one physical normalization. A mixed relation is

    a_phi^6*(F5+F6)=a_phi(T)*H5(u)+H6(u)=0,
    H_b=a_phi(T)^b*F_b(T).

Within one degree H_b has the parent carrier-germ form. Merely knowing
a_phi(T)->1 does NOT prove that a_phi(T) on each cell analytically
continues as a nonzero germ in u at zero. Without that property, applying
the distinct-carrier uniqueness lemma to a_phi*H5+H6 is unjustified.
The assertion that a relation is possible ONLY at common carriers itself
requires this normalization hypothesis; it cannot be used as a premise
for proving that hypothesis. Comparing orders 5 versus 6 also fails:
nonzero combinations can cancel their first jets and start at later
orders. We do not divide two separately normalized models and call them
the same physical space.

A precise sufficient condition is available. If the actual boundary
profiles of the taper are fixed translates independent of L, then

    ||phi_L||_2^2=L-c, a_phi(T)=1-c*u,

where c is the fixed integral of the two edge deficits 1-|phi|^2.
For a width-one LINEAR ramp, c=4/3. For any fixed translated profile,
c is fixed even if not rational. The resulting analytic germ is nonzero
at u=0. The restricted carrier uniqueness lemma then forces each mixed
carrier amplitude to vanish; because the carrier sets are disjoint,
H5=H6=0 as cell functions. This proves zero intersection of the fixed-section CELL germs. To
promote it to the literal global function space also requires an actual
selector/boundary convention determined by those cell germs (for example
a locally constant selector on cells, with matching one-sided boundary
values). Without that extra regularity a selector could choose a different
branch at isolated common zeros. The parent lower-bound argument did not
need this implication: it exhibited a carrier nonzero on every branch.
Thus even the conditional GLOBAL intersection conclusion requires this
additional extension check before adding the lower bounds to 54.

This is a CONDITIONAL theorem, not a claim that the present source fixes
such a profile. The read source WP84_VARIANCE_RAMP_TRANSFER.md states
width w=1 and 0<=phi<=1 at the edges, while the normalization definition
is a_phi=||phi||_2^2/L (WP84_BOUNDED_RESOLVENT_CONSUMER.md). Those facts
alone allow L-dependent edge profiles; they do not prove the exact
analytic continuation just required. No shape is silently selected to
make a_phi=1 or 1-4u/3. The physical mixed intersection is therefore
UNKNOWN from the audited assumptions. The bound is 0<=intersection<=72.
The exact empty carrier set survives as a certified result regardless.

## Global conclusion and verification boundary

Fifth rank 19..72; sixth 35..381; total 35..453; no global kernel vector
or smaller reconstruction basis is proved. Under fixed-profile normalization and the additional global cell-
extension/selector condition, intersection would be zero and total at
least 54. Neither condition is promoted into the unconditional certificate.

The first unresolved shared-carrier block is (5,empty,(2,1,1,1)), IDs
5 and 7. Its exact full jets through u^8 have rank one, so those jets
cannot certify its analytic rank two. The difference's first nonzero
higher jet or its all-orders vanishing is still unproved. Other non-
singleton blocks are bounded individually by 1..size; no higher-jet rank
is fabricated. The full arithmetic interpretation of any future kernel
must be replayed against all original classes, not just a finite jet.

Artifacts: exact tuple/path-to-jet builder in
src/wp84_shared_carrier_jet_rank.py, independent polynomial/partition
replay in src/wp84_shared_carrier_jet_replay.py; fifth and sixth block
ledgers, smallest-block symbolic jets, coefficient-builder regression
examples and rank-status certificate in adjacent JSON files. Prior source
hashes are pinned. Strict >79 and algebraic compression remain OPEN;
no arithmetic budget or consumer change is made. All prior audit commits
and notebooklm_packet are preserved. Local commit is reported after
verification.
Replay additionally exhausts every closed R=1 path, every sampled root
in a two-row algebraic section, and all six singleton-prime assignments
for both layouts, combining actual prime-coordinate monomials. Their
complete jet sums agree through u^8. This is an independent regression
of the general symbolic low-order proof, not a legal finite-height
analytic-rank specialization.
