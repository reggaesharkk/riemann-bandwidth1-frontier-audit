# WP84 — Cayley-defect form of the preferred r2 gate

Date: 2026-10-05

Status: **EXACT FINITE-d IDENTITY; MODEL/CONSUMER GATE ONLY**

No unconditional zero-density percentage is claimed here.

For the preferred consumer

    r2(x)=1-[(x-1)^2/(x^2+1)]^2

define, for a real-symmetric sharp matrix H,

    U=(H+iI)(H-iI)^(-1),
    R=(H-iI)^(-1).

Then U is unitary, U=I+2iR, and functional calculus gives

    I-Im U=(H-I)^2(H^2+I)^(-1).

Put

    B=I-Im U.

The scalar multiplier (x-1)^2/(x^2+1) lies in [0,2], hence

    0<=B<=2I.

Most importantly,

    boxed:
    r2(H)=I-B^2,

so

    boxed:
    tau r2(H)=1-tau(B^2).

Thus the first record gate is an upper bound on one positive defect energy.

For the public comparison

    C_pub=0.67350003708785588766...,

the positive-index threshold is

    q_pub=(1+C_pub)/2
         =0.8367500185439279....

Therefore it is enough to prove

    boxed:
    limsup tau(B_T^2)
      < 0.163249981456072....

The exact pinned model value of r2 is

    q_model=0.8833827124943086...,

so the model defect energy is

    E_model=0.1166172875056914...,

leaving the same record margin

    0.0466326939503807....

There is also an exact Cayley-moment identity

    tau r2(H)
      =2 Im tau(U)-1/2+(1/2)Re tau(U^2),

equivalent to

    2 Re[(2+i)m(i)-m'(i)].

## Positive displacement formula

Let

    D=diag(0,1,...,d-1).

Because B is real symmetric,

    B_ij=[D,B]_ij/(i-j),
    i!=j,

and hence exactly

    boxed:
    tau(B^2)
      =
      d^(-1) sum_i B_ii^2
      +
      d^(-1) sum_{i!=j}
        [D,B]_ij^2/(i-j)^2.

Both displayed terms are nonnegative.

Since

    B=I-2 Re R,

we have

    B_ii=1-2 Re R_ii,
    [D,B]=-2 Re[D,R].

The exact Loewner resolvent generator is

    [D,R]
      =pi^(-1)(v u^T-u v^T),

where

    u=R1,
    v=R a,

and a=Im Q is the scalar subset/state field.

Therefore

    boxed:
    tau(B^2)
      =
      d^(-1) sum_i (1-2 Re R_ii)^2

      +4/(pi^2 d)
        sum_{i!=j}
          Re(v_i u_j-u_i v_j)^2
          /(i-j)^2.

This uses only

    diag R(i),
    R(i)1,
    R(i) Im Q,

and the existing K2 squared-Cauchy kernel.

For the additive Gaussian heat flow

    H_u=H_1+sqrt(u)W,

the transported consumer is simply

    Phi_r2(u)=1-E tau(B_u^2).

So the remaining first-strike theorem can be phrased entirely as a
one-sided bound on a positive low-displacement energy.

See:

    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md
    notes/WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.md
    notes/WP84_BR_RANK3_SCALAR_D1.md
