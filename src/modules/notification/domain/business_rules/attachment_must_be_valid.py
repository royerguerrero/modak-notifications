"""Attachment Must Be Valid Business Rule"""

# Shared
from src.modules.shared.domain import BusinessRule, Base64File

# Build-ins
from dataclasses import dataclass


@dataclass
class AttachmentMustBeValid(BusinessRule):
    """
    Business rule that checks if an attachment is valid.

    An attachment is considered valid if it can be decoded from base64.

    Attributes:
        value (str): The attachment value to be checked.
    """
    value: str

    def is_broken(self) -> bool:
        """
        Checks if the attachment is broken.

        Returns:
            bool: True if the attachment is broken, False otherwise.
        """
        try:
            base64_file = Base64File(self.value)
            return not base64_file.value == self.value
        except ValueError:
            return True
