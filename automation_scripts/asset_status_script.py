"""
Locally executable asset status processing script.
"""

from maximo_lib.asset_utils import normalize_asset_number
from maximo_lib.asset_utils import normalize_asset_status
from maximo_lib.validation import validate_asset


def process_asset(asset_number, status):
    """
    Validate and process an asset.
    """
    valid, message = validate_asset(asset_number, status)

    if not valid:
        return message

    clean_asset_number = normalize_asset_number(asset_number)
    clean_status = normalize_asset_status(status)

    return (
        "Asset "
        + clean_asset_number
        + " processed successfully with status "
        + clean_status
    )


if __name__ == "__main__":
    result = process_asset(" pump-100 ", "active")
    print(result)
