"""Abstract Repository"""

# Build-ins
from abc import ABC, abstractmethod
from typing import List, Type, Union

# Local
from src.modules.shared.domain import Entity


class AbstractRepository(ABC):
    """
    Abstract class that defines the methods that a repository should implement.
    """
    entity: Type[Entity]

    @abstractmethod
    def add(self, entity: Type[Entity]):
        """
        Adds an entity to the repository.

        :param entity: The entity to be added.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, entity: Type[Entity]):
        """
        Removes an entity from the repository.

        :param entity: The entity to be removed.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, entity_id) -> Union[Type[Entity], None]:
        """
        Returns an entity from the repository by its ID.

        :param entity_id: The ID of the entity to be returned.
        :return: The entity with the given ID, or None if it doesn't exist.
        """
        raise NotImplementedError

    @abstractmethod
    def all(self) -> Union[List[Type[Entity]], None]:
        """
        Returns all entities from the repository.

        :return: A list with all the entities in the repository, or None if there are no entities.
        """
        raise NotImplementedError
