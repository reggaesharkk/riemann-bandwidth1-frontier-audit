# WP84 F1C — source-authentic first-strike endpoint audit

Date: 2026-10-10  
Repository branch: `codex/c5-c6-attack-20261006`  
Verified starting HEAD: `179f9959c4dabb675d1955646f212ddf6d3c51f5`  
Primary verdict: **F1C-A — the fifth/sixth first-strike one-prime endpoint theorem is independently established, and its endpoints can be selected jointly with Decision B boundary energy on the same adaptive window.**

This result does not validate the different fourth-order product-feature score in Decision D, and it does not close the signed arithmetic gate or strict $>79\%$ theorem. No source masks, pair-feature callbacks, or historical endpoint selectors are supplied or assumed.

## 1. The first-strike endpoint object

The actual source field used by the fifth/sixth finite-band reprojection is

$$
X=T/(2\pi),\quad L=\log X,\quad
N=\lfloor Xe^{-\sqrt L}\rfloor,\quad h=2\pi/L,
$$
$$
c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n},\quad
Q(t)=\sum_{p^v\le N}c_{p^v}e^{it\log(p^v)},
$$
with every prime power retained, and
$$
\alpha_k=\Im Q(T+hk),\qquad
\beta_k=2\Re\sum_{p^v\le N}c_{p^v}\left(1-\frac{\log(p^v)}L\right)e^{i(T+hk)\log(p^v)}.
\tag{1}
$$
The source normalization assumed in the notes is $a_\phi(T)\to1$ (in particular it is bounded away from zero). The exponentials in (1) are exactly $e^{iT\log n}e^{2\pi ik\log n/L}$; these are the actual carrier and sampled Fourier phases.

For fixed band radius $R$ the hard-band matrix has diagonal $\beta_i$ and, for $0<|i-j|\le R$, off-diagonal entry
$$
\frac{\alpha_i-\alpha_j}{\pi(j-i)}.
\tag{2}
$$
The endpoint statistic in `WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md` is
$$
S_R(k)=\sum_{t=-12R}^{12R}(|\alpha_{k+t}|^2+|\beta_{k+t}|^2).
\tag{3}
$$
It is a local, endpoint-dependent nonnegative score. It is not a supremum over all endpoints, not an average asserted to hold pointwise, and not a product-frequency polynomial. A score-good endpoint is one for which (3) is bounded. That local bound controls every row sum of the finite band matrix needed by paths of length at most six.

## 2. Independent proof of the one-prime endpoint mean

Put $M=\lceil d e^{-\sqrt L/2}\rceil$, with $d=\lfloor XL\rfloor$, and let $q=M+1$ be the number of candidates at each edge of the Decision B pair window. Its physical width is
$$
U_T=hM\sim 2\pi X e^{-\sqrt L/2}=T e^{-\sqrt L/2}.
\tag{4}
$$
The coefficient square mass is
$$
\sum_{p^v\le N}|c_{p^v}|^2
=\frac1{|a_\phi(T)|^2L^2}\sum_{p^v\le N}\frac{(\log p)^2}{p^v}=O(1).
\tag{5}
$$
For $v=1$, Chebyshev's bound gives $\sum_{p\le N}(\log p)^2/p=O((\log N)^2)=O(L^2)$. For $v\ge2$, $\sum_p(\log p)^2\sum_{v\ge2}p^{-v}<\infty$, so the normalized proper-power square mass is $O(L^{-2})$. This is a full prime-power estimate; it does not replace the pool by ordinary primes.

The frequencies $\xi_n=\log n/L$, for the distinct integers $n=p^v\le N$, have no duplicates. If $m<n\le N$, then
$$
\xi_n-\xi_m\ge\frac1{(N+1)L}.
$$
The circular wrap gap is at least $1/\sqrt L$ since $\log N\le L-\sqrt L$; for sufficiently large $T$ the minimum circular spacing is therefore
$$
\delta_T\ge\frac1{(N+1)L}.
\tag{6}
$$
The discrete large-sieve inequality on any translate of $q$ consecutive indices gives
$$
\sum_{k=b}^{b+q-1}|Q(T+hk)|^2
\le (q-1+\delta_T^{-1})\sum_{p^v\le N}|c_{p^v}|^2.
\tag{7}
$$
Since
$$
\frac{M}{NL}\sim e^{\sqrt L/2}\to\infty,
\qquad \frac{N}{U_T}\sim\frac{e^{-\sqrt L/2}}{2\pi}\to0,
\tag{8}
$$
(7), divided by $q$, is uniformly $O(1)$ on every candidate window. The same proof applies to
$$
Q_1(t)=\sum_{p^v\le N}c_{p^v}\left(1-\frac{\log(p^v)}L\right)e^{it\log(p^v)},
$$
because its coefficient square mass is no larger than (5). As $|\Im Q|^2\le|Q|^2$ and $|2\Re Q_1|^2\le4|Q_1|^2$, the mean of $|\alpha_k|^2+|\beta_k|^2$ on any translated candidate window is bounded by a constant independent of $T$ and of the window location.

For each fixed shift $t\in[-12R,12R]$, the same estimate holds on the translated window $k+t$. Summing its finitely many shifts gives
$$
\frac1{M+1}\sum_{u=0}^{M}S_R(b+u)\le F_R,
\qquad
\frac1{M+1}\sum_{v=0}^{M}S_R(b+d-1-v)\le F_R,
\tag{9}
$$
where $F_R=O_R(1)$, uniformly in $b$ and $T$. This directly re-applies the source-local estimate on Decision B's smaller window; it does not infer a local bound there from the earlier wider $d/\sqrt L$ window.

Define lower and upper good endpoint sets by $S_R\le2F_R$. Markov applied separately to (9) gives
$$
\frac{|G_-|}{M+1}\ge\frac12,\qquad
\frac{|G_+|}{M+1}\ge\frac12.
\tag{10}
$$
The actual first-strike conditions are separate lower- and upper-endpoint neighborhood conditions, so their pair set is $G_-\times G_+$ and has exactly the Decision B uniform pair density at least $1/4$. No independence assertion is used.

## 3. What $K_R$ controls and the reprojection payment

At an endpoint with $S_R(k)\le2F_R$, every field value in its $12R$ neighborhood has absolute value at most $\sqrt{2F_R}$. For a row of (2), the diagonal contribution is at most $\sqrt{2F_R}$ and the off-diagonal absolute row sum is bounded by
$$
\sum_{r=1}^{R}\left(\frac{2\sqrt{2F_R}}{\pi r}+\frac{2\sqrt{2F_R}}{\pi r}\right)
=\frac{4\sqrt{2F_R}}\pi H_R,
\quad H_R=\sum_{r=1}^{R}\frac1r.
$$
Thus the local Hermitian block norm is at most
$$
K_R=\sqrt{2F_R}\left(1+\frac{4H_R}{\pi}\right)=O_R(1).
\tag{11}
$$
This is an endpoint-selected local row/operator bound, not a global operator-norm claim. All constants may depend on the fixed $R$; the sixth-degree path needs no more than the $12R$ neighborhoods recorded in the source proof.

For $I=[k_-,k_+]$, $d'=|I|$, the exact weighted reprojection difference is
$$
E_{b,R}(I)=d'^{-1}\operatorname{tr}\big((P_IA_RP_I)^b-P_IA_R^bP_I\big),\qquad b=5,6.
$$
Only roots within $bR$ of an endpoint can have a path leave and return. There are at most $2bR$ such roots; each of the two diagonal path sums is bounded by $K_R^b$. Hence
$$
|E_{b,R}(I)|\le \rho_b:=\frac{4bRK_R^b}{d'},\qquad b=5,6.
\tag{12}
$$
On Decision B's adaptive pair window, $d'=d-u-v\ge d-2M\sim XL$. With (11), both fixed-$R$ reprojection payments in (12) are $O_R((XL)^{-1})=o(1)$. The score does not grow with $T$; no pair-frequency F1B estimate is used.

## 4. Common section with adaptive boundary energy

For exactly the same pairs
$$
I_{u,v}=[b+u,b+d-1-v],\quad 0\le u,v\le M,
$$
Decision B proves the uniform-weight average $\mathbb E_{u,v}E(I_{u,v})\le C_B\log d$, where $E(I)=\|P_IV(1-P_I)\|_{HS}^2\ge0$. Restrict this average to the Cartesian set $G_-\times G_+$ from (10). Since that set has pair density $\gamma_T\ge1/4$ and $E\ge0$,
$$
\mathbb E_{(u,v)\in G_-\times G_+}E(I_{u,v})
\le\frac{C_B\log d}{\gamma_T}\le4C_B\log d.
\tag{13}
$$
There is therefore a pair in the endpoint-good Cartesian set with $E(I_{u,v})\le4C_B\log d$. The pair weights in (13) are the same equal finite weights used by Decision B. No endpoint/energy decorrelation is assumed.

For completeness, the finite-section cubic boundary identity separates $H=s_0I+V$ as
$$
\Delta_I=\operatorname{Tr}(PH^3P)-\operatorname{Tr}((PHP)^3)
=3s_0(T)E(I)+R_I,
\qquad |R_I|\le3\|V\|_{op}E(I),\quad \|V\|_{op}\le4S_1,
$$
where $S_1=\sum_{p^v\le N}|c_{p^v}|=O(\sqrt N/L)$ includes all prime powers. Therefore the selected pair satisfies
$$
\frac{|\Delta_I|}{d'}
\ll\frac{\log d}{d'}+\frac{S_1\log d}{d'}
=O(1/T)+O\!\left(\frac{\sqrt N}{TL}\right)
=O(1/T)+O\!\left(\frac{e^{-\sqrt L/2}}{\sqrt{2\pi T}\,L}\right)=o(1).
\tag{14}
$$
The first term in (14) is the scalar-background payment; the second is the signed $V$-boundary majorant. This is the complete compression-versus-compressed-cube boundary correction on the selected section. It is **not** a theorem that the raw cubic trace on the original length-$d$ section differs by $o(1)$ from the raw cubic on the trimmed section. That deletion/UI problem remains separate.

The same selected section simultaneously has (i) all first-strike endpoint neighborhoods bounded by (11), (ii) adaptive crossing energy $O(\log d)$, (iii) the normalized boundary correction (14), and (iv) both repeated finite-band reprojection bounds (12). The common section exists for every $T$ under the inherited source normalization and Decision B hypotheses.

## 5. Dependency test: fourth order versus fifth/sixth

The source dependency is

```text
one-prime prime-power field (1)
  -> local endpoint statistic S_R and selected K_R (9)--(11)
  -> fifth/sixth A_b -> B_b reprojection payment rho_5,rho_6 (12)
  -> direct first-strike signed gate (12) of the first-strike note [OPEN]

one-prime prime-power field (1)
  -> Decision B boundary-energy average
  -> common endpoint/boundary section (13)--(14)

separate fourth-order detuning route:
pair-frequency pq features -> rank-two detuning endpoint payment
  -> exact pair-feature generator / score-to-consumer map [MISSING]
```

The first-strike note states that its direct signed gate is formulated before the filtered-to-sharp ambiguity and retains the actual resolved prime words. Its endpoint ledger expressly uses the grouped linear-field $K_R$ and says that no high-product feature norm is assumed. The fourth-order detuning notes instead use pair frequencies and a different rank-two commutator. No dependency from the first-strike endpoint proof to the fourth-order pair-feature score was found. There is no identity equating the two, and none is needed for the direct fifth/sixth section selection.

Decision D's abstract Markov and nonnegative-energy restriction arithmetic remains valid, but its particular claim that the direct first-strike consumer's product-feature means are source-certified $O_R(1)$ is not supported by the F1 audit. The F1/F1B product-feature branch stays conditional. The direct first-strike endpoint conclusion survives by the independent one-prime proof above, not by transferring D's product score or by borrowing balanced-product coefficient mass.

## 6. Required wording corrections (no source report edited)

The following statements should be corrected in a future authorized edit; this note does not alter the consolidated report, Decision D note/certificate, or any historical source.

1. In `notes/WP84_CONSOLIDATED_HOSTILE_PROOF_AUDIT_B_TO_O.md`, the Decision D subsection says “the existing endpoint score estimates can be reapplied” and attributes the common direct-consumer section to D. Preserve the **same-section outcome**, but attribute it to the source-authentic one-prime statistic (3), the fixed-band reprojection theorem, and Decision B's adaptive energy average. Add that Decision D's separate product-feature $O_R(1)$ premise remains unsupported (F1), and that this correction does not affect the direct first-strike selection because its $K_R$ is a different one-prime object. The later sentence that the masked determinant consumer is not covered remains correct.
2. In `notes/WP84_DECISION_D_ENDPOINT_ADMISSIBILITY_DENSITY.md`, narrow D2: equations (1)--(7) prove the Markov/density/boundary restriction **conditional on** the declared score means and their consumer identity. They do not source-prove the pair-feature polynomial as written. Keep the D certificate/replay as finite conditional bookkeeping, not an endpoint-source proof. Cross-reference the separate F1C one-prime theorem for the direct first-strike route.
3. `notes/WP84_F1_ENDPOINT_FEATURE_LENGTH_INVESTIGATION.md` remains correct for the fourth-order pair-frequency source gap; do not replace its conclusion with the one-prime theorem. `notes/WP84_F1B_PRODUCT_FREQUENCY_ENDPOINT_BUDGET.md` remains a conditional generic payment analysis; F1C does not supply its missing pair-feature generator.
4. No referee-draft LaTeX source is tracked: `git ls-files '*Referee*' '*referee*' '*Draft*' '*draft*'` lists no such manuscript. Do not create a substitute. If the draft is restored, state separately the proved first-strike one-prime endpoint selection and the still-conditional fourth-order product-feature argument.

## 7. What this establishes and what remains open

Established in the stated scope: a uniformly bounded mean of the actual prime-power local endpoint statistic on each Decision B edge window; endpoint-good density at least $1/2$ at each edge; Cartesian pair density at least $1/4$; a common pair with $E(I)=O(\log d)$; complete normalized finite-section cubic boundary correction $o(1)$ on that pair; and repeated fixed-$R$ fifth/sixth finite-path reprojection errors $o(1)$ on the same section. F1C does not use the balanced product second-mass theorem or the fourth-order detuning commutator.

Still open and not implied here: the signed fifth/sixth arithmetic inequality (the first-strike gate), lower-moment identification in the same centered prime/Weil convention, uniform sixth Schatten/raw cubic deletion from the original full section, fourth-order filtered-to-sharp source transfer, source-masked determinant compatibility, actual $m_3=2$, conditioned Cayley energy below $0.105$, prime-to-Weil identification, zero-side block/tail transfer, and strict $>79\%$.

## Verification and artifact status

Replays run on this worktree:

- `python src/wp84_adaptive_boundary_large_sieve_replay.py` — PASS for finite separation/square-mass enumeration, crossing counts, endpoint-energy diagnostics, and stated scope.
- `python src/wp84_finite_section_boundary_cubic_replay.py` — PASS for exact finite block identity and scalar-background split; its signed cubic remainder remains open.
- `python src/wp84_non_gaussian_c5_c6_first_strike_replay.py` — PASS for exact rational consumer bookkeeping; signed arithmetic gate remains open.
- `python src/wp84_strict79_source_matched_replay.py` — PASS for its exact classification/coercivity/budget checks; signed source arithmetic remains open.
- `python src/wp84_decision_d_endpoint_admissibility_replay.py` — PASS only for conditional Markov/weight arithmetic and abstract hostile examples; it does not establish source support for pair features.

The analytic conclusions (5)--(14) follow from the source-local large-sieve and sampling proof, the endpoint row bound, the exact finite path count, and the Decision B nonnegative-energy average. Replays do not establish the asymptotic claims by themselves.

Starting and ending branch/HEAD are unchanged: `codex/c5-c6-attack-20261006` at `179f9959c4dabb675d1955646f212ddf6d3c51f5`. The existing uncommitted F1 and F1B notes were preserved. `notebooklm_packet/` was not inspected or modified. No push, merge, history rewrite, or `main` change occurred. This F1C note is new and left uncommitted because the linked Git index is outside the writable worktree.
