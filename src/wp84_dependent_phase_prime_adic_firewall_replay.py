"""Independent replay; intentionally does not import the certificate producer."""
from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL_CERTIFICATE.json"


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def log_enclosure(n, terms=260):
    """Independent exact atanh-series enclosure for log(n)."""
    x = Fraction(n - 1, n + 1)
    partial = Fraction(0)
    for j in range(terms):
        partial += 2 * x ** (2 * j + 1) / (2 * j + 1)
    tail = 2 * x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x * x))
    return partial, partial + tail


def replay_atom():
    # The nonzero p-adic insertion is 2^1; the response is 3^u/5^v.
    p, r, q, s, u, v, T = 2, 1, 3, 5, 253891, 173308, 7800
    l2, l3, l5 = (log_enclosure(n) for n in (2, 3, 5))
    lo = l2[0] + u * l3[0] - v * l5[1]
    hi = l2[1] + u * l3[1] - v * l5[0]
    target = (Fraction(1286529, 10**12), Fraction(1286530, 10**12))
    assert target[0] < lo <= hi < target[1]
    assert 2 * T * hi < Fraction(1, 40)

    # Natural cutoff: X>1000 from pi<22/7; X<1300 from pi>3.
    # The exact partial sums prove e^8>1300 and e^3<21.
    e8 = sum((Fraction(8**j, factorial(j)) for j in range(16)), Fraction(0))
    e3 = sum((Fraction(3**j, factorial(j)) for j in range(13)), Fraction(0))
    e3_tail = Fraction(14, 11) * Fraction(3**13, factorial(13))
    assert e8 > 1300 and e3 + e3_tail < 21
    assert Fraction(7800 * 7, 44) > 1000
    assert Fraction(7800, 6) == 1300  # strict X<1300 uses pi>3
    assert Fraction(1000, 21) > 47
    assert 2**2 <= 47
    floor = 1 - Fraction(1, 2 * 40**2)
    assert floor == Fraction(3199, 3200)
    return {
        "target_interval": [str(target[0]), str(target[1])],
        "strict_interval": [str(lo), str(hi)],
        "T": T,
        "bases": [p, q, s],
        "N_lower": 47,
        "kernel_lower": str(floor),
        "response_l2": 1,
        "response_valuation": 0,
        "inserted_valuation": r,
    }


def verify_input_hashes(cert):
    for rel, expected in cert["source_sha256"].items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        assert actual == expected, rel


def reject_hostile_mutations(cert):
    f, t = cert["prime_adic_firewall"], cert["trace_grid_discrepancy"]
    b, a, p = cert["Bohr_coefficients"], cert["A1_A2_status"], cert["periodic_aliases"]
    c = cert["p_adic_L2_hilbert_lemma"]
    failures = {
        "put p into leave-one-out state": "contains no p^a" in cert["prime_base_grouping"]["leave_one_out"],
        "independent phases for p powers": "same base phase z_p^a" not in cert["prime_base_grouping"]["definition"],
        "drop proper powers from A1": a["A1_proper_power_current"] != "discarded",
        "mean zero closes A1": a["A1_actual"].startswith("OPEN"),
        "covariance alone closes A2": a["A2_actual"].startswith("OPEN"),
        "omit same trace index": "common to every" in t["same_index"],
        "free grid-to-Haar replacement": "no grid-to-Haar estimate" in t["exact_residual"],
        "p occurs in response character": "p-adic exponent zero" not in f["exact_word_once"],
        "same-sign exact closure": "impossible" not in f["two_current_insertions"],
        "omit equal-power covariance subtraction": "cancels pointwise" in f["equal_power_actual_grid"],
        "assume a 1/T frequency gap": "minimum frequency gap" not in t["exact_residual"],
        "assume X irrational": "X may be tuned" in p["m_nonzero"],
        "drop periodic aliases": "not excluded" in p["m_nonzero"],
        "assume absolute Fourier convergence": "no absolute Fourier convergence" in b["expansion"],
        "reuse falsified L2 lemma": c["status"] == "FALSE for L2 coefficient control alone",
        "interchange R and T": "for each fixed R" in cert["first_remaining_theorem"] and cert["dependent_phase_law"] == "OPEN",
        "shorten natural cutoff": "natural cutoff" in cert["first_remaining_theorem"],
        "alter K or delta": cert["frozen"] == {"K": 32, "delta": "1/100000", "strict_gt79": "OPEN"},
        "synthetic atom is source coefficient": "not asserted to be an actual coefficient" in c["counterexample"]["scope_warning"],
        "claim strict >79": cert["strict_gt79"] is False,
        "drop masks and lag phases": "masks multiply coefficients only" in f["masks_lags"],
    }
    bad = [name for name, rejected in failures.items() if not rejected]
    assert not bad, f"mutations not rejected: {bad}"
    assert len(failures) == 21
    return len(failures)


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["schema"] == "wp84-dependent-phase-prime-adic-firewall-v1"
    assert cert["starting_head"] == "9ba9d4afad19cfdd8a9e4c2e5a386930fc16a14d"
    assert cert["decision"] == "C"
    assert cert["dependent_phase_law"] == "OPEN"
    replayed = replay_atom()
    atom = cert["p_adic_L2_hilbert_lemma"]["counterexample"]
    assert atom["log_frequency_interval"] == replayed["target_interval"]
    assert atom["geometric_kernel_modulus_lower"] == replayed["kernel_lower"]
    assert atom["natural_cutoff_lower_bound_N"] == replayed["N_lower"]
    verify_input_hashes(cert)
    count = reject_hostile_mutations(cert)
    print(f"PASS: independent rational replay, source hashes, {count} hostile mutations.")
    print("PASS: Haar cancellations are separated from the actual trace-grid theorem.")
    print("OPEN: actual A1/A2 trace-grid transfer; strict >79 remains OPEN.")


if __name__ == "__main__":
    main()
