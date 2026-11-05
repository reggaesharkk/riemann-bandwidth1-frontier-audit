# Mathematical decision record

## Decisions

| Label | Decision | Basis |
|---|---|---|
| `LOCAL_ORIGINALS_RECOVERED` | `YES_FOR_LOCAL_EVIDENCE; ORIGINAL_ACTIONS_ZIP_UNRECOVERED` | Nine screenshots, local packages, run logs, source files, result JSONs, snapshot archives, and V2 replay package are preserved. The original expired Actions artifact ZIP is not recovered. |
| `A1294_CI_REPLAY_STATUS` | `HISTORICAL_PASS_INDEPENDENTLY_RECORDED; ZIP_NOT_RECOVERED` | GitHub reports generate/verify jobs success; V2 package records and hashes independently checked; 18,897.781-second traversal not repeated. |
| `A1296` | `OPEN` | 5M diagnostic stopped with 1,024 pending; microscope covered 200. |
| `A1295` | `OPEN` | Adaptive diagnostic ended with 143 pending; no complete certificate or counterexample. |
| `A1297` | `COUNTEREXAMPLE_TO_FROZEN_CATALOG_INEQUALITY` | Exact rational witness is below .012970. |
| `A1298` | `COUNTEREXAMPLE_TO_FROZEN_CATALOG_INEQUALITY` | Exact rational witness is below .012980. |
| `A1299` | `COUNTEREXAMPLE_TO_FROZEN_CATALOG_INEQUALITY` | Exact rational witness has RHS below .012990. Historical runs were also incomplete. |
| `A12994` | `COUNTEREXAMPLE_TO_FROZEN_CATALOG_INEQUALITY` | Exact rational witness has RHS below .012994. Historical full-root run had 302 pending; fixed bracket was seed-only. |
| `A1300` | `COUNTEREXAMPLE_TO_FROZEN_CATALOG_INEQUALITY` | Exact rational witness has RHS below .013000. Historical full-root run had 345 pending; fixed bracket was seed-only. |
| `FROZEN_CATALOG_CEILING_VALIDITY` | `VALID_POINTWISE_UPPER_BOUND; SHARPNESS_OPEN` | The exact common-domain point limits any target A for the same global inequality to at most its RHS, approximately .01296158319578. No optimization proof is supplied. |
| `STRONGER_THAN_A1294_CERTIFICATE_FOUND` | `NO` | No complete certificate above A=.01294. Instead the exact point refutes candidates at/above .01297. |
| `NEW_MATHEMATICAL_INFORMATION` | `YES` | Independent exact catalog evaluation establishes the pointwise ceiling witness and five higher-target counterexamples. |
| `NEXT_COMPUTATION_JUSTIFIED` | `NO_BROAD_SEARCH` | Higher thresholds are already false for the frozen inequality; remaining .01295/.01296 cases have no complete closure and do not justify another broad run without a new proof plan. |

## Scope and limits

The A1294 source-free certificate concerns the fixed catalog inequality with its exact target and coefficients. The V2 replay record is independently checkable and its binary streams match the manifest. The original GitHub Actions artifact could not be downloaded because it had expired; no identical archive was found in either connected Drive collection. The local V2 ZIP is a different hash and is not represented as the GitHub ZIP.

The exact witness proves that a stronger fixed-catalog target cannot hold with these same catalogs and B. It does not show that the witness is the maximum, does not refute every possible new catalog or changed coefficient scheme, and does not itself establish a zero-density theorem. The q8 route, 68.820273% conditional route, strict greater-than-79% theorem, and RH remain separate and open/conditional according to their own proof records.

No proof claim is based solely on regression tests. The candidate counterexamples are exact rational evaluations at an admissible point.
