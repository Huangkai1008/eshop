from typing import Protocol, Sequence, Tuple

from seedwork.domain.typings import ID, T


class Paginator(Protocol[T, ID]):
    def list(self, page: int, size: int) -> Tuple[Sequence[T], int]:
        """Query entities with pagination.

        Args:
            page: The page number.
            size: The page size.

        Returns:
            A tuple of entities and the total count of entities.

        """
