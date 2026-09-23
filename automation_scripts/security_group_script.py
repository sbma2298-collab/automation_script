"""
Local simulation of a Maximo security condition script.
"""


def is_user_supervisor(service, username):
    """
    Return True when the user belongs to the SUPERVISOR group.
    """
    return service.isUserInGroup(
        "SUPERVISOR",
        username
    )
