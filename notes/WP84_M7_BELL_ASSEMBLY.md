# WP84 — exact Bell(7) model assembly

Date: 2026-10-05

Status: **SEVENTH-MOMENT LEDGER REDUCED TO TWO NEW MODEL CONSTANTS**

The model-side seventh moment can be assembled exactly from the Bell(7)
partition ledger and the already-established frozen-singleton identities.

The key result is

    boxed:
    m7
      = 1717/90
        + {5,2}
        + C7.

Thus the exact mixed spectator constant `{5,2}` and the pure connected
seven-cycle constant `C7` are the only new model values needed to freeze
`m7).

Companion checker:

    src/wp84_m7_bell_assembly.py

## 1. Bell(7) class counts

The 877 set partitions of seven slots split as

    1^7             1
    2,1^5          21
    2^2,1^3       105
    2^3,1         105
    3,1^4          35
    3,2,1^2       210
    3,2^2         105
    3^2,1          70
    4,1^3          35
    4,2,1         105
    4,3            35
    5,1^2          21
    5,2            21
    6,1             7
    7               1.

The classes containing a 3-block vanish under the already-established
odd-3-block local law.

## 2. Frozen lower-order pieces

The class `{2,2,1,1,1}` has the exact cyclic chord split

    70 noncrossing,
    35 crossing,

hence contributes

    70 t_adj + 35 t_opp.

The `{4,1,1,1}` class contributes

    35 Phi4.

Freezing one singleton in the no-singleton six-cycle classes gives seven
copies of each of

    {2,2,2},
    {4,2},
    {6}.

Freezing two singletons around the five-cycle connected class gives

    21 C5.

Together with the singleton/pair classes, the known contribution is

    1
    +21*(1/3)
    +70*(7/60)
    +35*(1/30)
    +35*(-1/60)
    +7*(131/420)
    +7*(-23/420)
    +21*(1/36)
    +7*(-1/126)

      = 1717/90.

The only no-singleton classes not already known are therefore

    {5,2},
    {7}=C7.

## 3. Useful form once C7 is certified

If the exact C7 computation closes at the reconnaissance value

    C7=-17/360,

then

    boxed:
    m7
      = 6851/360 + {5,2}.

This turns the entire exact m7 problem into one mixed `{5,2}` fraction after
C7 is certified.

## 4. Consequence for the >80 model gate

The exact k=8 go/no-go can now be staged efficiently:

1. complete C7;
2. compute exact `{5,2}`;
3. assemble exact m7 from the boxed identity;
4. assemble exact m8;
5. evaluate `m8<T80(m7)` before any new arithmetic transport.

No model value for `{5,2}` is inferred from the reconnaissance m7 band.
No >80 arithmetic theorem is claimed.
