# Lean filesystem resource comparison

## Method

Pinned Lean 4.33.0-rc2/Lake environment, upstream and Mathlib revisions match `environment_pinned.log`. The same `ImportOnlyCatalog18.lean` and byte-identical `Catalog18AllLookups.lean` were built with the same imports and `-M6800`, timeout 150s. The WSL pinned Lake environment points at the same already-built upstream/Mathlib dependencies. Only the packet/source roots and copies of the exact imported catalog `.olean` files moved between `/mnt/c` and ext4. No Mathlib rebuild or cache flush was done. The ext4 stage hashes are in `stage_ext4.log`.

Initial read-only memory and filesystem state is in `memory_start.log`. All runs returned exit 0 and no swap; full `/usr/bin/time -v` logs are retained alongside this file.

## Measurements

| Module | Filesystem | Elapsed | User s | System s | Peak RSS KiB | Major faults | Exit |
|---|---|---:|---:|---:|---:|---:|---:|
| `ImportOnlyCatalog18` | `/mnt/c` | 2:15.69 | 6.32 | 39.04 | 5,347,572 | 174,395 | 0 |
| `ImportOnlyCatalog18` | ext4 | 1:12.60 | 3.81 | 14.60 | 5,429,432 | 72,692 | 0 |
| `Catalog18AllLookups` | `/mnt/c` | 2:00.37 | 10.98 | 26.38 | 5,487,320 | 162,792 | 0 |
| `Catalog18AllLookups` | ext4 | 1:30.63 | 10.46 | 18.17 | 5,333,036 | 140,189 | 0 |

An earlier same-task `/mnt/c` lookup build in `catalog_all_lookups.log` took 1:12.05, peak RSS 5,497,184 KiB, and 169,579 major faults. The new `/mnt/c` lookup build took 2:00.37. This run-to-run difference is large relative to the ext4 comparison.

## Decision

Resource optimization is **measured but inconclusive**. The single ext4 observations were faster than the new `/mnt/c` observations, but are not a controlled repeated/cold-cache comparison; the earlier `/mnt/c` lookup was faster than the ext4 run. Peak RSS likewise does not show a stable improvement. No performance benefit is claimed. Heavy imported Lean project state dominates memory (about 5.3–5.5 GiB peak) on both filesystems. The minimal `Init`-only generic array proof (1.90 s, 518,752 KiB, 1,389 major faults) remains a useful contrast but is a different import closure, not a filesystem A/B.
