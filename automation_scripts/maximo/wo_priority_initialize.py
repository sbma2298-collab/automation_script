# MAXIMO DEPLOYMENT SCRIPT
#
# Launch point type: Attribute
# Object: WORKORDER
# Attribute: WOPRIORITY
# Event: Initialize Value

worktype = mbo.getString("WORKTYPE")

if worktype:
    worktype = worktype.strip().upper()

if worktype == "EM":
    thisvalue = 1
elif worktype == "CM":
    thisvalue = 3
elif worktype == "PM":
    thisvalue = 4
else:
    thisvalue = 5
