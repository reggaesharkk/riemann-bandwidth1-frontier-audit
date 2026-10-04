# A1294 full exact certificate — finite freeze v2

Status: **CERTIFIED_FINITE_EXACT + CATALOG_IDENTITY_PASS**  
Claim boundary: **not yet released as a new theorem; not RH**

## Finite certificate

The seam-aware full-domain certificate for

- A = 647/50000 = 0.01294
- B = 1094977/5000000000

closed exhaustively and independently replayed with exact rational arithmetic.

GitHub Actions run `37133363690`:

- generate: **PASS**
- independent verifier: **PASS**
- freeze/hash stage: **PASS**
- final verified artifact upload: **PASS**
- final artifact: `a1294-seam-aware-full-certificate`
- artifact ID: `11286675906`
- downloaded ZIP SHA-256:
  `11c1ab1820039284f60e492fe609f6a497175284acdd0c3c53d6ab62b8b1cd19`

Exact statistics:

- visited nodes: **13,454,121**
- leaves: **6,727,061**
- quadratic leaves: **6,725,258**
- tail leaves: **1,803**
- maximum depth: **80**
- full stack exhaustion: **true**
- generation time: **17,306.242381538 s**
- smallest exact quadratic margin:
  `33853157328150681621271330867899241 / 8192000000000000000000000000000000000000000000`
  ≈ `4.132465494159018684e-12`
- smallest tail margin: `49931/250000000`

## Directed analytic arithmetic — correction and conservative freeze

The first freeze note used the 20-decimal *lower* endpoint for pi in a place where
pi occurs with a negative coefficient. That direction is not suitable for a
rigorous lower bound. This v2 freeze corrects the arithmetic to Mathlib's
certified upper endpoint

[
pi < 3.14159265358979323847.
]

For the release-safe calculation we deliberately use the coarser
Lean-certified lower endpoint

[
HD(1) > 0.672500703679.
]

Together with A = 0.01294 and
B = 1094977/5000000000 this gives the exact rational lower bound

[
rac{201406213933795020896911983481}
     {299353000000000000000000000000}
=
0.6728050626978684726624152204287246160ldots
]

Therefore the fixed rational headline

[
oxed{0.67280506}
]

is below the directed lower bound with exact positive margin

[
rac{807615020896911983481}
     {299353000000000000000000000000}
=
2.6978684726624152204ldots	imes10^{-9}.
]

A finer stored HD lower rational gives the diagnostic value
`0.6728050626982810080982182263815...`, but it is not needed for the
publication-safe headline.

## Frozen inputs

- stable 56-piece table:
  `961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b`
- v1 216 refinements:
  `3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9`
- v3 394 refinements:
  `7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d`

All 666 JSON model definitions were compared field-by-field against the pinned
Lean definitions at upstream head
`fba91d214655aaa1fd0504bb893c8859c20c79f9`:

- stable 56: **56/56, zero mismatches**
- v1: **216/216, zero mismatches**
- v3: **394/394, zero mismatches**

## Canonical stream SHA-256

- anchors: `32e1264ab3c8350a31b9b8e1d260a16ef3ec82a71046378441f4f429dc4254f5`
- terminal kinds: `859e25cdff7379072c7a3928347b66dfbe762ff83c98035b0e3b591e9b533f06`
- topology: `9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76`

## Current proof boundary

Closed:

1. exhaustive five-dimensional coverage;
2. canonical certificate stream;
3. independent Fraction-only verifier;
4. frozen input and stream hashes;
5. exact replay of every terminal inequality;
6. all-666 JSON ↔ Lean parameter identity;
7. upstream theorem-level soundness chain for the pinned catalog models;
8. exact seam-envelope lemma at the mathematical level;
9. generic upstream analytic feedback/ledger chain identified for arbitrary A,B;
10. conservative directed arithmetic proving the fixed headline `0.67280506`.

Still required before the public theorem/release freeze:

1. source-free full replay outside the generating GitHub CI environment;
2. preferably a formal Lean integration/kernel replay of the seam-aware finite
   certificate (or an equivalently independently audited proof artifact);
3. final broad novelty/priority audit;
4. release packaging, rights notices, and DOI deposit.

No claim of the Riemann Hypothesis is made.
