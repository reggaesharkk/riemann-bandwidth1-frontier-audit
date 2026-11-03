import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

from src.wp84_r400_cumulant_endpoint_tensor import (
    DELTA,
    ZERO,
    cabs2,
    csub,
    delete_endpoint_mean,
    exp_quarter,
    exact_ledgers,
    kappa,
    l1_measure,
    ordered_anchored_partitions,
    partition_deletion_delta,
    partition_term,
    path_root_interval,
    path_root_sum,
    report_data,
    row_measure,
    section_tensor_weights,
    tensor_fourier_value,
    tv_cumulant_bound,
)


ROOT = Path(__file__).resolve().parents[1]


class CumulantEndpointTensorTests(unittest.TestCase):
    def test_partition_counts_and_terms_match_parent_source_ledger(self):
        rows, counts, block_total = ordered_anchored_partitions()
        self.assertEqual((len(rows), counts, block_total), (26, {1: 1, 2: 7, 3: 12, 4: 6}, 75))
        parent = json.loads((ROOT / "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json").read_text())
        source_rows = parent["ordinary_prime_exact_source"]["all_26_ordered_partition_terms"]
        self.assertEqual(len(source_rows), 26)
        for (coefficient, blocks), source in zip(rows, source_rows):
            self.assertEqual(coefficient, source["coefficient"])
            self.assertEqual([list(b) for b in blocks], source["ordered_blocks_zero_based"])

    def test_total_variation_bound_and_300r_over_d_consequence(self):
        v = (F(1, 4), F(-1, 4), F(1, 2), F(-1, 2))
        mu = row_measure(0, 12)
        first = row_measure(2, 10)
        second = row_measure(1, 10)
        self.assertEqual(l1_measure(mu, first), F(1, 3))
        self.assertLessEqual(
            cabs2(csub(kappa(2, 10, v), kappa(0, 12, v))),
            tv_cumulant_bound(mu, first) ** 2,
        )
        r, d = 2, 12
        self.assertLessEqual(
            cabs2(csub(kappa(2, 10, v), kappa(1, 10, v))),
            (F(300 * r, d)) ** 2,
        )
        self.assertEqual(tv_cumulant_bound(mu, first), F(25))

    def test_left_and_right_mean_deletion_identity_exact(self):
        for x in (F(0), F(1, 4), F(-1, 2)):
            delete_endpoint_mean(3, 9, x, "left")
            delete_endpoint_mean(3, 9, x, "right")

    def test_each_of_26_partition_terms_has_exact_endpoint_telescope(self):
        vector = (F(1, 4), F(-1, 4), F(1, 2), F(-1, 2))
        for coefficient, blocks in ordered_anchored_partitions()[0]:
            for side in ("left", "right"):
                delta = partition_deletion_delta(1, 8, side, blocks, vector)
                if side == "left":
                    newer = partition_term(coefficient, blocks, 2, 7, vector)
                else:
                    newer = partition_term(coefficient, blocks, 1, 7, vector)
                older = partition_term(coefficient, blocks, 1, 8, vector)
                self.assertEqual((coefficient * delta[0], coefficient * delta[1]), (newer[0] - older[0], newer[1] - older[1]))

    def test_tensor_weights_normalize_and_reconstruct_every_partition_term(self):
        sections = [(0, 6, F(1, 4)), (1, 5, F(1, 4)), (1, 4, F(1, 4)), (2, 4, F(1, 4))]
        vector = (F(1, 4), F(-1, 4), F(1, 2), F(-1, 2))
        for _, blocks in ordered_anchored_partitions()[0]:
            weights = section_tensor_weights(blocks, sections)
            self.assertEqual(sum(weights.values(), F(0)), F(1))
            direct = ZERO
            for start, length, mass in sections:
                value = (F(1), F(0))
                for block in blocks:
                    from src.wp84_r400_cumulant_endpoint_tensor import cmul, row_mean, vector_block_sum

                    value = cmul(value, row_mean(start, length, vector_block_sum(vector, block)))
                from src.wp84_r400_cumulant_endpoint_tensor import cadd, cscale

                direct = cadd(direct, cscale(value, mass))
            self.assertEqual(tensor_fourier_value(weights, blocks, vector), direct)

    def test_exact_carrier_overlap_weighted_tensor_ledger_keeps_all_terms(self):
        tensor = exact_ledgers()["tensor_average"]
        checked = tensor["physical_weighted_terms_checked"]
        self.assertEqual(len(checked), 26)
        self.assertTrue(all(row["exact_identity"] for row in checked))
        self.assertIn("generally complex and not 1", tensor["physical_weighted_W_normalization"])

    def test_compressed_path_root_intervals_and_endpoint_deletions(self):
        lags = (2, -2, 0, 0)
        old = path_root_interval(3, 9, lags)
        left = path_root_interval(4, 8, lags)
        right = path_root_interval(3, 8, lags)
        self.assertEqual((old["lower"], old["upper"], old["count"]), (3, 9, 7))
        self.assertEqual((left["lower"], left["upper"], left["count"]), (4, 9, 6))
        self.assertEqual((right["lower"], right["upper"], right["count"]), (3, 8, 6))
        old_mu = {k: F(1, 9) for k in range(old["lower"], old["upper"] + 1)}
        left_mu = {k: F(1, 8) for k in range(left["lower"], left["upper"] + 1)}
        right_mu = {k: F(1, 8) for k in range(right["lower"], right["upper"] + 1)}
        self.assertLessEqual(l1_measure(old_mu, left_mu), F(2, 9))
        self.assertLessEqual(l1_measure(old_mu, right_mu), F(2, 9))
        max_span = path_root_interval(0, 1000, (400, 400, -400, -400))
        self.assertEqual(max(max_span["prefixes"]) - min(max_span["prefixes"]), 800)
        self.assertEqual(max_span["count"], 200)
        for side, start, length in (("left", 3, 9), ("right", 3, 9)):
            original = path_root_sum(start, length, lags, F(1, 4))
            if side == "left":
                changed = path_root_sum(start + 1, length - 1, lags, F(1, 4))
            else:
                changed = path_root_sum(start, length - 1, lags, F(1, 4))
            self.assertNotEqual(original, changed)

    def test_zero_detuning_zero_margin_and_near_product_indices_are_retained(self):
        zero_vector = (F(0), F(0), F(0), F(0))
        self.assertEqual(kappa(0, 9, zero_vector), ZERO)
        balanced = (F(1, 4), F(-1, 4), F(1, 2), F(-1, 2))
        self.assertEqual(sum(balanced, F(0)), 0)
        self.assertEqual(exp_quarter(17, sum(balanced, F(0))), (F(1), F(0)))
        grouping = json.loads((ROOT / "evidence/WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json").read_text())
        near = grouping["ordinary_product_grouping"]["near_product_source_summand"]
        self.assertEqual(near["products"], [10403, 10379])
        self.assertEqual(near["absolute_integer_gap"], 24)
        self.assertIn("not an asymptotic", near["scope"])

    def test_near_alias_row_cluster_has_exact_rational_real_lower_bound(self):
        # Relative row frequency x=1/(100d); for every 0<=k<d,
        # |2*pi*k*x| < 11/175 using pi<22/7. Then cos(t)>=1-t^2/2.
        d = 60
        theta_bound = F(11, 175)
        real_lower = F(1) - theta_bound * theta_bound / 2
        self.assertGreater(real_lower, F(998, 1000))
        x = F(1, 100 * d)
        self.assertLessEqual((d - 1) * x, F(1, 100))
        self.assertEqual(x, F(1, 6000))

    def test_record_budget_decisions_remain_open_or_conditional(self):
        decisions = report_data()["decisions"]
        self.assertEqual(decisions["CUMULANT_ENDPOINT_IDENTITY"], "PROVED")
        self.assertEqual(decisions["TENSOR_AVERAGING"], "EXACT")
        self.assertEqual(decisions["SOURCE_WEIGHTED_CORRECTION"], "OPEN")
        self.assertEqual(decisions["ORDINARY_CONNECTED_RECORD_BOUND"], "OPEN")
        self.assertEqual(decisions["R400_CONSUMER"], "CONDITIONAL")
        self.assertEqual(DELTA, F(3675673694911, 148250000000000))


if __name__ == "__main__":
    unittest.main()
