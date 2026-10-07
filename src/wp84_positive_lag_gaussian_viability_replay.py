"""Independent Fraction-only all-radius Gaussian viability replay.

No SymPy, mpmath, producer import, numerical integration or random samples.
"""
import json
import math
from fractions import Fraction as F
from pathlib import Path
import wp84_mehler_weak_dual_certificate as dual


def check(ok, msg):
    if not ok:
        raise ValueError(msg)


def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def add(p,q):
    out=[F(0)]*max(len(p),len(q))
    for i,v in enumerate(p):out[i]+=v
    for i,v in enumerate(q):out[i]+=v
    return trim(out)


def mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return trim(out)


def scale(p,v):return [x*v for x in p]


def remainder(p,q):
    p=p[:]
    while len(p)>=len(q) and any(p):
        k,v=len(p)-len(q),p[-1]/q[-1]
        for j,x in enumerate(q):p[j+k]-=v*x
        trim(p)
    return p


def variation(signs):
    signs=[v for v in signs if v]
    return sum(a!=b for a,b in zip(signs,signs[1:]))


def sign(x):return int(x>0)-int(x<0)


def positive_sturm(poly):
    normalize=lambda p:scale(p,1/abs(p[-1]))
    seq=[normalize(poly),normalize([j*poly[j] for j in range(1,len(poly))])]
    while len(seq[-1])>1:
        v=scale(remainder(seq[-2],seq[-1]),F(-1))
        check(any(v),'unexpected repeated root')
        seq.append(normalize(v))
    roots=variation([sign(p[0]) for p in seq])-variation([sign(p[-1]) for p in seq])
    check(poly[0]>0 and roots==0,'global positive minorant numerator')
    return roots


def consumer_minorant(coeff):
    c,a=F(3142,2415),F(131,200)
    p=[F(1),-F(43428,13891),F(37704,13891),-F(9660,13891)]
    def shifted(e):
        return [sum(p[j]*math.comb(j,k)*e**k for j in range(k,len(p)))
                for k in range(len(p))]
    pp,pm=shifted(1),shifted(-1)
    dp=[(1-c)**2+a*a,2*(1-c),F(1)]
    dm=[(1-c)**2+a*a,-2*(1-c),F(1)]
    dp,dm=mul(mul(dp,dp),dp),mul(mul(dm,dm),dm)
    num=scale(add(mul(mul(pp,pp),dm),mul(mul(pm,pm),dp)),(c*c+a*a)**3)
    den=scale(mul(dp,dm),F(2))
    even=[F(0)]*(2*len(coeff)-1)
    for j,v in enumerate(coeff):even[2*j]=v
    polynomial=add(num,scale(mul(even,den),F(-1)))
    check(all(polynomial[j]==0 for j in range(1,len(polynomial),2)),'even symmetry')
    return polynomial[::2]


def machin():
    def atan(q):
        n=60
        v=sum((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(n))
        w=v+(-1)**n*q**(2*n+1)/F(2*n+1)
        return min(v,w),max(v,w)
    a,b=atan(F(1,5)),atan(F(1,239))
    return 16*a[0]-4*b[1],16*a[1]-4*b[0]


def main():
    check(__debug__,'No -O')
    path=Path(__file__).resolve().parents[1]/'notes/WP84_POSITIVE_LAG_GAUSSIAN_VIABILITY_CERTIFICATE.json'
    data=json.loads(path.read_text())
    for key in ('quartic_minorant','sextic_minorant'):
        q=data[key]
        coeff=list(map(F,q['coefficients_in_x_squared']))
        p=consumer_minorant(coeff)
        check(p==list(map(F,q['positive_numerator_coefficients_in_x_squared'])),'reconstruct minorant')
        positive_sturm(p)
    plo,phi=machin()
    check([str(plo),str(phi)]==data['pi_Machin_bounds'],'Machin intervals')
    check(phi<F(355,113) and plo*plo>F(1000,103) and phi*phi<10,'pi rational bounds')
    t=F(100001,100000)
    # Independent polynomial operations derive the two-site Wick moments.
    v0=[t/F(12),-t/F(4)];v1=[t/F(12),t/F(4)];v2=[F(0),t/F(2)]
    er2=add(v1,v2)
    er4=add(add(scale(mul(v1,v1),F(3)),scale(mul(v1,v2),F(2))),scale(mul(v2,v2),F(3)))
    er6=add(add(scale(mul(mul(v1,v1),v1),F(15)),scale(mul(mul(v1,v1),v2),F(9))),
            add(scale(mul(v1,mul(v2,v2)),F(9)),scale(mul(mul(v2,v2),v2),F(15))))
    m2=add(v0,er2)
    m4=add(add(scale(mul(v0,v0),F(3)),scale(mul(v0,er2),F(6))),er4)
    m6=add(add(scale(mul(mul(v0,v0),v0),F(15)),scale(mul(mul(v0,v0),er2),F(45))),
           add(scale(mul(v0,er4),F(15)),er6))
    q=list(map(F,data['sextic_minorant']['coefficients_in_x_squared']))
    lower=[q[0]]
    for weight,moment in zip(q[1:],[m2,m4,m6]):lower=add(lower,scale(moment,weight))
    check(lower==list(map(F,data['two_site_lower_coefficients_in_u'])),'independent Gaussian moments')
    lb=sum(v*(F(1,10)**j if v>=0 else F(103,1000)**j) for j,v in enumerate(lower))
    check(lb==F(data['two_site_simple_rational_lower']) and lb>F(109,1000),'two-site gap')
    big=-F(3,250)+F(27,50)*t*(F(1,6)+F(3,4)*F(113,355)**2)-t*t/F(100)
    check(big==F(data['all_m_ge3_simple_rational_lower']) and big>F(109,1000),'large-block moment gap')
    check(F(2813,25750)>F(109,1000),'one-site preserved gap')
    for w in data['witnesses']:dual.verify(w)
    check(F(109,1000)+F(53503,66000000)-F(21,200)==F(data['negative_margin_at_least']),
          'negative complete ledger')
    check(data['decision']=='A' and not data['arithmetic_attack_started'],'stop gate')
    print('PASS: independent Fraction-only global Sturm, Machin, Wick, weak-dual and all-R ledger.')
    print('Complete GaussianValue_R(U) >=109/1000 for every R>=0 and every U>=delta.')


if __name__=='__main__':main()
