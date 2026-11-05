from __future__ import annotations

from collections import defaultdict, deque


INVALIDATING_STATUSES = {"FALSIFIED", "RETRACTED"}


def propagate_statuses(claims: list[dict], status_by_id: dict[str, str]) -> dict[str, str]:
    """Propagate invalidation downstream through dependency edges.

    A falsified/retracted claim does not automatically falsify descendants. It marks
    them REVIEW_REQUIRED unless they are already terminal themselves.
    """
    children: dict[str, set[str]] = defaultdict(set)
    for claim in claims:
        cid = claim["claim_id"]
        for dep in claim.get("dependencies", []):
            parent = dep["claim_id"]
            children[parent].add(cid)

    out = dict(status_by_id)
    q = deque(cid for cid, st in out.items() if st in INVALIDATING_STATUSES)
    seen = set(q)
    while q:
        parent = q.popleft()
        for child in children.get(parent, ()): 
            if out.get(child) not in INVALIDATING_STATUSES:
                out[child] = "REVIEW_REQUIRED"
            if child not in seen:
                seen.add(child)
                q.append(child)
    return out
