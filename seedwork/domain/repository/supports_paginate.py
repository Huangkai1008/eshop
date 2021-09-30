from abc import abstractmethod
from typing import List, Optional, Protocol, runtime_checkable

from seedwork.domain.typings import T


@runtime_checkable
class SupportsPaginate(Protocol[T]):
    @abstractmethod
    def find_all(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        **filters: dict,
    ) -> List[T]:
        """Query entities with pagination.

        Args:
            page: The page number.
            size: The page size.
            filters: The query filters.

        Returns:
            The entities.

        """

    @abstractmethod
    def get_count(self, **filters: dict) -> int:
        """Get the total count of entities.

        Args:
            filters: The query filters.

        Returns:
            The total count.

        """
