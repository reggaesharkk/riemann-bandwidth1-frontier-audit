# WP84 — reconciliation of the external hostile audits

Date: 2026-10-06

Status: **INDEPENDENT REPO-LEVEL AUDIT; CONSTANT 72 SURVIVES, TRANSPOSE CONVENTION SURVIVES, DIRECT POSITIVE ROUTE PROMOTED**

No unconditional zero-density percentage is claimed here.

Two external hostile audits were run against the handoff pack.

One audit challenged the direct repeated-pole constant 72 and proposed 96.
The other audit did not find a broken line, but marked the result conditional
because the handoff pack did not include the exact sharp-matrix definitions.

The private repository does include those definitions.

This note resolves the disagreement from the full branch state.

## 1. Sharp state used by the theorem

The sharp retained prime matrix is

    H
      =
      M_beta + [M_alpha,J],

with

    J_ij = 1/[pi(j-i)],
    J_ii = 0,

and alpha,beta real.

Therefore H is real symmetric.

For the displacement truncation,

    H=H_R+Delta,

where H_R keeps 0<|i-j|<=R and

    Delta_ij
      =
      (alpha_i-alpha_j)/[pi(j-i)]

for |i-j|>R, with zero diagonal.

The exact normalized tail estimates already on the branch are

    tau(Delta^2)
      <=
      8 q_alpha/(pi^2 R),

and

    ||[D,H_R]||_F^2/d
      <=
      8 R q_alpha/pi^2,

where

    q_alpha=||alpha||_2^2/d.

These are the missing hypotheses in the abbreviated external pack.

## 2. Re-audit of the differentiated resolvent identity

Write

    G=(H-zI)^(-1),
    S=(H_R-zI)^(-1),

with |Im z|>=eta.

The second resolvent identity is

    G-S
      =
      -S Delta S
      +S Delta S Delta G.

Differentiating gives exactly

    m_H'-m_R'

      =
      -2 tau(Delta S^3)

      +tau(S^2 Delta S Delta G)

      +tau(S Delta S^2 Delta G)

      +tau(S Delta S Delta G^2).

There are therefore:

- one linear-tail term with coefficient 2;
- three quadratic-tail terms.

## 3. Linear term constant

For i!=j,

    Delta_ij
      =
      (alpha_i-alpha_j)/[pi(j-i)],

and

    (S^3)_ji
      =
      [D,S^3]_ji/(j-i).

Hence

    |tau(Delta S^3)|

      <=
      1/(pi d)
      [
        sum_tail
          |alpha_i-alpha_j|^2/(i-j)^2
      ]^(1/2)

      [
        sum_tail
          |[D,S^3]_ji|^2/(i-j)^2
      ]^(1/2).

On the tail,

    1/|i-j|<=1/R.

Also

    [D,S]
      =
      -S[D,H_R]S,

so

    [D,S^3]
      =
      [D,S]S^2
      +S[D,S]S
      +S^2[D,S],

and therefore

    ||[D,S^3]||_F
      <=
      3 eta^(-4)
      ||[D,H_R]||_F.

Insert the two exact normalized Frobenius estimates:

    boxed:

    |tau(Delta S^3)|
      <=
      24 q_alpha/
      (pi^2 eta^4 R).

The differentiated linear contribution is therefore

    boxed:

    48 q_alpha/
    (pi^2 eta^4 R).

No additional asymmetric leakage term appears.

## 4. Quadratic terms

For any of the three quadratic differentiated terms, for example

    tau(S^2 Delta S Delta G),

cyclicity plus Hilbert--Schmidt Cauchy--Schwarz gives

    |tau(S^2 Delta S Delta G)|

      <=
      eta^(-4)
      tau(Delta^2).

The same estimate holds for the other two terms.

Therefore the three quadratic terms contribute at most

    3 eta^(-4) tau(Delta^2)

      <=
      24 q_alpha/
      (pi^2 eta^4 R).

## 5. Final constant

Adding Sections 3--4 gives

    boxed:

    |m_H'-m_R'|

      <=
      72 q_alpha/
      (pi^2 eta^4 R).

With q_alpha=1/4+o(1),

    boxed:

    |m_H'-m_R'|

      <=
      18/
      (pi^2 eta^4 R)

      +o(R^-1).

Thus the external proposed repair

    72 -> 96

is not required by the actual sharp-matrix argument.

The exact bookkeeping is simply

    72
      =
      2*24
      +3*8.

The branch keeps 72.

## 6. Numerical stress check

The existing regression gate

    src/wp84_direct_mprime_tail_o1_over_r_gate.py

already tests the 72 bound on random finite sharp-Loewner matrices.

A further hostile local stress test over

    d in {41,81,121,181},
    R in {2,4,8,16,32},
    eta in {0.7,1,1.26,1.6,2}

found worst observed

    actual / 72-bound
      <0.10.

This is only a regression check, not part of the proof.

## 7. Transpose versus adjoint

The external audit also warned that the heat curvature may require adjoints
instead of transposes.

For the actual sharp state this warning does not invalidate the current
formula.

Every subset sharp matrix is real symmetric:

    H^T=H.

The Gaussian bridge direction is also real symmetric because

    W
      =
      M_h+[M_a,J],

with a,h real and J real skew-symmetric; hence

    [M_a,J]^T=[M_a,J].

Therefore along the real-symmetric Gaussian bridge,

    H_u^T=H_u,

and for every nonreal z,

    R_u(z)^T=R_u(z).

The analytic D2 primitive is bilinear,

    tau((B R)^2),

not a Hilbert--Schmidt energy

    tau((BR)^*(BR)).

So the correct analytic contraction uses transpose symmetry, not an adjoint
replacement.

There is no missing O(1) phase leakage from this source.

## 8. The one-half derivative identity does not even need symmetry

For one fixed direction B define

    Xi_B(z)
      =
      tau(BRBR).

Then

    d/dz Xi_B

      =
      tau(BR^2BR)
      +tau(BRBR^2).

By cyclicity,

    tau(BR^2BR)
      =
      tau(R^2BRB),

and

    tau(BRBR^2)
      =
      tau(R^2BRB).

Hence

    boxed:

    (1/2) Xi_B'(z)
      =
      tau(RBRBR).

So the factor 1/2 in the D2 / heat-curvature derivative relation follows
from trace cyclicity alone.

The real-symmetric condition is needed for the explicit scalar reduction of
the resonant covariance, not for this one-half identity.

## 9. Arithmetic inconsistency in the 96 audit

Even if one temporarily used the proposed larger constant

    C=5.253018

at R=400, the direct fixed-band ceiling would be

    E_rec-C/R

      =
      0.150117436...,

not

      0.1356025.

Thus the external 96 audit mixed the residual model margin with the absolute
fixed-band ceiling in its final boxed inequality.

This does not affect the branch because the 96 repair itself is not needed.

## 10. Strategic verdict

After the hostile audits:

PASS:

- support-free sine-square inequality;
- one-point scalar formula;
- rank-four commutator;
- O(R^-1) m comparison;
- O(R^-1) m' comparison with constant 72;
- S4 kernel for heat T_ab after two commutators;
- S2 kernel for direct positive Q^2 energy;
- partial_z T12=T22+2T13;
- transpose convention on the actual real-symmetric sharp/Gaussian state.

OPEN:

- the final one-sided large-T transport of the positive rank-four energy.

The external audits therefore strengthen the case for prioritizing the
direct positive-energy route, but they do not produce the record theorem.

See:

    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
    notes/WP84_DIRECT_MPRIME_TAIL_O1_OVER_R.md
    notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md
    notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md
