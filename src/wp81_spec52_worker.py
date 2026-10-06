#!/usr/bin/env python3
"""Deterministic WP81 shard worker for laptop or Colab.

Reads a locked shard manifest, verifies the execution-lock receipt says PASS,
then executes selected non-overlapping shards through wp81_spec52_exact.py.

The worker never edits the manifest and never merges outputs.  Each shard has
one dedicated raw log.  Aggregation/verification is a separate step.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

def load_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--lock",required=True)
    ap.add_argument("--upstream",required=True)
    ap.add_argument("--workdir",default="work/spec52")
    ap.add_argument("--shards",required=True,
                    help="comma list/ranges, e.g. 0-4,12,20-23")
    a=ap.parse_args()

    man=load_json(a.manifest)
    lock=load_json(a.lock)
    if man.get("schema")!="wp81-spec52-shard-plan-v1" or man.get("status")!="LOCKED":
        raise SystemExit("invalid/unlocked shard manifest")
    if lock.get("schema")!="wp81-spec52-execution-lock-v1" or lock.get("status")!="PASS":
        raise SystemExit("execution lock is not PASS")
    if lock["shard_manifest"]["canonical_plan_sha256"] != man["canonical_plan_sha256"]:
        raise SystemExit("execution lock does not bind this manifest")

    ids=set()
    for tok in a.shards.split(","):
        tok=tok.strip()
        if not tok: continue
        if "-" in tok:
            x,y=map(int,tok.split("-",1))
            ids.update(range(x,y+1))
        else:
            ids.add(int(tok))
    byid={int(s["shard"]):s for s in man["shards"]}
    bad=sorted(ids-set(byid))
    if bad:
        raise SystemExit(f"unknown shard ids: {bad}")

    outdir=Path(a.workdir)
    outdir.mkdir(parents=True,exist_ok=True)
    driver=Path(__file__).resolve().parent/"wp81_spec52_exact.py"

    for sid in sorted(ids):
        s=byid[sid]
        out=outdir/s["output"]
        done=out.with_suffix(out.suffix+".DONE")
        if done.exists():
            print(f"shard {sid}: DONE marker exists; skipping")
            continue
        if out.exists() and out.stat().st_size:
            raise SystemExit(
                f"shard {sid}: partial log exists at {out}; inspect it before rerun "
                "to avoid duplicate primitive rows"
            )
        cmd=[
            sys.executable,str(driver),
            "--upstream",str(Path(a.upstream).resolve()),
            "--d",str(s["d"]),
            "--terms",f'{s["lo"]}:{s["hi"]}',
            "--out",str(out),
        ]
        print("RUN"," ".join(cmd),flush=True)
        p=subprocess.run(cmd)
        if p.returncode:
            raise SystemExit(f"shard {sid} failed with exit code {p.returncode}")
        done.write_text(
            f"shard={sid}\nd={s['d']}\nlo={s['lo']}\nhi={s['hi']}\n",
            encoding="utf-8",
        )
        print(f"shard {sid}: COMPLETE -> {out}",flush=True)

    print("RESULT: WP81_SELECTED_SHARDS_COMPLETE")

if __name__=="__main__":
    main()
