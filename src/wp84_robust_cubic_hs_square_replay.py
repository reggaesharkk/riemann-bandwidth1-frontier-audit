"""Independent Fraction-only scalar ledger and finite Walsh HS replay."""
from fractions import Fraction as F
from pathlib import Path
import json


def check(ok,label):
    if not ok: raise ValueError(label)


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def main():
    cert=json.loads((Path(__file__).resolve().parents[1]/'notes/WP84_ROBUST_CUBIC_HS_SQUARE_CERTIFICATE.json').read_text())
    a=[F(-19101,185500),F(961,3710),F(31,50),F(-371,500)]
    c=[F(0)]*7
    for r in range(4):
        for s in range(4): c[r+s]+=a[r]*a[s]
    check(list(map(str,c))==cert['square_coefficients'] and c[4]==0,'square convolution')
    band=3*F(137721,5000)*F(106,333)**2/6000
    var=-2*c[2]*F(106,333)**2/6000
    target=F(21,200)-band
    base=c[0]+c[2]/3
    ideal=base+c[5]/36+c[6]*F(157,630)
    relaxed=base+c[5]/36+c[6]*F(34,135)
    values={'square_threshold_strict':target,'band':band,'variance_envelope':var,
            'ideal_square_reference':ideal,'relaxed_square_reference':relaxed,
            'ideal_paid_slack':target-ideal-var,'relaxed_paid_slack':target-relaxed-var,
            'ideal_direct_slack_before_variance':target-ideal,
            'relaxed_direct_slack_before_variance':target-relaxed,
            'ideal_relative_paid_precision':(target-ideal-var)/ideal,
            'relaxed_relative_paid_precision':(target-relaxed-var)/relaxed,
            'signed_cap':target-base-var}
    for key,value in values.items(): check(F(cert[key])==value,key)
    X=[[F(1,3),F(2,5)],[F(2,5),F(-1,7)]]
    powers=[[[F(1),F(0)],[F(0),F(1)]]]
    for r in range(3): powers.append(mul(powers[-1],X))
    Q=[[sum(a[r]*powers[r][i][j] for r in range(4)) for j in range(2)] for i in range(2)]
    energy=sum(Q[i][j]**2 for i in range(2) for j in range(2))/2
    square=mul(Q,Q)
    check(energy==(square[0][0]+square[1][1])/2,'HS trace')
    spectral=F(0)
    for u in range(2):
        for v in range(2):
            amplitudes=[sum(powers[r][i][j]*(-1)**(u*i+v*j) for i in range(2) for j in range(2)) for r in range(4)]
            spectral+=sum(a[r]*amplitudes[r] for r in range(4))**2
    check(spectral/8==energy,'complete weighted Walsh square')
    check(cert['decision']=='D' and not cert['strict_gt79'] and not cert['prime_arithmetic_proved'],'evidence boundary')
    print('PASS: independent Fraction ledger, full weighted Walsh HS square, and evidence boundary.')


if __name__=='__main__': main()
