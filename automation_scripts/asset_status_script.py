
from maximo_lib.asset_utils import normalize_asset_number
from maximo_lib_asset_utils import validate_asset

def process_asset(asset_number,status):
  valid, message = validate_asset(asset_number,status)

  if not valid :
    return message
  clean_asset_number = normalize_asset_number(asset_number)
  return "Asset " + clean_asset_number + "processed sucessfully"
