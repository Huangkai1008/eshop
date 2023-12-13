from abc import abstractmethod
from typing import Optional, Protocol

from .basket import Basket


class IBasketRepository(Protocol):
    @abstractmethod
    def get(self, buyer_id: str) -> Optional[Basket]:
        """Get basket by buyer id.

        Args:
            buyer_id: Buyer id.

        """

    @abstractmethod
    def update(self, basket: Basket) -> Optional[Basket]:
        """Update a basket and return it.

        Args:
            basket: Basket.

        """

    @abstractmethod
    def delete(self, buyer_id: str) -> bool:
        """Delete a basket by buyer Id.

        If the basket doesn't exist, ignore it.

        Args:
            buyer_id: Buyer Id.

        Returns:
            Whether the basket is deleted.

        """
