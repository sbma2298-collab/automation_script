from local_runtime.mock_mbo import MockMbo
from local_runtime.mock_service import MockService

from automation_scripts.workorder_priority_script import (
    initialize_workorder_priority
)


def test_emergency_work_order_priority():
    mbo = MockMbo({
        "WORKTYPE": "EM"
    })

    priority = initialize_workorder_priority(
        mbo,
        MockService()
    )

    assert priority == 1


def test_corrective_work_order_priority():
    mbo = MockMbo({
        "WORKTYPE": "CM"
    })

    priority = initialize_workorder_priority(
        mbo,
        MockService()
    )

    assert priority == 3


def test_default_work_order_priority():
    mbo = MockMbo({
        "WORKTYPE": "OTHER"
    })

    priority = initialize_workorder_priority(
        mbo,
        MockService()
    )

    assert priority == 5
