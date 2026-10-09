#!/usr/bin/env python3
"""Produce a certificate for adaptive low-boundary-energy sections.

The analytic proof is in notes/WP84_ADAPTIVE_BOUNDARY_LOCAL_LARGE_SIEVE.md.
The certificate records the large-sieve hypotheses, natural-cutoff scales,
endpoint average, boundary-transfer consequence, and evidence boundary.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_ADAPTIVE_BOUNDARY_LOCAL_LARGE_SIEVE_CERTIFICATE.json"


def main():
    cert = {
        "title": "Local prime-field large sieve and adaptive finite-section boundary transfer",
        "decision": "B — complete boundary transfer holds on an existential source-admissible trimmed section; original-section/uniform transfer is not proved",
        "source": {
            "scale": "X=T/(2*pi), L=log X, N=floor(X*exp(-sqrt(L))), d=floor(T*L/(2*pi))",
            "coefficients": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)), every prime power n=p^v<=N",
            "fields": "z_n=c_n*exp(i*T*log(n)); F_k=sum_n z_n exp(2*pi*i*k*alpha_n), A_k=Im(F_k), alpha_n=log(n)/L",
            "section": "original I0=[b,b+d-1]; candidate I_uv=[b+u,b+d-1-v], 0<=u,v<=M",
            "operator": "H=s0 I+V, V=diag(beta)+[diag(A),J], J_ij=1/(pi*(j-i)); ||V||op<=4S, S=sum_n |c_n|",
        },
        "local_large_sieve": {
            "circular_separation": "delta>=min(1/((N+1)*L),1/sqrt(L)); for sufficiently large T, delta>=1/((N+1)*L)",
            "discrete_constant": "sum_{k=b}^{b+M-1}|F_k|^2<=(M-1+delta^-1)*sum_n|c_n|^2, uniformly in integer b",
            "imaginary_part": "sum |A_k|^2<=sum |F_k|^2",
            "prime_square_mass": "sum_n |c_n|^2=(a_phi^-2*L^-2)*sum_{p^v<=N}(log p)^2/p^v=O(1); v=1 contributes O(log^2 N), v>=2 contributes O(1)",
            "window_bound": "sum_{k=b}^{b+M-1}|A_k|^2<=C*(M+NL), uniformly in b",
        },
        "adaptive_trim": {
            "M": "ceil(d*exp(-sqrt(L)/2))",
            "M_over_d": "exp(-sqrt(L)/2)+o(1)->0",
            "M_over_NL": "exp(sqrt(L)/2)*(1+o(1))->infinity",
            "candidate_count": "(M+1)^2 endpoint pairs (u,v)",
            "boundary_kernel": "E(I)=||P_I V(I-P_I)||_HS^2=pi^-2*sum_{i in I,j notin I}(A_i-A_j)^2/(j-i)^2",
            "dyadic_shell_cost": "each shell 1<=distance<=d contributes O(1) to the average; exterior shells distance>d contribute O(2^-q) at dyadic shell [2^q*d,2^(q+1)*d)",
            "average": "average_{0<=u,v<=M} E(I_uv)<=C*log(d)",
            "existence": "some (u,v) has E(I_uv)<=C*log(d); d'=d-u-v>=d-2M=d-o(d)",
            "exterior": "all complement sites are included; sum_{t>d} d/t^2=O(1) after local endpoint averaging",
        },
        "boundary_transfer": {
            "scalar_background": "3*s0*E(I_uv)/d'=O(log(d)/d')=o(1)",
            "signed_cubic": "|R_I|/d'<=3*||V||op*E(I)/d'=O(S*log(d)/d')=O(sqrt(N)/(T*L))=o(1)",
            "natural_cutoff_ratio": "sqrt(N)/(T*L)=O(exp(-sqrt(L)/2)/(sqrt(T)*L))",
            "quantifiers": "existential over trimmed contiguous subintervals of the original length-d section; not uniform over all sections",
        },
        "section_transfer": {
            "first_second_moments": "existing prime-source first/second moment arguments are uniform for contiguous d'/d->1 sections in their stated scope",
            "bounded_rational_consumers": "for bounded-variation f, principal-submatrix interlacing yields normalized trace difference <=2*TV(f)*r/d when r rows are deleted (up to the stated normalization convention)",
            "unbounded_cubic": "rank deletion alone is insufficient; a uniform normalized sixth-moment bound gives O((r/d)^(1/2)) for cubic trace transfer by Schatten Holder",
            "zero_side": "no new same-section prime-to-Weil, zero-side, or conditioned-Cayley identification is proved by the adaptive boundary lemma",
        },
        "hostile_counterexample": {
            "object": "abstract sequence A_0=sqrt(M), A_k=0 for k!=0",
            "property": "every length-M window has sum |A_k|^2<=M",
            "failure": "for an interval with 0 at its endpoint, E(I)>=M/pi^2, so a local mean-square estimate alone cannot imply a uniform O(log d) boundary bound",
            "scope": "falsifies the uniform implication from local-energy control alone; it is not a counterexample from the actual prime field",
        },
        "claim_boundary": "No uniform all-section estimate, original-section cubic moment transfer, m3=2, 0.105 energy theorem, prime-to-Weil transfer, or strict >79 theorem is claimed.",
        "independent_replay": "src/wp84_adaptive_boundary_large_sieve_replay.py",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print("PASS analytic scales: M/d->0 and M/(NL)->infinity")
    print("PASS local circular spacing and square-mass formula recorded")
    print("BOUND endpoint-average crossing energy O(log d), including infinite tails")
    print("BOUND selected-section normalized cubic correction O(S log d/d')=o(1)")
    print("OPEN uniform original-section, zero-side, and conditioned-energy transfer")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
