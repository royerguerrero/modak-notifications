"""Test email value object"""

# Domain
from src.modules.shared.domain import Email

# Testing
import pytest


@pytest.mark.unit
def test_valid_email():
    email = Email('engineer@modak.com')
    assert email.value == 'engineer@modak.com'


@pytest.mark.unit
def test_invalid_email():
    with pytest.raises(ValueError):
        Email('invalid_email')


@pytest.mark.unit
def test_equality():
    email1 = Email('engineer@modak.com')
    email2 = Email('engineer@modak.com')
    email3 = Email('marketing@modak.com')
    assert email1 == email2
    assert email1 != email3
