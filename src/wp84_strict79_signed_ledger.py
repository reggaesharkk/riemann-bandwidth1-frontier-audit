"""Source-matched signed ledger and exact central-window error budgets."""
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PARENT='d6e5de5b1247f8fe1c7b64b235c81b186115d82e'
OUT=ROOT/'notes/WP84_STRICT79_SIGNED_LEDGER_CERTIFICATE.json'
R=6000;A=Q(11501,12500);B=Q(137641,250000)

def build():
    old=json.loads((ROOT/'notes/WP84_STRICT79_BALANCED_PAIR_CERTIFICATE.json').read_text())
    rows=[];totals={}
    for name,b,k,pairs,weight in [('D5',5,5,1,-A),('Q3',5,3,10,-A),
                                  ('D6',6,6,1,B),('Q4',6,4,15,B)]:
        budget=Q(0)
        for r in range(k+1):
            s=k-r
            removable=min(r,s)==1
            # Bound applies to the pre-PNT balanced pair as well: 2*sum c_p^2<=2 eventually.
            constant=Q(176,7)*2**k*factorial(r)*factorial(s)*comb(k,r)*pairs*(12001**(b-1))
            if k<b:constant*=2
            if removable:budget+=abs(weight)*constant
            near=[m for m in range(-s+1,r) if m!=0 or (r and s)]
            rows.append({'family':name,'original_degree':b,'visible_degree':k,'positive':r,'negative':s,
                         'ordered_sign_placements':comb(k,r),'pair_choices':pairs,'signed_weight':str(weight),
                         'factor_length_exponents':[r,s],'possible_near_aliases':near,
                         'central_window_empty':not(r and s),
                         'central_one_prime_removed':removable,
                         'absolute_central_error_constant':str(constant) if removable else None})
        totals[name]=str(budget)
    inputs=['notes/WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md',
            'notes/WP84_STRICT79_BALANCED_PAIR_CERTIFICATE.json',
            'notes/WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE.md',
            'notes/WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER.md']
    return {'input_head':PARENT,'R':R,'cutoff':'floor(exp(L-sqrt(L))), L=log(T/(2*pi))',
            'kernel':'original geometric grid sum with original path root interval and exp(i*T*m*L)',
            'prime_windows':'arbitrary original exact masks; no factor-restricted window is dropped',
            'rows':rows,'central_error_multiplier':'N*(1+log(3*N))/T',
            'signed_absolute_error_constants':totals,'total_absolute_error_constant':str(sum(map(Q,totals.values()))),
            'negative_saving_proved':'0','central_o1_proved':True,'all_aliases_removed':False,
            'frequency_supports':{'odd_visible_degrees':[3,5],'even_visible_degrees':[4,6],
                                  'cross_degree_exact_cancellation':False},
            'Jstar':old['constants']['Jstar'],'necessary_saving_lower':old['gaussian_pinching']['required_negative_residual_at_least'],
            'exact_target':'limsup Re F_remaining <= Jstar-B*Pair6_6000-eta, eta>0',
            'first_unproved_step':'negative joint bound on remaining central multi-product cells, all nonzero aliases and tails',
            'arithmetic_inequality_12_proved':False,'strict_gt79_proved':False,
            'source_pins':{p:{'sha256':sha256((ROOT/p).read_bytes()).hexdigest(),
                              'git_blob':subprocess.check_output(['git','rev-parse',PARENT+':'+p],cwd=ROOT,text=True).strip()} for p in inputs},
            'packet_sha256':old['packet_sha256']}

if __name__=='__main__':
    data=build();OUT.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print('Signed ledger:',len(data['rows']),'rows; central removals:',sum(r['central_one_prime_removed'] for r in data['rows']))
    print('Exact total central-error constant:',data['total_absolute_error_constant'])
    print('Negative constant saving proved: 0. Signed target remains OPEN.')
