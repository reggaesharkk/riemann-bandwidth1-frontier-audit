# WP84 good-endpoint / hidden-prime determinant compatibility audit

Date: 2026-10-08

Decision: **GOOD-ENDPOINT THEOREM IS A DIFFERENT OBJECT — exact first
incompatibility identified.**

This is a Gate 1 audit, not a selector reconstruction and not a determinant
calculation. The four historical inputs below were read from the pinned PR #5
source commit `908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5` with `git show`; the
worktree itself remained on its existing branch. The current amplitude source
was read at local HEAD `a07e52b4365c1094b3a82c045038ffc217fe8a4a`.

## Finding

The *interval geometry* is compatible: both constructions use integer Fourier
indices, contiguous inclusive intervals `[k_-, k_+]`, and the grid
`tau_k = T + (2 pi/L) k`. A good-endpoint interval can therefore be supplied
as a section argument to a formula whose only section input is `[k_-,k_+]`.
The stated dimension losses are also compatible asymptotically.

The theorem-side endpoint score, however, is not identified with the current
determinant amplitude object. The first exact failure occurs at the score's
summand identity: `WP84_GOOD_ENDPOINT_TRIMMING.md` bounds feature polynomials
`S_theta(tau) = sum_{m<=N} a_m(theta) exp(i tau log m)` through an integrated
second-mass estimate, but it never defines the coefficients `a_m(theta)` as
the complete, source-masked carrier/path summands of
`src/wp84_fifth_full_pool_amplitude.py`, nor proves that the corresponding
score contains those summands with their required weights. The latter iterator
explicitly takes a caller-provided `source_mask(fid, slots, lags, T, section,
alias)` and requires the complete ordinary-prime pool. There is no such
callback or an equivalent mask identity in the four pinned inputs.

This is an object-identification failure, not a mismatch in the integer
interval notation. The mean-square theorem cannot be transferred to the
determinant rows merely from their common use of Fourier sections. Under the
requested gate order, this prevents both a selector-free determinant theorem
and a deterministic argmin based on the trimming score from being certified.
Routes A and B are therefore not entered. No source selector, mask, matrix
row, or determinant value is guessed.

## Compatibility table

| Required input | Good-endpoint theorem at pinned PR #5 head | Current hidden-prime/determinant object | Audit |
|---|---|---|---|
| Row indexing | Fourier samples `tau_k`; spacing `Delta_tau=2 pi/L` | Integer source rows in `I(T)=[k_-,k_+]`; row phase uses the same `2 pi/L` grid | Compatible at the coordinate-formula level |
| Fourier coordinates | `tau_k=T+(2 pi/L)k` and feature phases `exp(i tau log m)` | Slot phases and root phases use `2 pi/L` times integer row/root coordinates and log-prime sums | Compatible frequency lattice; no termwise feature-to-atom identification |
| Endpoint convention | Candidate lower/upper Fourier indices, yielding a contiguous principal section | Inclusive endpoints; `n=k_+-k_-+1` | Compatible notation and interval convention |
| Candidate geometry | `epsilon_L=L^(-1/2)`, `r=floor(epsilon_L d)`; endpoints drawn from end windows | Actual section is a source-selected input; no executable selector is encoded | Candidate geometry could define a new section, but source legality is not shown |
| Dimensions | Deletes `o(d)` rows; states `d'=d(1+O(epsilon_L))` | `d=floor(TL/(2 pi))`, `d'=|I(T)|`, requires `d'/d -> 1` | Compatible asymptotic condition; the source's exact endpoint rule is absent |
| Principal contiguity | Explicit contiguous principal submatrix | Iterator takes one inclusive interval and uses its root interval | Compatible as an operation |
| Root sums | Endpoint proof controls endpoint vectors/features; it does not state the source root-sum identity | For closed path prefix `v`, root count is `max(0,n-range(v))`, roots run from `k_- - min(v)` through `k_+ - max(v)` | Not identified term by term; shared interval alone is insufficient |
| Carrier normalization | Endpoint cost is normalized by `1/d'` and the feature-family second-mass bound | Five-slot amplitude retains `a_phi(T)^(-5)`, slot factors `-log(p)/(a_phi(T)L sqrt(p))`, root divisor `1/n`, and positive-carrier real-part factor | No normalization map in endpoint theorem |
| `R=400` | Fixed-band pair stability and quartic first-record consumer | Not the determinant path cutoff | Distinct role; no direct equality claimed |
| `R=6000` | Absent from endpoint score theorem | Every closed five-step path has `|ell_s|<=6000`, `sum ell_s=0` | Required determinant structure is absent from the score statement |
| Source masks | No `source_mask` signature or mask formula in the four theorem inputs | Iterator requires the exact callback on `(fid, slots, lags, T, section, alias)` | **First exact incompatibility: no theorem-to-source-mask summand identity** |
| Prime pool | Generic Dirichlet coefficients; endpoint note uses `N<=T^2` for its MV bound | Complete ordinary primes `p<=N(T)=floor(exp(L-sqrt(L)))`, with exact slot-window/equality/alias masks; hidden canceled-prime sums are retained | No transfer of the full pool or hidden-prime coefficients is proved |
| Adjacent-index / rank-two | Adjacent Fourier index is expressly included in the endpoint score; endpoint commutator has rank two | Determinant rows are built from all source-masked paths and carrier assignments | Endpoint mechanism is analogous, but not a determinant-row identity |
| Four determinant blocks | Not part of the R=400 endpoint argument | Current block families have sizes `6, 8, 16, 8`; entries depend on full-pool source atoms | No block rows, visible subset, or determinant score is supplied |

## Exact first incompatibility

Let `Score_good` denote the finite feature score whose existence is asserted
by the trimming proof. Its construction in that note is through generic
`a_m(theta)`, the integrated bound

`int sum_m |a_m(theta)|^2 dtheta <= C`,

and the Montgomery--Vaughan/sampling estimates. The current determinant entry
is instead a sum over injective equality-block prime assignments and all
closed `R=6000` paths, with an indicator returned by `source_mask`, the
carrier alias restriction, source slot filters, exact root sum, and the
`a_phi(T)^(-5)` normalization. None of the four pinned files supplies an
identity

`a_m(theta) = (or a proved aggregate of) the current source-masked determinant atoms`,

nor a bound showing that `Score_good` dominates the endpoint functional of
those atoms uniformly in the feature and carrier indices. The endpoint
second-mass theorem consequently has no established hypothesis for these
determinant rows.

This is the first missing bridge in the dependency order. Because the requested
Gate 1 required exact compatibility for the masks, retained/cancelled primes,
and determinant normalizations as well as the interval, it is not valid to
mark Gate 1 “compatible” and move to Routes A/B. In particular, choosing an
argmin of an unspecified/generic score would not make its section
source-authentic.

## Scope and limits

- The R=400 pair-stability result remains a statement about the fixed-band
  pair layer and contiguous `o(d)` trimming.
- The R=400 first-record assembly remains internal theorem-side bookkeeping;
  it does not establish the R=6000 full-pool determinant source map.
- The current full-pool iterator remains a lazy formal constructor. It
  requires external `source_mask` and a section supplied by the source.
- No fifth-block rank, hidden-prime subset `K`, first coefficient
  `C_(m-1)`, or strict `>79` conclusion is computed or promoted here.
- `notebooklm_packet/` was not read or modified in this audit.

The minimum continuation needed to reopen Gate 1 is a source-authentic lemma
that expands each trimming feature score into the current masked, normalized
full-pool atoms (or proves a uniform domination of the determinant endpoint
score by the stated trimming score), with the same row/root ordering and
section endpoints. Only after that lemma can selector-free uniformity or a
deterministic minimizer be tested.

## Reproduction

Run:

```powershell
python src/wp84_good_endpoint_determinant_compatibility_replay.py
```

The script verifies the pinned commit, required source paths and defining
source signatures, then writes
`notes/WP84_GOOD_ENDPOINT_DETERMINANT_COMPATIBILITY_CERTIFICATE.json`.
It performs no checkout, fetch, push, packet write, or theorem calculation.
