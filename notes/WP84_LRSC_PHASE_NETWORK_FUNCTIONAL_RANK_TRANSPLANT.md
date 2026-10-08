# LRSC / phase-network functional-rank transplant

Parent 7addc6e33f6fd3053145155747e97f2a755f2e77, isolated branch
codex/c5-c6-attack-20261006. Decision **F**. No physical theorem or numerical
constant is a Riemann premise. Strict >79 remains OPEN, charge UNKNOWN.

The first missing step is an injectivity or full kernel characterization
for evaluation of the complete weighted atomic features on the span of
453 functionals. The proved upper bound on their real analytic rank is
453; no positive lower bound or exact rank is certified. The previously
certified symmetry reconstruction stays valid, but does not prove that
its 453 retained representatives are an independent basis.

## Provenance and evidence levels

The requested public repositories were read at these pinned heads:

- reggaesharkk/lrsc-odd-ring-spectral-rank:
  96cdd83ceadfff766d98ffdf2249a9de43fe74de.
- reggaesharkk/physics-v1-dynamical-sector:
  d409fd30bcd7c071ef92558f3fe8c1adff3f3022.
- reggaesharkk/navier-stokes-bridge-audit:
  4790a7edbabdcc8f4bdf1bde1c67b44f0ccc238f.

WP84_RANK_TRANSPLANT_SOURCE_MANIFEST.json records every downloaded original
path, pinned commit, Git blob ID, SHA256 and local cache path (28 files).
The cache is ignored; the hash manifest is committed. Exact mechanism
sources, with their full hashes available in that manifest, are:

1. LRSC odd-ring-rank-theorem/v1.2/THEOREM_v1_2.md and
   LRSC_Odd_Ring_Rank_Theorem_v1_2.tex: nonzero channel-scale removal,
   Chebyshev evaluation at distinct cosine nodes, and injectivity of the
   stencil on the masked channel span. The theorem proves matrix rank,
   not catalogue cardinality or minimum subset size.
2. LRSC odd-ring-rank-theorem/v1.2.2-supplement/README.md,
   ERRATA.md and source/part1_theorem.py, source/part2_build.py,
   source/run_bnb.py: independent reconstruction and distinction between
   matrix rank and finite subset cardinality. Numerical finite benchmark
   machinery is not imported as an analytic independence theorem.
3. LRSC finite-benchmark/mask-transition/REPORT.md: the exact update
   is separable because the added two sites are a reflection pair with
   identical channel values. This special reason for an outer product
   must be reproduced before using rank-one algebra elsewhere.
4. Physics appendix/v1.4/THEOREM.md, THEOREM.txt, README.md and
   appendix/v1.4.1/PROOF_AUDIT.md, CHANGES.md, README.md: impose the
   exact constraint before rational simplification and sign certification.
   The audit explicitly separates positivity of certificate coefficients
   from the identity connecting that certificate to the observable.
5. Navier-Stokes notes/WP16_036_LOCAL_PHASE_NETWORK_CERTIFICATE_2026_09_26.md:
   translation gives zero phase defect by the exact triad relation. Its
   local envelope bound does not prove a continuum statement.
6. Navier-Stokes notes/WP16_CROSS_CUTOFF_ORBIT_RANK_GATE_2026_09_25.md:
   response-vector construction is a prospective numerical diagnostic.
   Its SVD/effective-rank mechanism is NOT an exact-rank theorem.

Repository links: https://github.com/reggaesharkk/lrsc-odd-ring-spectral-rank,
https://github.com/reggaesharkk/physics-v1-dynamical-sector,
https://github.com/reggaesharkk/navier-stokes-bridge-audit.
No outside analytic estimate or broad theorem search was undertaken.

## Full-weight feature/evaluation construction

The feature constructor exports a symbolic finite-atom grammar for every
one of the 453 real representatives. It retains every raw orbit origin,
exact equality partition, signs, block multiplicities, ordinary-prime
windows, alias list, all closed Fourier paths, selected root section,
a_phi, carrier, sampled roots, raw cumulant coefficient 1 and external
consumer coefficient. It retains balanced blocks in the weight.

For each b,epsilon,pi assign distinct block primes q_B<=N,
N=floor(exp(L-sqrt(L))), X=T/(2*pi), L=log X, p_j=q_[j],
alpha_j=log(p_j)/L. For |l_j|<=6000 and sum l_j=0 define
u_0=0, u_j=sum_(i<=j)l_i, imin=k_- -min u,
M=max(0,d'-range u), d'=k_+-k_-+1. For k=0,...,M-1,

    atom amplitude=chi/d' * prod_j
       [-log p_j/(a_phi L sqrt(p_j))*f_l_j^epsilon_j(alpha_j)],
    atom phase=T*lambda + 2*pi/L *
       [sum_j epsilon_j*u_(j-1)*log(p_j)+(imin+k)*lambda],
    lambda=sum_j epsilon_j log(p_j),
    alias mask=1_(0<|lambda-mL|<=H/T), nearest residual [-L/2,L/2).

Use f_0=1-alpha, f_l^+=(1-exp(2*pi*i*l*alpha))/(2*pi*i*l),
f_l^-=conj(f_l^+), and the original real window chi. Summing these
atoms and taking the real part gives the representative exactly. Its
external coefficient is its raw orbit size times omega_b.

This defines a vector in the free full-atom feature space and a REAL-linear
evaluation E_T. Full feature-vector equality implies equal evaluations
by linearity. That implication is proved; it is not injectivity. Features
may have a nonzero vector in ker E_T, and different labelled atoms may
coalesce after actual logs, prime restrictions and path sums are evaluated.
The smallest faithful representation would be the quotient by the actual
common evaluation kernel over the admissible T family. That kernel is
UNKNOWN. No finite explicit smaller quotient or Vandermonde family is
certified. The exported grammar is exact and sufficient, not advertised
as smallest.

Removing an individual nonzero scalar is legal only after proving it is
nonzero on the actual support. No common scale is removed here: filters
can vanish, M can be zero, resonance masks depend on T, and different
multiplicity weights do not share a common evaluation row. In particular
453 different atom sums are not polynomial degrees evaluated at 453 known
distinct nodes. A Vandermonde proof cannot be copied without those facts.

## Two distinct incidence problems: cycle gauge versus closed displacements

For the abstract oriented b-cycle let B have entries
B_(v,e)=1_(v=e+1 mod b)-1_(v=e). Its rank over Q is b-1:
removing one vertex and the closing edge leaves a triangular minor of
absolute determinant 1. Its edge-cycle kernel is span{(1,...,1)}, dimension
1. Vertex potentials theta modulo constants have dimension b-1 and give
edge phase changes B^T theta. They telescope around the closed cycle.
Thus edge phase data modulo vertex gauges have one holonomy coordinate.
If eta are edge phases, the only invariant is sum eta; if sum eta=0,
eta is pure gauge. This is the exact analogue of zero network defect.

The Fourier displacement space is DIFFERENT. It is {l:sum l_j=0},
dimension b-1, parametrized by u_1,...,u_(b-1), with u_0=u_b=0,
l_j=u_j-u_(j-1). It is not ker B (which consists of constant circulations).
The bounded integer paths are a finite subset, not a vector space; these
dimensions concern the underlying rational linear constraints.

The arithmetic phase coefficients are epsilon_j*u_(j-1). In independent
symbolic alpha_j coordinates, with u_0 fixed and epsilon_j!=0, their
relative-prefix map has rank b-1. Hence the exact dimensions are:

    b=5: closed displacement 4; vertex-gauge image 4;
         graph cycle/holonomy 1; relative arithmetic phase rank 4.
    b=6: closed displacement 5; vertex-gauge image 5;
         graph cycle/holonomy 1; relative arithmetic phase rank 5.

There is separately one root-origin gauge per degree: u_j->u_j+c,
imin->imin-c leaves the FULL phase unchanged, since the two changes
contribute +c*lambda and -c*lambda. Changing the PHYSICAL root without
this compensation changes the carrier and is not a gauge. General
vertex potentials can be implemented by diagonal conjugation of all
compressed matrices; their factors telescope in the trace and the
compression projection commutes with that diagonal unitary. They do not
turn one multiplicity/equality/alias class into another. No further pair
of the 453 representatives is identified by these gauges.

After prime equalities, alpha variables are block logs and their rank may
decrease on a specific cell. Such a decrease is not analytic rank of the
prime sum. Near resonance is an inequality, not an exact equation to
eliminate; setting delta=0 would remove the actual survivor incorrectly.

## Elementary-transition and low-rank tests

The correct feature operator for a fixed finite-T atom domain is a
multiplier D(w)=diag(w_atom), followed by actual evaluation. A change in
weights or masks has Delta D=diag(Delta w_atom), whose exact symbolic
rank is the number of nonzero diagonal entries. This provides a concrete
matrix representation for every elementary mask/weight transition once
its affected atoms are specified; it is not generally rank one.

- Equality-block merge: changes assignment domain, nu powers, masks and
  phase. Embed both domains into their union; differences are supported
  on many coordinates. No fixed common vector h is established.
- Alias change: changes disjoint near-window masks at different X^m.
  Union-domain diagonal rank is the number of affected nonzero atoms.
  Reciprocal conjugation is an exact symmetry, not an independent update.
- Compensated root-origin shift: Delta=0 exactly, rank zero.
  Uncompensated physical root: diagonal phase multiplier differences,
  potentially on every nonzero atom; no fixed small rank follows.
- Fourier displacement change: changes filter factors, prefix phases,
  M and imin. In a common domain it can affect many atom coordinates.
  Cyclic/reversal symmetries remain rank-zero observable changes.
- Prime-window boundary: one added PRIME is not one added atom. It can
  participate with every assignment of the other blocks, many Fourier
  paths and sampled roots. Rank is atom-support dependent, not automatically
  one. Degenerate empty support gives rank zero, not a universal law.

The transition builder exports exact diagonal examples of sizes 1,2,3,6,
with entries 1,...,n, rank n and determinant n!. These are symbolic
countermodels to inference of rank one from mask terminology, NOT proofs
that a particular prime transition attains these ranks. The formula
rank Delta D=#nonzero affected coordinates is exact; actual counts and
cancellations depend on the arithmetic domain. The minimum proved
state-generator count g and actual generator rank remain UNKNOWN.

A tautological one-row change in a matrix with 453 labelled rows is rank
one, but using 453 such unrelated rows manufactures no compression.
The LRSC mechanism requires common h across all channel columns because
of exact evaluation equality at the new sites. No corresponding common
Riemann response vector has been proved. Sherman-Morrison/Woodbury is
therefore not invoked. The general rank inequality for a genuine update
is valid but supplies only rank<=453 here, not a sharper bound or sharpness.

## Exact orbit response, Gram firewall and symbolic certificates

Stack responses to four/five independent vertex gauges and the two
compensated root-origin gauges. The exact response matrix is 453 by 11,
identically zero: rank 0, left nullity 453, right nullity 11. Both row and
column bases are empty and both null spaces have their standard bases.
This is a faithfully ZERO response to these specified gauges, not a
complete elementary-transition response. For the non-gauge transitions
above no small fixed generator family has been certified, so no complete
finite orbit-response rank is claimed. A zero gauge-response matrix says
nothing about rank of the unperturbed functional family.

The independent-label feature Gram can be I_453, rank 453, determinant 1,
no null vectors. It is explicitly a proxy: the arithmetic evaluation may
have a kernel, and these labels need not remain orthogonal or independent
after evaluation. An actual Gram for the functions of T could be defined
using an admissible positive measure over heights, but its entries would
be correlations of the very prime sums at issue. No exact entries,
nonzero minor, rank or null relations of that Gram have been established.

For the certified phase-incidence minor, root-compensated maps and formal
update diagonals, redundant variables are eliminated by u_0=u_b=0 and
sum l=0. Their exact determinants are +/-1 and n!, respectively; there
are no denominators to clear and their positive signs/nonvanishing follow
from exact factors. The zero-response minors vanish identically. These
certificates address the identified rational matrices only. There is no
candidate decisive ANALYTIC minor to certify by positive coefficients,
Sturm chains, resultants or intervals. Logarithms, exponentials and
shrinking inequalities do not become rational polynomial variables merely
by naming them. We do not confuse sign of a proxy minor with equality of
that proxy to the actual function-space Gram.

## Reconstruction, fifth/sixth and bound consequence

Every one of the 8,740 raw classes has a reconstruction record containing
its phase pattern, phase orbit and full-weight representative. The exact
path is raw -> certified dihedral/conjugate representative; the phase
pattern/orbit are metadata projections, not enough to reconstruct weights.
There is no new basis identifier because no smaller analytic basis is
proved. The parent exact orbit replay remains the identity verifier.

The parity sum |e_B| congruent b mod 2 is preserved. Root/vertex gauges
alter neither multiplicities nor carriers. No fifth/sixth class becomes
the same class under these transformations. Disjoint formal label spaces
are proved; disjoint ANALYTIC functional subspaces are not. Taking real
parts, or quotienting the gauge, does not supply a new cross-degree relation.

No certified r was obtained, so no new basis-weighted arithmetic bound is
computed. The old retained-family coefficient mass and sufficient common
bound 1.7670578586835696e-8 remain unchanged and unachieved. One must not
replace that bound by Delta_rel/453 or by a phase-cycle dimension. Optimal
weighted allocation would require a proved reconstruction and individual
certified costs/sign information; none is newly available.

**F. INCONCLUSIVE:** first missing step is evaluation-kernel faithfulness
on the full weighted span. Certified ranks are graph incidence 4/5,
cycle 1, zero-gauge response 0, parent formal incidence 453; actual
state-generator rank UNKNOWN; analytic rank upper bound 453, exact rank
UNKNOWN; no smaller basis, no new analytic null relation, no paid charge.
Strict >79 remains OPEN. All previous audit commits and notebooklm_packet
are preserved. Local commit hash is supplied after additive verification.
