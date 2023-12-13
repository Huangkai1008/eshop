from typing import Optional

from module.basket.domain import Basket, IBasketRepository
from seedwork.infrastructure.cache import CacheClient
from seedwork.infrastructure.logging import Logger
from seedwork.infrastructure.serialization.json import dumps as json_dumps
from seedwork.infrastructure.serialization.json import loads as json_loads


class BasketRepository(IBasketRepository):
    basket_key_prefix = 'basket'

    def __init__(self, logger: Logger, database: CacheClient) -> None:
        self._logger = logger
        self._database = database

    def get(self, buyer_id: str) -> Optional[Basket]:
        key = self._get_basket_key(buyer_id)
        basket: Optional[str] = self._database.get(key)
        if not basket:
            return None

        return Basket(json_loads(basket))

    def update(self, basket: Basket) -> Optional[Basket]:
        key = self._get_basket_key(basket.buyer_id)
        value = json_dumps(basket)
        self._database.set(key, value)
        return self.get(key)

    def delete(self, buyer_id: str) -> bool:
        key = self._get_basket_key(buyer_id)
        return self._database.delete(key)

    def _get_basket_key(self, buyer_id: str) -> str:
        return f'{self.basket_key_prefix}:{buyer_id}'
