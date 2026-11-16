# WP84 — sharp multiplication-resolvent trace closure

Date: 2026-10-04

Status: **DRIFT AND SAME-SIGN VARIANCE VANISH EXACTLY INSIDE THE SHARP MULTIPLICATION ALGEBRA; MIXED VARIANCE FUNCTIONAL EXPLICIT; ALGEBRA-CLOSURE TRANSFER OPEN**

This note turns the sharp variance channel into the exact scalar functional needed by the Lindeberg resolvent term.

## 1. Assume one multiplication resolvent

In the sharp flat physical representation, suppose an intermediate resolvent is multiplication by

    R=M_r

on x in [0,1].

For s in (0,1], write the two complex prime blocks, omitting only their harmless constants, as partial shifts

    U_s^+ F(x)=1_{x<=1-s} F(x+s),

    U_s^- F(x)=1_{x>=s} F(x-s).

The actual Cplus/Cminus blocks are 2*pi times these shifts with global carriers exp(+/- iTy).

## 2. First-order prime drift vanishes

The operator

    R U_s^+ R

is still a nonzero partial translation by +s. It has no diagonal kernel for s>0. The -s branch is identical.

Hence, in the sharp continuum trace model,

    boxed:
    tau(R C(s) R)=0

for every s>0.

The only zero shift would be n=1, but Lambda(1)=0.

Thus the prime-block first-order drift disappears identically **if the intermediate resolvent lies in the multiplication algebra**.

## 3. Same-sign variance branches vanish

Similarly,

    R U_s^+ R U_s^+ R

is a partial translation by +2s and has zero diagonal for every s>0. The negative branch translates by -2s.

Therefore

    boxed:
    tau(R Cplus(s) R Cplus(s) R)
      = tau(R Cminus(s) R Cminus(s) R)
      = 0

in the sharp multiplication model.

This kills V-sum geometrically; no twisted prime exponential-sum estimate is needed in that ideal algebra.

## 4. Mixed branches are explicit

The mixed traces are

    tau(R Cplus(s) R Cminus(s) R)
      = (2*pi)^2 integral_0^(1-s) r(x)^2 r(x+s) dx,

and

    tau(R Cminus(s) R Cplus(s) R)
      = (2*pi)^2 integral_s^1 r(x)^2 r(x-s) dx.

After the real-cosine factor 1/4 and the prime-square measure, Chebyshev--Mertens gives the limiting mixed variance scalar

    boxed:
    Vsharp[r]
      = 1/a_phi^2 * integral_0^1 r(x)^2
          [integral_0^1 |x-u| r(u) du] dx.

Equivalently, with

    (K r)(x)=a_phi^(-2) integral_0^1 |x-u|r(u)du,

we have

    Vsharp[r]=integral_0^1 r(x)^2 (K r)(x) dx.

This is exactly the trace-only functional sought in `WP84_VARIANCE_TOEPLITZ_RULES.md`.

## 5. Exact finite analogue

`src/wp84_sharp_resolvent_trace.py` verifies over exact rational arithmetic that for non-cyclic finite shifts and diagonal R:

- first-order shifted traces vanish;
- same-sign second-order shifted traces vanish;
- mixed traces equal the shifted cubic diagonal sums.

So no cancellation assumption is hidden in the branch bookkeeping.

## 6. New theorem bottleneck

The resolvent problem is now conditional on one structural statement:

    **ALG-star:** after permutation averaging, the intermediate resolvents are asymptotically represented, in the normalized traces consumed by Lindeberg, by multiplication/Toeplitz symbols on the sharp physical interval.

If ALG-star holds with o(1) error, then:

1. the prime drift is o(1);
2. V-sum is o(1);
3. V-diff is the explicit |x-u| functional above;
4. cubic-and-higher block terms are already O(L^-3).

At that point the fixed-circle law becomes a closed commutative integral-equation problem rather than a new prime-correlation theorem.

## 7. What ALG-star must include

A theorem-grade version must control:

- the actual w=1 ramp taper versus the sharp interval;
- finite Gabor compression versus the infinite physical representation;
- the smooth mu+Pi background;
- uniformity for z on the fixed Cauchy circle;
- stability through the permutation/subset evolution.

These are now the only places where noncommutative leakage can re-enter.

## 8. Evidence boundary

This note does not assert that the true intermediate resolvent is multiplication. It proves exactly what follows **if** that algebra closure is established, and identifies the corresponding scalar functional without guessing it.

## 9. Order-four status correction

The multiplication-algebra hypothesis used in §§2--4 is **not** an
established closure theorem.

The exact order-four audit now shows why it cannot be promoted:

- scalar multiplication covariance retains only the adjacent pair class and
  gives centered m4=7/30;
- the full operator pair layer must also retain the alternating/crossing class
  t_opp=1/30, raising the pair layer to 4/15;
- the connected non-pair sector then contributes Phi4=-1/60, giving 1/4.

Therefore the statements

    drift vanishes,
    same-sign variance vanishes

remain valid only **inside the assumed multiplication algebra**.  They may
not be used to eliminate those channels in the true operator-valued flow,
because doing so deletes the word sectors needed at order four.

The multiplication calculation is retained as a falsified closure benchmark,
not as the active theorem route.

See:

    notes/WP84_M4_LINDEBERG_WORD_ATTACK.md
    notes/WP84_M4_LATEST_BLOCK_DECOMPOSITION.md
    notes/WP84_OPERATOR_GENERATOR_M4_GATE.md
