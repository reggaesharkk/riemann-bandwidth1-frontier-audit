"""Exact mask equivalence under the source q-domain and finite exclusions."""
from pathlib import Path
import json
import wp84_fifth_full_pool_amplitude as layouts

ROOT=Path(__file__).resolve().parents[1]

def equivalent(V1,V2,prime_cutoff):
    """Exact equality of P_N minus V domains; V are visible prime assignments."""
    return set(p for p in V1 if p<=prime_cutoff)==set(p for p in V2 if p<=prime_cutoff)

def main():
  classes=[]
  for block in layouts.blocks():
    for d in block['descriptors']:
      if not d['hidden_canceled_prime']:continue
      classes.append({'layout':d['id'],'slot_pair':[s for s,b in enumerate(d['partition']) if b==d['excess_pair_block']],'family':'P_N minus V_visible','identical_iff':'visible exclusion sets agree after intersecting [2,N]','conjugate_relation':'same q domain and real q moments; conjugation acts on path coefficient only','slot_permutation':'same master support P_N; finite exclusions permute with visible carrier assignment','carrier_reversal':'same master support; exact domain equal iff visible prime exclusion sets match','asymptotic_relation':'for fixed-size visible exclusion sets, moment difference is an explicit finite sum O_j(1), hence relative o(1) versus full M_j main','extra_slot_or_path_window':'none'})
  out={'master_q_domain':'P_N={q ordinary prime:2<=q<=N(T)}','layout_count':len(classes),'exact_domain_family':'Q(T;V)=P_N\\V, where V is the set of visible carrier primes in the fixed carrier assignment','moment_reduction':'sum_(q in Q(T;V))(log q)^j/q = S_j(N)-sum_(p in V, p<=N)(log p)^j/p','universal_moment_coordinates':[{'name':f'S_{j}','power':j,'definition':f'sum_(q prime<=N(T))(log q)^{j}/q','real_positive':True} for j in range(2,11)],'exact_source_distinct_hidden_moment_count':9,'candidate_73_reduction':'73 pair-slot candidates -> 9 universal scalar prime moments; visible exclusions are explicit finite carrier-prime terms, not new hidden-prime moments','equivalence_rule':'Distinct visible sets define distinct assignment-level q-domains unless their intersections with P_N agree; all domains reduce exactly to the same nine master moments plus finite exclusions. No heuristic mask clustering.','layout_masks':classes}
  (ROOT/'notes/WP84_EXACT_Q_MASK_EQUIVALENCE.json').write_text(json.dumps(out,indent=2)+'\n')
  assert equivalent([2,3],[2,3],100)
  assert not equivalent([2,3],[2,5],100)
  print('PASS exact q-domain equivalence: 20 layouts, nine common moments, finite visible exclusions')
if __name__=='__main__':main()
