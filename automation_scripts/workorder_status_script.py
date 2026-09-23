"""
Local simulation of a WORKORDER object launch point.
"""

from maximo_lib.workorder_rules import should_set_actual_finish
from local_runtime.constants import MockMboConstants


def process_workorder_status(mbo, service):
    """
    Populate ACTFINISH when a PM work order becomes complete.
    """
    worktype = mbo.getString("WORKTYPE")
    status = mbo.getString("STATUS")
    status_modified = mbo.isModified("STATUS")
    actual_finish = mbo.getDate("ACTFINISH")

    should_update = should_set_actual_finish(
        worktype=worktype,
        status=status,
        status_modified=status_modified,
        actual_finish=actual_finish
    )

    if not should_update:
        service.log("ACTFINISH update was not required")
        return False

    mbo.setValue(
        "ACTFINISH",
        service.date(),
        MockMboConstants.NOACCESSCHECK
    )

    service.log(
        "ACTFINISH populated for completed PM work order "
        + mbo.getString("WONUM")
    )

    return True
