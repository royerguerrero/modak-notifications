"""Base64 File Value Object"""

# Shared
from src.modules.shared.domain import ValueObject

# Build-ins
import base64


class Base64File(ValueObject):
    def __init__(self, value: str):
        if not self.is_base64(value):
            raise ValueError("Invalid base64 value")
        self.value = value

    @classmethod
    def from_bytes(cls, bytes_: bytes):
        value = base64.b64encode(bytes_).decode('utf-8')
        return cls(value)

    def to_bytes(self) -> bytes:
        return base64.b64decode(self.value.encode('utf-8'))

    @staticmethod
    def is_base64(s: str) -> bool:
        try:
            return base64.b64encode(base64.b64decode(s)) == s.encode()
        except Exception:
            return False
