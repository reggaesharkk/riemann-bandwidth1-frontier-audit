# WP84 — exact continuous spread–Dirichlet trace identity

Date: 2026-10-05

Status: **FINITE FOURIER-COMPRESSION WORD TRACE CLOSED EXACTLY; NEAR-RESONANCE KERNEL EXPOSED**

The earlier non-cyclic lattice identity says that a translation word has zero
trace unless its total discrete shift closes exactly.

The actual Gabor compression has real, non-lattice shifts.  Its exact analogue
is a Dirichlet kernel rather than a Kronecker delta.

This note derives that analogue.

## 1. Sharp partial-translation word

On the physical interval

    I=[-L/2,L/2],

let

    U_y f(x)
      = 1_{x,x+y in I} f(x+y)

for signed y.

For a word

    W=U_{y_1} ... U_{y_b},

define partial sums

    p_0=0,
    p_j=y_1+...+y_j,

the net displacement

    Y=p_b,

and the spread

    R=max_j p_j - min_j p_j.

Then exactly

    W
      = M_{I_word} T_Y,

where T_Y is translation by Y and I_word is one interval of length

    boxed:
    |I_word|
      = (L-R)_+.

This is the continuous version of the truncated-shift overlap law.

## 2. Compress to d consecutive Fourier modes

Let

    e_k(x)=L^(-1/2) exp(i2*pi*k*x/L),
    k=0,...,d-1,

and let P_d be their projection.

For every k,

    <e_k, W e_k>
      = (L-R)_+/L
          * exp(i2*pi*k*Y/L).

Therefore the normalized finite trace is exactly

    boxed:
    tau_d(P_d W P_d)
      = O_b(y_1,...,y_b)
          D_d(Y/L),

where

    O_b
      = (1-R/L)_+,

and

    D_d(s)
      = (1/d) sum_{k=0}^{d-1} exp(i2*pi*k*s).

If the prime carrier factors are retained, the word merely acquires the
unit-modulus scalar

    exp(iT Y).

Thus the full finite trace is

    exp(iT Y) O_b D_d(Y/L).

## 3. Closed words recover the exact overlap model

If

    Y=0,

then

    D_d(0)=1

and hence

    tau_d = O_b.

So every exact closed multiplicative word reproduces the overlap factor used
by the connected/cumulant model **without any limiting argument**.

This is the exact bridge between the finite Fourier compression and the
previous spread law.

## 4. Nonclosed words carry a universal Dirichlet penalty

For s not an integer,

    |D_d(s)|
      = |sin(pi d s)|/[d |sin(pi s)|]
      <= 1/[d |sin(pi s)|].

A nonzero word with O_b>0 has

    |Y|<L,

so |s|<1.

Using

    sin(pi u) >= 2u,
    0<=u<=1/2,

and symmetry around 1 gives:

for

    0<|Y|<=L/2,

    boxed:
    |tau_d|
      <= L/(2d |Y|);

for

    L/2<=|Y|<L,

the overlap itself obeys

    O_b <= 1-|Y|/L,

which cancels the endpoint singularity and yields

    boxed:
    |tau_d|
      <= 1/(2d).

Since

    d=floor(TL/(2*pi)),

the only macroscopic nonclosed leakage occurs in the window

    boxed:
    |Y| = O(1/T).

Equivalently, for multiplicative words,

    Y=log(A/B),

so the finite-compression debt is exactly a near-multiplicative-resonance
problem

    |log(A/B)| <= O(1/T).

## 5. Interaction with prime-base grouping

For a first-order current prime-base group G_p, unique factorization rules out

    Y=0

at every finite word length because the previous state contains no p-base
factor.

Therefore every such monomial is forced into the Dirichlet leakage term.

The arithmetic theorem is now sharply stated:

    bound the weighted population of distinct-base words with
        |log(A/B)| <= O(1/T).

No exact current-base diagonal remains hidden in the drift.

## 6. Cheap low-word consequences

Suppose every individual prime power in a word is at most N<T.

For a two-factor nonclosed relation A/B with A,B<=N,

    |log(A/B)|
      >= c/N

for an absolute c once N is large.

Hence if

    N/T -> 0,

the two-factor leakage is uniformly o(1).

The adaptive endpoint deletion gives exactly

    N/T <= exp(-W+o(1))

with W->infinity.

Thus all one-current/one-previous two-factor leakage is automatically
suppressed.

At three and more factors the elementary integer-spacing bound becomes

    |log(A/B)| >= c/N^m,

which is not sufficient when N=T^(1-o(1)).

That is where genuine higher joint-prime information begins.

## 7. Strategic consequence

The retained-range bounded theorem no longer has an amorphous
"finite-compression error."

It has an exact kernel:

    overlap spread
      x
    normalized Dirichlet kernel
      x
    carrier exp(iT log(A/B)).

Closed words are the exact model geometry; nonclosed words are localized to
1/T-scale multiplicative near-resonances.

This is the arithmetic interface to attack next.

No unconditional >79 theorem is claimed.
