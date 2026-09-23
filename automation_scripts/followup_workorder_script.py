"""
Local simulation of a follow-up Work Order action script.
"""

from maximo_lib.workorder_rules import build_followup_description
from local_runtime.constants import MockMboConstants
from local_runtime.mock_mbo import MockMbo


def create_followup_workorder(source_mbo, workorder_set, service):
    """
    Create a simulated corrective follow-up work order.
    """
    source_wonum = source_mbo.getString("WONUM")
    description = source_mbo.getString("DESCRIPTION")
    site_id = source_mbo.getString("SITEID")
    org_id = source_mbo.getString("ORGID")

    followup = MockMbo()

    followup.setValue(
        "WORKTYPE",
        "CM",
        MockMboConstants.NOACCESSCHECK
    )

    followup.setValue(
        "DESCRIPTION",
        build_followup_description(description),
        MockMboConstants.NOACCESSCHECK
    )

    followup.setValue(
        "ORIGRECORDID",
        source_wonum,
        MockMboConstants.NOACCESSCHECK
    )

    if site_id:
        followup.setValue(
            "SITEID",
            site_id,
            MockMboConstants.NOACCESSCHECK
        )

    if org_id:
        followup.setValue(
            "ORGID",
            org_id,
            MockMboConstants.NOACCESSCHECK
        )

    workorder_set.add(followup)
    workorder_set.save()

    service.log(
        "Follow-up work order created for " + source_wonum
    )

    return followup
