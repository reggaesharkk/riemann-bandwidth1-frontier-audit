"""Hostile mutation tests for the exact fifth-block audit boundary."""
import copy
import json
import unittest
from pathlib import Path

import wp84_determinant_visible_hidden_prime_replay as replay

ROOT = Path(__file__).resolve().parents[1]


class CompressionReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "notes/WP84_DETERMINANT_VISIBLE_HIDDEN_PRIME_COMPRESSION.json").read_text())

    def rejected(self, mutate):
        data = copy.deepcopy(self.base)
        mutate(data)
        self.assertTrue(replay.validate(data, verify_disk=False))

    def test_good_certificate_replays(self):
        self.assertEqual([], replay.validate(self.base, verify_disk=False))

    def test_wrong_basis_merger_rejected(self):
        self.rejected(lambda d: d["frozen_basis"].update(J=8))

    def test_wrong_moment_power_rejected(self):
        self.rejected(lambda d: d["frozen_basis"].update(master_moments=[f"S_{j}" for j in range(3, 12)]))

    def test_R_mutation_rejected(self):
        self.rejected(lambda d: d.update(R=5999))

    def test_unsupported_K_rejected(self):
        self.rejected(lambda d: d.update(global_K=[2, 3]))

    def test_unsupported_block_K_rejected(self):
        self.rejected(lambda d: d["blocks"][0].update(determinant_visible_K=[2]))

    def test_deleted_block_rejected(self):
        self.rejected(lambda d: d["blocks"].pop())

    def test_section_row_change_rejected(self):
        self.rejected(lambda d: d["blocks"][0].update(formal_first_possible_deficit=4))

    def test_perturbed_first_coefficient_rejected(self):
        self.rejected(lambda d: d["blocks"][0].update(first_nonzero_deficit=5))

    def test_hidden_minor_claim_rejected(self):
        self.rejected(lambda d: d["blocks"][1].update(visible_only_minor=[[1]]))

    def test_rank_promotion_rejected(self):
        self.rejected(lambda d: d.update(new_fifth_analytic_rank=1))

    def test_deleted_correction_rank_boundary_rejected(self):
        self.rejected(lambda d: d["blocks"][2].update(correction_span_rank=1))


if __name__ == "__main__":
    unittest.main()
