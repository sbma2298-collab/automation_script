from local_runtime.mock_mbo import MockMbo
from local_runtime.mock_mboset import MockMboSet
from local_runtime.mock_service import MockService

from automation_scripts.followup_workorder_script import (
    create_followup_workorder
)


def test_followup_workorder_creation():
    source = MockMbo({
        "WONUM": "1005",
        "DESCRIPTION": "Inspect leaking pump",
        "SITEID": "BEDFORD",
        "ORGID": "EAGLENA"
    })

    workorder_set = MockMboSet()
    service = MockService()

    followup = create_followup_workorder(
        source_mbo=source,
        workorder_set=workorder_set,
        service=service
    )

    assert followup.getString("WORKTYPE") == "CM"

    assert followup.getString("DESCRIPTION") == (
        "Follow-up: Inspect leaking pump"
    )

    assert followup.getString("ORIGRECORDID") == "1005"
    assert followup.getString("SITEID") == "BEDFORD"
    assert followup.getString("ORGID") == "EAGLENA"
    assert workorder_set.count() == 1
    assert workorder_set.saved is True
