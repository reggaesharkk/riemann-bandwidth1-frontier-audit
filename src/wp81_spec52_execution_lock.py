#!/usr/bin/env python3
"""
WP81 deterministic execution lock for the exact {5,2} certificate.

There is intentionally NO RNG seed.  The exact-polytope computation is
fully deterministic.  Reproducibility is locked by source identity,
upstream commit identity, shard-plan identity, Python/environment metadata,
and SHA-256 digests of the exact bytes actually executed.

The script additionally verifies Git blob SHA-1 identities of the critical
producer and upstream files against the frozen repository records.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, subprocess, sys
from pathlib import Path

UPSTREAM_COMMIT="d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8"

# Frozen Git blob identities from the repositories.
EXPECTED_BLOBS={
    "src/wp81_spec52_exact.py":"107fe5b2a888e482035b953048dbd3cece226ea9",
    "src/wp81_spec52_shard_plan.py":"25a25beb734ae20f76315769d0ee1f4436ddb163",
    "src/wp81_spec52_verify.py":"021c80f34475589f65d412cfddb1ba95dfe607b7",
}
EXPECTED_UPSTREAM_BLOBS={
    "gpu/exact_connected.py":"2983c1e03217d55cdebae45210d7f2b8861435cc",
    "gpu/exact_polytope.py":"8738e1f9f6ac30730c9e84b2d4a469959714cca9",
}

def sha256_bytes(b:bytes)->str:
    return hashlib.sha256(b).hexdigest()

def git_blob_sha1(b:bytes)->str:
    hdr=("blob %d\0"%len(b)).encode("ascii")
    return hashlib.sha1(hdr+b).hexdigest()

def git_head(root:Path)->str:
    return subprocess.check_output(
        ["git","-C",str(root),"rev-parse","HEAD"],
        text=True,stderr=subprocess.STDOUT
    ).strip()

def check_files(root:Path, expected:dict[str,str]):
    out={}
    for rel,want in expected.items():
        p=root/rel
        b=p.read_bytes()
        got=git_blob_sha1(b)
        if got!=want:
            raise SystemExit(f"blob mismatch {p}: {got} != {want}")
        out[rel]={
            "bytes":len(b),
            "git_blob_sha1":got,
            "sha256":sha256_bytes(b),
        }
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",default=".")
    ap.add_argument("--upstream",required=True)
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--out",default="wp81_spec52_execution_lock.json")
    a=ap.parse_args()

    root=Path(a.repo).resolve()
    upstream=Path(a.upstream).resolve()
    manifest=Path(a.manifest).resolve()

    up_head=git_head(upstream)
    if up_head!=UPSTREAM_COMMIT:
        raise SystemExit(f"upstream HEAD {up_head} != pinned {UPSTREAM_COMMIT}")

    local=check_files(root,EXPECTED_BLOBS)
    up=check_files(upstream,EXPECTED_UPSTREAM_BLOBS)

    mb=manifest.read_bytes()
    mobj=json.loads(mb)
    if mobj.get("schema")!="wp81-spec52-shard-plan-v1":
        raise SystemExit("unexpected shard-plan schema")
    if mobj.get("primitive_work_units")!=450:
        raise SystemExit("manifest does not cover 450 primitive units")
    if mobj.get("status")!="LOCKED":
        raise SystemExit("manifest not LOCKED")

    receipt={
        "schema":"wp81-spec52-execution-lock-v1",
        "status":"PASS",
        "determinism":{
            "rng_used":False,
            "rng_seed":None,
            "reason":"exact Fraction/polytope computation; no stochastic initialization",
        },
        "repo_head_recorded":git_head(root),
        "upstream_commit":up_head,
        "critical_local_files":local,
        "critical_upstream_files":up,
        "shard_manifest":{
            "path":str(manifest),
            "bytes":len(mb),
            "sha256":sha256_bytes(mb),
            "canonical_plan_sha256":mobj.get("canonical_plan_sha256"),
            "shard_count":mobj.get("shard_count"),
            "shard_size":mobj.get("shard_size"),
        },
        "environment":{
            "python":sys.version,
            "python_implementation":platform.python_implementation(),
            "platform":platform.platform(),
            "machine":platform.machine(),
        },
    }
    out=json.dumps(receipt,indent=2,sort_keys=True)
    Path(a.out).write_text(out+"\n",encoding="utf-8")
    print(out)
    print("RESULT: WP81_SPEC52_EXECUTION_LOCK_PASS")

if __name__=="__main__":
    main()
