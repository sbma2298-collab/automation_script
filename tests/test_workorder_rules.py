from maximo_lib.workorder_rules import should_set_actual_finish
from maximo_lib.workorder_rules import get_default_priority
from maximo_lib.workorder_rules import build_followup_description


def test_completed_pm_requires_actual_finish():
    result = should_set_actual_finish(
        worktype="PM",
        status="COMP",
        status_modified=True,
        actual_finish=None
    )

    assert result is True


def test_completed_cm_does_not_require_actual_finish():
    result = should_set_actual_finish(
        worktype="CM",
        status="COMP",
        status_modified=True,
        actual_finish=None
    )

    assert result is False


def test_existing_actual_finish_is_not_overwritten():
    result = should_set_actual_finish(
        worktype="PM",
        status="COMP",
        status_modified=True,
        actual_finish="EXISTING DATE"
    )

    assert result is False


def test_emergency_priority():
    assert get_default_priority("EM") == 1


def test_corrective_priority():
    assert get_default_priority("CM") == 3


def test_preventive_priority():
    assert get_default_priority("PM") == 4


def test_default_priority():
    assert get_default_priority("OTHER") == 5


def test_followup_description():
    result = build_followup_description(
        "Repair leaking pump"
    )

    assert result == "Follow-up: Repair leaking pump"
