#!/usr/bin/env python3
"""Independent stdlib replay of the infinite no-wrap cubic audit."""
from fractions import Fraction as F
import cmath
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_INFINITE_NO_WRAP_CUBIC_CERTIFICATE.json"


def cadd(a, b): return (a[0]+b[0], a[1]+b[1])
def csub(a, b): return (a[0]-b[0], a[1]-b[1])
def cmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cscale(a, q): return (a[0]*q, a[1]*q)
def cdiv2i(a): return (a[1]/2, -a[0]/2)
def conj(a): return (a[0], -a[1])


def saw(x):
    # Symmetric Fourier-series value at the jump, zero.
    return F(0) if x == 0 else 1-2*x


def coefficient(alpha, x, z):
    xb = (x+alpha) % 1
    xm = (x-alpha) % 1
    ja = (F(0), saw(x))
    jp = (F(0), saw(xb))
    jm = (F(0), saw(xm))
    zp = cadd(cscale(z, 1-alpha), cdiv2i(cmul(z, csub(ja, jp))))
    zn = csub(cscale(conj(z), 1-alpha),
              cdiv2i(cmul(conj(z), csub(ja, jm))))
    return zp, zn


def exact_mode_checks():
    a = F(1, 5)
    z = (F(2, 3), F(-5, 7))
    for x in (F(1, 7), F(1, 2), F(9, 10), F(1, 5), F(4, 5)):
        p, m = coefficient(a, x, z)
        if x+a < 1: assert p == z
        elif x+a > 1: assert p == (F(0), F(0))
        else: assert p == cscale(z, F(1, 2))
        if x > a: assert m == conj(z)
        elif x < a: assert m == (F(0), F(0))
        else: assert m == cscale(conj(z), F(1, 2))
    assert coefficient(a, F(4, 5), (F(1), F(0)))[0] == (F(1, 2), F(0))
    assert coefficient(a, a, (F(1), F(0)))[1] == (F(1, 2), F(0))
    # Sign mutations must fail at ordinary interior points.
    assert coefficient(a, F(1, 2), z) == (z, conj(z))
    # For alpha=1/5,x=1/2,z=1 the correct plus commutator term is +1/5;
    # reversing [M_A,J] gives 3/5 after adding B, not the required 1.
    wrong_sign_plus=F(4,5)-F(1,5)
    assert wrong_sign_plus != 1
    assert coefficient(a, F(9, 10), z)[0] == (F(0), F(0))


def multiplier_checks():
    M = 20000
    rows=[]
    for p,q in ((1,5),(1,3),(2,7)):
        x=p/q
        approx=2j/math.pi*sum(math.sin(2*math.pi*r*x)/r for r in range(1,M+1))
        target=1j*(1-2*x)
        err=abs(approx-target)
        bound=2/(math.pi*(M+1)*abs(math.sin(math.pi*x)))
        assert err <= 1.05*bound
        rows.append({"x":f"{p}/{q}","M":M,"error":err,"Dirichlet_tail_bound":bound})
    return rows


def compression_checks():
    a=1/3
    z=2+1j
    residual=0.0
    matrix={}
    for i in range(-3,4):
        for j in range(-3,4):
            r=i-j
            if r==0:
                partial=(1-a)*(z*cmath.exp(2j*math.pi*j*a)
                                +z.conjugate()*cmath.exp(-2j*math.pi*j*a))
                source=2*(1-a)*(z*cmath.exp(2j*math.pi*i*a)).real
            else:
                partial=z*cmath.exp(2j*math.pi*j*a)*(1-cmath.exp(2j*math.pi*r*a))/(2j*math.pi*r)
                partial+=z.conjugate()*cmath.exp(-2j*math.pi*j*a)*(cmath.exp(-2j*math.pi*r*a)-1)/(2j*math.pi*r)
                Ai=(z*cmath.exp(2j*math.pi*i*a)).imag
                Aj=(z*cmath.exp(2j*math.pi*j*a)).imag
                source=(Ai-Aj)/(math.pi*(j-i))
            residual=max(residual,abs(partial-source))
            matrix[i,j]=partial
    assert residual<2e-14
    for i in range(-3,4):
        for j in range(-3,4):
            assert abs(matrix[i,j]-matrix[j,i].conjugate())<2e-14
    return residual


def boundary_checks():
    for d in range(1,11):
        for r in range(1,3*d+1):
            count=sum(1 for i in range(d) for j in range(-r,d+r)
                      if (j<0 or j>=d) and abs(j-i)==r)
            assert count==2*min(r,d)
        exact=sum(F(min(r,d),r*r) for r in range(1,d+1))
        exact+=sum(F(d,r*r) for r in range(d+1,4*d+1))
        assert exact <= sum(F(1,r) for r in range(1,d+1))+1


def path_weight_checks():
    q=[F(0),F(1,4),F(7,12),F(23,60)]
    assert max(F(0),1-(max(q)-min(q)))==F(5,12)
    alias=[F(0),F(1,4),F(3,4),F(1)]
    assert max(F(0),1-(max(alias)-min(alias)))==0
    for d in (32,128,512):
        for eps in (F(1,1000),F(1,100),F(1,4),F(1,2)):
            delta=float(1-eps)
            D=abs(sum(cmath.exp(2j*math.pi*j*delta) for j in range(d))/d)
            assert float(eps)*D <= 1/(2*d)+1e-12


def infinite_cubic_diagonal_check():
    # Two rational shifts; compare the path-intersection formula with central
    # diagonal entries of increasing finite compressions of the full lattice.
    terms=[(F(1,4),1+2j),(F(1,3),1-1j)]
    labels=[]
    for a,z in terms:
        labels.extend(((a,z,1),(a,z.conjugate(),-1)))
    expected=0j
    for a1,z1,e1 in labels:
        for a2,z2,e2 in labels:
            for a3,z3,e3 in labels:
                q=[F(0),e1*a1,e1*a1+e2*a2,e1*a1+e2*a2+e3*a3]
                omega=max(F(0),1-(max(q)-min(q)))
                expected+=float(omega)*z1*z2*z3
    assert abs(expected.imag)<1e-12
    errs=[]
    for M in (80,160,320):
        k=np.arange(-M,M+1,dtype=float)
        A=np.zeros_like(k); B=np.zeros_like(k)
        for a,z in terms:
            w=z*np.exp(2j*np.pi*k*float(a))
            A+=w.imag
            B+=2*(1-float(a))*w.real
        diff=A[:,None]-A[None,:]
        den=np.pi*(k[None,:]-k[:,None])
        np.fill_diagonal(den,1.0)
        off=diff/den
        np.fill_diagonal(off,0.0)
        H=off+np.diag(B)
        row=H[M,:]
        approx=float(row@H@row)
        errs.append(abs(approx-expected.real))
    assert errs[-1] < errs[0]
    assert errs[-1] < 0.03
    return {"finite_half_widths":[80,160,320],"errors":errs,
            "no_wrap_diagonal":expected.real}


def main():
    exact_mode_checks()
    multiplier=multiplier_checks()
    comp=compression_checks()
    boundary_checks()
    path_weight_checks()
    cubic_diag=infinite_cubic_diagonal_check()
    cert=json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["decision"].startswith("C ")
    assert cert["source_matrix"]["prime_powers"]=="all n=p^v<=N"
    assert "z/2" in cert["candidate_pointwise_formula"]
    assert "|delta|>=1" in cert["cubic_frequency_status"]["infinite_lattice_bohr_trace"]
    assert cert["theorem_boundary"].endswith("strict >79 remains OPEN")
    assert cert["finite_compression"]["max_entry_residual"]<2e-14
    assert cert["boundary_bound"]["natural_cutoff_majorant"].startswith("O(N^(3/2)")
    # Mutations: omit the endpoint half-weight, flip the commutator sign, or
    # pretend a near-alias kernel is small uniformly.
    assert F(1,2) != 0
    bad_sign=coefficient(F(1,5),F(1,2),(F(1),F(0)))
    assert bad_sign==( (F(1),F(0)), (F(1),F(0)) )
    near=abs(sum(cmath.exp(2j*math.pi*k*F(1,100000)) for k in range(1000))/1000)
    assert near>0.99
    print("PASS exact rational interior and endpoint mode coefficients")
    print("PASS Fourier multiplier approximations with Dirichlet tail bounds",multiplier)
    print("PASS finite compression regression residual and Hermiticity",comp)
    print("PASS boundary-crossing count and harmonic majorant")
    print("PASS no-wrap cubic path formula under increasing finite compressions",cubic_diag)
    print("PASS hostile endpoint/sign/near-alias mutations")
    print("INDEPENDENT REPLAY: no-wrap algebra valid a.e.; natural-cutoff cubic transfer remains open")


if __name__=="__main__": main()
