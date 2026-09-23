"""
Simplified Maximo service simulation.
"""

from datetime import datetime, timezone


class MockService:
    def __init__(self, security_groups=None):
        self.logs = []
        self.security_groups = security_groups or {}

    def date(self):
        """
        Return the current UTC date and time.
        """
        return datetime.now(timezone.utc)

    def log(self, message):
        """
        Print and store a simulated Maximo log message.
        """
        clean_message = str(message)
        self.logs.append(clean_message)

        print("[MAXIMO LOG] " + clean_message)

    def error(self, message_group, message_key, parameters=None):
        """
        Simulate a Maximo application error.
        """
        message = str(message_group) + "." + str(message_key)

        if parameters:
            message += ": " + str(parameters)

        raise ValueError(message)

    def isUserInGroup(self, group_name, username):
        """
        Check local sample security group membership.
        """
        users = self.security_groups.get(group_name, [])

        return username in users
