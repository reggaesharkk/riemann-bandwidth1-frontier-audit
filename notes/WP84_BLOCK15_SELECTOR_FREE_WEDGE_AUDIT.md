# Block `{15,20,26,28,31,32}`: selector-free exterior-power audit

## Decision

**E. SOURCE INPUT STILL MISSING.** The requested six-column block remains
uncertified. This audit does not search for or assume a historical row
selector. It proves an exact conditional endpoint-translation result for the
source-derived real jet operator, but the full source-projected six-column
wedge is not instantiated. No rank is promoted.

The only new uniform algebraic bound is that the sixth exterior action on the
14-dimensional real jet stack has polynomial degree at most **24**, sharper
than the generic `m*hmax=36` bound. If a fixed source-cell, fixed-section-
length projected wedge is not the zero polynomial in a one-parameter endpoint
translation, it can vanish at at most 24 translation values. The premise is
not established for this block, and translations do not change section
lengths or cross source-mask cells.

## Exact object boundary

The block is the six canonical functionals `15,20,26,28,31,32`, at `R=6000`.
The source-linked amplitude file identifies the complete natural prime cutoff,
injective equality-block assignments, closed five-step paths, root interval,
carrier and real-part conventions. But the executable interface does not
produce the required six columns:

* `source_amplitude_entry(...)` returns a summand schema, not evaluated matrix
  entries or a coefficient-column basis;
* `iter_source_atoms(...)` requires a caller-provided
  `source_mask(fid, slots, lags, T, section, alias)` and a complete prime
  stream; the module contains no implementation of that mask callback;
* the complete hidden-prime contributions in columns 31 and 32, along with
  all visible assignments, paths and source normalizations, are not evaluated
  into a common coefficient/jet matrix;
* therefore neither the actual source projection `P_B` nor the actual jet
  column space `V_B` is represented as executable data.

This is not a demand for one historically preferred section. A selector-free
claim still needs a defined source mask and the exact complete-pool columns
for each section to which the universal quantifier applies. The repository's
asymptotic condition `d'/d -> 1` and a schema accepting endpoints do not
instantiate those inputs. The exact physical-admission conditions and the
distinction between prescribed-prime realization and complete carrier sums
are recorded in `WP84_FIFTH_LEGAL_STENCIL_AND_PRIME_REALIZATION.md`.

## Exact exterior-power calculation

For one frozen source cell let `J_h` be the complex coefficient of the
normalized amplitude at jet order `h`, for `h=0,...,6`. Under a root-origin
translation by `s` that keeps the cell, masks and length fixed, the exact
source root identity is

\[
J_h(a+s)=\sum_{r=0}^h\frac{(2\pi i\lambda s)^{h-r}}{(h-r)!}J_r(a).
\]

On coordinates `(Re J_0, Im J_0, ..., Re J_6, Im J_6)`, write the generator
as `G=eta G0`, `eta=2*pi*lambda`. The nonzero entries of `G0`, in zero-based
coordinates, are

\[
(G_0)_{2h,2h-1}=-1,\qquad
(G_0)_{2h+1,2h-2}=1,\qquad 1\le h\le6.
\]

This retains the real/imaginary coupling. The ambient real dimension is 14.
The sixth exterior space has dimension `binom(14,6)=3003`, with the exact
induced generator

\[
D_6=d\Gamma(G_0)=\sum_{r=1}^{6}
 I\wedge\cdots\wedge G_0\wedge\cdots\wedge I,
\qquad
\bigwedge^6 e^{\eta sG_0}=e^{\eta sD_6}.
\]

Index a coordinate in jet level `h` with grade `h`. Each nonzero entry of
`D_6` raises the sum of the six grades by exactly one. Among six-element
subsets of two coordinates at each level `0,...,6`, the minimum grade sum is
`6` (levels `0,0,1,1,2,2`) and the maximum is `30` (levels `4,4,5,5,6,6`).
Consequently `D_6^25=0` and `exp(eta*s*D_6)` has degree at most 24. The exact
constructor enumerates 9,504 nonzero exterior-generator transitions and
records all 12 nonzero entries of `G0`.

For any fixed linear map `P` and six-column source blade
`v=\bigwedge^6 V_B`, each coordinate of

\[
W(s)=(\bigwedge^6P)e^{\eta sD_6}v
\]
is therefore a polynomial of degree at most 24. If `W` is not identically
zero, one nonzero coordinate polynomial bounds the common zero set by at most
24 points on that translation line. If `W` is identically zero, translation
algebra alone gives no nonvanishing. The implication “`e^{sG}` is invertible,
therefore `P e^{sG}V_B` has rank six” is false for arbitrary projections: for
example, any rank-five `P` annihilates every sixth exterior vector.

This theorem applies only to a fixed cell, fixed length and fixed projection.
The source root formula does not give this translation identity across a
mask/cell boundary. Changing the section length changes the root-count
polynomials, so the degree-24 result does not compare different lengths.

## Outcome fields

| Requested item | Result |
|---|---|
| Exact block | `{15,20,26,28,31,32}` |
| Source-legal object actually used | Exact fixed-cell root-translation operator only; no full `P_B,V_B` |
| Exterior dimension | `3003`; ambient real jet dimension `14` |
| First section-expansion candidate | Deficit `m-1=5` is the first possible coefficient from the common-leading-row identity; its value may vanish and is not evaluated here |
| Endpoint-translation degree | At most `24` on one fixed-cell, fixed-length orbit |
| `K_B` | Unknown; no determinant-visible moment subset computed |
| Section dependence | Translation polynomial as above; arbitrary lengths/masks remain unlinked |
| Exceptional sections | Unknown for the actual block. Conditional bound: at most 24 translated endpoints if the actual projected wedge is not identically zero on the orbit |
| Block rank | Not certified |
| Fifth rank | Unchanged: `38–72`; zero dimensions added |
| Strict `>79` | Open |

`S_2,...,S_8` are the candidate hidden-prime moments for this depth-six block,
but the determinant-visible subset `K_B` is not inferred from that candidate
list. The first possible deficit-5 cofactor expression remains unevaluated.
The files `WP84_EXACT_Q_MASK_AND_DETERMINANT_VISIBLE_MOMENT_BASIS.md` and
`WP84_DETERMINANT_VISIBLE_HIDDEN_PRIME_COMPRESSION.md` explain why PNT moment
asymptotics and the 73-to-9 compression do not determine its signed
coefficients.

## Smallest remaining lemma

Instantiate, from the original source masks, the complete `R=6000` realified
coefficient/jet map for this six-column block (including all injective visible
assignments and complete cancelled-prime sums), and prove that its
source-projected sixth wedge is nonzero at one admissible section in each
fixed-length/source-cell class to which the selector-free claim is applied.
Then the degree-24 result controls endpoint translations within that class.
If even this seed cannot be shown, determine whether the actual projected
wedge is identically zero. No smaller numerical coefficient statement can
decide `K_B` without these source entries. This is a precise matrix
instantiation/nonvanishing lemma, not the historical-selector problem.

## Verification

Run from the repository root:

```powershell
python src/wp84_block15_selector_free_wedge.py
python src/wp84_block15_selector_free_wedge_replay.py
```

The independent replay reconstructs the 14-coordinate generator and all
3,003 sixth-exterior basis states without importing the constructor; checks
the exact real/imaginary generator, the 9,504 transitions and grade range;
and rejects eight hostile mutations (wrong block or generator sign, false
degree, invented projection, invented `K_B`, false rank promotion, fabricated
source-mask implementation, and a fabricated dependency on the historical
selector). Both commands pass.
They verify the operator algebra and evidence boundary only, not the actual
source wedge. Machine-readable result:
`WP84_BLOCK15_SELECTOR_FREE_WEDGE_CERTIFICATE.json`.
