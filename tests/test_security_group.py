from local_runtime.mock_service import MockService

from automation_scripts.security_group_script import (
    is_user_supervisor
)


def test_supervisor_user():
    service = MockService({
        "SUPERVISOR": [
            "MAXADMIN",
            "SAGAR"
        ]
    })

    assert is_user_supervisor(
        service,
        "SAGAR"
    ) is True


def test_non_supervisor_user():
    service = MockService({
        "SUPERVISOR": [
            "MAXADMIN"
        ]
    })

    assert is_user_supervisor(
        service,
        "USER1"
    ) is False
