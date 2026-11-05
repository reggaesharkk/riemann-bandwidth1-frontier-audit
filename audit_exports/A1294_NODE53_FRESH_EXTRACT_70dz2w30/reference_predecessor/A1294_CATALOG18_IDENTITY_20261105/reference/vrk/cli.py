from __future__ import annotations

import argparse
import json
from pathlib import Path

from .authority import issue_authority_receipt
from .capsule import build_capsule, verify_capsule
from .graph import propagate_statuses
from .ledger import append_event, verify_ledger
from .redteam import run_mutation_suite
from .verify import verify_claim


def main() -> int:
    ap = argparse.ArgumentParser(prog="vrk")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("claim")
    p_verify.add_argument("--receipt")

    p_red = sub.add_parser("redteam")
    p_red.add_argument("claim")
    p_red.add_argument("--output")

    p_ledger = sub.add_parser("ledger-verify")
    p_ledger.add_argument("ledger")

    p_append = sub.add_parser("ledger-append")
    p_append.add_argument("ledger")
    p_append.add_argument("event_json")

    p_prop = sub.add_parser("propagate")
    p_prop.add_argument("claims_json")
    p_prop.add_argument("statuses_json")

    args = ap.parse_args()
    if args.cmd == "verify":
        result = verify_claim(args.claim)
        print(json.dumps(result, indent=2))
        if args.receipt:
            Path(args.receipt).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return 0 if result["pass"] else 1
    if args.cmd == "redteam":
        result = run_mutation_suite(args.claim)
        print(json.dumps(result, indent=2))
        if args.output:
            Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        return 0 if result["all_rejected"] else 1
    if args.cmd == "ledger-verify":
        ok, detail = verify_ledger(args.ledger)
        print("PASS" if ok else "FAIL", detail)
        return 0 if ok else 1
    if args.cmd == "ledger-append":
        event = json.loads(Path(args.event_json).read_text(encoding="utf-8"))
        print(json.dumps(append_event(args.ledger, event), indent=2))
        return 0
    if args.cmd == "propagate":
        claims = json.loads(Path(args.claims_json).read_text(encoding="utf-8"))
        statuses = json.loads(Path(args.statuses_json).read_text(encoding="utf-8"))
        print(json.dumps(propagate_statuses(claims, statuses), indent=2, sort_keys=True))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
