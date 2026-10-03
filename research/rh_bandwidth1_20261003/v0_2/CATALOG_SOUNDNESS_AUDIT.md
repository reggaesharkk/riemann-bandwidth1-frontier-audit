# A1294 catalog soundness audit

## Scope

This note audits the one-dimensional lower-model layer used by the A1294
seam-aware five-dimensional search.  It does not establish the A1294 affine
certificate by itself.

## Pinned upstream

Repository: mdumitrean/zeta-23-lean
Commit: fba91d214655aaa1fd0504bb893c8859c20c79f9

Critical Lean blobs:

- Zeta23/ThmD/Sextuple/A1290/Catalog.lean
  blob a63e7ff07afc0b4433aa6c98d35236a615dcf298
- Zeta23/ThmD/Sextuple/A1290/RefinementData2.lean
  blob 31aa32eb7716a4b7e76ad852e4bcd4dea259fd07
- Zeta23/ThmD/Sextuple/Macro/Analytic.lean
  blob 187964fbb9833dd74e86410634532f63f876bb70

Frozen JSON inputs in this repository have SHA-256:

- stable 56-piece catalog:
  961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b
- v1 216 refinements:
  3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9
- v3 extension:
  7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d

## Formal soundness chain

The pinned upstream source defines a 666-model table:

- indices 0..55: stable macro pieces;
- indices 56..271: v1 refinement catalog;
- indices 272..665: second refinement table.

In A1290/Catalog.lean:

    theorem improvedCatalog2_check (i : Fin 666) :
      (improvedCatalog2 i).check = true

is proved by reduction to the previously checked stable/v1 catalog and
RefinementData2.

Macro/Analytic.lean proves:

    lemma MacroPiece.check_sound
      (hp : p.check = true)
      (hx : Holds p.box x) :
      p.model x <= abs (mtClosedForm x)

with the base and well cases delegated to the corresponding analytic
certificate soundness theorems.

Therefore, for every catalog entry whose Lean object agrees with the frozen
JSON parameters, the model is formally proved to lower-bound the target
one-dimensional kernel magnitude on its declared interval.

## Seam composition

Our v0.2 search sometimes partitions a scalar interval at exact catalog
boundaries and combines several certified models.  The elementary composition
lemma is recorded separately in SEAM_ENVELOPE_LEMMA.md.

Given individually sound pieces, taking on each segment the maximum of valid
lower models, followed by the minimum across segments, remains a valid lower
bound on the whole interval.

This seam-composition step is currently audited mathematically and by exact
Python replay; it is not yet ported into the upstream Lean tree layer.

## Remaining checks before theorem claim

1. Confirm byte/parameter identity between all 666 frozen JSON pieces and the
   corresponding Lean table entries.
2. Independently replay the 666 boolean checks or rebuild the relevant Lean
   catalog modules at the pinned commit.
3. Port or separately formalize the seam-envelope composition rule if a
   machine-checked finite certificate is desired.
4. Keep the catalog-soundness layer distinct from exhaustive five-dimensional
   tree coverage.

## Current classification

CATALOG_SOUNDNESS_SOURCE_CHAIN_IDENTIFIED

The catalog is not being treated as an unverified numerical fit.  The pinned
upstream formalization contains a theorem-level soundness chain for every
piece, subject to the remaining JSON-to-Lean identity/rebuild audit above.
