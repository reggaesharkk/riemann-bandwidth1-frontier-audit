"""Exact third-aware consumer tradeoff and same-section variance budget."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json,subprocess,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
HEAD='7d0dd111138b2812d798f644c1bed11c8da9dacf'
OUT=ROOT/'notes/WP84_THIRD_AWARE_MARGIN_CERTIFICATE.json'
def convolve(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def build():
    R=6000;c=convolve([-Q(19101,185500),Q(961,3710),Q(31,50),-Q(371,500)],[-Q(19101,185500),Q(961,3710),Q(31,50),-Q(371,500)])
    A=-c[5];B=c[6];pi_inv_upper=Q(106,333)**2
    band=3*Q(137721,5000)*pi_inv_upper/R
    oldvar=-2*c[2]*pi_inv_upper/R
    newvar=-c[2]*pi_inv_upper/Q(2*R+1,2)
    oldcap=Q(21,200)-c[0]-c[2]/3-band-oldvar
    oldmargin=oldcap+A/36-B*Q(34,135)
    saving=oldvar-newvar;cap=oldcap+saving;margin=oldmargin+saving
    h=sum((Q(1,r*r) for r in range(1,R+1)),Q(0))
    old=json.loads((ROOT/'notes/WP84_REFEREE_FOUNDATIONS_CERTIFICATE.json').read_text())
    rows=[]
    for signed_debit in [Q(-1,10000),Q(0),Q(1,100000),Q(1,20000),Q(1,10000)]:
        rows.append({'fifth_sixth_signed_debit':str(signed_debit),'third_strict_ceiling_at_eta_zero':str((margin-signed_debit)/c[3])})
    # Exact moment-admissible example: spectral law, NOT source prime data.
    m=[Q(1,4)+Q(3,4)*(-Q(1,3))**j for j in range(7)]
    paths=['notes/WP84_INDEPENDENT_REFEREE_RESPONSE_FOUNDATIONS_AND_GUE.md',
           'notes/WP84_REFEREE_FOUNDATIONS_CERTIFICATE.json',
           'notes/WP84_STRICT79_SIGNED_ARITHMETIC_THEOREM_OR_OBSTRUCTION.md',
           'notes/WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md',
           'notes/WP84_FUNCTIONAL_BAND_THEOREM_DELTA80.md']
    return {'input_head':HEAD,'R':R,'cutoff':'floor(exp(L-sqrt(L))), L=log(T/(2*pi))',
            'consumer_changed':False,'coefficients':list(map(str,c)),
            'first_second_source_scope':'actual prime matrix, same contiguous section n/d->1; Weil identification separate',
            'variance_formula':'1/6+(1/pi^2)*sum_(r=1)^6000 1/r^2+o_T(1)',
            'harmonic_square_sum_sha256':sha256(str(h).encode()).hexdigest(),
            'tail_majorant':'1/(6000+1/2)',
            'budget':{'band':str(band),'old_variance':str(oldvar),'new_variance':str(newvar),
                      'earned_variance_saving':str(saving),'old_Jstar':str(oldcap),'new_Jstar':str(cap),
                      'old_reference_margin':str(oldmargin),'new_reference_margin':str(margin),
                      'old_third_ceiling':str(oldmargin/c[3]),'new_third_ceiling':str(margin/c[3]),
                      'new_necessary_saving_lower':str(Q(old['budget']['required_saving_lower'])-saving)},
            'tradeoff_rows':rows,
            'joint_gate':'limsup(c3*mu3-A*mu5+B*mu6) < new_Jstar; eta>0',
            'third_central_error_constant':str(Q(176,7)*8*2*6*12001**2),
            'third_remaining_scope':'all-distinct third nonzero aliases and far tails; original kernel and carrier',
            'conditional_holder_fourth_power':'34/3645',
            'moment_law_example':{'purpose':'no universal necessity for mu3=0; not zeta/prime evidence',
                                  'atoms':['1','-1/3'],'weights':['1/4','3/4'],
                                  'moments':list(map(str,m)),'square_expectation':str(sum(x*y for x,y in zip(c,m)))},
            'mu3_o1_proved':False,'small_one_sided_third_proved':False,
            'positive_third_fifth_sixth_signed_saving_proved':False,'strict_gt79_proved':False,
            'zero_side_transfer':'separate inherited analytic obligation; no new certification',
            'source_pins':{p:{'sha256':sha256((ROOT/p).read_bytes()).hexdigest(),
                             'git_blob':subprocess.check_output(['git','rev-parse',HEAD+':'+p],cwd=ROOT,text=True).strip()} for p in paths},
            'packet_sha256':old['packet_sha256']}
if __name__=='__main__':
    d=build();OUT.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
    for k,v in d['budget'].items():print(k,v,float(Q(v)))
    print('Actual third and joint arithmetic gates remain OPEN. Variance payment alone improves.')
