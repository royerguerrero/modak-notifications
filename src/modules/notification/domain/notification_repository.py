"""Notification Abstract Repository"""

# Local
from src.modules.notification.domain import Notification

# Shared
from src.modules.shared.domain import AbstractRepository


class NotificationRepository(AbstractRepository):
    """Interface for notification repository"""
    entity = Notification
