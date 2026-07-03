from __future__ import annotations

import copy

from tools.queue_common import load_queue
from tools.queue_controller import select_execution_slice


def _task(
    template: dict,
    *,
    task_id: str,
    task_type: str,
    stage_id: str | None,
) -> dict:
    task = copy.deepcopy(template)
    task["id"] = task_id
    task["spec"]["task_type"] = task_type
    task["spec"]["stage_id"] = stage_id
    task["spec"]["depends_on"] = []
    task["runtime"]["status"] = "pending"
    return task


def test_execution_slice_keeps_one_primary_and_three_safe_preparations() -> None:
    queue = load_queue()
    queue["controller_policy"]["max_planned_preparation_tasks"] = 3
    template = queue["tasks"][0]
    primary = _task(
        template,
        task_id="RQ-1000",
        task_type="stage_finalization",
        stage_id="KB-004",
    )
    second_mutation = _task(
        template,
        task_id="RQ-1001",
        task_type="stage_authoring",
        stage_id="KB-005",
    )
    same_stage_preparation = _task(
        template,
        task_id="RQ-1002",
        task_type="fixture_collection",
        stage_id="KB-004",
    )
    preparations = [
        _task(
            template,
            task_id=f"RQ-{number}",
            task_type=task_type,
            stage_id=stage_id,
        )
        for number, task_type, stage_id in [
            (1003, "fixture_collection", "KB-005"),
            (1004, "manual_evidence_request", "KB-018"),
            (1005, "documentation_sync", None),
            (1006, "fixture_collection", "KB-019"),
        ]
    ]

    selected = select_execution_slice(
        queue,
        [primary, second_mutation, same_stage_preparation, *preparations],
    )

    assert [task["id"] for task in selected] == [
        "RQ-1000",
        "RQ-1003",
        "RQ-1004",
        "RQ-1005",
    ]


def test_execution_slice_defaults_to_three_preparations() -> None:
    queue = load_queue()
    assert "max_planned_preparation_tasks" not in queue["controller_policy"]
    template = queue["tasks"][0]
    tasks = [
        _task(
            template,
            task_id="RQ-1100",
            task_type="stage_finalization",
            stage_id="KB-004",
        )
    ] + [
        _task(
            template,
            task_id=f"RQ-{number}",
            task_type="fixture_collection",
            stage_id=f"KB-0{number - 1095}",
        )
        for number in range(1101, 1105)
    ]

    assert len(select_execution_slice(queue, tasks)) == 4
