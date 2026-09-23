# MAXIMO DEPLOYMENT SCRIPT
#
# Script type: Condition
#
# The service method signature must be verified in the target
# Maximo version.

user_info = mbo.getUserInfo()
username = user_info.getUserName()

retVal = service.isUserInGroup(
    "SUPERVISOR",
    username
)
