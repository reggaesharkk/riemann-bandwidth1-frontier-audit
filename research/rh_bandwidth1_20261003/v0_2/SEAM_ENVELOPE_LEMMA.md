# Seam-aware scalar envelope lemma

## Status

**MATHEMATICAL_COMPOSITION_PASS + CATALOG_IDENTITY_PASS**

This is the exact composition lemma used by the v0.2 A1294 certificate.
The upstream one-dimensional pieces and the finite five-dimensional tree are
separate proof layers.

## Lemma

Let (K:I	omathbb R) and let

[
I=[a,b]=igcup_{j=1}^{m} I_j,qquad
I_j=[x_{j-1},x_j],
]

where (a=x_0<x_1<cdots<x_m=b).

For each segment (I_j), suppose a finite nonempty family of functions
(L_{j,r}) is available with

[
L_{j,r}(x)le K(x)qquad(xin I_j).
]

Define

[
ell_j=max_rinf_{xin I_j}L_{j,r}(x),
qquad
ell=min_jell_j.
]

Then

[
K(x)geellqquad(xin I).
]

### Proof

Fix (xin I) and choose a segment (I_j) containing it. For every admissible
model (r),

[
K(x)ge L_{j,r}(x)geinf_{yin I_j}L_{j,r}(y).
]

Taking the maximum over (r) preserves the lower bound, hence
(K(x)geell_j). Since (ellleell_j), (K(x)geell).
QED.

No continuity between neighboring models is assumed.

## Exact implementation used by A1294

For every scalar partial-sum interval the checker:

1. clips at the exact cutoff (A/B);
2. inserts every exact catalog endpoint that lies inside the interval;
3. obtains atomic rational segments;
4. on each segment considers only catalog models whose certified domain
   contains that full segment;
5. evaluates each constant/quadratic segment infimum exactly with
   `fractions.Fraction`;
6. takes the maximum valid lower model on the segment;
7. takes the minimum over all segments.

For a convex quadratic lower well the exact infimum is evaluated at its center
when the center is inside the segment, otherwise at the nearest endpoint.
The segmented bound is used only when it improves on the available direct
single-piece model.

## Closed trust obligations

The earlier version of this note left catalog soundness as an open premise.
That premise has now been audited against the pinned upstream Lean source.

At upstream head
`fba91d214655aaa1fd0504bb893c8859c20c79f9`:

- all **56** stable JSON records match the Lean definitions;
- all **216** v1 records match;
- all **394** refinement2/v3 records match;
- total mismatches across **666** models: **0**;
- `improvedCatalog2_check` proves every corresponding Lean catalog entry
  passes its formal check;
- the upstream `MacroPiece.check_sound` chain turns those checks into the
  required one-dimensional pointwise lower bounds.

An exact structural audit at the A1294 cutoff also found:

- 598 distinct scalar boundaries;
- 597 atomic segments;
- 0 uncovered atomic segments;
- 0 uncovered boundary points;
- 0 parent-containment mismatches among refinements that declare stable owners
  (with the owner -1 [59,60] extension treated separately as designed).

Therefore the mathematical premise required by the seam-envelope lemma is
satisfied by the exact catalog used by the A1294 certificate.

## Evidence boundary

What is now established:

- mathematical seam composition: **PASS**;
- exact finite implementation/replay: **PASS**;
- all-666 JSON ↔ Lean identity: **PASS**;
- upstream one-dimensional soundness chain: **identified and matched**.

What remains optional but desirable for the strongest machine-checked release:

- port this segmented composition and the A1294 canonical finite tree into Lean
  and replay it in the kernel.

The current external certificate does not rely on a continuity assumption or
on interpolation across catalog seams.
