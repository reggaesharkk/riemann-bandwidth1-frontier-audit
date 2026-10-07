"""Exact structural compression; formal incidence rank is not analytic rank."""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction as Q
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def load():return list(csv.DictReader((ROOT/'notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv').open()))
def key(r):
    a,b,m=json.loads(r['canonical_reduced_key']);return int(r['degree']),tuple(a),tuple(b)
def flip(p):return p[0],p[2],p[1]
def raw(r):return int(r['degree']),r['sign_word'],r['equality_labels']
def conjraw(t):return t[0],''.join('-' if x=='+' else '+' for x in t[1]),t[2]
def normalize(seq):
    labels={};out=[]
    for x in seq:
        if x not in labels:labels[x]=len(labels)
        out.append(labels[x])
    return ','.join(map(str,out))
def raworbit(r):
    b,word,labels=r;pi=list(map(int,labels.split(',')));out=set()
    for rev in (False,True):
        w=word[::-1] if rev else word;q=pi[::-1] if rev else pi
        for k in range(b):
            t=(b,w[k:]+w[:k],normalize(q[k:]+q[:k]));out.add(t);out.add(conjraw(t))
    return out
def omega(b):return -Q(11501,12500) if b==5 else Q(137641,250000)
def kind(p):
    _,a,b=p;n,m=sum(a),sum(b)
    if not a or not b:return 'one-sided higher-alias prime product'
    if all(e==1 for e in a+b):
        return {(1,1):'prime-prime',(1,2):'prime x semiprime',(2,1):'prime x semiprime',(2,2):'semiprime x semiprime',(2,3):'restricted d2-d3',(3,2):'restricted d2-d3',(3,3):'restricted d3-d3'}.get((n,m),'higher multilinear')
    return 'restricted prime-power-factor correlation'
def main():
    rows=load();by=defaultdict(list);raws={raw(r) for r in rows}
    types={(key(r),int(r['m'])) for r in rows}; raw_lookup={raw(r):r for r in rows}
    for r in rows:by[key(r)].append(r)
    pats=sorted(by);orb=sorted({min(p,flip(p)) for p in pats});torb=sorted({min((p,m),(flip(p),-m)) for p,m in types})
    assert len(pats)==105 and len(types)==336
    assert all(flip(p) in by for p in pats)
    assert all((flip(p),-m) in types for p,m in types)
    assert all(conjraw(r) in raws for r in raws)
    records=[];fun=[]
    for i,p in enumerate(pats):
        rs=by[p];origin=sorted({raw(r)[1:] for r in rs});aliases=sorted({int(r['m']) for r in rs})
        records.append({'id':i,'degree':p[0],'numerator_exponents':p[1],'denominator_exponents':p[2],'origins':[{'sign_word':s,'equality_partition':e} for s,e in origin],'aliases':aliases,'ordinary_prime_windows':'each distinct block prime q<=floor(exp(L-sqrt(L))); original slot-window intersections retained','fourier_displacements':'all l in [-6000,6000]^b with sum l=0; u_j=sum_(i<=j)l_i','sampled_kernel':'exp(i*T*lambda+2*pi*i*imin*lambda/L)/dprime * sum_(k=0..M-1)exp(2*pi*i*k*lambda/L)','weight':'prod_j[-log(p_j)/(a_phi L sqrt(p_j))*f_l_j^eps_j(log(p_j)/L)] * exp(2*pi*i*sum eps_j*u_(j-1)*log(p_j)/L)','cumulant_coefficient':'1: raw trace consumer, no added cumulant subtraction','consumer_coefficient':str(omega(p[0])),'conjugate_pattern_id':pats.index(flip(p)),'arithmetic_type':kind(p),'raw_classes':len(origin),'phase_orbit_id':orb.index(min(p,flip(p)))})
    # Explicit, exact functionals of the ACTUAL object: conjugate raw pairs.
    # They retain all origins, windows and paths, and aggregate admissible m.
    reps=sorted({min(raworbit(r)) for r in raws}); orbit_members={r:sorted(raworbit(r)) for r in reps}; assert all(set(v)<=raws for v in orbit_members.values())
    for j,r in enumerate(reps):
        p=key(raw_lookup[r]);aliases=sorted({int(v['m']) for v in by[p] if raw(v)==r})
        fun.append({'id':j,'degree':r[0],'sign_word':r[1],'equality_partition':r[2],'aliases':aliases,'conjugate_sign_word':conjraw(r)[1],'definition':'Re of complete raw correlation with all listed m, prime blocks and closed Fourier paths; excludes omega','exact_alpha':str(len(orbit_members[r])*omega(r[0])),'raw_orbit_members':orbit_members[r],'pattern':p,'status':'nonzero formal coefficient; analytic independence NOT proved'})
    assert sum(len(v) for v in orbit_members.values())==8740
    incidence=[]
    for rid,r in enumerate(sorted(raws)):
        rr=raw_lookup[r];p=key(rr)
        incidence.append([rid,r[0],r[1],r[2],pats.index(p),orb.index(min(p,flip(p))),reps.index(min(raworbit(r))),str(omega(r[0]))])
    with (ROOT/'notes/WP84_NEAR_ALIAS_COEFFICIENT_AGGREGATION.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['phase_orbit_id','degree','raw_class_count','exact_scalar_sum','scope'])
        for oid,o in enumerate(orb):
            members={raw(r) for p in by if min(p,flip(p))==o for r in by[p]}
            w.writerow([oid,o[0],len(members),str(len(members)*omega(o[0])),'formal coefficient sum only; full origin weights retained'])
    # Every column has disjoint nonempty row support; exact ranks without floats.
    ranks={'raw_to_phase_pattern':{'shape':[8740,105],'rank':105,'left_nullity':8635,'right_nullity':0},'raw_to_phase_orbit':{'shape':[8740,len(orb)],'rank':len(orb),'left_nullity':8740-len(orb),'right_nullity':0},'raw_to_conjugate_raw_functional':{'shape':[8740,len(reps)],'rank':len(reps),'left_nullity':8740-len(reps),'right_nullity':0}}
    bases={}
    for col,label in ((4,'pattern'),(5,'pattern_orbit'),(6,'conjugate_raw')):
        first={};relations=[]
        for row in incidence:
            rid=row[0];c=row[col]
            if c not in first:first[c]=rid
            else:relations.append([rid,first[c],1,-1])
        bases[label]={'row_basis':list(first.values()),'column_basis':sorted(first),'left_null_basis':relations,'meaning':'formal incidence row difference, NOT an analytic identity between original correlations'}
    mass=sum(abs(Q(f['exact_alpha'])) for f in fun)
    rel=Q(52897896569489,572357731837500000)
    cert={'parent':'dc71147aab7f7a3609fc2d0ca0a09cf0dfb32bf9','decision':'F','source_patterns':105,'raw_classes':8740,'pattern_orbits':len(orb),'pattern_orbit_sizes':dict(Counter(sum(min(p,flip(p))==o for p in pats) for o in orb)),'alias_orbits':len(torb),'alias_orbit_sizes':dict(Counter(sum(min((p,m),(flip(p),-m))==o for p,m in types) for o in torb)),'pattern_representatives':orb,'alias_representatives':torb,'certified_group':'dihedral slot rotations/reversals times C2 conjugation, with canonical dummy prime-label relabelling','actual_raw_conjugate_functionals':len(reps),'raw_orbit_size_histogram':dict(Counter(len(v) for v in orbit_members.values())),'incidence_ranks':ranks,'bases':bases,'actual_minimal_correlation_rank':None,'actual_nullity':None,'absolute_coefficient_mass':str(mass),'sufficient_common_bound_full_relaxed_allocation':str(rel/mass),'common_bound_achieved':False,'actual_charge':None,'strict_gt79':'OPEN','first_uncertified_step':'identification or linear dependence of actual path-weighted correlations sharing reduced phase patterns','frozen_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv','notes/WP84_NEAR_ALIAS_SURVIVOR_CERTIFICATE.json']}}
    for name,data in [('WP84_NEAR_ALIAS_CANONICAL_PATTERN_LEDGER.json',records),('WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json',fun),('WP84_NEAR_ALIAS_ORBIT_CERTIFICATE.json',cert)]:
        (ROOT/'notes'/name).write_text(json.dumps(data,indent=2)+'\n')
    with (ROOT/'notes/WP84_NEAR_ALIAS_EXACT_INCIDENCE.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['raw_id','degree','sign_word','equality_partition','phase_pattern_id','phase_orbit_id','raw_conjugate_functional_id','omega']);w.writerows(incidence)
    print('PASS:',len(orb),'phase orbits;',len(torb),'alias orbits;',len(fun),'explicit actual conjugate-pair functionals')
    print('Formal incidence ranks only:',ranks,'coefficient mass',mass,'common target',float(rel/mass))
if __name__=='__main__':main()
