from __future__ import annotations

from collections import defaultdict


def detect_claim_conflicts(receipts: list[dict]) -> dict[str, dict]:
    by_id_props: dict[str, set[str]] = defaultdict(set)
    by_prop_classes: dict[str, set[str]] = defaultdict(set)
    by_id_packages: dict[str, set[str]] = defaultdict(set)
    for r in receipts:
        cid = r.get("claim_id"); prop = r.get("proposition_digest"); cls = r.get("claim_class"); pkg = r.get("claim_digest")
        if cid and prop: by_id_props[cid].add(prop)
        if prop and cls: by_prop_classes[prop].add(cls)
        if cid and pkg: by_id_packages[cid].add(pkg)
    out = {}
    for cid, props in by_id_props.items():
        if len(props) > 1:
            out[cid] = {"type":"CLAIM_ID_SEMANTIC_CONFLICT", "proposition_digests":sorted(props)}
    for prop, classes in by_prop_classes.items():
        if len(classes) > 1:
            out[f"proposition:{prop}"] = {"type":"CLASSIFICATION_CONFLICT", "claim_classes":sorted(classes)}
    return out
