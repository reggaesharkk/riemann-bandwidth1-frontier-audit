# WP84 source-matched 26-term sign audit

**Decision: `BLOCKED_SOURCE_SEMANTICS_INCOMPLETE`.** The repository and the supplied package do not identify a genuine source-admissible balanced quadruple or instantiate its 26 source-selected connected weights. No source-matched counterexample is established. The exact positive reweighting witness below is only a logical countermodel. The unconditional greater-than-79% theorem remains open.

## Source revisions and hashes

The extracted task package names the source context as branch `codex/wp84-source-recovery-20261008`. Its HEAD is `be82c32cc00fce6d1c880ee5a4fe4a1300a194d1`. The six supplied document pins match that branch exactly. The later tracked source-audit snapshot searched for producer and selector implementations is branch `codex/c5-c6-attack-20261006`, HEAD `2caac1e6e4a8adfab7c74f87c805e6cd81d4f9a1`. The additive audit revision is branch `codex/wp84-source-mask-sign-audit-20261102`, based on that later snapshot. No remote operation was performed.

| Pinned source input | Git blob SHA-1 | Use in this audit |
|---|---|---|
| `notes/WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md` | `3f42b46baa727f5c13c244b9b20f18854a0cb030` | Exact overlap and finite Dirichlet trace |
| `notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md` | `5c0fa1e59c7bd398d20677d26d03b03497d7062f` | Exact nonclosed balanced overlap sign |
| `src/wp84_phi4_balanced_nonclosed_nonpositive.py` | `d11a21c4492135e7247c482efe48abe0ef0c3c3b` | 26-term construction and rational arrangement checker |
| `notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md` | `9ff0fd5ba59969ccd58aab28a0f9c3c489992c58` | Short-shift safe-lobe implication |
| `src/wp84_e2_shift_range_safe_lobe.py` | `4741f932c7fade6229d1f2a35447644a5440c7a9` | Floating regression for the safe-lobe calculation |
| `notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md` | `e48bb9871fbc4f9a4f320fa2b796d3a6a188d64f` | Exact 6/24/8 orientation normalization |

All 22 repository inputs used by the audit have both Git blob IDs and SHA-256 values in [`WP84_SOURCE_MATCHED_26_TERM_SIGN_AUDIT.json`](../evidence/WP84_SOURCE_MATCHED_26_TERM_SIGN_AUDIT.json). The task-package manifest was also verified: SHA-256 `e8389181a9cbfd40be3e247a36ab07bc03fd29203b09d2263eb95e4f9e57f4a7`, nine files verified.

## What the frozen formula establishes

The continuous trace note defines the word positions, net displacement (Y), spread (R), overlap ((L-R)_+/L), and normalized trace

\[
K_T(Y)=e^{iTY}D_d(Y/L),\qquad D_d(s)=d^{-1}\sum_{k=0}^{d-1}e^{2\pi i k s}.
\]

These are exact identities, including for nonclosed words; the terminal endpoint (Y) is retained in the nonclosed path. The real fourth-order contribution uses `Re K_T(Y)`, so the complex carrier and conjugation cannot be discarded. See pinned `notes/WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md` lines 13–42, 53–85, and 88–96; the nonclosed construction explicitly appends (Y) in `src/wp84_phi4_balanced_nonclosed_nonpositive.py` lines 44–58.

The 26 combinatorial terms are the ordered set-partition expansion: for a partition with (k) blocks, fix the first block to contain label 0, order the other blocks in ((k-1)!) ways, and attach coefficient ((-1)^{k-1}(k-1)!) before expanding that coefficient into ordered terms. The term counts by (k=1,2,3,4) are (1,7,12,6), with signs (+,-,+,-). The exact compiler is in the pinned `src/wp84_phi4_balanced_nonclosed_nonpositive.py` lines 26–42. The seven two-block terms contain three (2+2) pairings and four (1+3) splits. The three pairings are the entire fourth-cumulant pairing subtraction only if the four source factors are centered; the actual source centering rule is not identified here.

For the formula-level balanced sector, the six, 24, and eight orientation ledgers agree after their stated normalization:

\[
C_{24}=4C_6=C_8,\qquad C_6/2=C_8/8.
\]

The pinned orientation note gives the fixed-scale kernel (C_8/8=-(s-1)\min(d_s(x),d_s(y))), and its checker verifies all identities with rational arithmetic (`notes/WP84_BALANCED_ORIENTATION_NORMALIZATION.md` lines 41–96; `src/wp84_balanced_orientation_normalization.py` lines 10–30 and 50–66). This is an aggregate identity for the fixed-scale formula. It does not prove source-selected equality of term masks or weights.

The pinned nonclosed theorem proves (B_{4,nc}(v)\leq0) in the balanced two-positive/two-negative sign sector on common-first-walk support, without assuming (Y=0) (`notes/WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVITY.md` lines 15–40 and 44–72). Its exact arrangement checker has 45 hyperplanes and 327 rational vertices, and its acceptance test is exact (`src/wp84_phi4_balanced_nonclosed_nonpositive.py`). A common nonnegative scalar preserves this sign. This does not establish that the actual source puts one common scalar on all 26 terms.

For (L\geq1,T\geq12), the safe-lobe note proves

\[
|Y|\leq\pi/(3T)\quad\Longrightarrow\quad \operatorname{Re}K_T(Y)\geq0.
\]

On a product block (M<m,n\leq2M), the short range (|h|=|n-m|\leq M/T) implies (|Y|=|\log(m/n)|\leq-\log(1-1/T)<\pi/(3T)) (`notes/WP84_E2_SHIFT_RANGE_SAFE_LOBE.md` lines 99–136 and 143–186). Thus the formal balanced overlap contribution has nonpositive sign in that range, conditional on applying the balanced source expression.

For the diagonal (Y=0), (K_T(0)=1). The equal-product-scale connected kernel has the exact negative Brownian covariance representation (`notes/WP84_PHI4_EQUAL_SCALE_BROWNIAN_KERNEL.md` lines 38–49 and 87–137). In addition, the fixed-scale six-interleaving kernel combined with the positive semidefinite finite-trace Gram matrix gives a nonpositive connected quadratic form across all Dirichlet lobes (`notes/WP84_FIXED_SCALE_CONNECTED_KERNEL.md` lines 48–68 and 127–179). Unequal-scale source-selected consumption still needs an exact source mapping and a bounded perturbation argument.

## Source provenance stops before the 26 source weights

The later tracked candidate constructor `src/wp84_fifth_full_pool_amplitude.py` is a five-slot symbolic constructor, not an evaluated source matrix. Its `source_amplitude_entry` returns a summand schema and takes the section, carrier, and prime pool as inputs (lines 34–46). The atom iterator requires `source_mask` as an external argument (lines 73–80), calls it as a truthiness filter over aliases (line 96), and constructs root endpoints and the normalized expression only afterward (lines 98–114). The producer has no local callback implementation, no caller in tracked source, and no rule that selects the endpoints. The project helper `q_mask` only handles a specialized canceled-prime domain and takes the carrier-alias-admissibility Boolean as already supplied (`src/wp84_source_q_mask_extractor.py` lines 24–46); it cannot fill the missing full atom predicate.

The independent current-tree semantic reconstruction records that the original slot-window intersections, deterministic (T\mapsto(k_-(T),k_+(T))) rule, source row identities/order, and jet-to-row map are absent (`notes/WP84_BLOCK15_SOURCE_MASK_SEMANTIC_RECONSTRUCTION.md` lines 90–121 and 123–140). The audit replay independently checked tracked source at `2caac1e...` and reachable local history (871 commits at audit start): no tracked callback definition or iterator call site was found; no matching callback definition occurred in reachable Python history; no candidate section selector occurred in the candidate-module history search. The exact history search and all input hashes are recorded in the evidence JSON.

Some five-slot schema fields are specified symbolically, including slot coefficients, filters, carrier phase, alias list, root interval, and normalization. Those values cannot be transplanted into a four-slot connected source sum without a source-authentic map from the theorem-side matrix entry to these terms. Accordingly the 26-row register in the JSON is **model-only**: it records the ordered-partition structure and exact logical overlaps while setting every source eligibility, prime coefficient, carrier/phase, endpoint/normalization, and source weight field to `null`. Null means unknown; it is not a zero row and is not a positive row.

No source-admissible quadruple can be selected from the repository. Ordering dependence of actual masks, orientation-by-state changes, cutoff transitions, outer-lobe row weights, and the source pairing subtraction therefore cannot be tested. Fixed sections and toy masks were not substituted for source-selected sections.

## Exact logical countermodel, not a WP84 counterexample

An independent `Fraction` replay uses shifts

\[
(1/6,-1/6,11/12,-11/12),\qquad Y=0.
\]

The common first overlap is (1/12), and the unweighted 26-term bracket is exactly (-1/12), so their product is (-1/144). A common positive factor (7/3) leaves the bracket at (-7/36) and product at (-7/432). If the first model term receives weight 1 and the other 25 receive weight (1/100), every model weight is strictly positive but the reweighted bracket is (1187/1200>0), with product (1187/14400). All values are exact rationals.

This proves only that termwise nonnegative weights do not, by themselves, preserve this model cancellation. The witness is not generated by the actual WP84 selector, and the source does not permit it to be called a source counterexample.

The replay also has exact negative controls:

- changing the model weights produces the positive logical witness;
- deleting one of the eight alternating orientations breaks the exact normalized identity;
- a Gaussian-rational finite-trace example rejects omitting conjugation;
- changing the candidate selector/filter bytes fails the source hash pin, and changing the evidence to assert an invented mask fails the claim-boundary validator.

## Required gates

| Gate | Result | Reason |
|---|---|---|
| `SOURCE_MASK_RECONSTRUCTED` | `BLOCKED_SOURCE_SEMANTICS_INCOMPLETE` | No executable source callback or source-selected section/row predicate |
| `CONNECTED_WEIGHT_FACTORIZATION` | `BLOCKED_SOURCE_SEMANTICS_INCOMPLETE` | No source link showing a common factor or exact source-matched cancellation across the 26 terms |
| `SAFE_LOBE_SOURCE_SIGN` | Formal conditional sign proved; source match blocked | Exact balanced sign and short-lobe implications apply once the source sum is identified |
| `OUTER_LOBE_CONTROL` | Exact on common product scale; unequal-scale source consumer open | Fixed-scale PSD identity is exact; the source-selected off-diagonal sum is uninstantiated |
| `DIAGONAL_PAIR_MATCH` | Formal (Y=0) kernel exact; source row match blocked | (K_T(0)=1) and the fixed-scale kernel is negative semidefinite, but row/weight identity is absent |
| `FULL_BOUNDED_CONSUMER` | `OPEN` | No complete source-matched bounded sum and outer-lobe consumer |
| `UNCONDITIONAL_GT79` | `OPEN` | No theorem closure or source-matched counterexample |

## Minimal exact input needed to resume

1. An immutable, source-authentic theorem-side matrix-entry producer: repository commit/blob or contemporaneous generator with its exact inputs.
2. A deterministic row and section selector giving ordered row IDs and inclusive ((k_-(T),k_+(T))) endpoints for every admitted (T), including cutoff-transition and tie rules.
3. An executable per-term eligibility predicate covering prime and prime-power domains, all slot-window intersections, equality and distinctness, carrier and alias residual, orientation, path, root endpoints, and row identity.
4. The exact fourth-order expansion from each matrix entry through all 26 ordered partitions, including complex phases, conjugation, multiplicities, centering, pairing subtraction, and normalization.
5. The exact coefficient formula for every retained prime or prime power and a proof that the supplied pool is complete.

Prose that names these predicates without the original definitions, exact row selector, and source mapping is insufficient to reconstruct the selected weights. No mask has been invented in this audit.

## Replay and verification

From the repository root:

```powershell
python -B src/wp84_source_matched_26_term_sign_replay.py
python -B -m unittest discover -s tests -p 'test_wp84_source_matched_26_term_sign.py' -v
```

The audit ran the supplied package verifier and its seven tests; the independent audit tests also pass seven cases. The pinned exact nonclosed arrangement checker, fixed-scale kernel checker, and 3,395-point orientation checker pass. The safe-lobe script passes its 300-point seeded floating regression; the analytic safe-lobe proof is the pinned note, not that floating sample. The replay labels exact finite arithmetic, formal proof inputs, floating checks, and the abstract model separately in the evidence JSON.
