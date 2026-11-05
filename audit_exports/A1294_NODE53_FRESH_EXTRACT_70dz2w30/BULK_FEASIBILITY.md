# Bounded chunk feasibility: terminal 16 and node 53

## Measurement

| Module | Role | Source bytes | `.olean` bytes | wall time | peak RSS | major faults | exit |
|---|---|---:|---:|---:|---:|---:|---:|
| `Catalog16.lean` | source-selected block declarations | 6,881 | 452,616 | 92.83 s | 5,304,564 KiB | 168,979 | 0 |
| `Catalog16Identity.lean` | original-list / block-array identity | 9,919 | 52,704 | 78.14 s | 5,261,236 KiB | 165,410 | 0 |
| `Catalog16BoundaryBlocks.lean` | boundary/index transport | 1,067 | 30,976 | 30.20 s | 5,362,604 KiB | 81,749 | 0 |
| `Catalog16AllLookups.lean` | 166 original and local lookups | 100,961 | 1,221,656 | 32.17 s | 5,547,580 KiB | 91,069 | 0 |
| `Terminal16Compositional.lean` | 357 segments, 15 rows, tangent, acceptance | 310,586 | 12,473,880 | 240.65 s | 5,256,076 KiB | 177,049 | 0 |
| `Node53Replay.lean` | source-connected 15-node / eight-terminal chunk | 8,723 | 601,856 | 142.72 s | 5,287,912 KiB | 174,378 | 0 |

These are observed sequential builds in the pinned WSL project. Peak RSS is dominated by the imported Lean/Mathlib environment, not by the small replay source. The lookup and terminal modules also show that certificate-specific data creates sizable generated source and object files. No controlled cache-cold/warm study was run.

For context, the predecessor packet reports terminal-17 acceptance at 323,180 source bytes / 12,894,784 object bytes / 253.78 seconds / 5,282,856 KiB peak RSS, and node-55 replay at 8,306 / 597,864 / 95.25 seconds / 5,303,192 KiB. Terminal 18 was reported there at 312,061 / 12,403,104 / 82.65 seconds / 5,493,768 KiB. These runs are not controlled comparisons; they do not imply a scaling law. The node-53 result is an eight-terminal composition that imports the previously proved node-55 subtree.

## Architecture result

**Demonstrated in a bounded sample:** generated exact catalog blocks/lookups and segmented-row acceptance for an authentic quadratic terminal; reused proof objects and a generic replay transport to compose a complete small source subtree; Lean kernel accepted the result with only standard axioms.

**Not demonstrated:** a generic binary-stream parser proving the byte-to-literal conversion, a proof-producing catalog selector, compactness of all proof dependencies, predictable resource scaling, or feasibility for millions of nodes. The next credible improvement is a kernel-verified parser/selector bridge, not a larger manually enumerated replay. Full-certificate bulk verification remains OPEN.
