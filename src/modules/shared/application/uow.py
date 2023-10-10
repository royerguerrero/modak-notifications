"""Abstract Unit Of Work"""

# Build-ins
from abc import ABC, abstractclassmethod


class AbstractUnitOfWork(ABC):
    """Abstract Unit Of Work"""

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractclassmethod
    def commit(self):
        raise NotImplementedError

    @abstractclassmethod
    def rollback(self):
        raise NotImplementedError
