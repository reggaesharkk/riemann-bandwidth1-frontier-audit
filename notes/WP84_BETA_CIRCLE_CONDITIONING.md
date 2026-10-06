# WP84 — fixed-pole conditioning audit: b3 is the current theorem target, not b10

Date: 2026-10-05

Status: **IMPORTANT CORRECTION — BOUNDED b10 IS MODEL-STRONG BUT CAUCHY-CONDITIONED POORLY; b3 IS CURRENTLY THE EASIEST >79 FIXED-POLE CONSUMER**

The bounded beta family from `WP84_BOUNDED_BETA_MINORANT.md` solved the rank-robustness problem, but a second issue must be separated from rank robustness:

> how accurately must the fixed-circle Stieltjes transform be known in order to certify the beta statistic?

For high pole order this conditioning is nontrivial.

## 1. Laurent representation

For fixed m write

[
b_m(x)=sum_{k=1}^{2m+1}rac{a_{m,k}}{(x-i)^k}
      +sum_{k=1}^{2m+1}rac{overline{a_{m,k}}}{(x+i)^k}.
]

For a probability measure (
u) with Stieltjes transform

[
s_
u(z)=int rac{d
u(x)}{x-z},
]

we have

[
int (x-i)^{-k},d
u(x)
=
rac{s_
u^{(k-1)}(i)}{(k-1)!}.
]

If two Stieltjes transforms satisfy

[
sup_{|z-i|=ho}|s_
u(z)-s_{
u_*}(z)|learepsilon
]

and the conjugate bound around (-i), then Cauchy's estimate gives

[
oxed{
left|int b_m,d(
u-
u_*)ight|
le
mathcal C_m(ho),arepsilon,
}
]

with

[
oxed{
mathcal C_m(ho)
=
2sum_{k=1}^{2m+1}|a_{m,k}|ho^{-(k-1)}.
}
]

This is a rigorous worst-case conditioning constant for the fixed-circle interface.

## 2. Model margin versus Cauchy conditioning

The >79 simple-zero threshold is

[
q=int b_m,d
u > 0.895.
]

Using the exact current four-node model, the relevant margins and conditioning constants at (ho=0.9) are approximately:

| m | pole order | model q | q-0.895 | C_m(0.9) | sufficient circle error |
|---:|---:|---:|---:|---:|---:|
| 3 | 7 | 0.8964412949 | 1.4413e-3 | 4.0142e1 | **3.59e-5** |
| 4 | 9 | 0.8976115690 | 2.6116e-3 | 1.0796e2 | 2.42e-5 |
| 5 | 11 | 0.8979688714 | 2.9689e-3 | 2.9851e2 | 9.95e-6 |
| 6 | 13 | 0.8980813061 | 3.0813e-3 | 8.4354e2 | 3.65e-6 |
| 7 | 15 | 0.8981175304 | 3.1175e-3 | 2.4225e3 | 1.29e-6 |
| 8 | 17 | 0.8981294353 | 3.1294e-3 | 7.0408e3 | 4.44e-7 |
| 9 | 19 | 0.8981334160 | 3.1334e-3 | 2.0648e4 | 1.52e-7 |
| 10 | 21 | 0.8981347675 | 3.1348e-3 | 6.0978e4 | **5.14e-8** |

Thus the statement

> "a fixed-circle resolvent error below roughly 0.003 is enough for b10"

is false by four to five orders of magnitude under the raw Cauchy-transfer argument.

## 3. Correct strategic choice

The extra model gain from m=3 to m=10 is small compared with the analytic conditioning cost.

At (ho=0.9):

- b3 already clears 79%;
- b3 needs a worst-case circle accuracy of only about (3.6	imes10^{-5});
- b10 needs about (5.1	imes10^{-8}).

So, absent a much better transfer theorem that exploits Stieltjes positivity/structure rather than arbitrary analytic error,

[
oxed{	ext{b3 is the preferred theorem consumer.}}
]

b10 remains valuable as model reconnaissance and as an eventual high-precision target.

## 4. Contour tradeoff

Taking (ho	o1^-) improves Cauchy conditioning but sends the minimum imaginary part

[
eta_0=1-ho
]

to zero, worsening every resolvent bound.  For example b3 has:

- (ho=0.75): required error about (2.14	imes10^{-5}), (eta_0=0.25);
- (ho=0.90): required error about (3.59	imes10^{-5}), (eta_0=0.10).

The best theorem contour must therefore optimize both the analytic resolvent constants and (mathcal C_m(ho)); simply pushing (ho) to one is not free.

## 5. New fail-closed rule

Every future fixed-circle resolvent claim must report **both**:

1. its uniform circle error (arepsilon(ho));
2. the consumer transfer cost (mathcal C_m(ho)arepsilon(ho)).

A >79 claim is permitted only when

[
mathcal C_m(ho)arepsilon(ho)
<
q_m-0.895
]

after every other rank/taper/background error is included.

Companion exact/symbolic checker:

`src/wp84_beta_circle_conditioning.py`.
