"""Resolved signed open block, exact diagonal main term, and fail-closed residual ledger."""
from pathlib import Path
from fractions import Fraction as F
import json,subprocess,sympy as s
from wp84_full_pair_transfer_degree8 import carrier,offsets,marked_deletions
from wp84_repaired_open_diagonal import diagonal,covariance
ROOT=Path(__file__).resolve().parents[1]
def open_fraction(word,reserve_canonical=True):
    marks=[m for m in marked_deletions(word) if s.isprime(word[m[0]][0])]
    if not marks:return F(0)
    if reserve_canonical and s.isprime(word[-1][0]) and word[-2][0]==word[-1][0] and word[-2][1]==-word[-1][1] and word[-2][2]==word[-1][2]==0:return F(0)
    return F(sum(word[i][2]+word[j][2]!=0 for i,j,lo in marks),len(marks))
def resolved_open_term(word,T,L,a_phi,section):
    """Exact symbolic carrier/root kernel. Caller supplies actual prime powers; deletion marks are ordinary-prime pairs."""
    theta=open_fraction(word);u=offsets(word)
    if u[-1]!=0:raise ValueError('higher word must be closed')
    if not theta:return s.Integer(0)
    d=section[1]-section[0]+1;mn=max(0,d-max(u)+min(u));start=section[0]-min(u)
    if not mn:return s.Integer(0)
    lam=sum(e*s.log(p) for p,e,l in word);phase=sum(e*u[j]*s.log(p)/L for j,(p,e,l) in enumerate(word));coef=s.Rational(theta.numerator,theta.denominator)
    for p,e,l in word:
        alpha=s.log(p)/L;f=1-alpha if l==0 else (1-s.exp(e*2*s.pi*s.I*l*alpha))/(e*2*s.pi*s.I*l)
        factors=s.factorint(p)
        if len(factors)!=1:raise ValueError("leaf must be a prime power")
        base=next(iter(factors))
        coef*= -s.log(base)/(a_phi*L*s.sqrt(p))*f
    # D has its continuous value at zero; otherwise keep exact finite-kernel notation.
    lam=s.expand_log(lam,force=True);D=s.Integer(1) if s.simplify(lam)==0 else s.Function('D_'+str(mn))(lam/L)
    return coef*s.exp(s.I*T*lam+2*s.pi*s.I*(phase+start*lam/L))*s.Rational(mn,d)*D

def hard_lift_zero_lags(lower,pair_prime):
    """Exact injective masked lift of a distinct-prime hard word, not aggregate equivalence."""
    if len(lower) not in (5,6) or any(l for p,e,l in lower):raise ValueError('zero-lag five/six word required')
    if len({p for p,e,l in lower})!=len(lower) or pair_prime in {p for p,e,l in lower}:raise ValueError('disjoint ordinary pair required')
    altered=tuple((p,e,-1 if j in (0,2) else 0) for j,(p,e,l) in enumerate(lower))
    higher=((pair_prime,1,1),(pair_prime,-1,1))+altered
    assert offsets(higher)[-1]==0 and max(offsets(higher))-min(offsets(higher))==2
    assert carrier(higher)==carrier(lower) and open_fraction(higher)==1
    assert offsets(altered)[-1]==-2
    return higher

def residual_inventory():
    return {'ordinary_exact_diagonal':'subtract explicit M_open_8(R), O7=0; repeated groups o(1)','exact_nonzero_alias':'o(1), absolute bound extended to b<=8','proper_power_exact_diagonal':'o(1) by balanced prime-exponent group summation','masked_nonexact_proper_powers':'NOT removed unconditionally; full bounded-eighth signed gate needed','canonical_closed_component':'outside O by reserved definition; remains in complete consumer ledger','near_alias':'OPEN','central_nonexact':'OPEN','transition':'OPEN outside certified short-product cells','far':'OPEN outside certified short-product cells'}
def main():
    x=s.symbols('x');polys={b:sum(s.Rational(v.numerator,v.denominator)*x**i for i,v in enumerate(diagonal(1,b,kind='all'))) for b in (2,4,6,8)}
    k8=s.expand(polys[8]-28*polys[6]*polys[2]-35*polys[4]**2+420*polys[4]*polys[2]**2-630*polys[2]**4)
    opened=diagonal(1);assert opened==list(map(F,['0','0','373/36','-1293/4','36130/9']))
    old=json.loads((ROOT/'notes/WP84_AUGMENTED_OPEN_PATH_PAIR_CERTIFICATE.json').read_text())
    lifts={str(b):hard_lift_zero_lags(tuple((p,1 if j<2 else -1,0) for j,p in enumerate([2,3,5,7,11,13][:b])),17) for b in (5,6)}
    result={'decision':'F','hard_masked_lifts':lifts,'pair_window_multiplier_lower_limit':str(F(49,7744)*F(7,1152)),'ordinary_O7_diagonal':'0 exactly','R1_O8_diagonal_polynomial_in_x':[str(v) for v in opened],'x':'-1/(4*pi^2)','R1_full_diagonal_moments':{str(b):str(v) for b,v in polys.items()},'R1_scalar_kappa8':str(k8),'R6000_diagonal':'explicit finite covariance formula certified; numerical value/sign not evaluated','residual':residual_inventory(),'witness':old['witness'],'allowance_ceiling':old['uncharged_defect_slack'],'partial_variance_payment':old['partial_variance_payment'],'partial_allowance':old['relaxed_slack_after_variance_only'],'fully_paid_budget':'UNCERTIFIED','signed_open_coefficients':old['witness']['p_coefficients'][7:9],'hardness':'masked embedding preserves old carrier/shift, but full signed aggregate comparison uncertified','mu7_mu8':'NO-GO'}
    files=['src/wp84_full_pair_transfer_degree8.py','src/wp84_augmented_open_path_pair_transfer.py','notes/WP84_SIGNED_NEAR_PRODUCT_CELL_DECOMPOSITION.md','notes/WP84_POWER_SCALE_CENTRAL_WINDOW_AND_DENSITY_BRIDGE.md']
    result['parent']='def80b674410ff58361f506f1922cc2e952c646d'
    result['source_blobs']={f:subprocess.check_output(['git','rev-parse','def80b6:'+f],cwd=ROOT,text=True).strip() for f in files}
    (ROOT/'notes/WP84_REPAIRED_OPEN_PATH_SIGNED_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS signed diagonal enumeration; R1 full open main term positive; R6000 explicit formula only')
if __name__=='__main__':main()
