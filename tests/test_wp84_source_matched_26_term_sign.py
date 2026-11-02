from __future__ import annotations

import copy
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import wp84_source_matched_26_term_sign_replay as replay


class SourceMatched26TermAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = replay.build_evidence()

    def test_source_pins_and_historical_absence(self):
        manifest = {row["path"]: row for row in self.data["source_hash_manifest"]}
        self.assertEqual(len(manifest), 22)
        for path, blob in replay.PINNED_BLOBS.items():
            self.assertEqual(manifest[path]["git_blob"], blob)
            self.assertEqual(manifest[path]["source_revision"], replay.SOURCE_CONTEXT_REVISION)
        probe = self.data["source_producer_probe"]
        self.assertTrue(probe["callback_is_required_external_argument"])
        self.assertEqual(probe["callback_local_definitions"], 0)
        self.assertEqual(probe["project_callback_definitions_in_tracked_src"], [])
        self.assertEqual(probe["history_callback_definition_hits_all_refs"], [])

    def test_exact_26_term_logical_control(self):
        model = self.data["formula_level_results"]["abstract_countermodel"]
        self.assertEqual(model["term_count"], 26)
        self.assertEqual(model["terms_by_number_of_ordered_blocks"], {"1": 1, "2": 7, "3": 12, "4": 6})
        self.assertEqual(model["first_walk_overlap"], "1/12")
        self.assertEqual(model["unweighted_connected_bracket"], "-1/12")
        self.assertEqual(model["reweighted_bracket"], "1187/1200")
        self.assertEqual(model["reweighted_product"], "1187/14400")
        self.assertTrue(model["all_model_weights_strictly_positive"])
        self.assertEqual(len(model["model_term_register"]), 26)
        for row in model["model_term_register"]:
            self.assertEqual(row["source_eligibility"], "UNKNOWN_SOURCE_SEMANTICS_INCOMPLETE")
            self.assertIsNone(row["source_normalized_weight"])

    def test_common_factor_and_weight_perturbation_control(self):
        model = self.data["formula_level_results"]["abstract_countermodel"]
        self.assertEqual(Q(model["uniformly_scaled_bracket"]), Q(-7, 36))
        self.assertEqual(Q(model["uniformly_scaled_product"]), Q(-7, 432))
        self.assertGreater(Q(model["reweighted_bracket"]), 0)
        self.assertIn("ABSTRACT_LOGICAL_COUNTERMODEL", model["classification"])

    def test_orientation_counts_and_omission_control(self):
        orientation = self.data["formula_level_results"]["orientation_replay"]
        self.assertEqual(orientation["orientation_counts"], {
            "fixed_internal_order_sign_patterns": 6,
            "all_label_permutations": 24,
            "alternating_label_permutations": 8,
        })
        self.assertTrue(all(orientation["identities"][key] for key in (
            "C24_eq_4C6", "C24_eq_C8", "C6_over_2_eq_C8_over_8", "normalized_formula"
        )))
        self.assertEqual(orientation["two_two_pairing_subtraction_terms"], 3)
        self.assertTrue(orientation["omitted_orientation_negative_control"]["rejected"])

    def test_conjugation_control_is_exact_and_rejects_wrong_orientation(self):
        conjugation = self.data["formula_level_results"]["conjugation_replay"]
        self.assertEqual(conjugation["K_T_Y"], ["-1/14", "-1/14"])
        self.assertEqual(conjugation["K_T_minus_Y"], ["-1/14", "1/14"])
        self.assertEqual(conjugation["conjugate_pair_sum"], ["-1/7", "0"])
        self.assertEqual(conjugation["incorrect_same_orientation_pair_sum"], ["-1/7", "-1/7"])
        self.assertTrue(conjugation["conjugation_mutation_rejected"])

    def test_selection_mutations_cannot_pass_hash_or_claim_guard(self):
        source_rel = "src/wp84_fifth_full_pool_amplitude.py"
        source_row = next(row for row in self.data["source_hash_manifest"] if row["path"] == source_rel)
        original = (ROOT / source_rel).read_text(encoding="utf-8")
        changed_filter = original.replace(
            "if source_mask(fid,slots,lag,T,section,m)]",
            "if True]",
            1,
        )
        self.assertNotEqual(changed_filter, original)
        self.assertNotEqual(replay.sha256(changed_filter.encode("utf-8")), source_row["sha256"])

        changed_selector = original + "\ndef selected_section(T): return (0, 1)\n"
        self.assertNotEqual(replay.sha256(changed_selector.encode("utf-8")), source_row["sha256"])

        promoted = copy.deepcopy(self.data)
        promoted["gates"]["SOURCE_MASK_RECONSTRUCTED"] = "PASS"
        promoted["source_semantics"]["source_mask_order_dependence_testable"] = True
        promoted["formula_level_results"]["abstract_countermodel"]["model_term_register"][0]["source_mask"] = "all true"
        errors = replay.claim_boundary_errors(promoted)
        self.assertTrue(any("source-mask gate promoted" in error for error in errors))
        self.assertTrue(any("source-mask ordering result promoted" in error for error in errors))
        self.assertTrue(any("invented source value" in error for error in errors))

    def test_required_gates_remain_blocked_or_open(self):
        self.assertEqual(replay.claim_boundary_errors(self.data), [])
        gates = self.data["gates"]
        self.assertEqual(gates["SOURCE_MASK_RECONSTRUCTED"], "BLOCKED_SOURCE_SEMANTICS_INCOMPLETE")
        self.assertEqual(gates["CONNECTED_WEIGHT_FACTORIZATION"], "BLOCKED_SOURCE_SEMANTICS_INCOMPLETE")
        self.assertEqual(gates["FULL_BOUNDED_CONSUMER"], "OPEN")
        self.assertEqual(gates["UNCONDITIONAL_GT79"], "OPEN")


if __name__ == "__main__":
    unittest.main()
