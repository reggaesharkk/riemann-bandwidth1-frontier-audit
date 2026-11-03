import unittest
from fractions import Fraction as F

from src.wp84_r400_endpoint_near_product_audit import (
    DELTA,
    balanced_words,
    build_report_data,
    endpoint_intersection_ledger,
    source_product_grouping,
)


class R400EndpointNearProductAuditTests(unittest.TestCase):
    def test_exact_record_budget(self):
        data = build_report_data()
        record = data["decisions"]["record_budget"]
        self.assertEqual(DELTA, F(3675673694911, 148250000000000))
        self.assertEqual(F(record["pair_plus_delta_exact"]), F(43158947944911, 148250000000000))

    def test_all_six_balanced_sign_words_are_retained_once(self):
        self.assertEqual(balanced_words(), ["++--", "+-+-", "+--+", "-++-", "-+-+", "--++"])
        grouped = source_product_grouping()
        self.assertEqual(len(grouped["balanced_sign_words_each_counted_once"]), 6)
        self.assertIn("no extra factor of six", grouped["ordered_prime_tuple_multiplicity"])

    def test_independent_endpoint_existence_does_not_intersect(self):
        ledger = endpoint_intersection_ledger()
        bad = ledger["independent_existence_counterexample"]
        self.assertTrue(bad["endpoint_good_sections"])
        self.assertTrue(bad["connected_good_sections"])
        self.assertEqual(bad["intersection"], [])

    def test_joint_selection_requires_exact_source_mean_premise(self):
        joint = endpoint_intersection_ledger()["conditional_joint_selection"]
        self.assertEqual(joint["already_admissible_density_lower_bound"], "1/8")
        self.assertEqual(joint["exact_fraction"], "3675673694911/1186000000000000")
        self.assertIn("<", joint["sufficient_global_mean_positive_excess"])

    def test_grouping_retains_actual_near_product_tuple_and_limitation(self):
        row = source_product_grouping()
        summand = row["near_product_source_summand"]
        self.assertEqual(summand["products"], [10403, 10379])
        self.assertEqual(summand["absolute_integer_gap"], 24)
        self.assertIn("not an asymptotic", summand["scope"])
        self.assertIn("does not assert prime products occupy every integer gap", row["spacing_observation"]["scope"])

    def test_decisions_do_not_promote_the_consumer_or_connected_aggregate(self):
        decisions = build_report_data()["decisions"]
        self.assertEqual(decisions["SCHATTEN_TRANSFER"], "PROVED")
        self.assertEqual(decisions["EXISTENTIAL_ENDPOINT_REDUCTION"], "NOT_SUFFICIENT")
        self.assertEqual(decisions["ORDINARY_CONNECTED_AGGREGATE"], "OPEN")
        self.assertEqual(decisions["R400_CONSUMER"], "CONDITIONAL")


if __name__ == "__main__":
    unittest.main()
