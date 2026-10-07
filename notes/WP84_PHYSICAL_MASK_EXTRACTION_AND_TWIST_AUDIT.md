# Physical mask extraction and twist audit

Parent 876188d9f67cf8de5b3a15f6ed60b9ab3ea37596. Isolated branch
codex/c5-c6-attack-20261006; no push. Earlier Decision E is frozen. No new
consumer, actual mu7/mu8 integration or higher-degree route is attempted.

**Decision F: INCONCLUSIVE.** Exact physical ARITHMETIC-AUXILIARY mask extraction
exists at fixed T with finite norm. It uses mixed-slot matrix observables and
prime coefficient phases, not the existing scalar zero-side consumer. The
first uncertified gate is a UNIFORM estimate for the corresponding twisted
oriented discrepancies in the actual arithmetic norm, with comparisons that
also obey reconstruction. A bound on the single untwisted complete residual
does not supply such a family bound. No paid hardness transfer is proved.

New distinctions: global conjugation is useless on a closed trace; selective
slot conjugation recovers Delta; Delta alone does not recover the hard mask;
full slot/window/prime-equality characters do recover it as auxiliary data.
The reconstruction upper constant is large but is not a lower bound or a
proof of margin exhaustion. Natural untwisted physical amplitudes remain
uncontrolled. No complete physical cancellation coefficient is certified.

## 1. Exact quotient at fixed T,R

Use the parent resolved word/root space H_lab (with redundant deletion marks
allocated by the same frozen convention), retaining degree, actual prime-power
labels/signs, full lags, root, selected-section masks, insertion/deletion labels,
Delta, filter and carrier. At fixed T,R,N,I this is finite dimensional.

A maps labelled CONTRIBUTION coordinates to their summed carrier/root atoms:
(Ax)_(lambda,i)=sum_(alpha:lambda_alpha=lambda,i_alpha=i) x_alpha.
Root aggregation to sampled trace is an additional map. If using carrier-only
coordinates, sum the i atoms with their actual phases as in the parent. In either
version different paths at the same carrier/root are lost.
ker A consists of vectors whose contributions sum to zero in every retained
atom. M is the hard-coordinate selection followed by the exact inverse filter
multiplier and pair normalization from the parent. ker M consists of vectors
with zero selected/reweighted hard output. For the raw coordinate mask the
condition is simply that its selected coordinates vanish; for the final scalar
hard output additional cancellations inside that selection are possible.

The previous exact certificate has S=[1,1], raw mask=[1,0], vector=(1,-1).
It proves ker A is NOT contained in ker M on the free space. Equivalently a
mask descends to the quotient iff it annihilates ker A; boundedness requires
a bound in the actual quotient norm, not just coordinate TV.

## 2. Labels lost, and what the hard mask needs

A forgets full lags, selected deletion defect, pair slots, sign order, prime
assignment to slots, intermediate node/projection masks, endpoint path ranges,
filter-channel assignment and degree tags after the final scalar sum. Carrier
retains the REDUCED prime exponents and lambda; it does not retain cancelling
pair primes or how those exponents were assigned to leaves. Prime-cell membership
of unpaired factors may be inferred from a fully resolved carrier with known
signs, but not of the cancelled pair. A scalar primitive in xi loses still more.

To distinguish the hard mask from generic competitors, retain at least the
chosen slot path, signed prime-window membership per slot, identity of the
inserted pair, distinctness of lower primes, degree and required root range.
Delta by itself is not enough. The certificate supplies two unique-pair words
with the same carrier AND Delta=-2, but different insertion locations/lag paths.
Their Delta-character measurement has rank one while adjoining the hard mask
has rank two. This is an exact free-space falsifier, not a numerical sign test.

## 3. Actual matrix identities implementing twists

Let Q_theta=diag(exp(i theta k)) on Fourier indices. For any band matrix B,
(Q_theta B Q_theta^*)_(i,j)=exp(-i theta l) B_(i,j), l=j-i.
For a CLOSED word, conjugating every slot by the same Q telescopes to one:
tr((Q X Q^*)^n)=tr(X^n). Thus global diagonal conjugation cannot distinguish
any closed-path population. A spatial translation corresponding only to this
common phase has the same limitation.

For selected slots s,t, conjugate ONLY those two factors. Its exact closed-word
factor is exp(-i theta(l_s+l_t))=exp(i theta Delta_st). This is a legitimate
mixed matrix product, not a formal marker. The same identity holds for the
actual prime component matrices and explicit prime-pair correlations. In the
unmarked residual, sum the marked correlations with the frozen 1/D allocation;
this allocation remains the defined arithmetic object, not an extra zero-side
identity. A single mixed trace alone does not create that pair matching.

For Delta in [-2R,2R], q=4R+1 and theta_k=2pi k/q give EXACT inversion
 B_Delta=(1/q) sum_(k=0)^(q-1) exp(-i theta_k Delta) B(theta_k).
The coefficient l1 norm is one. For the hard mask more efficiently twist every
slot independently, theta_j=2pi k_j/(2R+1), j=1,...,n-1, theta_n=0.
Closed-path lag inversion recovers any specified l1,...,l_(n-1), with the final
lag fixed by closure. Its norm is one and its family has (2R+1)^(n-1) members.
At n7,R6000 this is 12001^6 members; do not enumerate them to evaluate the formula.
The same-Delta competitor is separated by these slot lags, not by global Q.

Insertion position is not a cyclic character visible in tr X^n: trace cyclicity
identifies common rotations. Mixed SLOT observables are physically definable
products of distinct matrix factors and break this equality of slots. Recover
pair positions from which slots have the prescribed prime-window/identity
labels; no fictitious position phase on an unchanged scalar polynomial is used.

## 4. Prime phases, windows, orientation and pair equality

For explicit ordinary prime components X_p^+ and X_p^-=(X_p^+)^*, define
 X(psi)=sum_p [exp(i psi_p) X_p^+ + exp(-i psi_p) X_p^-].
This is an actual Hermitian matrix assembled from finite Dirichlet coefficients.
Its construction is in physical_prime_matrix; no zeta/source interpretation
for arbitrary psi is claimed. Independent slot choices of psi attach the exact
leaf character exp(i eps_j psi_(j,p_j)). These are ARITHMETIC-ONLY AUXILIARIES.

A prime-window phase sets psi_p=eta 1_C(log p/L), leaving all nonordinary
prime-power leaves at phase zero, a directly specified change
of the known finite prime coefficients. For eta=2pi k/3 the leaf frequency
is eps*1_C in {-1,0,1}. A normalized three-point Fourier projector onto +1
selects the PLUS branch in C; onto -1 selects the MINUS branch in C. Norm one.
This implements a discontinuous cell switch because the auxiliary coefficient
operation itself reads the prime window. It is not claimed that three smooth
Mellin characters approximate a sharp interval exactly, or that the unchanged
matrix already contains these auxiliary observables.

For the selected pair slots in J, average SHARED independent prime phases
psi_p=2pi k_p/3 across those slots. Character orthogonality selects exactly the
same prime with opposite signs. Distinct primes give nonzero separate exponent
vectors and are killed. The projection norm is one; the finite family has
3^(#primes in J) members and is T-dependent. A torus integral gives the same
compact-family identity. No fixed-cardinality independent-of-T claim is made.

For equality of k selected slots with their prescribed signs, use independent
prime phases for the block and slot integer weights
(1,...,1,-(k-1)), divided by each prescribed eps at the coefficient phase.
Averaging roots of unity of order 2k-1 enforces all k primes equal: the last
prime must account for all k-1 positive units. This is an exact product of
coefficient-twisted factors, not a formal equality marker.

Distinctness is recovered by the EXACT partition lattice identity
 1_(all m labels distinct)=sum_pi [prod_(B in pi)(-1)^(|B|-1)(|B|-1)!]
                              1_(labels equal inside each B).
Its absolute coefficient sum is m! (permutations grouped by cycle partition).
The fifth mask has two positive-window and three negative-window primes,
whose windows are disjoint. The distinctness cost is 2!*3!=12. Sixth 2:4 and
3:3 masks have costs 48 and 36 respectively. These identities and norms are
independently checked. This avoids assuming prime indicators are free in the
norm of the UNTWISTED residual.

A global sign flip X->-X is implemented by psi_p=pi. Half the difference of
the degree-seven/eight residual at X and -X selects the odd order, with norm
one. It is arithmetic auxiliary; the physical zero-side matrix changes to
2I-H and its old eigenvalue/count interpretation does not follow. Carrier
parity characters on aggregated data supply no path information.

## 5. Exact reconstruction and norm certificate

The raw fifth hard-mask reconstruction consists of: degree parity projection,
full lag Fourier inversion, one signed-window projector per slot, pair-identity
phase average, and lower-prime distinctness inclusion--exclusion. Apply this
for BOTH orientations of the first pair. Each oriented component has all
projection/average norms one except distinctness 12. Summing them gives
 C_raw<=24.
No cancellation of the actual mask is assumed. This is a valid explicit upper
bound, not a proven optimal norm. Root admissibility is inherited from the
selected lag word; its root range is exactly I with the final two points removed.
For a root-by-root measurement, insert the actual diagonal root character
E_xi=diag(exp(i xi i)) and Fourier-invert it; this is another arithmetic-only
trace observable of norm one, not a new spectral consumer.

The hard inverse multiplier is factorizable in prime variables:
(1-alpha1)/f_-1^eps1(alpha1), (1-alpha3)/f_-1^eps3(alpha3), and the known
unit phase exp(-2pi i[2eps1 alpha1+eps2 alpha2+eps3 alpha3]).
On the frozen compact windows the magnitude bounds are B1=99/49,B3=143/49.
A bounded complex coefficient g, |g|<=B, has the exact representation
 g=(B/2)[exp(i(arg g+arccos(|g|/B)))
          +exp(i(arg g-arccos(|g|/B)))].
At g=0 choose opposite phases. These are explicit prime-dependent unit phases
in the actual Dirichlet coefficients; the minus branch is the conjugate, so
Hermitian pairing is preserved. Thus inverse-filter weighting is a linear
combination of physical coefficient-phase observables, with norm B1 B3.
It is NOT a pure bounded-frequency Mellin transform. Its normalization and
window cut are stated, rather than assumed costless.

C_T,J->C_J>=343/8921088; eventually C_T,J>=343/(2*8921088).
For the frozen consumer-scaled complete residual (c7!=0), the explicit
reconstruction upper bound for H_old^trim is

 C_extract=24 * [2*(14157/2401)*(8921088/343)] / |c7|
          = approximately 496043773947.67175.

The JSON contains the EXACT rational value. Its meaning is
 ||H_old^trim-error|| <= C_extract sup_(auxiliary twists)
                                  ||twisted discrepancy||,
provided each auxiliary comparison is reconstructed by the SAME formula,
and the discrepancy norm allows the stated linear operations. Normalized
integrated versions use the same total variation norm of the reconstruction
kernel. This is NOT an inequality from the one untwisted scalar gate. No
uniform twisted arithmetic error has been supplied; no actual hard-kernel norm
is declared invariant under arbitrary label restriction.

The old degree-six ideal and relaxed defect slacks are retained only for
comparison. Dividing them by this UPPER extraction bound gives sufficient
uniform auxiliary-error targets of approximately
3.1225864317157007e-15 and 1.8631629787834224e-16 respectively.
Their exact fractions are in JSON. These are not degree-eight paid allowances.
A finite large constant does not exhaust an asymptotic o(1) budget by itself.
No nonzero irreducible auxiliary error or lower bound on the optimum extraction
norm is proved. Thus Decision B would be unjustified.

## 6. Pure logarithmic/Mellin extraction: approximation and boundary gate

A logarithmic twist exp(2pi i t log p/L) is a coefficient phase with psi_p
proportional to log p. Uniform phase in the T carrier is likewise a legitimate
arithmetic height translation, but it multiplies only the signed frequency;
it does not mark insertion positions or cancelled prime identities.

No fixed finite smooth trigonometric sum equals a sharp interval indicator
on a continuum containing its boundary. For C=[a,b] on the alpha circle,
Fejer convolution gives
 g_K(alpha)=sum_(|r|<=K)(1-|r|/(K+1)) hat1_C(r) exp(2pi i r alpha),
 hat1_C(0)=b-a, |hat1_C(r)|<=1/(pi|r|).
Hence coefficient l1 norm is at most
 (b-a)+(2/pi)(H_K-K/(K+1)).
At distance >=delta from both boundary points, 0<delta<=1/2,
 |g_K-1_C|<=min(1,1/[(K+1)sin^2(pi delta)]).
This follows by bounding the Fejer tail; no prime theorem is used.
The remaining boundary strip |alpha-a|<delta or |alpha-b|<delta is explicit.
The CLOSED prime-square measure theorem bounds a REDUCED pair's boundary
mass after equality reduction. It does not bound the full signed near-product
word contribution in those strips. Paying that boundary term requires another
restricted-product discrepancy estimate. Neither smooth Mellin approximation
nor direct cell coefficient switching supplies the missing uniform theorem.

## 7. Measurement ranks and the physical-subspace distinction

Global Q/carrier-only measurement on the same-carrier pair of competing states
has rank one and fails mask factorization. Delta-only measurement on the
same-Delta certificate also has rank one; adding the mask raises rank to two.
Slot-lag characters separate that pair, yielding rank two. The full family
above annihilates every kernel vector with nonzero masked output: it reconstructs
M exactly on the WORD contribution space. Redundant deletion marks allocated
by the frozen convention are not independently physical coordinates; group
them first. The hard distinct-prime family has only one deletion mark anyway.
Thus ker A_aug subset ker M holds for this arithmetic-auxiliary family.
This is a finite-T rank/factorization theorem, not a uniform moment bound.

Define H_phys,natural precisely as the SET of amplitude vectors produced by
the original prime coefficients, natural L,T,N and specified selected section.
It is not a vector subspace. At fixed T and section it is one vector. The
linear span of that one vector has trivial kernel if its aggregate is nonzero;
that says nothing useful about uniform extraction constants. The actual kernel
question over naturally varying T/sections is UNRESOLVED. No arbitrary free
vector is asserted to be one original physical matrix's amplitude vector.

Define H_phys,aux-span instead as the linear span of actual mixed-slot
coefficient/lag/root-twisted Dirichlet-matrix correlations at fixed T. These
are legitimate finite arithmetic objects. Phase Fourier inversion can isolate
an actual leaf label/sign at each slot (finite prime code characters of order
>2#primes), specified lags and a root. Whenever its actual coefficient is
nonzero, the corresponding contribution coordinate is in this span. Therefore
free-coordinate cancellation vectors can be REALIZED AS LINEAR COMBINATIONS
of auxiliary measurements. This does not realize them as one untwisted matrix
and does not obstruct A_aug, which explicitly keeps the extra measurements.

An actual nonzero compatible masked ROOT atom is certified without numerical
sign guessing: L=10, T=2pi exp(10), primes (5;379,401;47,53,61), hard H=32,
with the selected M path. Rational Taylor upper/lower exponential bounds show
all leaves are below the natural cutoff (sqrt10<4, exp6>401), pair alpha5 in
[1/8,1/6], positive lower alphas in [11/20,13/20], negative lower alphas in
[7/20,9/20]. Products are 151979 and 151951; log(151979/151951)<28/151951,
T< (44/7)*22027, so T|lambda|<32. Filters at lags +/-1 and zero are nonzero
because 0<alpha<1. At any interior root the coefficient is nonzero; the two
pair orientations have positive cosine and no zero pair multiplier. The
certificate is a realizable auxiliary ROOT/word correlation, not the complete
sampled trace or a naturally selected-good-section theorem at that small height.
It disproves a blanket identity that all such auxiliary coefficients vanish.
It does NOT prove the full untwisted physical signed block is nonzero.

## 8. Zero-side compatibility and exact cancellation ledger

- Common unitary conjugation of the SAME Hermitian matrix: ALREADY ADMISSIBLE
  as a spectral identity, but contributes no new path data.
- Scalar spectral functions already in the source: admissible under their
  inherited hypotheses, but cannot independently mark words.
- Selective slot conjugation, prime/sign/window/Steinhaus phases, mixed traces,
  endpoint/root insertions and inverse-filter coefficient weights:
  ARITHMETIC-ONLY AUXILIARIES.
- Using those altered matrices/mixed traces as new zero-count consumers:
  REQUIRES NEW ZERO-SIDE THEOREM.
- A formal insertion-position character on unchanged tr X^n with no matrix
  implementation: INVALID; replaced here by mixed-slot identities.

The parent raw ledger still has coefficient 1 for each word, open allocation
1/D, exact filters/phases/endpoints and c7<0,c8>0. No cumulant subtraction is
silently added. Pair symmetry gives nonzero C_T,J on the selected mask; slot
characters isolate it but do not compute the untwisted sum of other paths.
Carrier conjugacy produces a real trace, not zero. The known R1 scalar diagonal
kappa8 is nonzero. No endpoint/insertion telescope cancels the selected bulk
atom by an established identity. The COMPLETE untwisted competing-population
coefficient remains UNCERTIFIED; so neither surviving full c_*!=0 nor complete
c_*=0 is reported. The masked pair coefficient has nonzero limit C_J, a different
and already-certified statement.

## 9. R6000 diagonal, budget and remaining gate

The previous arbitrary-fixed-R covariance formula and rational polynomial in
x=-1/(4pi^2) are reused. R1 regression remains positive. The open weighted sum
is not automatically a positive Gram functional; no monotonicity or all-R sign
has been proved. R6000 remains UNEVALUATED. No brute-force job is launched.

Degree-eight paid budget remains UNCERTIFIED; the relaxed uncharged witness
is not used as a margin. No family-wide twisted discrepancy estimate, reconstructed
comparison law or zero-side transfer for the auxiliary class is proved. Exact
extraction therefore cannot turn the single complete residual gate into a
hardness theorem. It also does not kill the arithmetic route by a norm lower
bound. The first missing gate is uniform control of the auxiliary discrepancy
family (or a physical cancellation/extraction theorem using a smaller family).

Requested report:
1. A: exact labelled carrier/root aggregation; free kernel inclusion fails.
2. M: selected hard word/window/path and inverse filter/pair normalization.
3. Lost labels: slot lags, pair identity/location, signed windows, roots/masks.
4. Physical twists: common and selective Q, explicit coefficient phases,
   prime-window phases, logarithmic phases and shared-prime phase averages.
5. Rank: Delta alone fails; full auxiliary reconstruction satisfies ker inclusion.
6. Reconstruction: exact finite Fourier/phase and Mobius formula above.
7. Norm: raw fifth mask <=24; trimmed inverse consumer bound in JSON (~4.96e11).
8. Zero side: only common conjugation is inherited; useful masks arithmetic-only.
9. Natural physical kernel: unresolved; aux-span is larger and reconstructible.
10. Competing full coefficient: explicit parent sum, not evaluated/certified zero.
11. Cancellation: selected C_J!=0; full untwisted cancellation UNCERTIFIED.
12. Hardness constant: conditional on UNIFORM auxiliary discrepancy, not untwisted.
13. Budget: old slack comparisons only; no paid degree-eight margin or exhaustion.
14. R6000 diagonal UNEVALUATED.
15. Strict >79 OPEN; actual mu7/mu8 deferred.
16. Local commit hash is reported in final response.

Artifacts: src/wp84_physical_mask_twist_audit.py (quotient/character tests,
physical matrix builder, equality/distinctness projector and exact norm certificate);
src/wp84_physical_mask_twist_replay.py (independent RGS norms, rank/constant
replay, two corruptions and actual-prime matrix identity regression);
notes/WP84_PHYSICAL_MASK_TWIST_CERTIFICATE.json (all exact constants/scopes).
The matrix regression is numerical algebra only; the identities are proved above.
Earlier local commits and notebooklm_packet are preserved. No push.
