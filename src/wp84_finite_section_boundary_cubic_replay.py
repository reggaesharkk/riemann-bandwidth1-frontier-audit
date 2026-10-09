#!/usr/bin/env python3
"""Independent exact replay of WP84 finite-section cubic boundary algebra.

This intentionally does not import the certificate producer.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_FINITE_SECTION_BOUNDARY_CUBIC_CERTIFICATE.json"


def independently_build_source_form():
    inds = tuple(range(-3, 5))
    p_labels = (0, 1, 2)
    alpha = sp.Rational(1, 3)
    phase = -sp.Rational(1, 2)+sp.I*sp.sqrt(3)/2
    amplitude = 2+sp.I
    scalar = sp.Rational(3, 5)
    fields = {}
    for k in inds:
        w = amplitude*phase**(k % 3)
        # Exact real/imag extraction for this root-of-unity phase.
        fields[k] = (sp.simplify(sp.im(w)),
                     sp.simplify(2*(1-alpha)*sp.re(w)))

    # Build from the defining commutator, independently of the producer's
    # closed entry formula.
    J = sp.zeros(len(inds), len(inds))
    M = sp.zeros(len(inds), len(inds))
    for r, i in enumerate(inds):
        M[r, r] = fields[i][0]
        for c, j in enumerate(inds):
            if i != j:
                J[r, c] = 1/(sp.pi*(j-i))
        M[r, r] = fields[i][0]
    beta = sp.diag(*[fields[i][1] for i in inds])
    V = beta + M*J-J*M
    H = V+scalar*sp.eye(len(inds))
    p = [inds.index(i) for i in p_labels]
    q = [j for j in range(len(inds)) if j not in p]
    cut = lambda A, rows, cols: A.extract(rows, cols)
    a, b, c, d = (cut(H,p,p),cut(H,p,q),cut(H,q,p),cut(H,q,q))
    lhs = sp.trace(cut(H**3,p,p))-sp.trace(a**3)
    rhs = 2*sp.trace(a*b*c)+sp.trace(b*d*c)
    assert sp.simplify(lhs-rhs)==0
    assert sp.simplify(H-H.conjugate().T)==sp.zeros(len(inds),len(inds))
    assert sp.simplify(c-b.conjugate().T)==sp.zeros(len(q),len(p))

    vp, vb, vc, vq = (cut(V,p,p),cut(V,p,q),cut(V,q,p),cut(V,q,q))
    full_delta = sp.trace(cut(H**3,p,p))-sp.trace(a**3)
    residual = 2*sp.trace(vp*vb*vc)+sp.trace(vb*vq*vc)
    scalar_delta = full_delta-residual
    expected_scalar = 3*scalar*sp.trace(vb*vc)
    assert sp.simplify(scalar_delta-expected_scalar)==0

    # Mutations: the scalar term cannot be omitted when s!=0; the wrong
    # commutator sign does not reconstruct the original source matrix.
    assert sp.simplify(expected_scalar)!=0
    wrong = beta-(M*J-J*M)+scalar*sp.eye(len(inds))
    assert sp.simplify(wrong-H)!=sp.zeros(len(inds),len(inds))
    return str(sp.simplify(full_delta)), str(sp.simplify(expected_scalar)), str(sp.simplify(residual))


def crossing_count_replay():
    # Independent direct enumeration on a shifted contiguous section.
    for lo, d in ((-4,1),(-2,3),(7,9)):
        P = set(range(lo,lo+d))
        for r in range(1,4*d+1):
            observed = 0
            for i in P:
                for j in range(lo-5*d,lo+6*d+1):
                    if j not in P and abs(j-i)==r:
                        observed += 1
            assert observed==2*min(r,d)
    # Exact harmonic envelope: sum min(r,d)/r^2 <= H_d+1 for sampled d.
    for d in range(1,40):
        partial=sum(sp.Rational(min(r,d),r*r) for r in range(1,15*d+1))
        bound=sum(sp.Rational(1,r) for r in range(1,d+1))+1
        assert partial<=bound


def hostile_mutations():
    doc=json.loads(CERT.read_text(encoding="utf-8"))
    assert doc["source"]["prime_powers"]=="all n=p^v<=N"
    assert "3*s0*||PVQ||_HS^2" in doc["block_identity"]["scalar_background_exact"]
    assert "signed V-cubic boundary transfer remains open" in doc["decision"]
    # Alias/sample rules are not weakened into a model result.
    assert "all prime powers" in doc["remaining_terms"]["first_unresolved_sum"]
    assert "strict >79" in doc["claim_boundary"]
    # Omitting s0 or flipping the source commutator is rejected by the exact
    # tests in independently_build_source_form above.
    return True


def main():
    full, scalar, remainder=independently_build_source_form()
    crossing_count_replay()
    hostile_mutations()
    print("PASS independent exact source-form Hermitian matrix regression")
    print("PASS block identity and scalar-background separation; finite delta =",full)
    print("PASS scalar term =",scalar)
    print("PASS signed cubic remainder =",remainder)
    print("PASS shifted boundary-crossing counts and harmonic envelope")
    print("PASS hostile omissions/sign mutation and claim-boundary checks")
    print("REPLAY VERDICT: scalar-background sector closes by the natural-cutoff majorant; signed V-cubic remains open")


if __name__=="__main__": main()
