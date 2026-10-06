# WP84 — centered-fourth scalar gate; lower-moment band penalty disappears

Date: 2026-10-05

Status: **EXACT ALGEBRAIC SHARPENING OF THE QUARTIC FALLBACK**

No unconditional zero-density percentage is claimed here.

The first fixed-band quartic note parameterized the theorem by the raw fourth
moment mu4(H_R).  A later note charged a positive O(1/R) penalty for the
band-induced variance deficit.

That penalty is unnecessary if the same quartic is written in the natural
centered variables.

## 1. Centered fixed-band state

Write

    H_R=I+P_R

up to the already-closed o(1) scalar-background errors.

Put

    v_R=tau(P_R^2),

    w_R=tau(P_R^4).

The degree-three gate gives

    tau(P_R)=o(1),

    tau(P_R^3)=o(1).

Hence

    mu1=1+o(1),

    mu2=1+v_R+o(1),

    mu3=1+3v_R+o(1),

    mu4=1+6v_R+w_R+o(1).

## 2. Exact simplification of the quartic majorant

Recall

    P4(x)
      =
      (593/2000)x^4
      -(212/125)x^3
      +(1761/500)x^2
      -(3133/1000)x
      +1011/1000.

Substitute the centered moments above.

The constant term is exactly

    boxed:
    1/2000,

and the variance coefficient is exactly

    boxed:
    213/1000.

Therefore

    boxed:

    tau P4(H_R)

      =
      1/2000
      +(213/1000) v_R
      +(593/2000) w_R
      +o(1).

At the target

    v=1/3,
    w=1/4,

this gives

    233/1600

as before.

## 3. Band variance deficit helps rather than hurts

The fixed-band pair variance satisfies

    v_R<=1/3+o(1).

Since the coefficient 213/1000 is positive,

    boxed:

    tau P4(H_R)

      <=
      1/2000
      +213/3000
      +(593/2000) w_R
      +o(1).

So no separate positive charge for

    1/3-v_R

is needed.

The earlier C_low/R term was an artifact of holding the raw mu4 fixed while
varying v_R independently.

For the actual centered identity

    mu4=1+6v_R+w_R,

the variance loss is favorable.

## 4. Exact centered-fourth threshold

Let

    E_rec
      =
      0.163249981456072...

and let the matched-filter full-to-band cost be

    C_match/R,

    C_match=2.1728342265....

A sufficient condition is

    boxed:

    w_R
      <
      W_R

where

    W_R
      =
      (2000/593)
      [
        E_rec
        -1/2000
        -213/3000
        -C_match/R
      ].

Numerically:

    R=256:
      W_R ~=0.2808173617,

    R=320:
      W_R ~=0.2865425784,

    R=400:
      boxed:
      W_R ~=0.2911227517,

    R=512:
      W_R ~=0.2951304034,

    R=768:
      W_R ~=0.2999014173,

    R=1024:
      W_R ~=0.3022869242.

## 5. Compare directly with the complete pair layer

The exact closed pair layer is

    P_pair
      =
      4/15
      =
      0.2666666666....

Therefore the allowed positive excess above the entire pair sector is

    B_R
      =
      W_R-4/15.

At useful bands:

    R=256:
      B_R ~=0.0141506951,

    R=320:
      B_R ~=0.0198759117,

    R=400:
      boxed:
      B_R ~=0.0244560851,

    R=512:
      B_R ~=0.0284637367,

    R=768:
      B_R ~=0.0332347506,

    R=1024:
      B_R ~=0.0356202576.

This is the cleanest arithmetic budget currently available.

## 6. Combine with pointwise Phi4 sign

The exact closed connected kernel now satisfies

    C4(v)<=0

pointwise.

Thus at the closed-cycle/model level

    centered fourth
      <=
      complete pair layer
      =
      4/15.

The theorem no longer needs to reproduce

    Phi4=-1/60

with its exact constant.

It only needs to control the positive finite-compression / near-resonance
error above the nonpositive closed connected main.

For R=400 that error may be as large as

    boxed:
    0.0244560851

and the record crossing still survives.

## 7. Corrected frontier

The previous statement

    "prove raw mu4(H_R)<3.288447..."

is sufficient but not the sharpest formulation.

The preferred statement is now

    boxed:

    prove
      tau(P_R^4)
        <
      0.2911227517

for R=400,

or equivalently prove that the positive finite-compression excess over the
closed pair layer 4/15 is less than

    0.0244560851.

This isolates exactly the part that needs arithmetic correlation control.

See:

    notes/WP84_MATCHED_QUARTIC_MAJORANT.md
    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
