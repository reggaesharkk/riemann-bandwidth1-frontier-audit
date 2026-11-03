import unittest
from fractions import Fraction as F

from src.wp84_r400_physical_endpoint_averaging import (
    DELTA,
    endpoint_kernel_weights,
    endpoint_kernel_weights_measure,
    endpoint_pairs,
    exact_ledgers,
    gaussian_weighted_sum,
    gaussian_unit_quarter,
    joint_selection_ledger,
    kappa_half,
    kappa_length_correction_bound,
    path_boundary_count,
)


class PhysicalEndpointAveragingTests(unittest.TestCase):
    def test_uniform_endpoint_kernel_identity_weights_are_exact_probability(self):
        weights = endpoint_kernel_weights(6, 2, b=3)
        self.assertEqual(sum(weights.values()), F(1))
        self.assertTrue(all(w >= 0 for w in weights.values()))
        direct = sum(
            (F(1, 9) / m for u, v, m in endpoint_pairs(6, 2) for _ in range(m)),
            F(0),
        )
        self.assertEqual(direct, F(1))

    def test_conditioned_source_selected_sections_have_exact_weights(self):
        selected = {(0, 0), (0, 1), (1, 0), (1, 1)}
        weights = endpoint_kernel_weights(6, 2, selected=selected)
        self.assertEqual(sum(weights.values()), F(1))
        self.assertTrue(all(w >= 0 for w in weights.values()))
        phase = gaussian_weighted_sum(weights)
        direct_real = F(0)
        direct_imag = F(0)
        rows = [(u, v, m) for u, v, m in endpoint_pairs(6, 2) if (u, v) in selected]
        for u, v, m in rows:
            for k in range(u, 6 - v):
                a, b = gaussian_unit_quarter(k)
                direct_real += F(a, len(rows) * m)
                direct_imag += F(b, len(rows) * m)
        self.assertEqual(phase, (direct_real, direct_imag))

    def test_arbitrary_nonnegative_section_measure_has_exact_kernel_weights(self):
        rho = {(0, 0): F(1, 3), (1, 2): F(2, 3)}
        weights = endpoint_kernel_weights_measure(8, 2, rho, b=5)
        self.assertTrue(all(w >= 0 for w in weights.values()))
        self.assertEqual(sum(weights.values()), F(1))
        for k in range(5, 13):
            expected = F(0)
            if 5 <= k < 13:
                expected += rho[(0, 0)] / 8
            if 6 <= k < 11:
                expected += rho[(1, 2)] / 5
            self.assertEqual(weights[k], expected)

    def test_normalization_and_endpoint_boundary_correction(self):
        data = exact_ledgers()["finite_endpoint_example"]
        self.assertEqual(data["weights_sum"], "1")
        self.assertEqual(data["unnormalized_row_sum_weights_total"], "4")
        path = path_boundary_count(9, (2, -2, 0, 0))
        self.assertEqual(path["span"], 2)
        self.assertEqual(path["fractional_path_correction_at_Y_zero"], F(-2, 9))

    def test_physical_cumulant_depends_on_trimmed_length(self):
        v = (F(1, 2), F(-1, 2), F(1, 2), F(-1, 2))
        self.assertEqual(kappa_half(2, v), F(-2))
        self.assertEqual(kappa_half(3, v), F(-32, 27))
        ledger = exact_ledgers()["section_dependent_cumulant_example"]
        self.assertNotEqual(ledger["uniform_section_average_kappa"], ledger["kappa_at_untrimmed_length_d"])
        self.assertEqual(kappa_length_correction_bound(10, 8), F(30))
        for m in range(2, 11):
            self.assertLessEqual(
                abs(kappa_half(m, v) - kappa_half(10, v)),
                kappa_length_correction_bound(10, m),
            )

    def test_joint_selection_improves_delta_over_eight_condition(self):
        old = joint_selection_ledger(F(1, 8))
        better = joint_selection_ledger(F(1, 16))
        self.assertEqual(F(old["exact_mean_budget"]), DELTA / 8)
        self.assertEqual(F(better["exact_mean_budget"]), 3 * DELTA / 16)
        self.assertEqual(DELTA / 4, F(3675673694911, 593000000000000))

    def test_positive_part_does_not_commute_with_endpoint_averaging(self):
        row = exact_ledgers()["positive_part_noncommutation"]
        self.assertEqual(row["average_signed"], "0")
        self.assertEqual(row["average_positive_part"], "1/2")
        self.assertEqual(row["positive_part_of_average"], "0")

    def test_all_26_terms_and_six_balanced_words_are_retained(self):
        data = exact_ledgers()["partitions"]
        self.assertEqual(data["total"], 26)
        self.assertEqual(data["block_counts"], {1: 1, 2: 7, 3: 12, 4: 6})
        self.assertEqual(data["sign_word_total"], 16)
        self.assertEqual(len(data["balanced_words"]), 6)

    def test_near_alias_cluster_stays_near_one_under_exact_interval_weights(self):
        from mpmath import iv

        iv.dps = 50
        weights = endpoint_kernel_weights(60, 3)
        eps = iv.mpf(1) / 60000
        value = sum(
            (iv.mpf(w.numerator) / w.denominator) * iv.cos(2 * iv.pi * k * eps)
            for k, w in weights.items()
        )
        self.assertTrue(value > iv.mpf("0.999"))
        self.assertEqual(sum(weights.values()), F(1))

    def test_zero_margin_and_abstract_positive_reweighting_are_preserved(self):
        from src.wp84_physical_kernel_proper_power_reconciliation import build_ledger

        ledger = build_ledger()
        zero = ledger["zero_margin_diagnostic"]
        self.assertEqual(zero["unweighted_bracket"], "0")
        self.assertEqual(zero["nonzero_term_vector_entries_one_based"], [[1, 1], [8, -1]])
        abstract = ledger["abstract_positive_weight_counterexample"]
        self.assertEqual(abstract["unweighted_public_bracket"], "-1/12")
        self.assertEqual(abstract["positively_reweighted_bracket"], "1187/1200")

    def test_near_and_unequal_product_scales_remain_distinct_source_groups(self):
        rows = exact_ledgers()["ordinary_prime_product_diagnostics"]
        self.assertEqual(rows["near_comparable_products"], {"A": 10403, "B": 10379, "gap": 24})
        self.assertEqual(rows["unequal_scale_products"]["A"], 6)
        self.assertEqual(rows["unequal_scale_products"]["B"], 10403)
        self.assertIn("neither example estimates", rows["scope"])

    def test_parent_source_interval_certificate_replays_without_writing(self):
        import sys
        from pathlib import Path

        root = Path(__file__).resolve().parents[1]
        sys.path.insert(0, str(root / "src"))
        try:
            import wp84_r400_source_interval_replay as replay

            data = replay.build()
        finally:
            sys.path.pop(0)
        self.assertEqual(data["r400_overlap"]["total_labeled_placements"], 48)
        self.assertEqual(data["r400_overlap"]["unique_interval_evaluations"], 24)
        self.assertEqual(data["row_cumulant"]["exact_rational_m10_lower_bound"], "384/625")

    def test_decisions_keep_aggregate_open(self):
        decisions = __import__("src.wp84_r400_physical_endpoint_averaging", fromlist=["build_report_data"]).build_report_data()["decisions"]
        self.assertEqual(decisions["AVERAGED_FOURIER_KERNEL"], "EXACT")
        self.assertEqual(decisions["PHYSICAL_CUMULANT_AVERAGING"], "CORRECTION_REQUIRED")
        self.assertEqual(decisions["JOINT_ENDPOINT_SELECTION"], "CONDITIONAL")
        self.assertEqual(decisions["ORDINARY_CONNECTED_AGGREGATE"], "OPEN")
        self.assertEqual(decisions["R400_CONSUMER"], "CONDITIONAL")


if __name__ == "__main__":
    unittest.main()
