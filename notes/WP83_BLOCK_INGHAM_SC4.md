# WP83 — block-Ingham theorem for confluent clusters of size <=4

Date: 2026-10-04
Status: **SEPARATED SMALL-CLUSTER LOWER FRAME CLOSED WITH A CRUDE EXPLICIT CONSTANT; ONE-COMPONENT SIGNED FLOOR STILL OPEN**

After translating and rescaling an observation interval of length H to x in [0,1], write a confluent cluster of at most four pairs as

    exp(i mu_C x) P_C(x),

where deg(P_C)<=3.

Let E_C=int_0^1 |P_C|^2. The exact 4x4 Hilbert certificate gives

    E_C >= c4 ||a_C||_2^2,

    c4=49/1395654656,

for the monomial coefficient vector a_C.

Therefore

    |P_C(0)|^2 <= E_C/c4,
    |P_C(1)|^2 <= 4 E_C/c4,
    ||P_C'||_2^2 <= 14 E_C/c4.

For two different block centers, one integration by parts turns

    int_0^1 P_C(x) conj(P_D(x)) exp(i(mu_C-mu_D)x) dx

into two endpoint Hilbert forms plus two derivative Hilbert forms. Summing over C!=D and using the source-closed Montgomery--Vaughan bilinear constant C_MV=26 gives

    |Off|
      <= (26/Delta) [5/c4 + 2 sqrt(14/c4)] E,

where

    E=sum_C E_C

and every pair of block centers is separated by at least Delta.

Using 2 sqrt(x)<=x+1 gives the rational sufficient threshold

    Delta >= K4

with

    K4=2*26*(19/c4+1)
      =1378906802676/49
      =2.814095515665306e10...

under which |Off|<=E/2. Hence

    boxed:
    int_0^1 |sum_C exp(i mu_C x)P_C(x)|^2 dx
      >= (1/2) sum_C int_0^1 |P_C(x)|^2 dx.

The constant is intentionally terrible: the monomial basis and rational square-root majorant were chosen for auditability, not optimization. Any finite constant suffices for the asymptotic exponent.

On a physical interval of length H, mu_C=H gamma_C, so the sufficient ordinate separation is

    |gamma_C-gamma_D| >= K4/H.

For H=theta L with fixed theta>0 this is still a constant multiple of the natural 1/L microscopic scale.

## Consequence for SC4

Interactions between **different separated components of size <=4** are no longer an open issue. The remaining small-component tasks are:

1. a uniform signed-energy floor for one reflection-paired component of size <=4, including the separated-to-confluent transition;
2. suppression of the shallower depth background by the D log L/L band;
3. transfer through the finite two-window sections.

Far comparable-depth components can be handled by this block lower-frame theorem instead of an absolute-value shell sum.

Companion exact constant checker: `src/wp83_block_ingham_constant.py`.
