from abc import abstractmethod
from typing import Optional

from module.basket.domain import Basket, IBasketRepository


class BasketRepository(IBasketRepository):
    def get(self, buyer_id: str) -> Optional[Basket]:
        pass

    def update(self, basket: Basket) -> Optional[Basket]:
        pass

    @abstractmethod
    def delete(self, basket_id: str) -> bool:
        pass
