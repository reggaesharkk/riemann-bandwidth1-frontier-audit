from __future__ import annotations

import sys
import unittest
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import replay_alpoge_furman as replay


class ConstantReplayTests(unittest.TestCase):
    def test_base_window_constants_are_exact(self):
        r0 = Fraction(4, 3)
        self.assertEqual(2 - r0, Fraction(2, 3))
        self.assertEqual((3 - r0) / 2, Fraction(5, 6))

    def test_mt_interval_contains_rounded_source_value(self):
        lo, hi = replay.mt_c0_interval()
        printed = Fraction(6725, 10_000)
        self.assertLess(lo, hi)
        self.assertLess(abs(lo - printed), Fraction(1, 100_000))
        self.assertLess(abs(hi - printed), Fraction(1, 100_000))

    def test_mt_rearrangements_are_consistent(self):
        lo, hi = replay.mt_c0_interval()
        c1lo, c1hi = (lo + 1) / 2, (hi + 1) / 2
        rlo, rhi = 2 - hi, 2 - lo
        self.assertEqual(2 - rhi, lo)
        self.assertEqual(2 - rlo, hi)
        self.assertEqual(c1lo, (3 - rhi) / 2)
        self.assertEqual(c1hi, (3 - rlo) / 2)

    def test_pair_ceiling_fraction_matches_published_rounding(self):
        printed_upper = Fraction(6818287, 10_000_000)
        self.assertLess(replay.P0, printed_upper)
        self.assertEqual(
            replay.P0,
            Fraction(
                10909258999421303588095230195816054408197,
                16000000000000000000000000000000000000000,
            ),
        )

    def test_json_records_conditional_boundary(self):
        result = replay.replay()
        ceiling = result["values"][-1]
        self.assertEqual(ceiling["status"], "PASS")
        self.assertIn("conditional", ceiling["claim_class"])
        self.assertEqual(result["gate_status"]["EnclOK_external_interval_replay"], "NOT_RUN")

    def test_committed_reports_match_recomputed_values(self):
        expected = replay.replay()
        reports = [
            ROOT / "research/rh_bandwidth1_20261003/replay.json",
            ROOT / "results/replay/replay.json",
        ]
        for report in reports:
            self.assertEqual(json.loads(report.read_text(encoding="utf-8")), expected)


class FiniteMatrixPilotTests(unittest.TestCase):
    def test_isolated_simple_zero_frame_normalization(self):
        # A normalized two-coordinate frame vector has unit trace contribution.
        vector = [Fraction(3, 5), Fraction(4, 5)]
        normalizer = sum((x * x for x in vector), Fraction(0))
        contribution = [
            [x * y / normalizer for y in vector]
            for x in vector
        ]
        self.assertTrue(replay.is_symmetric(contribution))
        self.assertEqual(replay.trace(contribution), Fraction(1))
        self.assertEqual(replay.rank(contribution), 1)

    def test_symmetric_matrix_trace_and_hilbert_schmidt_identities(self):
        g = [
            [Fraction(2), Fraction(1, 3), Fraction(0)],
            [Fraction(1, 3), Fraction(1), Fraction(1, 5)],
            [Fraction(0), Fraction(1, 5), Fraction(3)],
        ]
        self.assertTrue(replay.is_symmetric(g))
        self.assertEqual(replay.frobenius_sq(g), replay.trace(replay.matmul(g, g)))

    def test_trace_additivity_for_zero_side_split(self):
        p = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(2)]]
        q = [[Fraction(-1), Fraction(0)], [Fraction(0), Fraction(1)]]
        g = replay.matrix_add(p, q)
        self.assertEqual(replay.trace(g), replay.trace(p) + replay.trace(q))
        self.assertEqual(replay.frobenius_sq(g), replay.trace(replay.matmul(g, g)))

    def test_rank_trace_inertia_inequality_on_synthetic_diagonal_cases(self):
        cases = [
            (
                [[Fraction(1), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(1), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)]],
                [[Fraction(0), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)]],
                0,
            ),
            (
                [[Fraction(1), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)]],
                [[Fraction(-1), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(1), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)]],
                1,
            ),
            (
                [[Fraction(2), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)]],
                [[Fraction(-1), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(-1), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)]],
                0,
            ),
        ]
        for p, q, b in cases:
            self.assertTrue(replay.is_symmetric(p))
            self.assertTrue(replay.is_symmetric(q))
            self.assertTrue(all(p[i][i] >= 0 for i in range(3)))
            positive_index_q = sum(1 for i in range(3) if q[i][i] > 0)
            self.assertLessEqual(positive_index_q, b)
            self.assertGreaterEqual(replay.rank(p), replay.rank_trace_rhs(p, q, b))


if __name__ == "__main__":
    unittest.main()
