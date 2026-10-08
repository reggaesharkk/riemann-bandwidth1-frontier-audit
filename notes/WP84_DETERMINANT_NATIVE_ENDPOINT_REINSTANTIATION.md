# WP84: uniform endpoint theorem, native fifth carriers, and the jet gate

Date: 2026-10-08. Parent: `307fe32651d0378e439b69f110060d6c94ee1a15`.
Branch: `codex/c5-c6-attack-20261006`. Local only.

**Decision E: bridge reduced to the real source-jet intertwining lemma in
Section 9.** No source-legal determinant has been evaluated; fifth analytic
rank remains 38–72 and strict >79 remains OPEN.

## 1. What the historical theorem actually quantifies over

The analytic step in `WP84_GOOD_ENDPOINT_TRIMMING`, Sections 3–5, is uniform
over coefficient families meeting its hypotheses. Equality with the
historical semiprime coefficients is not necessary for that step. The prior
compatibility audit established a missing identification, not impossibility
of this uniform reinstantiation.

An exact schema, making the otherwise unspecified constants explicit, is:

* Input: finitely many channels indexed by j, with measurable parameter
  spaces Theta_j, and `S_j(theta,t)=sum_gamma c_j(theta,gamma) exp(i t lambda_gamma)`.
  The coefficients and frequencies may depend on T but are fixed as the
  endpoint index k varies. Equal frequencies are collapsed before estimating.
* Energy: `B=sum_j int_Theta_j sum_gamma |c_j(theta,gamma)|^2 dtheta < infinity`.
  For the historical specialization B=O(1), uniformly in T. Compact
  parameter spaces and bounded threshold features are sufficient ways to
  establish this, not additional restrictions on arbitrary coefficients.
* Frequency hypotheses: `|lambda_gamma|<=Omega`, and distinct frequencies
  within each channel have separation at least delta. Different channels
  need not be separated from each other.
* Samples: q consecutive Fourier indices, spacing h=2pi/L; the union of
  their centered sampling cells has length U=q h. Translates and finitely
  many adjacent-index scores have the same bound.
* Averaged score:

      (1/q) sum_k sum_j int |S_j(theta,T+h k)|^2 dtheta
        <= 2(1+h^2 Omega^2) [1+2pi/(U delta)] B.       (1)

* Endpoint conclusion: at least one sample has score no larger than (1).
  A finite sum of nonnegative scores controls every summand at that sample.
  A lexicographically first argmin exists mathematically on a finite set;
  an exact executable comparison of its transcendental values is a separate
  requirement, not a consequence of existence.
* Normalization: the historical commutator debt has the further factor
  `1/d'` and a product of two endpoint norms. Equation (1) alone is not a
  bound for an arbitrary determinant or Taylor-coefficient row.

Proof of (1): the fundamental theorem of calculus gives on each h-cell

    |S(t_k)|^2 <= (2/h) int_cell |S|^2 + 2h int_cell |S'|^2.

Montgomery–Vaughan gives `(U+2pi/delta)` times coefficient energy for
both integrals. Derivative energy is at most Omega^2 B. Sum the disjoint
cells, divide by q, and integrate the parameters. No historical feature
identity enters this proof. The Hilbert-space formulation follows by
applying the scalar bound componentwise and Tonelli.

For the old integer-product family, `lambda=log m`, `m<=X_old<=T^2`,
`delta>=1/(X_old+1)`, and `Omega=log X_old=O(L)`. Thus (1) is
`O(B(1+X_old/U))`; with B=O(1), `U~T/sqrt L`, and `d'~TL`, the
normalized endpoint cost is `O(L^(-1/2))`. This is uniform over arbitrary
families of this class. It is not uniform over all frequencies without a
separation/energy hypothesis, or over endpoint-dependent coefficient arrays.

The source features in `WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION` are
semiprime sums with thresholds. A bound for each fixed threshold does not
automatically bound a supremum of thresholds; any maximal selection must
itself be included in the proved energy/score hypotheses. No missing maximal
bound is supplied by the numerical verifiers.

The original Hilbert inequality input was checked at the author-hosted
[Montgomery–Vaughan paper, Theorem 2 and Corollary 2, pp. 74–75](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).
The accompanying R400 assembly scripts check decimal bookkeeping and
exponent ledgers. The commutator verifier checks a finite matrix identity
numerically; the exact pair verifier checks its rational constant. None is
an executable feature constructor or a determinant-jet theorem.

## 2. Actual source inputs and carrier classes

Read in full: the three requested historical notes, the first-record code,
the detuning feature/commutator/second-mass notes and verifiers, the same-
normalization replay, the exact pair verifier, the current full-pool
amplitude iterator, q-mask extractor, determinant coefficient builder,
evaluation-map constructor, wedge reducer, visible subsystem builder, and
the legal-stencil and full-pool section formulas. The certificate pins these
sources. This is no historical selector search.

Use `X=T/(2pi)`, `L=log X`, `N=floor(exp(L-sqrt L))`,
`d=floor(TL/(2pi))`, `h=2pi/L`, fixed R=6000, the prescribed nonzero
`a=a_phi(T)>0` at sufficiently large T, and the one declared fixed H. All block primes are ordinary,
distinct across equality blocks, and <=N. The source mask includes the
original alias list, nearest residual cell and `0<|lambda-mL|<=H/T`.
The exact q-mask note proves that the hidden-prime domain is the entire
prime pool minus visible primes, with no extra slot interval. The iterator
still takes its callback as an input; this audit uses that mathematical
predicate, not a newly invented callback.

| Block | Carrier, in reduced form | Alias | Hidden / visible-extra columns | Direct old integer-frequency class? |
|---|---|---:|---:|---|
| B6, size 6 | p q r, three distinct visible primes | 2 | 2 / 4 | Yes for physical endpoint fields: admitted products are <=X^2 exp(H/T)<=T^2 eventually |
| B8a, size 8 | p^2 q | 2 | 6 / 2 | Yes, with the repeated-prime weights retained |
| B16, size 16 | p q/r, distinct visible primes | 1 | 6 / 10 | No: noninteger rational carrier |
| B8b, size 8 | p^2/r | 1 | 6 / 2 | No: noninteger rational carrier |

All have total absolute net degree three and exactly one excess pair.
Hidden q is absent from lambda but remains in every full coefficient sum.
For a fixed mixed class, comparing two reduced ratios compares integers
<=N^3, so distinct log frequencies have separation >=1/(N^3+1).
The same real-frequency Hilbert theorem therefore applies, but with a
larger reciprocal separation. An O(1) energy bound alone would give the
unhelpful charge `O(N^3/(U d'))`. It is not legitimate to replace the
denominator phase by an integer polynomial without accounting for all
denominator channels and their cross terms.

## 3. Exact physical endpoint fields, including masks and full pool

Let v_0=0, v_j=sum_(s<=j) ell_s, minv=min v, maxv=max v, span=maxv-minv.
Every closed five-step R6000 path has span<=12000. For n>12000 its Boolean
root veto is identically one for every path. The source q/alias predicates
then do not change as the section endpoints vary at fixed T and n.

Write kappa_p=log(p)/(a L sqrt p), and let w_(j,P,ell) retain the product
of the five signed slot coefficients, the five exact filtered coefficients,
the exact prefix phase, and the complete source mask. In the positive-carrier
amplitude convention of the current iterator retain its orientation factor
1/2. This factor is never inserted again on top of a raw real trace.
The conservative inequalities below discard its saving and therefore cover
both conventions without changing either exact definition.

For section I=[a0,b0], define its exact unnormalized positive-carrier sum

    Phi_j(I)= (1/2) sum_(P injective, all primes<=N)
      sum_(ell closed, |ell_s|<=6000) w_(j,P,ell)
      sum_(i=a0-minv)^(b0-maxv) exp(i(T+h i)lambda_P).

The normalized amplitude is `Re Phi_j(I)/n`, with exactly n=b0-a0+1.
No carrier, canceled prime, source mask or root is discarded.
Define boundary fields

    D_j,-(k)= (1/2) sum_(P,ell) w_(j,P,ell)
                  exp(i(T+h(k-minv))lambda_P),
    D_j,+(k)= (1/2) sum_(P,ell) w_(j,P,ell)
                  exp(i(T+h(k-maxv))lambda_P).

Then `Phi_j([a0+1,b0])-Phi_j([a0,b0])=-D_j,-(a0)` and
`Phi_j([a0,b0+1])-Phi_j([a0,b0])=D_j,+(b0+1)` exactly.
Normalization of these differences also changes n; that is a separate
term and is not silently dropped. These fields concern physical values
at u=1/L. They are not the coefficient-extraction rows of Section 7.

The consumer weights are the exact `exact_alpha` fields of the canonical
ledger. A combined physical score is

    E_phys(k)=sum_(j in the 38 columns) |alpha_j|^2
          sum_(t in {0,1}) (|D_j,-(k+t)|^2+|D_j,+(k+t)|^2).

The offset set {0,1} expressly includes the adjacent-index terms. Conjugate
pairing and taking a real part do not increase these squared norm bounds.

## 4. Full-pool coefficient energy improves to O_R,H(1/T)

This improvement uses the actual alias mask, not oscillation or PNT/BV
replacement of signed sums. Put

    M=sum_(p<=N) kappa_p^2,
    beta_0=1, beta_l=1/(pi |l|) for l!=0,
    P_R=sum_(closed five-step paths) product_s beta_(ell_s).

Every exact source filter has modulus <=beta_l. Young/Cauchy–Schwarz give

    P_R <= (1+2 H_R/pi)^3 (1+2 H_(R,2)/pi^2).

P_6000 is a finite fixed constant, independent of T. One elementary rational
upper bound is 158171/243, using H_6000<10, pi>3, and H_(R,2)<2.
The prime-square input gives M=O(1) with its actual a_phi normalization.

For each visible assignment the full hidden-q sum is bounded by M times
the reduced three-occurrence coefficient. In a visible-extra column the
additional repeated factor kappa_p^2 is <=M instead. Thus every column,
including all hidden-prime sums, is treated by the same bound. Unique
factorization gives at most 3!=6 visible assignments per reduced carrier.
After summing all paths, a collapsed unweighted endpoint coefficient satisfies

    |c_j(A/B)| <= K /sqrt(A B),  K=6 M P_R/a^3.

For mixed carriers keep the useful additional factor log B/L on the right;
B is its denominator prime. Source masks can only decrease this absolute
majorant; source weights and phases remain in the exact coefficient.

Let t=H/T<=1/2. The interval [C exp(-t),C exp(t)] has width <=4tC,
contains at most 1+4tC integers, and its members are >=C/2.
For positive carriers C=X^2, so

    sum_A |c_j(A)|^2 <= K^2 (2/X^2+8H/T).           (2)

For mixed carriers, at each prime denominator B the numerator satisfies
A~XB and has at most 1+4HXB/T admissible integer values. Counting all
integers is an upper bound for its restricted semiprimes/squares. Hence

    sum_(A/B) |c_j(A/B)|^2
      <= K^2 [ (2/X) sum_B (log B/L)^2/B^2
                   +(8H/T) sum_B (log B/L)^2/B ]
      <= (K^2/T) [4pi+8H a^2 M].                  (3)

Here the last reciprocal-prime sum is exactly a^2 M, and the square sum
is bounded by sum_(n>=2) n^(-2)<1. No hidden-prime truncation occurs.
If W2=sum_j |alpha_j|^2, the total one-edge energy is consequently bounded by

    B_native <= (W2 K^2/T) [4pi+8H(1+a^2 M)].     (4)

This is a practical explicit norm bound, not an asserted sharp transfer
constant from the old feature family. H and a_phi remain source inputs.

Using Omega<=3L and delta>=1/(N^3+1) in (1), both endpoint fields together
have sampled score at most

    8(1+36pi^2) [1+2pi(N^3+1)/U] B_native.        (5)

At U~T/sqrt L, n~TL, (5)/n is

    O_R,H,W2( 1/(T^2 L) + N^3/(epsilon_L T^3 L))
      = O_R,H,W2( exp(-3sqrt L)/sqrt L ) + o(1). (6)

The last equality uses N<=X exp(-sqrt L), with the fixed factor (2pi)^-3
retained in an explicit evaluation of (5). Constants are fixed for R=6000
and fixed H. Equations (2)–(6) certify physical endpoint control; they do
not certify determinant jets or pay a bulk arithmetic moment.

## 5. Why a fixed linear transfer from the old features is unavailable

In the continuous endpoint variable used by the mean-square proof, the
historical coefficients have ordinary-semiprime frequencies log(pq).
The present fields have reduced net absolute degree three. Unique
factorization makes their carrier supports disjoint. Distinct finite real
exponentials are linearly independent on an interval. Therefore a
coefficient-independent, endpoint-independent linear map from those old
semiprime frequencies to a nonzero degree-three field cannot supply the
new carriers. This is a frequency-space statement, not analytic-rank
promotion in the source input domain.

The exact support projection onto the odd-carrier component annihilates
the old feature space and acts as the identity on D. A zero transfer
has rank zero, full old-feature kernel, image {0}, and residual D; it is
not a useful compression and rank(D) remains unknown after actual
evaluation. Theta-integrated old channels do not form a supplied finite
rank matrix whose rank can honestly be printed. Endpoint-dependent
multipliers can shift frequencies, but their quantitative operator norm
and legal jet action would need proof. No certified finite C for
`Score_det<=C Score_trim` follows from the old coefficients. Equation (4)
is instead a native energy bound.

## 6. Joint endpoints and fixed length

The source root divisor and moments depend jointly on the endpoints.
Independent minimization is not justified for a general determinant score.
For a constructive *physical* endpoint argument there is an exact coupled
candidate line avoiding that issue. With q=floor(d/sqrt L), use

    a0=k, b0=k+d-q, k=0,...,q-1;  n=d-q+1.

Both endpoints lie in their respective first/last-q windows. They are
ordered, contiguous, and n/d->1; deletion is q-1. At sufficiently large
T, n>12000, so every R6000 path has roots. The joint score uses
`D_j,-(a0+t)` and `D_j,+(b0+1+t)`, t in {0,1}. Both scores are sampled on
consecutive translated windows along the same k; their sum obeys (5).
Adjacent field evaluations do not append a row to the selected section.
The lexicographically first minimizer of that exact joint *physical* score
exists. No executable selector for the determinant jets is exported here.
The source does not require the candidate endpoints to be centered.

This coupled construction is not used to change the actual section or to
promote a raw-moment or determinant rank. It supplies an admissible geometry
for testing the finite intertwining lemma below.

## 7. First obstruction for the actual determinant: evaluation versus jets

The determinant coefficient builder asks for `[u^h]` of the entire source
root/filter expression, with the source pool and masks frozen on its cell.
Its root factor is

    R_(a0,n,ell,lambda)(u)
      = exp(c0(a0-minv)lambda u)/n
          sum_(r=0)^(n-span-1) exp(c0 r lambda u), c0=2pi i.

Its h-th coefficient is exactly

    (c0 lambda)^h/(n h!)
       sum_(r=0)^(n-span-1) (a0-minv+r)^h.         (7)

At u=1/L and integer k, lambda=mL+delta gives
`exp(2pi i k lambda/L)=exp(2pi i k delta/L)`.
Replacing lambda by delta in (7) is false: the removed factor
`exp(2pi i k mL u)` equals one at u=1/L but has nonzero jets at u=0.
For the legal zero-displacement path the h-th root coefficient grows like
`(c0 lambda)^h n^h/(h+1)!`. The full-root physical factor has modulus <=1;
that fact is not a bound on these unscaled Taylor coefficients. The slot
jets also introduce the full S2,...,S10 moment coefficients and cannot be
replaced by physical-slot values.

In particular the actual joint determinant-row score is schematically

    E_jet(a0,b0)=sum_(source rows i) sum_(columns j)
        |alpha_j * J_(i,j)(T_i,carrier_i,h_i;I)|^2,

where J is the exact coefficient-extraction sum, with its original
`-1/(2 a_phi^5 L^5)` and root divisor. It is not E_phys. At fixed source
cell its dependence on a0 and n is polynomial/Laurent-polynomial, rather
than the log-frequency exponential family assumed in (1). This is the
first exact mathematical obstruction to declaring that *the determinant
rows* satisfy the old score theorem or the new physical score theorem.
Rescaling those rows and then reporting a physical cost would omit the
rescaling operator from the consumer/determinant argument.

## 8. Exact residual identities; what survives at the wedge

For fixed carrier, fixed n and the full masked source sum, a physical
translation by s gives a common complex factor:

    Z_j(a0+s,u)=exp(c0 s lambda u) Z_j(a0,u),
    J_h(a0+s)=sum_(r=0)^h (c0 s lambda)^(h-r)/(h-r)! J_r(a0). (8)

This is exact, retains full canceled primes, and uses every path/root.
On a complete complex jet stack 0..hmax, (8) is lower triangular with
diagonal one, determinant one, and inverse obtained by s -> -s.
On its complete realification, using both Re and Im of each jet, it is
also invertible. This is the actual usable gauge/jet identity.

It does not establish invertibility on a selected real source stencil.
Odd powers of c0 mix the real and imaginary lower jets; lower same-cell
jets need not be rows of that stencil. A structural counterexample is the
two complex germs (1,i) with the real rows of orders 0 and 1. Before a
common multiplier exp(i s u), their matrix is [[1,0],[0,0]]. Afterwards
it is [[1,0],[0,-s]]. At s!=0 its determinant is -s. This is a universal
algebra falsifier for an unjustified real-jet invariance claim, not a
prime-source counterexample or a promoted diagnostic rank.

The existing common leading vector v_B(S2) does kill every exterior term
with two copies of that *same* vector. It yields the first possible
deficits 5,7,15,7. It says nothing about the collected subleading residual
or its nine-moment support. No all-ones replacement is made.

LRSC injectivity requires an injective evaluation stencil and nonzero
channel factors; neither follows from the endpoint energy bound. Its
rank-one update requires a common response vector. Here (8) involves
all lower jets. The old rank-two commutator acts on a carrier Gram matrix,
not on the source determinant rows. Root-origin compensation is a gauge;
moving physical endpoints without that compensation is (8). No boundary,
phase-odd, common-column or exterior-null conclusion for the missing jet
residual is justified by the preserved LRSC/physics/phase-network records.
The preserved packet was inspected read-only via its manifest and extracted
source references. No packet content is modified.

## 9. The reduced explicit lemma (the continuation gate)

**Real source-jet intertwining lemma at fixed admissible lengths.** For each
of the four blocks B, let W_B be its actual frozen source-legal evaluation
row space (with its actual carrier cells, jet orders and prescribed real
pairing). At each distinct frozen cell x fix n_x=d_x-q_x+1. Let a and s
be the vectors of root origins and translations for these cells. Prove
that the full complex lower jets appearing in (8), after prescribed real
pairing, induce an operator U_B(s) on W_B such that

    M_B(a+s,n;S)=U_B(s) M_B(a,n;S),
    U_B(s+t)=U_B(s)U_B(t), U_B(0)=Id, det U_B(s)!=0,       (9)

for every candidate integer translation vector s. The coefficients must
be independent of the column and of all master moment variables S,
retain the full source normalization,
and use only source-legal rows. Equivalently, certify that the real row
space is invariant under each cell's finite nilpotent generator of (8), including
its real/imaginary couplings and all same-cell lower jets. If (9) fails,
exhibit the first actual-source residual covector outside that row space;
the generic counterexample in Section 8 does not count as that witness.

An explicit finite sufficient test avoids any abstract determinant search.
Stack the complete realified jets of orders 0..8 by source cell, and let
P_B be the actual restriction to the frozen real source rows. The generator
G_x has, on cell x, subdiagonal 2-by-2 blocks
`2pi lambda_x * [[0,-1],[1,0]]`, and is zero on the other cells.
Let V_jet be the Krylov span generated from the actual constant and moment
coefficient columns by these commuting G_x (powers above 8 are zero).
Its ambient dimension is at most 18 times the number of source cells.
The precise finite lemma is

    ker(P_B restricted to V_jet) is G_x-invariant for every source cell x.

Equivalently, there are column- and moment-independent matrices H_x with
`P_B G_x=H_x P_B` on V_jet. Then the induced H_x commute and are nilpotent,
and `U_B(s)=exp(sum_x s_x H_x)` supplies (9), with determinant one on the
generated image. This is a linear intertwining check on actual source
coefficient vectors, before expanding or asserting a nonzero determinant.
It does not replace P_B by an arbitrary diagnostic stencil.

At distinct heights the components of S are S_j(N(T_x)); no equal value
of those moments at different heights is assumed. The complete realified
jet stack, stacked by source cell, satisfies (9) algebraically. Its
restriction to the frozen legal stencil is the unresolved finite lemma.
It is smaller than a new prime-correlation theorem and does not ask for
determinant nonvanishing or a new historical selector. A proof would let
the coupled good-endpoint choice preserve rank and determinant-visible
moment support at fixed n; it would still not compute a nonzero minor.
No assertion that the frozen rows are jet-complete is made.

## 10. Budget and evidence boundary

The available exact joint fifth/sixth cushion is
`52897896569489/572357731837500000`. The retained-family l1 coefficient
mass is `163444421/31250`, with the previous sufficient common threshold
about 1.76705785868357e-8. Those numbers are unchanged.

The physical bound (6) would cost zero in a limiting endpoint-only term
with its proved 1/d' normalization, for any fixed R6000,H and finite
weights. It is not a bound on the bulk 453 survivor sum or E_jet, and is
not charged as a paid arithmetic error. There is no certified finite T0,
feature-to-jet constant, determinant margin, K, correction rank, or new
minor. Fifth rank remains 38–72; V5 intersection V6 and strict >79 remain
OPEN. The first obstruction is coefficient extraction, not an absent
historical coefficient label.

Artifacts: the producer `src/wp84_determinant_native_endpoint_audit.py`,
the independent exact replay `src/wp84_determinant_native_endpoint_replay.py`,
and `notes/WP84_DETERMINANT_NATIVE_ENDPOINT_CERTIFICATE.json`. The replay
checks carrier supports, all weights, source/packet hashes, exact root jets,
binomial translation, realification, the real-stencil counterexample,
fixed-length joint windows and hostile mutations. Universal rational
fixtures certify identities only; they are not prime-generated minors.
