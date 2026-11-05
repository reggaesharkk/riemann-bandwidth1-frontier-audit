# Additive erratum: exact A12994 target and all point margins

This erratum corrects the generated point-witness checker and derived table values in the predecessor audit. The predecessor ZIP, checker, outputs, manifests, and history are retained byte-for-byte in `evidence/a1294_original_audit/` and in the separately delivered prior audit ZIP.

## Exact witness

The frozen catalogs give the value
\[
V=\frac{1739674247820415045342527228267900485813207074499}
 {134217728000000000000000000000000000000000000000000}
 =0.01296158319577883963\ldots.
\]
The five-coordinate rational witness is
\[
g=\left(\frac{6912667}{1048576},\frac{6541989}{524288},
\frac{860015}{131072},\frac{13083885}{1048576},
\frac{6912651}{1048576}\right),\qquad \operatorname{span}(g)=\frac{46873301}{1048576}.
\]
With (B=1094977/5000000000), the span is below (A/B) for the tightest target (A=1294/100000), and below 60. The independent replay scans 56 stable, 216 v1 and 394 v3 catalog pieces at all 15 contiguous partial sums, using `Fraction` throughout.

## Correct targets and exact signed margins

Here the margin is (V-A). Positive means the point exceeds the candidate and is a counterexample to the same pointwise catalog inequality; negative means this point does not refute that candidate.

| Target | Exact (A) | Exact (V-A) | Decimal sign check |
|---|---:|---:|---:|
| A1294 | (647/50000) | `2896847500415045342527228267900485813207074499 / 134217728000000000000000000000000000000000000000000` | positive, (2.15831957788396\times10^{-5}) |
| A1295 | (259/20000) | `1554670220415045342527228267900485813207074499 / 134217728000000000000000000000000000000000000000000` | positive, (1.15831957788396\times10^{-5}) |
| A1296 | (81/6250) | `212492940415045342527228267900485813207074499 / 134217728000000000000000000000000000000000000000000` | positive, (1.58319577883963\times10^{-6}) |
| A1297 | (1297/100000) | `-1129684339584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | negative, (-8.41680422116037\times10^{-6}) |
| A1298 | (649/50000) | `-2471861619584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | negative, (-1.84168042211604\times10^{-5}) |
| A1299 | (1299/100000) | `-3814038899584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | negative, (-2.84168042211604\times10^{-5}) |
| A12994 | (12994/1000000=6497/500000) | `-4350909811584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | negative, (-3.24168042211604\times10^{-5}) |
| A1300 | (13/1000) | `-5156216179584954657472771732099514186792925501 / 134217728000000000000000000000000000000000000000000` | negative, (-3.84168042211604\times10^{-5}) |

## Defect location and impact

The generated checker used `Fraction(n, 100000)` for every integer in `(1294,1295,1296,1297,1298,1299,12994,1300)`, making its A12994 entry (0.12994) rather than (0.012994). The derived `exact_witness_result.json` and its normal/`-O`/`-OO` copies inherited that target. The candidate matrix also carried an incorrect A12994 margin; its A12994 target label was right but its margin came from the wrong scale. The A12994 line in the mathematical decision (“witness below .012994”) has the correct qualitative conclusion but did not give a correct numerical margin.

The original ceiling and full-root source code, the historical full-root output, and its launcher use the correct target (6497/500000). Thus the source error is in the later generated independent checker and report, not in the original local A12994 scan. Hashes in the predecessor manifest remain valid hashes of the bytes that were actually packaged; a hash does not certify the arithmetic interpretation.

## Scope

The witness refutes the fixed-(B) pointwise catalog inequality at A1297, A1298, A1299, A12994 and A1300. It does not prove that (V) is the global catalog optimum. It does not refute the A1294 finite certificate: its margin is positive. It does not establish a zero-density theorem without the separate source-to-consumer proof.
