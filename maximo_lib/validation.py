
from maximo_lib.asset_utils import normalize_asset_number
from maximo_lib.asset_utils import is_valid_asset_status


def validate_asset(asset_number, status):

    clean_asset_number = normalize_asset_number(asset_number)

    if clean_asset_number == "":
        return False, "Asset number is required"

    if not is_valid_asset_status(status):
        return False, "Invalid asset status"

    return True, "Asset is valid"
