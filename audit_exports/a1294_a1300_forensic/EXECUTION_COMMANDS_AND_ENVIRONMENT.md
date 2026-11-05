# Execution commands and environment recovered from the launchers/logs

The commands below are transcribed from the copied launcher scripts. They document historical execution; they were not re-executed here. All launchers, logs, and result files remain preserved under `evidence/local/C_Users_Asus_Downloads/`. Do not rerun the batch launchers during this audit; they can recreate package directories.

## Common environment

- Screenshot and saved replay record: Windows 11 ARM64, CPython 3.12.10, 8 logical CPUs.
- Diagnostic launcher selected `py -3` when available; otherwise it fell back to `python`.
- Most diagnostic scans requested six workers and exact rational checker logic, but their saved outcomes are incomplete when `pending > 0`.
- The A1294 V2 replay record reports 18,897.781 seconds, 711.941841 nodes/s.

## Historical commands

The local benchmark launcher ran:

```text
benchmark_local.py --single-nodes 250000 --parallel-nodes-per-box 40000 --workers 6 --subboxes 8
```

The adaptive A1294–A1299 run ran:

```text
adaptive_frontier_scan.py --base <Downloads\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE> --workers 6 --chunk-nodes 5000 --initial-boxes 32 --budget-per-candidate 80000
```

The full-root A1299/A12994/A1300 diagnostic ran:

```text
fullroot_bracket.py --base <Downloads\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE> --workers 6 --chunk-nodes 10000 --budget 1000000 --initial-boxes 32
```

The A1296 diagnostic ran:

```text
a1296_5m.py --base <Downloads\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE> --workers 6 --chunk-nodes 10000 --budget 5000000 --initial-boxes 32
```

The V2 source-free replay launcher changed to its package directory and ran:

```text
replay_a1294_source_free.py --progress 250000
```

This V2 form deliberately omits `--package-root %~dp0`; the V1 form passed a quoted trailing-backslash path and failed on Windows. The V1 failure log and V1 package are included.

## Current audit checks

These are lightweight, standard-library-only checks included in this packet:

```powershell
python verification/verify_manifest.py
python verification/verify_packet.py
python verification/verify_exact_witness.py --output verification/exact_witness_result.json
python -O verification/verify_exact_witness.py
python -OO verification/verify_exact_witness.py
```

No A1295–A1300 search or five-hour certificate traversal was launched for this audit.
