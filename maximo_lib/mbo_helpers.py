"""
Reusable helper functions for MBO-style objects.

These functions work with local MockMbo objects and can later
be adapted for Maximo deployment.
"""


def get_string(mbo, attribute, default_value=""):
    """
    Safely retrieve a string value from an MBO.
    """
    value = mbo.getString(attribute)

    if value is None or value == "":
        return default_value

    return value


def get_integer(mbo, attribute, default_value=0):
    """
    Safely retrieve an integer value from an MBO.
    """
    try:
        return mbo.getInt(attribute)
    except (TypeError, ValueError):
        return default_value


def set_value(mbo, attribute, value, flags=0):
    """
    Set a value and return the updated value.
    """
    mbo.setValue(attribute, value, flags)

    return value
