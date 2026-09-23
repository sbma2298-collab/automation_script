"""
Local simulation of a WOPRIORITY attribute launch point.
"""

from maximo_lib.workorder_rules import get_default_priority


def initialize_workorder_priority(mbo, service=None):
    """
    Return the default priority based on WORKTYPE.
    """
    worktype = mbo.getString("WORKTYPE")
    priority = get_default_priority(worktype)

    if service is not None:
        service.log(
            "Priority "
            + str(priority)
            + " selected for work type "
            + worktype
        )

    return priority
