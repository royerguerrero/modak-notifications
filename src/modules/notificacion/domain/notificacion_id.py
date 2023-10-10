"""Notification ID Value Object"""

# Shared
from src.modules.shared.domain import ValueObject

# Build-ins
from uuid import UUID


class NotificationId(ValueObject):
    def __init__(self, value: UUID):
        self.value = value
