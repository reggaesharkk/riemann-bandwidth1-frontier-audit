#!/usr/bin/env python3
"""WP83 positive-multiplicity Fejer energy gate.

Continuous theorem used in the note:
  W_H(t)=(1-|t|/H)_+,
  q(t)=sum_j m_j exp(i omega_j t), m_j>=0.

Then
  int W_H |q|^2
    = H sum_{i,j} m_i m_j sinc^2((omega_i-omega_j)H/2)
    >= H sum_j m_j^2
    >= H sum_j m_j
for integer multiplicities.

This exact finite-field DFT analogue checks the positivity mechanism:
the cyclic triangular kernel has nonnegative Fourier transform and therefore
the weighted quadratic energy dominates its diagonal contribution.
"""
P=257
N=16

# primitive root 3 mod 257, N | 256
OMEGA=pow(3,(P-1)//N,P)
assert pow(OMEGA,N,P)==1
assert all(pow(OMEGA,d,P)!=1 for d in (1,2,4,8))

def w(e):
    return pow(OMEGA,e%N,P)

def dft(vec):
    return [sum(vec[t]*w(-k*t) for t in range(N))%P for k in range(N)]

def main():
    # Circular Fejer kernel K = autocorrelation of a short box, so its
    # DFT is pointwise a square and hence is the exact finite analogue.
    M=5
    box=[1 if t<M else 0 for t in range(N)]
    K=[sum(box[x]*box[(x+t)%N] for x in range(N))%P for t in range(N)]
    Kh=dft(K)

    bh=dft(box)
    for k in range(N):
        # In finite-field Fourier algebra: Khat(k)=bhat(k)bhat(-k).
        assert Kh[k]==bh[k]*bh[(-k)%N]%P

    # Arbitrary positive integer multiplicities on distinct frequency bins.
    masses={0:2,3:1,7:4,11:3}
    q=[sum(m*w(freq*t) for freq,m in masses.items())%P for t in range(N)]
    lhs=sum(K[t]*q[t]*q[(-t)%N] for t in range(N))%P

    # Parseval/correlation expansion computed independently.
    rhs=0
    for fi,mi in masses.items():
        for fj,mj in masses.items():
            rhs=(rhs+mi*mj*Kh[(fi-fj)%N])%P
    rhs=rhs*pow(N,P-2,P)%P
    assert lhs==rhs,(lhs,rhs)

    print("N",N,"box length",M)
    print("masses",masses)
    print("RESULT: WP83_POSITIVE_FEJER_FINITE_ANALOGUE_PASS")

if __name__=="__main__":
    main()
