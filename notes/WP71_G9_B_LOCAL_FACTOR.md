# WP71 G9-B — exact local factorization of the welding main term

Date: 2026-10-04  
Status: **LOCAL EULER-FACTOR IDENTITY CLOSED; global Abel/glue transport remains open**

Let

[
g=(b_1,b_2),qquad r=b_1/g,qquad q=b_2/g.
]

For a prime (p), write

[
e_1=v_p(b_1),qquad e_2=v_p(b_2),qquad
e=min(e_1,e_2),
]

so

[
v_p(r)=e_1-e,qquad v_p(q)=e_2-e,
]

and at most one of those last two exponents is positive.

Let (kappa_p(e_1,e_2;v)) be the exact public local factor for the linear
form (b_1m_1-b_2m_2=j), and put

[
	au_p(v):=kappa_p(0,0;v)
]

for the ordinary prime-pair local factor.

If (V=v_p(k)) for a uniformly distributed integer (k), then

[
Pr(V=v)=(1-1/p)p^{-v}.
]

The exact identity is

[
oxed{
mathbb E_Vigl[kappa_p(e_1,e_2;V)^2igr]
=
p^e,
mathbb E_Vigl[
	au_p(V+v_p(r)),
	au_p(V+v_p(q))
igr].
}
]

## Proof by local cases

### Case 1: (e_1=e_2=0)

Then (e=0), (r,q) are both (p)-units and the identity is tautological.

### Case 2: (e=0), exactly one of (e_1,e_2) is positive

Assume (v_p(r)>0), (v_p(q)=0).  The general linear-form local density is

[
kappa_p(e_1,0;V)=
egin{cases}
p/(p-1),&V=0,\\
0,&V>0.
end{cases}
]

Hence

[
mathbb E,kappa_p^2=rac{p}{p-1}.
]

Directly averaging
(	au_p(V+v_p(r))	au_p(V)) gives the same fraction.

### Case 3: (e_1=e_2=ege1)

The nonzero range starts at (V=e), and after shifting (V=e+u) the local
values are exactly (p^e	au_p(u)).  The valuation probabilities contribute
a factor (p^{-e}), hence

[
mathbb E,kappa_p^2
=
p^e,mathbb E,	au_p(V)^2.
]

### Case 4: (e_1
e e_2) and (ege1)

The general local factor is nonzero only at (V=e), where it equals

[
p^erac{p}{p-1}.
]

The same calculation reduces to Case 2 after stripping the common (p^e).

Thus the identity holds for every prime and every pair of local exponents.

## Global consequence

Multiplying the local identities over primes gives the main-term Euler-product
relation

[
oxed{
E_2(b_1,b_2)
=
g,
mathbb E_kigl[
mathfrak S(rk)mathfrak S(qk)
igr],
}
]

where

[
E_2(b_1,b_2)
=
prod_p mathbb E_v[kappa_p(v)^2].
]

Equivalently,

[
mathbb E_k[
mathfrak S(rk)mathfrak S(qk)]
=
rac{E_2(b_1,b_2)}{(b_1,b_2)}.
]

This is precisely the local factorization expected when the two prime-pair
mains produced by the welding reindexing are multiplied.

The companion exact checker is

`src/wp71_g9_b_local_factor.py`.

It exhaustively checks a grid of prime/exponent cases with
`fractions.Fraction`; the written case proof is the mathematical argument.

## What remains in G9-B

This closes only the **Euler-factor identity**.  To close the signed main door
we must still:

1. define (M_k(n)) with the exact moving interval (I(n));
2. perform Abel/partial summation against the slow geometric weight;
3. track the gcd/Jacobian factor so the (g) above cancels in the exact
   public normalization;
4. show the resulting signed main is exactly the same singular-series /
   continuum object already feeding (C_{m core}=-1/48).

No absolute value is permitted on this main term.
