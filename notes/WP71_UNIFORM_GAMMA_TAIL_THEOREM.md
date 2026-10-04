# WP71 — uniform \(\gamma\)-tail theorem for polylogarithmic modulus classes

Date: 2026-10-04  
Status: **ANALYTIC LEMMA DERIVED; BRIDGE NORMALIZATION STILL SEPARATE**

## Objective

Replace the finite-height \(P=40\) tail charge by an asymptotic theorem that
can actually support the exact \(71.1640\%\) Stage-A target.

The relevant coefficients are

\[
\gamma_d=\sum_{e\ge1}\mu(e)\beta_{de},
\]

with

\[
\beta_q=
\frac{\mu(q/(q,b_1))\mu(q/(q,b_2))}
{\varphi(q/(q,b_1))\varphi(q/(q,b_2))}.
\]

The modulus parameters consumed by the analytic reduction satisfy

\[
b_1,b_2\le(\log X)^B
\]

for fixed \(B\).

## 1. Exact Euler-local factorization

Because \(\beta\) is multiplicative and \(\mu(e)\) allows only local
exponents \(0,1\),

\[
\boxed{
\gamma_d=
\prod_p f_p(v_p(d)),
\qquad
f_p(v)=\beta_p(v)-\beta_p(v+1).
}
\]

This is the same local identity that exposed and repaired the bookkeeping bug
in the public diagnostic helper.

For a generic odd prime \(p\nmid b_1b_2\),

\[
f_p(0)=1-\frac1{(p-1)^2},
\qquad
f_p(1)=\frac1{(p-1)^2},
\qquad
f_p(v)=0\quad(v\ge2).
\]

At the generic prime \(2\),

\[
f_2(0)=0,\qquad f_2(1)=1,\qquad f_2(v)=0\ (v\ge2).
\]

For a special prime \(p\mid b_1b_2\), if

\[
E_p=\max(v_p(b_1),v_p(b_2)),
\]

then

\[
\boxed{f_p(v)=0\qquad(v\ge E_p+2).}
\]

So every special local factor has finite support.

## 2. Rankin moment

Fix \(0<\sigma<1\).  By positivity,

\[
\sum_{d>D}|\gamma_d|
\le
D^{-\sigma}
\sum_d|\gamma_d|d^\sigma
=
D^{-\sigma}
\prod_p L_p(\sigma),
\]

where

\[
L_p(\sigma)
=
\sum_{v\ge0}|f_p(v)|p^{\sigma v}.
\]

For a generic odd prime,

\[
L_p(\sigma)
=
1+\frac{p^\sigma-1}{(p-1)^2}
=
1+O(p^{\sigma-2}).
\]

Hence

\[
\boxed{
M_\sigma:=
\prod_{p>2,\ p\ {\rm generic}}L_p(\sigma)<\infty
}
\]

for every \(\sigma<1\).

The finite set of special primes changes this product only by local
replacement factors.

## 3. Uniform special-prime growth

For \(p\mid2b_1b_2\), use

\[
|f_p(v)|\le|\beta_p(v)|+|\beta_p(v+1)|\le2.
\]

Therefore

\[
L_p(\sigma)
\le
2\sum_{v=0}^{E_p+1}p^{\sigma v}
\ll_\sigma
p^{\sigma(E_p+1)}.
\]

There are at most the primes dividing \(2b_1b_2\), and \(b_1,b_2\) are
prime powers in the ledger.  Consequently

\[
\prod_{p\mid2b_1b_2}L_p(\sigma)
\ll_\sigma
(b_1b_2)^\sigma\,\operatorname{rad}(2b_1b_2)^\sigma
\ll_\sigma
(b_1b_2)^{2\sigma}.
\]

Thus a fully uniform crude bound is

\[
\boxed{
\sum_{d>D}|\gamma_d|
\ll_\sigma
D^{-\sigma}(b_1b_2)^{2\sigma}.
}
\]

Since \(b_1b_2\le(\log X)^{2B}\),

\[
\sum_{d>D}|\gamma_d|
\ll_{\sigma,B}
D^{-\sigma}(\log X)^{4B\sigma}.
\]

## 4. The finite class subtraction

The paper's \(\gamma^{\rm free}\) additionally subtracts the finite
\(D\)-bar/special-prime class.

That correction is supported only on the special primes.  From the local
support above,

\[
d_{\rm class}
\le
\prod_{p\mid2b_1b_2}p^{E_p+1}
\le
(2b_1b_2)^2.
\]

Therefore, if

\[
D>(2b_1b_2)^2,
\]

the class correction contributes **nothing** to the omitted \(d>D\) tail.

## 5. Polylogarithmic cutoff

Take

\[
D=(\log X)^K.
\]

For fixed \(B\), choosing

\[
\boxed{K>4B}
\]

kills the finite special class for all sufficiently large \(X\).

The full Rankin tail then satisfies

\[
\sum_{d>D}|\gamma_d|
\ll
(\log X)^{-\sigma K+4B\sigma}.
\]

Given any required power \(A>0\), it is enough to choose

\[
\boxed{
K>4B+\frac{A}{\sigma}.
}
\]

With the concrete \(\sigma=2/3\) used in our independent numerical closure,

\[
K>4B+\frac{3A}{2}
\]

gives

\[
\boxed{
\sum_{d>D}|\gamma_d|
=O((\log X)^{-A}).
}
\]

## 6. Sawtooth consumer

The finite-\(J\) identity has the form

\[
\sum_{j\le J}\mathrm{tail}(j)\,\mathrm{row}_j(\theta)
=
\sum_d\gamma_d^{\rm tail}
S_0(d\theta;\lfloor J/d\rfloor).
\]

Using the already certified uniform constant

\[
|S_0(x;K)|\le2.10,
\]

the omitted \(d>D\) part obeys

\[
\left|
\sum_{d>D}\gamma_d^{\rm tail}S_0(\cdots)
\right|
\le
2.10\sum_{d>D}|\gamma_d|
=
O((\log X)^{-A}).
\]

Because \(A\) is arbitrary after choosing \(K\), any fixed polylogarithmic
number of modulus families or bookkeeping factors can be absorbed.

Thus the signed \(\gamma\)-resummed singular-series tail is

\[
\boxed{o(1)}
\]

uniformly over the polylogarithmic modulus range.

## 7. What this closes

This removes the *arithmetic omitted-\(d\) tail* as a permanent constant in
the asymptotic Stage-A ledger.

It also explains why the crude absolute F-E3c helper can fire while the
correct signed resummation remains small: the two bounds discard different
amounts of local cancellation.

The proof does **not** by itself establish the final \(71.1640\%\) result.
Still separate are:

1. the exact bridge/glue normalization into the same \(R\);
2. the continuum transfer of the finite prime-power ledger;
3. covered/middle/low-zone and collar errors;
4. the third-moment input used by the degree-two consumer.

Subject to those interfaces, the tail contribution can be taken \(o(1)\), so
the exact core target remains

\[
R\le-\frac1{48}+o(1),
\]

which yields

\[
\frac{N_0^s}{N}\ge\frac{269}{378}=71.1640\ldots\%.
\]

## Machine audit

\`src/wp71_uniform_gamma_tail_local.py\` checks the exact local support and
generic local formulas over a finite adversarial grid of primes/exponents.
Those checks supplement, but do not replace, the analytic proof above.
