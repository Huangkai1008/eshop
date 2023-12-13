from dataclasses import dataclass
from decimal import Decimal

from seedwork.domain import Entity

from .exception import BasketDomainException


@dataclass
class BasketItem(Entity):
    product_id: int
    product_name: str
    unit_price: Decimal
    old_unit_price: Decimal
    quantity: int
    picture_url: str

    def __post_init__(self) -> None:
        self._quantity_should_greater_than_zero()

    def _quantity_should_greater_than_zero(self) -> None:
        if self.quantity <= 0:
            raise BasketDomainException('Invalid number of quantity')
