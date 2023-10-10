"""Query Shared"""

# Build-ins
from dataclasses import dataclass, field
from typing import Type, Any, Dict

# Local
from src.modules.shared.application.uow import AbstractUnitOfWork


class Query:
    """Query Abstract"""

    def as_dict(self):
        """Return the data as a dict"""
        return self.__dict__


@dataclass
class QueryResponse:
    """Query Response"""

    dto: Type[Query] = None
    extra_data: Dict[str, Any] = field(default_factory=dict)
    errors: Dict[str, Any] = field(default_factory=dict)

    @property
    def has_errors(self) -> bool:
        """
        Returns True if there are any errors in the response, False otherwise.
        """
        return len(self.errors) > 0
