"""Notification Aggregate Root."""

# Shared
from src.modules.shared.domain import AggregateRoot

# Build-ins
from typing import List
from uuid import UUID


class Notification(AggregateRoot):
    def __init__(
        self,
        id: UUID,
        user_email: int,
        subject: str,
        body: str,
        attachments: List[str]
    ):
        self.id = id
        self.user_email = user_email
        self.subject = subject
        self.body = body
        self.attachments = attachments

    @property
    def id(self) -> UUID:
        return self.__id

    @id.setter
    def id(self, id: UUID):
        self.__id = id

    @property
    def user_email(self) -> str:
        return self.__user_email

    @user_email.setter
    def user_email(self, user_email: str):
        self.__user_email = Email(user_email)

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def attachments(self):
        return self.__attachments

    @attachments.setter
    def attachments(self, attachments: List[str]):
        self.__attachments = attachments
