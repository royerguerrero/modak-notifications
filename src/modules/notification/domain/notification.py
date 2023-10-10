"""Notification Aggregate Root."""

# Local
from src.modules.notification.domain import NotificationId, NotificationTypes
from src.modules.notification.domain.business_rules import AttachmentMustBeValid, NotificationRateLimit

# Shared
from src.modules.shared.domain import AggregateRoot, Email, Base64File
from src.modules.shared.domain.business_rules import EmailMustBeValid

# Build-ins
from uuid import UUID
from datetime import datetime
from typing import List


class Notification(AggregateRoot):
    def __init__(
        self,
        id: UUID,
        user_email: int,
        subject: str,
        body: str,
        attachments: List[str],
        kind: NotificationTypes,
        sended_at: datetime = datetime.now(),
    ):
        self.id = id
        self.user_email = user_email
        self.subject = subject
        self.body = body
        self.attachments = attachments
        self.kind = kind
        self.sended_at = sended_at

    @property
    def id(self) -> UUID:
        return self._id.value

    @id.setter
    def id(self, id: UUID):
        self._id = NotificationId(id)

    @property
    def user_email(self) -> str:
        return self._user_email.value

    @user_email.setter
    def user_email(self, user_email: str):
        self.check_rule(EmailMustBeValid(user_email))
        self._user_email = Email(user_email)

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        self._subject = subject

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body: str):
        self._body = body

    @property
    def attachments(self) -> List[str]:
        return [attachment.value for attachment in self._attachments]

    @attachments.setter
    def attachments(self, attachments: List[str]):
        self._attachments = []

        for attachment in attachments:
            self.check_rule(AttachmentMustBeValid(attachment))
            self._attachments.append(Base64File(attachment))

    @property
    def kind(self) -> str:
        return self._kind.value

    @kind.setter
    def kind(self, kind: str):
        self._kind = NotificationTypes(kind)

    @property
    def sended_at(self) -> datetime:
        return self._sended_at

    @sended_at.setter
    def sended_at(self, sended_at: datetime):
        self._sended_at = sended_at

    def register(
        user_email: int,
        subject: str,
        body: str,
        kind: str,
        attachments: List[str] = [],
        previous_notifications: List['Notification'] = [],
        id: UUID = None,
    ):
        notification = Notification(
            id=id or Notification.next_id(),
            user_email=user_email,
            subject=subject,
            body=body,
            kind=kind,
            attachments=attachments
        )
        notification.check_rule(NotificationRateLimit(
            current_notification=notification,
            previous_notifications=previous_notifications
        ))
        return notification
