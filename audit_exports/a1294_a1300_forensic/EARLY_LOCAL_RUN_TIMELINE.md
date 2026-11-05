# Early local run timeline — October 3, 2026

Times below use the Windows local clock shown in the screenshots (India Standard Time, UTC+05:30). Screenshots establish what a launcher displayed at the captured moment. A start screen alone is not evidence of completion; result JSONs and logs establish the saved diagnostic outcomes.

| Approx. time | Evidence | What it establishes |
|---|---|---|
| 18:34 | `Screenshot 2026-10-03 183441.png` | A1294 local benchmark launcher found the package, extracted it, and began the run. It says diagnostic only. |
| 18:41–18:48 | `184200.png`, `184823.png`, `184837.png` | Benchmark environment: CPython 3.12.10, Windows 11 ARM64, 8 logical CPUs; six workers requested. Single process reached its 250,000-node cap. Parallel probe visited 43,557 nodes across eight subtrees; seven closed and one hit its 40,000-node cap with 25 pending. This is throughput/budget evidence, not a full-root certificate. |
| 19:04 | `190426.png` | Adaptive A1294–A1299 launcher started; six workers and diagnostic-only notice. The saved result records all six targets stopping at `BUDGET_REACHED_WITH_FRONTIER`. |
| 19:16 | `191652.png` | Fixed-B ceiling bracket launcher started on A1299 hard boxes at A values .012990 through .013000. The saved source and JSON show the seed set was only the first 80 stored deepest boxes. |
| 19:27 | `192713.png` | Full-root 1M bracket launcher started for A1299, A12994, A1300. Saved results show all three reached their node budgets with nonempty frontiers. |
| 19:58 | `195820.png` | A1296 5M diagnostic launcher shows A=.012960, B=1094977/5000000000, six workers and a 5,000,000-node budget. |
| 20:20 | `202037.png` | The A1296 diagnostic console still displays the same target and runtime description. The JSON result, not this static screen, records the eventual stop at 5,057,564 visited nodes with 1,024 unresolved boxes. |

## Local diagnostic results

- A1294–A1299 adaptive run: respectively 101,527; 102,135; 102,815; 103,487; 104,178; and 104,828 visited nodes. Pending counts: 149, 143, 131, 145, 142, and 154. All six statuses are `BUDGET_REACHED_WITH_FRONTIER`.
- A1299/A12994/A1300 full-root 1M bracket: 1,055,320 / 1,041,970 / 1,066,433 nodes; 366 / 302 / 345 pending; all stopped with frontier.
- A1296 5M diagnostic: 5,057,564 nodes, 1,024 pending, depth 79, 1,852.687 seconds. The microscope examined only 200 of those 1,024 boxes.
- Fixed-B bracket: all six candidates closed the 80 selected hard-seed boxes. The result JSON explicitly limits that status to the seed subset, not `[0,60]^5`.
- The complete A1294 source-free V2 replay is separate evidence: 13,454,121 nodes, 6,727,061 leaves, status `PASS`, saved runtime 18,897.781 seconds.

The A1294–A1300 local result JSONs are preserved under `evidence/local/C_Users_Asus_Downloads/A1294_LOCAL_BENCHMARK/A1294_LOCAL_BENCHMARK_PACKAGE/results/`. The nine screenshots are preserved byte-for-byte under `evidence/screenshots/`.
