# WP84 — bounded Christoffel ladder recovers the full 79.627 frontier

Date: 2026-10-05

Status: **PARAMETRIC BOUNDED CONSUMER FAMILY CLOSED; FULL HEADLINE RECOVERABLE IF THE FIXED-DELTA RESOLVENT THEOREM IS PROVED FOR EVERY FIXED DELTA**

Let

    g(x)=P(x)^2,

with the exact Christoffel cubic P, and

    w0 = 1415/13891.

For every delta>0 define

    F_delta(x)
      = (delta+1) g(x)/(g(x)+delta).

The pointwise half-line and moment bounds are

    F_delta(x)>=1     for x<=0,

and

    F_delta(x)
      <= (1+1/delta) g(x).

Hence every pinned-moment model law satisfies

    negative mass
      <= (1+1/delta) w0.

The exact simple-zero ledger therefore gives the bounded-consumer coefficient

    S(delta)
      = 1 - 2(1+1/delta)w0

      = 11061/13891
        - 2830/(13891 delta).

Thus S(delta) increases monotonically to

    boxed:
    11061/13891
      = 0.796270966813...
      = 79.6270966813... percent.

## 1. Concrete bounded targets

Examples:

    delta=161
      -> 79.5005569... percent

    delta=752
      -> 79.6000051... percent

    delta=2871
      -> 79.6200006... percent

    delta=9717
      -> 79.6250001... percent

    delta=18577
      -> 79.6260000... percent

    delta=1,000,000
      -> 79.6270763... percent.

Each target uses a **fixed bounded rational function**.  No delta(T)->infinity
limit is required.

Companion:

    src/wp84_bounded_christoffel_ladder.py

## 2. Full frontier from a fixed-parameter theorem family

Suppose the arithmetic theorem proves, for every fixed integer delta>=61,

    limsup_T tau(F_delta(H_T))
      <= (1+1/delta) w0.

Then for every such delta,

    liminf simple-zero proportion
      >= S(delta).

Because the left side is one fixed number independent of delta,

    liminf simple-zero proportion
      >= sup_{delta>=61} S(delta)

      = 11061/13891.

Therefore a theorem valid for **arbitrary fixed delta** recovers the complete
79.62709668... coefficient without ever using an unbounded finite-T
functional.

This is the key rank-robust replacement for the raw polynomial consumer.

## 3. Uniform pole strip for the whole ladder

The pole equation is

    P(z)^2 + delta = 0.

The exact delta=61 elimination shows that along

    Re P(x+iy)=0,
    |y|<=1,

one has

    |Im P(x+iy)|^2 < 61.

The real-part cubic has positive discriminant for every s=y^2>=0, so its
three real branches are continuous on 0<=s<=1.  Since the equality
|Im P|^2=61 has no solution there and all branches start at |Im P|=0 when
s=0, the strict inequality follows on the whole strip.

Consequently for every

    delta>=61,

the equation

    P(z)=+/- i sqrt(delta)

has no solution with |Im z|<=1.

Thus every F_delta in the active ladder has six nonreal poles satisfying

    boxed:
    |Im z_j|>1.

Moreover all poles are simple for delta>0 because P' has two real roots and
therefore cannot vanish at a point where P is nonzero purely imaginary.

So the fixed-nonreal resolvent geometry is stable throughout the entire
consumer ladder.

## 4. Strategic consequence

Do not freeze the project to delta=61.

Use delta=61 only as the easiest first closure target.

The theorem should be parameterized as:

    for every fixed delta>=61,
    bounded F_delta resolvent comparison holds.

Once that parameterized statement is closed, the exact headline returns to

    79.62709668... percent,

not merely 79.2931 percent.

No unconditional >79 theorem is claimed until the fixed-delta arithmetic
resolvent comparison is proved.
