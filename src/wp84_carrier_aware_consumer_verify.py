"""Reverify the preserved exact consumer; no new amplitude-safe candidate."""
from fractions import Fraction as F
from pathlib import Path
import json
from wp84_theorem_aware_degree6_verify import square_record
from wp84_signed_near_product_cell_decomposition import ledger

def main():
    rec=square_record([F(-19101,185500),F(961,3710),F(31,50),F(-371,500)],'preserved frozen square')
    assert rec['c5_over_c6']=='-620/371'
    amounts=ledger();c=list(map(F,rec['coefficients']))
    pair_reference=c[0]+c[2]/3+c[6]*F(131,420)
    deficit=pair_reference+F(amounts['band'])+F(amounts['variance'])-F(21,200)
    assert deficit==F(66998281104243827,1144715463675000000)>0
    out={'exact_consumer':rec,'new_carrier_safe_consumer_found':False,
         'search_stopped_at_exact_common_carrier_gate':True,
         'sharp_pair_reference_paid_deficit':str(deficit),
         'requested_previous_ratio':'-1240/371','actual_exact_c5_over_c6':'-620/371',
         'factor_two_error':'-1240/371 equals -2*abs(c5)/c6, not c5/c6',
         'strict_gt79':False,'amplitude_budget_paid':False}
    (Path(__file__).resolve().parents[1]/'notes/WP84_CARRIER_AWARE_CONSUMER_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: preserved rational support/PSD consumer, c4=0, ratio=-620/371; no new amplitude-safe consumer.')
if __name__=='__main__':main()
