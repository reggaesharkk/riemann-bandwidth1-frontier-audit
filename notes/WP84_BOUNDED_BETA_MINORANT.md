# WP84 — bounded fixed-pole beta minorants

Date: 2026-10-04

Status: **PREFERRED POSITIVE-INDEX CONSUMER; BOUNDED IN [-1,1], RANK-VARIATION CONSTANT INDEPENDENT OF DEGREE, MODEL m=10 AT 79.6269535%**

The earlier family r_m captured the positive-support model efficiently but paid an exponentially large negative penalty near x=-1. That makes it unnecessarily fragile if the true matrix has a nontrivial negative spectrum.

This note replaces it with a bounded family using the same fixed pole locations.

## 1. Definition

Put

    t(x)=2x/(1+x^2),

so t(x) lies in [-1,1] and has the same sign as x.

For m>=0 define

    D_m = integral_0^1 (1-s^2)^m ds

and

    p_m(t)=D_m^(-1) integral_0^t (1-s^2)^m ds.

Finally set

    boxed:
    b_m(x)=p_m(t(x)).

Since p_m is odd and monotone on [-1,1], with p_m(-1)=-1 and p_m(1)=1,

    -1 <= b_m(x) <= 1.

For x<=0, b_m(x)<=0. For x>0, 0<b_m(x)<=1. Therefore

    boxed:
    1_{x>0} >= b_m(x)

pointwise on the whole real line.

## 2. Rational / fixed-pole structure

Expanding

    p_m(t)
      = D_m^(-1) sum_{j=0}^m (-1)^j binom(m,j) t^(2j+1)/(2j+1),

shows that b_m is rational in x with denominator

    (1+x^2)^(2m+1).

Thus its only poles are still

    +i and -i,

now of order at most 2m+1.

A uniform resolvent law on one fixed circle around i therefore controls every fixed b_m by Cauchy's formula.

## 3. Rank robustness is degree-independent

As x runs from -infinity to +infinity, t(x) follows

    0 -> -1 -> +1 -> 0.

Because p_m is monotone, the total variation of b_m on the real line is

    boxed:
    Var(b_m)=1+2+1=4,

for every m.

Hence a rank-r Hermitian perturbation changes the normalized statistic by at most

    4r/d.

This is dramatically better than the exponential variation 2^(m+1) of the previous r_m family.

## 4. Trace-norm stability

The derivative in t is

    p_m'(t)=(1-t^2)^m/D_m,

so

    sup |p_m'|=1/D_m.

Also

    |t'(x)|<=2.

Therefore

    boxed:
    Lip(b_m)<=2/D_m.

For every fixed m this is an absolute constant, and

    |tr b_m(A)-tr b_m(B)|
      <= (2/D_m) ||A-B||_1.

So the source-closed tail trace-norm transfer remains compatible with this family.

## 5. Exact model reconnaissance

Using the same current four-node extremal quadrature and exact reduction modulo the Christoffel cubic gives:

| m | pole order | model q=E[b_m] | model simple 2q-1 |
|---:|---:|---:|---:|
| 0 | 1 | 0.803853818196... | 0.607707636393... |
| 1 | 3 | 0.877324405932... | 0.754648811865... |
| 2 | 5 | 0.892428709266... | 0.784857418532... |
| 3 | 7 | 0.896441294894... | 0.792882589788... |
| 4 | 9 | 0.897611568962... | 0.795223137924... |
| 5 | 11 | 0.897968871368... | 0.795937742735... |
| 6 | 13 | 0.898081306073... | 0.796162612147... |
| 7 | 15 | 0.898117530407... | 0.796235060813... |
| 8 | 17 | 0.898129435257... | 0.796258870514... |
| 9 | 19 | 0.898133415972... | 0.796266831944... |
| 10 | 21 | **0.898134767536...** | **0.796269535072...** |

The m=10 model consumer is already above 79% by about 0.62695 percentage points and lies only about 1.43e-6 below the current conditional Christoffel model rung.

More importantly, the positive-index threshold for >79% is q=0.895, so the m=10 model margin is

    boxed:
    q_10-0.895 ~= 0.00313477.

## 6. Why this is safer than the old r10 target

The old r10 minorant takes the value 1-2^10=-1023 at x=-1. Even a small amount of moderate negative spectrum can therefore destroy its trace statistic.

The new b_10 always lies in [-1,1]. It never charges one negative eigenvalue more than one unit.

Thus the model margin now corresponds to a genuinely robust bounded observable rather than a large-negative-tail surrogate.

## 7. Preferred theorem target

The fixed-circle resolvent theorem should now target b_10 (or, if derivative constants become inconvenient, b_4/b_5 as lower-order fallbacks).

A theorem-grade conclusion still requires the actual fixed-circle resolvent law. The table above is model reconnaissance and is not used as proof of that law.

Companion exact checker:

    `src/wp84_beta_minorant_model.py`.

## 8. Conditioning update — theorem target versus model target

A later fixed-circle conditioning audit shows that boundedness/rank robustness and analytic conditioning are different questions.

The Laurent pole order of b_m is 2m+1.  If a uniform Stieltjes-transform error epsilon is transferred by raw Cauchy estimates on |z-i|=rho, the statistic error is bounded by

    C_m(rho) * epsilon,

with C_m growing rapidly with m.

At rho=0.9:

- b3 has model q=0.8964412949 and requires epsilon < about 3.59e-5 to retain q>0.895;
- b10 has model q=0.8981347675 but requires epsilon < about 5.14e-8.

Therefore b10 remains the strongest model member of the displayed ladder, but **b3 is the current preferred theorem target** under the available fixed-circle transfer.

See `WP84_BETA_CIRCLE_CONDITIONING.md` and `src/wp84_beta_circle_conditioning.py`.


## 9. Hostile-audit correction — Radau values are not theorem margins

A subsequent exact falsifier shows that the displayed q_m table is evaluation
on one particular Radau representing measure, not a universal bound over all
measures with the pinned moments.

In particular, an exact positive rational seven-atom measure matching
m0..m6 has

    E[b3] = 0.890363090084... < 0.895.

Therefore the statement 'b3 already clears 79%' is valid only as model
reconnaissance for that chosen quadrature, not as a moment-implied theorem
margin.

Consequences:

- the 3.59e-5 fixed-circle number remains a correct Cauchy transfer tolerance
  relative to the Radau surrogate;
- it is not an active theorem budget until the actual limiting spectral law
  is identified and its b3 value is certified;
- neither b3 nor b10 is presently designated as the theorem consumer.

See:

    notes/WP84_EXTERNAL_AUDIT_RECONCILIATION_2026_10_05.md
    src/wp84_b3_radau_surrogate_falsifier.py
