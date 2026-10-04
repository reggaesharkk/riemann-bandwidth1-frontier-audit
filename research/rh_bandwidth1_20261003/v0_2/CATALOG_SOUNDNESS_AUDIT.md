# A1294 catalog soundness audit

## Status

**CATALOG_SOUNDNESS_IDENTITY_AND_SOURCE_CHAIN_PASS**

This note audits the one-dimensional lower-model layer used by the A1294
seam-aware five-dimensional certificate. It is deliberately separate from
the five-dimensional tree coverage itself.

## Pinned upstream

Repository: `anthropics/formal-math`  
Pinned head: `fba91d214655aaa1fd0504bb893c8859c20c79f9`

Critical Lean blobs:

- `zeta23/Zeta23/ThmD/Sextuple/A1290/Catalog.lean`
  blob `a63e7ff07afc0b4433aa6c98d35236a615dcf298`
- `zeta23/Zeta23/ThmD/Sextuple/A1290/RefinementData2.lean`
  blob `31aa32eb7716a4b7e76ad852e4bcd4dea259fd07`
- `zeta23/Zeta23/ThmD/Sextuple/Macro/Analytic.lean`
  blob `187964fbb9833dd74e86410634532f63f876bb70`

Frozen JSON SHA-256:

- stable 56-piece catalog:
  `961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b`
- v1 216 refinements:
  `3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9`
- v3 / refinement2 394 pieces:
  `7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d`

## Exact JSON ↔ Lean identity audit

All frozen model records were parsed and compared field-by-field against the
corresponding Lean definitions at the pinned upstream head.

Results:

| layer | JSON pieces | Lean definitions | mismatches |
|---|---:|---:|---:|
| stable | 56 | 56 | **0** |
| v1 refinement | 216 | 216 | **0** |
| v3/refinement2 | 394 | 394 | **0** |
| total | **666** | **666** | **0** |

Compared data include each piece's rational interval endpoints and all
model-defining rational parameters. For wells this includes side, q, v, m,
positivity and turn data; for base/barrier/zero pieces the corresponding
constant/cell data were checked.

The Python representation of a well is algebraically identical to the Lean
well model: the Lean form `2*(v + m*(q-x))^2` on the left (and its right-side
analogue) becomes a quadratic with center `q+v/m` (respectively `q-v/m`)
and coefficient `2*m^2`.

## Formal one-dimensional soundness chain

The pinned upstream source defines the full 666-model table as

- indices 0..55: stable macro pieces;
- indices 56..271: v1 refinements;
- indices 272..665: refinement2 pieces.

In `A1290/Catalog.lean`:

    theorem improvedCatalog2_check (i : Fin 666) :
      (improvedCatalog2 i).check = true

reduces the complete table to the already checked stable/v1 catalog and
`RefinementData2`.

The analytic layer proves soundness of every checked model. In particular,
`MacroPiece.check_sound` converts a successful Boolean certificate plus an
interval-membership hypothesis into the pointwise lower-bound statement for
the target Montgomery--Taylor kernel quantity.

Because the exact JSON parameters now match the exact Lean objects for all 666
entries, the search is no longer relying on an unverified fitted surrogate.

## Exact seam-domain structural audit

For A1294,

    cutoff = A / B = 64700000 / 1094977
           ≈ 59.08799910865708.

Taking every exact catalog endpoint inside [0, cutoff] gives:

- **598** distinct boundaries;
- **597** atomic open segments;
- atomic segments with no covering certified catalog model: **0**;
- boundary points with no covering certified catalog model: **0**.

All v1/v3 entries that declare a stable parent lie inside that parent's
declared interval: **0 parent-containment mismatches**. The 64 refinement2
entries with owner `-1` are the intentional extension over [59,60], not
parented stable pieces.

This matters because the seam-aware checker never needs to interpolate across
an uncovered scalar gap.

## Seam composition

The exact composition argument is recorded in `SEAM_ENVELOPE_LEMMA.md`.
On each atomic segment, the checker uses only models whose certified interval
contains the full segment, takes the strongest exact segment infimum available,
and then takes the minimum across segments.

The composition rule is mathematically sound given the one-dimensional
pointwise bounds established above. It is implemented with exact
`fractions.Fraction` arithmetic in the finite certificate verifier.

## What remains

The catalog-soundness/identity gate itself is closed.

Remaining higher-level obligations are:

1. source-free replay of the complete A1294 certificate outside the generating
   GitHub CI environment;
2. formal Lean integration/kernel replay of the seam-aware finite certificate
   if we want the entire new finite layer checked by Lean rather than by the
   independent exact verifier;
3. final theorem/release/novelty audit.

The five-dimensional certificate and the upstream one-dimensional soundness
chain remain distinct evidence layers even though both now agree on the exact
666 model parameters.
