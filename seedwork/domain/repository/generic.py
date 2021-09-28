from abc import ABCMeta, abstractmethod
from typing import Generic, Optional, TypeVar

from seedwork.domain.entity import Entity, EntityId

__all__ = ['GenericRepository']

T = TypeVar('T', bound=Entity)


class GenericRepository(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def add(self, entity: T) -> T:
        """Add an entity.

        Returns:
            The added entity instance.

        """

    @abstractmethod
    def update(self, entity: T) -> Optional[T]:
        """Update and return an entity based on the given primary key identifier.

        Returns:
            The updated entity instance or `None` if not found.

        """

    @abstractmethod
    def delete(self, entity_id: EntityId) -> None:
        """Delete an entity.

        If the entity doesn't exist, do nothing.

        """

    @abstractmethod
    def commit(self) -> None:
        """Commit the current transaction.

        If the implementation isn't transactional, this method does nothing.

        """

    @abstractmethod
    def get(self, entity_id: EntityId) -> Optional[T]:
        """Get an entity based on the given primary key identifier.

        Returns:
            The entity instance or `None` if not found.

        """
