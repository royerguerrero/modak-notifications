# Pytest
import pytest

# Build-ins
from uuid import uuid4
from datetime import datetime, timedelta
import random

# Domain
from src.modules.notification.domain import Notification, NotificationTypes
from src.modules.shared.domain import BusinessRuleException


@pytest.mark.unit
@pytest.mark.parametrize(
    'user_email, subject, body, attachments',
    [
        (
            "engineer@modak.com",
            "Test Subject",
            "Test Body",
            []
        ),
        (
            "developer@modak.com",
            "Another Subject",
            "Another Body",
            ['dGhpcyBpcyBhIHRlc3Q=', 'dGhpcyBpcyBhIHRlc3QgdG8gd29ybGQ=']
        ),
        (
            "tester@modak.com",
            "Third Subject",
            "Third Body",
            ['dGhpcyBpcyBhIHRlc3QgdG8gd29ybGQgdGhpcyBpcyBhIHRlc3Q=']
        ),
    ])
def test_notification_creation(user_email, subject, body, attachments):
    id = uuid4()

    notification = Notification.register(
        id=id,
        user_email=user_email,
        subject=subject,
        body=body,
        attachments=attachments,
        kind=random.choice(list(NotificationTypes)).value,
    )

    assert notification.id == id
    assert notification.user_email == user_email
    assert notification.subject == subject
    assert notification.body == body
    assert notification.attachments == attachments


@pytest.mark.unit
def test_notification_status_rate_limit():
    with pytest.raises(BusinessRuleException):
        notification = Notification.register(
            id=Notification.next_id(),
            user_email='developer@modak.com',
            subject='Rate Limit Exercise',
            body='Test Body',
            kind=NotificationTypes.STATUS.value,
            previous_notifications=[
                Notification(
                    id=Notification.next_id(),
                    user_email='test@modak.com',
                    subject='Test Subject',
                    body='Test Body',
                    kind=NotificationTypes.STATUS.value,
                    attachments=[],
                    sended_at=datetime.now() - timedelta(seconds=15)
                ),
                Notification(
                    id=Notification.next_id(),
                    user_email='test@modak.com',
                    subject='Test Subject',
                    body='Test Body',
                    kind=NotificationTypes.STATUS.value,
                    attachments=[],
                    sended_at=datetime.now() - timedelta(seconds=10)
                ),
            ]
        )


@pytest.mark.unit
def test_notification_news_rate_limit():
    with pytest.raises(BusinessRuleException):
        notification = Notification.register(
            id=Notification.next_id(),
            user_email='developer@modak.com',
            subject='Rate Limit Exercise',
            body='Test Body',
            kind=NotificationTypes.NEWS.value,
            previous_notifications=[
                Notification(
                    id=Notification.next_id(),
                    user_email='test@modak.com',
                    subject='Test Subject',
                    body='Test Body',
                    kind=NotificationTypes.NEWS.value,
                    attachments=[],
                    sended_at=datetime.now() - timedelta(hours=23)
                ),
            ]
        )


@pytest.mark.unit
def test_notification_marketing_rate_limit():
    with pytest.raises(BusinessRuleException):
        notification = Notification.register(
            id=Notification.next_id(),
            user_email='developer@modak.com',
            subject='Rate Limit Exercise',
            body='Test Body',
            kind=NotificationTypes.MARKETING.value,
            previous_notifications=[
                Notification(
                    id=Notification.next_id(),
                    user_email='test@modak.com',
                    subject='Test Subject',
                    body='Test Body',
                    kind=NotificationTypes.MARKETING.value,
                    attachments=[],
                    sended_at=datetime.now() - timedelta(minutes=30)
                ),
                Notification(
                    id=Notification.next_id(),
                    user_email='test@modak.com',
                    subject='Test Subject',
                    body='Test Body',
                    kind=NotificationTypes.MARKETING.value,
                    attachments=[],
                    sended_at=datetime.now() - timedelta(seconds=10)
                ),
                Notification(
                    id=Notification.next_id(),
                    user_email='test@modak.com',
                    subject='Test Subject',
                    body='Test Body',
                    kind=NotificationTypes.MARKETING.value,
                    attachments=[],
                    sended_at=datetime.now() - timedelta(seconds=10)
                ),
            ]
        )


@pytest.mark.unit
def test_invalid_email():
    with pytest.raises(BusinessRuleException):
        Notification.register(
            id=uuid4(),
            user_email='invalid_email',
            subject='Test Subject',
            body='Test Body',
            attachments=[],
            kind=random.choice(list(NotificationTypes)).value,
        )


@pytest.mark.unit
def test_invalid_attachment():
    with pytest.raises(BusinessRuleException):
        Notification.register(
            id=uuid4(),
            user_email='test@example.com',
            subject='Test Subject',
            body='Test Body',
            attachments=['invalid_base64'],
            kind=random.choice(list(NotificationTypes)).value,
        )
