"""Exact SOS parameterization, surrogate obstruction, and hostile fallback duals.
Does not identify sharp geometry with the finite arithmetic measure.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import sympy as s
from wp84_signed_near_product_cell_decomposition import ledger

ROOT=Path(__file__).resolve().parents[1]
MU=list(map(s.Rational,[1,0,F(1,3),0,F(1,4),F(1,36),F(157,630)]))
X,y=s.symbols('X y',real=True)
def rational(z):return s.Rational(z.numerator,z.denominator) if isinstance(z,F) else s.Rational(z)
def coef(G):return [sum(G[i,j] for i in range(4) for j in range(4) if i+j==k) for k in range(7)]
def principal_minors(G):
    values=[G.extract(ix,ix).det() for k in range(1,5) for ix in combinations(range(4),k)]
    assert all(v>=0 for v in values)
    return list(map(str,values))
def square_record(a,label):
    a=list(map(rational,a));G=s.Matrix(a)*s.Matrix(a).T;c=coef(G)
    q=sum(a[i]*X**i for i in range(4));support=s.Poly(s.expand(q.subs(X,-1-y)**2-1),y)
    assert all(z>=0 for z in support.all_coeffs())
    E=sum(c[i]*MU[i] for i in range(7));assert c[4]==0
    return {'label':label,'q_centered':str(q),'G':[[str(x) for x in row] for row in G.tolist()],
            'principal_minors':principal_minors(G),'coefficients':list(map(str,c)),
            'support_p_minus_one_nonnegative_y_coefficients':list(map(str,support.all_coeffs())),
            'c5_over_c6':str(c[5]/c[6]) if c[6] else None,'model_defect':str(E),
            'model_simple_zero_coefficient':str(1-2*E),
            'lower_moment_part':str(c[0]+c[2]/3),'c4_part':'0','fifth_part':str(c[5]/36),
            'sixth_pair_part':str(c[6]*s.Rational(131,420)),
            'sixth_42_part':str(-c[6]*s.Rational(23,420)),
            'sixth_6_part':str(-c[6]/126)}
def main():
    # PSD Gram coefficient identities.
    symbols=s.symbols('g00 g01 g02 g03 g11 g12 g13 g22 g23 g33')
    a,b,c,d,e,f,g,h,i,j=symbols
    G=s.Matrix([[a,b,c,d],[b,e,f,g],[c,f,h,i],[d,g,i,j]])
    assert coef(G)==[a,2*b,2*c+e,2*d+2*f,2*g+h,2*i,j]
    # Exact degree-two dual, after disjoint-domain safety forces G33=G22=0.
    v=s.Matrix([1,-1]);M=s.diag(1,s.Rational(1,3));D=M-v*v.T/4
    assert D==s.Matrix([[s.Rational(3,4),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,12)]])
    assert D.det()==0 and D.trace()>0
    # Positive quadrature, matching every coefficient except the forced zero c4,c5.
    nodes=[s.Rational(-1),s.Rational(-1,2),s.Integer(0),s.Rational(1,2),s.Integer(1)]
    weights=[s.Rational(1151,9450),s.Rational(848,4725),s.Rational(626,1575),s.Rational(848,4725),s.Rational(1151,9450)]
    moments=[sum(w*t**k for w,t in zip(weights,nodes)) for k in range(7)]
    assert all(w>0 for w in weights)
    assert all(moments[k]==MU[k] for k in [0,1,2,3,6])
    assert moments[5]==0
    bound=1-2*weights[0];assert bound==s.Rational(3574,4725)<s.Rational(79,100)
    frontier=s.factor(36*(s.Rational(21,200)-weights[0]))
    # The original rational square is valid but arithmetic-inaccessible.
    original=square_record([F(-19101,185500),F(961,3710),F(31,50),F(-371,500)],'frozen_original')
    linear=square_record([F(-1,4),F(3,4),0,0],'exact_safe_disjoint_proxy_optimum')
    cubic=square_record([F(157,787),0,0,F(-630,787)],'c5_zero_single_square_hostile')
    assert linear['model_defect']=='1/4'
    # A negative geometric coefficient times a negative real sampled kernel is positive.
    realD=(2-s.sqrt(5))/6;assert realD<0 and -realD>0
    # Literal unshifted centered support at zero would yield E>=1/2 already.
    M6=s.Matrix(4,4,lambda i,j:MU[i+j]);dual0=M6-s.diag(s.Rational(1,2),0,0,0)
    assert all(dual0[:k,:k].det()>0 for k in range(1,5))
    parent=json.loads((ROOT/'notes/WP84_POWER_SCALE_CENTRAL_WINDOW_CERTIFICATE.json').read_text())
    region={'sixth_positive_U_box':parent['sixth_sign_boxes'][0],
            'sixth_negative_U_box':parent['sixth_sign_boxes'][1],
            'fifth_sharp_kernel_nonnegative':True,'ratio_on_disjoint_sixth_domain':'0',
            'ratio_on_fifth_domain':'undefined (K6=0)',
            'global_safe_proxy_requires':'c6=0 -> PSD row 3 zero -> c4=0 -> row 2 zero -> quadratic',
            'actual_positive_measure_transfer_proved':False,
            'sampled_negative_real_kernel':str(realD)}
    dual={'scope':'EXACT disjoint sharp-proxy obstruction and c5=0 model bound; not a dual for an unidentified actual joint kernel',
          'quadratic_dual_matrix':[[str(z) for z in row] for row in D.tolist()],
          'quadratic_lower_model_defect':'1/4','quadratic_upper_simple_zero_coefficient':'1/2',
          'fallback_nodes':list(map(str,nodes)),'fallback_weights':list(map(str,weights)),
          'fallback_moments':list(map(str,moments)),
          'c5_zero_model_lower_defect':str(weights[0]),'c5_zero_model_upper_coefficient':str(bound),
          'Pareto_outer_bound':'E_model >= 1151/9450 + c5/36 (c4=0)',
          'necessary_c5_for_model_gt79':str(frontier),'exact_full_Pareto_frontier_proved':False}
    certificate={'parent':'195928861e6227d6b7cd824fd35b7eccda7d139c','decision':'D',
       'actual_safe_consumer_found':False,'actual_degree6_impossibility_proved':False,
       'first_uncertified_step':'joint kernel coupling and positive arithmetic measure for sign transfer',
       'coefficient_parameterization':list(map(str,coef(G))),'centered_support':'X<=-1; physical x=X+1<=0',
       'exact_candidates':[original,linear,cubic],'ledger_frozen':ledger(),
       'proper_power_and_exact_alias_closures_preserved':True,
       'strict_gt79':False,'new_candidate_band_charges_certified':False,
       'numerical_candidates_promoted':False}
    for name,value in [('WP84_DEGREE6_CONSUMER_EXACT_CERTIFICATE',certificate),
                       ('WP84_DEGREE6_CONSUMER_REGION_SIGN_CERTIFICATE',region),
                       ('WP84_DEGREE6_CONSUMER_DUAL_OBSTRUCTION_CERTIFICATE',dual)]:
        (ROOT/'notes'/f'{name}.json').write_text(json.dumps(value,indent=2)+'\n')
    print('PASS: Gram coefficients, exact PSD/support certificates, quadratic safe-proxy dual, c5-zero positive quadrature, sign-transfer falsifier.')
    print('c5=0 upper model percentage:',float(100*bound),'necessary c5:',frontier)
    print('D: actual safe-consumer theorem not certified; numerical output is discovery only.')
if __name__=='__main__':main()
