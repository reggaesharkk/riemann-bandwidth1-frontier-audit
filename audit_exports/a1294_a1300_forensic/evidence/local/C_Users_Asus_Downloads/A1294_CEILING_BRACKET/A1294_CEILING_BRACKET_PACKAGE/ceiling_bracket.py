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

CHECKER = None
A_GLOBAL = None
B_GLOBAL = None
WEIGHTS = None

def q(x):
    return x if isinstance(x, F) else F(str(x))

def fstr(x):
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

def init_worker(base_dir, A, B):
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
        A_GLOBAL, B_GLOBAL
    )

def process_chunk(payload):
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

        margin = B_GLOBAL * sum((x[0] for x in cur), F(0)) - A_GLOBAL
        if margin >= 0:
            leaves += 1; tail += 1
            smallest = margin if smallest is None else min(smallest, margin)
            continue

        margin = CHECKER.lower(cur) - A_GLOBAL
        if margin >= 0:
            leaves += 1; quadratic += 1
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
        "frontier": [{"box": serialize_box(b), "depth": d} for b,d in stack],
        "elapsed_seconds": time.monotonic() - t0,
    }

def feedback_value(A_str, B_str):
    HD = F(1345001407358823291468759581606590377186806057252528157859,
           2000000000000000000000000000000000000000000000000000000000)
    PIU = F(157079632679489661923,50000000000000000000)
    A, B = q(A_str), q(B_str)
    c = (6*HD - 10*PIU*B)/(6-A)
    return c

def run_targeted(base, seed_boxes, A, B, workers, chunk_nodes, budget):
    global WEIGHTS
    sys.path.insert(0, str(base))
    from a1294_seam_pilot import WEIGHTS as W
    WEIGHTS = W

    frontier = deque(seed_boxes)
    active = {}
    visited = leaves = tail = quadratic = 0
    max_depth = 0
    smallest = None
    worker_nodes = defaultdict(int)
    chunks = 0
    t0 = time.monotonic()

    with ProcessPoolExecutor(
        max_workers=workers,
        initializer=init_worker,
        initargs=(str(base), A, B)
    ) as pool:

        def submit(item):
            fut = pool.submit(process_chunk, (item["box"], item["depth"], chunk_nodes))
            active[fut] = item

        while frontier and len(active) < workers*2:
            submit(frontier.popleft())

        while active:
            done, _ = wait(tuple(active), return_when=FIRST_COMPLETED)
            for fut in done:
                active.pop(fut, None)
                res = fut.result()
                chunks += 1
                visited += res["visited"]
                leaves += res["leaves"]
                tail += res["tail"]
                quadratic += res["quadratic"]
                max_depth = max(max_depth, res["max_depth"])
                worker_nodes[str(res["pid"])] += res["visited"]
                if res["smallest_margin"] is not None:
                    m = F(*res["smallest_margin"])
                    smallest = m if smallest is None else min(smallest, m)
                for item in res["frontier"]:
                    frontier.append(item)

            while frontier and len(active) < workers*2 and visited < budget:
                submit(frontier.popleft())

            if visited >= budget and not active:
                break
            if not active and frontier and visited < budget:
                while frontier and len(active) < workers*2:
                    submit(frontier.popleft())

    wall = time.monotonic() - t0
    pending = list(frontier)
    depth_hist = {}
    for item in pending:
        depth_hist[str(item["depth"])] = depth_hist.get(str(item["depth"]), 0) + 1

    return {
        "A": A, "B": B,
        "visited": visited,
        "closed_leaves": leaves,
        "tail_leaves": tail,
        "quadratic_leaves": quadratic,
        "pending": len(pending),
        "maximum_depth": max_depth,
        "smallest_closed_margin": None if smallest is None else fstr(smallest),
        "wall_seconds": wall,
        "nodes_per_second": visited/wall if wall else 0.0,
        "chunks": chunks,
        "worker_nodes": dict(worker_nodes),
        "pending_depth_histogram": depth_hist,
        "deepest_pending_boxes": sorted(pending, key=lambda x:x["depth"], reverse=True)[:80],
        "directed_density_if_certified": str(float(feedback_value(A,B))),
        "status": "FULLY_CLOSED_HARD_SEED" if not pending else "BUDGET_REACHED_WITH_FRONTIER"
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--chunk-nodes", type=int, default=5000)
    ap.add_argument("--budget", type=int, default=180000)
    args = ap.parse_args()

    base = Path(args.base)
    previous = base / "results" / "A1294_A1299_ADAPTIVE_FRONTIER_RESULT.json"
    if not previous.exists():
        raise SystemExit(f"Previous adaptive result not found: {previous}")

    prev = json.loads(previous.read_text())
    a1299 = next(r for r in prev["results"] if r["A"] == "1299/100000")
    seeds = a1299.get("deepest_pending_boxes", [])
    if not seeds:
        raise SystemExit("Previous A1299 result contains no deepest_pending_boxes")

    # Keep all recorded hard boxes, not just one branch.
    print("Loaded", len(seeds), "A1299 hard seed boxes from previous scan")

    B = "1094977/5000000000"
    candidates = [
        ("12990/1000000","0.012990"),
        ("12992/1000000","0.012992"),
        ("12994/1000000","0.012994"),
        ("12996/1000000","0.012996"),
        ("12998/1000000","0.012998"),
        ("13000/1000000","0.013000"),
    ]

    print("="*78)
    print("FIXED-B CEILING BRACKET: 0.012990 ... 0.013000")
    print("="*78)
    print("Machine:", platform.machine(), platform.platform())
    print("Workers:", args.workers, "chunk:", args.chunk_nodes, "budget/candidate:", args.budget)
    print("Hard seed boxes:", len(seeds))
    print()

    results=[]
    total0=time.monotonic()
    for A,label in candidates:
        print("-"*78)
        print("A =", label)
        r = run_targeted(base, seeds, A, B, args.workers, args.chunk_nodes, args.budget)
        results.append(r)
        print("Visited:", f'{r["visited"]:,}')
        print("Pending:", r["pending"])
        print("Max depth:", r["maximum_depth"])
        print("Throughput:", f'{r["nodes_per_second"]:.2f}', "nodes/sec")
        print("Status:", r["status"])
        print("Density if eventually certified:", r["directed_density_if_certified"])
        print()

    report = {
        "schema":"a1294-fixed-b-ceiling-bracket-v1",
        "source_previous_result":str(previous),
        "seed_source":"A1299 deepest pending boxes from prior adaptive scan",
        "seed_box_count":len(seeds),
        "settings":{
            "workers":args.workers,
            "chunk_nodes":args.chunk_nodes,
            "budget_per_candidate":args.budget,
            "B":B
        },
        "results":results,
        "total_wall_seconds":time.monotonic()-total0,
        "interpretation_boundary":[
            "This is a targeted complexity bracket on previously hard A1299 boxes.",
            "Failure to close under budget is not a counterexample.",
            "FULLY_CLOSED_HARD_SEED proves only closure of the recorded hard-seed subset, not the full [0,60]^5 domain.",
            "A full theorem still requires exhaustive full-domain certificate and independent verifier."
        ]
    }

    out = base/"results"/"A1294_FIXED_B_CEILING_BRACKET_RESULT.json"
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("="*78)
    print("DONE")
    print("Result:",out)
    print("Total wall:",f'{report["total_wall_seconds"]:.2f}',"sec")
    print("="*78)

if __name__=="__main__":
    main()
