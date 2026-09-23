"""
Reusable asset validation functions.
"""

from maximo_lib.asset_utils import normalize_asset_number
from maximo_lib.asset_utils import normalize_asset_status
from maximo_lib.asset_utils import is_valid_asset_status


def validate_asset(asset_number, status):
    """
    Validate an asset number and asset status.

    Returns:
        tuple: Boolean result and validation message
    """
    clean_asset_number = normalize_asset_number(asset_number)
    clean_status = normalize_asset_status(status)

    if clean_asset_number == "":
        return False, "Asset number is required"

    if clean_status == "":
        return False, "Asset status is required"

    if not is_valid_asset_status(clean_status):
        return False, "Invalid asset status: " + clean_status

    return True, "Asset is valid"
