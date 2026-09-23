"""
Simplified Maximo Business Object simulation.

This class only implements methods needed by the sample scripts.
It is not a replacement for the real Maximo MBO framework.
"""


class MockMbo:
    def __init__(self, values=None, modified_fields=None):
        self.values = dict(values or {})
        self.modified_fields = set(modified_fields or [])
        self.set_history = []

    def getString(self, attribute):
        value = self.values.get(attribute)

        if value is None:
            return ""

        return str(value)

    def getInt(self, attribute):
        value = self.values.get(attribute)

        if value is None or value == "":
            return 0

        return int(value)

    def getDate(self, attribute):
        return self.values.get(attribute)

    def getBoolean(self, attribute):
        return bool(self.values.get(attribute, False))

    def isNull(self, attribute):
        return self.values.get(attribute) is None

    def isModified(self, attribute=None):
        if attribute is None:
            return len(self.modified_fields) > 0

        return attribute in self.modified_fields

    def setValue(self, attribute, value, flags=0):
        old_value = self.values.get(attribute)

        self.values[attribute] = value
        self.modified_fields.add(attribute)

        self.set_history.append({
            "attribute": attribute,
            "old_value": old_value,
            "new_value": value,
            "flags": flags
        })

    def to_dict(self):
        return dict(self.values)
