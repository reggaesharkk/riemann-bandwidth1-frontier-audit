# WP84 alias-resolved positive-part attack

**Starting state:** `codex/c5-c6-attack-20261006` at `96960fb563aac5144045e5bf7be9cdc528bd9f7f`. Local-only audit. `notebooklm_packet/` was present as pre-existing untracked content and was not read or changed by the verifier, staged, or included in the commit.

**Decision E — one precise analytic lemma remains.** The exact unrestricted Boolean-mask support function is now split by alias, but no nontrivial numerical upper bound or positive asymptotic lower bound for it is established. This run does not prove the unrestricted-mask route impossible. Strict >79 remains OPEN.

## Exact object and alias split

For a full callback key

```text
k = (fid, slots, lag, T, section, m)
```

let `a_k(T,I)` be the sum of all source atoms having that *entire* key, with the degree-five and degree-six coefficients retained. The unrestricted Boolean support function is

\[
 P(T,I)=\sup_{\chi:K\to\{0,1\}}\sum_{k\in K}\chi(k)a_k
      =\sum_{k\in K}[a_k]_+.
\]

The equality is finite-dimensional Boolean optimization; it does not assert anything about the actual omitted callback. Partition the key set by its integer alias:

\[
K_{T,I}=\bigsqcup_m K_{T,I,m},\qquad
P(T,I)=\sum_m P_m(T,I),\qquad
P_m(T,I)=\sum_{k\in K_{T,I,m}}[a_k(T,I)]_+.
\]

For the frozen *near-alias survivor census*, the CSV gives exactly:

| degree | raw origins | origin/alias pairs | near-survivor alias set |
|---|---:|---:|---|
| 5 | 1,132 | 1,956 | \(\{-4,-3,-2,-1,1,2,3,4\}\) |
| 6 | 7,608 | 19,632 | \(\{-5,-4,-3,-2,-1,1,2,3,4,5\}\) |
| total | 8,740 | 21,588 | alias-resolved; m is part of every callback key |

These are support possibilities from the frozen pattern census; the counts do not assert that each prime/window assignment is occupied. The historical 453 is the unmasked origin-functional catalogue and cannot be used as a mask-component count. The formal 1,148 alias-resolved components and size histogram `{2:7,4:10,6:44,10:79,12:290,20:58,24:660}` are only conditional on the extra full dihedral/conjugation covariance. No nontrivial equality of callback bits is proved.

For any degree-b pattern, \(|\lambda|<bL\), because every slot prime is at most \(N(T)<e^L\). In the nearest residual cell \(\lambda-mL\in[-L/2,L/2)\), this gives the exact outer candidate envelope \(|m|\le b\). Thus the long-tail aliases are contained in \(\{\pm1,\ldots,\pm5\}\) at degree 5 and \(\{\pm1,\ldots,\pm6\}\) at degree 6. The full active tail occupancy is **not** determined: it depends on the exact prime/window gates, and no tail-support occupancy certificate is present. Candidate pair-count ceilings from this envelope are 11,320 (degree 5) and 91,296 (degree 6), not observed counts.

If two windows both hold,

\[
|\lambda-mL|\le H/T,\qquad |\lambda-m'L|\le H/T,
\]

then \(|m-m'|L\le 2H/T\). Therefore `2H/T < |m-m'|L` makes their intersection empty; since distinct integer aliases satisfy \(|m-m'|\ge1\), `2H/T < L` suffices. For fixed H this holds eventually because \(T\log(T/(2\pi))\to\infty\). At H=400 it holds for T≥1000 and thereafter: `800/1000 < log(1000/(2π))`, with the left side decreasing and right side increasing. If H varies, the exact symbolic condition remains `2H(T)/T < L(T)`.

This proves support disjointness in \(\lambda\), not mask-bit equality and not orthogonality. Indeed, at integer root index k,

\[
e^{2\pi i k\lambda/L}=e^{2\pi i k(m+\delta/L)}=e^{2\pi i k\delta/L},
\]

so the integer alias disappears from the section-root factor while the carrier retains \(e^{iTmL}\). There is no orthogonal-projection identity. The cross contribution is explicitly

\[
2\operatorname{Re}\sum_{m<m'} F_m\overline{F_{m'}}.
\]

The finite-average identity \(A^{-1}\int_0^A e^{i(\xi-\eta)t}\,dt=(e^{i(\xi-\eta)A}-1)/(i(\xi-\eta)A)\) is generally nonzero; hence disjoint labels alone do not imply norm additivity.

## Exact coefficient grouping and positive parts

The atomic source formula retained by the checked-in constructor is

\[
\operatorname{Re}\!\left(\omega_b\,\chi(k)\,\prod_{j=1}^b
 {-\log p_j\over a_\phi(T)L\sqrt{p_j}}f_{\ell_j}^{\epsilon_j}(\log p_j/L)
 \ e^{2\pi i\sum_j\epsilon_j u_{j-1}\log p_j/L}\ K_\ell(\lambda)\right),
\]

with the original ordinary-prime pool \(p\le N(T)=\lfloor e^{L-\sqrt L}\rfloor\), injective equality-block assignments, every closed R=6000 path, the actual root sum, and all source indicators. Here \(\omega_5=-11501/12500\), \(\omega_6=137641/250000\),

\[
K_\ell(\lambda)={e^{iT\lambda+2\pi i i_{\min}\lambda/L}\over d'}
\sum_{r=0}^{M-1}e^{2\pi i r\lambda/L},\quad M=\max(0,d'-\operatorname{range}(u)).
\]

An exact duplicate full key must be aggregated before applying `[x]_+`. Different `m` values are different keys. The only positive-part identity available without an equality theorem is `[x]_+ + [-x]_+ = |x|` when the same scalar expression occurs with those exact signs at two keys. The frozen coefficient table gives a negative degree-five coefficient and a positive degree-six coefficient; since degree/fid is part of the key, this is not a cancellation. The consumer-weight magnitudes sum to `163444421/31250` only under the additional covariant collapse and are not a valid unrestricted-mask bound.

**Zero census:** zero exact full-key templates were proved by the present symbolic audit. This is a count of certified eliminations, not a claim that all fully expanded amplitudes are nonzero. The lazy iterator does not instantiate source masks, prime windows, or all exact duplicate-key expressions, so it cannot certify further cancellations. No positive part was taken before key aggregation in the stated target.

## Upper bounds and their gaps

For every T the direct rigorous inequalities are

\[
0\le P_{\rm near}+P_{\rm tail}\le\sum_k|a_k|
\le \sum_{\text{retained source atoms}}|\omega_b|
\prod_j{\log p_j\over a_\phi(T)L\sqrt{p_j}}\,1_{\rm source\ gates}.
\]

The exact filter and root estimates used are \(|f_\ell^\epsilon(\alpha)|\le1\) on \(0\le\alpha\le1\) and \(|K_\ell(\lambda)|\le M/d'\le1\). This is the strongest direct triangle statement available without claiming a duplicate-key cancellation. If every mask/window restriction is dropped for a deliberately enlarged upper bound, put

\[
S_1(T)=\sum_{p\le N(T)}{\log p\over a_\phi(T)L\sqrt p}.
\]

There are at most \((2R+1)^4=12001^4\) closed paths, because four displacements determine the fifth. The candidate alias ceilings give the explicit, valid but intentionally weak majorant

\[
B_{L1}(T)=12001^4\left({11501\over12500}\,11320\,S_1(T)^5
 +{137641\over250000}\,91296\,S_1(T)^6\right).
\]

PNT partial summation gives \(\sum_{p\le N}\log p/\sqrt p\sim2\sqrt N\); with the inherited `a_phi(T)→1`, \(N\sim e^{L-\sqrt L}\), hence

\[
S_1(T)\sim {2e^{(L-\sqrt L)/2}\over L}.
\]

So this absolute-value ceiling grows like its degree-six term, of order \(e^{3L-3\sqrt L}/L^6\), up to the displayed fixed constant. Its ratio to the relaxed budget tends to infinity. This says the triangle estimate is useless; it is **not** a lower bound on P and does not show P diverges.

At atom level, the square-weight prime mass is

\[
S_2(T)=\sum_{p\le N(T)}{(\log p)^2\over a_\phi(T)^2L^2p}\sim {1\over2},
\]

again by PNT and `a_phi→1`. This does not equal the L2 energy of the canonical coefficients `a_k`: summing atoms with a common carrier/key creates cross terms. Cauchy after aggregation requires the exact key incidence and a usable count of aggregated coefficients; neither is available. The complete coefficient energy and a numerical L2 bound are therefore unproved.

| method | actual object / hypotheses | result |
|---|---|---|
| triangle/L1 | complete pool; |f|, |K|≤1; exact path ceiling | rigorous symbolic bound above; budget ratio grows, so no close |
| L2/Cauchy | needs square energy after full callback-key aggregation | requires unavailable key-incidence/cross-term lemma |
| Montgomery–Vaughan / Hilbert | needs a separated frequency set and coefficients fixed independently of the averaging variable | not verified after alias folding; `mL+δ` folds to δ in root index |
| large sieve | needs specified separated frequencies/weights and a compatible interval average | section mask/root weights and key-dependent gates prevent direct instantiation |
| PNT | controls marginal sums, e.g. S1 and S2 | does not control signed/window-intersected near-product correlations or their positive parts |

No mean-value result yields an `o(1)` estimate for the full P. No numeric upper bound below or finite multiple of `Delta_relaxed` is obtained. The absolute L1 ceiling / budget diverges and must not be confused with the actual P / budget.

## Lower bounds, phase, and tail

The only unconditional lower bound here is `P≥0`, or zero times the budget. No legal fixed-carrier pilot gives a positive asymptotic contribution: the available constructor still requires the actual original slot windows and callback values; no one template is certified admissible with a nonzero normalized limiting amplitude. Thus no lower bound above the budget, and no kill result, follows.

For fixed complex B,

\[
{1\over2\pi}\int_0^{2\pi}[\operatorname{Re}(e^{i\theta}B)]_+\,d\theta={|B|\over\pi}.
\]

Likewise a fixed nonzero carrier frequency and fixed B have that long-time mean. In the source family, B, prime windows, section/root multiplier, and admissibility depend on T; the target is a limsup over heights, not a certified phase-Cesàro average. No equidistribution or actual signed saving is earned.

The exact split is `P=P_near+P_tail` with aliases and support above. Both charges remain unknown. The near piece has the finite 21,588 origin/alias support census; the long tail has only the nearest-cell candidate envelope. Neither is bounded below by a positive constant or above by an asymptotically useful number. H cannot be optimized: no proved near(H), tail(H), or budget(H) functions are in the source.

## Budget replay and exact remaining lemma

The frozen arithmetic is replayed exactly:

\[
\Delta_{\rm relaxed}={52897896569489\over572357731837500000}
\quad(\approx9.2421\cdot10^{-5}),
\]

and at H=400 the reference primitive scale is

\[
\Delta_{\rm relaxed}/201={52897896569489\over115043904099337500000}
\quad(\approx4.5981\cdot10^{-7}).
\]

Both remain reference allocations. No charge has been paid, and the H=400 multiplier is not an estimate of P.

The single sufficient analytic lemma still needed is exactly:

> For the full source-defined callback tuple `(fid, slots, lag, T, section, m)`, complete prime pool `p≤N(T)`, every closed R=6000 path and exact section-root sum, prove uniformly over admissible sections and executable Boolean masks that
> \[
> \limsup_{T\to\infty}\sum_{k\in K_{T,I(T)}}[a_k(T,I(T))]_+\le {52897896569489\over572357731837500000},
> \]
> including the near aliases and retained long tail.

This is a precise unresolved estimate, not a claim that the inequality is false. The first missing step is a quantitative bound after complete full-key aggregation that retains the prime-restricted product correlations and their phases. The run stops here: no alternate search branch is opened.

## Replay

Run:

```powershell
python src/wp84_alias_resolved_positive_part.py
python src/wp84_alias_resolved_positive_part_replay.py
```

The replay reconstructs the CSV census independently, checks the rational budget and disjointness condition, and rejects 18 hostile mutations, including dropping `m`, using 453 as the mask count, changing R or either consumer coefficient, truncating primes, deleting the tail, taking positive parts in the wrong order, assuming covariance/equidistribution, or fabricating a selector. It does not claim a source selector or a theorem-side bound.
