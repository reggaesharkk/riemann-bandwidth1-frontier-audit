# Local terminal and search inventory

This inventory reconciles saved Windows terminal captures, ZIP results and JSON records from the previous forensic package. Historical large searches were not restarted. “Visited nodes” is not treated as “exhausted” when a pending frontier remains.

## Environment visible in recovered terminal screenshots

- Windows 11 ARM64, CPython 3.12.10, 8 logical CPUs, six requested workers.
- The A1294 local benchmark reported 683.09 nodes/s for the 250,000-node serial cap and 605.35 aggregate nodes/s for an 8-subtree/6-worker probe. Those are environment-specific diagnostics, not proof data.
- The historical local A1294 V2 replay record reports 18,897.781 seconds, 13,454,121 nodes, 6,727,061 leaves, maximum pending stack 55 and status PASS. The full traversal is not repeated here.

## Candidate-by-candidate status

| Candidate | Recovered local search | Exact point result | Classification |
|---|---|---|---|
| A1294 = 0.012940 | GitHub Actions certificate and saved local V2 source-free replay both record a full tree closure at 13,454,121 nodes / 6,727,061 leaves. | (V-A>0); witness does not contradict the bound. | **Finite catalog inequality closed in recorded certificate.** The expired original Actions ZIP was not recovered; the local V2 package is distinct and its manifest was checked. No full tree recomputation here. |
| A1295 = 0.012950 | Adaptive scan: 102,135 nodes; 143 pending. | (V-A>0). | **OPEN**, not a counterexample and not a certificate. |
| A1296 = 0.012960 | Adaptive scan: 102,815 nodes; 131 pending. Separate 5M diagnostic: 1,024 pending. | (V-A>0). | **OPEN**; both searches stopped with pending nodes. |
| A1297 = 0.012970 | Adaptive scan: 103,487 nodes; 145 pending. | (V-A<0). | **Exact pointwise counterexample** to the fixed-(B) catalog inequality; scan remains incomplete. |
| A1298 = 0.012980 | Adaptive scan: 104,178 nodes; 142 pending. | (V-A<0). | **Exact pointwise counterexample**; scan remains incomplete. |
| A1299 = 0.012990 | Adaptive scan: 104,828 nodes; 154 pending; full-root 1M scan: 1,055,320 nodes; 366 pending; fixed-(B) bracket closed only 80 hard-seed boxes. | (V-A<0). | **Exact pointwise counterexample**; no global full-root closure. |
| A12994 = 0.012994 | Full-root 1M scan: 1,041,970 nodes; 302 pending; fixed-(B) bracket closed only 80 hard-seed boxes. Original scripts/log encode `6497/500000`. | Corrected margin (V-A<0), as in the erratum. | **Exact pointwise counterexample**; no global full-root closure. |
| A1300 = 0.013000 | Full-root 1M scan: 1,066,433 nodes; 345 pending; fixed-(B) bracket closed only 80 hard-seed boxes. | (V-A<0). | **Exact pointwise counterexample**; no global full-root closure. |

## Execution evidence categories

- `A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip` is a complete stored replay package, not the original GitHub Actions artifact. Its package manifest covers its 14 members; the prior audit checked file lengths, SHA-256, ZIP CRC and three binary stream hashes. The package records `A=647/50000`, `B=1094977/5000000000`, status PASS and the node/leaf totals above.
- The old audit's exact point witness checker is intentionally included in its original form under `evidence/a1294_original_audit/verification/`. It is superseded by the new corrected checker.
- The `A1294_FULLROOT_BRACKET` source and terminal JSON are preserved. “80 hard seeds closed” is a bounded subtask, not a theorem over all starting boxes.
- The October screenshots show launch screens and one completed local benchmark; they are corroborating context. The packages' recorded terminal JSON/logs are the machine-readable source of counts.

The previous complete local/GitHub forensic ZIP is included as an untouched nested evidence file. Its SHA-256 is also listed in `SOURCE_HASH_INVENTORY.json`.
