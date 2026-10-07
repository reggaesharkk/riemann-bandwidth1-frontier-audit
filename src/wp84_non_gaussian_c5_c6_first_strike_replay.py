"""Independent Fraction-only first-strike scalar certificate replay.

Does not import the producer or prove a prime moment theorem. The reference
pair-sector constants are the pinned geometric integrals, not prime inputs.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def check(ok, label):
    if not ok:
        raise ValueError(label)


def mul(a,b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def main():
    check(__debug__, 'No optimized Python')
    path = Path(__file__).resolve().parents[1]/'notes/WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE_CERTIFICATE.json'
    cert = json.loads(path.read_text())
    data = cert['budget']
    q = [F(-19101,185500),F(961,3710),F(31,50),F(-371,500)]
    c = mul(q,q)
    check(c == list(map(F,data['square_coefficients'])), 'independent square')
    check(c[4] == 0, 'no fourth debt')
    A,B = -c[5],c[6]
    base = c[0]+c[2]/3
    # Independent scalar band payment reconstruction from curvature and pi.
    band = 3*F(137721,5000)*F(106,333)**2/F(6000)
    var = -2*c[2]*F(106,333)**2/F(6000)
    target = base-A/36+B*F(157,630)
    robust = base-A/36+B*F(34,135)
    margin = F(21,200)-robust-band-var
    joint = F(21,200)-base-band-var
    check(margin == F(data['joint_margin']), 'joint margin')
    check(joint == F(data['single_signed_cap_strict']), 'one inequality')
    check(target == F(data['E_target_sharp_model']), 'target square')
    check(robust == F(data['E_relaxed_target']), 'relaxed square')
    check(band == F(data['band_payment']) and var == F(data['variance_payment']), 'payments')
    pair = 5*F(3,70)+6*F(1,90)+3*F(1,180)+F(1,70)
    check(pair == F(131,420), 'pair class assembly')
    gaussian = base+B*pair
    gains = [A/36,B*F(23,420),B/126]
    check(gaussian-target == sum(gains), 'exact order decomposition')
    check(gaussian == F(data['E_gaussian_sharp_pair_reference']), 'sharp reference only')
    check(gaussian+band+var-F(21,200) == F(data['required_robust_gain_strict']), 'required gain')
    check(F(109,1000)-F(21,200) == F(data['required_old_Gaussian_gain_before_payments_strict']), 'old before')
    check(F(109,1000)+F(53503,66000000)-F(21,200)
          == F(data['required_old_Gaussian_gain_after_initial_strict']), 'old after')
    expected = [1-36*margin/A,1-36*(margin+B/378)/A,F(2,3)-126*margin/B]
    keys = ['fifth_fraction_if_sixth_at_relaxed_ceiling_strict',
            'fifth_fraction_if_sixth_at_model_strict',
            'sixth_connected_fraction_if_full_fifth_strict']
    for v,key in zip(expected,keys):
        check(v == F(data[key]), 'fraction '+key)
    check(F(0)<expected[1]<expected[0]<1 and F(0)<expected[2]<F(2,3), 'strict tradeoff')
    # Independently verify the polynomial square-completion coefficients.
    center = F(310,371)
    check(B*(-2*center) == -A and B*center**2 == F(961,2500), 'joint square completion')
    # Polynomial hybrid diagnostics must include all higher-order terms.
    for row in cert['hybrid_noncommutative_replay']:
        diff = F(row['empirical_trace'])-F(row['Gaussian_trace'])
        higher = sum(map(F,row['A3_to_A6']))
        check(diff == F(row['A1'])+F(row['A2'])+higher, 'complete hybrid telescope')
        check(higher != 0, 'reject first-two-only claim')
    for row in cert['resolved_Parseval_replay']:
        check(F(row['lock_variance']) == F(row['spectral_value']), 'resolved replay output')
    check(cert['decision']=='B' and not cert['strict_gt79']
          and not cert['arithmetic_theorem_proved'], 'evidence boundary')
    check(not data['finite_R_Gaussian_value_numeric_certified'], 'no sharp-to-filtered substitution')
    print('PASS: independent Fraction convolution, payments, signed gate, moment-order gains and thresholds.')
    print('OPEN: actual signed resolved-prime theorem (12); strict >79 is not certified.')


if __name__ == '__main__':
    main()
