"""Independent partition generation and recursive Wick replay. No producer import."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'notes/WP84_STRICT79_BALANCED_PAIR_CERTIFICATE.json'

def all_partitions(n):
    out=[]
    def visit(blocks,i):
        if i==n:
            out.append(tuple(next(k for k,b in enumerate(blocks) if j in b) for j in range(n)));return
        for k in range(len(blocks)):
            visit([b+[i] if t==k else b[:] for t,b in enumerate(blocks)],i+1)
        visit([b[:] for b in blocks]+[[i]],i+1)
    visit([],0);return out

def counts(n):
    rows=[];cnt=Counter()
    for pi in all_partitions(n):
        blocks=[[i for i,x in enumerate(pi) if x==k] for k in range(max(pi)+1)]
        shape=sorted(map(len,blocks))
        for signs in product((-1,1),repeat=n):
            charges=[sum(signs[i] for i in b) for b in blocks]
            if max(shape)>=3 and shape.count(1)<=2: tag='prior_closed'
            elif shape==[2,2,2]: tag='exact_pair_main' if not any(charges) else 'prior_closed'
            elif shape==[1,2,2]: tag='prior_closed'
            elif shape==[1,1,2,2]:
                tag='new_unconditional_degree_two' if not any(e for b,e in zip(blocks,charges) if len(b)==2) else 'new_orientation_summed_self_bound'
            elif shape==[1,1,1,3]: tag='new_orientation_summed_self_bound'
            elif 2 in shape:
                tag='surviving_balanced_pair' if next(e for b,e in zip(blocks,charges) if len(b)==2)==0 else 'new_orientation_summed_self_bound'
            else: tag='surviving_all_distinct'
            cnt[tag]+=1;rows.append([list(pi),list(signs),tag])
    return {'degree':n,'counts':dict(sorted(cnt.items())),'class_count':len(rows),
            'sha256':sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()}

def recursive_pair_polynomial(m):
    edges=[(i,j) for i in range(m) for j in range(i,m)]
    ids={e:k for k,e in enumerate(edges)}
    alpha=[]
    for i,j in edges:
        v=[Q(0)]*m
        if i!=j: v[i]=Q(1,j-i);v[j]=-Q(1,j-i)
        alpha.append(v)
    cov={}
    for a,(i,j) in enumerate(edges):
        for b,(k,l) in enumerate(edges):
            if i==j and k==l:
                cov[a,b]=(0,Q(1,6)) if i==k else (1,-Q(1,2*(i-k)**2))
            else: cov[a,b]=(1,sum(x*y for x,y in zip(alpha[a],alpha[b]))/4)
    @lru_cache(None)
    def wick(es):
        if not es:return (Q(1),)
        acc=[Q(0)]*(len(es)//2+1)
        for j in range(1,len(es)):
            deg,val=cov[es[0],es[j]]
            if val:
                for k,v in enumerate(wick(es[1:j]+es[j+1:])): acc[k+deg]+=val*v
        return tuple(acc)
    walks=Counter(tuple(sorted(ids[tuple(sorted((w[j],w[(j+1)%6])))] for j in range(6)))
                  for w in product(range(m),repeat=6))
    result=[Q(0)]*4
    for es,multiplicity in walks.items():
        for k,v in enumerate(wick(es)):result[k]+=multiplicity*v/m
    return result,len(walks)

def atan_interval(x,n):
    s=sum((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(n))
    tail=(-1)**n*x**(2*n+1)/Q(2*n+1)
    return min(s,s+tail),max(s,s+tail)

def check_merges():
    checked=0
    for n in (5,6):
        for pi in all_partitions(n):
            sizes=[pi.count(k) for k in range(max(pi)+1)]
            shape=sorted(sizes)
            if shape not in ([1,1,1,2],[1,1,1,1,2],[1,1,2,2],[1,1,1,3]):continue
            for signs in product((-1,1),repeat=n):
                charges=[sum(signs[i] for i,x in enumerate(pi) if x==k) for k in range(len(sizes))]
                charged_pair=any(e for e,v in zip(charges,sizes) if v==2)
                triple=shape==[1,1,1,3]
                balanced_two=shape==[1,1,2,2] and not charged_pair
                if not (charged_pair or triple or balanced_two):continue
                for merge in all_partitions(len(sizes)):
                    if len(set(merge))==len(sizes):continue
                    if balanced_two:
                        singles=[k for k,v in enumerate(sizes) if v==1]
                        if merge[singles[0]]==merge[singles[1]]:continue
                    w=tuple(merge[k] for k in pi)
                    new_sizes=[w.count(k) for k in range(max(w)+1)]
                    new_charges=[sum(signs[i] for i,x in enumerate(w) if x==k) for k in range(len(new_sizes))]
                    # No retained all-distinct or balanced-one-pair shape is generated.
                    assert len(set(w))<n
                    if sorted(new_sizes) in ([1,1,1,2],[1,1,1,1,2]):
                        assert any(e for e,v in zip(new_charges,new_sizes) if v==2)
                    if sorted(new_sizes)==[2,2,2]:assert any(new_charges)
                    checked+=1
    return checked

def verify(data, recomputed):
    assert data['input_head']=='06e51fbdb4150d2dbbbb4ddda6097575d9d2dcfa'
    assert data['R']==6000 and data['cutoff']=='floor(exp(L-sqrt(L))), L=log(T/(2*pi))'
    assert data['original_masks'] and data['alias_carrier_retained'] and data['proper_powers_retained_before_gate_reduction']
    assert data['scope']=='complete orientation-summed populations; never individual sign or frequency masks'
    assert data['census']==[counts(5),counts(6)]
    assert data['constants']=={'A':'11501/12500','B':'137641/250000',
       'Jstar':'64788151489666079/572357731837500000',
       'frozen_reference_margin':'52897896569489/572357731837500000'}
    g=data['gaussian_pinching'];p=recomputed
    assert g['block_size']==9 and list(map(Q,g['coefficients']))==p and all(v>0 for v in p)
    assert g['x']=='1/pi^2' and g['pi_lower']=='333/106' and g['pi_upper']=='22/7'
    a,b=atan_interval(Q(1,5),10);c,d=atan_interval(Q(1,239),3)
    assert Q(333,106)<16*a-4*d and 16*b-4*c<Q(22,7)
    lower=sum(v*(Q(7,22)**2)**k for k,v in enumerate(p))
    assert Q(g['lower'])==lower
    gap=Q(137641,250000)*lower-Q(data['constants']['Jstar'])
    assert Q(g['required_negative_residual_at_least'])==gap and gap>0
    assert not g['upper_bound_on_full_Pair6']
    assert data['self_bound']['bounded_gate_equivalence_proved'] and not data['self_bound']['sixth_bound_unconditional']
    assert not any(data[k] for k in ('arithmetic_inequality_12_proved','strict_gt79_proved','new_signed_saving_proved'))
    for path,pin in data['source_pins'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==pin['sha256']
        assert subprocess.check_output(['git','rev-parse',data['input_head']+':'+path],cwd=ROOT,text=True).strip()==pin['git_blob']
    for path,expected in data['packet_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==expected

if __name__=='__main__':
    data=json.loads(PATH.read_text());p,unique=recursive_pair_polynomial(9);verify(data,p)
    merges=check_merges()
    # Rank deletion alone fails even for diagonal Hermitian band matrices.
    for t in (2,3,7):
        d=t**30
        assert Q((t**5)**6,d)==1 and Q((t**5)**5,d)==Q(1,t**5)
        assert Q((t**6)**5,d)==1 and Q((t**6)**6,d)==t**6
        # L2 small pair field times four L2-bounded singleton fields can grow.
        assert Q(1,t**2)*(t**4)==t**2
        # Exact Young optimum used for the noncircular bootstrap.
        e=Q(t,7);U=(4*e/3)**3
        assert e*(4*e/3)**2-U/2==16*e**3/27
    mutations=[('R',400),('cutoff','N=T^0.1'),('alias_carrier_retained',False),
               ('original_masks',False),('proper_powers_retained_before_gate_reduction',False),
               ('scope','individual sign and near-alias masks'),('arithmetic_inequality_12_proved',True),
               ('strict_gt79_proved',True),('new_signed_saving_proved',True)]
    for key,value in mutations:
        bad=json.loads(json.dumps(data));bad[key]=value
        try:verify(bad,p)
        except AssertionError:pass
        else:raise AssertionError('accepted hostile mutation '+key)
    print('PASS independent 14656-class census; 531441 nine-site walks;',unique,'Wick multisets')
    print('PASS',merges,'new-population distinctness coarsenings; no retained balanced-one-pair correction')
    print('PASS exact pi enclosure, pair lower bound, rank/L2 falsifiers, Young optimum,',len(mutations),'hostile mutations')
    print('Actual signed inequality (12) remains OPEN.')
