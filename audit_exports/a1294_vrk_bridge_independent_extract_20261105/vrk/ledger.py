from __future__ import annotations

import hmac
import json
from hashlib import sha256
from pathlib import Path

from .canonical import canonical_json_bytes, sha256_bytes

GENESIS = "0" * 64


def append_event(path: str | Path, event: dict) -> dict:
    p = Path(path)
    prev = GENESIS
    seq = 1
    if p.exists():
        lines = [line for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
        if lines:
            last = json.loads(lines[-1])
            prev = last["event_hash"]
            seq = int(last["seq"]) + 1
    body = {"seq": seq, "prev_hash": prev, "event": event}
    event_hash = sha256_bytes(canonical_json_bytes(body))
    row = {**body, "event_hash": event_hash}
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")
    return row


def verify_ledger(path: str | Path) -> tuple[bool, str]:
    p = Path(path)
    prev = GENESIS
    expected_seq = 1
    if not p.exists():
        return True, "empty ledger"
    for line_no, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            if row["seq"] != expected_seq:
                return False, f"line {line_no}: seq mismatch"
            if row["prev_hash"] != prev:
                return False, f"line {line_no}: prev_hash mismatch"
            body = {"seq": row["seq"], "prev_hash": row["prev_hash"], "event": row["event"]}
            actual = sha256_bytes(canonical_json_bytes(body))
            if actual != row["event_hash"]:
                return False, f"line {line_no}: event_hash mismatch"
            prev = row["event_hash"]
            expected_seq += 1
        except Exception as e:
            return False, f"line {line_no}: {e}"
    return True, f"{expected_seq-1} events; head={prev}"


def ledger_head(path: str | Path) -> tuple[int, str]:
    p = Path(path)
    if not p.exists() or not p.read_text(encoding="utf-8").strip():
        return 0, GENESIS
    last = json.loads([x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()][-1])
    return int(last["seq"]), str(last["event_hash"])


def seal_ledger_head(path: str | Path, key: bytes, *, anchor_id: str) -> dict:
    ok, detail = verify_ledger(path)
    if not ok:
        raise ValueError(detail)
    seq, head = ledger_head(path)
    body = {"schema": "intentseal-vrk-ledger-anchor-v1", "anchor_id": anchor_id, "seq": seq, "head_hash": head}
    body["mac"] = hmac.new(key, canonical_json_bytes(body), sha256).hexdigest()
    return body


def verify_ledger_anchor(path: str | Path, anchor: dict, key: bytes) -> tuple[bool, str]:
    ok, detail = verify_ledger(path)
    if not ok:
        return False, detail
    mac = anchor.get("mac")
    unsigned = dict(anchor); unsigned.pop("mac", None)
    expected = hmac.new(key, canonical_json_bytes(unsigned), sha256).hexdigest()
    if not isinstance(mac, str) or not hmac.compare_digest(mac, expected):
        return False, "anchor MAC mismatch"
    seq, head = ledger_head(path)
    if seq != anchor.get("seq") or head != anchor.get("head_hash"):
        return False, "ledger head differs from sealed anchor"
    return True, "ledger matches authenticated external anchor"
