# Failed-box and budget analysis

## What `BUDGET_REACHED_WITH_FRONTIER` means

The adaptive and full-root jobs use exact rational arithmetic on closed leaves, but they stop with unresolved boxes when the node budget is reached. A closed-leaf margin is not a global lower bound over pending boxes. In particular, 1,055,320 visited nodes and 366 pending boxes do not certify A1299; 5,057,564 nodes and 1,024 pending boxes do not certify A1296.

The adaptive scan's configured “80,000 budget/candidate” is a chunk budget, not a hard cap on total visited nodes: workers finish submitted chunks, and the saved results exceed 80,000 visits per candidate. The exact result JSON is authoritative for visits and unresolved counts.

## Fixed-B bracket scope

The bracket source reads `deepest_pending_boxes` from the A1299 adaptive result. That result retains only 80 boxes while recording 154 pending boxes. The bracket result records `seed_box_count=80` and six statuses `FULLY_CLOSED_HARD_SEED`; its own interpretation states this closes only the selected hard-seed subset, not the full `[0,60]^5` domain. The script likewise loads those 80 boxes. The pointwise witness is not contained in any of those 80 saved boxes.

Because the historical JSON omits the other 74 pending boxes, this packet does not claim to identify the exact omitted subtree containing the witness. The full-domain counterexample comes from direct evaluation of the point, not from that frontier reconstruction.

## Exact pointwise falsification

The source-independent evaluator in this packet computes all 15 partial sums and scans every closed-domain model in the stable (56), v1 (216), and v3 (394) catalogs. The exact RHS is the fraction shown in the candidate matrix. It is below `1297/100000`, `649/50000`, `1299/100000`, `6497/50000`, and `13/1000`. Those five global inequalities are therefore false at a legal point of the catalog domain, regardless of historical search completion.

For A1295 and A1296 the witness lies above target, so it provides no counterexample. The local runs for those targets still have frontiers. No claim of their completion follows from their positive margins on this single point.

## Search decision

No additional million-node search was launched. It cannot rescue a target at or above .012970 under the unchanged fixed-B catalog inequality because an exact point already refutes it. A1295 and A1296 remain open; a future proof attempt would need a complete root certificate with a preserved full frontier and independent replay, not another partial microscope or selected-box closure.
