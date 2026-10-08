"""Exact ledger and finite combinatorial certificate; no prime simulation."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json, subprocess
ROOT=Path(__file__).resolve().parents[1]
HEAD='8db0eb54019a7b69d18f4ba937b26e98d0c9a1d2'
OUT=ROOT/'notes/WP84_JOINT_CUBIC_ALIAS_CERTIFICATE.json'
def build():
    old=json.loads((ROOT/'notes/WP84_THIRD_AWARE_MARGIN_CERTIFICATE.json').read_text())
    c=list(map(F,old['coefficients'])); A=-c[5]
    adjacent=[]; separated=[]
    for a,b in combinations(range(5),2):
        (adjacent if (b-a) in (1,4) else separated).append([a,b])
    p3=12001**2;p5=12001**4
    pins=['notes/WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md',
          'notes/WP84_THIRD_AWARE_MARGIN_CERTIFICATE.json',
          'notes/WP84_STRICT79_SOURCE_MATCHED_ARITHMETIC_REDUCTION.md',
          'notes/WP84_STRICT79_SIGNED_ARITHMETIC_THEOREM_OR_OBSTRUCTION.md',
          'notes/WP84_INDEPENDENT_REFEREE_RESPONSE_FOUNDATIONS_AND_GUE.md']
    return dict(input_head=HEAD,R=6000,coefficients=list(map(str,c)),budget=old['budget'],
        adjacent_pairs=adjacent,separated_pairs=separated,
        cubic_contraction='Q3 = 5*tau(D*Y^3)+5*tau(V(Y)*Y^2)+o(1)',
        contraction_scope='conditional bounded complete signed gate; auxiliary Gaussian covariance only, not a law for Y',
        source_covariance={'alpha':'delta_ij/4','beta_diagonal':'1/6','beta_off_diagonal':'-1/(2*pi^2*(i-j)^2)','alpha_beta':'0'},
        coefficient_bounds={'all_zero_displacement':str(c[3]-F(5,3)*A),
                            'operator_upper_scalar':str(c[3]-F(5,6)*A)},
        exact_alias={'mixed_denominator':'1 or a single visible prime; denominator 1 impossible for distinct triples',
                     'third_absolute_constant':str(288*p3),
                     'joint_cubic_absolute_constant':str(288*(c[3]*p3+20*A*p5)),
                     'rate':'X^(-1/2)','carrier_retained':True},
        new_unconditional_removals=['D3 and Q3: mixed visible semiprime product U<=N',
                                    'D3 and Q3: same-sign visible triple product U<=N^2',
                                    'D3 and Q3: all exact nonzero aliases'],
        low_product_rates={'mixed':'O_R(N*(1+log(3*N))/T)',
                           'same_sign':'O_R(N/T+L/sqrt(X))'},
        residual_cubic=['mixed: U>N, abs(log(U/V))>1, nonexact aliases and tails',
                        'same-sign: U>N^2, nonexact second-alias neighborhood and all tails'],
        period_four={'values':['1','-1/3','-1/3','-1/3'],'mean':'0','second':'1/3','third':'2/9',
                     'shift_zero_mod_four':'2/9','other_shifts':'-2/27',
                     'cubic_upper_bound':str(F(2,9)*c[3]-F(25,81)*A),
                     'scope':'Loewner-form sign-method falsifier, not source prime data'},
        positive_constant_arithmetic_saving='0',proper_power_removal_unconditional=False,
        mu3_o1_proved=False,strict_gt79_proved=False,
        source_pins={p:{'sha256':sha256((ROOT/p).read_bytes()).hexdigest(),
                       'git_blob':subprocess.check_output(['git','rev-parse',HEAD+':'+p],cwd=ROOT,text=True).strip()} for p in pins})
if __name__=='__main__':
    obj=build(); OUT.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    for key,value in obj['coefficient_bounds'].items():print(key,value,float(F(value)))
    print('reference margin',obj['budget']['new_reference_margin'])
    print('No positive constant arithmetic saving; joint gate remains OPEN.')
