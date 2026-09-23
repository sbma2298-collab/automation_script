"""
Simplified Maximo MboSet simulation.
"""


class MockMboSet:
    def __init__(self, records=None):
        self.records = list(records or [])
        self.current_position = -1
        self.saved = False
        self.cleaned_up = False
        self.closed = False

    def count(self):
        return len(self.records)

    def isEmpty(self):
        return len(self.records) == 0

    def moveFirst(self):
        if self.isEmpty():
            self.current_position = -1
            return None

        self.current_position = 0
        return self.records[0]

    def moveNext(self):
        next_position = self.current_position + 1

        if next_position >= len(self.records):
            return None

        self.current_position = next_position
        return self.records[next_position]

    def add(self, mbo):
        self.records.append(mbo)
        return mbo

    def save(self):
        self.saved = True
        return True

    def cleanup(self):
        self.cleaned_up = True

    def close(self):
        self.closed = True
