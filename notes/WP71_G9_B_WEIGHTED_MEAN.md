# WP71 G9-B — uniform mean of the twin-product main

Date: 2026-10-04  
Status: **ARITHMETIC MEAN / TRIANGULAR CALIBRATION CLOSED; moving-geometry Abel step remains**

This note continues the exact local identity in
`WP71_G9_B_LOCAL_FACTOR.md`.

Let

[
g=(b_1,b_2),qquad r=b_1/g,qquad q=b_2/g,
qquad (r,q)=1,
]

and define

[
F_{r,q}(k):=mathfrak S(rk)mathfrak S(qk).
]

The local-factor result already proved

[
mathbb E F_{r,q}
=
rac{E_2(b_1,b_2)}{g}.
]

Here we make that mean effective enough for the welding main.

## 1. Exact odd-prime divisor expansion

For an odd prime (p), the ordinary twin local factors are

[
	au_0(p)=1-rac1{(p-1)^2}
=rac{p(p-2)}{(p-1)^2},
]

when (p
mid h), and

[
	au_1(p)=1+rac1{p-1}
=rac p{p-1},
]

when (pmid h).

Because ((r,q)=1), at most one of (r,q) is divisible by (p).

If (p
mid rq), the normalized jump when (pmid k) is

[
R_p^{m gen}
=
left(rac{	au_1}{	au_0}ight)^2
=
left(rac{p-1}{p-2}ight)^2,
]

so

[
a_p^{m gen}:=R_p^{m gen}-1
=
rac{2p-3}{(p-2)^2}.
]

If (pmid rq), one of the two singular-series factors already sees (p)
before (k) is divisible by (p).  The jump is only

[
R_p^{m sp}
=
rac{	au_1}{	au_0}
=
rac{p-1}{p-2},
]

hence

[
a_p^{m sp}
=
rac1{p-2}.
]

Therefore

[
0le a_p^{m sp}le a_p^{m gen}=O(1/p).
]

After extracting the fixed baseline (C_{r,q}), the (k)-dependence is

[
prod_{substack{pmid k\\p>2}}(1+a_p)
=
sum_{substack{dmid k\\d {m odd, squarefree}}}a_d,
qquad
a_d=prod_{pmid d}a_p.
]

## 2. The prime 2 is exact and harmless

Since ((r,q)=1), at least one of (r,q) is odd.  Consequently

[
F_{r,q}(k)=0qquad(k {m odd})
]

at the (p=2) local factor, while for even (k) the (p=2) product factor
is exactly (4).

Thus parity is an exact factor, not an error term.

## 3. Uniform ordinary mean

For the divisor coefficients above,

[
sum_d rac{|a_d|}{d^{1/2}}
=
prod_{p>2}left(1+rac{a_p}{p^{1/2}}ight)
]

converges, because (a_p=O(1/p)).  Since the special jump is no larger than
the generic jump, the convergence bound is uniform in the coprime pair
((r,q)).

Using

[
sum_{nle K}sum_{dmid n}a_d
=
sum_d a_dleftlfloorrac Kdightfloor
]

and splitting at (d=K), Rankin with exponent (1/2) gives

[
oxed{
sum_{kle K}F_{r,q}(k)
=
rac{E_2(b_1,b_2)}{g},K
+
O!left(C_{r,q}K^{1/2}ight).
}
]

The fixed baseline (C_{r,q}) differs from the generic baseline only at
primes dividing (rq).  For (rqle(log X)^B),

[
C_{r,q}ll_B(log X)^{O(1)}.
]

Hence the error is uniform enough for Stage A.

## 4. Triangular welding weight

Let the outer (m)-block contain (M) consecutive integers.  For fixed
(k), the exact number of ordered pairs

[
(m,m-rk)
]

remaining in the block is

[
(M-r|k|)_+.
]

Abel summation with the ordinary mean above gives

[
sum_{k
e0}
(M-r|k|)_+F_{r,q}(k)
=
rac{E_2(b_1,b_2)}{g}
rac{M^2}{r}
+
o!left(rac{M^2}{r}ight),
]

uniformly when (r,q) are polylogarithmic and (M) is on the Stage-A prime
scale.

Because

[
gr=b_1,
]

the gcd factor cancels:

[
oxed{
sum_{k
e0}
(M-r|k|)_+
mathfrak S(rk)mathfrak S(qk)
=
E_2(b_1,b_2)rac{M^2}{b_1}
+
o(M^2/b_1).
}
]

## 5. Calibration against the (MT^2) main

The inner (j)-strip contributes leading width

[
rac{2J}{b_1}.
]

With

[
M=rac{mathrm{len}}{b_2},
]

the welded prime-pair main therefore becomes

[
rac{2J}{b_1}
E_2(b_1,b_2)rac{M^2}{b_1}
=
oxed{
2J,E_2(b_1,b_2)
left(rac{mathrm{len}}{b_1b_2}ight)^2
},
]

which is exactly the leading (MT^2) constant stated in the public dispersion
swap lemma.

This identifies the origin of the cancellation: the local (g) from
(E_2=g,mathbb E[mathfrak S(rk)mathfrak S(qk)]) cancels the density of
the structured (k)-lattice through (r=b_1/g).

## 6. Remaining part of G9-B

The rectangular leading main is now calibrated.  What remains is the actual
Stage-A geometry:

- (I(n)) moves with (n);
- the overlap/kernel weight is not constant;
- endpoint collars must be charged;
- the signed main must be Abel-summed against that slow geometry in the exact
  (R)-normalization.

That is a deterministic weighted-Abel problem, not a new prime-correlation
constant.

Companion exact algebra checker:
`src/wp71_g9_b_twin_product_mean.py`.
