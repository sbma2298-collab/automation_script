from automation_scripts.asset_status_script import process_asset
from maximo_lib.asset_utils import normalize_asset_number
from maximo_lib.asset_utils import is_valid_asset_status
from maximo_lib.validation import validate_asset


def test_normalize_asset_number():
    assert normalize_asset_number(" pump-100 ") == "PUMP-100"


def test_normalize_none_asset_number():
    assert normalize_asset_number(None) == ""


def test_valid_asset_status():
    assert is_valid_asset_status("active") is True


def test_invalid_asset_status():
    assert is_valid_asset_status("UNKNOWN") is False


def test_validate_asset_success():
    valid, message = validate_asset(
        "pump-100",
        "ACTIVE"
    )

    assert valid is True
    assert message == "Asset is valid"


def test_asset_number_is_required():
    valid, message = validate_asset(
        "",
        "ACTIVE"
    )

    assert valid is False
    assert message == "Asset number is required"


def test_process_asset_success():
    result = process_asset(
        " pump-100 ",
        "active"
    )

    assert result == (
        "Asset PUMP-100 processed successfully with status ACTIVE"
    )


def test_process_asset_invalid_status():
    result = process_asset(
        "pump-100",
        "UNKNOWN"
    )

    assert result == "Invalid asset status: UNKNOWN"
