# WP84 F1 — endpoint-feature length and Decision D proof-gap audit

Date: 2026-10-10  
Scope: targeted audit of the endpoint-score input used by Decision D. This is
not a new optimization or an arithmetic counterexample.

## Verdict

**Decision C.** The finite Markov and same-weight energy-restriction arguments
in Decision D are correct *conditional on* source-valid lower- and
upper-endpoint score means (O_R(1)). The cited source notes do not establish
that input for the endpoint features produced by the detuning reduction. In
particular, the reduction explicitly exhibits two-prime features at frequency
`pq`, while Decision D inserts the single-prime cutoff `N` into the
Montgomery–Vaughan length term. No checked-in product restriction `pq <= N`,
or exact feature generator proving such a restriction, was found. With
two-prime support up to (N^2), the stated mean-value argument gives a bound
that diverges on Decision B's window. This is an insufficient estimate, not a
counterexample to the desired score bound.

Claude's F1 objection is therefore **substantially correct as a proof-gap
objection**: Decision D's source-specific score conclusion is not proved by
its cited calculation. The evidence does not prove the actual endpoint-score
bound false. The repository also contains a separate first-strike ledger
entry referring to a grouped linear-field score `K_R=O_R(1)`, but neither
that entry nor the audited endpoint notes identify `K_R` with the
product-frequency detuning features. The exact consumer-to-score interface
must be supplied before that entry can repair Decision D.

The independent Proposition S decoupling is valid for the *boundary energy*
and yields separate good endpoint sets of positive density. It does not bound
the endpoint feature scores and so does not repair F1.

Strict (>79\%\), raw cubic deletion, conditioned energy below (0.105), the
signed fifth/sixth gate, prime-to-Weil transfer, and zero-side transfer remain
OPEN.

## Verified state and evidence read

- Branch: `codex/c5-c6-attack-20261006`.
- HEAD: `179f9959c4dabb675d1955646f212ddf6d3c51f5`, matching the required
  `179f995` prefix.
- The only pre-existing untracked path is `notebooklm_packet/`; it was not
  opened or modified.
- The linked Git index is outside this worktree's writable root (see final
  operational note); this report is therefore left uncommitted.

The eight requested notes were read in full. The central source statements
are cross-checked below against the Decision D producer, certificate and
replay, the adaptive-boundary replay, the balanced-product gate, and the
direct first-strike ledger. The requested manuscript path
`notes/WP84_Referee_Draft_Adaptive_Cubic_Boundary.tex` is absent from the
tracked repository; `git ls-files` confirms it is not tracked.

## Source-support audit

The issue is the integer indexing the exponential in the *particular score*,
not whether the coefficient mass is bounded. For a polynomial

\[
S_\theta(t)=\sum_{m\le N_{\rm feat}}a_m(\theta)e^{it\log m},
\]
the mean-value length is (N_{\rm feat}), the largest integer frequency in
that sum. Bounded ℓ2 coefficient mass does not change that support.

| Object in the repository | Frequency and proved range | What the cited result actually establishes |
|---|---|---|
| Adaptive-boundary source field `F_k` | `n=p^v`, `p^v<=N=floor(X exp(-sqrt(L)))`; phase `exp(i T log n) exp(2 pi i k log(n)/L)` | This is the actual one-prime source field. Its discrete local large-sieve estimate and `sum |c_(p^v)|^2=O(1)` prove local `A_k=Im(F_k)` square mass `O(M)` on the adaptive endpoint window. This controls boundary energy, not the detuning endpoint score. |
| Balanced ordinary-prime pair coefficient | `m=pq`; phase `e^(i tau log(pq))`; coefficient `kappa_p kappa_q w_(p,q)` with `abs(w_(p,q))<=1` | `WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION.md` explicitly identifies this endpoint form. `WP84_BALANCED_PRODUCT_SECOND_MASS.md` proves coefficient ℓ2 mass (O(1)) after product collapse for its stated pool `p,q<=e^L=X`; that documented pool permits support up to `X^2`, before any additional feature gates. The note supplies no `pq<=N` restriction. |
| Pair made from two natural-cutoff source powers | `m=n_1*n_2=p^a*q^b`, with `n_1,n_2<=N`, if this is the actual factor pool | The support bound would be `N_feat<=N^2`. Repeated bases give `p^(a+b)<=N^2`; retaining proper powers does not reduce the maximum. The existing endpoint notes do not give the exact fixed-`R` coefficient/gate map needed to assert that this is the complete pool. |
| Threshold indicators, finite paths, and root/path weights | Multiply or truncate pair coefficients; the displayed feature weights are bounded | At fixed `R=6000`, finite multiplicity can enter `C_R`. The notes provide no proof that these weights force the product frequency below `N`, and no exact endpoint feature generator enumerating all path, root, sign, and overlap gates. A bounded taper is not a support restriction. |
| Generic polynomial in `WP84_GOOD_ENDPOINT_TRIMMING.md` | Written as `m<=N`, with only the coarse statement `N<=T^2` in its mean-value calculation | This is a valid abstract MV setup once the true `N` and coefficient mass are supplied. The note does not derive `N=N_nat` for the product features. Its own coarse bound produces mean score `O(T/epsilon_L)`, not `O_R(1)`. |
| Decision D polynomial and certificate | Rewritten as `n<=N_nat`, `integral sum |a_n|^2 <= C_R` | The producer records these as strings/hypotheses; it does not construct `a_n(theta)`, test their support, or derive them from prime coefficients. The replay checks abstract Markov/weight arithmetic only. |

The source coefficients available in the one-prime construction are
\[
c_{p^v}=-\frac{\Lambda(p^v)}{a_\phi(T)L\sqrt{p^v}},\qquad
z_{p^v}=c_{p^v}e^{iT\log(p^v)}.
\]
For ordinary primes the balanced-product note uses
\[
\kappa_p=c_0\frac{\log p}{L\sqrt p},\qquad
z_{p,q}=\kappa_p\kappa_q w_{p,q},\quad |w_{p,q}|\le1.
\]
Its product collapse (c(m)=\sum_{pq=m}z_{p,q}) has at most two ordered
representations for distinct ordinary primes, which proves its (O(1)) square
mass. This argument concerns the coefficient norm; it does not change
\(m=pq\) to (p), nor does it establish the exact (R=6000) endpoint
feature's full signed/path/root coefficient map. Proper prime powers have
lower coefficient square mass in the cited lemma, but still have product
frequencies when paired with another factor.

The direct Decision D formulation has no external `source_mask` callback.
That fact does not fill the missing direct score generator. The separate
hidden-prime determinant iterator does have such a callback and remains
unrelated; the established determinant-compatibility firewall must remain in
place.

## Mean-value calculation with the correct length

Put (X=T/(2\pi)\), (L=\log X\),
\[
N=\lfloor Xe^{-\sqrt L}\rfloor,\quad
U\sim T e^{-\sqrt L/2},\quad h=2\pi/L.
\]
For an integer-frequency Dirichlet polynomial, Montgomery–Vaughan gives an
integral bound proportional to
\((U+N_{\rm feat})\sum_m|a_m|^2\). Applying the same cell-sampling estimate
to (S_\theta) and its derivative, with (\log N_{\rm feat}=O(L)), gives
\[
\frac1{M+1}\sum_{u=0}^M\int |S_\theta(\tau_{b+u})|^2d\theta
\ \ll_R\ 1+\frac{N_{\rm feat}}U,
\qquad M\asymp UL.
\]
This is a valid inequality under the indicated integrated coefficient
second-mass hypothesis. It is not a bounded-mean conclusion unless
\(N_{\rm feat}=O(U)\), or a separate source-weighted estimate replaces it.

For the one-prime field, the scale substitution used by Decision D is
correct:
\[
\frac NU\sim\frac{e^{-\sqrt L/2}}{2\pi}\longrightarrow0.
\]
But for a pair supported on two natural-cutoff factors,
\[
\frac{N^2}{U}
\sim\frac{X e^{-3\sqrt L/2}}{2\pi}
=\frac{e^{L-3\sqrt L/2}}{2\pi}\longrightarrow\infty.
\]
If the pool in the balanced-product second-mass note is taken literally,
(p,q\le X), then
\[
\frac{X^2}{U}\sim\frac{X e^{\sqrt L/2}}{2\pi}
=\frac{e^{L+\sqrt L/2}}{2\pi}\longrightarrow\infty.
\]
The generic old allowance (N_{\rm feat}\le T^2) is also much longer than
the Decision D window and gives (N_{\rm feat}/U\asymp T e^{\sqrt L/2}\).
Floors, ceilings, and the (O(h)) sampling enlargement do not change these
limits. Differentiating adds a factor at most (2L+O(1)) for product support,
which changes only the implied constant in the sampled estimate.

Thus the substitution `N_feat<=N_nat` is **not justified**
for the product feature displayed in the maximal-reduction note. If its two
factors both range to (N_{\rm nat}), the natural support bound is (N_{\rm
nat}^2), not (N_{\rm nat}). The currently documented broader pair pool
allows (X^2). Neither produces the claimed (O_R(1)) from generic MV.

## Attempted repairs and the first missing estimate

1. **Bounded product coefficients do not shorten frequency support.**
   (\sum_m|c(m)|^2=O(1)) is already used correctly for the coefficient
   mass, but with (N_{\rm feat}\asymp N^2) it yields only a mean majorant
   (O_R(1+N^2/U)), which diverges.
2. **The balanced-product taper does not repair the estimate as documented.**
   Its only recorded hypothesis is |w|\le1. No decay in (pq) or support
   gate (pq\le N) is proved.
3. **Finite (R) does not by itself shorten the product.** The (R=6000)
   path set contributes finite constants/multiplicities, but the cited
   feature reduction has no theorem that converts this into a one-factor
   support restriction. Exact root/path weights and the per-feature source
   gate are absent from an executable generator.
4. **The product-block large sieve is a different scale statement.** The
   cited full-section block bound (1+16\pi M/T), on a product block of
   integer size (M), becomes (1+O(M/U)) on a physical window of length
   (U) (the sampled polynomial length is (\asymp UL), while the
   log-frequency separation is (\gg1/(ML))). For (M\asymp N^2), this
   factor diverges. The extra (1/(TL)) payment discussed in that note
   belongs to a separately assumed detuning perturbation; it is not present
   in the endpoint-score second moment and cannot be transferred to it.
5. **Proper-power disposal is not enough.** The cited (O(L^{-2})) proper-
   power coefficient square mass is a coefficient-side estimate, not a bound
   on a long product polynomial. It does not control all ordinary-prime
   product features and, by itself, does not make their local mean bounded.

The first missing source theorem is a uniform short-window estimate for the
actual weighted product-frequency endpoint score, separately at both ends:
\[
\frac1{M+1}\sum_{u=0}^M\int_\Theta
\left|\sum_{n_1,n_2\le N}
 c_{n_1}c_{n_2}\,W^-_{n_1,n_2}(\theta;R,T,I_0)
 e^{i\tau_{b+u}\log(n_1n_2)}\right|^2d\theta
\ \ll_R\ 1,
\tag{F1-}
\]
and the analogous (W^+) estimate at (b+d-1-v). Here
\(c_n=-\Lambda(n)/(a_\phi L\sqrt n)\), all (n=p^a\le N\) are retained,
and (W^\pm\) must be the *actual* (R=6000) feature/path/root/overlap
weights from the endpoint derivation, including exact gates and multiplicity.
The carrier `e^(i T log(n_1 n_2))` is retained through
`tau_k=T+hk` in the displayed phase. This displayed inequality is the target shape for the
identified product-frequency component, not a claim that it exhausts every
feature: ratio-frequency components, if present in the complete derivation,
must also be listed and controlled. No such (W^\pm) generator or estimate
is currently checked in. A mere replacement of (N_{\rm feat}) by (N)
would assume the missing conclusion.

The first source-definition subgap is correspondingly precise: provide the
exact endpoint coefficient map (a_m^\pm(\theta;T,I_0)), with its
fixed-(R) path and root sums, signs, prime-power gates, and normalization,
and prove which (m)'s survive. Until that map is supplied, no exact
source support census beyond the pair component above is justified.

## Proposition S — valid boundary-energy decoupling

Let the original source interval be (I_0=[b,b+d-1]\), and let
\(I_{u,v}=[\ell_u,r_v]\), where
\[
\ell_u=b+u,\quad r_v=b+d-1-v,\quad 0\le u,v\le M,
\]
with (2M<d\). For the actual bounded one-prime source field (A_k=\Im F_k\),
define the finite-energy endpoint functions
\[
\Phi(u)=\frac1{\pi^2}
\sum_{i=\ell_u}^{b+d-1}\sum_{j<\ell_u}
\frac{(A_i-A_j)^2}{(i-j)^2},\qquad
\Psi(v)=\frac1{\pi^2}
\sum_{i=b}^{r_v}\sum_{j>r_v}
\frac{(A_i-A_j)^2}{(j-i)^2}.
\]
All index ranges are nonsingular; the (i)-range is finite and the
one-sided (j)-tail converges because (A_k) is bounded for each finite
source cutoff. Splitting the complement of (I_{u,v}) into (j<\ell_u)
and (j>r_v), and enlarging the inside (i)-ranges to the indicated
subranges of (I_0), gives exactly
\[
0\le E(I_{u,v})\le\Phi(u)+\Psi(v).
\tag{S}
\]

Their separate means are (O(\log d)). To see this, use
\((A_i-A_j)^2\le2A_i^2+2A_j^2\) and the already-proved uniform local
one-prime square bound
\[
\sum_{k=a}^{a+M}A_k^2\le C M,
\]
which follows from (M/(NL)\to\infty) in the adaptive-boundary
large-sieve note. For (i=\ell_u+t\),
\[
\sum_{j<\ell_u}(i-j)^{-2}\le\frac{2}{t+1};
\]
for (j=\ell_u-s\), (s\ge1\), the sum over the finite (i)-range obeys
\[
\sum_{t=0}^{b+d-1-\ell_u}(t+s)^{-2}
\le \min(2/s,\,d/s^2).
\]
For each fixed offset (t) or (s), summing the corresponding (A^2) over
the moving (u)-window is (O(M)) by the local square bound. After dividing
by (M+1), the interior offsets contribute a harmonic sum (O(\log d));
the external offsets contribute (O(\sum_{s\le d}s^{-1}+\sum_{s>d}d/s^2)
=O(\log d)). The right endpoint is symmetric. Therefore
\[
\frac1{M+1}\sum_u\Phi(u)\le C_\Phi\log d,\qquad
\frac1{M+1}\sum_v\Psi(v)\le C_\Psi\log d.
\]
Markov gives sets (G_-,G_+\) each of endpoint density at least (1/2)
on which (\Phi\le2C_\Phi\log d) and
\(\Psi\le2C_\Psi\log d). Their Cartesian product has exact uniform pair
density at least (1/4); on it,
\[
E(I_{u,v})\le2(C_\Phi+C_\Psi)\log d.
\]
This is a genuine separated-endpoint selection for boundary energy, derived
from the one-prime source. It is compatible with independent choices of the
two endpoints and has the same (O(\log d)) scale as the existing adaptive
pair-average theorem. It does **not** establish a score-good endpoint set for
the product features in (F1±), so it cannot by itself establish Decision D's
claimed jointly admissible set.

## Decision D and Proposition S disposition

- **A — not established:** the product endpoint support is not shown to be
  (N_{\rm nat}\). The one-prime mean-value substitution is invalid for the
  displayed (pq) feature absent a product cutoff theorem.
- **B — not established:** no separate source-matched weighted short-window
  product mean, maximal estimate, or product-block bound strong enough to
  yield (O_R(1)) is in the cited files.
- **C — established:** the abstract Markov argument, exact (1/4) Cartesian
  density arithmetic under separate score gates, nonnegative energy
  restriction (C_B\log d/\gamma), and weighted-measure cautions are valid
  conditionally. The source-specific bounded-score premise is not established
  for the endpoint feature family claimed by Decision D.
- **D — not established:** no source-legal counterexample to the (O_R(1)
  score bound was found. The (N^2/U\to\infty) calculation only shows the
  generic MV majorant is too weak.
- **Proposition S — proved for boundary energy:** it gives separate
  (O(\log d)) boundary scores and a product good set. Its combination with
  endpoint feature admissibility remains conditional on (F1±), or on a
  different independently proved endpoint score theorem.

## Required correction plan (no source files changed here)

1. **`notes/WP84_Referee_Draft_Adaptive_Cubic_Boundary.tex`:** the requested
   path is absent and untracked, so there is no manuscript text to edit. If
   this draft is restored, replace any claim that the Decision D endpoint
   scores have length (N_{\rm nat}) with the exact feature support table;
   state Decision D as conditional until (F1±) or an exact linear-field
   score identity is proved. Preserve the separate adaptive boundary result.
2. **`notes/WP84_CONSOLIDATED_HOSTILE_PROOF_AUDIT_B_TO_O.md`:** replace
   Decision D's current “Survives (B, in exact scope)” endpoint admissibility
   statement with: Markov/weighted restriction is correct conditionally;
   actual (O_R(1)) feature-score input is open because pair support can be
   (pq). Keep Decision B's adaptive selected-section boundary transfer and
   Proposition S boundary-energy result proved, but do not claim that they
   jointly select a Decision-D-admissible section. Retain the determinant
   source-mask scope firewall and all unrelated open gates.
3. **`notes/WP84_DECISION_D_ENDPOINT_ADMISSIBILITY_DENSITY.md`:** downgrade
   D2 to conditional/open for its source premise; identify the actual
   (N_{\rm feat}) as unresolved, show the (N^2/U\) and (X^2/U) scales,
   and mark the certificate's `n<=N` coefficient mass as an unverified
   hypothesis rather than a source theorem. Keep its exact weighted Markov
   argument as a conditional lemma. Do not edit the certificate in this
   run, per the instruction to preserve historical certificates.

## Verification and strongest surviving claims

The existing `src/wp84_decision_d_endpoint_admissibility_replay.py` passed.
It verifies finite Markov arithmetic, the conditional (1/4) density,
weighted-mass bookkeeping and abstract anticorrelation tests; its own header
states that it does not verify the endpoint polynomial's source support. The
existing `src/wp84_adaptive_boundary_large_sieve_replay.py` also passed. It
checks finite square-mass/kernel/block identities and diagnostics, while its
analytic one-prime local large-sieve proof remains the cited asymptotic
argument. Neither replay verifies (F1±), (pq\le N), or an identity from
the first-strike (K_R) ledger entry to the detuning feature scores.

The strongest unaffected analytic result is Decision B: for the actual
one-prime prime-power field and its natural cutoff, an existential
(o(d))-trimmed section has (E(I)=O(\log d)), giving complete normalized
finite-section cubic *boundary correction* (o(1)). Proposition S gives a
second separated-endpoint proof of an (O(\log d)) boundary-energy good set.
Neither result transfers the unbounded raw cubic from the original full
section, proves the high-order signed arithmetic gate, or closes the strict
zero-proportion theorem.

## Operational status

No prior note, certificate, script, Git history, or `notebooklm_packet/` file
was modified. This is the only intended new path:
`notes/WP84_F1_ENDPOINT_FEATURE_LENGTH_INVESTIGATION.md`.
The shared/linked index resolves outside the writable worktree under the
Downloads checkout; no staging or commit was attempted. Thus the report is
new local audit documentation only. No push or merge occurred.
