"""
Pure Work Order business rules.

These functions do not use Maximo classes. They can therefore
be tested in Google Colab before production deployment.
"""

WORKTYPE_PM = "PM"
WORKTYPE_EM = "EM"
WORKTYPE_CM = "CM"

STATUS_COMPLETE = "COMP"


def normalize_code(value):
    """
    Normalize a status, work type, or domain value.
    """
    if value is None:
        return ""

    return str(value).strip().upper()


def should_set_actual_finish(
    worktype,
    status,
    status_modified,
    actual_finish=None
):
    """
    Determine whether ACTFINISH should be populated.
    """
    clean_worktype = normalize_code(worktype)
    clean_status = normalize_code(status)

    return (
        clean_worktype == WORKTYPE_PM
        and clean_status == STATUS_COMPLETE
        and status_modified is True
        and actual_finish is None
    )


def get_default_priority(worktype):
    """
    Return the default priority based on work type.
    """
    clean_worktype = normalize_code(worktype)

    if clean_worktype == WORKTYPE_EM:
        return 1

    if clean_worktype == WORKTYPE_CM:
        return 3

    if clean_worktype == WORKTYPE_PM:
        return 4

    return 5


def build_followup_description(description):
    """
    Build a follow-up work order description.
    """
    if description is None:
        description = ""

    clean_description = str(description).strip()

    if clean_description == "":
        return "Follow-up work order"

    return "Follow-up: " + clean_description
