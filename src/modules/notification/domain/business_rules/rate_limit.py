"""Rate limit business rules"""

# Local
from src.modules.notification.domain import NotificationTypes

# Shared
from src.modules.shared.domain import BusinessRule, Entity

# Build-ins
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Type


@dataclass
class NotificationRateLimit(BusinessRule):
    current_notification: Type[Entity]
    previous_notifications: List[Type[Entity]]

    def is_broken(self) -> bool:
        notification_limits = {
            NotificationTypes.STATUS: {
                'time_limit': 2,
                'max_notifications': 2
            },
            NotificationTypes.NEWS: {
                'time_limit': 24,
                'max_notifications': 1
            },
            NotificationTypes.MARKETING: {
                'time_limit': 3,
                'max_notifications': 3
            },
        }

        if self.current_notification._kind not in notification_limits:
            return False

        previous_notifications = [
            notification
            for notification in self.previous_notifications
            if notification.kind == self.current_notification.kind
        ]
        now = datetime.now()

        last_notifications = [
            notification
            for notification in previous_notifications
            if notification.sended_at > now - timedelta(hours=notification_limits[self.current_notification._kind]['time_limit'])
        ]

        if len(last_notifications) >= notification_limits[self.current_notification._kind]['max_notifications']:
            return True

        return False
