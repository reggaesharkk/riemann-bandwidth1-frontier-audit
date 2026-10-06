# WP84 — C5/C6 finite compression audit and exact joint error budget

Date: 2026-10-06. Starting commit: 908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5.

Status: **CLOSED finite identities and counterexamples; CONDITIONAL consumer;
OPEN arithmetic transport. Promotion work stopped after a compression mismatch.**

No unconditional simple-zero result is claimed. All changes are local.

## 1. CLOSED: exact joint error region

For the frozen cubic and its stated lower-order inputs at R=6000, assume

    mu5 >= 1/36-eps5+o(1),  mu6 <= 34/135+eps6+o(1).

The sufficient strict >79 region is exactly

    (11501/12500) eps5 + (137641/250000) eps6
      < 52897896569489/572357731837500000 = M.

This is the exact affine budget of the FROZEN consumer, not an optimization
over all cubics. It retains the existing rational pi lower bound and band
charge; validity of the analytic comparison and lower-order inputs remains
an assumption. No quantitative fourth moment is used.

Derivation: add |c5| eps5+c6 eps6 to E_rob and its two charges in
WP84_M4_FREE_ROBUST_CUBIC_R6000.md. Subtract from 21/200. Fraction arithmetic
reproduces M = 0.00009242103954753147... .

Axis intercepts:

    eps5 < 52897896569489/526614901909047000
         = 0.00010044891699366519...  (eps6=0),
    eps6 < 52897896569489/315119562271381350
         = 0.0001678661146524863...   (eps5=0).

Signed eps6 permits a stronger sixth ceiling. If mu6<=157/630, then
eps6=-1/378 and the fifth-loss allowance becomes

    eps5 < 110818441526008/65826862738630875.

Thus loss in the fifth moment can be exchanged for additional sixth-moment
negativity. Equality on the displayed boundary does not prove a strict >79.

## 2. CLOSED: actual finite-T word representation

Use the exact sharp prime matrix of
WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md. Let L be the physical interval
length, d=floor(TL/(2pi)), tau_i=T+2pi i/L, and retain prime powers n<=N.
Keep the actual real coefficients

    c_n=-Lambda(n)/(a_phi L sqrt(n)),  s_n=log(n)/L,

where a_phi is the source taper-mass normalization, not the consumer pole
height 221/200. If a source retains additional real coefficient weights,
they stay inside c_n throughout this identity.

For integer r define

    f_0(s)=1-s,
    f_r(s)=(1-exp(2pi i r s))/(2pi i r),  r != 0,
    f_r^+(s)=f_r(s),  f_r^-(s)=conjugate(f_r(s)).

Then the compressed signed branch at row i, column i+r is exactly

    B_n^epsilon(i,i+r)
      = c_n exp(i epsilon tau_i log(n)) f_r^epsilon(s_n).

The symmetry of the partial-shift matrix makes the negative branch its
entrywise conjugate. Define X_R by summing the two branches and setting
entries with |r|>R to zero. For k=5 or 6 take r_1,...,r_k in [-R,R] with
sum r_j=0. Set a_0=0, a_j=sum_{h<=j} r_h, and

    I_r={i: 0<=i+a_j<d for every j},
    q_r=|I_r|/d,
    K_{T,r}(Y)=d^(-1) sum_{i in I_r} exp(i tau_i Y).

The exact finite prime-sum identity is

    tau(X_R^k)
      = sum_{r: sum r=0} sum_{n_1,...,n_k<=N} sum_{epsilon in {+,-}^k}
          (product_j c_{n_j} f_{r_j}^{epsilon_j}(s_{n_j}))
          exp(2pi i sum_j epsilon_j a_{j-1} s_{n_j})
          K_{T,r}( log(A/B) ),

    A=product_{epsilon_j=+} n_j,
    B=product_{epsilon_j=-} n_j.

Every prime power, intermediate Fourier projection, band constraint,
carrier, endpoint restriction, and trace normalization is retained.
For a contiguous principal section use its absolute Fourier indices and
replace d by the section dimension. This is a finite sum, not a continuum
integral and not a product of physical overlaps.

Proof: insert the one-step Fourier entry formula into the ordinary matrix
trace path expansion. Factor the root-index phase out of each word. No
exchange of limits or arithmetic estimate occurs.

## 3. CLOSED: why the proposed spread bridge is not this identity

WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md correctly computes

    tau(P_d U_{y_1} ... U_{y_k} P_d).

Actual finite-matrix moments instead contain

    tau(P_d U_{y_1} P_d ... P_d U_{y_k} P_d).

Intermediate projections cannot be erased by an exact spread law.
Here is an exact counterexample, within the same Fourier convention:
d=2, y=L/2, and any R>=1. The compressed U_y matrix is

    [ 1/2   -i/pi ]
    [ -i/pi -1/2  ].

The scalar carrier cancels in the closed pair. Consequently

    tau((P_d U_y P_d)(P_d U_-y P_d)) = 1/4+1/pi^2,
    tau(P_d U_y U_-y P_d)            = 1/2.

Their difference is 1/4-1/pi^2 > 65945/443556 > 0, using pi>333/106.

This falsifies an exact identification, not a possible asymptotic theorem.
Such a theorem would need to bound the accumulated interprojection defect
in the actual weighted prime sums, uniformly at fixed R. It has not been
supplied by the cited spread identity. In addition, fixed R changes the
bulk path kernel; its error is not automatically o(1) as T grows.

**Promotion stop:** neither the C5 sign certificate nor its continuum integral
is invalidated. The assumed finite-compression transport interface is what
fails. Do not identify the public O5*C5 kernel with an actual trace sector
without an additional theorem.

## 4. CLOSED finite connected-sector definition; OPEN model identification

There is a canonical finite empirical cumulant decomposition of the actual
path trace. For each r choose i uniformly from I_r and put

    Z_j(i)=X_R(i+a_{j-1},i+a_j).

For any nonempty set S of positions define

    kappa_r(S)=sum_{partitions pi of S}
        (-1)^(|pi|-1)(|pi|-1)! product_{B in pi} E_{i in I_r} product_{j in B} Z_j(i).

Then define the fully connected finite sector

    Ck_actual(T,R)=sum_{r: sum r=0} q_r kappa_r({1,...,k}).

The exact identity is

    tau(X_R^k)=sum_r q_r sum_{partitions pi of {1,...,k}}
                                  product_{B in pi} kappa_r(B).

This explicitly defines one legitimate arithmetic object replacing a fully
connected model sector. It is not asserted to be the unique convention intended
by earlier notes, nor to equal their O_k*C_k integral. The cumulant expectations
are over actual Fourier root indices, not independent prime phases. Expanding
them gives explicit prime sums with product constraints and finite trace factors
from Section 2, one per cumulant block.

Degree five has 52 partitions: one {5}, ten {3,2}, and 41 containing
singletons. Therefore a lower bound on C5_actual alone is not yet a lower bound
on mu5 without control of the other sectors in this same finite convention.

Degree six has 203 partitions. The no-singleton sectors are

| Sector | Number of labelled partitions | Finite expression per path |
| --- | ---: | --- |
| {2,2,2} | 15 | product of three kappa_r(pair) |
| {4,2} | 15 | kappa_r(four positions) times kappa_r(pair) |
| {3,3} | 10 | product of two kappa_r(triple) |
| {6} | 1 | kappa_r(all six positions) |

There are also 162 singleton-containing partitions. Centering by subtracting
I does not set every local entry's empirical first cumulant to zero.
The scalar assertion tau(X_R^3)=o(1) does not by itself eliminate the
{3,3} tensor contraction. Thus the frozen three-number decomposition is a
CONDITIONAL model specialization, not an exact finite arithmetic ledger.

An exact Fraction regression reconstructs both degree-five and degree-six
moments from all partitions on a finite synthetic root ensemble. It checks
the combinatorics, not the asymptotic prime law.

## 5. Prime multiplicities and signs are a different classification

Unique factorization implies that a closed word of ordinary primes balances
positive and negative occurrences separately at each prime. Therefore no
ordinary-prime degree-five word has A=B. Positive fifth mass, if it exists,
must come from nonexact near products or proper powers; it cannot be recovered
as an ordinary-prime exact diagonal using PNT alone.

For degree six, closed ordinary-prime words have sign population 3-vs-3 and
prime-label multiplicities {2,2,2}, {4,2}, or {6}, with balanced signs in each
label. The last two LABEL collision classes have vanishing coefficient
diagonal mass: sum_p |c_p|^4=O(L^-4) and sum_p |c_p|^6=O(L^-6), by absolute
convergence. These are not the public connected-cumulant {4,2} and {6}
constants. Confusing the two classifications would discard the desired
connected correction entirely.

Nonclosed degree-five sectors include 3-vs-2; degree-six sectors include
4-vs-2 and 3-vs-3, as well as their conjugates and smaller sign populations.
Proper powers remain explicitly included in Section 2. Their small coefficient
second mass alone does not justify deletion from an unbounded degree-six
observable. A weighted higher-order estimate is needed.

The existing sign-spacing gate gives a per-word bound; summing it over all
weighted words also requires a summable estimate. Likewise the fast D2 gate
has a bounded independent-state contraction; it is not automatically a sixth
raw-moment bound for a state that contains the same primes.

## 6. OPEN: the current machinery does not transport positive C5 mass

Even granting the cited degree-four reductions, their negative-semidefinite
reference proves an upper bound. It supplies no quantitative lower bound on
the positive C5 sector. In particular:

- PNT's s ds measure controls prime-square contractions, not a 2-prime versus
  3-prime near-product correlation.
- The public C5 positivity concerns a closed normalized vector and a physical
  overlap kernel. It does not fix the sign of the actual band path factors or
  the oscillatory finite trace in Section 2.
- Rank deletion is safe for the bounded consumer but gives no direct raw fifth
  or sixth moment stability. Principal-section locality controls path range,
  not the tails of products of unbounded prime fields.
- The degree-four good-endpoint estimate relies on two product polynomials
  of length at most T^2 with bounded second mass. A fifth 2-vs-3 adaptation
  has one side of length up to T^3. Even assuming bounded coefficient masses,
  generic mean value plus Cauchy--Schwarz and 1/d gives only
  O(T^(1/2)/(epsilon_L L)), not o(1). A sixth 3-vs-3 version gives
  O(T/(epsilon_L L)). Additional geometric factorization would be necessary.
- The degree-four detuning feature representation does not establish a
  corresponding representation for either the 150-term fifth or the
  1082-term sixth kernel.

No lower-bound-preserving equality to 1/36 has been proved. Nor has the
relaxed sixth connected ceiling -1/189 been proved.

## 7. CLOSED: C6 evaluator and explicit structural falsifier

The standard ordered-partition cyclic construction has 1082 terms at b=6.
With v summing to zero its exact pointwise kernel is

    C6(v)=sum_{(P,sigma)} (-1)^(|P|-1)
                           (1-spread(merged-prefix walk))_+.

The accompanying tool evaluates this with Fraction arithmetic. Reproducible
search first located both signs, then exact arithmetic and cyclic/negation
symmetries checked the witnesses:

    v=(-7/10,4/5,-7/10,3/5,-2/5,2/5),
    O6(v)=1/5, C6(v)=2/5;

    w=(-1/10,3/10,-1/5,-3/10,4/5,-1/2),
    O6(w)=1/5, C6(w)=-1/10.

Thus the tempting representation as a universally negative Gram norm, or
minus a PSD diagonal evaluation, is impossible for this pointwise kernel.
This does not rule out a signed decomposition or a negative integrated
operator after additional variables are averaged. Positive leakage is real;
both witnesses lie in the supercritical region. No global sign claim is made.

The evaluator also builds the complete 93-wall common breakpoint arrangement
in five free coordinates and returns its exact sign signature at a rational
point, with zero entries marking cell boundaries. It reports a selected
active affine branch and checks its value exactly. Both witnesses meet three
walls, so these selected branches are not claimed to be gradients on an open
cell. No exhaustive five-dimensional cell enumeration has been performed.

## 8. Reproduction and effect on the kill gate

Run:

    python src/wp84_c5_c6_transport_audit.py
    python src/wp84_c5_c6_transport_audit.py --point=-7/10,4/5,-7/10,3/5,-2/5,2/5
    python src/wp84_m4_free_robust_cubic_r6000.py
    python src/wp84_c5_pointwise_supercritical_sign.py

The pre-change cubic regression and complete 148995-intersection C5
certificate both passed. The new audit checks the exact joint budget,
compression counterexample, full finite cumulant counts/reconstruction, and
exact C6 mixed-sign witnesses.

After the modifications the frozen cubic and sharp Loewner regression passed.
An independent 50-digit prime-branch/path check against matrix powers gives
degree-five residual 1.04405e-53 and degree-six residual 1.67048e-52.
These are numerical checks of the finite identity, not asymptotic evidence.

Pinned public engine copies were retrieved for inspection from
JoshuaHKU/zeta-0.7947-reproduction at
d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8, under
certificates/wp84_c5_c6_upstream/. Engine and archive hashes match the existing
WP81/WP79 pins, and every archived term is independently re-summed to C5=1/36,
{4,2}=-23/420, {6}=-1/126. The triple-pair source has four placement classes
T0=3/70, T1=1/90, T2=1/180, T3=1/70, assembled as
5*T0+6*T1+3*T2+T3=131/420. The full integrals were not rerun. These are model
evidence only. The public
polytope engine integrates two overlaps; it does not encode the intervening
Fourier projections or the fixed displacement mask in Section 2.

The consumer error region is CLOSED conditional algebra. Actual C5/C6
transport, sector elimination, and a common-normalization asymptotic
comparison are OPEN. The >79 theorem is not promoted.
