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
    weighted = [(hi-lo)*WEIGHTS[i] for i,(lo,hi) in enumerate(box)]
    axis = max(range(5), key=weighted.__getitem__)
    lo,hi = box[axis]
    mid = (lo+hi)/2
    left,right = list(box),list(box)
    left[axis]=(lo,mid)
    right[axis]=(mid,hi)
    return axis,tuple(left),tuple(right)

def partition_root(limit,count):
    boxes=[(tuple((F(0),F(limit)) for _ in range(5)),0)]
    while len(boxes)<count:
        idx=max(
            range(len(boxes)),
            key=lambda k:max((hi-lo)*WEIGHTS[i] for i,(lo,hi) in enumerate(boxes[k][0]))
        )
        box,depth=boxes.pop(idx)
        _,left,right=split_box(box)
        boxes.extend([(left,depth+1),(right,depth+1)])
    return boxes

def init_worker(base_dir,A,B):
    global CHECKER,A_GLOBAL,B_GLOBAL,WEIGHTS
    base=Path(base_dir)
    sys.path.insert(0,str(base))
    from a1294_seam_pilot import Checker, WEIGHTS as W
    WEIGHTS=W
    A_GLOBAL,B_GLOBAL=q(A),q(B)
    CHECKER=Checker(
        base/"data"/"macro-data-exact.json",
        base/"data"/"refinement-catalog-v1-exact.json",
        base/"data"/"refinement-catalog-v3.json",
        A_GLOBAL,B_GLOBAL
    )

def process_chunk(payload):
    box_raw,start_depth,node_cap=payload
    box=deserialize_box(box_raw)
    stack=[(box,start_depth)]
    visited=leaves=tail=quadratic=0
    max_depth=start_depth
    smallest=None
    t0=time.monotonic()

    while stack and visited<node_cap:
        cur,depth=stack.pop()
        visited+=1
        max_depth=max(max_depth,depth)

        margin=B_GLOBAL*sum((x[0] for x in cur),F(0))-A_GLOBAL
        if margin>=0:
            leaves+=1; tail+=1
            smallest=margin if smallest is None else min(smallest,margin)
            continue

        margin=CHECKER.lower(cur)-A_GLOBAL
        if margin>=0:
            leaves+=1; quadratic+=1
            smallest=margin if smallest is None else min(smallest,margin)
            continue

        _,left,right=split_box(cur)
        stack.append((right,depth+1))
        stack.append((left,depth+1))

    return {
        "pid":os.getpid(),
        "visited":visited,
        "leaves":leaves,
        "tail":tail,
        "quadratic":quadratic,
        "max_depth":max_depth,
        "smallest_margin":None if smallest is None else [smallest.numerator,smallest.denominator],
        "frontier":[{"box":serialize_box(b),"depth":d} for b,d in stack],
        "elapsed_seconds":time.monotonic()-t0
    }

def run_candidate(base,A,B,workers,chunk_nodes,budget,initial_boxes,limit):
    global WEIGHTS
    sys.path.insert(0,str(base))
    from a1294_seam_pilot import WEIGHTS as W
    WEIGHTS=W

    frontier=deque(
        {"box":serialize_box(box),"depth":depth}
        for box,depth in partition_root(limit,initial_boxes)
    )
    active={}
    visited=leaves=tail=quadratic=0
    max_depth=0
    smallest=None
    worker_nodes=defaultdict(int)
    worker_chunks=defaultdict(int)
    t0=time.monotonic()

    with ProcessPoolExecutor(
        max_workers=workers,
        initializer=init_worker,
        initargs=(str(base),A,B)
    ) as pool:

        def submit(item):
            fut=pool.submit(process_chunk,(item["box"],item["depth"],chunk_nodes))
            active[fut]=item

        while frontier and len(active)<workers*2:
            submit(frontier.popleft())

        while active:
            done,_=wait(tuple(active),return_when=FIRST_COMPLETED)
            for fut in done:
                active.pop(fut,None)
                res=fut.result()
                visited+=res["visited"]
                leaves+=res["leaves"]
                tail+=res["tail"]
                quadratic+=res["quadratic"]
                max_depth=max(max_depth,res["max_depth"])
                worker_nodes[str(res["pid"])]+=res["visited"]
                worker_chunks[str(res["pid"])]+=1
                if res["smallest_margin"] is not None:
                    m=F(*res["smallest_margin"])
                    smallest=m if smallest is None else min(smallest,m)
                for item in res["frontier"]:
                    frontier.append(item)

            while frontier and len(active)<workers*2 and visited<budget:
                submit(frontier.popleft())

            if visited>=budget and not active:
                break
            if not active and frontier and visited<budget:
                while frontier and len(active)<workers*2:
                    submit(frontier.popleft())

    wall=time.monotonic()-t0
    pending=list(frontier)
    hist={}
    for item in pending:
        hist[str(item["depth"])]=hist.get(str(item["depth"]),0)+1

    return {
        "A":A,"B":B,
        "visited":visited,
        "closed_leaves":leaves,
        "tail_leaves":tail,
        "quadratic_leaves":quadratic,
        "pending":len(pending),
        "maximum_depth":max_depth,
        "smallest_closed_margin":None if smallest is None else fstr(smallest),
        "wall_seconds":wall,
        "nodes_per_second":visited/wall if wall else 0.0,
        "worker_nodes":dict(worker_nodes),
        "worker_chunks":dict(worker_chunks),
        "pending_depth_histogram":hist,
        "deepest_pending_boxes":sorted(pending,key=lambda x:x["depth"],reverse=True)[:120],
        "status":"FULLY_CLOSED" if not pending else "BUDGET_REACHED_WITH_FRONTIER"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--base",required=True)
    ap.add_argument("--workers",type=int,default=6)
    ap.add_argument("--chunk-nodes",type=int,default=10000)
    ap.add_argument("--budget",type=int,default=1000000)
    ap.add_argument("--initial-boxes",type=int,default=32)
    args=ap.parse_args()

    base=Path(args.base)
    if not (base/"a1294_seam_pilot.py").exists():
        raise SystemExit("Existing benchmark base not found: "+str(base))

    B="1094977/5000000000"
    candidates=[
        ("1299/100000","A1299"),
        ("6497/500000","A12994"),
        ("13/1000","A1300"),
    ]

    print("="*78)
    print("FULL-ROOT 1M BRACKET: A1299 / A12994 / A1300")
    print("="*78)
    print("Machine:",platform.machine(),platform.platform())
    print("Workers:",args.workers,"chunk:",args.chunk_nodes,"budget:",args.budget)
    print()

    results=[]
    total0=time.monotonic()
    for A,label in candidates:
        print("-"*78)
        print(label,"A =",A)
        r=run_candidate(
            base,A,B,args.workers,args.chunk_nodes,args.budget,args.initial_boxes,60
        )
        results.append(r)
        print("Visited:",f'{r["visited"]:,}')
        print("Pending:",r["pending"])
        print("Max depth:",r["maximum_depth"])
        print("Throughput:",f'{r["nodes_per_second"]:.2f}',"nodes/sec")
        print("Status:",r["status"])
        print()

    report={
        "schema":"a1294-full-root-million-bracket-v1",
        "machine":{
            "machine":platform.machine(),
            "platform":platform.platform(),
            "python":sys.version,
            "logical_cpu_count":os.cpu_count()
        },
        "settings":{
            "workers":args.workers,
            "chunk_nodes":args.chunk_nodes,
            "budget_per_candidate":args.budget,
            "initial_boxes":args.initial_boxes,
            "B":B
        },
        "results":results,
        "total_wall_seconds":time.monotonic()-total0,
        "claim_boundary":[
            "This is a capped full-root exact diagnostic, not a complete certificate unless status FULLY_CLOSED.",
            "A larger pending frontier or deeper maximum depth is complexity evidence, not a mathematical counterexample."
        ]
    }

    out=base/"results"/"A1294_FULLROOT_1M_BRACKET_RESULT.json"
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")

    print("="*78)
    print("DONE")
    print("Result:",out)
    print("Total wall:",f'{report["total_wall_seconds"]:.2f}',"sec")
    print("="*78)

if __name__=="__main__":
    main()
