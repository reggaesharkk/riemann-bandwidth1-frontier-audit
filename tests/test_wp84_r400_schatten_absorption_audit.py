import unittest
import json
from fractions import Fraction as F
from pathlib import Path

from src.wp84_r400_schatten_absorption_audit import (
    build_report_data,
    concentration_countermodel,
    finite_band_identity_replay,
    ordinary_prime_product_audit,
    partition_ledger,
)
from src.wp84_physical_kernel_proper_power_reconciliation import build_ledger as replay_parent_atom


class R400SchattenAbsorptionTests(unittest.TestCase):
    def test_exact_finite_t_matrix_commutator_identity(self):
        replay = finite_band_identity_replay(radius=3)
        self.assertTrue(replay["exact_gaussian_rational_match"])
        self.assertEqual(replay["entries_checked"], 25)

    def test_l2_does_not_generically_imply_operator_bound(self):
        row = concentration_countermodel(12)
        self.assertEqual(row["tau_Q2"], str(F(1, 12**2)))
        self.assertEqual(row["operator_norm"], 12)
        self.assertEqual(row["section_size"], 12**4)

    def test_ordinary_exact_closure_and_near_product(self):
        row = ordinary_prime_product_audit()
        self.assertTrue(row["all_exact_equalities_are_same_multiset"])
        self.assertEqual(row["near_product_values"], [10403, 10379])
        self.assertEqual(row["absolute_integer_difference"], 24)

    def test_all_26_source_partition_products_are_explicit(self):
        rows, counts = partition_ledger()
        self.assertEqual(len(rows), 26)
        self.assertEqual(counts, {1: 1, 2: 7, 3: 12, 4: 6})
        self.assertEqual(rows[0]["coefficient"], 1)
        self.assertTrue(all(row["coefficient"] == (-1) ** (len(row["ordered_blocks_zero_based"]) - 1) for row in rows))
        self.assertEqual(sum(row["coefficient"] for row in rows if len(row["ordered_blocks_zero_based"]) == 2), -7)

    def test_parent_one_base_exception_replays_from_original_exact_checker(self):
        ledger = replay_parent_atom()
        self.assertEqual(ledger["partition_counts"], {"1": 1, "2": 7, "3": 12, "4": 6})
        family = ledger["proper_power_ledger_entry"]
        self.assertEqual(family["prime_exponents"], [1, 2, 3, 2])
        self.assertEqual(family["signed_exponent_sum"], 0)
        self.assertEqual(family["family_aggregate_bound"], "O_R(L^-4); this controls this complete one-base resonance family only")
        self.assertEqual(ledger["kernel_reconciliation"]["finite_section"], "at m=10 the physical term vector is e_1 exactly; for every selected m>=10 the independent 25-term bound gives kappa_m>=384/625")
        abstract = ledger["abstract_positive_weight_counterexample"]
        self.assertEqual(abstract["unweighted_public_bracket"], "-1/12")
        self.assertEqual(abstract["positively_reweighted_bracket"], "1187/1200")
        zero = ledger["zero_margin_diagnostic"]
        self.assertEqual(zero["unweighted_bracket"], "0")
        self.assertEqual(zero["nonzero_term_vector_entries_one_based"], [[1, 1], [8, -1]])

    def test_source_interval_replay_covers_all_labeled_placements(self):
        path = Path(__file__).resolve().parents[1] / "evidence" / "WP84_R400_SOURCE_INTERVAL_REPLAY.json"
        replay = json.loads(path.read_text(encoding="utf-8"))
        overlap = replay["r400_overlap"]
        self.assertEqual(overlap["total_labeled_placements"], 48)
        self.assertEqual(overlap["unique_interval_evaluations"], 24)
        self.assertTrue(all(row["strictly_above_799_over_4000"] for row in overlap["placements"]))
        self.assertEqual(replay["row_cumulant"]["exact_rational_m10_lower_bound"], "384/625")

    def test_proper_power_absorption_does_not_use_target_moment_bound(self):
        data = build_report_data()
        gate = data["proper_power_mass_and_transfer"]
        self.assertEqual(gate["proof_status"], "PROVED for every permitted contiguous section of length m>=d-2q, using source frequencies and actual finite-band matrix entries")
        self.assertIn("no bound on either target fourth moment", gate["normalized_schatten4"])
        self.assertEqual(data["decisions"]["PROPER_POWER_SCHATTEN_ABSORPTION"], "PROVED")

    def test_parent_positive_atom_and_kernel_discrepancy_preserved(self):
        data = build_report_data()
        atom = data["prior_positive_atom"]
        self.assertEqual(atom["physical_kappa_m10"], 1)
        self.assertEqual(atom["public_OA"], "2/5")
        self.assertEqual(atom["public_B4"], 0)
        self.assertEqual(atom["root_intervals_in_slot_order"], [["0", "4/5"], ["2/5", "1"], ["0", "2/5"], ["2/5", "1"]])
        self.assertEqual(data["decisions"]["ORDINARY_PHYSICAL_CONNECTED_AGGREGATE"], "OPEN")
        self.assertEqual(data["decisions"]["R400_CONSUMER"], "OPEN")
        diagnostics = data["prior_weight_cone_diagnostics"]
        self.assertEqual(diagnostics["abstract_positive_weight_example"]["reweighted_bracket"], "1187/1200")
        self.assertEqual(diagnostics["zero_margin_example"]["unweighted_bracket"], "0")
        ordinary = data["ordinary_prime_exact_source"]
        self.assertEqual(len(ordinary["all_26_ordered_partition_terms"]), 26)
        self.assertEqual(ordinary["ordered_partition_counts_by_blocks"], {"1": 1, "2": 7, "3": 12, "4": 6})
        self.assertEqual(len(ordinary["all_orientation_words"]), 16)
        self.assertEqual(len(ordinary["six_balanced_orientation_words"]), 6)
        self.assertTrue(all(word.count("+") == 2 for word in ordinary["six_balanced_orientation_words"]))
        self.assertEqual(ordinary["closed_lag_path_count"], 342615201)


if __name__ == "__main__":
    unittest.main()
