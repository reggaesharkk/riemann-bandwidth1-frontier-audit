# WP84 — symmetric cubic linearization of the bounded Christoffel consumer

Date: 2026-10-06

Status: **EXACT BOUNDED-FUNCTIONAL REDUCTION — THE SIX H-PLANE POLES COLLAPSE TO ONE CORNER OF ONE 3-LAYER SYMMETRIC LINEAR PENCIL; DISPLACEMENT RANK IS AT MOST SIX**

No unconditional >79 percent theorem is claimed in this note.

The degree-six Christoffel square should not be transported as a raw sixth
moment of the full arithmetic matrix.  The bounded rational consumer can
instead be linearized before any arithmetic comparison.  This keeps the
Proposition-R firewall intact and turns the active >79 target into a
goal-oriented finite-channel problem.

## 1. Christoffel polynomial

Write

    P(x)=p0+p1 x+p2 x^2+p3 x^3

with

    p0 = 1,
    p1 = -43428/13891,
    p2 =  37704/13891,
    p3 =  -9660/13891.

Put

    r = -p3 = 9660/13891,

    b = -p2/(2r)
      = -1571/805,

    c = -p1-r b^2
      = 5343048/11182255.

These constants are exact rationals.

For a complex parameter z define the 3 by 3 symmetric scalar pencil

    L_z(x)
      =
      [ r x        1             0          ]
      [ 1          0             x+b        ]
      [ 0          x+b           c x+z-p0   ].

A direct determinant expansion gives

    boxed:
    det L_z(x)
      =
      P(x)-z.

The (3,3) cofactor is exactly -1.  Therefore

    boxed:
    (L_z(x)^(-1))_33
      =
      -1/(P(x)-z).

This identity contains the whole cubic rationalization.

## 2. Matrix functional calculus

For a real-symmetric Hermitian theorem matrix H, replace x by H blockwise:

    mathcal L_z(H)
      =
      [ rH          I             0              ]
      [ I           0             H+bI           ]
      [ 0           H+bI          cH+(z-p0)I     ].

Because every block is a polynomial in H, diagonalizing H reduces
mathcal L_z(H) to the scalar fibers L_z(lambda).  Hence for Im z != 0 it is
invertible and

    boxed:
    (P(H)-zI)^(-1)
      =
      -[mathcal L_z(H)^(-1)]_33.

The pencil is symmetric under transpose:

    mathcal L_z(H)^T=mathcal L_z(H),

so its inverse has the same transpose symmetry.  This preserves the algebraic
symmetry used by the existing D1/D2 displacement calculations.

For each fixed nonreal z,

    sup_{x real} ||L_z(x)^(-1)|| < infinity.

Indeed every inverse entry is a rational function with numerator degree at
most two and denominator P(x)-z; it is continuous on the real line and
decays or stays bounded at infinity.  Thus the linearized inverse has a
T-independent operator bound.  No raw H^6 bound is needed.

## 3. Exact one-corner form of F_delta

Let

    q=sqrt(delta),
    z=i q,

and

    F_delta(x)
      =
      (delta+1) P(x)^2/(P(x)^2+delta).

For real x,

    Im [1/(P(x)-i q)]
      =
      q/(P(x)^2+delta).

Therefore

    boxed:

    F_delta(x)
      =
      (delta+1)
      [
        1
        -
        q Im (P(x)-i q)^(-1)
      ].

Using the corner identity,

    boxed:

    tau F_delta(H)
      =
      (delta+1)
      [
        1
        +
        q Im tau(
          [mathcal L_(iq)(H)^(-1)]_33
        )
      ].

Thus the six simple H-plane poles of P(x)^2+delta are not required as six
separate theorem states.  Their conjugate information is encoded in one
corner of one symmetric 3-layer inverse.

For the moment-certified bound

    w0=1415/13891,

the theorem target is exactly

    boxed:

    -q Im tau(
      [mathcal L_(iq)(H)^(-1)]_33
    )
      >=
      1-w0/delta
      +o(1).

At delta=61,

    1-w0/61
      =
      845936/847351
      =
      0.9983300898919....

This is equivalent to

    limsup tau F_61(H)
      <=
      87730/847351,

and therefore to the 79.29311466... percent simple-zero rung.

## 4. Linear prime-block dependence

The pencil is affine in H.  Define the fixed internal matrix

    K =
      [ r   0   0 ]
      [ 0   0   1 ]
      [ 0   1   c ].

Then

    mathcal L_z(H)
      =
      K tensor H
      +
      A_z tensor I

for a fixed 3 by 3 matrix A_z.

Consequently a prime block update

    H -> H+B_p

becomes simply

    mathcal L -> mathcal L + K tensor B_p.

Hence

    ||K tensor B_p||op
      <=
      ||K||op ||B_p||op,

and the source-closed infinitesimal-block ledger immediately gives

    sum_p ||K tensor B_p||op^3
      =
      o(1).

The usual second-order Lindeberg expansion is therefore still legal, but now
there is only one 3-layer inverse state rather than six unrelated H-plane
resolvents.

## 5. LRSC displacement channel has rank at most six

Let

    mathcal D=I_3 tensor D.

Since A_z commutes with mathcal D,

    [mathcal D,mathcal L_z(H)]
      =
      K tensor [D,H].

The sharp Loewner state has

    rank[D,H]<=2.

Because K has rank three,

    boxed:
    rank[
      mathcal D,
      mathcal L_z(H)
    ]
      <=6.

For

    mathcal R_z=mathcal L_z(H)^(-1),

    [mathcal D,mathcal R_z]
      =
      -mathcal R_z
       [mathcal D,mathcal L_z]
       mathcal R_z,

so

    boxed:
    rank[
      mathcal D,
      mathcal R_z
    ]
      <=6.

This is the direct LRSC-style channel reduction: the internal dimension rises
from one to three, but the spatial theorem state remains finite-rank in the
displacement direction.

## 6. Goal-oriented Gaussian bridge lifts exactly

For the artificial Gaussian bridge

    H_t=s0 I+tP_full+sqrt(v(t)) W,
    v=t(1-t),

set

    mathcal R_t
      =
      mathcal L_z(H_t)^(-1),

and use the goal functional

    ell(X)=tau_d(X_33).

Let

    mathcal P=K tensor P_full,

    mathcal W=K tensor W,

and let mathcal V be the covariance map built from the lifted directions

    mathcal E_j=K tensor E_j.

The same finite-d Gaussian integration-by-parts calculation gives

    F(t)=E ell(mathcal R_t),

    C(t)=E sum_j
      ell(
        mathcal R_t mathcal E_j
        mathcal R_t mathcal E_j
        mathcal R_t
      ).

If

    mathcal B_z
      =
      mathcal L_z(s0 I),

then exactly

    t D(t)-2v(t)C(t)
      =
      F(t)
      -
      E ell(
        mathcal R_t mathcal B_z mathcal R_t
      ),

where D is the deterministic-prime drift term.  Substitution into the bridge
derivative eliminates D and yields

    boxed:

    F_t
      +
      [
        F
        -
        E ell(
          mathcal R_t mathcal B_z mathcal R_t
        )
      ]/t
      +
      C
      =
      0.

No explicit deterministic prime sum remains.

The extra background term is only a fixed 3 by 3 internal directional
derivative:

    D_(mathcal B_z) F
      =
      -
      E ell(
        mathcal R_t mathcal B_z mathcal R_t
      ).

Thus the goal-oriented state is finite in the internal variable.  It is not a
full d by d adjoint problem.

This is the direct methodological transfer from the Navier--Stokes WP19
goal-oriented-adjoint lesson: dualize the one scalar observable that is
actually consumed instead of proving a worst-case full-state estimate.

## 7. What this removes

This formulation removes, simultaneously:

- finite-T raw sixth moments;
- the six separate H-plane pole bookkeeping;
- the large residue-sum conditioning of the partial-fraction representation;
- any need to identify a full limiting spectral law before attacking >79;
- any generic d^2 covariance state.

It retains:

- one symmetric 3-layer inverse;
- one (3,3) corner trace;
- displacement rank at most six;
- the existing prime-square covariance and Gaussian bridge;
- a fixed finite internal background derivative.

## 8. Exact remaining theorem gate

The next theorem-grade task is now:

1. lift the already-closed resonant prime-square covariance substitution to
   the fixed 3-layer directions K tensor B_p;
2. lift the carrier-2T fast-channel o(1) bound to the same finite internal
   state;
3. reduce C(t) and the internal background derivative to the rank-six
   displacement generators and diagonal block traces;
4. prove the single one-sided endpoint inequality

       -sqrt(delta) Im tau(
         [mathcal L_(i sqrt(delta))(H)^(-1)]_33
       )
       >=
       1-w0/delta
       +o(1).

For delta=61 this is already an unconditional >79 target if the four items
above close.  For every fixed delta the same architecture applies, and the
fixed-delta theorem ladder can approach 11061/13891 only after each fixed
rung is proved.

## Claim firewall

This is an exact theorem reduction, not the theorem itself.  No >79 percent
claim is promoted until the remaining finite-channel expectation inequality is
proved.

Cross-project inputs used only as mechanisms, not imported conclusions:

- LRSC: finite channel/rank factorization;
- Navier--Stokes WP19: goal-oriented observable/adjoint principle;
- WP84: bounded rank robustness, Gaussian bridge, covariance closure, and
  fail-closed evidence boundaries.
