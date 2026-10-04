# A1294 full exact certificate — final finite freeze

Status: **CERTIFIED_FINITE_EXACT**  
Claim boundary: **not yet a new published theorem; not RH**

## Result

The seam-aware full-domain certificate for

- A = 647/50000 = 0.01294
- B = 1094977/5000000000

closed exhaustively and independently replayed with exact rational arithmetic.

Directed density arithmetic:

`0.672805062698281008098221884193539254919846831626471836523602569541644813982154847287316312`

Gain over the public A1293 arithmetic point:

`1.123763481466361689604801487528...e-6`

## GitHub Actions proof run

- run: 37133363690
- head: `3b748a75ad619ee130c4fabd22792102ccbe986c`
- generate: **PASS**
- independent verifier: **PASS**
- final artifact: `a1294-seam-aware-full-certificate`
- artifact ID: `11286675906`
- downloaded artifact ZIP SHA-256:
  `11c1ab1820039284f60e492fe609f6a497175284acdd0c3c53d6ab62b8b1cd19`

## Exact certificate statistics

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

## Frozen inputs

- stable: `961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b`
- v1: `3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9`
- v3: `7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d`

## Canonical stream SHA-256

- anchors: `32e1264ab3c8350a31b9b8e1d260a16ef3ec82a71046378441f4f429dc4254f5`
- terminal kinds: `859e25cdff7379072c7a3928347b66dfbe762ff83c98035b0e3b591e9b533f06`
- topology: `9726eb31321c84dc22ae90f16bfe48a2fa57ff96ab404af644d33294951b8c76`

The downloaded final ZIP was independently rehashed after download; every listed member matches the committed `SHA256SUMS.txt`.

## Remaining theorem gates

1. Audit exact JSON ↔ Lean catalog identity and the upstream one-dimensional soundness chain.
2. Port/check the seam-aware scalar-envelope composition at the formal proof layer, or provide an equivalently rigorous audited bridge.
3. Re-audit the analytic implication from the affine sextuple inequality to the simple-on-critical-line proportion.
4. Perform a source-free independent full replay outside the generating CI environment.
5. Complete a fresh public-literature / repository novelty audit.
6. Only then freeze a release/preprint and invite external reproduction.

No claim of the Riemann Hypothesis is made.
