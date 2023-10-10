"""Email value object"""

# Shared
from src.modules.shared.domain import ValueObject

# Build-ins
import re


class Email(ValueObject):
    def __init__(self, value: str):
        if not self._is_valid_email(value):
            raise ValueError('Invalid email address')
        self.value = value

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Email):
            return False
        return self.value == other.value
