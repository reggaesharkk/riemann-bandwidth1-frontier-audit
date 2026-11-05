from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet

CLAIM_CLASSES = {
    "CONJECTURE",
    "NUMERICAL_OBSERVATION",
    "REPRODUCED_RESULT",
    "EXHAUSTIVE_FINITE_RESULT",
    "INTERVAL_CERTIFIED_RESULT",
    "ANALYTIC_THEOREM",
}

LIFECYCLE_STATUSES = {"ACTIVE", "REVIEW_REQUIRED", "FALSIFIED", "RETRACTED", "SUPERSEDED"}
KERNEL_STATUSES = {"UNVERIFIED", "EVIDENCE_BOUND", "LOCALLY_REPLAYED", "CERTIFIED"}

# Class-specific obligations.  A role being present is not sufficient for local replay;
# required roles must also satisfy their role policy below.
REQUIRED_ROLES: dict[str, FrozenSet[str]] = {
    "CONJECTURE": frozenset(),
    "NUMERICAL_OBSERVATION": frozenset({"definition", "execution_record"}),
    "REPRODUCED_RESULT": frozenset({"definition", "execution_record", "independent_replication"}),
    "EXHAUSTIVE_FINITE_RESULT": frozenset({
        "definition", "passing_witness", "exclusion_certificate",
        "coverage_certificate", "independent_verification",
    }),
    "INTERVAL_CERTIFIED_RESULT": frozenset({"definition", "interval_certificate", "verifier"}),
    "ANALYTIC_THEOREM": frozenset({"definition", "proof", "scope_statement", "independent_verification"}),
}

# Required roles that count as locally replayed only when a verifier plugin ran.
REPLAY_REQUIRED_ROLES = {
    "execution_record", "independent_replication", "passing_witness",
    "exclusion_certificate", "coverage_certificate", "interval_certificate",
    "verifier", "proof", "independent_verification",
}

@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str
