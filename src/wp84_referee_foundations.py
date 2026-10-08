"""Exact rational curvature certificate and foundation-status ledger."""
from fractions import Fraction as Q
from functools import reduce
from hashlib import sha256
from math import gcd,lcm
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
HEAD='8a36b35d103850c4a8b37e2e1334364483b0b500'
OUT=ROOT/'notes/WP84_REFEREE_FOUNDATIONS_CERTIFICATE.json'
def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p
def add(p,q):return trim([(p[i] if i<len(p) else Q(0))+(q[i] if i<len(q) else Q(0)) for i in range(max(len(p),len(q)))])
def scale(p,a):return trim([a*x for x in p])
def mul(p,q):
    out=[Q(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return trim(out)
def power(p,n):
    out=[Q(1)]
    for _ in range(n):out=mul(out,p)
    return out
def diff(p):return trim([i*p[i] for i in range(1,len(p))] or [Q(0)])
def primitive(p):
    den=lcm(*(x.denominator for x in p));v=[int(x*den) for x in p];g=reduce(gcd,(abs(x) for x in v));return [Q(x//g) for x in v]
def remainder(p,q):
    p=p[:]
    while len(p)>=len(q) and any(p):
        shift=len(p)-len(q);a=p[-1]/q[-1]
        for j,v in enumerate(q):p[j+shift]-=a*v
        trim(p)
    return p
def sturm(p):
    seq=[primitive(p),primitive(diff(p))]
    while True:
        r=remainder(seq[-2],seq[-1])
        if not any(r):break
        seq.append(primitive(scale(r,-1)))
    return seq
def build():
    a=Q(221,200);M=Q(137721,5000)
    P=[Q(1),-Q(594893,185500),Q(1423,500),-Q(371,500)]
    N=scale(mul(P,P),a**6);D=[a*a,Q(0),Q(1)]
    H=add(add(mul(diff(diff(N)),power(D,2)),scale(mul([Q(0),Q(1)],mul(diff(N),D)),-12)),mul([-6*a*a,Q(0),Q(42)],N))
    den=power(D,5)
    gates=[add(scale(den,M),H),add(scale(den,M),scale(H,-1))]
    c=[Q(364848201,34410250000),-Q(18356061,344102500),-Q(26060119,430128125),Q(21981971,46375000),Q(0),-Q(11501,12500),Q(137641,250000)]
    band=3*M*Q(106,333)**2/6000;var=-2*c[2]*Q(106,333)**2/6000
    cap=Q(21,200)-c[0]-c[2]/3-band-var
    margin=cap+c[5]/-36-c[6]*Q(34,135) # cap + A/36 - B*ceiling
    old=json.loads((ROOT/'notes/WP84_STRICT79_SIGNED_LEDGER_CERTIFICATE.json').read_text())
    inputs=['notes/WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md','src/wp84_m4_free_robust_cubic_r6000.py',
            'notes/WP71_M3_ARCHIVE_RECONSTRUCTION.md','notes/WP84_FIXED_BAND_LOWER_MOMENT_COLLAPSE.md',
            'notes/WP84_SIGN_BALANCE_NEAR_RESONANCE_GATE.md','notes/WP84_TWO_SCALE_FILTERED_TO_SHARP_MOMENT_BRIDGE.md',
            'notes/WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md']
    inventory=[]
    pattern=re.compile(r'mu3|mu_3|mu_\{3\}|[μµ].?3|third[- ]moment|third.*cumulant|third.*PRIME|P_R\^3',re.I)
    for path in subprocess.check_output(['git','ls-tree','-r','--name-only',HEAD],cwd=ROOT,text=True).splitlines():
        if not path.endswith(('.md','.py')):continue
        for number,line in enumerate((ROOT/path).read_text(encoding='utf-8-sig').splitlines(),1):
            if pattern.search(line):inventory.append({'path':path,'line':number,'text':line})
    return {'input_head':HEAD,'R':6000,'curvature':{'bound':str(M),'a':str(a),'P':list(map(str,P)),
             'numerator':list(map(str,H)),'denominator':list(map(str,den)),
             'sturm_gates':[[list(map(str,p)) for p in sturm(g)] for g in gates]},
            'budget':{'band':str(band),'variance':str(var),'Jstar':str(cap),'reference_margin':str(margin),
                      'curvature_error_allowance':str(margin/(3*Q(106,333)**2/6000)),
                      'third_moment_adverse_allowance':str(margin/c[3]),
                      'third_coefficient':str(c[3]),'sixth_ceiling_slack':str(Q(34,135)-Q(157,630)),
                      'required_saving_lower':old['necessary_saving_lower']},
            'foundation_status':{'sampling_cell':'proved deterministic; continuous mean square has stated separation hypothesis',
             'C_ab_replacement':'proved bounded-gate implication; not unconditional sixth control',
             'Pair6_lower':'proved via exact covariance, Wick and Schatten pinching',
             'curvature':'proved by independent rational Sturm certificate',
             'functional_band':'proved for Loewner matrices; source identification conditional',
             'same_section_centered_mu3':'not proved by cited source; keep original third coefficient',
             'zero_side':'counting implication proved; analytic block/tail/normalization transfer not newly proved',
             'GUE_dictionary':'not established at finite R; STOP, no model moment computation'},
            'finite_R_multiplicativity':False,'GUE_fifth_sixth_computed':False,'strict_gt79_proved':False,
            'third_claim_search_inventory':inventory,
            'inventory_scope':'all tracked markdown/Python candidate mentions at input HEAD; model/conditional mentions are not theorem promotions',
            'source_pins':{p:{'sha256':sha256((ROOT/p).read_bytes()).hexdigest(),
                             'git_blob':subprocess.check_output(['git','rev-parse',HEAD+':'+p],cwd=ROOT,text=True).strip()} for p in inputs},
            'packet_sha256':old['packet_sha256']}
if __name__=='__main__':
    d=build();OUT.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
    print('Curvature Sturm degrees:',[[len(p)-1 for p in seq] for seq in d['curvature']['sturm_gates']])
    print(d['budget']);print('Same-section third gate OPEN; GUE dictionary blocked, no computation.')
