# WP84 — R400 endpoint quantifiers and near-product attack

Base commit: `6d4d43cea2479966ba0081dfbb38058fe6fffb87`
Audit branch: `codex/wp84-r400-endpoint-near-product-20261103`

This additive audit preserves the predecessor source, commits, certificates,
positive atoms, and negative results. It does not push, merge, publish, or make
an unconditional theorem claim.

| Decision | Result |
|---|---|
| `SCHATTEN_TRANSFER` | **PROVED** |
| `EXISTENTIAL_ENDPOINT_REDUCTION` | **NOT_SUFFICIENT** with current evidence |
| `ORDINARY_CONNECTED_AGGREGATE` | **OPEN** |
| `R400_CONSUMER` | **CONDITIONAL** on the selected-section record-budget inequality |

## 1. Result of the finite-T Schatten replay

The fourth-order source operator is the finite matrix already recorded in the
parent audit. With (u_n=log n/L), (z_n=c_n e^{iTlog n}), and
(F_k=sum_n z_ne^{2pi iku_n}), its fields are

\[
\alpha_k=\Im F_k,\qquad
\beta_k=2\Re\sum_n(1-u_n)z_ne^{2\pi iku_n},
\]

and the proper-power part on a section (I) is exactly

\[
Q_{400,I}=E_I\bigl(M_{\beta^{pow}}+[M_{\alpha^{pow}},J_{400}]\bigr)E_I,
\quad (J_{400})_{ij}=\frac{1}{\pi(j-i)}\,1_{0<|i-j|\le400}.
\]

This is a finite-(T) identity before the principal-section compression.
The diagonal is β_i; an in-band off-diagonal is
\((\alpha_i-\alpha_j)/(\pi(j-i))\); all other entries are zero. The band is
hard-truncated before compression. There is no circular wrap in the matrix.
The prior exact Gaussian-rational direct-integral replay covers diagonal,
in-band, and out-of-band entries.

### 1.1 The cited large-sieve theorem does transfer

Montgomery–Vaughan Theorem 1 is a trigonometric-polynomial inequality at
points separated modulo one. Its proof explicitly states the matrix
self-duality lemma (their Lemma 1): the coefficient-to-sample inequality and
its transposed form are equivalent. This is the needed step here; simply
calling the application “dual” without identifying the matrix is too terse.
The source states both the theorem and self-duality in the [author-hosted
paper](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf)
(Theorem 1 and Lemma 1, pp. 119–122).

For an interval (I=\{k_0,\ldots,k_0+m-1\}), form the matrix
\[
V_{r,n}=e^{2\pi i r u_n},\quad 0\le r<m.
\]
The theorem applied to the (m) consecutive integer frequencies (r) and
sample points (u_n\pmod1) bounds the map (V^T) by
\[
\|V^T\|_{op}^2\le m-1+\delta^{-1}.
\]
The same bound holds for (V), since a complex matrix and its transpose have
the same singular values. Absorb (k_0) into the arbitrary source
coefficients (z_n e^{2\pi i k_0u_n}). Thus, for every complex source vector,
\[
\frac1m\sum_{k\in I}\left|\sum_n a_ne^{2\pi iku_n}\right|^2
\le \left(1+\frac{\delta^{-1}}m\right)\sum_n|a_n|^2.
\]
The theorem’s diagonal contribution is included in (m-1+\delta^{-1}).

Here the source points are the distinct frequencies (u_n=\log n/L) for
distinct source integers (2\le n\le N). For consecutive source integers,
\[
u_{n+1}-u_n=\frac{\log(1+1/n)}L\ge\frac1{(N+1)L}.
\]
The wrap gap is at least (L^{-1/2}), because (u_n\le1-L^{-1/2}).
Therefore the circular separation obeys
\(\delta\ge((N+1)L)^{-1}\) for all sufficiently large (T). Aliases are
handled by this circular spacing; no diagonal-only estimate is used.

For every permitted section (m\ge d-2q), where
\(d=\lfloor TL/(2\pi)\rfloor\) and
\(q=\lfloor d/\sqrt L\rfloor\). Hence
\[
\frac{\delta^{-1}}m\le\frac{(N+1)L}{d-2q}=O(e^{-\sqrt L})=o(1),
\]
uniformly in the start and length of every permitted section. The constant
depends on the fixed (R=400), not on (T) or section location.

The coefficient square mass satisfies
\[
M_2^{pow}=\sum_{p^e\le N,e\ge2}|c_{p^e}|^2
\le\frac{64}{|a_\phi(T)|^2L^2}=O(L^{-2}).
\]
Apply the source-grid estimate to (F^{pow}) and to the beta field, whose
coefficients are (c_n(1-u_n)). Then
\[
\operatorname{avg}_I|\alpha^{pow}|^2\le(1+o(1))M_2^{pow},\qquad
\operatorname{avg}_I|\beta^{pow}|^2\le4(1+o(1))M_2^{pow}.
\]
For the actual matrix entries,
\[
\tau_I(Q^2)=\operatorname{avg}_I\beta_i^2+
\frac{2}{\pi^2m}\sum_{r=1}^{400}\frac1{r^2}
\sum_{i,i+r\in I}(\alpha_i-\alpha_{i+r})^2
=O_{400}(L^{-2}).
\]
This explicitly transfers the source mass through the finite Fourier grid and
the hard-band trace. Separately,
\[
M_1^{pow}\le\frac1{|a_\phi|L}
\sum_{p\le\sqrt N}\frac{\log p}{p(1-p^{-1/2})}=O(1),
\]
so \(\|Q\|_{op}\le2M_1^{pow}(1+2H_{400}/\pi)=O_{400}(1)\) on every
section. The (\ell^1) estimate is essential: normalized (L^2) mass alone
does not control operator norm, as the inherited exact diagonal-spike
countermodel shows.

Consequently
\[
\tau_I(Q^4)\le\|Q\|_{op}^2\tau_I(Q^2)=O_{400}(L^{-2}),\qquad
\left|\tau_I((A+Q)^4)^{1/4}-\tau_I(A^4)^{1/4}\right|
=O_{400}(L^{-1/2}).
\]
No target fourth-moment bound is assumed. I found no invalid use of
Montgomery–Vaughan in this transfer after making the transpose/self-duality
step explicit. **This proves the stated proper-power Schatten transfer, not
the ordinary-prime connected inequality.**

## 2. The consumer is existential; the current endpoint argument is not joint

The bounded-consumer route deletes (o(d)) endpoint rows, chooses one
principal section, and then applies the fixed-band quartic majorant there.
The proof therefore needs one common admissible section for each large (T),
not a bound on every conceivable section. The older uniform formulation
\(\sup_{I\in\mathcal G_T}\) is stronger than the consumer’s quantifier.

The required form is: there are sections
\(I_T\in\mathcal A_T\), chosen using all endpoint, boundary, normalization,
and source conditions, for which
\[
\limsup_{T\to\infty}\Re C_T(I_T)\le\Delta_{max}.
\]
Here \(\mathcal A_T\) is the common candidate family after endpoint-score and
boundary-energy restrictions, and \(C_T(I)\) is the source-matched physical
ordinary-prime connected aggregate defined in Section 3.

Separate existence is insufficient. The exact two-point counterexample in
the machine ledger has a nonempty endpoint-good set \(\{0\}\) and a nonempty
connected-good set \(\{1\}\), with empty intersection. Thus one cannot take
the F1C endpoint selection and a separate connected selection and assume they
coincide.

### 2.1 A sufficient joint-selection lemma, with its missing premise exposed

The source-authentic one-prime endpoint result gives lower- and upper-endpoint
good sets of density at least (1/2) each, hence a Cartesian endpoint-good
set of density at least (1/4). The nonnegative boundary-crossing score has
mean at most (C_B\log d) over the same endpoint-pair universe. Markov at
threshold (8C_B\log d) removes at most (1/8) of all candidate pairs.
Therefore at least (1/8) of all candidate pairs are simultaneously
one-prime endpoint-good and have crossing score at most
\(8C_B\log d\).

For any family (C_T(I)) of real connected contributions, if one could prove
\[
\frac1{|\mathcal X_T|}\sum_{I\in\mathcal X_T}(C_T(I))_+
<\frac18\Delta_{max}
=\frac{3675673694911}{1186000000000000},
\tag{1}
\]
then Markov shows that fewer than (1/8) of candidates have
\(C_T(I)>\Delta_{max}). Such a section intersects the simultaneously
endpoint- and boundary-good set. This is a valid joint-selection implication;
the missing content is the **source-valid mean bound (1)** for the physical
fourth-order product aggregate.

The selection preserves the other stated costs. Every candidate deletes
\(O(M)=o(d)) rows, so bounded-variation consumers pay (O(M/d)=o(1)).
The pair layer is stable uniformly over all contiguous (d-o(d)) sections:
its change is (O(R/d')+o(1)), with fixed (R=400). For a chosen section
whose crossing score is (O(\log d)), the recorded compression boundary
identity gives
\[
\frac{|\Delta_I|}{d'}\ll\frac{\log d}{d'}+
\frac{S_1\log d}{d'},\quad S_1=O(\sqrt N/L),
\]
which is (o(1)). The direct one-prime endpoint score also retains the
recorded fifth/sixth finite-path reprojection bound. These are distinct from
the missing fourth-order pair-feature estimate: F1C explicitly identifies
the product-frequency endpoint generator and its score-to-consumer identity
as missing. The one-prime score cannot be substituted for that product
score.

Accordingly, the correct decision is `NOT_SUFFICIENT`: existential selection
is the correct consumer target and the conditional joint lemma is proved,
but the current source evidence supplies no bound that makes its hypotheses
hold for (C_T).

## 3. Source-matched ordinary-prime grouping

Write
\[
D_m(x)=\frac1m\sum_{r=0}^{m-1}e^{2\pi irx},\quad
v_j=\epsilon_j\frac{\log p_j}{L},\quad
S=\sum_jv_j.
\]
The physical cumulant is the full 26-term ordered anchored-partition sum
\[
\kappa_m(v)=\sum_{\pi}(-1)^{|\pi|-1}
\prod_{B\in\pi}D_m\!\left(\sum_{j\in B}v_j\right),
\]
with the ordered block counts (1,7,12,6) and signs (+,-,+,-). The
source-matched fourth-order factor is
\(\Phi_{4,400,m}(v)=\Omega_{4,400}(v)\kappa_m(v)\), with the same filtered
root intervals, hard band, and ordered lag-path overlap as in the parent
report. The parent machine ledger
`evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json` preserves every labeled
anchored ordered partition product and coefficient, all 16 sign words, and
the six balanced words. This audit retains those six words exactly once in
each ordered tuple sum.

Let \(\mathcal E_2\) be the six balanced sign words. For each ordered tuple
and word define
\[
A=\prod_{\epsilon_j=+1}p_j,\qquad
B=\prod_{\epsilon_j=-1}p_j.
\]
Then \(S=\log(A/B)/L\), and the exact carrier on
\(I=[k_-,k_-+m-1]\) is
\[
e^{iT\log(A/B)}e^{2\pi ik_-\log(A/B)/L}.
\]
The complete balanced connected expression, before any near/far split, is
\[
C_T(I)=\Re\sum_{\epsilon\in\mathcal E_2}
\sum_{p_0,\ldots,p_3\le N\atop A\ne B}
\left(\prod_{j=0}^3c_{p_j}\right)
\Omega_{4,400}(v)\kappa_m(v)
e^{iT\log(A/B)}e^{2\pi ik_-\log(A/B)/L}.
\tag{2}
\]
Equivalently group (2) by exact integer pair \((A,B)\), defining its
coefficient as the sum over **all labeled prime splits and all six sign
words** with those products. No factor of six is added after that grouping.
The tuple coefficient ∏ c_p, external overlap, and physical cumulant remain
inside each grouped coefficient; replacing them by a function of (A,B)
alone would discard source information.

If (A=B), unique factorization says the two positive-slot prime
multisets equal the two negative-slot multisets. Those exact product
coincidences are the pair contractions already assigned to the pair layer.
This exclusion says nothing about (A\ne B), even when their products are
very close. The exact near-product group is, for any specified window (H),
\[
0<|T\log(A/B)|\le H,
\]
and its complement remains in (2); neither is discarded. The inherited actual
prime tuple \((101\cdot103=10403,\;97\cdot107=10379)\) remains a
nonexact summand with product gap (24). It is not an asymptotic sequence
or a positive aggregate certificate.

The individual cutoff relation \(N/T\to0\) is not a product-spacing
estimate. In fact
\[
\frac{N^2}{T}\sim\frac{T}{2\pi}e^{-2\sqrt L}\to\infty,
\]
and the integer-grid lower spacing at \(A,B\le N^2\) is only
\(T|\log(A/B)|\ge T/(N^2+1)\to0\). This establishes that the cutoff alone
cannot remove the dangerous product scale; it does not claim every integer
gap is realized by two prime products.

Each lower/upper endpoint window has about \(M\asymp T\sqrt L\) row choices,
so the pair family has about \(M^2\) candidates. One endpoint window spans
Fourier-frequency length \(U\asymp T/\sqrt L\). The phase alone averages
geometrically only once
\(T|\log(A/B)|\gg\sqrt L\). The range
\(T|\log(A/B)|\lesssim\sqrt L\) receives no cancellation from this
endpoint averaging. Moreover \(m\), and hence \(\kappa_m\), changes with
both endpoints; applying a geometric-series estimate to the carrier alone
does not bound the actual grouped coefficient. The generic mean-value bound
for pair frequencies up to \(N^2\) pays \(N^2/U\), which diverges in this
scaling, so it does not establish (1).

No Gram/Schur identity, one-sided arithmetic cancellation, or quantitative
bound for these actual weighted near-product groups is proved here. The
positive proper-power atom and the physical/geometric kernel mismatch from
the parent audit remain intact. The former is not evidence for the
ordinary-prime aggregate; the latter blocks importing the public nested
overlap sign theorem without a new source-matching identity.

## 4. Record threshold and remaining implication

The exact available record budget is
\[
\Delta_{max}=\frac{3675673694911}{148250000000000}
=0.02479375173633052276559865092748\ldots.
\]
With the independently recorded pair estimate
\(\mathrm{Pair}_{400}<0.266329+o(1)\), the budget would give
\[
w_{400}(I)\le0.29112275173633052276559865092748\ldots+o(1)
\]
on the common selected section, provided (1), or the direct selected-section
bound \(C_T(I)\le\Delta_{max}+o(1)\), is source-proved. The exact pair plus
budget fraction is \(43158947944911/148250000000000\). The current evidence
does not prove either condition, so the consumer remains conditional.

The separate 68.82027318675% route needs the stronger
\(C_T(I)\le0+o(1)\) gate; the record budget does not establish that route.
No conclusion is promoted about the 79.627% benchmark, a strict greater-than
79% theorem, or RH.

**Smallest unresolved source inequality:** prove, for the source-selected
sections that also satisfy the one-prime endpoint and boundary requirements,
\[
\limsup_{T\to\infty}\frac1{|\mathcal A_T|}
\sum_{I\in\mathcal A_T}(C_T(I))_+\le\Delta_{max},
\tag{3}
\]
or directly exhibit one such section with
\(\limsup C_T(I_T)\le\Delta_{max}\). Here \(\mathcal A_T\) is the already-admissible
common section family; (3) is the conditional-average form of the exact
existential target, not a uniform supremum requirement. The broader candidate
average threshold in (1) is a convenient sufficient condition.

## 5. Preserved evidence and reproduction

The parent positive atom \((p,p^2,p^3,p^2)\), its \(O_R(L^{-4})\) one-base
aggregate, the proper-power Schatten absorption, all 26 cumulant terms, the
48 labeled placement replay, and the geometric/physical kernel mismatch are
preserved and referenced in the source inventory. The older `GOOD_ENDPOINT`
claim for product-frequency features is not overwritten; the later F1C audit
records its missing source generator and consumer identity, so that claim is
not used here as a proof of (1) or (3).

The exact rational and finite logic checks are in
`src/wp84_r400_endpoint_near_product_audit.py`, with independent tests in
`tests/test_wp84_r400_endpoint_near_product_audit.py`. The complete report,
tests, machine-readable source hash inventory, and SHA-256 manifest are listed
in `evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_SHA256_MANIFEST.json` and its
`.sha256` sidecar. Tests replayed in normal, `-O`, and `-OO` Python do not
establish the unproved analytic estimate (3).
