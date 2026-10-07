from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from functools import lru_cache
import json
from pathlib import Path

def pairings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        for rest in pairings(items[1:j]+items[j+1:]):yield ((a,b),)+rest

def covariance(l,m,d):
    # x=(2*pi*i)^-2=-1/(4*pi^2); return (degree, rational coefficient).
    if l==m==0:return (0,F(1,6)) if d==0 else (1,F(2,d*d))
    if l==0 or m==0:return (0,F(0))
    k=(int(d==0)-int(d+l==0)-int(d-m==0)+int(d+l-m==0))
    return (1,F(-k,l*m))

def diagonal(R,b=8,reserve_canonical=True,kind="open"):
    if kind not in ("open","all"):raise ValueError(kind)
    if b%2:return [F(0)]
    pairs=list(pairings(tuple(range(b))));out=[F(0)]*(b//2+1);n=0
    for prefix in product(range(-R,R+1),repeat=b-1):
        last=-sum(prefix)
        if abs(last)>R:continue
        lag=prefix+(last,);u=[0]
        for l in lag:u.append(u[-1]+l)
        for pi in pairs:
            if kind=="open" and reserve_canonical and (b-2,b-1) in pi and lag[-2:]==(0,0):continue
            opened=sum(lag[i]+lag[j]!=0 for i,j in pi)
            if kind=="open" and opened==0:continue
            degree=0;coef=F(opened,len(pi)) if kind=="open" else F(1)
            for i,j in pi:
                k,v=covariance(lag[i],lag[j],u[i]-u[j]);degree+=k;coef*=v
                if not coef:break
            out[degree]+=coef;n+=1
    return out
if __name__=='__main__':
    v=diagonal(1);print([str(t) for t in v]);print('approx',sum(float(t)*(-1/(4*3.141592653589793**2))**i for i,t in enumerate(v)))
