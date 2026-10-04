#!/usr/bin/env python3
"""Deterministic laptop/Colab shard plan for WP81 {5,2}."""
import argparse, hashlib, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--shard-size",type=int,default=10)
    ap.add_argument("--out",default="wp81_spec52_shards.json")
    a=ap.parse_args()
    if a.shard_size<=0 or 150%a.shard_size:
        raise SystemExit("shard-size must be a positive divisor of 150")
    shards=[]; sid=0
    for d in (1,2,3):
        for lo in range(0,150,a.shard_size):
            hi=lo+a.shard_size
            shards.append({
              "shard":sid,"d":d,"lo":lo,"hi":hi,"term_count":hi-lo,
              "output":"spec52_d%d_%03d_%03d.txt"%(d,lo,hi)
            })
            sid+=1
    units=[(s["d"],i) for s in shards for i in range(s["lo"],s["hi"])]
    assert len(units)==450 and len(set(units))==450
    assert set(units)=={(d,i) for d in (1,2,3) for i in range(150)}
    canonical="".join(
      "%d\t%d\t%d\t%d\t%s\n"%(s["shard"],s["d"],s["lo"],s["hi"],s["output"])
      for s in shards
    ).encode("utf-8")
    payload={
      "schema":"wp81-spec52-shard-plan-v1","status":"LOCKED",
      "primitive_work_units":450,"shard_size":a.shard_size,
      "shard_count":len(shards),
      "canonical_plan_sha256":hashlib.sha256(canonical).hexdigest(),
      "shards":shards,
    }
    Path(a.out).write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2,sort_keys=True))
    print("RESULT: WP81_SPEC52_SHARD_PLAN_LOCKED")

if __name__=="__main__":
    main()
