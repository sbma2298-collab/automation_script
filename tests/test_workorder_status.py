from local_runtime.mock_mbo import MockMbo
from local_runtime.mock_service import MockService

from automation_scripts.workorder_status_script import (
    process_workorder_status
)


def test_completed_pm_sets_actual_finish():
    mbo = MockMbo(
        values={
            "WONUM": "1001",
            "WORKTYPE": "PM",
            "STATUS": "COMP",
            "ACTFINISH": None
        },
        modified_fields=["STATUS"]
    )

    service = MockService()

    result = process_workorder_status(
        mbo,
        service
    )

    assert result is True
    assert mbo.getDate("ACTFINISH") is not None
    assert len(mbo.set_history) == 1


def test_incomplete_pm_does_not_set_actual_finish():
    mbo = MockMbo(
        values={
            "WONUM": "1002",
            "WORKTYPE": "PM",
            "STATUS": "INPRG",
            "ACTFINISH": None
        },
        modified_fields=["STATUS"]
    )

    service = MockService()

    result = process_workorder_status(
        mbo,
        service
    )

    assert result is False
    assert mbo.getDate("ACTFINISH") is None


def test_completed_cm_does_not_set_actual_finish():
    mbo = MockMbo(
        values={
            "WONUM": "1003",
            "WORKTYPE": "CM",
            "STATUS": "COMP",
            "ACTFINISH": None
        },
        modified_fields=["STATUS"]
    )

    service = MockService()

    result = process_workorder_status(
        mbo,
        service
    )

    assert result is False
