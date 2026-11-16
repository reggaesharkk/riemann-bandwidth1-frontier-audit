# WP84 — permutation-Lindeberg resolvent reduction

Date: 2026-10-04

Status: **CUBIC-AND-HIGHER RESOLVENT DEBT REMOVED UNIFORMLY OFF THE REAL AXIS; THEOREM REDUCED TO TWO CONDITIONAL ARITHMETIC OPERATORS**

The fixed-pole hierarchy only needs a resolvent law on one fixed circle around `i`. The infinitesimal prime-block estimate now allows a deterministic Lindeberg reduction that is independent of any arbitrary ordering of the prime powers.

## 1. Setup

Write the normalized prime-side matrix as

[
H=S+sum_{j=1}^M B_j,
]

where `S` contains the smooth/background terms and the `B_j` are the prime-power blocks from `WP84_INFINITESIMAL_PRIME_BLOCKS.md`.

For `zinmathbb C_+` write

[
R_A(z)=(A-zI)^{-1},
qquad
	au_d(A)=d^{-1}operatorname{tr}A.
]

For Hermitian `A`,

[
|R_A(z)|_{m op}le(Im z)^{-1}.
]

## 2. Exact one-block expansion

For Hermitian `A,B`,

[
R_{A+B}
=
R_A-R_ABR_A+R_ABR_ABR_A
-R_ABR_ABR_ABR_{A+B}.
]

Therefore

[
egin{aligned}
	au_d(R_{A+B}-R_A)
={}&-	au_d(R_ABR_A)\
&+	au_d(R_ABR_ABR_A)
+mathcal E_3,
end{aligned}
]

with the explicit bound

[
oxed{
|mathcal E_3|
le
rac{|B|_{m op}^3}{(Im z)^4}.
}
]

No dimension factor appears because `|	au_d(M)|le|M|_{m op}`.

## 3. Random permutation as a proof device

Let `pi` be a permutation of the `M` prime-power blocks and define

[
H_k^pi=S+sum_{a=1}^k B_{pi(a)},
qquad
R_k^pi=(H_k^pi-zI)^{-1}.
]

For **every** permutation,

[
	au_d(R_H)-	au_d(R_S)
=
sum_{k=1}^M
	au_d(R_k^pi-R_{k-1}^pi).
]

Average this exact identity over the finite set of all permutations. The left side is unchanged. Hence

[
oxed{
m_H(z)-m_S(z)
=
-mathcal A_1(z)+mathcal A_2(z)+mathcal E_{ge3}(z),
}
]

where

[
mathcal A_1
=
mathbb E_pi
sum_k
	au_d(R_{k-1}^pi B_{pi(k)}R_{k-1}^pi),
]

[
mathcal A_2
=
mathbb E_pi
sum_k
	au_d(
R_{k-1}^pi B_{pi(k)}
R_{k-1}^pi B_{pi(k)}
R_{k-1}^pi),
]

and

[
oxed{
|mathcal E_{ge3}(z)|
le
(Im z)^{-4}sum_j|B_j|_{m op}^3.
}
]

The permutation is not a random-matrix assumption. It is only an exact symmetrization of a deterministic telescoping identity.

## 4. Uniform closure on the fixed circle

Take the circle

[
Gamma_ho={z:|z-i|=ho},
qquad 0<ho<1.
]

Then

[
Im zge1-ho
]

throughout (Gamma_ho). Since the prime-block cube mass is

[
sum_j|B_j|_{m op}^3=O(L^{-3}),
]

we obtain the **uniform** bound

[
oxed{
sup_{zinGamma_ho}
|mathcal E_{ge3}(z)|
=
O_ho(L^{-3})
=o(1).
}
]

This is exactly the mode of convergence needed by the `r_m` Cauchy-circle interface.

## 5. Conditional-operator form

Condition on the unordered set (mathcal S) of blocks already inserted. The next block is uniform among the complement.

Define

[
R_{mathcal S}(z)
=
left(S+sum_{jinmathcal S}B_j-zIight)^{-1},
]

the remaining first-moment operator

[
mathcal M_1(mathcal S)
=
rac1{M-|mathcal S|}
sum_{j
otinmathcal S}B_j,
]

and the remaining variance map

[
mathcal V_{mathcal S}(A)
=
rac1{M-|mathcal S|}
sum_{j
otinmathcal S}B_j A B_j.
]

Then the two surviving terms are exactly averages of

[
oxed{
	au_d(R_{mathcal S}mathcal M_1(mathcal S)R_{mathcal S})
}
]

and

[
oxed{
	au_d(
R_{mathcal S}
mathcal V_{mathcal S}(R_{mathcal S})
R_{mathcal S})
}.
]

So all higher single-block Taylor terms have disappeared from the theorem frontier.

## 6. What must now be proved arithmetically

The resolvent law is reduced to two statements, uniform on (Gamma_ho):

1. **drift closure:** evaluate the permutation/subset average of the (mathcal M_1) term;
2. **variance closure:** evaluate the corresponding (mathcal V) term.

The modulated-Toeplitz structure gives

[
B_n
=
-rac{Lambda(n)}{pisqrt n,aL}
,C(log n),
]

so (mathcal M_1) is a weighted first prime-frequency average and (mathcal V) is a weighted double modulation/conjugation operator.

This is the exact place where Chebyshev--Mertens, phase cancellation, and the overlap geometry must enter.

## 7. Why this is narrower than a raw moment theorem

The old fourth/eighth-moment route sums all closed words of fixed length in the (B_j), including configurations whose magnitude is dominated by rare deep zero outliers after transfer.

The present reduction keeps the resolvent bounded at every intermediate step:

[
|R_{mathcal S}(z)|le(1-ho)^{-1}.
]

Only the first two infinitesimal block operators are exposed, and the entire cubic block mass is already (o(1)).

Thus this reduction remains Proposition-R safe.

## 8. New kill gate

For a >79% theorem via `r10`, it is enough to prove a deterministic limit/inequality for the two symmetrized operators above on one fixed circle (Gamma_ho), with total error small compared with the `r10` model margin

[
q_{10}-0.895approx3.135	imes10^{-3}.
]

No raw fourth or higher even trace moment is part of this interface.
