from abc import abstractmethod
from typing import Any, Generic, Optional

from seedwork.domain.typings import ID, T


class CRUDRepository(Generic[T, ID]):
    @abstractmethod
    def add(self, entity: T) -> T:
        """Add an entity.

        Returns:
            The added entity instance.

        """

    @abstractmethod
    def update(self, entity_id: ID, payload: dict[str, Any]) -> Optional[T]:
        """Partial update an entity based on the given primary key identifier.

        If the entity doesn't exist, do nothing.

        Returns:
            The updated entity instance.

        """

    @abstractmethod
    def delete(self, entity_id: ID) -> None:
        """Delete an entity.

        If the entity doesn't exist, do nothing.

        """

    @abstractmethod
    def get(self, entity_id: ID) -> Optional[T]:
        """Get an entity based on the given primary key identifier.

        Returns:
            The entity instance or `None` if not found.

        """
