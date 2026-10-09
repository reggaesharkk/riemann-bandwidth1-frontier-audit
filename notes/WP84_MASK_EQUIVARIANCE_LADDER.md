# WP84 mask-equivariance ladder

**Decision F — the prior 453 mask-component collapse omits the callback alias index.** No nontrivial callback equality is forced by the present source semantics. The exact real-part identity for conjugate pairs is valid, but it does not tie their Boolean callback values together. Even granting every old full-orbit covariance, the class-alias Boolean nodes have **1,148** components, not 453. The 453 count aggregates alias lists after dropping the callback's explicit `m` coordinate.

This audit starts at `0a4aade6900d2e4ed11cb534508461d0aeab0fad` on `codex/c5-c6-attack-20261006`. It does not search for the missing historical selector, change the frozen consumer, or estimate any prime sum. The strict `>79%` theorem remains **OPEN**.

## Source boundary and finite object

The frozen survivor census is 8,740 distinct raw sign/equality origins: 1,132 of degree five and 7,608 of degree six. Their table has 21,588 distinct `(raw origin,m)` pairs: 1,956 fifth-order and 19,632 sixth-order. The old quotient has 453 full-covariant origin functionals, each carrying a list of aliases.

The iterator in `src/wp84_fifth_full_pool_amplitude.py` receives a required external `source_mask` and calls it as

```text
source_mask(fid, slots, lag, T, section, m)
```

It consumes the return value as a truthiness filter. The checked-in project has no implementation of this callback, no exact slot-window predicate, and no executable selected-section rule. In particular, no source rule imposes equality between callback values on distinct six-tuples. A table callback that returns one on one key and zero on another is admitted by the executable call signature. This is an **interface counterexample** to covariance being forced by the code; it is not a counterexample to a yet-unwritten authentic source predicate.

The alias-index defect is directly visible in the checked-in source: `WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json` stores a list of aliases on each of the 453 representatives, while `iter_source_atoms` loops over that list and calls `source_mask(...,m)` separately for each alias. The older orbit catalogue then describes one real functional with all listed aliases inside its sum. Replacing that alias-indexed family of callback bits by a single functional bit is an extra identification; it is not implied by the D_b x C2 origin action.

The 21,588 class-alias pairs are the smallest finite Boolean-node refinement consistent with the displayed callback key, because `m` is a separate argument. The full actual key set is larger: at fixed `(T,I)` it also ranges over prime assignments and paths, and the source does not enumerate it because `source_mask` and the section rule are missing. The actual component count is `|K_T|` under literal key identity. At the reduced symbolic levels, the proved counts are 8,740 singleton raw origins or 21,588 singleton class-alias nodes; neither number purports to enumerate all actual callback keys.

## Generator audit

Here A–E classify the assertion that a transformation forces equality of mask bits. D means an explicit truthiness callback can distinguish its different arguments under the executable contract. E means the authentic source-mask symmetry cannot be decided because its predicate is absent. A coordinate relabeling is A only when it leaves the semantic six-tuple unchanged. A functional symmetry is recorded separately and never promoted to mask covariance.

| Transformation | Mask classification | Exact action and status |
|---|---|---|
| Literal same callback key | **A** | Identical `(fid,slots,lag,T,section,m)` is one bit by definition. This is already handled when duplicate atoms are added into `a_k`. |
| Equality-block labels renamed consistently | **A** | This only renames dummy variables. After canonical partition normalization and reassignment of the same physical primes, the ordered slot tuple is unchanged. This is not a physical slot permutation and identifies no distinct raw origin beyond the canonicalization already in the input. |
| Dummy prime-block labels renamed with all block data | **A** | Same coordinate-gauge argument: the physical slot primes, path, and callback tuple do not change. |
| Cyclic slot rotation | **D** for mask; complete unmasked path sum is a **functional symmetry** | Degree fixed; signs, equality labels, slots, and closed lag path rotate together; alias `m`, `T`, and section endpoints stay fixed; `lambda` stays fixed. In the full path sum, `W` acquires `exp(-2*pi*i*u_s*lambda/L)` and the root factor `K` contributes the compensating phase, with the root count unchanged. Thus `Re(WK)` is unchanged after reindexing the complete path sum. But canonical `fid` stays fixed and `slots`/`lag` generally change in the callback tuple, so an arbitrary callback can distinguish them. |
| Reversal with negative reversed lags | **D** for mask; complete unmasked path sum is a **functional symmetry** | Degree fixed; signs, equality labels, and slots reverse; `lag` maps to reverse order with each entry negated; `m`, `T`, section, and `lambda` remain fixed. Prefix extrema and the root kernel are unchanged. The identity `f_{-l}^epsilon(alpha)=exp(-2*pi*i*epsilon*l*alpha) f_l^epsilon(alpha)` cancels the reversed slot-start phase, hence the full `W` and `K` are preserved. The callback `slots`/`lag` tuple changes in general. |
| Simultaneous sign reversal/conjugation and `m -> -m` | **D** for mask; complete real correlation is a **functional symmetry** | Degree and equality partition fixed; signs and `lambda` reverse; slots, lag, `T`, and section stay fixed; `W,K` conjugate and `Re` is unchanged. On the canonical API, `fid` is an orbit representative while the callback receives the alias separately; `m` changes sign. The callback may distinguish it. The exact map from each nonrepresentative raw origin into API arguments is not separately implemented. |
| Carrier inversion alone | **D** | It is only a symmetry when combined with the preceding conjugation action. On its own it changes the source frequency/admission data. |
| Alias exchange `m -> -m` alone | **D** | It changes a callback argument and moves the alias-centered detuning condition. No callback equality follows. |
| Arbitrary physical slot permutation | **D** | No general permutation symmetry of the ordered path/root expression is certified. A callback can distinguish the ordered slots. The certified dihedral actions above are the only path transformations inherited here. |
| Negate Fourier displacements alone | **D** | The lag tuple changes; `W` and `K` need not be preserved. This is not the reversal action, which also reverses slot order and signs. |
| Translate/reindex dummy root-sum variable | **A** only as a reindexing | Root indices are computed after the callback and are not callback arguments. A valid dummy reindexing leaves the six-tuple identical and creates no new bit relation. |
| Swap repeated equal-prime slots physically | **D** in general | The corresponding slot-prime entries can agree numerically while lag positions and possibly the canonical origin change. Equal prime values do not impose equal callback bits. A complete source/window identity and a valid path symmetry would be needed. |
| Swap slots under a stipulated identical-window predicate | **B**, conditional only | If the *complete* admission predicate is invariant under this physical swap, then the callback values agree. Identical window factors alone do not prove that the trace/path functional is invariant. No such property is frozen in the current source. |
| Unspecified slot-window-intersection symmetry | **E** for the authentic source | The slot-window formula is missing. No particular intersection identity can be decided or used. The executable callback interface still permits different values on distinct keys. |
| Take a real part / conjugate pair | **C**, functional/algebraic only | For independent bits `x,y in {0,1}`, `Re(x*z+y*conj(z))=(x+y)Re(z)`. The scalar coefficients are equal, not opposite, but `x` and `y` remain independent. |

The complete-path rotation, reversal, and conjugation identities preserve the natural prime pool, every `R=6000` path after bijective reindexing, and the alias/detuning conditions as a set. Conjugation changes `delta` to `-delta`; the conditions on `|delta|` and the symmetric nearest-residual cell are unchanged. Rotation and reversal preserve `lambda` and hence preserve both the central `|delta|<=H/T` indicator and its complementary long-tail indicator. These facts prove the unmasked functional identities, not the missing window-admission covariance.

The formal raw group is `D_b x C2` with consistent dummy prime-label renaming. It is not a group of admissible source masks unless the source predicate is separately proved equivariant. The group action keeps degree fixed and acts on `(raw origin,m)`: cyclic rotation/reversal preserve `m`, while conjugation sends `m` to `-m`. `T` and supplied section endpoints are fixed. The real-part operation removes conjugation of `W K`, but does not remove changes to the callback tuple. The 453 canonical IDs do not define a separate source-mask argument for each raw origin; that origin-to-key map remains outside the checked-in implementation.

## Exact component counts and conditional ladder

No nontrivial cross-key equality edge is proved. On the 8,740-origin refinement, there are 8,740 singleton components, histogram `{1: 8740}`. On the callback-alias refinement, there are 21,588 singleton nodes, histogram `{1: 21588}`. The actual callback-key graph has one singleton for each distinct key in `K_T`; its size is not available from the missing predicate/section implementation.

The following are **conditional quotient counts**, obtained by independently closing the frozen origin set under the named algebraic actions. They are not proved mask components.

| Level | Added source property | Components | Component-size histogram | Status |
|---:|---|---:|---|---|
| 0 | No cross-key covariance; literal-key identity only | 21,588 | `1: 21,588` | Current finite origin-alias model |
| 1 | Consistent dummy-label gauge | 21,588 | `1: 21,588` | Already canonicalized; no additional merge |
| 2 | `P_conj`: source-admission invariance under conjugation and `m -> -m` | 10,794 | `2: 10,794` | Not proved |
| 3 | `P_conj` plus `P_rev`: source-window and section predicate invariant under reversed slots and negative reversed lag | 5,530 | `2: 266; 4: 5,264` | Not proved |
| 4 | Previous properties plus `P_cyc`: source-window and section predicate invariant under cyclic slot/lag rotation | 1,148 | `2: 7; 4: 10; 6: 44; 10: 79; 12: 290; 20: 58; 24: 660` | Conditional full action on `(origin,m)` |

For comparison, suppressing the alias coordinate gives the historical origin-only counts `8,740 -> 4,370 -> 2,237 -> 453`. This is a different quotient. The 453 origin functionals sum each representative's *whole alias list*; the callback call is made separately for every listed `m`, so the 453 count is not the Boolean component count for the specified key.

Independent subgroup cross-checks are included in the certificate for both node sets. On origins, cyclic rotations alone give 1,516; reversal alone 4,446; dihedral without conjugation 887; conjugation plus cyclic rotation 763. On `(origin,m)` nodes, cyclic rotations alone give 3,748; reversal alone 11,060; dihedral without conjugation 2,296; conjugation plus cyclic rotation 1,874. Exact size histograms are in the certificate. All alias-expanded counts are computed from the 21,588 frozen CSV rows.

The minimal missing mathematical statements can be expressed without asking for the old selector:

1. `P_conj`: on raw-origin nodes, simultaneous sign conjugation and `m -> -m` preserves the source admission bit. The corresponding mapping from the transformed raw origin to the current canonical `fid` callback tuple is not implemented. Keeping `fid`, slots, and lag literally fixed while changing only `m` is not the raw conjugation action on the carrier phase.
2. `P_rev`: on raw-origin nodes, reversal of signs/partition/slots together with negative reversal of lag preserves the source admission bit at fixed `m`. The source slot-window family and all endpoint/section tests must commute with reversal.
3. `P_cyc`: on raw-origin nodes, cyclic rotation of signs/partition/slots and lag preserves the source admission bit at fixed `m`. The indexed window family and source-section/root eligibility must commute with cyclic rotation.
4. `P_alias_merge`: reaching 453 would additionally require merging distinct alias-indexed bits inside each canonical functional's alias list. The exact alias windows are disjoint: if `m != m'`, then `|lambda-mL|<=H/T` and `|lambda-m'L|<=H/T` cannot both hold when `2H/T<|m-m'|L`. With `H/T<L/2` and distinct integer aliases, this holds eventually. Thus at any input admitted at one alias, the other alias bit must be zero. Alias aggregation into one bit is not a valid source property.

The first three are candidate properties, not inherited facts. On the alias-expanded census they lead to `21,588 -> 10,794 -> 5,530 -> 1,148`. Their origin-only projections are `8,740 -> 4,370 -> 2,237 -> 453`. The last 453 count is not reached on callback bits: it would require the invalid alias merge. A different subgroup ordering gives other intermediate counts, recorded in the JSON artifact.

## Real-part and coefficient compression

For an exact conjugate pair with unmasked scalar `a=Re(z)`,

```text
Re(x*z + y*conj(z)) = x*a + y*a = (x+y)*a.
sup_{x,y in {0,1}} (x*a+y*a) = 2*[a]_+ = [2*a]_+.
```

Thus the two formal coefficients are identical after the full path/prime reindexing. They are not opposite. The identity does not require `x=y`, and it gives no saving relative to the unrestricted support function: two independent bits with coefficient `a` contribute exactly `2[a]_+`. If two atoms have the exact same full callback key, they already occur in the coefficient `a_k`; no extra edge is needed. A pair of opposite coefficients attached to the same bit could cancel after exact same-key aggregation, but no additional origin-to-key census or such cancellation is supplied here. Distinct keys with opposite coefficients would instead have unrestricted support `[a]_+ + [-a]_+ = |a|`, not zero.

The actual exact key-pair classification is unavailable because the source does not enumerate `K_T` or implement the mask. At the formal complete-origin level the conjugate pair has equal real coefficient; whether the original caller would assign it the same bit is precisely the covariance question. No floating-point equality is used in any orbit or coefficient decision.

## Support theorem and budget status

With no proved off-diagonal mask relations, first combine all atom coefficients having the exact same callback tuple, as `a_k(T,I)`. Then

```text
S_T(chi) = sum_{k in K_T} chi_k a_k(T,I),
sup_{chi in {0,1}^{K_T}} S_T(chi) = sum_{k in K_T} [a_k(T,I)]_+.
```

In the 21,588-node class-alias refinement this is `sum_{(r,m)}[a_{r,m}]_+`; in the origin-only projection it is `sum_{r=1}^{8740}[a_r]_+`. If a proved source theorem later makes `chi` constant on components `C`, the exact formula becomes `sum_C [sum_{(r,m) in C} a_{r,m}]_+`. Full `D_b x C2` covariance gives 1,148 alias-expanded components, while 453 functionals arise only after additionally erasing the `m` index. Coefficient equality by itself does not change the formula.

The exact relaxed allowance remains

```text
Delta_relaxed = 52897896569489 / 572357731837500000,
Delta_relaxed / 201 = 52897896569489 / 115043904099337500000.
```

It is **UNPAID**. This structural audit proves no signed arithmetic saving and does not change the fifth analytic rank `38–72`. All prior gates, including source-normalization and zero-side obligations, remain open as previously recorded. Strict `>79%` remains **OPEN**.

## Reproducibility and hostile checks

Run from the repository root:

```powershell
python src/wp84_mask_equivariance_ladder.py
python src/wp84_mask_equivariance_ladder_replay.py
```

The builder pins hashes of the frozen survivor CSV, canonical functional ledger, source-mask identifiability certificate, and amplitude iterator. The replay independently reconstructs the origin action and subgroup counts. It also rejects 18 mutations: false cyclic/reversal/conjugation promotion; changed partition, slots, alias, `R`, or census; deletion of an origin; finite-core substitution; independent-bit merge or proved identity split; floating coefficient; diagnostic rows; invented selector; unconditional 453 claim; altered component counts or fifth/sixth signs; and omission of long-tail compatibility.

Artifacts:

- `notes/WP84_MASK_EQUIVARIANCE_LADDER_CERTIFICATE.json` — machine-readable transformation, census, graph, ladder, coefficient, and hostile-witness data.
- `src/wp84_mask_equivariance_ladder.py` — exact origin census and certificate builder.
- `src/wp84_mask_equivariance_ladder_replay.py` — independent orbit and mutation replay.
