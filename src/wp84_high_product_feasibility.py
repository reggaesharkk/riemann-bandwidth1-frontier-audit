"""Exact budget/range certificate. No sampled prime data or extrapolation."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json, subprocess
ROOT=Path(__file__).resolve().parents[1]
HEAD='d8b2746e437ae7e8f9e681ef172fc286e11a6698'
OUT=ROOT/'notes/WP84_HIGH_PRODUCT_FEASIBILITY_CERTIFICATE.json'
def build():
    old=json.loads((ROOT/'notes/WP84_JOINT_CUBIC_ALIAS_CERTIFICATE.json').read_text())
    c=list(map(F,old['coefficients']));A=-c[5]
    ranges=[]
    for name,positive,negative,m in [
        ('cubic mixed hard',[F(4,5),F(4,5)],[F(3,5)],1),
        ('cubic same-sign second alias',[F(2,3)]*3,[],2),
        ('fifth central 2:3',[F(3,5)]*2,[F(2,5)]*3,0),
        ('sixth central 3:3',[F(2,5)]*3,[F(2,5)]*3,0),
        ('sixth single-pair central 2:2',[F(3,5)]*2,[F(3,5)]*2,0)]:
        alpha=sum(positive,F(0));beta=sum(negative,F(0))
        ranges.append(dict(name=name,positive=list(map(str,positive)),negative=list(map(str,negative)),
            alpha=str(alpha),beta=str(beta),alias=m,
            core_width_exponent=str(alpha-1),
            divisor_bulk_exponent=str((alpha+beta)/2-1)))
    pins=['notes/WP84_JOINT_THIRD_FIFTH_SIXTH_ARITHMETIC_OBSTRUCTION.md',
          'notes/WP84_JOINT_CUBIC_ALIAS_CERTIFICATE.json',
          'notes/WP84_SIGNED_NEAR_ALIAS_ATTACK.md',
          'notes/WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md']
    return dict(input_head=HEAD,R=6000,coefficients=old['coefficients'],budget=old['budget'],
        exact_kernel='exp(i*T*m*L)*exp(i*(T+h*i_min)*delta)*sum_j exp(i*h*j*delta)/n',
        real_offset='u-X^m*v; not assumed integer',
        dyadic_partition='half-open prime intervals intersected with ALL original masks; half-open product intervals; no smoothing',
        cubic_mixed_per_path_bound={'formula':'96*X^(-1/2)*H_Z+192*X^(-1/2)*Z*(1+log(3*X*Z+2))',
                                    'coefficients':[96,192],
                                    'eventual_L_bound_coefficients':[96,48,192,384],
                                    'Z':'floor(sqrt(X)/L^3)','rate':'O(L^(-2))+O(L/sqrt(X))',
                                    'scope':'entire abs(log(u/(X*v)))<=1, v<=Z'},
        joint_multiplier=str(6*(c[3]*12001**2+20*A*12001**4)),
        same_sign_second_alias={'unit_window':'288/X+576*(1+log(3*X^2+2))',
                                'coefficients':[288,576,288,96],
                                'core_abs_delta_le_1_over_X':'288+96/X',
                                'scope':'one path and one same-sign orientation; upper bounds only'},
        ranges=ranges,gram_cross_examples=['1/2','-1/2'],gram_determinant='3/4',
        new_constant_signed_saving='0',third_moment_retained=True,strict_gt79_proved=False,
        tails_retained=True,carrier_retained=True,proper_power_disposal_unconditional=False,
        verdict='NO-GO for closure with the audited estimates; stop speculative regrouping',
        primary_sources=[
          'https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf',
          'https://arxiv.org/pdf/2102.12297',
          'https://arxiv.org/abs/1510.06005'],
        source_pins={p:{'sha256':sha256((ROOT/p).read_bytes()).hexdigest(),
                       'git_blob':subprocess.check_output(['git','rev-parse',HEAD+':'+p],cwd=ROOT,text=True).strip()} for p in pins})
if __name__=='__main__':
    d=build();OUT.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
    print('Saved exact range/budget certificate. Constant signed saving: 0. Verdict: NO-GO.')
