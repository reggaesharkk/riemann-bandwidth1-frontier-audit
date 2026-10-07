"""Frozen near-alias survivor extraction, exact Mobius identities and budgets."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter,defaultdict
from math import factorial,prod,gcd
from functools import lru_cache
import csv,json,hashlib
from wp84_signed_near_alias_attack import partitions,pattern,alias_status
from wp84_near_alias_long_tail_discharge import tuple_constructor
from wp84_direct_signed_correlation_attack import identities
ROOT=Path(__file__).resolve().parents[1]
A=F(11501,12500);B=F(137641,250000)
def redkey(e,m):return tuple(sorted((v for v in e if v>0),reverse=True)),tuple(sorted((-v for v in e if v<0),reverse=True)),m
def canonical(labels):
    d={};out=[]
    for v in labels:
        if v not in d:d[v]=len(d)
        out.append(d[v])
    return tuple(out)
@lru_cache(None)
def coarsenings(pi):
    k=max(pi)+1;out=[]
    for q in partitions(k):
        sigma=canonical(q[v] for v in pi)
        mu=prod((-1)**(q.count(j)-1)*factorial(q.count(j)-1) for j in range(max(q)+1))
        out.append((sigma,mu))
    return tuple(out)
def refines(pi,rho):
    d={}
    for a,b in zip(pi,rho):
        if a in d and d[a]!=b:return False
        d[a]=b
    return True
def piece_words(k,scheme):
    tags=('I1','I2','SHORT','II','POWER_COMP') if scheme=='Vaughan' else ('HB1','HB2','HB3','POWER_COMP')
    yield from product(tags,repeat=k)
def exact_atom():
    ps=[2,3,11,13,17];eps=[1,1,-1,-1,-1]
    atom=tuple_constructor(ps,eps,[0]*5,405,10,0,2430)
    labels=canonical(ps);nu,e,ap,am=pattern(labels,eps)
    assert atom['sector']=='NearAlias' and alias_status(e,atom['m'],nu)=='remaining_signed_dilated_product'
    ur=prod(p**max(v,0) for p,v in zip(dict.fromkeys(ps),e));vr=prod(p**max(-v,0) for p,v in zip(dict.fromkeys(ps),e))
    assert gcd(ur,vr)==1
    atom.update({'equality_labels':labels,'block_multiplicities':nu,'net_block_exponents':e,'A_red':ur,'B_red':vr,'gcd_reduced':1})
    return atom

def main():
    rows=list(csv.DictReader((ROOT/'notes/WP84_SIGNED_NEAR_ALIAS_SUPPORT.csv').open()))
    red=Counter();decor=Counter();classes=Counter();pairs=Counter();group=defaultdict(set);extract=[]
    for r in rows:
        if not r['alias_statuses']:continue
        b=int(r['degree']);pi=tuple(map(int,r['equality_labels'].split(',')));eps=tuple(1 if v=='+' else -1 for v in r['sign_word'])
        nu,e,ap,am=pattern(pi,eps);used=False
        for m,z in zip(map(int,r['asymptotic_support_alias_m'].split(',')),r['alias_statuses'].split(',')):
            if z!='remaining_signed_dilated_product':continue
            assert alias_status(e,m,nu)==z;used=True;pairs[b]+=1
            key=redkey(e,m);red[(b,key)]+=1;de=(tuple(sorted(zip(nu,e))),m);decor[de]+=1
            assert (ap+am-b)%2==0
            group[(b,eps,m)].add(pi)
            extract.append([b,r['sign_word'],r['equality_labels'],r['block_multiplicities'],r['net_block_exponents'],m,json.dumps(key)])
        if used:classes[b]+=1
    assert dict(classes)=={5:1132,6:7608} and dict(pairs)=={5:1956,6:19632}
    with (ROOT/'notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['degree','sign_word','equality_labels','multiplicities','net_exponents','m','canonical_reduced_key']);w.writerows(extract)
    reduced_without_m=set((key[0],key[1]) for b,key in red)
    with (ROOT/'notes/WP84_NEAR_ALIAS_REDUCED_FACTORS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['degree','positive_prime_exponents','negative_prime_exponents','m','class_count','raw_consumer_coefficient_sum','scope'])
        for (b,key),n in sorted(red.items()):
            w.writerow([b,json.dumps(key[0]),json.dumps(key[1]),key[2],n,str((-A if b==5 else B)*n),'raw combinatorial sum only; filters/windows/paths remain labelled'])
    # Complete equality-poset inversion for each sign word and alias integer.
    parts={b:list(partitions(b)) for b in (5,6)}
    ancestors={b:{rho:[pi for pi in parts[b] if refines(pi,rho)] for rho in parts[b]} for b in parts}
    mob_hist=Counter();mob_records=[];verified=0
    for (b,eps,m),selected in sorted(group.items()):
        coeff=Counter()
        for pi in selected:
            for sigma,mu in coarsenings(pi):coeff[sigma]+=mu
        for rho in parts[b]:
            assert sum(coeff[pi] for pi in ancestors[b][rho])==int(rho in selected);verified+=1
        for sigma,c in coeff.items():
            if not c:continue
            nu,e,ap,am=pattern(sigma,eps);mob_hist[c]+=1
            mob_records.append([b,''.join('+' if v==1 else '-' for v in eps),m,','.join(map(str,sigma)),c,json.dumps(redkey(e,m))])
    with (ROOT/'notes/WP84_NEAR_ALIAS_MOBIUS_COEFFICIENTS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['degree','sign_word','m','coarse_equality_constraints','exact_mobius_coefficient','coarse_reduced_factor_key']);w.writerows(mob_records)
    # Explicit finite decomposition generator, checked for every occurring block count.
    decomp={};decorated_catalog=[]
    for (blocks,m),n in sorted(decor.items()):
        k=len(blocks);decomp[k]={'Vaughan_pieces':5**k,'HB_pieces':4**k}
        decorated_catalog.append({'blocks_nu_e':blocks,'m':m,'class_count':n,'block_count':k,'Vaughan_pieces':5**k,'HB_pieces':4**k})
    for k,c in decomp.items():
        assert sum(1 for _ in piece_words(k,'Vaughan'))==c['Vaughan_pieces']
        assert sum(1 for _ in piece_words(k,'HB'))==c['HB_pieces']
    J=F(64788151489666079,572357731837500000);ideal=J+A/36-B*F(157,630);rel=J+A/36-B*F(34,135)
    alloc=[]
    for h in (F(1),F(10),F(100),F(400)):
        for share in (F(1),F(1,2),F(1,4),F(1,10)):
            alloc.append({'H':str(h),'share':str(share),'allocated_alias_charge':str(share*rel),'primitive_requirement':str(share*rel/(1+h/2)),'not_achieved':True})
    pins={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ('notes/WP84_SIGNED_NEAR_ALIAS_SUPPORT.csv','notes/WP84_SIGNED_NEAR_ALIAS_ATTACK.md','notes/WP84_SIGNED_NEAR_ALIAS_CERTIFICATE.json')}
    result={'decision':'F','parent':'b704d607fe08a656f5c7f5dfd2bc5e7f4149117d','surviving_sign_equality_classes':dict(classes),'surviving_pattern_alias_pairs':dict(pairs),'canonical_oriented_factor_m_patterns':len(red),'canonical_factor_patterns_without_m':len(reduced_without_m),'canonical_decorated_patterns':len(decor),'decorated_catalog':decorated_catalog,'parity_separation_5_vs_6':True,'exact_primitive_atom':exact_atom(),'mobius':{'group_count':len(group),'coefficient_records':len(mob_records),'inversion_tests':verified,'coefficient_histogram':dict(sorted(mob_hist.items())),'scope':'exact disjoint equality-mask inversion; NOT new cumulants or an analytic saving'},'prime_identities':identities(),'decomposition_counts':decomp,'relaxed_allowance':str(rel),'ideal_allowance':str(ideal),'primitive_allocations':alloc,'soft_falsifier':{'source':'WP84_SIGNED_NEAR_ALIAS_CERTIFICATE.json','symmetrization':'conjugate aliases make the real positive example double, with only factor-two norm costs','scope':'pointwise envelope/l2/support/kernel/conjugacy only; NOT prime or PNT/BV compatible'},'actual_survivor_charge':None,'remaining_ideal_allowance':None,'remaining_relaxed_allowance':None,'relation_to_central':'STRUCTURALLY DIFFERENT; no quantitative reduction or ordering proved','strict_gt79':'OPEN','frozen_sha256':pins}
    (ROOT/'notes/WP84_NEAR_ALIAS_SURVIVOR_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS extraction:',dict(classes),dict(pairs),'red,m patterns',len(red),'decorated',len(decor))
    print('PASS Mobius inversion:',verified,'tests;',len(mob_records),'coefficients; exact prime identities and allocation targets')
    print('Decision F: signed survivor prime correlation remains uncertified')
if __name__=='__main__':main()
