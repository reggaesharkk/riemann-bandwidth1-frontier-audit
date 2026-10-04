# Frontier reset: 67.350003708785593% — 2026-10-04

## Decision

The A1294 bandwidth-one sextuple route is no longer the numerical frontier.

A fresh public audit located a stronger strict finite-dimensional certificate released
with VeriLoop E2 / Libo Wang:

[
C_V=
rac{722547711262091300265625000000000}
     {1072825050442925667061714615173641}
=
0.67350003708785588766ldots
]

or

[
oxed{67.350003708785588ldots%}.
]

The repository displays this as **67.350003708785593%**.

This is the strongest public finite-dimensional certificate claim located in the
2026-10-04 audit. It is not treated here as an end-to-end Lean theorem or as
peer-reviewed community consensus.

## Comparison

| line | proportion | status used in this audit |
|---|---:|---|
| A1294, this repo | 0.67280506 fixed safe headline | exact finite certificate; lower numerical line |
| Devine Zenodo | 0.673399 | public preprint/certificate claim |
| Rakitin | 0.6734775921119 | public exact fusion claim with imported trust boundaries |
| VeriLoop E2 | **0.67350003708785588766...** | strongest located strict finite certificate claim |

Exact difference VeriLoop minus Rakitin:

[
rac{240795324620654333443434374437320095975721}
{10728250504429256670617146151736410000000000000}
approx 2.24449759559	imes10^{-5}.
]

## Independent exact assembly replay

Using only the public frozen constants

- q = 8
- m = 531
- eta = 1
- B = 93/23000
- H = 672167187145431 / 10^15
- R =
  1113172768314043426732876281699 /
  265625000000000000000000000000

the exact assembly formula

[
C=rac{mH-eta B(m-q)}{m-R}
]

reconstructs the published fraction exactly.

The script `src/frontier6735_exact_baseline.py` is an independent standard-library
Fraction replay of this scalar assembly. It does not verify the 190,375,830-node
local certificate; that is a separate trust layer.

## VeriLoop finite certificate structure

The public strict q=8 package reports:

- slope 1/2: epsilon = 526/78125, 23,644,472 nodes, PROVED;
- slope 19/20: epsilon = 9879/1250000, 75,294,070 nodes, PROVED;
- slope 1: epsilon = 20033/2500000, 91,437,288 nodes, PROVED;
- total: **190,375,830** strict B&B nodes;
- 327/327 difficult well boxes independently closed;
- exact rational R and C assembly PASS.

The public package explicitly leaves the full upstream analytic normalization/Lean bridge
as a separate unfinished layer.

## Where the next gain actually is

The public development history is unusually useful because it exposes the measured
bandwidth ladder:

- q=8 deterministic floating ceiling: about 0.673522454;
- q=9: about 0.673529201;
- q=10: about 0.673552660;
- q=12: about 0.673577795;
- q=13: about 0.673572287 (turnover).

The higher-q values are **not certificates**. Thin-sampling experiments at larger q were
explicitly rejected by the source project after missed minimizers inflated epsilon targets.

### Primary attack: tighten q=8 before climbing dimensions

The gap between the current strict q=8 result and its own reported deterministic q=8
ceiling is

[
0.673522454 - 0.67350003708785593
approx 2.2416912144	imes10^{-5}.
]

This is the best immediate target because:

1. the complete q=8 proof architecture already exists;
2. no new matrix theorem is needed;
3. the dimensional certification burden does not increase;
4. a gain can come solely from stronger rigorously certified local epsilon values,
   stronger terminal lower bounds, or a better q=8 window/pressure configuration;
5. the source project itself reports that node volume is not the dominant bottleneck:
   terminal-box proof precision is.

Therefore the first target is not q=12. It is:

[
oxed{C>0.67350003708785588766ldots}
]

with the smallest possible q=8 certificate change.

### Secondary attack

If q=8 tightening stalls, move to q=9 or q=10 with the same fail-closed discipline.
Do not use sparse multistart minima as theorem inputs.

## Non-negotiable kill gates

Any candidate above 0.673500037... is rejected unless it survives all of:

1. exact span-capacity identities;
2. nonnegative pressure/pair weights;
3. complete adversarial seed families, including the known three-level
   {1.04, 1.975, 2.915} structures;
4. independent terminal/well certification;
5. zero unresolved B&B boxes;
6. directed transcendental enclosures;
7. exact rational R and final C;
8. no duplicated spectral/residual credit;
9. explicit analytic normalization bridge;
10. source-free independent replay before release.

## Freeze rule

A1294 remains a certified infrastructure milestone, but no more compute is spent trying to
make it the numerical headline.

The active numerical frontier is now **67.350003708785593%** until a stronger public,
better-supported result is located or we certify one ourselves.
