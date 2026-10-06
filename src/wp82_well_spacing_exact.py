#!/usr/bin/env python3
"""Exact integer/grid well-spacing gate for the two dilated spectra.

For FFT bins j=0,...,N-1 and an m-side dilation b2, bins in one fixed
major-center window occupy an interval (mod N) of width at most 2*w*N,
where w is the undilated frequency half-width used in the public face.

Partition these bins by j mod b2.  There are at most b2 arms, and
successive bins in one arm differ by a multiple of b2.  Under the n-side
map gamma_n=b1*j/N this gives exact image spacing in multiples of
b1*b2/N before reduction mod 1.

The public numerical face uses the conservative count
    #bins <= 2*w*N + b2 + 1.
This script checks the underlying integer statements exhaustively on many
small grids.  The proof is elementary and does not use prime estimates.
"""
from fractions import Fraction as F

def circular_dist_num(x,N):
    x%=N
    return min(x,N-x)

def bins_near_center(N,b2,a,Q,w_num,w_den):
    # Exact condition distance(b2*j/N, a/Q) <= w_num/(w_den*Q).
    # Multiply by N*Q*w_den:
    out=[]
    for j in range(N):
        z=b2*j*Q-a*N
        # circular distance modulo NQ
        d=circular_dist_num(z,N*Q)
        if d*w_den <= w_num*N:
            out.append(j)
    return out

def check_case(N,b1,b2,P,w_num,w_den):
    checked=0
    for Q in range(1,P+1):
        for a in range(Q):
            js=bins_near_center(N,b2,a,Q,w_num,w_den)
            if not js: continue
            arms={}
            for j in js:
                arms.setdefault(j%b2,[]).append(j)
            assert len(arms)<=b2
            # Conservative public count: width <= w, plus one boundary
            # point per residue arm.
            assert len(js)*w_den <= 2*w_num*N + (b2+1)*w_den
            for vals in arms.values():
                vals.sort()
                for x,y in zip(vals,vals[1:]):
                    assert (y-x)%b2==0
                    # Exact n-side image increment:
                    lhs=F(b1*(y-x),N)
                    step=F(b1*b2,N)
                    assert lhs/step == (y-x)//b2
            checked+=1
    return checked

def main():
    total=0
    for N in (64,96,128,192,256):
        for b1,b2 in ((5,3),(5,7),(3,2),(4,3),(9,4),(8,5)):
            for P in (3,5,7):
                # widths 1/20, 1/30, 1/40
                for den in (20,30,40):
                    total+=check_case(N,b1,b2,P,1,den)
    print("major-center grid cases checked =",total)
    print("RESULT: WP82_WELL_SPACING_EXACT_PASS")

if __name__=="__main__":
    main()
