"""
Simplified Maximo MBO constants for local learning.

These values are simulation values only. Production Maximo scripts
must use psdi.mbo.MboConstants.
"""


class MockMboConstants:
    NONE = 0
    NOVALIDATION = 1
    NOACCESSCHECK = 2
    DELAYVALIDATIONONLY = 4
    NOACTION = 8
    NOVALIDATION_AND_NOACTION = 9
