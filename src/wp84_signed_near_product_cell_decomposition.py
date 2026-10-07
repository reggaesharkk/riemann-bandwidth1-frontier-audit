"""Exact signed-cell support, ledger, Abel and geometric reconnaissance gates.
Finite identities do not certify the arithmetic inequality. No cutoff changes.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import csv
import json
import sympy as sp
from wp84_c5_pointwise_supercritical_sign import arrangement,c5,outer_overlap,dot

ROOT=Path(__file__).resolve().parents[1]
A=F(11501,12500); B=F(137641,250000)


def check(ok,label):
    if not ok: raise ValueError(label)


def ledger():
    a=[F(-19101,185500),F(961,3710),F(31,50),F(-371,500)]
    c=[sum((a[r]*a[s] for r in range(4) for s in range(4) if r+s==b),F(0)) for b in range(7)]
    band=3*F(137721,5000)*F(106,333)**2/6000
    var=-2*c[2]*F(106,333)**2/6000
    base=c[0]+c[2]/3
    j=F(21,200)-band-var-base
    ideal=F(21,200)-band-var-(base-A/36+B*F(157,630))
    relaxed=F(21,200)-band-var-(base-A/36+B*F(34,135))
    check(c[4]==0 and -c[5]==A and c[6]==B,'consumer coefficients')
    check(j==F(64788151489666079,572357731837500000),'signed target')
    check(ideal==F(27704610381502,17886179119921875),'ideal ledger')
    check(relaxed==F(52897896569489,572357731837500000),'relaxed ledger')
    return {'coefficients':list(map(str,c)),'signed_target':str(j),'band':str(band),'variance':str(var),
            'ideal_slack':str(ideal),'conservative_slack':str(relaxed),
            'illustrative_half_ideal_cell_allowance':str(ideal/2),
            'illustrative_half_conservative_cell_allowance':str(relaxed/2),
            'fifth_fraction_model_sixth':str(1-36*ideal/A),
            'fifth_fraction_relaxed_sixth':str(1-36*relaxed/A),
            'sixth_6_fraction_full_fifth_with_42':str(F(2,3)-126*relaxed/B)}


def alias_support():
    # Exact support endpoints at representative natural L; rational bounds prove
    # eventual tables when b/sqrt(L)<1/2. No prime existence asserted.
    L=F(10000); lo=F(1,10000); cut=F(99,100)
    rows=[]
    for b in [5,6]:
        for r in range(b+1):
            s=b-r
            lower=r*lo-s*cut; upper=r*cut-s*lo
            bins=[m for m in range(-7,8) if lower<m+F(1,2) and upper>=m-F(1,2)]
            resonances=[m for m in range(-7,8) if lower<=m<=upper]
            check(bins==list(range(-s,r+1)),'nearest alias bin support')
            expected=list(range(-s+1,r))
            if r==0: expected=list(range(-s+1,0))
            if s==0: expected=list(range(1,r))
            check(resonances==expected,'near-resonance support')
            rows.append({'b':b,'positive_slots':r,'negative_slots':s,
                         'nearest_bins':bins,'resonance_support':resonances})
    return rows


def model_cell():
    x=[F(603,1000),F(-397,1000),F(598,1000),F(-406,1000)]
    hyperplanes=arrangement()
    delta=min(abs(dot(a,x)-c)/sum(abs(t) for t in a) for a,c in hyperplanes)/2
    check(delta==F(49,1500),'exact affine-cell radius')
    for a,c in hyperplanes:
        check(abs(dot(a,x)-c)>delta*sum(abs(t) for t in a),'all walls excluded')
    C,O=c5(x),outer_overlap(x)
    gradC=[];gradO=[]
    for i in range(4):
        y=x[:];y[i]+=delta
        gradC.append((c5(y)-C)/delta)
        gradO.append((outer_overlap(y)-O)/delta)
    for corner in product([-1,1],repeat=4):
        y=[x[i]+delta*corner[i] for i in range(4)]
        check(c5(y)==C+delta*sum(gradC[i]*corner[i] for i in range(4)),'affine C5 corners')
        check(outer_overlap(y)==O+delta*sum(gradO[i]*corner[i] for i in range(4)),'affine outer corners')
    mass=(2*delta)**4*(C*O+delta**2*sum(u*v for u,v in zip(gradC,gradO))/3)
    check(mass==F(1505310601921,2135742187500000000),'exact cell integral')
    check(0<mass<F(1,36),'positive incomplete model mass')
    # First four signed free coordinates; fifth exponent follows closure.
    bounds=[(abs(x[i])-delta,abs(x[i])+delta) for i in range(4)]
    bounds.append((sum(x)-4*delta,sum(x)+4*delta))
    check(all(0<l<u<1 for l,u in bounds),'natural interior support')
    return {'free_center':list(map(str,x)),'delta':str(delta),'orientation':[1,-1,1,-1,-1],
            'prime_exponent_intervals':[[str(l),str(u)] for l,u in bounds],
            'C5_center':str(C),'outer_center':str(O),'C5_gradient':list(map(str,gradC)),
            'outer_gradient':list(map(str,gradO)),'exact_model_cell_mass':str(mass),
            'exact_total_complement_mass':str(F(1,36)-mass),
            'exact_subcritical_model_mass':'0','exact_small_factor_boundary_mass':'0',
            'fraction_of_total_model_mass':str(36*mass),
            'arithmetic_fraction_certified':'0'}


def finite_gates():
    # Hard central masks do not preserve the PSD of a sampled correlation kernel.
    hard=sp.Matrix([[1,1,0],[1,1,1],[0,1,1]])
    check(hard.det()==-1,'hard-window Gram counterexample')
    completion=sp.Matrix([[0,-sp.Rational(A.numerator,A.denominator)/2],
                          [-sp.Rational(A.numerator,A.denominator)/2,sp.Rational(B.numerator,B.denominator)]])
    check(completion.det()<0,'signed 2/3-array form indefinite')
    x=sp.symbols('x',real=True)
    # The nonoriented radial real count is insufficient: i at +x and -i at -x.
    check(sp.re(sp.I*sp.exp(sp.I*x)-sp.I*sp.exp(-sp.I*x))==-2*sp.sin(x), 'orientation loss witness')
    y=sp.symbols('y',nonnegative=True)
    aa=sp.Rational(A.numerator,A.denominator);bb=sp.Rational(B.numerator,B.denominator)
    check(sp.expand(bb*y**6-aa*y**5-bb*y**6/2-y**5*(bb*y/2-aa))==0, 'coercivity identity')
    # Exact summation-by-parts identity, with a polynomial test kernel and complex weights.
    points=[F(1,7),F(2,5),F(4,5)]; weights=[1+sp.I,-2+3*sp.I,4-sp.I]
    kernel=lambda z: z*z+sp.I*z+1
    direct=sum(weights[i]*kernel(sp.Rational(p.numerator,p.denominator)) for i,p in enumerate(points))
    end=sp.Rational(1); cum=0; integral=0
    for i,p in enumerate(points):
        cum+=weights[i]
        upper=points[i+1] if i+1<len(points) else F(1)
        integral+=cum*sp.integrate(sp.diff(kernel(x),x),(x,sp.Rational(p.numerator,p.denominator),sp.Rational(upper.numerator,upper.denominator)))
    check(sp.expand(direct-(cum*kernel(end)-integral))==0,'oriented complex Abel formula')
    # Proper-power coefficient higher masses: v=2 first mass has nonvanishing log scale;
    # all j>=2 bound an absolutely convergent base-prime geometric series.
    return {'hard_window_Gram_determinant':'-1','local_completion_determinant':str(completion.det()),
            'radial_count_counterexample':'weights i at +x and -i at -x: A_abs=0, contribution=-2 sin(tau*x)',
            'Abel_test':'PASS','proper_power_first_mass_limit':'1/2',
            'proper_power_coefficient_mass_orders':[2,3,4,5,6],
            'proper_power_high_moment_deletion_proved':False,
            'proper_power_bounded_signed_gate_equivalence_proved':True,
            'proper_power_Schatten6_norm_order':'O_R(L^(-1/3))',
            'coercive_radius':str(2*A/B)}


def coverage_grid(write):
    # Coarse rational quarter-log cells. Full exact coverage is the H-polytope
    # in the note; boxes crossing its boundary are deliberately not marked closed.
    records=[];counts={}
    for b,r in [(5,2),(6,2),(6,3)]:
        s=b-r
        for ix in product(range(4),repeat=b):
            lo=[F(k,4) for k in ix]; hi=[F(k+1,4) for k in ix]
            ul=sum(lo[:r]); uh=sum(hi[:r]); vl=sum(lo[r:]); vh=sum(hi[r:])
            possible=max(ul,vl)<=min(uh,vh)
            short=uh+vh<2
            if not possible: status='CENTRAL_SUPPORT_EMPTY'
            elif short: status='SHORT_PRODUCT_BOUND_CLOSED'
            else: status='UNCONTROLLED_OR_BOUNDARY_SPLIT_REQUIRED'
            key=f'{b}:{r}:{status}'; counts[key]=counts.get(key,0)+1
            records.append([b,r,s,','.join(map(str,lo)),','.join(map(str,hi)),str(ul),str(uh),str(vl),str(vh),status])
    if write:
        with (ROOT/'notes/WP84_SIGNED_NEAR_PRODUCT_EXPONENT_CELLS.csv').open('w',newline='') as f:
            writer=csv.writer(f);writer.writerow(['degree','positive_slots','negative_slots','alpha_lower','alpha_upper',
                                                'A_exp_lower','A_exp_upper','B_exp_lower','B_exp_upper','central_status'])
            writer.writerows(records)
    check(len(records)==9216,'complete coarse cell grid')
    return {'grid':'quarter-log intervals; natural cutoff intersects each box at 1-1/sqrt(L)',
            'row_count':len(records),'counts':counts,'closed_arithmetic_model_C5_mass':'0',
            'uncovered_polytope':'0<=alpha_i<=1-1/sqrt(L); sum_plus alpha=sum_minus alpha=gamma; gamma>=1',
            'all_but_one_cell_closed':False}


def main(write):
    cert={'parent':'40684faa2fc278d319b89df2550e82eb874ae0c7','decision':'D',
          'decision_scope':'audited number-theory theorems do not cover the specified resolved cell',
          'strict_gt79':False,'arithmetic_theorem_proved':False,'R_band':6000,'pole_height':'221/200',
          'ledger':ledger(),'alias_support':alias_support(),'model_cell':model_cell(),
          'finite_gates':finite_gates(),'coverage':coverage_grid(write),
          'continuation_replay':'WP84_RESTRICTED_SHIFTED_CONVOLUTION_REPLAY.json',
          'restricted_shift_kernel':'K_T(n,h), not an h-only weight',
          'H_optimized':False,'remaining_open':['near aliases',
               'long-product far and transition terms','supercritical central cells','cell-model identification']}
    if write:
        (ROOT/'notes/WP84_SIGNED_NEAR_PRODUCT_CELL_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: independent rational ledger, all sign-pattern alias supports, affine C5 cell integral, oriented Abel and hostile Gram gates.')
    print('C5 positive cell mass:',cert['model_cell']['exact_model_cell_mass'])
    print('Covered short-product model fifth mass = 0; arithmetic fraction certified = 0.')
    print('Decision D: specific supercritical cell is not covered by the audited theorem hypotheses. Multiple other sectors remain open.')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');main(p.parse_args().write)
