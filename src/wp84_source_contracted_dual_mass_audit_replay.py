"""Independent replay of source-completeness and contour-weight checks."""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes/WP84_SOURCE_CONTRACTED_DUAL_MASS_AUDIT_CERTIFICATE.json"


def validate(c):
    assert c["schema"] == "wp84-source-contracted-dual-mass-audit-v1"
    assert c["decision"] == "E"
    assert c["frozen"]["K"] == 32
    assert c["frozen"]["delta"] == "1/100000"
    assert c["frozen"]["cutoff"] == "N=floor(X*exp(-sqrt(log X)))"
    assert c["frozen"]["strict_gt79"] == "OPEN"
    assert c["source_object_inventory"]["section_kernel"]["status"] == "FORMULA_EXECUTABLE_GIVEN_I"
    assert c["source_object_inventory"]["Gamma_source_tensors"]["status"] == "SYMBOLIC_PLACEHOLDER"
    assert c["source_object_inventory"]["K1_K2"]["status"] == "FORMAL_DEFINITIONS_ONLY"
    assert c["source_object_inventory"]["proper_power_vectors"]["status"] == "GROUPED_SYMBOLIC_WITH_NORM_ENVELOPE"
    assert c["source_object_inventory"]["response_coefficients"]["status"] == "BOUNDED_BUT_NOT_INSTANTIATED"
    assert c["source_object_inventory"]["selected_section"]["status"] == "NOT_INSTANTIATED_FOR_DUAL_MASS"
    assert c["source_object_inventory"]["source_mask_callback"]["status"] == "EXTERNAL_IN_SEPARATE_FULL_POOL_ATOM_ITERATOR"
    assert "not silently identified" in c["source_object_inventory"]["source_mask_callback"]["scope_warning"]
    assert len(c["source_object_inventory"]["Gamma_source_tensors"]["exact_missing"]) == 4
    assert "D1_T=o(1)" in c["mathematical_results_rechecked"]["conditional_dual_estimates"]["A1"]
    assert "D2_T=o(L^4)" in c["mathematical_results_rechecked"]["conditional_dual_estimates"]["A2"]
    assert c["falsification_matrix"]["exact_m0"].startswith("CLOSED")
    assert "POSSIBLE" in c["falsification_matrix"]["nonzero_periodic_alias"]
    assert "UNKNOWN" in c["falsification_matrix"]["near_alias"]
    assert "UNKNOWN" in c["falsification_matrix"]["row_dependent_masks"]
    assert c["falsification_matrix"]["generic_reciprocal_weight_test"]["status"] == "CRUDE_MAJORANT_FAILS_UNIFORMLY_FOR_THIS_SCHEDULE"
    assert "does not show the actual K-weighted" in c["falsification_matrix"]["generic_reciprocal_weight_test"]["proof"]
    assert "monotone convergence" in c["falsification_matrix"]["infinite_limit_order"]
    assert "no uniform-in-T dual bound" in c["falsification_matrix"]["infinite_limit_order"]
    assert c["countermodel_boundary"]["source_legal_counterexample"] == "NONE ESTABLISHED"
    assert c["countermodel_boundary"]["uniform_from_documented_constraints"].startswith("UNKNOWN")
    assert c["strict_gt79"] == "OPEN"
    assert len(c["source_sha256"]) == 15
    return True


def replay_source_facts(c):
    src = c["source_sha256"]
    paths = list(src)
    texts = {p: (ROOT / p).read_text(encoding="utf-8") for p in paths}
    mix = texts["src/wp84_contour_mixture_prime_mass.py"]
    firewall = texts["src/wp84_dependent_phase_prime_adic_firewall.py"]
    localize = texts["notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md"]
    amplitude = texts["src/wp84_fifth_full_pool_amplitude.py"]
    assert '"exact_grouped_kernel_definition": "For each p,nu, K1_' in mix
    assert '"exact_grouped_kernel_definition": "For each p,nu, K2_' in mix
    assert "def contract_k1" not in mix and "def contract_k2" not in mix
    assert "K_I(omega)=d'" in firewall and "sum_{k in I}" in firewall
    assert "V_p(K)=c_p e^{iT\\log p}" in localize
    assert "source_mask(fid,slots,lag,T,section,m)" in amplitude
    assert "def source_mask(" not in amplitude
    assert "gamma contains c_{p^a}" in firewall
    assert '"m_zero": "impossible for r!=0 by unique factorization"' in firewall
    return len(texts)


def replay_reciprocal_weight_failure(c):
    d = c["falsification_matrix"]["generic_reciprocal_weight_test"]
    # Feasible uniform log radii have aggregate perturbation <= theta*a.
    assert F(128) * F(131, 51200) == F(131, 400)
    # On the explicit all-prime schedule rho_q<=1 eventually, so the n=0,+/-1
    # terms in each one-dimensional reciprocal-weight sum imply this factor.
    factor = 1 + 2 / math.cosh(2)
    assert factor > 1
    assert "(1+2/cosh(2))^s" in d["proof"]
    assert "|K|<=1 alone" in d["proof"]
    assert "optimized_arbitrary_measure" in d
    return factor


def hostile_mutations(c):
    mutations = [
        lambda x: x.update(decision="A"),
        lambda x: x["source_object_inventory"]["K1_K2"].update(status="EXECUTABLE"),
        lambda x: x["source_object_inventory"]["Gamma_source_tensors"].update(status="EXECUTED_ARRAYS"),
        lambda x: x["source_object_inventory"]["selected_section"].update(status="INSTANTIATED"),
        lambda x: x["source_object_inventory"]["proper_power_vectors"].update(status="FIRST_POWER_ONLY"),
        lambda x: x["falsification_matrix"].update(exact_m0="possible"),
        lambda x: x["falsification_matrix"].update(nonzero_periodic_alias="actual coefficient proved nonzero"),
        lambda x: x["falsification_matrix"].update(row_dependent_masks="CLOSED cancellation"),
        lambda x: x["mathematical_results_rechecked"]["conditional_dual_estimates"].update(A1="D1 closed"),
        lambda x: x["falsification_matrix"]["generic_reciprocal_weight_test"].update(status="UNIFORMLY SUMMABLE"),
        lambda x: x["countermodel_boundary"].update(source_legal_counterexample="YES"),
        lambda x: x.update(strict_gt79="PROVED"),
        lambda x: x["falsification_matrix"].update(infinite_limit_order="Uniform in T bound exists"),
        lambda x: x["source_object_inventory"]["source_mask_callback"].update(scope_warning="is the Lindeberg mask"),
        lambda x: x["source_object_inventory"]["Gamma_source_tensors"]["exact_missing"].pop(),
    ]
    for i, mutate in enumerate(mutations, 1):
        bad = deepcopy(c)
        mutate(bad)
        try:
            validate(bad)
        except (AssertionError, KeyError, TypeError, AttributeError):
            continue
        raise AssertionError(f"hostile mutation {i} was not detected")
    return len(mutations)


def verify_hashes(c):
    for rel, expected in c["source_sha256"].items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        assert actual == expected, rel
    return len(c["source_sha256"])


def main():
    c = json.loads(CERT.read_text(encoding="utf-8"))
    validate(c)
    nsrc = replay_source_facts(c)
    factor = replay_reciprocal_weight_failure(c)
    nmut = hostile_mutations(c)
    nhash = verify_hashes(c)
    print(f"PASS: inspected {nsrc} source files; reciprocal-weight factor {factor:.8f}>1; {nmut} hostile mutations rejected; {nhash} hashes verified.")
    print("UNKNOWN: actual source-contracted D1/D2, aggregate aliases, and uniformity over actual row masks/sections.")
    print("Decision E: source tensors and selected-section inputs are not instantiated; strict >79 remains OPEN.")


if __name__ == "__main__":
    main()
