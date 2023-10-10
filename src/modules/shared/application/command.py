"""Shared command stuffs"""

# Build-ins
from abc import ABC
from typing import Dict, Any, Type
from dataclasses import dataclass, field


class Command(ABC):
    """Abstract base class for the commands"""


@dataclass
class CommandResponse:
    """Represents the response of a command execution"""

    entity_id: Any = None
    dto: Type[Command] = None
    extra_data: Dict[str, Any] = field(default_factory=dict)
    errors: Dict[str, Any] = field(default_factory=dict)

    @property
    def has_errors(self) -> bool:
        """
        Returns True if there are any errors in the response, False otherwise.
        """
        return len(self.errors) > 0
