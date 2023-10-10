"""Send notification command."""

# Shared
from src.modules.shared.application import Command, AbstractUnitOfWork

# Build-ins
from dataclasses import dataclass
from typing import List


@dataclass
class SendNotificationCommand(Command):
    email: str
    subject: str
    body: str
    attachments: List[str]


def send_notification(
    command: SendNotificationCommand,
    uow: AbstractUnitOfWork,
):
    with uow:
        previous_notifications = uow.notification_repository.find_by_email(
            email=command.email
        )
