# Proof-status ledger

## A1294 tail

Set `A = 647/50000` and `B = 1094977/5000000000`. Exact rational arithmetic gives

```text
60 B - A = 49931/250000000 > 0.
```

The pinned upstream lemma `sextupleEnergy_nonneg` proves `0 ≤ sextupleEnergy g`. Therefore,
for every `g : Fin 5 → ℝ` with `60 ≤ sextupleSpan g`, Lean proves

```text
A ≤ sextupleEnergy g + B * sextupleSpan g.
```

For nonnegative gaps, failure to belong to `initialGapBox 60 = [0,60]^5` implies span at
least 60. The pilot theorem `tail_covers_root_complement` formalizes this implication.
These results close only the region outside the root cube.

## Source tail leaf

The V2 streams have hashes:

- topology: `9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76`
- terminal kinds: `859e25cdff7379072c7a3928347b66dfbe762ff83c98035b0e3b591e9b533f06`
- anchors: `32e1264ab3c8350a31b9b8e1d260a16ef3ec82a71046378441f4f429dc4254f5`

The structural extractor identifies node 13,353,584 (zero-based) and leaf 6,676,785
(zero-based) as a tail terminal. Its path has 25 midpoint splits and reconstructs exactly
the box

```text
g0, g1, g3 ∈ [45/4, 105/8]
g2          ∈ [45/8, 15/2]
g4          ∈ [165/8, 45/2].
```

The lower endpoints sum to 60, so the exact tail margin is `49931/250000000`. Lean checks
the path-to-box equalities coordinate by coordinate, the upstream `affineTailCheck`, and
the one-terminal `checkAffineTree` stream with exact exhaustion. `selected_complete_subtree_sound`
then applies the upstream checker soundness theorem to this one-node subtree.

The source identity of that terminal is independently established by the included Python
extractor reading the hashed V2 streams and checking all weighted split-axis decisions on
the prefix through that node. The Lean kernel proof establishes the mathematics of the
translated leaf; it does not verify the SHA-256 algorithm or the entire preceding tree.

## Not established

- No A1294 quadratic terminal has been kernel-checked in this pilot.
- No Lean theorem consumes the 666 JSON catalog entries or proves their stable-owner
  refinement relation.
- No theorem checks the full topology, all anchors, all 6,725,258 quadratic terminals, or
  root-cube coverage.
- No global A1294 theorem, zero-density result, or RH statement follows from this pilot.
