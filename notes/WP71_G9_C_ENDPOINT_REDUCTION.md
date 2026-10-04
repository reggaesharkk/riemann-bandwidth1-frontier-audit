# WP71 G9-C — endpoint reduction and the single analytic target

Date: 2026-10-04
Status: **EXACT REDUCTION CLOSED; maximal shifted-prime input still to be proved**

The moving-interval audit reduced the general welding error, outside the
lower-dimensional j=0 puncture family, to

e_k(n) = E_{rk}(U_k(n)) - E_{rk}(L_k(n)-1),

where E_h(t) is the cumulative prime-pair error at shift h.

This note isolates one sufficient analytic statement which would close the
general middle-band remainder.

## 1. Maximal short-interval pair-error norm

On a dyadic prime scale M let Y be an upper bound for the length of every
moving interval in the cell. For the hard j-strip,

Y <= min(B_k-A_k+1, floor(2J/b2)+2).

Define

D_h(u,v)
 =
sum_{u<m<=v} Lambda(m)Lambda(m-h)
-
S(h)(v-u),

and

Emax(h;M,Y)
 =
sup_{M<=u<v<=2M, v-u<=Y} |D_h(u,v)|.

The moving interval I_k(n) is always one of these intervals, up to the
already isolated j=0 puncture. Therefore

|e_k(n)| <= 2 Emax(rk;M,Y)

for every admissible n.

No smoothness or number theory is used here; this follows directly from the
two-endpoint representation.

## 2. Exact shift-only Cauchy--Schwarz

Let G_{k,n} be the signed slow geometry/kernel coefficient after all fixed
cell prefactors are extracted, and put

A_{k,n}=Lambda(n)Lambda(n-qk).

The endpoint remainder is

R_end = sum_k sum_n G_{k,n} A_{k,n} e_k(n).

Define the nonnegative outer weight budget

W_k = sum_n |G_{k,n}| A_{k,n}.

Then, without applying Cauchy--Schwarz in n or across the cell family,

|R_end| <= 2 sum_k Emax(rk;M,Y) W_k,

and hence

boxed:
|R_end|
 <=
2
( sum_k Emax(rk;M,Y)^2 )^(1/2)
( sum_k W_k^2 )^(1/2).

This is exactly the allowed use of Cauchy--Schwarz: in the shift variable
only.

The signed main has already been removed before this inequality is invoked.

## 3. Sufficient analytic input

A sufficient prime-correlation theorem for G9-C is:

For every A and every polylogarithmic structured multiplier r,

boxed:
sum_{k<=K}
Emax(rk;M,Y)^2
 <<_A
K Y^2 (log M)^(-A),

uniformly in the Stage-A shift range and in the actual cell widths Y supplied
by the middle-band/Gallagher decomposition.

Call this the **maximal short-window structured-shift L2 input**.

Once it is available, any fixed logarithmic losses in the deterministic
outer budget W_k can be beaten by choosing A larger.

This is stronger than the already-derived fixed-window G2 statement for two
reasons: it is maximal over interval endpoints, and it must scale with the
actual short moving-window length Y rather than the ambient dyadic scale M.
Therefore G2 by itself does not close G9-C.

## 4. MRT evidence relevant to this target

The published MRT paper contains two pieces that are directly relevant:

1. Lemma 2.2 introduces a maximal-sum norm over arbitrary subintervals and
   proves summation-by-parts control for that maximal norm.
2. Corollary 2.5 controls an arbitrary interval truncation of a Dirichlet
   series by the untruncated Dirichlet series with only logarithmic losses.
   The proof of Proposition 5.4 explicitly invokes Corollary 2.5 to remove a
   support truncation before the mean-value argument.

Those facts make a maximal short-window extension plausible, but they do not
by themselves prove the exact Stage-A statement above. The scale Y and all
MRT parameter inequalities still have to be tracked through the circle-method
reduction.

## 5. Two legitimate completion routes

### Route M1 — smooth maximal family

Replace the hard endpoint indicator by the same smooth family used at the
Gallagher scale, use MRT's truncation/maximal machinery before the
mean-value estimate, and pay the hard/smooth difference through G7.

### Route M2 — direct endpoint family

Push Corollary 2.5 through the Proposition 5.4 to Proposition 3.4 reduction
with the interval endpoints left arbitrary, and then prove the resulting
correlation estimate in the maximal norm of Lemma 2.2.

This route must verify, cell by cell:

- X and the dyadic prime scale;
- the short interval length Y;
- H >= X^(8/33+epsilon);
- q <= (log X)^B;
- X^(-1/6-epsilon) <= lambda <= 1/(qQ);
- all extra logarithmic losses from truncation/maximalization.

Until M1 or M2 is written completely, G9-C remains open.

## 6. Deterministic outer-budget obligation

The second factor

( sum_k W_k^2 )^(1/2)

contains no inner prime-pair uncertainty. It is a geometry/outer-pair budget.
G9-D must place it in the exact public normalization

1/(pi*l*X*ell1^4)

and prove that its growth costs only fixed logarithmic powers plus the already
charged cell-mass factors.

## 7. Gate map

- G9-A exact welding reindexing: CLOSED.
- G9-B local Euler factorization: CLOSED.
- G9-B rectangular main calibration: CLOSED.
- G9-B moving-interval combinatorics: CLOSED.
- G9-B j=0 support isolation: CLOSED IN SHAPE / lower-dimensional charge.
- G9-C endpoint reduction: CLOSED.
- G9-C maximal short-window structured-shift L2 theorem: OPEN.
- G9-D exact R-unit outer-budget normalization: OPEN.

This is the smallest honest analytic target currently visible for the
middle-band glue.
