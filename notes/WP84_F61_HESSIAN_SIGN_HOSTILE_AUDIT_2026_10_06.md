# WP84 F61 Hessian sign hostile audit — 2026-10-06

Status: **GLOBAL HESSIAN-KERNEL POSITIVITY FALSIFIED EXACTLY**

This is a sign audit of the active bounded consumer
\[
 f(x)=F_{61}(x)=\frac{62P(x)^2}{P(x)^2+61},\qquad
 P(x)=1-\frac{43428}{13891}x+\frac{37704}{13891}x^2-\frac{9660}{13891}x^3.
\]

It does not affect the consumer certificate or the fixed-pole representation. It rules out one proposed shortcut for the active Lindeberg Hessian.

## Exact calculation

Set \(g=P^2\). Direct differentiation gives
\[
 f''(x)=62\cdot61\,
 \frac{g''(x)(g(x)+61)-2g'(x)^2}{(g(x)+61)^3}.
\]
The divided-difference kernel in the functional Lindeberg formula has diagonal
\[
 K_f(x,x)=\frac12 f''(x).
\]

Exact rational substitution yields
\[
 f''(0)=\frac{183349199136}{6394291229}>0,
\]
whereas
\[
 f''(1)=-
 \frac{7327100576350070179618547976}
 {40792215364263396525173233475}<0.
\]
The executable regression gate `src/wp84_f61_hessian_sign_gate.py` reproduces both fractions using only Python's standard-library `Fraction`.

Therefore \(K_f\) is not a positive semidefinite kernel: its one-point diagonal already takes both signs. Since the spectral transition measure \(\Gamma_A\) is positive, its positivity alone does not imply a sign for
\[
 D_2(A;B)=\int K_f(x,y)\,d\Gamma_A(x,y).
\]

## Consequence for the proof route

A closure that replaces \(\Gamma_A\) by its total mass, or invokes Gram positivity without controlling where its mass lies, cannot establish the required one-sided six-pole inequality. A valid closure must retain enough spectral-location information to bound the positive and negative parts of \(K_f\), or prove a specific cancellation using the actual permutation state.

This is a hostile-audit result about a proposed method. It neither disproves the six-pole theorem target nor establishes an arithmetic limit. The large-\(T\) permutation-averaged drift/Hessian transport remains open.
