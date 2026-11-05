from __future__ import annotations
import argparse, json, os, platform, sys, time
from collections import deque, defaultdict
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
from fractions import Fraction as F
from pathlib import Path

CHECKER=None
A_GLOBAL=None
B_GLOBAL=None
WEIGHTS=None

def q(x): return x if isinstance(x,F) else F(str(x))
def fstr(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def serialize_box(box): return [[fstr(lo),fstr(hi)] for lo,hi in box]
def deserialize_box(raw): return tuple((q(lo),q(hi)) for lo,hi in raw)

def split_box(box):
    weighted=[(hi-lo)*WEIGHTS[i] for i,(lo,hi) in enumerate(box)]
    axis=max(range(5),key=weighted.__getitem__)
    lo,hi=box[axis]; mid=(lo+hi)/2
    left,right=list(box),list(box)
    left[axis]=(lo,mid); right[axis]=(mid,hi)
    return axis,tuple(left),tuple(right)

def partition_root(limit,count):
    boxes=[(tuple((F(0),F(limit)) for _ in range(5)),0)]
    while len(boxes)<count:
        idx=max(range(len(boxes)),
                key=lambda k:max((hi-lo)*WEIGHTS[i] for i,(lo,hi) in enumerate(boxes[k][0])))
        box,depth=boxes.pop(idx)
        _,l,r=split_box(box)
        boxes.extend([(l,depth+1),(r,depth+1)])
    return boxes

def init_worker(base_dir,A,B):
    global CHECKER,A_GLOBAL,B_GLOBAL,WEIGHTS
    base=Path(base_dir); sys.path.insert(0,str(base))
    from a1294_seam_pilot import Checker, WEIGHTS as W
    WEIGHTS=W; A_GLOBAL=q(A); B_GLOBAL=q(B)
    CHECKER=Checker(base/"data"/"macro-data-exact.json",
                    base/"data"/"refinement-catalog-v1-exact.json",
                    base/"data"/"refinement-catalog-v3.json",
                    A_GLOBAL,B_GLOBAL)

def process_chunk(payload):
    box_raw,start_depth,node_cap=payload
    stack=[(deserialize_box(box_raw),start_depth)]
    visited=leaves=tail=quadratic=0; max_depth=start_depth; smallest=None
    t0=time.monotonic()
    while stack and visited<node_cap:
        cur,depth=stack.pop(); visited+=1; max_depth=max(max_depth,depth)
        margin=B_GLOBAL*sum((x[0] for x in cur),F(0))-A_GLOBAL
        if margin>=0:
            leaves+=1; tail+=1; smallest=margin if smallest is None else min(smallest,margin); continue
        margin=CHECKER.lower(cur)-A_GLOBAL
        if margin>=0:
            leaves+=1; quadratic+=1; smallest=margin if smallest is None else min(smallest,margin); continue
        _,l,r=split_box(cur); stack.append((r,depth+1)); stack.append((l,depth+1))
    return {
        "pid":os.getpid(),"visited":visited,"leaves":leaves,"tail":tail,"quadratic":quadratic,
        "max_depth":max_depth,
        "smallest_margin":None if smallest is None else [smallest.numerator,smallest.denominator],
        "frontier":[{"box":serialize_box(b),"depth":d} for b,d in stack],
        "elapsed_seconds":time.monotonic()-t0
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--base",required=True)
    ap.add_argument("--workers",type=int,default=6)
    ap.add_argument("--chunk-nodes",type=int,default=10000)
    ap.add_argument("--budget",type=int,default=5000000)
    ap.add_argument("--initial-boxes",type=int,default=32)
    args=ap.parse_args()

    base=Path(args.base); sys.path.insert(0,str(base))
    from a1294_seam_pilot import WEIGHTS as W
    global WEIGHTS; WEIGHTS=W

    A="1296/100000"; B="1094977/5000000000"
    frontier=deque({"box":serialize_box(b),"depth":d} for b,d in partition_root(60,args.initial_boxes))
    active={}; visited=leaves=tail=quadratic=0; max_depth=0; smallest=None
    worker_nodes=defaultdict(int); worker_chunks=defaultdict(int)
    t0=time.monotonic()

    with ProcessPoolExecutor(max_workers=args.workers,initializer=init_worker,
                             initargs=(str(base),A,B)) as pool:
        def submit(item):
            fut=pool.submit(process_chunk,(item["box"],item["depth"],args.chunk_nodes))
            active[fut]=item

        while frontier and len(active)<args.workers*2: submit(frontier.popleft())
        next_print=500000
        while active:
            done,_=wait(tuple(active),return_when=FIRST_COMPLETED)
            for fut in done:
                active.pop(fut,None); res=fut.result()
                visited+=res["visited"]; leaves+=res["leaves"]; tail+=res["tail"]; quadratic+=res["quadratic"]
                max_depth=max(max_depth,res["max_depth"])
                worker_nodes[str(res["pid"])]+=res["visited"]; worker_chunks[str(res["pid"])]+=1
                if res["smallest_margin"] is not None:
                    m=F(*res["smallest_margin"]); smallest=m if smallest is None else min(smallest,m)
                frontier.extend(res["frontier"])
            while frontier and len(active)<args.workers*2 and visited<args.budget:
                submit(frontier.popleft())
            if visited>=next_print:
                print(json.dumps({"visited":visited,"pending":len(frontier)+len(active),
                                  "max_depth":max_depth,"elapsed":time.monotonic()-t0}),flush=True)
                next_print+=500000
            if visited>=args.budget and not active: break
            if not active and frontier and visited<args.budget:
                while frontier and len(active)<args.workers*2: submit(frontier.popleft())

    wall=time.monotonic()-t0; pending=list(frontier)
    report={
        "schema":"a1296-fullroot-5m-diagnostic-v1",
        "A":A,"B":B,"visited":visited,"closed_leaves":leaves,"tail_leaves":tail,
        "quadratic_leaves":quadratic,"pending":len(pending),"maximum_depth":max_depth,
        "smallest_closed_margin":None if smallest is None else fstr(smallest),
        "wall_seconds":wall,"nodes_per_second":visited/wall if wall else 0.0,
        "worker_nodes":dict(worker_nodes),"worker_chunks":dict(worker_chunks),
        "deepest_pending_boxes":sorted(pending,key=lambda x:x["depth"],reverse=True)[:200],
        "status":"FULLY_CLOSED" if not pending else "BUDGET_REACHED_WITH_FRONTIER",
        "catalog_ceiling_witness_decimal":"0.01296158319577883963",
        "headroom_of_A1296_below_witness":"0.00000158319577883963",
        "claim_boundary":"Diagnostic only unless FULLY_CLOSED; even FULLY_CLOSED here is a search result, not the final theorem without independent canonical verification."
    }
    out=base/"results"/"A1296_FULLROOT_5M_DIAGNOSTIC_RESULT.json"
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps({k:report[k] for k in ["status","visited","pending","maximum_depth","wall_seconds","nodes_per_second"]},indent=2))
    print("RESULT",out)

if __name__=="__main__": main()
