"""Email Must Be Valid Business Rule"""

# Shared
from src.modules.shared.domain import BusinessRule, Email

# Build-ins
from dataclasses import dataclass


@dataclass
class EmailMustBeValid(BusinessRule):
    """
    Business rule that checks if an email is valid.
    """
    value: str

    def is_broken(self) -> bool:
        """
        Checks if the email is valid.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        try:
            email = Email(self.value)
            return not email.value == self.value
        except ValueError:
            return True
