from typing import Optional, Protocol

from .basket import Basket


class IBasketRepository(Protocol):
    def get(self, buyer_id: str) -> Optional[Basket]:
        """Get basket by buyer id.

        Args:
            buyer_id: Buyer id.

        """

    def update(self, basket: Basket) -> Optional[Basket]:
        """Update a basket and return it.

        Args:
            basket: Basket.

        """

    def delete(self, basket_id: str) -> bool:
        """Delete a basket by id.

        If the basket doesn't exist, ignore it.

        Args:
            basket_id: Basket id.

        Returns:
            Whether the basket is deleted.

        """
