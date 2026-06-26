"""Deterministic graph checks for claim provenance."""
from __future__ import annotations

from typing import Any

UNGROUNDED_STATES = {"proposed", "unverified", "insufficient_evidence"}


def claim_graph_errors(claims: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    state = {claim_id: 0 for claim_id in claims}
    stack: list[str] = []
    positions: dict[str, int] = {}
    cycles: set[tuple[str, ...]] = set()

    for claim_id, claim in sorted(claims.items()):
        if claim.get("evidence_state") != "derived":
            continue
        for reference in claim.get("derived_from", []):
            if reference == claim_id:
                errors.append(f"{claim_id}: derived claim cannot reference itself")
                continue
            parent = claims.get(reference)
            if parent is None:
                errors.append(f"{claim_id}: unknown derived_from claim {reference}")
            elif parent.get("evidence_state") in UNGROUNDED_STATES:
                errors.append(f"{claim_id}: derived_from claim {reference} is not grounded")

    def canonical_cycle(path: list[str]) -> tuple[str, ...]:
        ring = path[:-1]
        rotations = [tuple(ring[index:] + ring[:index]) for index in range(len(ring))]
        selected = min(rotations)
        return selected + (selected[0],)

    def visit(claim_id: str) -> None:
        state[claim_id] = 1
        positions[claim_id] = len(stack)
        stack.append(claim_id)
        for reference in sorted(
            item for item in claims[claim_id].get("derived_from", []) if item in claims
        ):
            if state[reference] == 0:
                visit(reference)
            elif state[reference] == 1:
                cycles.add(canonical_cycle(stack[positions[reference] :] + [reference]))
        stack.pop()
        positions.pop(claim_id, None)
        state[claim_id] = 2

    for claim_id in sorted(claims):
        if state[claim_id] == 0:
            visit(claim_id)
    errors.extend("derived claim cycle: " + " -> ".join(cycle) for cycle in sorted(cycles))
    return sorted(set(errors))
