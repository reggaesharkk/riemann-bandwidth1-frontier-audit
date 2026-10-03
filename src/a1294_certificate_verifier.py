#!/usr/bin/env python3
"""Independent exact verifier for the seam-aware A1294 certificate stream.

This file intentionally does not import the search generator or Checker.
No floating point is used in certificate acceptance.
"""
from __future__ import annotations

import argparse, bisect, hashlib, json, struct
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

WEIGHTS=(5,8,9,8,5)
PARTIALS=tuple((i,j) for i in range(5) for j in range(i,5))
VECTORS=tuple(tuple(1 if i<=k<=j else 0 for k in range(5)) for i,j in PARTIALS)
ANCHOR_DEN=16384

@dataclass(frozen=True)
class Piece:
    lo:F; hi:F; q:F; a:F; c:F; owner:int; idx:int

def q(x):
    return x if isinstance(x,F) else F(str(x))

def sha256(path:Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse_model(item,owner,idx):
    lo,hi=q(item["lo"]),q(item["hi"])
    kind=item["kind"]
    if kind in ("low","barrier","zero"):
        return Piece(lo,hi,F(0),q(item.get("a","0")),F(0),owner,idx)
    if kind=="well":
        m,v,e=q(item["m"]),q(item["v"]),q(item["q"])
        center=e+v/m if item["side"]=="left" else e-v/m
        return Piece(lo,hi,center,F(0),2*m*m,owner,idx)
    raise ValueError(kind)

def model_min(p,lo,hi):
    x=p.q if lo<=p.q<=hi else lo if p.q<lo else hi
    return p.a+p.c*(x-p.q)**2

class ExactVerifierModel:
    def __init__(self,stable_path,v1_path,v3_path,A,B):
        raw=json.loads(Path(stable_path).read_text())["pieces"]
        self.stable=[parse_model(it,i,i) for i,it in enumerate(raw)]
        assert len(self.stable)==56
        self.highs=[p.hi for p in self.stable]
        self.groups={i:[] for i in range(56)}
        self.groups[-1]=[]
        idx=56
        for it in json.loads(Path(v1_path).read_text())["pieces"]:
            owner=int(it["stable_piece_index"])
            cp=dict(it); cp["kind"]="well"
            self.groups[owner].append(parse_model(cp,owner,idx)); idx+=1
        for it in json.loads(Path(v3_path).read_text())["pieces"]:
            owner=int(it["stable_piece_index"])
            self.groups[owner].append(parse_model(it,owner,idx)); idx+=1
        assert idx==666
        self.A,self.B,self.cutoff=A,B,A/B
        self.group_bounds={
            owner:sorted(set(([self.stable[owner].lo,self.stable[owner].hi] if owner>=0 else [])
                             +[p.lo for p in pieces]+[p.hi for p in pieces]))
            for owner,pieces in self.groups.items()
        }
        self.cache={}

    def owner(self,x):
        return min(bisect.bisect_left(self.highs,x),55)

    def best_cover(self,lo,hi):
        o=self.owner(lo)
        cand=[]
        for owner in (o,max(0,o-1),min(55,o+1)):
            st=self.stable[owner]
            if st.lo<=lo and hi<=st.hi:
                cand.append(st)
                cand.extend(p for p in self.groups[owner] if p.lo<=lo and hi<=p.hi)
        cand.extend(p for p in self.groups[-1] if p.lo<=lo and hi<=p.hi)
        if not cand:
            return None
        return max(cand,key=lambda p:(model_min(p,lo,hi),-p.idx))

    def segmented_scalar(self,lo,hi):
        hi=min(hi,self.cutoff)
        if hi<lo:
            return F(0)
        key=(lo,hi)
        if key in self.cache:
            return self.cache[key]
        boundaries={lo,hi}
        first=self.owner(lo)
        last=self.owner(min(hi,F(59)))
        for owner in range(max(0,first-1),min(55,last+1)+1):
            for x in self.group_bounds[owner]:
                if lo<x<hi: boundaries.add(x)
        for x in self.group_bounds[-1]:
            if lo<x<hi: boundaries.add(x)
        ordered=sorted(boundaries)
        if lo==hi:
            p=self.best_cover(lo,hi)
            ans=F(0) if p is None else model_min(p,lo,hi)
        else:
            vals=[]
            for left,right in zip(ordered,ordered[1:]):
                p=self.best_cover(left,right)
                if p is None:
                    allp=[p for ps in self.groups.values() for p in ps
                          if p.lo<=left and right<=p.hi]
                    if not allp:
                        raise AssertionError(("catalog gap",left,right))
                    p=max(allp,key=lambda z:model_min(z,left,right))
                vals.append(model_min(p,left,right))
            ans=min(vals)
        self.cache[key]=ans
        return ans

    def quadratic_data(self,box):
        M=[[F(0) for _ in range(5)] for _ in range(5)]
        linear=[self.B for _ in range(5)]
        constant=F(0)
        for vector,(li,ri) in zip(VECTORS,PARTIALS):
            lo=sum((box[k][0] for k in range(li,ri+1)),F(0))
            hi=sum((box[k][1] for k in range(li,ri+1)),F(0))
            chi=min(hi,self.cutoff)
            p=self.best_cover(lo,chi) if lo<=chi else None
            if p is None:
                constant+=self.segmented_scalar(lo,hi)
                continue
            if p.idx<56 and self.groups.get(p.owner):
                scalar=self.segmented_scalar(lo,hi)
                if scalar>model_min(p,lo,chi):
                    constant+=scalar
                    continue
            constant+=p.a+p.c*p.q*p.q
            if p.c:
                for r in range(5):
                    if not vector[r]: continue
                    linear[r]-=2*p.c*p.q
                    for c in range(5):
                        if vector[c]: M[r][c]+=p.c
        return M,linear,constant

    def tangent_at_codes(self,box,codes):
        M,linear,constant=self.quadratic_data(box)
        point=[lo+F(code,ANCHOR_DEN)*(hi-lo)
               for code,(lo,hi) in zip(codes,box)]
        value=constant+sum(linear[i]*point[i] for i in range(5))
        value+=sum(M[i][j]*point[i]*point[j] for i in range(5) for j in range(5))
        grad=[linear[i]+2*sum(M[i][j]*point[j] for j in range(5)) for i in range(5)]
        return value+sum(min(grad[i]*(box[i][0]-point[i]),
                             grad[i]*(box[i][1]-point[i])) for i in range(5))

def split(box):
    weighted=[(hi-lo)*WEIGHTS[i] for i,(lo,hi) in enumerate(box)]
    axis=max(range(5),key=weighted.__getitem__)
    lo,hi=box[axis]; mid=(lo+hi)/2
    left,right=list(box),list(box)
    left[axis]=(lo,mid); right[axis]=(mid,hi)
    return axis,tuple(left),tuple(right)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--stable",required=True)
    ap.add_argument("--v1",required=True)
    ap.add_argument("--v3",required=True)
    ap.add_argument("--tree-dir",required=True)
    ap.add_argument("--report",required=True)
    args=ap.parse_args()

    tree=Path(args.tree_dir)
    manifest=json.loads((tree/"manifest.json").read_text())
    assert manifest["schema"]=="a1294-seam-aware-certificate-v1"
    A,B=q(manifest["A"]),q(manifest["B"])
    assert manifest["weights"]==list(WEIGHTS)
    assert manifest["anchor_denominator"]==ANCHOR_DEN
    assert sha256(Path(args.stable))==manifest["input_sha256"]["stable"]
    assert sha256(Path(args.v1))==manifest["input_sha256"]["v1"]
    assert sha256(Path(args.v3))==manifest["input_sha256"]["v3"]

    topology=(tree/"topology-u8.bin").read_bytes()
    kinds=(tree/"terminal-kinds-u8.bin").read_bytes()
    anchor_raw=(tree/"anchors-u16le.bin").read_bytes()
    assert hashlib.sha256(topology).hexdigest()==manifest["stream_sha256"]["topology"]
    assert hashlib.sha256(kinds).hexdigest()==manifest["stream_sha256"]["kinds"]
    assert hashlib.sha256(anchor_raw).hexdigest()==manifest["stream_sha256"]["anchors"]
    assert len(anchor_raw)%2==0
    anchors=list(struct.unpack("<"+"H"*(len(anchor_raw)//2),anchor_raw))
    assert all(0<=x<=ANCHOR_DEN for x in anchors)

    model=ExactVerifierModel(args.stable,args.v1,args.v3,A,B)
    root=tuple((F(0),F(manifest["limit"])) for _ in range(5))
    stack=[root]
    token_cursor=kind_cursor=anchor_cursor=0
    tail=quad=0
    smallest_tail=smallest_quad=None

    while stack:
        assert token_cursor<len(topology)
        box=stack.pop()
        token=topology[token_cursor]; token_cursor+=1
        if token:
            axis,left,right=split(box)
            assert token==axis+1
            stack.append(right); stack.append(left)
            continue

        assert kind_cursor<len(kinds)
        kind=kinds[kind_cursor]; kind_cursor+=1
        if kind==0:
            margin=B*sum((x[0] for x in box),F(0))-A
            assert margin>=0
            tail+=1
            smallest_tail=margin if smallest_tail is None else min(smallest_tail,margin)
        elif kind==1:
            assert anchor_cursor+5<=len(anchors)
            codes=anchors[anchor_cursor:anchor_cursor+5]; anchor_cursor+=5
            margin=model.tangent_at_codes(box,codes)-A
            assert margin>=0
            quad+=1
            smallest_quad=margin if smallest_quad is None else min(smallest_quad,margin)
        else:
            raise AssertionError(("bad leaf kind",kind))

    assert token_cursor==len(topology)
    assert kind_cursor==len(kinds)
    assert anchor_cursor==len(anchors)
    assert tail==manifest["tail_leaves"]
    assert quad==manifest["quadratic_leaves"]
    assert tail+quad==manifest["leaves"]

    report={
        "schema":"a1294-seam-aware-independent-replay-v1",
        "status":"PASS",
        "A":str(A),"B":str(B),
        "visited_nodes":manifest["visited_nodes"],
        "leaves":tail+quad,"tail_leaves":tail,"quadratic_leaves":quad,
        "smallest_tail_margin":None if smallest_tail is None else str(smallest_tail),
        "smallest_quadratic_margin":None if smallest_quad is None else str(smallest_quad),
        "stream_sha256":manifest["stream_sha256"],
        "input_sha256":manifest["input_sha256"],
        "trust_note":"Verification uses Fraction arithmetic only and reconstructs coverage and every terminal inequality independently of generator anchor proposals."
    }
    Path(args.report).write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
