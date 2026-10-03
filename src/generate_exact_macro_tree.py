from __future__ import annotations
import bisect, hashlib, json, os, struct
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

WEIGHTS=(5,8,9,8,5)
PARTIALS=tuple((i,j) for i in range(5) for j in range(i,5))
VECTORS=tuple(tuple(F(1) if i<=k<=j else F(0) for k in range(5)) for i,j in PARTIALS)

@dataclass(frozen=True)
class Piece:
    lo:F; hi:F; q:F; a:F; c:F; kind:str=''

def q(x):
    s=str(x).strip()
    while s.startswith('(') and s.endswith(')'):
        s=s[1:-1].strip()
    if '/' in s:
        a,b=s.split('/')
        return F(int(a),int(b))
    return F(int(s))

def qs(x:F):
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def model_min(p,lo,hi):
    x=p.q if lo<=p.q<=hi else lo if p.q<lo else hi
    return p.a+p.c*(x-p.q)**2

def read_pieces(path:Path):
    raw=json.loads(path.read_text())
    out=[]
    for it in raw['pieces']:
        lo,hi,kind=q(it['lo']),q(it['hi']),it['kind']
        if kind=='low':
            p=Piece(lo,hi,F(0),F(1,4),F(0),kind)
        elif kind=='zero':
            p=Piece(lo,hi,F(0),F(0),F(0),kind)
        elif kind=='barrier':
            p=Piece(lo,hi,F(0),q(it['a']),F(0),kind)
        elif kind=='well':
            m,v,e=q(it['m']),q(it['v']),q(it['q'])
            c=e+v/m if it['side']=='left' else e-v/m
            p=Piece(lo,hi,c,F(0),2*m*m,kind)
        else:
            raise ValueError(kind)
        out.append(p)
    assert len(out)==56
    return out

def sha256(path:Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def atomic_bytes(path:Path,data:bytes):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.new')
    tmp.write_bytes(data)
    os.replace(tmp,path)

def atomic_json(path:Path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.new')
    tmp.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    os.replace(tmp,path)

def box_json(box):
    return [[qs(a),qs(b)] for a,b in box]

def pack_topology(tokens):
    words=[]
    for off in range(0,len(tokens),20):
        w=0
        for i,t in enumerate(tokens[off:off+20]):
            w|=(int(t)&7)<<(3*i)
        words.append(w)
    return struct.pack('<'+'Q'*len(words),*words),words

def relative_anchor(point,box):
    codes=[]; exact=[]
    for x,(lo,hi) in zip(point,box):
        if hi==lo:
            code=0; val=lo
        else:
            r=(x-lo)/(hi-lo)
            code=max(0,min(16384,round(float(r)*16384)))
            val=lo+F(code,16384)*(hi-lo)
        codes.append(code); exact.append(val)
    return codes,exact

def tangent_lower(M,lin,const,box,point):
    value=const+sum(lin[i]*point[i] for i in range(5))
    value+=sum(M[i][j]*point[i]*point[j] for i in range(5) for j in range(5))
    grad=[lin[i]+2*sum(M[i][j]*point[j] for j in range(5)) for i in range(5)]
    return value+sum(min(grad[i]*(box[i][0]-point[i]),
                         grad[i]*(box[i][1]-point[i])) for i in range(5))

class ExactChecker:
    def __init__(self,stable,A,B):
        self.stable=stable
        self.A=A
        self.B=B
        self.cutoff=A/B
        self.highs=[p.hi for p in stable]
        self.scalar_certificates=[]
        self.scalar_cache={}

    def containing(self,lo,hi):
        idx=bisect.bisect_left(self.highs,lo)
        for k in (idx,idx+1):
            if 0<=k<len(self.stable):
                p=self.stable[k]
                if p.lo<=lo and hi<=p.hi:
                    return k,p
        return None

    def scalar_segments(self,lo,hi):
        bounds={lo,hi}
        for p in self.stable:
            if lo<p.lo<hi: bounds.add(p.lo)
            if lo<p.hi<hi: bounds.add(p.hi)
        ordered=sorted(bounds)
        segs=[]
        for l,r in zip(ordered,ordered[1:]):
            cand=[(model_min(p,l,r),i) for i,p in enumerate(self.stable)
                  if p.lo<=l and r<=p.hi]
            if not cand:
                continue
            v,i=max(cand,key=lambda z:(z[0],-z[1]))
            segs.append({'lo':qs(l),'hi':qs(r),'piece_index':i,'model_min':qs(v)})
        if lo==hi:
            cand=[(model_min(p,lo,hi),i) for i,p in enumerate(self.stable)
                  if p.lo<=lo<=p.hi]
            v,i=max(cand,key=lambda z:(z[0],-z[1]))
            segs=[{'lo':qs(lo),'hi':qs(hi),'piece_index':i,'model_min':qs(v)}]
        return segs

    def scalar_id(self,lo,hi):
        hi=min(hi,self.cutoff)
        if hi<lo:
            return 65535,F(0)
        key=(lo,hi)
        if key in self.scalar_cache:
            return self.scalar_cache[key]
        segs=self.scalar_segments(lo,hi)
        if not segs:
            ans=(65535,F(0))
        else:
            val=min(q(s['model_min']) for s in segs)
            if val==0:
                ans=(65535,val)
            else:
                code=32768+len(self.scalar_certificates)
                if code>=65535:
                    raise ArithmeticError('too many scalar certificates')
                self.scalar_certificates.append({
                    'lo':qs(lo),'hi':qs(hi),'a':qs(val),'segments':segs
                })
                ans=(code,val)
        self.scalar_cache[key]=ans
        return ans

    @staticmethod
    def float_coordinate_descent(M,lin,box,sweeps=10):
        mf=[[float(v) for v in row] for row in M]
        lf=[float(v) for v in lin]
        lo=[float(x[0]) for x in box]
        hi=[float(x[1]) for x in box]
        p=[(a+b)/2 for a,b in zip(lo,hi)]
        for _ in range(sweeps):
            for r in range(5):
                d=mf[r][r]
                if d>0:
                    off=sum(mf[r][c]*p[c] for c in range(5) if c!=r)
                    v=-(lf[r]+2*off)/(2*d)
                    p[r]=min(max(v,lo[r]),hi[r])
                else:
                    p[r]=lo[r] if lf[r]>=0 else hi[r]
        return p

    @staticmethod
    def rationalize_proposal(point,box):
        out=[]
        for v,(lo,hi) in zip(point,box):
            if lo==hi:
                out.append(lo)
                continue
            code=max(0,min(16384,round((v-float(lo))/float(hi-lo)*16384)))
            out.append(lo+F(code,16384)*(hi-lo))
        return out
