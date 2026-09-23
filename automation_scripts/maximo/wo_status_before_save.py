# MAXIMO DEPLOYMENT SCRIPT
#
# Launch point type: Object
# Object: WORKORDER
# Event: Before Save
#
# This file requires the Maximo runtime.

from psdi.mbo import MboConstants
from psdi.server import MXServer

worktype = mbo.getString("WORKTYPE")
status = mbo.getString("STATUS")
status_modified = mbo.isModified("STATUS")
actual_finish = mbo.getDate("ACTFINISH")

if (
    worktype == "PM"
    and status == "COMP"
    and status_modified
    and actual_finish is None
):
    server_date = MXServer.getMXServer().getDate()

    mbo.setValue(
        "ACTFINISH",
        server_date,
        MboConstants.NOACCESSCHECK
    )

    service.log(
        "ACTFINISH populated for work order "
        + mbo.getString("WONUM")
    )
