# WP84 — endpoint-restricted ordinary-prime theorem attack

Base commit: `13752ebd5cc399bf5cd04b74b679a0f59ab8eb41`; audit branch: `codex/wp84-endpoint-restricted-ordinary-attack-20261103`.

## Decisions

| Gate | Decision |
|---|---|
| `GOOD_SECTION_SET` | **INCOMPLETE** |
| `RESTRICTED_THEOREM` | **OPEN** |
| `SOURCE_CONDITIONING_ADVANTAGE` | **NONE_FOUND** |
| `R400_RECORD_BUDGET` | **OPEN** |
| `NEXT_ACTION` | **FREEZE_R400_ROUTE** |

The direct bounded-consumer endpoint/boundary section set is source-defined and has positive density. The full set needed by the fourth-order detuning endpoint reduction is not reconstructible from checked-in source: its pair-frequency feature generator and consumer-to-score map remain missing. Restricting the ordinary connected sum to the known set is a logically weaker target, but no source-specific correlation estimate makes that restriction analytically easier. The route is frozen at that gap; prior exact finite results remain preserved.

## 1. Exact section set that is established

Use the Decision-B quantities
\[
X=T/(2\pi)=e^L,\quad N=\lfloor Xe^{-\sqrt L}\rfloor,\quad
d=\lfloor TL/(2\pi)\rfloor,\quad
M=\lceil d e^{-\sqrt L/2}\rceil,
\]
and the uniform candidate space \(\mathcal W_T=\{0,\ldots,M\}^2\), with
\[
I_{u,v}=[b+u,b+d-1-v],\qquad m_{u,v}=d-u-v.
\]
Each candidate is a contiguous principal section and deletes \(r=u+v\le2M=o(d)\) rows. In particular \(m\ge d-2M\sim d\).

The source-authentic one-prime endpoint score used by the direct bounded first-strike construction is
\[
S_R(k)=\sum_{t=-12R}^{12R}(|\alpha_{k+t}|^2+|\beta_{k+t}|^2),
\]
where \(\alpha_k,\beta_k\) are the actual prime-power fields with \(p^a\le N\) and carrier \(e^{i(T+2\pi k/L)\log(p^a)}\). Its lower and upper endpoint sets are
\[
G_- =\{u:S_R(b+u)\le2F_R\},\qquad
G_+ =\{v:S_R(b+d-1-v)\le2F_R\},
\]
where the source proof gives the uniform edge-window means \(\le F_R=O_R(1)\). Markov gives \(|G_-|/(M+1)\ge1/2\) and \(|G_+|/(M+1)\ge1/2\). The actual crossing energy is
\[
E(I)=\|P_I V(1-P_I)\|_{HS}^2\ge0,
\qquad \mathbb E_{\mathcal W_T}E(I)\le C_B\log d.
\]
For fixed \(0<\epsilon<1/4\), the exact known direct-consumer set is therefore
\[
\mathcal G_T^{(1)}(\epsilon)=
\{(u,v)\in G_-\times G_+:
E(I_{u,v})\le C_B\log(d)/\epsilon\}.
\]
Its membership indicator is the product of the two displayed endpoint-score indicators and the crossing-energy indicator. Its uniform density satisfies
\[
\gamma_T^{(1)}=|\mathcal G_T^{(1)}|/(M+1)^2\ge1/4-\epsilon.
\]
This follows by restricting the same uniform nonnegative energy average; no independence assumption is used. All constants \(F_R,C_B\) are implicit source constants, and \(R\) is fixed.

For every member of this set, the already checked one-prime local row bound gives the direct fifth/sixth finite-path reprojection payment \(4bRK_R^b/m=o(1)\), \(b=5,6\), and the selected boundary-energy bound gives the normalized compression-versus-compressed-cube correction \(o(1)\). Bounded-consumer rank deletion costs \(O(r/d)=O(e^{-\sqrt L/2})=o(1)\) when performed before the quartic step. The R=400 pair certificate is stable uniformly on these candidate sections: \(\mathrm{Pair}_{400}(I)=\mathrm{Pair}_{400}+o(1)<0.266329+o(1)\).

This is not yet an exact full R400 endpoint set. The fourth-order detuning endpoint argument uses pair-frequency features supported at \(pq\), and its complete fixed-\(R\) coefficient/gate generator is absent. The latest F1/F1B audit specifically says the one-prime score \(S_R\) is not identified with those product-frequency features, and that the claimed product-score mean does not follow by substituting the one-prime cutoff. F1B gives a conditional growing-score payment only if an exact feature generator, its \(N^2\) support, fixed-coefficient threshold structure, and the consumer's gate are verified. No such source identity is present. Thus \(\mathcal G_T^{(1)}\) is exact for its stated direct consumer, while the full \(\mathcal G_T^{R400}\) requested for every connected endpoint obligation remains **incomplete**.

There is no definitional circularity in \(\mathcal G_T^{(1)}\): its score and energy predicates do not use \(C^{ord}_{T,I}\). The unresolved issue is correlation, not circular definition. Defining a set by \(C^{ord}_{T,I}\le\Delta\) would be tautological and is not used.

## 2. Exact implication of the restricted positive-part condition

For any finite nonempty section set \(\mathcal G_T\), if
\[
\limsup_{T\to\infty}\mathbb E_{I\in\mathcal G_T}
 (\Re C^{ord}_{T,I})_+ < \Delta_{max},\qquad
\Delta_{max}=\frac{3675673694911}{148250000000000},
\]
then some fixed \(\eta>0\) makes the conditional mean at most \(\Delta_{max}-\eta\) for all sufficiently large \(T\). A finite average is at least its minimum, so for each such \(T\) there is \(I_T\in\mathcal G_T\) with
\[
(\Re C^{ord}_{T,I_T})_+<\Delta_{max},
\quad\text{hence}\quad \Re C^{ord}_{T,I_T}<\Delta_{max}.
\]
This implication is exact and does not replace a mean positive part by a positive part of a mean. If \(\mathcal G_T\) is the *complete* consumer-admissible set, it supplies the connected budget on a common admissible section. In particular, the record arithmetic would then use \(\mathrm{Pair}_{400}(I_T)<0.266329+o(1)\), plus the controlled proper-power and other already closed \(o(1)\) terms.

For the known set \(\mathcal G_T^{(1)}\), the implication only selects a section satisfying the direct one-prime endpoint, boundary, principal-section, and bounded row-deletion requirements. Because the fourth-order product-feature consumer interface is not supplied, this is not a proof that \(\mathcal G_T^{(1)}=\mathcal G_T^{R400}\). The strict budget therefore remains open. The exact extra hypothesis is the missing source-defined fourth-order endpoint-score/feature map (or a proof that no additional score gate is required and that the rank-two payment alone closes).

Other conditions have mixed status. The pair-section stability, bounded-consumer order of operations, direct one-prime endpoint selection, crossing-energy boundary estimate, and proper-power absorption are proved in their recorded scopes. The physical ordinary-prime connected estimate is open. The F1C audit also keeps the signed fifth/sixth arithmetic gate, raw cubic deletion/uniform integrability, same-convention lower-moment and prime-to-Weil identification, zero-side block/tail transfer, and the conditioned energy gate open. These independent obligations prevent promotion of the percentage consumer even if the restricted connected inequality were later proved.

## 3. Exact restricted average with all physical source terms

For \(\epsilon\in\{++--,+-+-,+--+,-++-,-+-+,--++\}\), ordinary primes \(p_j\le N\), and
\[
A=\prod_{\epsilon_j=+1}p_j,\quad B=\prod_{\epsilon_j=-1}p_j,
\quad Y=\log(A/B),\quad v_j=\epsilon_j\log(p_j)/L,
\quad c_p=-\frac{\log p}{a_\phi(T)L\sqrt p},
\]
the pair-subtracted physical source has the exact form
\[
C^{ord}_{T,I}=\Re\sum_{\substack{\epsilon\ \mathrm{balanced},\ p_0,\ldots,p_3\le N\\A\ne B}}
e^{iTY}\Bigl(\prod_{j=0}^3c_{p_j}\Bigr)
\left[\Omega_{4,400}(v)\kappa_{m,I}(v)
+\mathcal R^{root}_{T,I}(\epsilon,\mathbf p)\right].
\]
The inner source multiplier retains the exact filtered R400 overlap, the selected-section carrier exactly once, and every finite root/path term with its source normalization and valid-root interval. The physical row cumulant remains
\[
\kappa_{m,I}(v)=\sum_{\pi\in\Pi^{ord}_{4,anch}}
(-1)^{|\pi|-1}\prod_{D\in\pi}
\left(\frac1m\sum_{k\in I}e^{2\pi i k v_D/L}\right),
\]
with all 26 ordered terms, multiplicities \(1,7,12,6\), and 75 block factors. Exact \(A=B\) ordinary-prime pair contractions are removed by unique factorization; every \(A\ne B\) tuple, all six orientations, unequal product scales, aliases, and root corrections remain.

The endpoint-restricted average is exactly
\[
\frac1{|\mathcal G_T|}\sum_{(u,v)\in\mathcal W_T}
\mathbf1_{\mathcal G_T}(u,v)
\left(\Re\sum_{\substack{\epsilon\ \mathrm{balanced},\ p_j\le N\\ A\ne B}}
e^{iTY}\Bigl(\prod_jc_{p_j}\Bigr)
\left[\Omega_{4,400}(v)\kappa_{m_{uv},I_{uv}}(v)
+\mathcal R^{root}_{T,I_{uv}}\right]\right)_+.
\]
No endpoint indicator is moved through the positive part.

For the *signed* average before taking positive part, tensorization remains exact. For a partition \(\pi\) with \(q=|\pi|\), define
\[
W^{\mathcal G}_{\pi}(\mathbf k)=\frac1{|\mathcal G_T|}
\sum_{(u,v)\in\mathcal G_T}m_{uv}^{-q}
\prod_{D\in\pi}\mathbf1_{k_D\in I_{uv}}.
\]
Then \(W^{\mathcal G}_{\pi}\ge0\), \(\sum_{\mathbf k}W^{\mathcal G}_{\pi}=1\), and
\[
\mathbb E_{I\in\mathcal G_T}\kappa_{m,I}(v)=
\sum_{\pi}(-1)^{|\pi|-1}\sum_{\mathbf k}
W^{\mathcal G}_{\pi}(\mathbf k)
e^{2\pi i\sum_{D\in\pi}k_Dv_D/L}.
\]
The physical \(\Omega\), section start convention, source coefficients, and each path/root correction remain inside their respective source sums. This is a finite exact rearrangement; the signed Möbius sum and complex source weights carry no new sign or norm bound.

## 4. Scale/detuning ledger and exact budget allocation

Group the retained nonexact tuples by ordered dyadic product scales \((M_+,M_-)\), with \(A\asymp M_+\), \(B\asymp M_-\), and by the exact detuning
\[
z=T|\log(A/B)|.
\]
For comparable products \(A=n\), \(B=n+h\), this is exactly \(T|\log(1+h/n)|\), and for \(|h|=o(n)\) it is asymptotic to \(T|h|/n=|h|/(n/T)\). The near-product band \(z\le1\) therefore includes \(|h|\lesssim n/T\); the source cutoff has \(N^2/T\to\infty\), so this band is not eliminated by \(N/T\to0\). The exact zero \(z=0\) is the removed pair layer. No source-certified sign decides the positive part in any \(z>0\) band. In particular, the public scalar safe-lobe sign is not a physical cumulant sign theorem.

Across the candidate endpoint window, the scalar carrier changes phase by scale
\[
2\pi M|Y|/L\asymp T|Y|e^{-\sqrt L/2}=z e^{-\sqrt L/2}.
\]
This gives the exact scale at which endpoint motion could begin to oscillate the carrier. If it is small, the carrier itself has little endpoint variation. If it is large, cancellation still needs regularity or correlation of the selected endpoint weights. The threshold indicator and crossing-energy condition give neither. They can select irregular subsets, and the row cumulant/root term also changes with \(m_{uv}\).

For any disjoint dyadic-scale/detuning partition \(C^{ord}=\sum_j C_j\), the exact sufficient positive-part budget is
\[
\sum_j\limsup_{T\to\infty}\mathbb E_{I\in\mathcal G_T}(\Re C_{j,T,I})_+<\Delta_{max}.
\]
Equivalently one may assign source-uniform budgets \(\Delta_j\ge0\) with \(\sum_j\Delta_j<\Delta_{max}\) and prove each regime bound. This follows from \((\sum_j x_j)_+\le\sum_j(x_j)_+\); it is only sufficient and may overpay cancellations. No numerical exponent or nonzero-detuning regime saving is inferred. The smallest outstanding inequality is the full, unsplit conditional mean above, with the exact \(\Delta_{max}\) and the complete physical weights.

The checked source does not determine which individual \((A,B)\) or detuning regimes contribute positively after all 26 terms and orientations are summed. In general \((\sum_j C_j)_+\) is not \(\sum_j(C_j)_+\), so assigning positive-part mass to a particular near-product band requires a new decomposition inequality. The only exact budget statement presently justified is the total conditional inequality; any regime-wise \(\Delta_j\) allocation is an optional stronger sufficient route, not a source-derived necessary allocation.

## 5. Falsification and route decision

Endpoint density and boundary energy alone cannot force a smaller connected contribution. An exact rational *abstract* control illustrates the issue without purporting to be a prime-source configuration. Take a \(4\times4\) endpoint grid; make three of four lower endpoints and three of four upper endpoints score-good, so \(\gamma=9/16\). Give the single bad endpoint at each edge score \(3B\), good endpoints score zero, and use threshold \(2B\); each edge mean is \(3B/4\le B\). Set \(E=0\) everywhere. Then assign \(C=2\Delta_{max}\) on all 9 admissible pairs and \(C=-18\Delta_{max}/7\) elsewhere. Exactly,
\[
\mathbb E_{\mathcal W}C=0,\quad
\mathbb E_{\mathcal W}C_+=9\Delta_{max}/8,\quad
\mathbb E_{\mathcal G}C_+=2\Delta_{max}>\Delta_{max}.
\]
Thus the endpoint Markov and boundary-energy hypotheses do not imply the restricted theorem, even when the signed mean vanishes. This is an abstract negative control only. The audited evidence contains no source-compatible ordinary-prime counterexample and no evidence that the actual source concentrates this way.

Conditioning is formally useful because it ignores positive excess outside \(\mathcal G_T\), but its indicator is built from the same prime-power field and its energy and does not yield a positive-definite or translation-invariant product weight. The exact conditional tensor weights are normalized but do not control the 26-term signed sum or its positive part. No source-specific cancellation, arithmetic saving, or reduction in near-product kernel norm is established. The restricted estimate is therefore still the missing source-weighted aggregate problem on a smaller, data-selected family. Since no measurable analytic reduction was obtained and the full R400 admissible set is incomplete, **freeze this R400 route**.

The conditional 68.820273% route, 79.62709668% benchmark, and RH remain separate and open/conditional. The preceding ordinary-prime feasibility audit, proper-power absorption, physical positive atom, physical/geometric discrepancy, endpoint/tensor identities, and all earlier counterexamples are unchanged.

## Verification

The source inventory is `evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_SOURCE_HASHES.json`; the artifact manifest and sidecar are `evidence/WP84_R400_ENDPOINT_RESTRICTED_ATTACK_SHA256_MANIFEST.json` and `.sha256`. The exact rational checker and its five tests are `src/wp84_r400_endpoint_restricted_attack.py` and `tests/test_wp84_r400_endpoint_restricted_attack.py`. Runs use only the exact selection arithmetic and one abstract negative control; they are not source-prime experiments and do not certify the unresolved asymptotic inequality.

The inventory hashes 15 relevant predecessor source/evidence files against raw blobs at the stated base and confirms each working copy is unchanged after CRLF/LF normalization. It also pins the immediately preceding theorem-feasibility manifest, whose sidecar and all 10 listed artifacts replay successfully. The new manifest covers the report, checker, tests, test logs, arithmetic summary, and source inventory; its sidecar is the exact SHA-256 of the manifest bytes.
