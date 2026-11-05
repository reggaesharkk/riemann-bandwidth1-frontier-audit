from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from collections import deque, defaultdict
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
from fractions import Fraction as F
from pathlib import Path

# The existing benchmark package contains the exact checker and frozen inputs.
CHECKER = None
A_GLOBAL = None
B_GLOBAL = None
WEIGHTS = None

def q(x):
    return x if isinstance(x, F) else F(str(x))

def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def serialize_box(box):
    return [[fstr(lo), fstr(hi)] for lo, hi in box]

def deserialize_box(raw):
    return tuple((q(lo), q(hi)) for lo, hi in raw)

def split_box(box):
    weighted = [(hi - lo) * WEIGHTS[i] for i, (lo, hi) in enumerate(box)]
    axis = max(range(5), key=weighted.__getitem__)
    lo, hi = box[axis]
    mid = (lo + hi) / 2
    left, right = list(box), list(box)
    left[axis] = (lo, mid)
    right[axis] = (mid, hi)
    return axis, tuple(left), tuple(right)

def partition_root(limit: int, count: int):
    boxes = [(tuple((F(0), F(limit)) for _ in range(5)), 0)]
    while len(boxes) < count:
        # Split the shallowest/largest-weighted-width box deterministically.
        idx = max(
            range(len(boxes)),
            key=lambda k: (
                max((hi-lo)*WEIGHTS[i] for i,(lo,hi) in enumerate(boxes[k][0])),
                -boxes[k][1],
            ),
        )
        box, depth = boxes.pop(idx)
        _, left, right = split_box(box)
        boxes.append((left, depth+1))
        boxes.append((right, depth+1))
    return boxes

def init_worker(base_dir: str, A: str, B: str):
    global CHECKER, A_GLOBAL, B_GLOBAL, WEIGHTS
    base = Path(base_dir)
    sys.path.insert(0, str(base))
    from a1294_seam_pilot import Checker, WEIGHTS as W
    WEIGHTS = W
    A_GLOBAL, B_GLOBAL = q(A), q(B)
    CHECKER = Checker(
        base / "data" / "macro-data-exact.json",
        base / "data" / "refinement-catalog-v1-exact.json",
        base / "data" / "refinement-catalog-v3.json",
        A_GLOBAL,
        B_GLOBAL,
    )

def process_chunk(payload):
    # One exact branch-and-bound chunk. If the chunk does not close, its exact
    # dyadic frontier is returned to the coordinator for redistribution.
    box_raw, start_depth, node_cap = payload
    box = deserialize_box(box_raw)
    stack = [(box, start_depth)]
    visited = leaves = tail = quadratic = 0
    max_depth = start_depth
    smallest = None
    t0 = time.monotonic()

    while stack and visited < node_cap:
        cur, depth = stack.pop()
        visited += 1
        max_depth = max(max_depth, depth)

        margin = B_GLOBAL * sum((bounds[0] for bounds in cur), F(0)) - A_GLOBAL
        if margin >= 0:
            leaves += 1
            tail += 1
            smallest = margin if smallest is None else min(smallest, margin)
            continue

        margin = CHECKER.lower(cur) - A_GLOBAL
        if margin >= 0:
            leaves += 1
            quadratic += 1
            smallest = margin if smallest is None else min(smallest, margin)
            continue

        _, left, right = split_box(cur)
        stack.append((right, depth + 1))
        stack.append((left, depth + 1))

    return {
        "pid": os.getpid(),
        "visited": visited,
        "leaves": leaves,
        "tail": tail,
        "quadratic": quadratic,
        "max_depth": max_depth,
        "smallest_margin": None if smallest is None else [smallest.numerator, smallest.denominator],
        "frontier": [
            {"box": serialize_box(b), "depth": d}
            for b, d in stack
        ],
        "elapsed_seconds": time.monotonic() - t0,
        "scalar_cache_entries": len(CHECKER.scalar_cache),
    }

def run_candidate(base_dir: Path, A: str, B: str, workers: int,
                  budget: int, chunk_nodes: int, initial_boxes: int, limit: int):
    global WEIGHTS
    # Needed in coordinator for deterministic initial partition.
    sys.path.insert(0, str(base_dir))
    from a1294_seam_pilot import WEIGHTS as W
    WEIGHTS = W

    frontier = deque(
        {"box": serialize_box(box), "depth": depth}
        for box, depth in partition_root(limit, initial_boxes)
    )
    active = {}
    completed_nodes = 0
    leaves = tail = quadratic = 0
    global_max_depth = 0
    smallest = None
    worker_nodes = defaultdict(int)
    worker_seconds = defaultdict(float)
    worker_chunks = defaultdict(int)
    started = time.monotonic()
    chunks_done = 0

    with ProcessPoolExecutor(
        max_workers=workers,
        initializer=init_worker,
        initargs=(str(base_dir), A, B),
    ) as pool:

        def submit_one(item):
            payload = (item["box"], item["depth"], chunk_nodes)
            fut = pool.submit(process_chunk, payload)
            active[fut] = item

        # Prime all workers.
        while frontier and len(active) < workers * 2:
            submit_one(frontier.popleft())

        while active:
            done, _ = wait(tuple(active.keys()), return_when=FIRST_COMPLETED)
            for fut in done:
                active.pop(fut, None)
                res = fut.result()
                chunks_done += 1
                completed_nodes += res["visited"]
                leaves += res["leaves"]
                tail += res["tail"]
                quadratic += res["quadratic"]
                global_max_depth = max(global_max_depth, res["max_depth"])
                worker_nodes[str(res["pid"])] += res["visited"]
                worker_seconds[str(res["pid"])] += res["elapsed_seconds"]
                worker_chunks[str(res["pid"])] += 1

                if res["smallest_margin"] is not None:
                    m = F(*res["smallest_margin"])
                    smallest = m if smallest is None else min(smallest, m)

                for item in res["frontier"]:
                    frontier.append(item)

            # Keep workers fed until the global diagnostic budget is reached.
            while (
                frontier
                and len(active) < workers * 2
                and completed_nodes < budget
            ):
                submit_one(frontier.popleft())

            # Once budget is crossed, let already-running chunks finish but do
            # not schedule more. Their remaining frontiers are retained.
            if completed_nodes >= budget and not active:
                break

            # If nothing is active but frontier remains below budget, continue.
            if not active and frontier and completed_nodes < budget:
                while frontier and len(active) < workers * 2:
                    submit_one(frontier.popleft())

    wall = time.monotonic() - started

    # active is empty here. frontier is the exact unresolved diagnostic frontier.
    frontier_list = list(frontier)
    by_depth = defaultdict(int)
    for item in frontier_list:
        by_depth[str(item["depth"])] += 1

    deepest = sorted(frontier_list, key=lambda x: x["depth"], reverse=True)[:80]
    nps = completed_nodes / wall if wall else 0.0
    github_nps = 1_000_000 / 1406.36

    return {
        "A": A,
        "B": B,
        "diagnostic_status": "FULLY_CLOSED" if not frontier_list else "BUDGET_REACHED_WITH_FRONTIER",
        "visited": completed_nodes,
        "closed_leaves": leaves,
        "tail_leaves": tail,
        "quadratic_leaves": quadratic,
        "pending_frontier_boxes": len(frontier_list),
        "maximum_depth": global_max_depth,
        "smallest_closed_margin": None if smallest is None else fstr(smallest),
        "wall_seconds": wall,
        "aggregate_nodes_per_second": nps,
        "speedup_vs_github_reference": nps / github_nps if github_nps else None,
        "chunks_completed": chunks_done,
        "worker_stats": {
            pid: {
                "nodes": worker_nodes[pid],
                "chunk_cpu_seconds": worker_seconds[pid],
                "chunks": worker_chunks[pid],
            }
            for pid in sorted(worker_nodes)
        },
        "pending_depth_histogram": dict(sorted(by_depth.items(), key=lambda kv: int(kv[0]))),
        "deepest_pending_boxes": deepest,
        "note": (
            "Diagnostic adaptive exact search. Closed leaves use exact Fraction "
            "arithmetic. Pending boxes are not failures or counterexamples."
        ),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="Existing A1294_LOCAL_BENCHMARK_PACKAGE directory")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--chunk-nodes", type=int, default=5000)
    ap.add_argument("--initial-boxes", type=int, default=32)
    ap.add_argument("--budget-per-candidate", type=int, default=80000)
    ap.add_argument("--limit", type=int, default=60)
    args = ap.parse_args()

    base = Path(args.base)
    required = [
        base / "a1294_seam_pilot.py",
        base / "data" / "macro-data-exact.json",
        base / "data" / "refinement-catalog-v1-exact.json",
        base / "data" / "refinement-catalog-v3.json",
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit("Missing required existing benchmark files:\n" + "\n".join(missing))

    candidates = [
        ("1294/100000", "A1294"),
        ("1295/100000", "A1295"),
        ("1296/100000", "A1296"),
        ("1297/100000", "A1297"),
        ("1298/100000", "A1298"),
        ("1299/100000", "A1299"),
    ]
    B = "1094977/5000000000"

    out_dir = base / "results"
    out_dir.mkdir(exist_ok=True)

    print("=" * 78)
    print("A1294-A1299 ADAPTIVE FRONTIER SCAN")
    print("=" * 78)
    print("Machine:", platform.machine(), platform.platform())
    print("Python:", sys.version.replace("\n", " "))
    print("Workers:", args.workers)
    print("Chunk nodes:", args.chunk_nodes)
    print("Initial boxes:", args.initial_boxes)
    print("Budget/candidate:", f"{args.budget_per_candidate:,}", "nodes")
    print()

    all_results = []
    total_started = time.monotonic()

    for A, label in candidates:
        print("-" * 78)
        print(label, "A =", A)
        print("-" * 78)
        t0 = time.monotonic()
        res = run_candidate(
            base, A, B,
            workers=args.workers,
            budget=args.budget_per_candidate,
            chunk_nodes=args.chunk_nodes,
            initial_boxes=args.initial_boxes,
            limit=args.limit,
        )
        all_results.append(res)
        print("Visited:", f'{res["visited"]:,}')
        print("Pending frontier:", res["pending_frontier_boxes"])
        print("Max depth:", res["maximum_depth"])
        print("Throughput:", f'{res["aggregate_nodes_per_second"]:.2f}', "nodes/sec")
        print("Vs GitHub:", f'{res["speedup_vs_github_reference"]:.2f}x')
        print("Wall:", f'{res["wall_seconds"]:.2f}', "sec")
        print()

    total_wall = time.monotonic() - total_started

    report = {
        "schema": "a1294-a1299-adaptive-frontier-scan-v1",
        "machine": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "python": sys.version,
            "logical_cpu_count": os.cpu_count(),
        },
        "settings": {
            "workers": args.workers,
            "chunk_nodes": args.chunk_nodes,
            "initial_boxes": args.initial_boxes,
            "budget_per_candidate": args.budget_per_candidate,
            "limit": args.limit,
            "B": B,
            "github_reference_nodes_per_second": 1_000_000 / 1406.36,
        },
        "results": all_results,
        "total_wall_seconds": total_wall,
        "claim_boundary": (
            "This is a diagnostic frontier/complexity scan, not a complete "
            "certificate for any candidate unless that candidate reports FULLY_CLOSED."
        ),
    }

    outfile = out_dir / "A1294_A1299_ADAPTIVE_FRONTIER_RESULT.json"
    outfile.write_text(json.dumps(report, indent=2), encoding="utf-8")

    summary = out_dir / "A1294_A1299_ADAPTIVE_FRONTIER_SUMMARY.txt"
    rows = [
        "A1294-A1299 adaptive frontier scan",
        "",
        "A       visited   pending   depth   nodes/sec   vs GitHub",
    ]
    for r in all_results:
        rows.append(
            f'{r["A"]:<8} {r["visited"]:>8} {r["pending_frontier_boxes"]:>9} '
            f'{r["maximum_depth"]:>7} {r["aggregate_nodes_per_second"]:>11.2f} '
            f'{r["speedup_vs_github_reference"]:>10.2f}x'
        )
    rows += [
        "",
        "Send A1294_A1299_ADAPTIVE_FRONTIER_RESULT.json back to ChatGPT",
        "or upload/sync the results folder to Google Drive.",
    ]
    summary.write_text("\n".join(rows) + "\n", encoding="utf-8")

    print("=" * 78)
    print("DONE")
    print("Result:", outfile)
    print("Summary:", summary)
    print("Total wall seconds:", f"{total_wall:.2f}")
    print("=" * 78)

if __name__ == "__main__":
    main()
