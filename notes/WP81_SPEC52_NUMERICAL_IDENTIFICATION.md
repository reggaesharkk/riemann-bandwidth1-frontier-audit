# WP81 — numerical identification of the {5,2} model constant

Date: 2026-10-05

Status: **THREE-RUNG MIDPOINT IDENTIFICATION; EXACT POLYTOPE CERTIFICATION STILL REQUIRED**

A direct midpoint implementation of the already-frozen `{5,2}` specification
was run at three grid spacings.

The implementation was first regression-checked against the public
`{4,2}` spectator-pair specification.  At both `dv=0.1` and `dv=0.05`
it reproduces all three recorded class values to floating-point roundoff:

    dv=0.1:
      U1=-0.006870600
      U2=-0.000765600
      U3=-0.004327950
      total=-0.058801050

    dv=0.05:
      U1=-0.0064807515625
      U2=-0.0007866890625
      U3=-0.00405844453125
      total=-0.05577997734375.

Thus the pair-placement geometry, midpoint convention, connected-cumulant
signs, and class multiplicities agree with the frozen lower-rung reference.

## 1. New {5,2} ladder

For the seven-cycle spectator-pair specification

    {5,2}=7(U1+U2+U3),

the first three midpoint rungs are:

    dv=0.20:
      U1 = 0.0105216000000000
      U2 = 0.0028064000000000
      U3 = 0.0059840000000000
      {5,2} = 0.135184000000000

    dv=0.10:
      U1 = 0.0100831500000000
      U2 = 0.0027847875000000
      U3 = 0.0053666250000000
      {5,2} = 0.127641937500000

    dv=0.05:
      U1 = 0.0099620414062500
      U2 = 0.0027795181640625
      U3 = 0.0052107871093750
      {5,2} = 0.125666426757812.

## 2. Pre-registered rational candidates

The clean denominator-2520 candidates are

    boxed:
    U1 = 5/504   = 25/2520,
    U2 = 1/360   =  7/2520,
    U3 = 13/2520,

so

    U1+U2+U3 = 1/56

and therefore

    boxed:
    {5,2} = 1/8.

The errors against these candidates obey the expected midpoint h^2 profile:

    total error:
      dv=.20  +0.0101840000
      dv=.10  +0.0026419375
      dv=.05  +0.000666426758

    successive error ratios:
      3.85475,
      3.96433,

approaching the quadratic value 4.

Componentwise, the .10/.05 error ratios are

    U1: 3.92487
    U2: 4.02768
    U3: 3.99360.

The two-rung Richardson extrapolation from .10/.05 is

    {5,2} = 0.125007923177...

which lies 7.9e-6 above 1/8.

This is identification evidence only.  The exact producer remains
target-blind; no candidate is inserted into the exact polytope computation.

## 3. Consequence if exact certification lands on 1/8

The exact Bell(7) assembly is

    m7 = 1717/90 + {5,2} + C7.

If the two independent exact certificates close at

    {5,2}=1/8,
    C7=-17/360,

then

    boxed:
    m7 = 862/45
       = 19.155555555....

This lies above the older reconnaissance upper endpoint 19.136.

Therefore that reconnaissance interval is now a fired diagnostic and must not
be used as a model constraint unless its assembly is independently recovered.

At the candidate exact value `m7=862/45`, the exact >80 m8 corridor has
width

    T80(m7)-F8(m7)
      = 14045331169/64647954000
      = 0.2172587112...,

almost an order of magnitude wider than the 0.02373565 corridor at
`m7=19.136`.

This materially improves the plausibility of the k=8 >80 rung, but it remains
conditional on exact `{5,2}`, exact `C7`, and the exact model `m8`.

## 4. Promotion rule

Do not consume `1/8` in a theorem or in the exact model go/no-go until the
450-term exact rational aggregate closes independently.

The exact verification should compare to the candidates only **after** all
work units are complete and the evidence digest is frozen.

No >80 theorem is claimed.
