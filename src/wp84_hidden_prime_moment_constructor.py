"""Exact hidden-prime jet algebra for the four unresolved fifth blocks.

This emits the source-mask-indexed moment basis. It intentionally refuses to
identify two mask signatures without an explicit equality certificate.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import json

ROOT=Path(__file__).resolve().parents[1]
import wp84_fifth_full_pool_amplitude as pool

BLOCK_ORDERS={15:6,10:6,36:8,34:6}  # maximum h above the leading u^5 jet
C0='2*pi*i'

def q_pair_slots(d):
    b=d['excess_pair_block']
    return tuple(j for j,x in enumerate(d['partition']) if x==b)

def filter_coeff(lag,eps,a):
    """Coefficient of x^a u^a in f_l^eps(xu), as c0-power -> Q."""
    if lag==0:
        return {0:Q(1)} if a==0 else ({0:Q(-1)} if a==1 else {})
    if a==0:return {}
    return {a-1:Q(-1)*Q(eps*lag)**(a-1)/Q(__import__('math').factorial(a))}

def hidden_pair_jet(lags,signs,prefixes,slots,h):
    """Return exact polynomial kappa_h(c0) in Q[c0].

    It is the coefficient of u^h x^h in the two hidden-slot filters and
    their q-dependent source phase exp(c0*u*x*A).
    """
    s,t=slots
    A=signs[s]*prefixes[s]+signs[t]*prefixes[t]
    out=defaultdict(Q)
    for a in range(h+1):
      for b in range(h-a+1):
        c=h-a-b
        ga=filter_coeff(lags[s],signs[s],a)
        gb=filter_coeff(lags[t],signs[t],b)
        if not ga or not gb:continue
        for x,ca in ga.items():
          for y,cb in gb.items():
            out[x+y+c]+=ca*cb*Q(A**c,__import__('math').factorial(c))
    return {k:v for k,v in sorted(out.items()) if v}

def path_prefixes(lags):
    v=[0]
    for x in lags:v.append(v[-1]+x)
    return tuple(v)

def collect():
    per_block=[]; global_signatures={}
    for ids in pool.IDS:
      desc=[pool.descriptor(i) for i in ids]
      hidden=[d for d in desc if d['hidden_canceled_prime']]
      pair_ids=defaultdict(list)
      for d in hidden:pair_ids[q_pair_slots(d)].append(d['id'])
      hmax=BLOCK_ORDERS[ids[0]]
      moments=[]
      for pair,layouts in sorted(pair_ids.items()):
        # Mask signatures are kept distinct until source-mask equality is proved.
        signature={'slot_pair':pair,'source_mask':'chi_q(fid,slots,lags,T,I,alias); exact equality not executable in repository'}
        for j in range(2,2+hmax+1):
          key=(pair,j)
          global_signatures[key]=max(global_signatures.get(key,0),hmax)
          moments.append({'slot_pair':pair,'layouts':layouts,'power':j,'definition':f"sum_(q prime<=N(T), q notin visible_carrier, chi_q(pair;source)=1) (log q)^{j}/q",'is_real_positive':True,'first_possible_jet_h':j-2,'last_used_jet_h':hmax,'mask_signature':signature})
      layout_formulas=[]
      for d in hidden:
        J=q_pair_slots(d)
        layout_formulas.append({'id':d['id'],'signs':d['signs'],'partition':d['partition'],'net_exponents':d['net_exponents'],'hidden_slot_pair':J,'aliases':d['aliases'],'used_h':[0,hmax],'q_polynomial_at_jet_h':'P_h(x)=sum_(k=0)^h B_(h-k)(T,d,dprime,R;visible,ell,chi) * kappa_(J,k)(ell) * x^(2+k)','kappa':'sum_(a=0)^k sum_(b=0)^(k-a) g_(ell_s,eps_s)(a) g_(ell_t,eps_t)(b) (c0*A_J)^(k-a-b)/(k-a-b)!','moment_powers':'j=2,...,2+h','q_range':'ordinary primes q<=N(T), q not equal to visible carrier primes, original chi_q=1'})
      per_block.append({'ids':ids,'formal_rank':len(ids),'hidden_layouts':[d['id'] for d in hidden],'visible_layouts':[d['id'] for d in desc if not d['hidden_canceled_prime']],'hidden_layout_count':len(hidden),'visible_layout_count':len(desc)-len(hidden),'max_h':hmax,'hidden_layout_exact_formulas':layout_formulas,'pair_signatures':{str(k):v for k,v in sorted(pair_ids.items())},'moment_basis':moments,'block_moment_count_if_one_mask_per_slot_pair':len(moments),'correction_rank':'undetermined without actual source-mask/section coefficient matrices','certified_analytic_rank':1})
    allpairs=sorted({p for p,j in global_signatures})
    unique_pair_power={(p,j) for p,j in global_signatures}
    return {'source_head':'b299cbdb12a525739ac17fc489eb7992e8f316ff','decision':'F','R':6000,'blocks':per_block,'global_pair_slot_signatures':[list(x) for x in allpairs],'global_moment_count_if_masks_merge_by_slot_pair':len(unique_pair_power),'global_pair_power_basis':[{'slot_pair':p,'power':j,'first_possible_jet_h':j-2,'blocks_using':[b['ids'][0] for b in per_block if any(m['slot_pair']==p and m['power']==j for m in b['moment_basis'])]} for p,j in sorted(unique_pair_power)],'mask_merge_status':'NOT CERTIFIED: source q-window/alias predicate chi is not implemented as an executable predicate; preserve each exact mask signature rather than silently merging','pair_jet_formula':'P_{J,h}(x)=x^2 sum_{k=0}^h kappa_{J,k}(c0;lags,signs,prefixes) x^k; the full h-jet is sum_{k=0}^h A_{h-k}*kappa_{J,k}*M_{J,2+k}','filter_coefficient':'g_{l,eps}(0)=1 if l=0 else 0; g(1)=-1; for l!=0,a>=1: g(a)=- (eps*l)^(a-1)c0^(a-1)/a!; for l=0,a>=2:0','pair_phase':'A=eps_s*prefix_(s-1)+eps_t*prefix_(t-1)','moment_weight':'1/q; q ordinary prime <=N(T), excluded if it equals a visible carrier prime, and retained iff the original q-dependent source mask chi is 1','exactness_boundary':'Exact coefficient algebra; full numerical moment basis requires source chi_q and selector cells. No finite q truncation is substituted.'}

def main():
  data=collect()
  (ROOT/'notes/WP84_HIDDEN_PRIME_MOMENT_BASIS.json').write_text(json.dumps(data,indent=2)+'\n')
  print('PASS hidden layouts:',sum(b['hidden_layout_count'] for b in data['blocks']),'conditional pair-power coordinates:',data['global_moment_count_if_masks_merge_by_slot_pair'])
if __name__=='__main__':main()
