# Bounded bulk-generation feasibility

The terminal-17 generator produced the complete certificate-derived Lean data for 175 catalog references, 375 segment occurrences, and all 15 model rows from the reconstructed JSON. The proof method reuses generic catalog-array identity, lookup, segment, piecewise-row, tangent, and leaf-soundness lemmas; it does not hand-author each rational comparison. This is an existence demonstration for one more authentic segmented leaf and a bounded 13-node parent replay.

## Measurements available

| Module | Source bytes | `.olean` bytes | wall time | peak RSS | major faults | exit |
|---|---:|---:|---:|---:|---:|---:|
| terminal 18 compositional acceptance (predecessor) | 312,061 | 12,403,104 | 82.65 s | 5,493,768 KiB | 160,981 | 0 |
| terminal 17 compositional acceptance | 323,180 | 12,894,784 | 253.78 s | 5,282,856 KiB | 183,295 | 0 |
| node 55 replay module | 8,306 | 597,864 | 95.25 s | 5,303,192 KiB | 164,957 | 0 |

The terminal-18 run is the predecessor's original successful measurement; terminal 17 was built in this continuation. They are comparable in proof purpose and pinned environment, but not a controlled benchmark: cache state, process conditions, and exact term shape differ. The 0.49 MB object-size difference between the two leaf modules and the wall-time spread do not establish a stable scaling law. The node-55 `.olean` excludes the imported predecessor object closure; its 597,864 bytes are not the total dependency cost.

Catalog declaration/identity/lookups were also generated and proved in separate modules. The full 175-lookup module compiled with exit 0 in 112.89 s, peak RSS 5,534,272 KiB, and 154,946 major faults; its object is 1,289,480 bytes. Heavy Zeta23/Mathlib imports dominate memory (roughly 5.3–5.5 GiB in these runs).

## Decision

`AUTOMATIC_CERTIFICATE_DATA_GENERATION=DEMONSTRATED_FOR_TERMINAL17`.
`SMALL_AUTHENTIC_SEGMENTED_LEAF_SAMPLE=2` (terminals 17 and 18).
`FULL_CERTIFICATE_BULK_FEASIBILITY=OPEN`.

A chunked generator using the generic soundness and replay interfaces is credible as an architecture, but the measured sample is far too small to estimate throughput, total object size, peak memory, or full-certificate build feasibility. No full-tree run or extrapolation is made.

