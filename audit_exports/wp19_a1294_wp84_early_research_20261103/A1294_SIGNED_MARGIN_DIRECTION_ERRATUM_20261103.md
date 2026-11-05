# Additive erratum: direction of the signed margin

This sidecar corrects one sentence in `A1294_A1300_EXACT_ERRATUM.md`. The earlier file and the historical ZIP are retained unchanged.

For the stated pointwise inequality `A <= V`, the signed margin is `V - A`:

- `V - A > 0`: the inequality holds strictly at this point.
- `V - A = 0`: equality holds at this point.
- `V - A < 0`: the inequality fails at this point, giving a pointwise counterexample.

Thus the predecessor erratum's sentence saying that a positive margin is a counterexample, and that a negative margin does not refute the candidate, has both implications reversed. Applying the corrected sign to its exact table: A1294, A1295, and A1296 have positive margins and satisfy `A <= V` at this witness; A1297, A1298, A1299, A12994, and A1300 have negative margins and violate it at this witness. This is a pointwise classification only; it does not establish or refute any separate global extremal or analytic theorem beyond the stated inequality.

The separately recorded A1294 finite certificate and the exact higher-target pointwise counterexamples remain as recorded. This erratum changes no WP84 or R400 proof status.

## Provenance

Added as a separate audit note on 2026-11-03. No historical file, ZIP, manifest, source commit, or theorem inventory was edited.
