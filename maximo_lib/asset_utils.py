
def normalize_asset_number(asset_number):

    if asset_number is None:
        return ""

    return asset_number.strip().upper()


def is_valid_asset_status(status):


    allowed_statuses = [
        "ACTIVE",
        "INACTIVE",
        "DECOMMISSIONED"
    ]

    return status in allowed_statuses


def create_asset_message(asset_number, status):

    clean_asset_number = normalize_asset_number(asset_number)

    return "Asset " + clean_asset_number + " has status " + status
