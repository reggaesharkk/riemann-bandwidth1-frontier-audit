# WP84 F1B — product-frequency endpoint budget repair

Date: 2026-10-10  
Base: `179f9959c4dabb675d1955646f212ddf6d3c51f5`  
Decision: **F1B-B — the generic two-factor normalized payment vanishes under an explicit maximal-truncation hypothesis, but the source feature generator and consumer identification needed to promote it are absent.**

This is an endpoint-payment audit, not a signed-arithmetic result. It does not change the prior F1 conclusion that Decision D's product-feature (O_R(1)) score claim has not been proved. It also does not establish any of the strict (>79\%), raw-cubic deletion, conditioned-Cayley, signed fifth/sixth, determinant-compatibility, prime-to-Weil, or zero-side statements.

## 1. Source objects and their different degrees

The audited notes support the following separation.

| Source object | Frequency degree and range | What the source actually proves | Status for this task |
|---|---|---|---|
| Linear prime-power fields α, β in `WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md` | (n=p^v\le N); phase (e^{i(T+hk)\log n}); degree 1 | α, β have coefficient square mass (O(1)), sampled mean (O_R(1)) on any translate of the endpoint window, and local neighborhood norm (K_R=O_R(1)). The fifth/sixth finite-path payment is ρ_b (=4bRK_R^b/d'=o(1)), (b=5,6). | Source-backed for that reprojection. It is not the pair-frequency detuning feature. |
| Fourth-order detuning feature in `WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION.md` | An ordered pair has phase (e^{i\tau\log(pq)}) and coefficient κ_pκ_q times bounded overlap/factor-slice weights. If both source factors are (n_1,n_2\le N), its support envelope is (N_{\rm feat}\le N^2). | The note proves exact indicator-feature reduction and identifies a moving prefix/interval truncation after fixing the other feature index. `WP84_BALANCED_PRODUCT_SECOND_MASS.md` proves (O(1)) coefficient square mass for its ordinary-prime pair family, with a wider stated pool through (X=e^L), and lower-order proper-power mass. | Structural two-factor description exists; the exact fixed-(R) generator, all gates and exact factor cutoffs are not executable or fully specified. The (N^2) envelope is conditional on both factors actually inheriting the original (n\le N) gate. |
| Generic polynomial written in `WP84_GOOD_ENDPOINT_TRIMMING.md` and Decision D | Written as (m\le N_{\rm feat}). | Its MV-plus-sampling calculation is valid once the actual support and coefficient mass are supplied. | It does not itself identify the product feature's (N_{\rm feat}), coefficient map, or threshold dependence. |
| Fifth/sixth first-strike consumer | The trace word has degree (b=5,6) when fully expanded, but the endpoint reprojection proof groups it through the local linear fields α, β. | The selected-neighborhood proof controls the whole weighted word error by (4bRK_R^b/d'), without forming a length-(N^b) polynomial. | Do not transfer a pair-feature score requirement into this proof, or conversely use its (K_R) result to certify the fourth-order detuning features. |
| Hidden-prime determinant callback | Requires external `source_mask(fid, slots, lag, T, section, alias)`. | No authentic callback-to-feature map is present. | No transfer from any result here. |

The source coefficients in the linear construction are

\[
c_n=-\frac{\Lambda(n)}{a_\phi L\sqrt n},\qquad n=p^v\le N,
\]

including every retained prime power. In the ordinary-prime pair-mass note,
\(\kappa_p=c_0\log p/(L\sqrt p)\) and
\(z_{p,q}=\kappa_p\kappa_qw_{p,q}\), \(|w_{p,q}|\le1\). For a genuine
two-factor source feature with both factors bounded by the natural cutoff,
the integer frequency is (m=n_1n_2\le N^2), not (N). The broader
coefficient-mass pool (p,q\le X) in the balanced-product note only gives a
possible (X^2) support envelope; it is not proof that the direct endpoint
feature uses that broader pool. Conversely, the original prime cutoff alone
does not authenticate every gate or prove that the complete feature consists
only of these pair terms.

No checked-in producer enumerates, at (R=6000), the complete
\(a_m^\pm(\theta;T,I_0)\): roots, signed paths, overlap weights, repeated
presentations, proper powers, endpoint dependence and exact source gates.
This remains the first source-definition gap. The manuscript path named in
the F1 audit is absent from the tracked tree.

## 2. Fixed-polynomial mean and discrete sampling

Let (J) be an interval of physical length (U+O(h)), with
\(h=2\pi/L), and let
\[
S(t)=\sum_{m\le D}a_m e^{it\log m}
\]
with duplicate integer frequencies combined. Distinct integers satisfy
\(|\log m-\log n|\ge\log(1+1/D)\ge1/(D+1)\). Montgomery--Vaughan's
Hilbert-inequality form therefore yields
\[
\int_J|S(t)|^2dt\le (U+2\pi(D+1))\sum_m|a_m|^2.
\tag{1}
\]
The starting point of (J) only changes coefficient phases. On disjoint
centered cells of width (h), the same elementary Sobolev estimate used in
`WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md` gives
\[
\sum_{t_k\in J}|S(t_k)|^2
\le {2\over h}\int_{J^+}|S|^2+2h\int_{J^+}|S'|^2.
\tag{2}
\]
Since \(\log m\le\log D\), applying (1) to (S') multiplies coefficient
square mass by at most \((\log D)^2\). For fixed degree (q), (D\le N^q)
implies \(\log D\le qL\). If the number of samples is comparable to
\(UL/(2\pi)\), dividing (2) by the *actual uniform sample count* gives
\[
\operatorname{Mean}_{k\in J}|S(t_k)|^2
\le C_q\left(1+{D\over U}\right)\sum_m|a_m|^2.
\tag{3}
\]
This is a valid fixed-polynomial bound. It is not an (O(1)) conclusion for
long support.

For the pair feature, the ordered coefficient square mass before frequency
collapse is bounded by
\[
\sum_{n_1,n_2\le N}|c_{n_1}c_{n_2}w_{n_1,n_2}|^2
\le\left(\sum_{n\le N}|c_n|^2\right)^2=O(1),
\]
if \w_ is uniformly bounded and the actual source factors are exactly
the stated natural-cutoff terms. The ordinary-prime collapse in the balanced
product note preserves (O(1)). Proper powers have the stated lower-order
one-factor square mass; their exact feature multiplicity still belongs in
the missing generator. Thus the coefficient-mass part is compatible with a
polylogarithmic majorant, conditional on those source hypotheses.

## 3. Moving thresholds: a proved generic maximal lemma

A fixed-polynomial estimate does not bound a supremum over truncations. The
following conditional lemma supplies a precise logarithmic loss.

Suppose (g_1,\ldots,g_K) are a fixed ordering of terms with integer
frequencies (m_j\le D), and every moving feature is a prefix or interval
of this same ordered list. Assume the coefficient vector does not change
when the truncation endpoint moves. Then
\[
\int_J\max_{r\le K}\left|\sum_{j\le r}a_je^{it\log m_j}\right|^2dt
\le C\log^2(2K)(U+D)\,\mathcal M\,\sum_j|a_j|^2,
\tag{4}
\]
where \(\mathcal M\) is an upper bound for the maximum multiplicity of an
integer frequency among the ordered terms. An interval sum is a difference
of two prefixes and changes only the absolute constant.

Proof: pad the list to a power of two. Every prefix is a disjoint union of
at most one aligned dyadic block at each scale. Cauchy--Schwarz over the
\(O(\log(2K))\) scales bounds its square by that factor times the sum of
the squared block sums over all blocks at all scales. At one scale the blocks
partition the list. Combine equal integer frequencies inside each block;
by Cauchy, the squared collapsed coefficient mass is at most
\(\mathcal M\) times that block's original mass. Apply (1) to each block,
sum the blocks at that scale, then sum the (O(\log(2K))) scales. This
proves (4). It does not assume orthogonality of exponentials on the short
interval.

For sampled maxima, set \(G(t)=\max_r|S_r(t)|\). It is locally Lipschitz,
with \(|G'(t)|\le\max_r|S'_r(t)|\) almost everywhere. The cell estimate
(2) applies to (G) using this derivative bound. Apply (4) to the derivative
prefixes; multiplying coefficients by \(\log m_j\) costs at most
\((\log D)^2\le q^2L^2\). The (h\) and \(h^{-1}\) factors in (2),
followed by division by (\asymp UL) samples, cancel the extra (L), so
\[
\operatorname{Mean}_{k\in J}\max_{r\le K}|S_r(t_k)|^2
\le C_q\log^2(2K)\,\mathcal M
\left(1+{D\over U}\right)\sum_j|a_j|^2.
\tag{5}
\]
For a two-prime-power product (m=n_1n_2), any one (m) has at most
\(O(L^2)) ordered decompositions into two prime powers (n_i\le N): it
has at most two distinct prime bases, and each exponent split has at most
\(O(L)) choices. Thus \(\mathcal M\ll L^2\) for that specified pair
pool. With (K\le N^2), the maximal factor in (5) is at most another
\(O(L^2)\). The resulting generic endpoint-score majorant is therefore of
the requested shape
\[
\mathcal B_T\le C_R L^4\left(1+{N^2\over U}\right),
\tag{6}
\]
for a fixed finite feature family, **provided** its actual coefficients
satisfy the stated mass bound and every threshold changes only a prefix or
interval in one fixed ordering. A fixed finite number of endpoint-adjacent
terms and feature integrals changes (C_R), not the exponent. If the source
weights themselves vary with the endpoint or threshold outside these
indicators, (4)--(6) do not apply. The notes do not verify that compatibility
for the complete WP84 feature map.

## 4. Final normalized payment and degree test

`WP84_GOOD_ENDPOINT_TRIMMING.md` gives the endpoint term for its rank-two
commutator reduction as
\[
\mathrm{Pay}_{\rm end}\le {C\over d'}\sqrt{B_-(T)B_+(T)}.
\tag{7}
\]
This is the exact payment form recorded there: each endpoint carries a
\(d'^{-1}\) rank-two normalization, and Cauchy in the finite feature
parameter produces the product of the lower/upper score square roots. If
both score means are bounded by \(\mathcal B_T\), Markov thresholds
\(2\mathcal B_T\) at both ends give
\[
\mathrm{Pay}_{\rm end}\le {2C\mathcal B_T\over d'}.
\tag{8}
\]
Thus bounded endpoint means are stronger than needed for this particular
normalized payment. They are not automatically dispensable if the consumer
contains a separate score admissibility condition.

Use the exact asymptotic scales
\[
X={T\over2\pi}=e^L,\quad
N\sim Xe^{-\sqrt L},\quad d'\sim d\sim XL,\quad
M\sim d e^{-\sqrt L/2},\quad
U={2\pi M\over L}\sim2\pi X e^{-\sqrt L/2}.
\]
For a fixed degree (q), put (D=N^q). Equations (3)--(5), with any
fixed polylogarithmic losses collected as (L^C), give
\[
{L^C(1+N^q/U)\over d'}
=O\!\left({L^{C-1}\over X}
+{L^{C-1}\over2\pi}X^{q-2}e^{-(q-1/2)\sqrt L}\right).
\tag{9}
\]
The degree ledger is:

| Degree (q) | Leading normalized term, up to (L^{C-1}/(2\pi)) | Outcome of generic bound |
|---:|---|---|
| 1 | (X^{-1}e^{-\sqrt L/2}) | Tends to zero. |
| 2 | (e^{-3\sqrt L/2}) | Tends to zero, even after any fixed power of (L). |
| 3 | (X e^{-5\sqrt L/2}=e^{L-(5/2)\sqrt L}) | Diverges; this majorant cannot close. |
| fixed (q\ge3) | (X^{q-2}e^{-(q-1/2)\sqrt L}) | Diverges for every fixed (q\ge3); no conclusion that the actual feature is large. |

For (q=2), (6)--(9) yield the conditional rate
\[
\mathrm{Pay}_{\rm end}
=O_R\!\left({L^3\over X}+{L^3\over2\pi}e^{-3\sqrt L/2}\right)=o(1),
\]
using (C=4) in (6). The score bound itself grows like
\(L^4 X e^{-3\sqrt L/2}\); it is not (O_R(1)). If instead the actual
factor pool is the broader (p,q\le X) admitted by the coefficient-mass
note and the support is (X^2), the normalized generic term is
\(L^{C-1}e^{\sqrt L/2}\), which diverges. The exact cutoff is therefore
load-bearing.

## 5. Consumer and simultaneous-selection audit

There are two nonidentical consumer statements in the source tree.

1. The fourth-order detuning endpoint argument uses (7). If its only endpoint
   requirement is to make that final normalized payment vanish, growing
   product-feature score thresholds are sufficient under (6), (8), and the
   natural (N^2) support. For this payment, (O_R(1)) endpoint means are
   unnecessary.
2. `WP84_DECISION_D_ENDPOINT_ADMISSIBILITY_DENSITY.md` says the direct
   first-strike endpoint theorem requires (O_R(1)) feature-score gates.
   The later first-strike source ledger instead records a one-prime local
   field bound (K_R=O_R(1)), and `WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md`
   proves its distinct payment (4bRK_R^b/d'=o(1)). Its one-prime sampled
   mean estimate is uniform on any translated candidate window satisfying
   N/(q h)->0; on the Decision-B window this ratio is N/U_T->0, so this
   separate linear-field gate can be reselected there. No source identity
   equates those (K_R) fields with the pair-frequency detuning features.
   The ledger explicitly says no high-product feature norm is assumed.

Consequently the repository does **not** prove that the direct first-strike
consumer needs the growing pair score, or that it accepts replacing its
stated (O_R(1)) product-score gate by a growing threshold. The one-prime
local condition is already bounded and cannot certify the fourth-order
product feature. Conversely, if the Decision-D product score is a genuine
separate consumer gate, (6) only gives a growing threshold and does not meet
that gate. This consumer-to-score identification is unresolved.

Conditionally, if the actual lower and upper endpoint statistics are exactly
those in (6), apply Markov to the *combined normalized score* at each end.
If there are (s) nonnegative endpoint conditions with means at most
\(B_j(T)), the statistic \(\sum_{j=1}^s S_j/B_j(T)\) has mean at most
\(s); threshold (2s) leaves at least half of each equally weighted
endpoint window good and bounds every score by (2sB_j(T)). The lower/upper
good-set product has exact pair density at least (1/4). Restricting the
nonnegative Decision-B boundary-energy mean to that Cartesian product costs
at most a factor four, without any independence assumption. The growing
product-score payment still tends to zero by (8)--(9); the separate linear
\(K_R) condition remains (O_R(1)). This is a valid conditional
simultaneous-selection argument on the same finite window, not a source
theorem until the feature map and consumer gate are authenticated.

No such statement transfers to the hidden-prime determinant iterator: its
callback and source-row map remain absent.

## 6. Decision and required corrections

**F1B-B.** A precise generic maximal estimate and vanishing normalized
two-factor payment are available under the explicit fixed-coefficient,
interval-truncation, (N^2)-support hypotheses. The complete actual source
degree/gates and the direct-consumer endpoint-score interface remain
unidentified. F1B-A is therefore not established. This is not a
counterexample and not a higher-degree failure for the actual fourth-order
feature. The generic method simply stops closing at degree three.

The narrow source evidence needed to promote the conditional repair is one
checked endpoint-feature generator specifying, for each finite (R=6000)
feature, the coefficient (a_m^\pm(\theta;T,I_0)), its exact source-factor
cutoffs and root/path weights, and proving that all threshold dependence is
only an interval selector in a fixed ordering (or supplying another
maximal bound). The direct consumer must then state whether its endpoint
condition is (7) alone or separately requires (O_R(1)) scores, and identify
those scores with either this generator or the independent one-prime
\(K_R) construction.

Proposed correction to Decision D and any manuscript: do not state that
product-frequency endpoint-score means are (O_R(1)) by using the
single-prime cutoff. State the conditional growing-score implication
\(B_T\ll_R L^4(1+N^2/U)\Rightarrow\mathrm{Pay}_{\rm end}=o(1)\) only
after verifying the exact generator and truncation hypotheses. Keep the
independent (K_R=O_R(1)) first-strike reprojection result in its own scope.
Do not describe the growing-score argument as closing Decision D, the
fourth-order arithmetic transfer, or any (>79\%) theorem.

## 7. Verification and scope

The endpoint payment identity (7) is transcribed from the finite rank-two
commutator calculation in `WP84_GOOD_ENDPOINT_TRIMMING.md`; the degree rates
in (9) were independently symbolically replayed after substituting
\(N=Xe^{-\sqrt L}\), \(U=2\pi Xe^{-\sqrt L/2}\), and \(d'=XL\):
the ratios are \(e^{-\sqrt L/2}/(2\pi XL)\),
\(e^{-3\sqrt L/2}/(2\pi L)\), and
\(Xe^{-5\sqrt L/2}/(2\pi L)\) for degrees 1, 2, and 3 respectively.
These give vanishing normalized generic bounds for degrees 1 and 2 and a
divergent majorant at degree 3, also after any fixed polylogarithmic loss.
The generic maximal lemma (4)--(5) is proved above by dyadic blocks,
Montgomery--Vaughan on each block, frequency-multiplicity Cauchy, and the
same sampling estimate; its hypotheses are stated explicitly so
source-incompatible threshold dependence is not silently accepted.

The existing Decision-D replay verifies only its conditional Markov,
weighted-density, and abstract energy-restriction arithmetic. It does not
verify the pair-feature generator or the maximal hypothesis here. The
adaptive-boundary replay concerns the one-prime field and likewise cannot
verify this product-frequency step. The artifact changes no prior note,
certificate, producer, replay, history, or `notebooklm_packet/` content.
