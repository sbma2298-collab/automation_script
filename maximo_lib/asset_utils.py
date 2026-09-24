"""
Reusable asset business logic.

This file contains pure Python functions that can be tested
without connecting to Maximo.
"""

ALLOWED_ASSET_STATUSES = (
    "ACTIVE",
    "INACTIVE",
    "DECOMMISSIONED"
)


def normalize_asset_number(asset_number):
    """
    Convert an asset number to trimmed uppercase text.

    Example:
        " pump-100 " becomes "PUMP-100"
    """
    if asset_number is None:
        return ""

    return str(asset_number).strip().upper()


def normalize_asset_status(status):
    """
    Convert an asset status to trimmed uppercase text.
    """
    if status is None:
        return ""

    return str(status).strip().upper()


def is_valid_asset_status(status):
    """
    Check whether the status is in the allowed status list.
    """
    clean_status = normalize_asset_status(status)

    return clean_status in ALLOWED_ASSET_STATUSES


def create_asset_message(asset_number, status):
    """
    Create a standardized asset status message.
    """
    clean_asset_number = normalize_asset_number(asset_number)
    clean_status = normalize_asset_status(status)

    return (
        "Asset "
        + clean_asset_number
        + " has status "
        + clean_status
    )
