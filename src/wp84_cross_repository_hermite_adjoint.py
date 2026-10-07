#!/usr/bin/env python3
"""Exact Hermite dual/Lyapunov/boundary-flux replay; NOT a consumer certificate.

Independent polynomial Gaussian projection is compared with coefficient
evolution. Unnormalized probabilists' Hermites use Gram diag(alpha!), so
all witnesses and final values are rational. SymPy performs symbolic algebra;
no sampled integral or numerical ODE solver is used.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import sympy as s

u, v = s.symbols("u v", positive=True)
g = s.symbols("g0:2", real=True)
DELTA, U = s.Rational(1, 2), s.Rational(2)
EINF = s.Rational(7761139416076220170204368647089,
                  1680256283972002400160000000000)
CUSHION = s.Rational(8711, 2778200)
# A nonorthogonal, positive Hilbert channel Gram; retain signed cross terms.
HGRAM = s.Matrix([[2, -1, 1], [-1, 2, 0], [1, 0, 2]])


def zero(expr, label):
    if s.simplify(s.expand(expr)) != 0:
        raise ValueError(f"FAIL {label}: {expr}")


def matrix_zero(matrix, label):
    for entry in matrix:
        zero(entry, label)


def basis(K):
    out = sorted((a for a in itertools.product(range(K + 1), repeat=2)
                  if sum(a) <= K), key=lambda a: (sum(a), a))
    if len(out) != math.comb(K + 2, 2):
        raise ValueError("Incomplete Hermite multi-index domain")
    return out


def hermite(a):
    return s.prod(s.hermite_prob(n, x) for n, x in zip(a, g))


def gaussian_average(poly):
    out = 0
    for powers, coefficient in s.Poly(s.expand(poly), *g).terms():
        moment = 1
        for n in powers:
            if n % 2:
                moment = 0
                break
            moment *= math.factorial(n) // (2 ** (n // 2) * math.factorial(n // 2))
        out += coefficient * moment
    return s.simplify(out)


def project(polys, indices):
    return s.Matrix([[s.simplify(gaussian_average(p * hermite(a)) /
                                math.prod(math.factorial(n) for n in a))
                      for p in polys] for a in indices])


def chain(indices):
    lookup = {a: j for j, a in enumerate(indices)}
    n = len(indices)
    L = s.zeros(n)
    for j, beta in enumerate(indices):
        for coord in range(2):
            if beta[coord] < 2:
                continue
            alpha = list(beta)
            alpha[coord] -= 2
            alpha = tuple(alpha)
            if alpha in lookup:
                L[lookup[alpha], j] += beta[coord] * (beta[coord] - 1)
    M = s.diag(*(math.prod(math.factorial(n) for n in a) for a in indices))
    N = s.diag(*(sum(a) for a in indices))
    A0 = (N + L) / 2
    Cform = (M * L + L.T * M) / 2
    Sform = M * N + Cform
    matrix_zero(A0.T * M + M * A0 - Sform, "energy normalization")
    return M, N, L, A0, Cform, Sform


def propagator(indices, end, start):
    # Independent scaling of the actual Hermite POLYNOMIALS, not exp(A0 log).
    polys = [hermite(a).subs({x: s.sqrt(end / start) * x for x in g},
                             simultaneous=True) for a in indices]
    return project(polys, indices)


def contract(left, form, right):
    return s.simplify(s.trace(left.T * form * right * HGRAM))


def integral(expr, lo=DELTA, hi=U):
    return s.simplify(s.integrate(s.expand(expr), (u, lo, hi)))


def expect_rejection(action, label):
    try:
        action()
    except ValueError:
        return label
    raise ValueError(f"Mutation accepted: {label}")


def consumer_gate():
    # Algebra replay supplies NONE of the uniform actual-prime inequalities.
    raise ValueError("Missing actual-state signed dual-flux lemma (13)")


def replay(K, full_indices, full, full_L, polys):
    indices = basis(K)
    row_map = [full_indices.index(a) for a in indices]
    tail_rows = [j for j in range(len(full_indices)) if j not in row_map]
    x = full[row_map, :]
    tail = full[tail_rows, :]
    M, N, L, A0, Cform, Sform = chain(indices)
    A = A0 / u
    # Boundary built independently from the omitted coefficients.
    r = full_L.extract(row_map, tail_rows) * tail / (2 * u)
    matrix_zero(x.diff(u) - A * x - r, "projected actual evolution")
    for j, a in enumerate(indices):
        if any(r[j, c] != 0 for c in range(r.cols)) and sum(a) not in (K-1, K):
            raise ValueError("Nonlocal boundary row")
    for b in (full_indices[j] for j in tail_rows):
        if sum(b) > K + 2:
            col = full_indices.index(b)
            matrix_zero(full_L.extract(row_map, [col]), "two-level boundary support")

    phi = propagator(indices, U, u)
    phi_forward = propagator(indices, u, DELTA)
    matrix_zero(phi.diff(u) + phi * A, "backward propagator")
    matrix_zero(phi_forward.diff(u) - A * phi_forward, "forward propagator")
    matrix_zero(phi.subs(u, U) - s.eye(len(indices)), "terminal propagator")

    Yform = s.simplify(phi.T * M * phi)
    Xform = Yform - M
    matrix_zero(Xform.diff(u) + A.T * Xform + Xform * A + Sform/u,
                "total operator Lyapunov")
    matrix_zero(Xform.subs(u, U), "zero terminal Lyapunov")
    Xop = M.inv() * Xform
    Aadj = M.inv() * A.T * M
    matrix_zero(Xop.diff(u) + Aadj * Xop + Xop * A + M.inv()*Sform/u,
                "weighted Hilbert adjoint")

    early = gaussian_average((s.Matrix(polys).T * HGRAM * s.Matrix(polys))[0])
    early = s.simplify(early.subs(u, DELTA) - early.subs(u, 0))
    initial = contract(x, Xform, x).subs(u, DELTA)
    flux = 2 * integral(contract(x, Yform, r))
    Mt = s.diag(*(math.prod(math.factorial(n) for n in full_indices[j])
                  for j in tail_rows))
    tail_energy = contract(tail, Mt, tail) if tail_rows else s.Integer(0)
    tail_initial, tail_terminal = tail_energy.subs(u, DELTA), tail_energy.subs(u, U)
    direct_energy = gaussian_average((s.Matrix(polys).T * HGRAM * s.Matrix(polys))[0])
    direct_change = s.simplify(direct_energy.subs(u, U) - direct_energy.subs(u, 0))
    transported = s.simplify(early + initial + flux + tail_terminal - tail_initial)
    zero(direct_change - transported, "whole-chain signed boundary-flux identity")
    # Compare energy with an independent integral of the differentiated polynomial.
    zero(direct_change - integral(s.diff(direct_energy, u), 0, U), "direct integral")
    internal = integral(contract(x, Sform/u, x))
    zero(internal - initial - 2*integral(contract(x, Xform, r)), "quadratic dual identity")

    # CROSS-only operator solved by a finite-horizon integral, independently of Y.
    phi_v = propagator(indices, v, u)
    integrand = (phi_v.T * Cform * phi_v / v).applyfunc(s.simplify)
    Xcross = integrand.applyfunc(lambda z: s.simplify(s.integrate(z, (v, u, U))))
    matrix_zero(Xcross.diff(u) + A.T * Xcross + Xcross * A + Cform/u,
                "cross-only Lyapunov")
    matrix_zero(Xcross.subs(u, U), "cross terminal condition")
    h = phi_forward * x.subs(u, DELTA)
    e = x - h
    lam_form = 2 * Xcross * h
    matrix_zero(-lam_form.diff(u) - A.T * lam_form - 2*Cform*h/u,
                "linear goal adjoint forcing and sign")
    matrix_zero(lam_form.subs(u, U), "zero terminal linear adjoint")
    pair = s.simplify(s.trace(lam_form.T * e * HGRAM))
    signed = s.simplify(s.trace(lam_form.T * r * HGRAM))
    zero(s.diff(pair,u) + 2*contract(h,Cform/u,e) - signed, "joint signed derivative")
    goal_difference = integral(contract(x,Cform/u,x)-contract(h,Cform/u,h))
    dual_difference = pair.subs(u,DELTA) + integral(signed) + integral(contract(e,Cform/u,e))
    zero(goal_difference-dual_difference, "quadratic goal remainder and endpoint")

    rejections = []
    if K == 2:
        rejections.append(expect_rejection(
            lambda: matrix_zero(phi.diff(u)-phi*A, "wrong adjoint time sign"), "reverse sign"))
        rejections.append(expect_rejection(
            lambda: matrix_zero(x.diff(u)-A*x-r/2, "missing boundary factor two"), "boundary normalization"))
        rejections.append(expect_rejection(
            lambda: matrix_zero(Xop.diff(u)+A.T*Xop+Xop*A+M.inv()*Sform/u,
                                "Euclidean instead of Hilbert adjoint"), "weighted adjoint"))
        rejections.append(expect_rejection(
            lambda: matrix_zero((Xform+M).subs(u,U), "unpaid terminal endpoint"), "terminal endpoint"))
        rejections.append(expect_rejection(
            lambda: zero(direct_change-(early+initial+flux/2+tail_terminal-tail_initial),
                         "halved total signed flux"), "signed flux"))
        diagonal_metric = s.diag(*HGRAM.diagonal())
        rejections.append(expect_rejection(
            lambda: zero(direct_energy-gaussian_average(
                (s.Matrix(polys).T*diagonal_metric*s.Matrix(polys))[0]),
                         "discarded channel Gram cross terms"), "channel scalarization"))
        rejections.append(expect_rejection(consumer_gate, "algebra-to-theorem promotion"))
    lower = s.simplify(early + initial + flux - tail_initial)
    if direct_change < lower:
        raise ValueError("Positive tail endpoint has wrong lower-bound sign")
    return {"K": K, "retained_multi_indices": len(indices),
            "direct_total_integral": str(direct_change), "initial_layer": str(early),
            "initial_dual_form": str(s.simplify(initial)), "signed_dual_flux": str(flux),
            "tail_initial": str(tail_initial), "tail_terminal": str(tail_terminal),
            "certified_polynomial_lower_bound": str(lower),
            "cross_goal_difference": str(goal_difference),
            "quadratic_goal_remainder": str(integral(contract(e,Cform/u,e))),
            "rejected_mutations": rejections}


def constants():
    x, w = s.symbols("x w")
    c, a = s.Rational(3142,2415), s.Rational(131,200)
    z, delta = c+s.I*a, 2*s.I*a
    r6 = (c*c+a*a)**3
    P = 1-s.Rational(43428,13891)*x+s.Rational(37704,13891)*x*x-s.Rational(9660,13891)*x**3
    cayley_num = z*w-s.conjugate(z)
    qpoly = s.Poly(s.expand(s.sqrt(r6)/delta**3 *
        sum(s.Poly(P,x).nth(j)*cayley_num**j*(w-1)**(3-j) for j in range(4))),w)
    q = [qpoly.nth(j) for j in range(4)]
    # Rational upper enclosures via |q_j|², without floating square roots.
    def sqrt_upper(rational):
        rational = s.cancel(rational)
        if not rational.is_Rational or rational < 0:
            raise ValueError("Nonrational squared magnitude")
        scale = 10**12
        n, d = map(int, s.fraction(rational))
        k = math.isqrt(n*scale*scale//d)
        if k*k*d < n*scale*scale:
            k += 1
        upper = s.Rational(k,scale)
        if upper**2 < rational:
            raise ValueError("Inward radical enclosure")
        return upper
    mags = [sqrt_upper(s.expand_complex(q[j]*s.conjugate(q[j]))) for j in range(1,4)]
    K1 = 2/a*sum((j+1)*mags[j] for j in range(3))
    K2 = 4/a**2*sum((j+1)**2*mags[j] for j in range(3))
    if not (K1 < 10 and K2 < 74 and sqrt_upper(EINF) < s.Rational(43,20)):
        raise ValueError("Frozen consumer conditioning upper bounds changed")
    # Rank-zero spatial witness; m=8, t=1/5: C-D=(16/5)e > 3e.
    m,t = s.Integer(8),s.Rational(1,5)
    excess = 2*t*m
    if excess <= 3:
        raise ValueError("Rank-zero dimension obstruction lost")
    return {"E_inf": str(EINF), "target": str(EINF-s.Rational(21,200)),
            "model_cushion": str(CUSHION), "K1_rational_upper": str(K1),
            "K2_rational_upper": str(K2), "sqrt_Einf_upper": str(sqrt_upper(EINF)),
            "rank_zero_witness_C_minus_D_over_energy": str(excess)}


def spatial_and_flux_obstructions():
    # Statewise low rank is not preserved by coefficient averaging.
    D=s.diag(0,1,2,3)
    def loewner(a,diagonal):
        return s.Matrix(4,4,lambda i,j: diagonal[i] if i==j else
                        s.Rational(a[j]-a[i],i-j))
    z=s.Rational(3142,2415)+s.I*s.Rational(131,200)
    resolvents=[(loewner(a,d)-z*s.eye(4)).inv() for a,d in
                [([1,0,2,-1],[1,2,3,4]),([0,1,-1,3],[2,-1,1,0])]]
    comm=[D*R-R*D for R in resolvents]
    ranks=[C.rank() for C in comm]+[(comm[0]+comm[1]).rank()]
    if ranks != [2,2,4]:
        raise ValueError("Averaging displacement-rank obstruction changed")
    # K=0, F=1-u*g0²: x=1-u, r=-1, Y=1. This is a NEW boundary
    # pairing obstruction, not a repeated pointwise consumer sign test.
    flux=2*s.integrate(-(1-u),(u,s.Rational(1,4),s.Rational(1,2)))
    if flux != -s.Rational(5,16):
        raise ValueError("Signed boundary flux was made positive")
    return {"individual_resolvent_displacement_ranks":ranks[:2],
            "sum_displacement_rank":ranks[2],
            "scalar_polynomial_signed_boundary_flux":str(flux),
            "scope":"Generic algebra obstruction; not a counterexample to the actual prime-state inequality"}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    if not all(HGRAM[:j,:j].det() > 0 for j in range(1,4)):
        raise ValueError("Hilbert channel Gram is not positive definite")
    polys=[1+u*g[0]**2+u*u*g[0]**2*g[1]**2,
           -1+u*(g[1]**2-g[0]**2)+u*u*g[0]**4/3,
           2+u*g[0]*g[1]-u*u*g[1]**4/5]
    indices=basis(4)
    full=project(polys,indices)
    M,N,L,A0,_,_=chain(indices)
    reconstructed=[sum(full[j,c]*hermite(a) for j,a in enumerate(indices)) for c in range(3)]
    for p,h in zip(polys,reconstructed):
        zero(p-h,"independent Gaussian projection and reconstruction")
        zero(2*u*s.diff(p,u)-sum(x*s.diff(p,x) for x in g),"actual radial dilation")
    matrix_zero(2*u*full.diff(u)-(N+L)*full,"full coefficient radial equation")
    result={"schema":"wp84-cross-repository-hermite-adjoint-v1",
            "arithmetic":"exact rational symbolic polynomial replay",
            "starting_commit":"6ab4622cea3833e847e005eb30f0a2e1c7bf5cf1",
            "delta":str(DELTA),"U":str(U),"constants":constants(),
            "spatial_and_flux_obstructions":spatial_and_flux_obstructions(),
            "blocks":[replay(K,indices,full,L,polys) for K in (0,1,2,3)],
            "algebra_status":"PASS", "consumer_certified":False,
            "actual_prime_bound_available":False,
            "decision":"B: uniform actual-state signed dual-flux lemma remains OPEN"}
    output=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(output,encoding="utf-8")
    print(output,end="")


if __name__=="__main__":
    main()
