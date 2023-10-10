"""Email value object"""

# Shred
from src.modules.shared.domain import ValueObject


class Email(ValueObject):
    def __init__(self, value: str):
        self.value = value
