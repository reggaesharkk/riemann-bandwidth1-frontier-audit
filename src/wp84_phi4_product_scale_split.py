#!/usr/bin/env python3
"""Exact split of the public Phi4=-1/60 connected integral by product scale.

Requires the pinned public reproduction tree at:
    upstream/gpu/exact_connected.py

For a closed four-step cycle v0+v1+v2+v3=0 define
    s = sum_{v_j>0} v_j = (|v0|+|v1|+|v2|+|v3|)/2.
In the arithmetic interpretation s=log(A)/L=log(B)/L for a balanced
2-vs-2 multiplicative relation A/B=1.

This script splits the exact connected integral into s<=1 and s>1 pieces.
The extra absolute-value and s=1 walls are inserted into the exact rational
polytope breakpoint engine, so each piece is certified with the same
whole-cell vs two-half Newton-Cotes identity as the upstream verifier.
"""
from fractions import Fraction as F
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
UP=ROOT/"upstream"/"gpu"/"exact_connected.py"
assert UP.exists(), f"missing pinned upstream source: {UP}"

spec=importlib.util.spec_from_file_location("ec",UP)
ec=importlib.util.module_from_spec(spec)
spec.loader.exec_module(ec)

ZERO,ONE=F(0),F(1)

def add_forms_for_scale(base_forms,d):
    fs=set(base_forms)

    # v0,v1,v2 are free; v3=-(v0+v1+v2).
    vecs=[]
    for j in range(3):
        v=[ZERO]*(d+1); v[j+1]=ONE; vecs.append(tuple(v))
    v3=tuple([ZERO]+[-ONE,-ONE,-ONE])
    vecs.append(v3)

    # Sign-orthant walls vi=0.
    for v in vecs:
        fs.add(v)

    # In a fixed sign orthant, sum |vi| = sum eps_i vi.
    # Add every possible scale wall sum eps_i vi = 2.
    from itertools import product
    for eps in product((-1,1),repeat=4):
        co=[F(-2)]+[ZERO]*d
        for e,v in zip(eps,vecs):
            for j in range(d+1):
                co[j]+=F(e)*v[j]
        fs.add(tuple(co))
    return sorted(fs)

class SplitCls(ec.Cls):
    def __init__(self,d,posA,posB,wsign=None,name="",mode="low"):
        self.mode=mode
        super().__init__(d,posA,posB,wsign,name)
        self.forms=add_forms_for_scale(self.forms,d)
        self.BP=self._breakpoints()

    def scale(self,xs):
        v0,v1,v2=xs
        v3=-(v0+v1+v2)
        return (abs(v0)+abs(v1)+abs(v2)+abs(v3))/2

    def f(self,xs):
        r=super().f(xs)
        if r==0:
            return r
        s=self.scale(xs)
        if self.mode=="low":
            return r if s<=1 else ZERO
        if self.mode=="high":
            return r if s>1 else ZERO
        raise ValueError(self.mode)

def split_terms(mode):
    out=[]
    for sign,cls in ec.cycle_terms(4):
        out.append((sign,SplitCls(
            cls.d,cls.posA,cls.posB,cls.wsign,
            f"{cls.name}/{mode}",mode
        )))
    return out

def integrate(mode):
    tot=ZERO
    terms=split_terms(mode)
    for i,(sign,cls) in enumerate(terms):
        val=cls.integrate()
        tot += sign*val
        print(mode,"term",i,"sign",sign,"value",val,flush=True)
    return tot

def main():
    low=integrate("low")
    high=integrate("high")
    total=low+high
    target=F(-1,60)
    assert total==target,(low,high,total,target)
    print("Phi4 s<=1 =",low,"~",float(low))
    print("Phi4 s>1  =",high,"~",float(high))
    print("sum        =",total,"~",float(total))
    print("target     =",target)
    print("RESULT: WP84_PHI4_PRODUCT_SCALE_SPLIT_PASS")

if __name__=="__main__":
    main()
