# WP84 — scale conditioning for the preferred r2 theorem

Date: 2026-10-05

Status: **THEOREM-CONDITIONING RECONNAISSANCE — a=6/5 IMPROVES THE NEW O(R^-1) BAND-TAIL MARGIN RATIO OVER a=1 WHILE RETAINING A LARGE RECORD GAP**

No unconditional zero-density percentage is claimed here.

The model-only hierarchy initially preferred

    a=1

because it maximizes the available r2 model value among the simple scales we
tested.

After the new one-point resolvent tail theorem, however, the proof cost has
an explicit dependence on the pole height a.

That changes the conditioning problem.

## 1. Scaled consumer

For a>0,

    r_{2,a}(x)
      =
      1
      -
      [
        (x-a)^2/(x^2+a^2)
      ]^2.

It is support-free:

    r_{2,a}(x)<=0  for x<=0,
    0<r_{2,a}(x)<=1 for x>0.

Its exact partial fraction formula is

    r_{2,a}(x)
      =
      a(2+i)/(x-ia)
      - a^2/(x-ia)^2

      + conjugate lower-half-plane terms.

So the theorem consumes only

    m(ia),
    m'(ia).

## 2. New O(R^-1) truncation constant scales like a^-2

The sharpened displacement-tail theorem gives, with q_alpha=1/4+o(1),

    |
      m_H(ia)-m_{H_R}(ia)
    |

      <=
      6/(pi^2 a^3 R)
      +o(R^-1).

For m'(ia), take a Cauchy circle of radius

    rho a,
    0<rho<1.

The minimum imaginary part on the circle is

    a(1-rho),

hence

    |
      m_H'(ia)-m_{H_R}'(ia)
    |

      <=
      6/
      [
        pi^2
        rho(1-rho)^3
        a^4 R
      ]
      +o(R^-1).

Insert the coefficients of r_{2,a}.  The total r2 displacement error is

    <=
    12/
    (pi^2 a^2 R)
    [
      sqrt(5)
      + 1/(rho(1-rho)^3)
    ]
    +o(R^-1).

The factor

    rho(1-rho)^3

is maximized at

    rho=1/4.

Therefore the explicit leading constant is

    boxed:

    C_band(a)
      =
      12/pi^2
      [
        sqrt(5)+256/27
      ]
      * a^(-2)

      ~= 14.24683177/a^2.

Thus larger pole height buys a quadratic improvement in the leading
band-tail constant.

## 3. Exact model value at a=6/5

Using exact reduction modulo the pinned Christoffel cubic,

    boxed:

    q_{6/5}

      =
      113898001480425765678720
      /
      130234262317191955294681

      =
      0.8745624957203779....

The corresponding model simple-zero ledger is

    boxed:

    2 q_{6/5}-1

      =
      97561740643659576062759
      /
      130234262317191955294681

      =
      0.7491249914407558....

So this rung has model simple-zero value

    74.912499144...%.

It remains a model/consumer value only.

## 4. Record margin

Against

    q_rec
      =
      0.8367500185439279...,

the positive-index model margin is

    boxed:

    Delta_{6/5}
      =
      0.03781247717644998....

For comparison:

    a=1:
      Delta_1
        =
        0.0466326939503807....

The raw margin is smaller at a=6/5.

But the analytic band-tail constant is also substantially smaller.

## 5. Proof-conditioning metric

If band truncation were the dominant error, the required R scales like

    C_band(a)/Delta_a.

Equivalently one should maximize

    Delta_a a^2.

Numerical reconnaissance of the exact pinned quadrature gives a smooth
maximum near

    a ~= 1.21038.

At the simple rational choice

    boxed:
    a=6/5=1.2,

we have

    Delta_a a^2
      ~= 0.05444997,

whereas

    a=1

gives

    Delta_1
      ~= 0.04663269.

Thus the new leading-margin efficiency improves by about

    16.8%.

The exact continuous optimum is not needed for the theorem architecture.

The rational a=6/5 is preferable for exact bookkeeping.

## 6. Other proof constants also improve with a

The same direction helps several other active errors.

Global Lipschitz:

    Lip(r_{2,a})
      <=
      8/a.

Fixed-pole resolvent norm:

    ||R(ia)||op
      <=
      1/a.

The Gaussian/Bernoulli replacement constants contain fixed powers of the
inverse pole gap and therefore also improve as a increases.

Finite-band Combes--Thomas localization at z=ia likewise permits a larger
conjugation perturbation before the spectral gap is exhausted.

So the a^-2 band improvement is not an isolated benefit.

## 7. Why a=3/2 is too far

At a=3/2 the model positive-index margin falls to about

    0.0165040971,

and

    Delta_a a^2
      ~= 0.0371342,

which is worse than both a=1 and a=6/5.

Thus the earlier a=3/2 rung remains a robustness check but is no longer the
best conditioned first strike.

## 8. Updated recommendation

Maintain two parallel exact consumers:

A. maximal raw model margin:
       a=1,
       model simple ledger 76.6765425...%;

B. better current theorem conditioning:
       a=6/5,
       model simple ledger 74.9124991...%.

For the current O(R^-1) displacement/locality architecture, use a=6/5 as the
primary conditioning candidate and keep a=1 as the stronger-margin fallback.

Do not freeze this choice irreversibly until the remaining local arithmetic
error is expressed with its explicit a-dependence.

See:

    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md
    notes/WP84_SCALED_R2_RECORD_RUNG.md
