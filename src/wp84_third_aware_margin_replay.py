"""Independent exact first/second-moment ledger, tradeoff and hostile tests."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json,subprocess,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'notes/WP84_THIRD_AWARE_MARGIN_CERTIFICATE.json'
def verify(d):
    assert d['input_head']=='7d0dd111138b2812d798f644c1bed11c8da9dacf' and d['R']==6000
    assert d['cutoff']=='floor(exp(L-sqrt(L))), L=log(T/(2*pi))' and not d['consumer_changed']
    q=[-F(19101,185500),F(961,3710),F(31,50),-F(371,500)]
    c=[sum(q[i]*q[j] for i in range(4) for j in range(4) if i+j==k) for k in range(7)]
    assert list(map(F,d['coefficients']))==c and c[4]==0 and c[3]==F(21981971,46375000)
    assert d['first_second_source_scope']=='actual prime matrix, same contiguous section n/d->1; Weil identification separate'
    # Covariance 1/4 at zero and 0 at nonzero lattice offsets gives edge variance
    # 1/(2*pi^2*r^2); two oriented displacement slots give the following sum.
    h=F(0)
    for r in range(6000,0,-1):h+=2*F(1,2*r*r)
    assert sha256(str(h).encode()).hexdigest()==d['harmonic_square_sum_sha256']
    assert d['variance_formula']=='1/6+(1/pi^2)*sum_(r=1)^6000 1/r^2+o_T(1)'
    assert d['tail_majorant']=='1/(6000+1/2)'
    # Convex midpoint integral: int_(r-.5)^(r+.5) x^-2 dx > r^-2.
    for r in range(2,100):assert 1/F(2*r-1,2)-1/F(2*r+1,2)>F(1,r*r)
    R=6000;piinv=F(106,333)**2
    band=3*F(137721,5000)*piinv/R;oldvar=-2*c[2]*piinv/R
    newvar=-c[2]*piinv*F(2,12001);save=oldvar-newvar
    oldcap=F(21,200)-c[0]-c[2]/3-band-oldvar
    oldmargin=oldcap-c[5]/36-c[6]*F(34,135)
    newcap=oldcap+save;newmargin=oldmargin+save
    expected={'band':band,'old_variance':oldvar,'new_variance':newvar,'earned_variance_saving':save,
              'old_Jstar':oldcap,'new_Jstar':newcap,'old_reference_margin':oldmargin,'new_reference_margin':newmargin,
              'old_third_ceiling':oldmargin/c[3],'new_third_ceiling':newmargin/c[3]}
    assert save>0 and F(1,1000000)<save<F(11,10000000)
    for k,v in expected.items():assert F(d['budget'][k])==v
    old=json.loads((ROOT/'notes/WP84_REFEREE_FOUNDATIONS_CERTIFICATE.json').read_text())
    assert F(d['budget']['new_necessary_saving_lower'])==F(old['budget']['required_saving_lower'])-save>0
    for row in d['tradeoff_rows']:
        debit=F(row['fifth_sixth_signed_debit']);u=F(row['third_strict_ceiling_at_eta_zero'])
        assert c[3]*u+debit==newmargin
    e=d['moment_law_example'];atoms=list(map(F,e['atoms']));weights=list(map(F,e['weights']))
    moments=[sum(w*x**j for w,x in zip(weights,atoms)) for j in range(7)]
    assert moments==list(map(F,e['moments'])) and moments[1]==0 and moments[2]==F(1,3)
    assert moments[3]==F(2,9)>F(d['budget']['new_third_ceiling'])
    assert moments[5]>F(1,36) and moments[6]<F(34,135)
    val=sum(a*b for a,b in zip(c,moments));assert val==F(e['square_expectation'])
    assert val+band+newvar<F(21,200)
    assert F(d['conditional_holder_fourth_power'])==F(1,3)**3*F(34,135)
    assert F(31,100)**4<F(34,3645)<F(32,100)**4
    # The dimension-three Loewner sign diagnostic omits pi by taking alpha_i=pi*i.
    # Then all off-diagonal entries equal -1; negate alpha to reverse the cubic.
    off=[[F(0) if i==j else -F(1) for j in range(3)] for i in range(3)]
    cube_trace=sum(off[i][j]*off[j][k]*off[k][i] for i in range(3) for j in range(3) for k in range(3))/3
    assert cube_trace==-2 and -cube_trace==2
    assert F(d['third_central_error_constant'])==F(176,7)*8*2*6*12001**2
    assert not any(d[k] for k in ('mu3_o1_proved','small_one_sided_third_proved','positive_third_fifth_sixth_signed_saving_proved','strict_gt79_proved'))
    for p,hsh in d['source_pins'].items():
        assert sha256((ROOT/p).read_bytes()).hexdigest()==hsh['sha256']
        assert subprocess.check_output(['git','rev-parse',d['input_head']+':'+p],cwd=ROOT,text=True).strip()==hsh['git_blob']
    for p,hsh in d['packet_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==hsh
if __name__=='__main__':
    d=json.loads(PATH.read_text());verify(d)
    mutations=[('R',400),('consumer_changed',True),('mu3_o1_proved',True),('small_one_sided_third_proved',True),
               ('positive_third_fifth_sixth_signed_saving_proved',True),('strict_gt79_proved',True),
               ('first_second_source_scope','automatic zeta moment theorem')]
    for k,v in mutations:
        x=json.loads(json.dumps(d));x[k]=v
        try:verify(x)
        except AssertionError:pass
        else:raise AssertionError('accepted '+k)
    x=json.loads(json.dumps(d));x['budget']['earned_variance_saving']=str(2*F(d['budget']['earned_variance_saving']))
    try:verify(x)
    except AssertionError:pass
    else:raise AssertionError('accepted double payment')
    print('PASS independent square coefficients, 6000-displacement covariance sum, exact budgets, strict tradeoffs and spectral-law falsifier')
    print('PASS 8 hostile mutations; source/packet hashes. Positive variance-payment saving only; third arithmetic estimate OPEN.')
