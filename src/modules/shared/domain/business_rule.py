"""Business Rule"""

# Build-ins
from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class BusinessRule(ABC):
    """
    Abstract base class for defining business rules.
    """

    @abstractmethod
    def is_broken(self) -> bool:
        """
        Check if the business rule is broken.

        Returns:
            bool: True if the business rule is broken, False otherwise.
        """
        raise NotImplementedError
