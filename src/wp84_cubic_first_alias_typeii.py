"""Focused source-window exponent/identity certificate; no numerical prime model."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json,subprocess
ROOT=Path(__file__).resolve().parents[1]
HEAD='9203b8e5d2c1466ad2c1e038ab945fdb86362602'
OUT=ROOT/'notes/WP84_CUBIC_FIRST_ALIAS_TYPEII_CERTIFICATE.json'
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def mu(n):
    f=factors(n);return 0 if any(x>1 for x in f.values()) else (-1)**len(f)
def lam(n):
    f=factors(n);return {next(iter(f)):1} if len(f)==1 else {}
def add(a,b,m=1):
    out=dict(a)
    for p,x in b.items():out[p]=out.get(p,0)+m*x
    return {p:x for p,x in out.items() if x}
def formal_vaughan(limit=192,U=5,V=7):
    rows=[]
    for n in range(1,limit+1):
        val={}
        for a in range(1,n+1):
            if n%a:continue
            t=n//a
            if a<=U:
                val=add(val,factors(t),mu(a))
                for c in range(1,min(t,V)+1):
                    if t%c==0:val=add(val,lam(c),-mu(a))
            else:
                for c in range(V+1,t+1):
                    if t%c==0:val=add(val,lam(c),mu(a))
        if n<=V:val=add(val,lam(n))
        assert val==lam(n)
        if len(factors(n))==1 and sum(factors(n).values())>1:val=add(val,lam(n),-1)
        target=lam(n) if sum(factors(n).values())==1 else {}
        assert val==target
        rows.append({str(p):x for p,x in sorted(val.items())})
    return sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def build():
    old=json.loads((ROOT/'notes/WP84_HIGH_PRODUCT_FEASIBILITY_CERTIFICATE.json').read_text())
    rows=[]
    for a in [F(13,20),F(7,10),F(3,4),F(4,5),F(17,20),F(9,10),F(19,20)]:
        b=F(8,5)-a
        rows.append({'p':str(a),'q':str(b),'r':'3/5','q_core_interval_exponent':str(b-1),'baseline_loss':'1/10'})
    blocks=[]
    for a in [F(1,5),F(1,4),F(3,10),F(7,20),F(2,5)]:
        blocks.append({'a':str(a),'b':str(F(3,5)-a),'inner_core_interval_exponent':str(F(3,5)-a-1)})
    hs=[F(0),F(1,10),F(1,5),F(1,4),F(3,10)]
    paths=['notes/WP84_HIGH_PRODUCT_SIGNED_FEASIBILITY.md','notes/WP84_HIGH_PRODUCT_FEASIBILITY_CERTIFICATE.json',
           'notes/WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md','notes/WP84_JOINT_THIRD_FIFTH_SIXTH_ARITHMETIC_OBSTRUCTION.md']
    return {'input_head':HEAD,'R':6000,'budget':old['budget'],'coefficients':old['coefficients'],
            'prime_ranges':rows,'denominator_typeii_blocks':blocks,
            'linearization':{'pointwise_error_constant_pi':16,'mass_constants':[32,96],
                'aggregate_error_constants_pi':[512,3072],
                'H_exponents':[{'h':str(h),'error_power':str(F(9,10)-3*h)} for h in hs],
                'fixed_H_accuracy_power':'9/10','source_magnitude_saving':'0'},
            'rectangular_dft':{'constant':1,'relative_gain':'3/10','full_rectangle_after_denominator_sum_exponent':'4/5',
                'illegally_subtracted_strip_exponent':'-1/5','exact_strip_transfer_proved':False},
            'vaughan':{'limit':192,'U':5,'V':7,'prime_only_formal_log_sha256':formal_vaughan(),
                'proper_power_compensation_retained':True,'prime_indicator_kept_on_typeii_factors':False},
            'mask_completion':{'example_modulus':1009,'positive_residues':[1],
                'cancelled_frequency_index':1008,'zero_frequency_coefficient_nonzero':True},
            'toy_envelope':{'M':16,'X':16**5,'U':16**8,'V':16**3,
                'cosine_lower':'4999/5000','absolute_growth_exponent':'1/10',
                'lower_prefactor':'4999/20000000','scope':'integer coefficient-envelope falsifier, NOT source prime data'},
            'carrier_retained':True,'source_masks_retained':True,'window_covariance_substitution':False,
            'power_saving_on_actual_window':'0','constant_signed_saving':'0','strict_gt79_proved':False,
            'verdict':'NO-GO for denominator Vaughan plus rectangular DFT transfer; signed strip estimate remains open',
            'source_pins':{p:{'sha256':sha256((ROOT/p).read_bytes()).hexdigest(),
                           'git_blob':subprocess.check_output(['git','rev-parse',HEAD+':'+p],cwd=ROOT,text=True).strip()} for p in paths}}
if __name__=='__main__':
    d=build();OUT.write_text(json.dumps(d,indent=2)+'\n',encoding='utf8')
    print('Certified fixed-core linearization accuracy X^(-9/10); actual magnitude saving 0; NO-GO.')
