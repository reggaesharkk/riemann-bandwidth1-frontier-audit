# Candidate matrix: A1294 through A1300

All targets use the frozen catalog and `B=1094977/5000000000`, unless noted. “Search result” describes the historical computational run. “Mathematical status” is the conclusion after the independent exact point check in `verification/verify_exact_witness.py`.

| Candidate A | Historical evidence | Exact witness comparison | Audit status |
|---:|---|---|---|
| .012940 | GitHub Actions source-free full certificate; V2 independent replay record PASS, 13,454,121 nodes | Witness value exceeds A by `2896847500415045342527228267900485813207074499 / 134217728000000000000000000000000000000000000000000` | `CERTIFICATE_PASS` (frozen-catalog inequality only) |
| .012950 | Adaptive local run: 102,135 nodes, 143 pending | Witness value exceeds A by `1554670220415045342527228267900485813207074499 / 134217728000000000000000000000000000000000000000000` | `OPEN`; no complete root certificate, no point counterexample |
| .012960 | Adaptive local run: 102,815 nodes, 131 pending; separate 5M run had 1,024 pending | Witness value exceeds A by `212492940415045342527228267900485813207074499 / 134217728000000000000000000000000000000000000000000` | `OPEN`; budget run is not closure |
| .012970 | Adaptive local run: 103,487 nodes, 145 pending | Witness value is below A by `1129684339584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | `COUNTEREXAMPLE` to the fixed-B catalog inequality |
| .012980 | Adaptive local run: 104,178 nodes, 142 pending | Witness value is below A by `2471861619584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | `COUNTEREXAMPLE` |
| .012990 | Adaptive local run: 104,828 nodes, 154 pending; 1M run: 1,055,320 nodes, 366 pending; fixed-B bracket closed 80 hard seeds | Witness value is below A by `3814038899584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | `COUNTEREXAMPLE`; hard-seed closure is not global closure |
| .012994 | 1M run: 1,041,970 nodes, 302 pending; fixed-B bracket closed 80 hard seeds | Witness value is below A by `15700577328499584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | `COUNTEREXAMPLE` |
| .013000 | 1M run: 1,066,433 nodes, 345 pending; fixed-B bracket closed 80 hard seeds | Witness value is below A by `5156216179584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | `COUNTEREXAMPLE` |

The point is

```text
g = (6912667/1048576, 6541989/524288, 860015/131072,
     13083885/1048576, 6912651/1048576)
span(g) = 46873301/1048576
E6_catalog(g) + B span(g)
  = 1739674247820415045342527228267900485813207074499
    / 134217728000000000000000000000000000000000000000000
  = 0.01296158319577883963…
```

The exact evaluator scans all 666 stable/refinement models from the three preserved JSON catalogs at each of the 15 contiguous partial sums. It requires all five coordinates positive and below 60. The span is below the tightest target cutoff `A/B = 64700000/1094977`, so the point is admissible for every row in the table.

Thus the witness is a necessary upper bound on any A satisfying the same pointwise global catalog inequality. It does **not** prove this is the optimum over the full domain. It also does not independently imply an analytic zero-density theorem; that requires the separately specified source-to-consumer implications.
