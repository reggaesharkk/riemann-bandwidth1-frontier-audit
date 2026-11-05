from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace

from a1294_seam_pilot import Checker, WEIGHTS, q, run_prefix

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
STABLE = DATA / "macro-data-exact.json"
V1 = DATA / "refinement-catalog-v1-exact.json"
V3 = DATA / "refinement-catalog-v3.json"

A = "1294/100000"
B = "1094977/5000000000"
GITHUB_NODES_PER_SEC = 1_000_000 / 1406.36


def split_box(box):
    weighted = [(hi - lo) * WEIGHTS[i] for i, (lo, hi) in enumerate(box)]
    axis = max(range(5), key=weighted.__getitem__)
    lo, hi = box[axis]
    mid = (lo + hi) / 2
    left, right = list(box), list(box)
    left[axis] = (lo, mid)
    right[axis] = (mid, hi)
    return tuple(left), tuple(right)


def make_subboxes(n=8):
    boxes = [tuple((F(0), F(60)) for _ in range(5))]
    while len(boxes) < n:
        # Split the first/current largest-volume box deterministically.
        idx = max(
            range(len(boxes)),
            key=lambda k: float(
                __import__("functools").reduce(
                    lambda a, b: a * b,
                    (hi - lo for lo, hi in boxes[k]),
                    F(1),
                )
            ),
        )
        box = boxes.pop(idx)
        left, right = split_box(box)
        boxes.extend([left, right])
    return boxes[:n]


def run_box(payload):
    box, max_nodes, stable, v1, v3 = payload
    checker = Checker(stable, v1, v3, q(A), q(B))
    stack = [(box, 0)]
    visited = leaves = tail = quadratic = max_depth = 0
    smallest = None
    started = time.monotonic()

    while stack:
        cur, depth = stack.pop()
        visited += 1
        max_depth = max(max_depth, depth)
        if visited > max_nodes:
            return {
                "status": "NODE_CAP",
                "visited": visited - 1,
                "pending": len(stack) + 1,
                "leaves": leaves,
                "tail": tail,
                "quadratic": quadratic,
                "maximum_depth": max_depth,
                "smallest_closed_margin": None if smallest is None else str(smallest),
                "elapsed_seconds": time.monotonic() - started,
            }

        margin = q(B) * sum((bounds[0] for bounds in cur), F(0)) - q(A)
        if margin >= 0:
            leaves += 1
            tail += 1
            smallest = margin if smallest is None else min(smallest, margin)
            continue

        margin = checker.lower(cur) - q(A)
        if margin >= 0:
            leaves += 1
            quadratic += 1
            smallest = margin if smallest is None else min(smallest, margin)
            continue

        left, right = split_box(cur)
        stack.append((right, depth + 1))
        stack.append((left, depth + 1))

    return {
        "status": "PASS",
        "visited": visited,
        "pending": 0,
        "leaves": leaves,
        "tail": tail,
        "quadratic": quadratic,
        "maximum_depth": max_depth,
        "smallest_closed_margin": None if smallest is None else str(smallest),
        "elapsed_seconds": time.monotonic() - started,
    }


def estimate(minutes_nodes_per_sec):
    if minutes_nodes_per_sec <= 0:
        return None
    return {
        "5M_nodes_minutes": 5_000_000 / minutes_nodes_per_sec / 60.0,
        "10M_nodes_minutes": 10_000_000 / minutes_nodes_per_sec / 60.0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--single-nodes", type=int, default=250_000)
    ap.add_argument("--parallel-nodes-per-box", type=int, default=40_000)
    ap.add_argument("--workers", type=int, default=min(6, os.cpu_count() or 1))
    ap.add_argument("--subboxes", type=int, default=8)
    args = ap.parse_args()

    for p in [STABLE, V1, V3]:
        if not p.exists():
            raise SystemExit(f"Missing required data file: {p}")

    print("=" * 72)
    print("A1294 LOCAL BENCHMARK")
    print("=" * 72)
    print("Python:", sys.version.replace("\n", " "))
    print("Platform:", platform.platform())
    print("Machine:", platform.machine())
    print("CPU logical count:", os.cpu_count())
    print("Requested workers:", args.workers)
    print("GitHub reference throughput: %.2f nodes/sec" % GITHUB_NODES_PER_SEC)
    print()

    # Exact single-process benchmark on the same full root.
    ns = SimpleNamespace(
        stable=str(STABLE),
        v1=str(V1),
        v3=str(V3),
        a=A,
        b=B,
        limit=60,
        max_nodes=args.single_nodes,
    )
    print(f"[1/2] Single-process exact run: {args.single_nodes:,} node cap...")
    t0 = time.monotonic()
    single = run_prefix(ns)
    wall_single = time.monotonic() - t0
    single_nps = single["visited"] / wall_single if wall_single else 0.0
    print("Single-process result:", single["status"])
    print("Visited:", f'{single["visited"]:,}')
    print("Wall seconds:", f"{wall_single:.3f}")
    print("Throughput:", f"{single_nps:.2f} nodes/sec")
    print("Vs GitHub:", f"{single_nps / GITHUB_NODES_PER_SEC:.2f}x")
    print()

    # Multiprocess throughput probe on deterministic subtrees.
    boxes = make_subboxes(args.subboxes)
    payloads = [
        (box, args.parallel_nodes_per_box, str(STABLE), str(V1), str(V3))
        for box in boxes
    ]
    print(
        f"[2/2] Parallel exact probe: {args.subboxes} subtrees, "
        f"{args.workers} workers, up to {args.parallel_nodes_per_box:,} nodes/subtree..."
    )
    t1 = time.monotonic()
    results = []
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(run_box, p) for p in payloads]
        for fut in as_completed(futures):
            results.append(fut.result())
    wall_parallel = time.monotonic() - t1
    total_parallel_nodes = sum(r["visited"] for r in results)
    parallel_nps = total_parallel_nodes / wall_parallel if wall_parallel else 0.0
    print("Parallel total visited:", f"{total_parallel_nodes:,}")
    print("Parallel wall seconds:", f"{wall_parallel:.3f}")
    print("Aggregate throughput:", f"{parallel_nps:.2f} nodes/sec")
    print("Vs GitHub:", f"{parallel_nps / GITHUB_NODES_PER_SEC:.2f}x")
    print()

    out = {
        "schema": "a1294-local-benchmark-v1",
        "candidate": {"A": A, "B": B},
        "machine": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "python": sys.version,
            "logical_cpu_count": os.cpu_count(),
        },
        "github_reference": {
            "nodes": 1_000_000,
            "seconds": 1406.36,
            "nodes_per_second": GITHUB_NODES_PER_SEC,
        },
        "single_process": {
            "requested_node_cap": args.single_nodes,
            "result": single,
            "wall_seconds": wall_single,
            "nodes_per_second": single_nps,
            "speedup_vs_github": single_nps / GITHUB_NODES_PER_SEC,
            "estimated_large_runs": estimate(single_nps),
        },
        "parallel_probe": {
            "workers": args.workers,
            "subboxes": args.subboxes,
            "node_cap_per_subbox": args.parallel_nodes_per_box,
            "results": results,
            "total_visited": total_parallel_nodes,
            "wall_seconds": wall_parallel,
            "aggregate_nodes_per_second": parallel_nps,
            "speedup_vs_github": parallel_nps / GITHUB_NODES_PER_SEC,
            "estimated_large_runs": estimate(parallel_nps),
        },
        "note": (
            "This is a speed benchmark and search probe, not a complete A1294 "
            "certificate. Exact Fraction arithmetic is used for acceptance."
        ),
    }

    results_dir = ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    outfile = results_dir / "A1294_LOCAL_BENCHMARK_RESULT.json"
    outfile.write_text(json.dumps(out, indent=2), encoding="utf-8")

    summary = results_dir / "A1294_LOCAL_BENCHMARK_SUMMARY.txt"
    summary.write_text(
        "\n".join(
            [
                "A1294 local benchmark",
                f"Single:   {single_nps:.2f} nodes/sec  ({single_nps / GITHUB_NODES_PER_SEC:.2f}x GitHub)",
                f"Parallel: {parallel_nps:.2f} nodes/sec  ({parallel_nps / GITHUB_NODES_PER_SEC:.2f}x GitHub)",
                f"Workers: {args.workers}",
                f"Machine: {platform.machine()}",
                "",
                "Send A1294_LOCAL_BENCHMARK_RESULT.json back to ChatGPT.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print("=" * 72)
    print("DONE")
    print("Result JSON:", outfile)
    print("Summary:", summary)
    print("=" * 72)


if __name__ == "__main__":
    main()
