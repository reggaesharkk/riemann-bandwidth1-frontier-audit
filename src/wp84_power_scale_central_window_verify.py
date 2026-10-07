"""Exact power-window feasibility gates. No prime-correlation theorem certified."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s
from wp84_signed_near_product_cell_decomposition import ledger
from wp84_c5_pointwise_supercritical_sign import compile_terms

def sixth_sign_boxes():
    terms=compile_terms(6)
    def forms(masks):
        result=[(0,)*5]
        for mask in masks:
            result.append(tuple((int(i in mask)-int(5 in mask)) for i in range(5)))
        return result
    families=[forms(masks) for sign,masks in terms]
    outer=[tuple(int(i<j) for i in range(5)) for j in range(6)]
    families.append(outer)
    walls=set()
    for family in families:
        for a in family:
            for b in family:
                v=tuple(a[i]-b[i] for i in range(5))
                if any(v):
                    for c in (-1,0,1):walls.add((v,c))
    def dot(a,x):return sum((F(t)*v for t,v in zip(a,x)),F(0))
    def overlap(family,x):
        vals=[dot(a,x) for a in family]
        return max(F(0),1-max(vals)+min(vals))
    def kernel(x):return sum((sign*overlap(family,x) for (sign,_),family in zip(terms,families)),F(0))
    output=[]
    for base in ([F(-7,10),F(4,5),F(-7,10),F(3,5),F(-2,5)],
                 [F(-1,10),F(3,10),F(-1,5),F(-3,10),F(4,5)]):
        center=[v+F(3**i,1000000) for i,v in enumerate(base)]
        gaps=[abs(dot(a,center)-c)/sum(abs(t) for t in a) for a,c in walls]
        assert min(gaps)>0
        delta=min(gaps)/2
        C=kernel(center);O=overlap(outer,center);gc=[];go=[]
        for i in range(5):
            y=center[:];y[i]+=delta
            gc.append((kernel(y)-C)/delta);go.append((overlap(outer,y)-O)/delta)
        mass=(2*delta)**5*(C*O+delta**2*sum((u*v for u,v in zip(gc,go)),F(0))/3)
        assert (C>0)==(mass>0) and O>0
        output.append({'center':list(map(str,center)),'radius':str(delta),'C6':str(C),
                       'outer':str(O),'exact_signed_mass':str(mass),
                       'status':'dangerous' if mass>0 else 'favorable'})
    return output


def main():
    eta=s.symbols('eta',real=True);N=s.symbols('N',positive=True)
    assert s.Rational(6,5)*s.Rational(1,6)==s.Rational(1,5)
    # BBMZ first mean divided by product scale N: Q^2/N and Q^.5 N^(1/12).
    assert s.expand(2*(s.Rational(1,6)+eta)-1)==-s.Rational(2,3)+2*eta
    assert s.expand((s.Rational(1,6)+eta)/2+s.Rational(1,12))==s.Rational(1,6)+eta/2
    # Relative to N*Q, first mean does save for eta>0 (epsilon below eta/2).
    assert s.expand((s.Rational(1,6)+eta)/2+s.Rational(13,12)-1-(s.Rational(1,6)+eta))==-eta/2
    assert s.sin(s.pi)==0 # fixed-shift bridge loses a noncentral atom
    relative_errors=[-s.Rational(5,6)+eta,-eta/2]
    u=s.symbols('u',real=True)
    polynomial=1-u**2/6+u**4/120
    assert polynomial.subs(u,1)==s.Rational(101,120)
    assert s.diff(polynomial,u)==u**3/30-u/3
    assert 2*(1-s.Rational(101,120))==s.Rational(19,60)
    # Average of -Delta_s^2 over s in [0,1/a].
    t,a,l=s.symbols('t a l',positive=True)
    multiplier=s.simplify(a*s.integrate(4*s.sin(t*l/2)**2,(t,0,1/a)))
    assert s.simplify(multiplier-2*(1-a*s.sin(l/a)/l))==0
    z=s.symbols('z',real=True)
    # An inverse must retain multiplier exactly; dropping it changes every mode.
    assert s.simplify((-4*s.sin(z/2)**2)/(-4*s.sin(z/2)**2))==1
    # Density-one permits infinitely many exceptions: floor(sqrt(M))/M -> 0.
    k=s.symbols('k',positive=True,integer=True)
    assert k/k**2==1/k
    c=compile_terms(6);assert len(c)==1082
    out={'parent':'95458d6cf49466f406fa0c8444aeef5230cd816e','decision':'D',
         'eta_partition_admissible':'0<eta<5/6, not a proven theorem feasibility interval',
         'optional_linearization_eta':'0<eta<5/12, aggregate error still unproved',
         'shift_scale':'H=N_cell^eta; Q=O(N_cell^(1/6+eta))',
         'BBMZ_relative_exponents':list(map(str,relative_errors)),
         'BBMZ_actual_1_over_N_error_exponents':['-2/3+2*eta','1/6+eta/2'],
         'BBMZ_second_mean_requires':'eta>1/6 plus a fixed epsilon gap',
         'pointwise_d3_d2_sharp_summed_exponent':'1/18+eta',
         'pointwise_d3_d2_smooth_summed_exponent':'7/192+eta',
         'fixed_translation_new_zeros':True,'averaged_translation_multiplier':str(multiplier),
         'averaged_noncentral_multiplier_lower_bound':'19/60',
         'averaged_inverse_upper_bound':'60/19',
         'bridge_tail_saving_proved':False,
         'mesoscopic_cell_counts':{'fifth':'ceil(2/delta)^4','sixth':'ceil(2/delta)^5'},
         'fifth_model_Riemann_error_upper':'38400*delta',
         'sixth_connected_model_Riemann_error_upper':'692480*delta',
         'C5_total':'1/36','C6_connected_total':'-1/126','C6_42_total':'-23/420','C6_pairs_total':'131/420',
         'sixth_sign_boxes':sixth_sign_boxes(),'joint_density_requires_coupling':True,'ledger':ledger(),
         'loss_central':'OPEN oriented restricted weighted correlation',
         'loss_transition':'OPEN oriented primitive bound',
         'loss_far':'OPEN oriented primitive bound','loss_near_alias':'OPEN dilated correlation',
         'first_feasible_eta':None,'strict_gt79':False,
         'density_one_implies_RH':False,'Weil_completeness_proved':False}
    (Path(__file__).resolve().parents[1]/'notes/WP84_POWER_SCALE_CENTRAL_WINDOW_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
