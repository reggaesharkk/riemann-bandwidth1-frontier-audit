# WP84 Consolidated Hostile Proof Audit: Decisions B–O

**Audit snapshot:** branch `codex/c5-c6-attack-20261006`, HEAD `8d1163d3396291ccfcdc4f8ff5a4e21d6bf616a2`  
**Scope:** independent algebraic, exponent, source-scope, and replay audit of Decisions B–O.  
**Disposition:** strict (>79\%\) remains **OPEN**. This report is not a proof of a zero-proportion theorem and does not alter any frozen source note or certificate.

## Executive verdict

The audit confirms a collection of exact finite-matrix identities and several source-specific estimates with deliberately limited scopes. The strongest completed pieces are: (i) the finite-section block formula and scalar-background payment for arbitrary sections, together with a complete boundary correction o(1) for an existential adaptively trimmed section; (ii) the same-window endpoint-density selection for the *direct* first-strike consumer; (iii) exact cubic block and zero-carrier decompositions; (iv) exact finite-frequency/path and product-separation reductions; and (v) the carrier linearization and Fourier-completion bookkeeping in the critical block.

None of these supplies the missing full source-weighted signed cubic correlation, the signed fifth/sixth arithmetic gate, or the remaining prime-to-Weil and zero-side transfers. Decision O rules out only the tested completion and Cauchy-dispersion bounds at their displayed exponents. It is neither a counterexample to the arithmetic target nor a no-go theorem for all methods. The masked determinant consumer remains a distinct, source-incomplete route.

**Primary decision-level count (14 decisions):** 11 contain at least one in-scope exact identity or limited analytic estimate that survives this audit (B, D, G, H, I, J, K, L, M, N, O); 3 are primarily conditional reductions toward their stated cubic-transfer target (C, E, F). One displayed exponent formula in M is false as printed and is corrected below; its qualitative small-singleton theorem survives. No source-legal counterexample to the WP84 arithmetic inequality was found. Finite and abstract counterexamples remain stress tests only.

These counts describe each decision’s surviving *component*, not closure of every requested scope. In particular, Decision B's arbitrary-section uniform claim, Decision E–H's raw-cubic transfer claims, and Decisions J–O's full-residual claims remain open. Replays are computational checks of stated algebra and finite bookkeeping; they are not by themselves proofs of asymptotic estimates.

## Evidence hierarchy and claim discipline

The labels used here follow the requested scheme:

| Label | Meaning |
|---|---|
| **A** | Exact algebra independently checked. |
| **B** | Analytic estimate whose hypotheses and stated scope fit the source object. |
| **C** | Correct implication conditional on an explicitly missing estimate or inherited hypothesis. |
| **D** | Finite computational certificate/diagnostic only. |
| **E** | Unsupported inference or unresolved proof gap. |
| **F** | Falsified displayed statement. |
| **G** | Source definition is insufficient to instantiate the claimed object/bridge. |

An item can contain multiple labels: for example, an identity can be A while its asymptotic use is C/E. “Proved” below means only the exact scope stated in the underlying note. It does not silently enlarge a finite identity into a natural-cutoff limit.

## Decision-by-decision proof ledger

### B — finite-section cubic boundary transfer

**Survives (A; limited B):** For (P) the contiguous-section projection, (Q=I-P), and Hermitian block matrix

\[
H=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},\qquad A=PHP,\quad B=PHQ,\quad D=QHQ,
\]

cyclicity and block multiplication give the exact identity

\[
\operatorname{Tr}(PH^3P)-\operatorname{Tr}((PHP)^3)
 =2\operatorname{Tr}(A BB^*)+\operatorname{Tr}(BDB^*).
\]

For the source decomposition (H=s_0I+V), the scalar-background contribution separates exactly as (3s_0\|PVQ\|_{HS}^2), with the remaining term the signed (V)-cubic boundary residual. The crossing count at displacement (q) is (2\min(q,d')); the accepted harmonic envelope yields

\[
\|PVQ\|_{HS}^2\le {8S^2\over\pi^2}(H_{d'}+1),\qquad S=\sum_{n\le N}|c_n|=O(\sqrt N/L).
\]

At the natural cutoff, the scalar payment for every admissible section is (O(N/(TL^2))=O(e^{-\sqrt L}/L^2)=o(1)). The source-form finite-matrix replay independently checks the block identity, scalar coefficient, crossing count, and hostile sign/omission mutations.

**Arbitrary-section statement (E):** uniformly over all admissible sections, the full normalized signed (V)-cubic residual is not proved (o(1)). The accepted absolute envelope (O(N^{3/2}\log(d')/(TL^3))) does not decay at the natural cutoff. No cancellation is inferred from Hermiticity.

**Adaptive selected-section statement (B):** `WP84_ADAPTIVE_BOUNDARY_LOCAL_LARGE_SIEVE.md` proves that, inside any original length-d source interval, there is an endpoint pair (0≤u,v≤M), with (M=ceil(d exp(-sqrt(L)/2)))=o(d), whose contiguous trimmed section has (E(I)=||P_I V(I-P_I)||_HS^2=O(log d)); the total number u+v of deleted rows is at most 2M=o(d). The local large-sieve bound and endpoint-shell averaging retain the natural prime-power cutoff and all source coefficients. Substitution into the exact block identity gives the complete normalized finite-section boundary correction (O(S log(d)/d')=O(sqrt(N)/(T L))=O(exp(-sqrt(L)/2)/(sqrt(T) L))=o(1)) on that selected section. This is existential under the source hypotheses (a_phi(T)->1) and (s_0(T)->1), not a uniform-in-section theorem.

This adaptive result does not transfer the raw cubic trace from the full interval to the trimmed interval. That is the separate deletion/UI question in Decision E. Nor does it prove the unpaid high-product signed fifth/sixth arithmetic estimate.

### C — same-section compatibility and raw-cubic deletion

**Survives (A/C):** empirical-CDF interlacing gives bounded-observable deletion stability with an (O(r/d)) loss when deleting (r) rows. The conditioned two-atomic witness and the sixth-moment spike stress test replay exactly. These show why first two moments or small rank alone do not control raw cubic deletion.

**Conditional (C/E):** transfer for the unbounded cubic observable needs uniform integrability, e.g. an actual-source sixth Schatten bound or another explicit tail estimate. No such bound follows from a fourth-moment estimate alone. The moment-only conditioned-Cayley obstruction is abstract; it is not an actual zeta-source spectral law. Decision D later resolves endpoint selection for the direct consumer only; it does not repair this raw-cubic implication or the determinant route.

### D — endpoint admissibility and density

**Survives (B, in exact scope):** on Decision B’s equally weighted endpoint-pair window, the existing endpoint score estimates can be reapplied at the natural cutoff using their finite Dirichlet-polynomial mean-value and sampling steps. Markov gives at least half of each endpoint window good, hence the Cartesian product of separately admissible endpoints has weighted density

\[
\gamma_T\ge {1\over4}.
\]

Since crossing energy (E(I)\ge0), the adaptive theorem's endpoint averaging bounds its mean over the full Decision B pair window with the same finite uniform weights,

\[
\mathbb E_{(u,v)\in G} E(I_{u,v})\le {C_B\log d\over\gamma_T}\le 4C_B\log d.
\]

Thus a common pair meets the direct endpoint-score gates and has (E(I)=O(log d)); the same interval is covered by Decision B's complete adaptive finite-section boundary estimate. Equivalently, the conditional mean of nonnegative E on the admissible Cartesian subset is at most four times the full-window mean. This does not assume independence or favorable correlation. For a general weighted window, the relevant density is weighted mass, not unweighted cardinality. The density loss inserted into the boundary estimate gives the sufficient condition

\[
{\gamma_Td'\over(1+S)\log d}\longrightarrow\infty.
\]

A fixed (1/4) density satisfies this scale. The inherited constants (C_B,C_R) are (O_R(1)), not explicit numerical constants.

**Scope boundary (G):** these endpoint features belong to the direct first-strike consumer. They have no proved identity with the hidden-prime determinant callback `source_mask(fid,slots,lag,T,section,alias)`, its selected rows, root sums, or normalization. D is not an admissibility theorem for the masked determinant route.

### E — prime-source cubic deletion stability

**Survives (A/C):** the full-trace deletion identity, including the deleted-block cubic and dimension renormalization, is exact. A uniform actual-source τ(|H|^6) bound, or a weaker cubic uniform-integrability estimate, would suffice for the relevant tail step.

**Open (C/E):** neither the sixth Schatten bound nor the needed prime-source UI estimate has been proved. The diagonal-spike example has rank fraction tending to zero and cubic loss one, but is abstract and is not a prime-source counterexample. The first missing estimate is a bound on the normalized deleted-block cubic (with the correct dimension correction), or a source-derived condition that makes this quantity (o(1)). Finite diagnostics do not establish this asymptotic statement.

### F — exact signed deleted-block cubic

**Survives (A):** the scalar, linear, quadratic, and cubic decomposition is exact; zero diagonal gives \(\operatorname{Tr}W=\operatorname{Tr}(B^2W)=0\); the C1/C2/C3 index expansions and ordered-triangle multiplicities are checked. A rational three-index Hermitian example has \(\operatorname{Tr}(W^3)=-18\) before the common normalization, disproving a proposed cyclicity-based cancellation.

**Conditional/open (C/E):** the replay also gives an abstract signed-mean counterexample showing that zero signed mean does not control absolute endpoint mass. The prime-source residual remains unpaid. The rational matrix is not source legal; it falsifies only the alleged universal algebraic cancellation.

### G — one-sided cubic localization

**Survives (A/C):** the separated-block cube identity has the factor (3) on the cross interaction. The cross-block term is small only by the stated distance estimate, not identically zero. Exact row-increment and centering identities retain the unknown source mean.

**Open (E):** the reduction leaves a one-sided centered cubic endpoint statistic for the actual source. L2/L3 endpoint bounds, signed cancellation, or selection of a different endpoint do not supply it. Hostile tests reject those substitutions. No unconditional raw-cubic estimate follows.

### H — global cubic-score discrepancy

**Survives (A):** the full-score trace identity and diagonal contribution have the stated coefficients and normalizations.

**Open (E):** the available local score-square control does not reach the required global cubic discrepancy scale. An interior-spike array shows abstractly that endpoint S2 control can coexist with a large interior cubic score; it is not prime-source data. Signed average cancellation does not bound absolute partial sums. A source-localization or global discrepancy estimate is missing.

### I — zero-carrier prime resonance

**Survives (A/B, narrow sector):** exact UFD enumeration shows the zero-carrier equation closes only on the stated same-base prime-power configurations; the six sign placements, ordered exponent pairs, and multiplicities yield the factor (48) (and the two-endpoint expression’s factor (192)). The finite-(J) compression factor is used only under its norm-≤1 hypothesis. The exact zero-carrier contribution has the stated (O(L^{-3})) operator scale, yielding the stated centered-endpoint (O(M/L^3)=o(d)) contribution under the note’s normalization.

**Scope limitation:** this discharges only the exact zero-carrier sector. Nonzero/near aliases and the complete endpoint discrepancy remain open; “zero carrier” is not a proof that the full near-resonance mass vanishes.

### J — full-frequency cubic path reduction

**Survives (A/B, limited):** the finite-lag/root-restricted cubic expansion matches direct matrix multiplication; orientation and endpoint intersections are checked. The discrete Young lag bound and its (R^{-1/3}) tail are valid with the weights shown. The fixed-gap far-frequency estimate improves the inherited envelope.

**Open (E):** after insertion of the actual source coefficient mass, the weighted fixed-(R) tail is not shown negligible at natural cutoff. It is explicitly retained rather than declared (o(1)). The finite-(J) compression and root terms remain part of the source expression. The result is a representation and partial estimate, not the full-frequency signed discrepancy.

### K — central alias exclusion and low-product discharge

**Survives (A/B, limited):** integer separation proves the central nonzero-coherence range empty under the stated inequality (M>L(eN+1)). The low-product absolute estimate is valid in its stated exponent range θ<2/3; full prime powers, lags, and the finite root sum are retained.

**Open (E):** the high-product region is outside this estimate. Finite ordered-divisor checks verify multiplicities but do not replace the asymptotic source-weighted signed estimate.

### L — square-root product and same-sign first alias

**Survives (A/B, limited):** the low nonzero-product estimate extends to each fixed θ<1 under the note’s stated hypotheses. The square-root integer-separation/divisor argument discharges the complete same-sign first-alias sector, including exact and near centers, with all prime powers in scope.

**Open (E):** the result does not apply to mixed signs or the high-product/fringe sectors. It does not imply cancellation in those terms.

### M — mixed first-alias small-singleton sector

**Survives (A/B, with correction):** the near/small-singleton argument, exact/near alias partition, reciprocal-sign reflection, and epsilon conditions are supported by the independent finite replay and the written divisor argument. Under the note’s restrictions (near η<1/2 and whole-bin far η<1/4), the intended small-singleton contribution is (o(1)); the full mixed-sign residual remains open.

**Falsified displayed formula (F):** the certificate/note’s first normalized near bound omits one factor of (X^\epsilon). M.4 gives the first unnormalized term (X^{\epsilon-1/2}MZ^\epsilon). With (M=ceil(d exp(-sqrt(L)/2))), (d\asymp XL), and (Z=X^\eta),

\[
{X^{\epsilon-1/2}MZ^\epsilon\over d}
=X^{-1/2+\epsilon(1+\eta)}e^{-\sqrt L/2}(1+o(1)),
\]

up to fixed implied constants. The second M.4 term similarly gives (X^{-1/2+\eta+\epsilon(1+\eta)}L). Thus the first normalized exponent is

\[
X^{-1/2+\epsilon(1+\eta)}e^{-\sqrt L/2},
\]

not the printed (X^{-1/2+\epsilon\eta}e^{-\sqrt L/2}). For the near bound the original valid choice is (0<ε<(1/2-η)/(1+η)); it makes both corrected near exponents negative. The whole small-singleton first-bin conclusion additionally retains the original far-range restriction (0≤η<1/4). No endpoint η=1/4 or η=1/2 is asserted. The old frozen certificate is not modified; this report records the correction.

### N — coherent alias to modular correlation

**Survives (A/B, limited):** the real-center and additive-character identities are exact; the carrier replacement has the pointwise error stated in the note and the aggregate source-weighted error is (O_\epsilon(X^{-1/2+2\epsilon}e^{-\epsilon\sqrt L})=o(1)) in its range (including endpoint and prime-power leaves). The CRT/DFT argument is not separable because the source weight couples the variables. The source-dependent absolute baseline is (O_\epsilon(X^{1/10+8\epsilon/5})).

**Open (E):** no signed modular saving for the coupled source weight follows. A separable DFT estimate cannot be imported without a proof of that separability or a replacement theorem.

### O — critical signed dispersion feasibility

**Survives (A/B/D, method-limited):** in the representative block (B\asymp X^{3/5}), (n_1,n_2\asymp X^{4/5}), the admissible (n_2) interval has width (O(X^{-1/5}e^{\sqrt L/2})=o(1)), hence at most one integer. This gives no prime-power occupancy or sign information. The existing divisor/absolute bound is

\[
O_\epsilon(X^{1/10+8\epsilon/5});\quad \epsilon=1/100\implies X^{29/250}.
\]

Exact sharp interval Fourier completion is valid, but costs (O(LX^{7/5}e^{-\sqrt L/2})), worse than baseline by (321/250-o(1)) powers. The tested Cauchy dispersion estimate is (O(X^{3/10-o(1)})), also insufficient. The exceptional (B=2^v) subfamily alone is (O(X^{-17/50})) at ε=1/10 and is (o(1)).

**No-go scope:** these calculations show only that this exact completion and this Cauchy bound do not pay the needed exponent. The first unresolved term is the source-weighted signed (B\ne B') off-diagonal prime-power correlation, including shared-prime/proper-power gcd strata, narrow product-window intersections, finite-(J) factors, roots, and endpoint. No counterexample to the original inequality, and no impossibility theorem for other analytic methods, is established.

## Hostile arithmetic checks and theorem assumptions

The independent replays exercise exact signs, dimensions, proper powers, repeated bases, exact versus near integer centers, endpoint orientation, all stated finite (J) and (R) boundaries, root centering, and selected omitted-term mutations. The full commands and their scope are listed below. These checks do not prove uniform asymptotics in (T), endpoint position, or a source mask.

The endpoint mean-value invocation is the classical Hilbert/Montgomery–Vaughan mean-value framework for finite Dirichlet polynomials with integer frequencies. Its use is appropriate only for the finite endpoint feature polynomial and the length/weight bounds recorded in Decision D; it gives no theorem for the coupled signed multi-prime product in Decisions N–O. The reference is H. L. Montgomery and R. C. Vaughan, “Hilbert’s Inequality,” *Journal of the London Mathematical Society* (2) 8 (1974), 73–82, [DOI](https://doi.org/10.1112/jlms/s2-8.1.73), [author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf). No stronger literature result is imported here.

Specific checks:

- Floor/ceiling and dyadic endpoint effects are retained where an interval is proved to have length (o(1)); that conclusion is “at most one integer,” not a density assertion.
- Proper powers and repeated bases are counted in the UFD/divisor strata and not silently treated as independent primes.
- Exact carrier aliases, sampled aliases, and near-integer product centers are kept distinct.
- (R=6000) and finite-(J) compression are not replaced by a diagnostic small core in the claimed source bounds.
- Absolute estimates cover only their named product sectors. Same-sign conclusions are not transferred to mixed-sign sectors.
- No infinite sum/limit interchange is used to claim the unpaid full tail is negligible.
- The Decision M exponent typo is the only concrete incorrect displayed formula identified in B–O. It does not reverse M’s stated o(1) sector conclusion under the given stricter epsilon range.

## Consumer compatibility and dependency map

### Direct first-strike consumer

The relevant chain is

\[
\text{prime-source matrix and fixed-}R\text{ filtered moments}
\longrightarrow \text{same-section cubic/endpoint transfer}
\longrightarrow \text{signed fifth/sixth gate (12)}
\longrightarrow \text{prime-to-Weil identification}
\longrightarrow \text{zero-side block/tail transfer}.
\]

Decision D establishes same-window endpoint admissibility and crossing-energy averaging for the direct first-strike consumer. Its good-endpoint product set uses the same endpoint-pair weights as Decision B's adaptive averaging, so restricting the nonnegative energy average to that set costs at most a factor four. Consequently D and the adaptive B theorem select a common direct-consumer section on which endpoint gates hold and the complete normalized finite-section boundary correction is o(1). This does not establish Decision E's full-to-trimmed raw-cubic trace transfer/UI condition, the signed fifth/sixth gate, the prime-to-Weil identification, or the zero-side transfer. For arbitrary sections the complete boundary correction is not shown uniformly o(1); for the existential adaptive section it is proved o(1). These boundary statements concern the difference between the full compression trace and the compressed-cube trace. They do not identify that trace with the original raw cubic on the selected section. Decisions I–M remove named arithmetic subpopulations only. Decision O leaves a critical high-product mixed-sign correlation. Thus gate (12) remains open. The exact first-strike note gives the signed target and frozen coefficients; its condition includes all non-exact products and aliases, not just model closures.

### Source-masked determinant consumer

This is a separate route. The exact callback interface includes `source_mask(fid,slots,lag,T,section,alias)`. Current executable evidence does not authenticate the row-membership rule and its exact mapping to the original endpoint-score features, roots, and normalization. Therefore its source-to-consumer bridge is **UNDEFINED** on the audited evidence. Decision D’s endpoint-density theorem cannot be transferred to it.

### Status table

| Bridge/claim | Status | Reason |
|---|---|---|
| Finite block identities and exact finite path/algebra formulas | **PROVED** | Exact matrix/Fourier identities; stated finite scope. |
| Scalar part of finite-section cubic boundary payment, arbitrary section | **PROVED** | Natural-cutoff majorant is (o(1)). |
| Complete normalized finite-section boundary correction, arbitrary section uniformly | **OPEN** | Existing absolute remainder estimate does not decay uniformly over sections. |
| Complete normalized finite-section boundary correction, existential adaptive trim | **PROVED** | Local large-sieve endpoint averaging gives (E(I)=O(log d)), hence the block remainder is (o(1)) on that selected section under source hypotheses. |
| Full-to-trimmed raw cubic trace transfer | **OPEN** | Adaptive boundary control does not imply deletion stability for the unbounded cubic; needs source UI/deleted-block cubic or direct estimate. |
| Direct endpoint admissibility with averaged crossing energy | **PROVED** | Density (≥1/4) on the specified equally weighted window; inherited (O_R(1)) constants. |
| Named zero-carrier, low-product, same-sign, and small-singleton sectors | **PROVED** | Only exact sectors and ranges stated in I–M. |
| Full cubic endpoint discrepancy | **CONDITIONAL / OPEN** | High-product signed sectors remain. |
| Signed fifth/sixth gate (12), including (m_3) and fixed-(R) arithmetic | **OPEN** | No positive signed saving at required scale proved. |
| (m_3=2) for the actual same-section source | **OPEN** | Model value is not an actual-source theorem. |
| Conditioned Cayley energy (<0.105) for actual source | **OPEN** | No source-valid spectral separator/energy theorem established here. |
| Source-masked determinant compatibility | **UNDEFINED** | Authentic selector/feature-to-atom map absent. |
| Prime-to-Weil identification | **OPEN** | Inherited transfer not independently proved in this audit. |
| Zero-side consumer and tail-Weyl transfer | **OPEN** | No complete source proof audited/closed here. |
| Strict (>79\%\) simple-zero conclusion | **OPEN** | Multiple independent gates remain unpaid. |

## Critical residual and exact exponent ledger

For the Decision O representative block, the complete (o(1)) target is not met by any audited bound:

| Method/part | Certified normalized size | Result |
|---|---:|---|
| Divisor/absolute baseline, ε=1/100 | (O(X^{29/250})) | Grows; no saving. |
| Fixed-((B,n_1)) thin interval | At most one integer (n_2) | No occupancy/sign estimate. |
| Exact interval DFT | (O(LX^{7/5}e^{-\sqrt L/2})) | Worse by (321/250-o(1)) powers. |
| Cauchy dispersion | (O(X^{3/10-o(1)})) | Worse than baseline. |
| (B=2^v) singleton subfamily | (O(X^{-17/50})) | This subfamily alone is (o(1)). |

The exact missing theorem can be stated as follows: **prove a source-matched signed estimate for the (B\ne B') off-diagonal in the square of the Decision O block, retaining its actual prime-power coefficients, near-product window, finite-(J) weights, root sums and endpoint, strong enough to make the full normalized block (o(1)).** The existing norm/divisor estimates do not supply it. Its failure under the tested methods is a method obstruction only, not a mathematical counterexample.

The independent strict first-strike ledger still records a required arithmetic gain greater than

\[
{317503\over66000000}=0.00481065151515\ldots
\]

under the frozen initial upper payment, with further paid costs increasing the required gain. The separate model/robust margin (52897896569489/572357731837500000\approx9.24210395475\times10^{-5}) is not interchangeable with the Decision O block exponent, nor is either an earned zeta-side saving. The conditioned energy target (0.105) and model moments do not discharge (12).

## Falsified statements versus unresolved theorems

1. **One formula falsified:** Decision M’s displayed normalized near exponent omitted (X^\epsilon); corrected above. The stricter epsilon condition still gives the same qualitative sector result.
2. **One proposed algebraic cancellation falsified:** Decision F’s rational Hermitian three-index example has nonzero cubic trace. This defeats the claim that cyclicity/zero diagonal alone annihilates the cubic term.
3. **Abstract hostile witnesses:** endpoint anticorrelation, shrinking-density, and diagonal-spike arrays falsify inferences from their abstract hypotheses only. They are not examples from the prime source.
4. **No arithmetic target counterexample:** neither the failure of the O completion/Cauchy exponents nor the open residual proves that the desired signed inequality is false.

## Strongest referee-ready standalone statements

These are candidates for an external mathematical referee, not novelty claims:

1. **Finite-section block identity and adaptive boundary theorem.** The block identity/scalar correction are exact; the adaptive large-sieve argument proves complete normalized boundary correction (o(1)) on an existential trimmed section. The same bound is not uniform over arbitrary sections, and it does not transfer the full raw cubic trace to the trim.
2. **Endpoint-pair selection lemma.** A nonnegative energy with mean bound (C_B\log d), combined with two endpoint-good sets each of density at least (1/2), has an endpoint-admissible pair with energy at most (4C_B\log d), for the specified identical finite weights. This is a standard averaging argument with a source-specific endpoint application.
3. **Exact zero-carrier prime-power classification.** UFD closure and the factor-48 count are proved for the named carrier-zero sector; no conclusion for near/nonzero carriers is included.
4. **Source-sector product reductions.** K–M provide named low-product, same-sign first-alias, and small-singleton bounds with full path/power handling in their stated ranges. The Decision M exponent correction must accompany any reuse.
5. **Critical-block feasibility ledger.** O’s finite interval/DFT/Cauchy calculations are reproducible computational certificates explaining why those specific estimates fail. This is a method audit, not an arithmetic theorem.

No global literature/priority audit was performed in this run. The matrix algebra, Markov selection, Hilbert/Montgomery–Vaughan mean-value method, divisor estimates, and Fourier orthogonality are established tools. Repository presence does not establish historical novelty. Any publication claim needs a separate literature review and self-contained proofs of each asymptotic hypothesis.

## Research recommendation

Keep the theorem claim frozen. The next justified target is the one explicit signed high-product off-diagonal estimate stated above, together with a source-authentic coefficient/weight theorem that can actually be applied to it. Do not reopen broad rank, model optimization, or generic Cauchy iterations. Independently, do not use the direct endpoint theorem to populate the masked determinant callback until the source selector is authenticated. The remaining prime-to-Weil and zero-side obligations must be solved after the arithmetic gate, not inferred from its model analogue.

## Reproduction, integrity, and provenance

### Verified repository state

- Worktree root: `C:/Users/Asus/.codex/worktrees/0498/riemann-bandwidth1-frontier-audit`
- Branch: `codex/c5-c6-attack-20261006`
- HEAD: `8d1163d3396291ccfcdc4f8ff5a4e21d6bf616a2`
- Tracked working-tree changes: none at audit start.
- Untracked `notebooklm_packet/`: present before this report; preserved and not read for report content or modified.
- Linked Git index: `C:/Users/Asus/Downloads/riemann-bandwidth1-frontier-audit/.git/worktrees/riemann-bandwidth1-frontier-audit/index`, outside this worktree’s writable root. No index write was attempted; this report is left uncommitted.

Decision O’s four tracked files match their recorded artifact hashes at the audited HEAD:

| Path | SHA-256 |
|---|---|
| `notes/WP84_DECISION_O_CRITICAL_SIGNED_DISPERSION_FEASIBILITY.md` | `963A999FC3173CD8F00D79D5F3747B2E1C6E8320D6051106D20260E936C0935D` |
| `certificates/WP84_DECISION_O_CRITICAL_SIGNED_DISPERSION_CERTIFICATE.json` | `64E7D247E5FF1E5D0C9839DBEBF21C8553D1298662E75D6073C65FEE2D13F049` |
| `src/wp84_decision_o_critical_signed_dispersion.py` | `1AB39619F888CC3F2DA93EA1C6FBC3BAF33533932456629FFD65399F64952342` |
| `src/wp84_decision_o_critical_signed_dispersion_replay.py` | `B7555FAB814E36C68C04F5234C6919EA5243B73B5A477D9511DBBA588D24A0EB` |

### Independent replay commands

Run from repository root:

```powershell
python src/wp84_finite_section_boundary_cubic_replay.py
python src/wp84_decision_c_same_section_compatibility_replay.py
python src/wp84_decision_d_endpoint_admissibility_replay.py
python src/wp84_decision_e_prime_source_cubic_deletion_replay.py
python src/wp84_decision_f_exact_signed_deleted_block_cubic_replay.py
python src/wp84_decision_g_one_sided_cubic_localization_replay.py
python src/wp84_decision_h_global_cubic_score_discrepancy_replay.py
python src/wp84_decision_i_cubic_prime_resonance_replay.py
python src/wp84_decision_j_full_frequency_cubic_paths_replay.py
python src/wp84_decision_k_central_low_product_replay.py
python src/wp84_decision_l_square_root_product_first_alias_replay.py
python src/wp84_decision_m_mixed_first_alias_small_singleton_replay.py
python src/wp84_decision_n_coherent_alias_modular_correlation_replay.py
python src/wp84_decision_o_critical_signed_dispersion_replay.py
python src/wp84_cubic_first_alias_typeii_replay.py
```

All 15 commands exited 0 in this audit. The displayed output explicitly marks finite diagnostics as such and leaves the corresponding asymptotic prime-source claims open. JSON parsing succeeded for the 13 C–O decision certificates and the connected-kernel manifests.

### Manifest qualifications

- `WP84_FIXED_SCALE_CONNECTED_KERNEL_MANIFEST.json` references two source Git blobs that match.
- `WP84_CONNECTED_DETUNING_MANIFEST.json` points to a historical blob for `notes/WP84_CROSS_SCALE_BROWNIAN_REFERENCE.md`; the current file differs because it was subsequently revised. This is a stale historical manifest, not a current-file integrity certificate.
- `.cache/publication_safety/TRACKED_VERIFICATION_MANIFEST.json` is pinned to historical HEAD `f962f23e8b427e787593725003ba144475de249b`. Its one known mismatch is `notes/WP84_GOOD_ENDPOINT_DETERMINANT_COMPATIBILITY_CERTIFICATE.json`, later changed in the audit history; it is not a manifest for the present HEAD.
- The existing `notebooklm_packet/MANIFEST.txt` was left untouched. Its local historical Git objects can be checked for the entries that name them, but the pinned external public-repository source files are not present as local Git objects, so their bytes cannot be independently revalidated from this repository alone. No packet file is claimed verified by this audit.
- Old publication/snapshot manifests are provenance artifacts for their pinned historical states; they should not be presented as fresh hashes for the current tree.

### Reproduction limits and external assumptions

The analytic D endpoint argument depends on the endpoint feature polynomial definition, its source coefficient square-mass bound, and the stated uniform short-interval mean-value/sampling estimates in the cited source notes. The replays check the density/weight arithmetic and hostile substitutions, not those asymptotic analytic hypotheses from first principles. Likewise, I–N use their written source coefficient and divisor bounds; O’s replay verifies exact exponent arithmetic and finite Fourier identities, not the missing signed correlation. A reader seeking a theorem proof should inspect each linked decision note and its cited definitions rather than treating this summary or a passing script as an asymptotic proof.

**Final theorem status: strict (>79\%\) remains OPEN.**
