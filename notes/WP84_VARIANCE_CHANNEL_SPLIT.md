# WP84 — exact modulated-Toeplitz multiplication rule for the variance map

Date: 2026-10-05

Status: EXACT FOUR-CHANNEL ALGEBRA CLOSED; RESONANT/FAST ARITHMETIC ESTIMATES OPEN

Write the normalized prime block as

    B_n = - Lambda(n)/(pi*sqrt(n)*a*L) * C(log n).

For y=log n, the complexified overlap block is

    Cplus(y) = (2*pi/L) D_y T_y D_y,

with (D_y)_{kk}=exp(i alpha_k y/2), alpha_k=T+k*(2*pi/L), and T_y Toeplitz from the overlap kernel.

The real block is

    C(y)=1/2*(Cplus(y)+Cplus(-y)).

For any matrix A this gives the exact identity

    B_n A B_n
      = Lambda(n)^2/(n*a^2*L^4)
        * sum_{sigma,tau in {+1,-1}}
          D_y^sigma T_y D_y^sigma
          A
          D_y^tau T_y D_y^tau.

All pi-constants cancel exactly.

Now write alpha_k=T+k h, h=2*pi/L.  In the (sigma,tau) channel the common carrier is

    exp(i*T*y*(sigma+tau)).

Hence the four channels split exactly into:

- resonant (+,-) and (-,+): carrier cancels;
- fast (+,+) and (-,-): carrier is exp(+/-2 i T y)=n^(+/-2 i T).

Therefore

    V(A)=sum_n B_n A B_n = V_res(A)+V_fast(A)

is an exact algebraic decomposition.

Important evidence boundary:

- The resonant part is weighted by Lambda(n)^2/n and is compatible with the square-prime Mertens measure, but total mass alone does not close the operator-valued y-dependence.  A variation estimate is still required.
- The fast part contains genuinely twisted sums of Lambda(n)^2/n * n^(+/-2 i T).  No source-closed estimate strong enough for this operator sum has yet been identified, so it may not be dropped merely as 'oscillatory'.
- The first-order drift has analogous carriers exp(+/- i T y) and likewise needs a theorem-grade oscillatory prime estimate in the actual overlap kernel.

New variance frontier:

1. V-res: operator-variation/continuum closure;
2. V-fast: twisted square-prime cancellation;
3. drift: twisted Lambda/sqrt(n) cancellation in the exact block geometry.
