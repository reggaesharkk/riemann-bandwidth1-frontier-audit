"""Exact source-amplitude constructors and omitted balanced-prime moments.

This is a lazy symbolic constructor. It does not truncate the source prime pool.
"""
from pathlib import Path
from collections import defaultdict
from itertools import product
from fractions import Fraction as Q
from math import factorial
import json
ROOT=Path(__file__).resolve().parents[1]
FUNCS=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
CERT=json.loads((ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json').read_text())
IDS=[[15,20,26,28,31,32],[10,12,16,17,21,22,25,29],[36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69],[34,37,39,43,53,56,60,63]]
R_SOURCE=6000

def descriptor(fid):
 f=FUNCS[fid];pi=tuple(map(int,f['equality_partition'].split(',')));eps=tuple(1 if x=='+' else -1 for x in f['sign_word']);nu=tuple(pi.count(b) for b in range(max(pi)+1));e=tuple(sum(eps[i] for i in range(5) if pi[i]==b) for b in range(len(nu)))
 assert sum(nu)==5 and sum((nu[b]-abs(e[b]))//2 for b in range(len(nu)))==1
 excess=next(b for b in range(len(e)) if nu[b]>abs(e[b]))
 return {'id':fid,'signs':eps,'partition':pi,'multiplicities':nu,'net_exponents':e,'excess_pair_block':excess,'hidden_canceled_prime':e[excess]==0,'aliases':f['aliases']}

def paths(R):
 """Yield all exact closed five-step displacement words; huge for R=6000."""
 for l in product(range(-R,R+1),repeat=4):
  last=-sum(l)
  if -R<=last<=R:yield (*l,last)

def root_count(section,lag):
 kminus,kplus=section;v=[0]
 for x in lag:v.append(v[-1]+x)
 return max(0,kplus-kminus+1-(max(v)-min(v)))

def source_amplitude_entry(fid,carrier,T,section,core_primes=None):
 """Exact finite-sum specification at a source cell, returned lazily.

    carrier: sorted (ordinary prime, net exponent) vector.
    section: actual source-selected inclusive endpoint pair (k_-,k_+).
    core_primes=None means every ordinary prime <= N(T).
    A set means a diagnostic core restriction and is never source-legal.
    Every path, assignment, mask and source normalization remains explicit.
 """
 f=FUNCS[fid];d=descriptor(fid);L=__import__('math').log(T/(2*__import__('math').pi));N=int(__import__('math').exp(L-L**.5));kminus,kplus=section;n=kplus-kminus+1
 assert n>0
 # Return the exact summand schema because an R=6000 path expansion is enormous.
 return {'id':fid,'T':T,'L':L,'N':N,'section':section,'n':n,'R':R_SOURCE,'carrier':carrier,'complete_pool':core_primes is None,'prime_domain':'ordinary primes p<=N satisfying the original slot-window masks','assignment_rule':'injective primes on equality blocks, exact net valuation carrier','path_rule':'l in [-6000,6000]^5, sum l=0','root_sum':'exp(c0*i_min*lambda/L)/n * sum_(r=0)^(max(0,n-range(prefix))-1) exp(c0*r*lambda/L)','slot_filter':'f_0=1-alpha; f_l^eps=(1-exp(eps*2*pi*i*l*alpha))/(eps*2*pi*i*l)','row_phase':'exp(2*pi*i*u*sum_slot eps*prefix_before_slot*log(p_slot)/L)','slot_coefficient':'-log(p_slot)/(a_phi(T)*L*sqrt(p_slot))','alias_mask':'nearest source alias m and 0<|log(carrier)-m*L|<=H/T','real_part':True,'normalization':'exact source a_phi(T), n; positive carrier has Re factor 1/2'}

def prime_moment_decomposition(fid,carrier,core,N):
 """Exact identity for a fixed carrier, one balanced pair, and one jet h.

    S_r(N;A,K)=sum_{q<=N prime, q notin A union K} (log q)^r/q.
    The omitted coefficient is sum_{r=2}^{2+h} C_{h,r} S_r.
    Coefficients C depend on actual visible assignments, path and section.
 """
 d=descriptor(fid)
 hidden=d['hidden_canceled_prime']
 return {
  'id':fid,
  'excess_pair_block':d['excess_pair_block'],
  'excess_pair_slot_positions':[j for j,b in enumerate(d['partition']) if b==d['excess_pair_block']],
  'excess_pair_is_hidden':hidden,
  'balanced_slot_window_signature':('intersection of chi over the two slots' if hidden else 'not applicable: excess pair is attached to the visible carrier prime'),
  'balanced_multiplicity':2,
  'carrier_visible_primes':'prime factors with nonzero net valuation',
  'selected_core':sorted(core),
  'omitted_set':('{q prime: q<=N, q not a carrier-visible prime, q not in selected core}' if hidden else 'empty: excess occurrences belong to a visible carrier prime'),
  'moment_definition':'S_(r,eta)(N;A,K)=sum_{q<=N prime, q notin A union K, balanced-pair source-window signature eta}(log q)^r/q',
  'jet_formula':({f'h={h}':f'E_{h}=sum_eta sum_(r=2)^{2+h} C_{{{h},r,eta}}(visible primes;R=6000;I(T);chi) * S_(r,eta)(N;A,K)' for h in range(0,9)} if hidden else {f'h={h}':'E_h=0 for the independent canceled-prime omission; all five occurrences belong to visible carrier blocks' for h in range(0,9)}),
  'order5':('E_0=sum_eta C_(0,2,eta)*S_(2,eta); each term is nonpositive in the normalized positive carrier amplitude; S2 is common only when all columns have identical pair-window signatures' if hidden else 'E_0=0 for independent canceled-prime omission; repeated occurrences are fixed by visible carrier primes'),
  'exactness':('Taylor coefficients of the two hidden balanced-slot factors and all other slot factors are polynomials in log q. Every extra log q power is counted in r. No prime q is dropped.' if hidden else 'No independent canceled-prime variable exists in this layout; the repeated prime is fixed by the carrier.')
 }

def iter_source_atoms(fid, carrier, T, N, section, prime_stream, source_mask,
                      core_primes=None, R=R_SOURCE):
    """Yield exact symbolic summands; never silently shortens prime/path sets.

    prime_stream must be the COMPLETE source prime set <=N(T), and
    source_mask(fid,slots,lags,T,section,m) must check every original window/alias indicator exactly.
    Values are expression records (logs/exponentials remain symbolic), so
    this is an exact constructor rather than floating-point evaluation.
    """
    f=FUNCS[fid];d=descriptor(fid);primes=tuple(prime_stream)
    kminus,kplus=section;n=kplus-kminus+1
    assert n>0 and all(2<=p<=N for p in primes)
    assert tuple(sorted(set(primes)))==tuple(sorted(primes)), 'prime stream must be sorted and duplicate-free'
    target=tuple(sorted(carrier));eps=d['signs'];pi=d['partition'];nb=len(d['multiplicities'])
    for assignment in product(primes, repeat=nb):
        if len(set(assignment))!=nb:continue
        if core_primes is not None and d['hidden_canceled_prime'] and assignment[d['excess_pair_block']] not in core_primes:continue
        valuation=defaultdict(int)
        for block,q in enumerate(assignment):valuation[q]+=d['net_exponents'][block]
        got=tuple((q,e) for q,e in sorted(valuation.items()) if e)
        if got!=target:continue
        slots=tuple(assignment[pi[j]] for j in range(5));lam=('sum_eps_log_slots',tuple((eps[j],slots[j]) for j in range(5)))
        for lag in paths(R):
            aliases=[m for m in f['aliases'] if source_mask(fid,slots,lag,T,section,m)]
            if not aliases:continue
            v=[0]
            for h in lag:v.append(v[-1]+h)
            span=max(v)-min(v);count=max(0,n-span)
            if count==0:continue
            imin=kminus-min(v)
            for alias in aliases:
                yield {'id':fid,'carrier':target,'block_primes':assignment,'slot_primes':slots,
                  'lags':lag,'prefixes':tuple(v),'source_root_interval':(imin,imin+count-1),
                  'root_sum_expression':('exp',('i*2pi*i_min*lambda/L',imin,lam,L),
                     ('sum',count,('exp',('i*2pi*r*lambda/L','r',lam,L)))),
                  'normalized_root_divisor':n,'slot_coefficients':tuple(('minus_log_over_a_phi_L_sqrt',slots[j],T) for j in range(5)),'filter_expressions':tuple(('f',lag[j],eps[j],slots[j],L) for j in range(5)),
                  'slot_phase_expression':('exp',('i*2pi/L',tuple((eps[j],v[j],slots[j]) for j in range(5)),L)),
                  'carrier_character':('exp_iTlambda',lam,T),'alias':alias,
                  'delta_expression':('sum_eps_log_slots',tuple((eps[j],slots[j]) for j in range(5)),'minus',alias,'*L(T)'),
                  'source_mask':True,'common_slot_coefficient':Q((-1)**5,2*n),
                  'normalization':'a_phi(T)^-5 is retained in product slot factors'}


def blocks():
 result=[]
 for ids in IDS:
  ds=[descriptor(i) for i in ids]
  # Net carrier is fixed by the first descriptor; visible blocks are its nonzero exponents.
  d=ds[0];visible=[j for j,e in enumerate(d['net_exponents']) if e]
  result.append({'ids':ids,'descriptors':ds,'visible_block_indices':visible,'excess_pair_block_indices':[x['excess_pair_block'] for x in ds],'every_layout_has_one_excess_pair':True,'hidden_pair_ids':[d['id'] for d in ds if d['hidden_canceled_prime']],'visible_excess_pair_ids':[d['id'] for d in ds if not d['hidden_canceled_prime']],'core_pool':[2,3,5,7,11,13],'source_prime_cutoff':'N(T)=floor(exp(L-sqrt(L)))','source_section':'I(T)=[k_-(T),k_+(T)] chosen by source; d\'=|I|, d=floor(TL/(2pi)), d\'/d->1','moment_decomposition':[prime_moment_decomposition(i,None,[2,3,5,7,11,13],None) for i in ids],'source_matrix_schema':{'formula':'A_j(T)=Re sum_{p_blocks injective, carrier v} sum_{l in [-6000,6000]^5, sum l=0} chi_j(p,l,T) * product_slot[-log p/(a_phi L sqrt p)*f_l^eps(log p/L)] * exp(2*pi*i*sum eps*prefix_before*log p/L) * exp(i*T*lambda+2*pi*i*i_min*lambda/L)/n * sum_(k=0)^(max(0,n-range(prefix))-1) exp(2*pi*i*k*lambda/L)','section':'actual I(T)=[k_-(T),k_+(T)] only','root_count':'max(0,n-range(prefix))','masks':'the exact source slot-window/equality/alias masks chi_j; no finite pool restriction','core_decomposition':'for hidden-pair layouts, fix all visible carrier primes and sum the excess net-zero block over q in K; omitted q is every source-admissible prime <=N outside K and visible carrier primes. For visible-excess layouts the repeated prime is fixed by the carrier and there is no canceled-prime tail.'},'leading_omitted_moment':'for hidden-pair columns, positive S_(2,eta) times a column-specific visible coefficient; visible-excess columns have E_h=0 for the independent balanced-prime omission.'})
 return result

def main():
 data={'source_head':'fc04f3b3440adb2862a47e73e1a02db3f0deb0e3','decision':'F','four_blocks':blocks(),'matrix_difference':'M_source-M_formal=(M_full(T,N,R,I,logs,a_phi)-M_core(T,N,R,I,logs,a_phi))+(M_core(T,N,R,I,logs,a_phi)-M_core(T,n0,R0,I0,z,1)); first term is exact omitted-prime sum; second is section+band+prime-coordinate+normalization difference','section_root_identity':'after common translation, coefficient u^h is c0^h*lambda^h/n * sum_(j=0)^h (-minprefix)^(h-j)*S_j(n-span)/((h-j)!*j!), S_j(M)=sum_(r=0)^(M-1)r^j','R':6000,'diagnostic_R_values':[1,2],'large_section':'source d prime-scale with dprime/d->1; n is source-selected; higher root jets grow polynomially in n and fixed-cell expansion is not uniform in n','no_rank_claim_beyond38':True}
 (ROOT/'notes/WP84_FIFTH_FULL_POOL_LIFT_CERTIFICATE.json').write_text(json.dumps(data,indent=2)+'\n')
if __name__=='__main__':main()
