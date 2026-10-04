# A1294 release rights and DOI plan — 2026-10-04

## Release rule

Do not publish the DOI record until the source-free external replay is PASS and
its result/log are frozen.

## Rights posture

The repository root now contains:

- `LICENSE`: all rights reserved for original copyrightable material owned by
  Prince Upadhyay;
- `THIRD_PARTY_NOTICES.md`: explicit carve-out preserving all third-party
  licenses and provenance.

This is intentionally a mixed-rights repository.

The restrictive root notice **does not** relicense or override the upstream
Anthropic/Zeta23 material. Upstream files carrying Apache-2.0/SPDX notices
remain under those terms.

The rights notice also does not claim exclusive copyright in mathematical
facts, numerical results, theorem facts, ideas, methods, or algorithms where
copyright law does not create such rights.

## Zenodo deposit strategy

Use a **manual Zenodo software deposit** for the final immutable release ZIP,
rather than allowing a default GitHub archival flow to select a permissive
license automatically.

Zenodo permits custom licenses and mixed-license records.

For the final record:

- resource type: **Software** (with the technical note/preprint included inside
  the release bundle if desired);
- creator: **Upadhyay, Prince**;
- affiliation: **Independent Research**;
- version: the frozen release tag, e.g. `v0.2.0-a1294`;
- files: one preservation ZIP containing the exact release tree and
  reproducibility artifacts;
- primary custom rights title:
  **All rights reserved — Prince Upadhyay original contributions**;
- also declare **Apache-2.0** for included upstream files to which it applies;
- description must map the restrictive notice to original contributions and
  the Apache license to third-party material;
- preserve `THIRD_PARTY_NOTICES.md` and upstream notices inside the ZIP.

Zenodo metadata itself is CC0 under Zenodo policy; an all-rights-reserved file
license does not change the metadata license.

## DOI workflow

Zenodo can reserve a DOI before publication. The final sequence is:

1. finish source-free replay;
2. freeze result/log and final checksums;
3. create final release ZIP;
4. create a Zenodo draft;
5. reserve DOI;
6. add the reserved DOI to release metadata / citation files;
7. regenerate the final ZIP so the DOI is embedded;
8. verify final ZIP SHA-256;
9. upload final ZIP;
10. set custom/mixed rights exactly as above;
11. preview the record;
12. publish;
13. add the DOI badge/link back to GitHub;
14. tag the same immutable Git commit/release.

GitHub itself does not mint the research DOI. The Zenodo DOI is attached back
to the GitHub release/repository for citation.

## Title recommendation

**A1294: An Exact Seam-Aware Certificate in the Six-Translate
Montgomery–Taylor Zeta-Zero Framework**

This title deliberately avoids a global numerical-record claim.

## Public claim sentence

> We provide an independently replayed exact A=0.01294 certificate in the
> six-translate bandwidth-one / 666-model Montgomery–Taylor framework. With
> the pinned generic analytic bridge and conservative directed constants, the
> certificate supports the fixed coefficient 0.67280506. This advances the
> public A1293 external replay point within that certificate framework; it is
> not claimed as the largest numerical simple-critical-zero bound across all
> public computational constructions.

## No RH claim

The release must explicitly state that this result concerns a lower bound on
the proportion of zeros that are simple and on the critical line and is not a
proof of the Riemann Hypothesis.
