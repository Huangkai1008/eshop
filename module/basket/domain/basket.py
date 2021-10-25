from dataclasses import dataclass, field

from seedwork.domain import AggregateRoot

from .basket_item import BasketItem


@dataclass
class Basket(AggregateRoot):
    buyer_id: str
    items: list[BasketItem] = field(default_factory=list)
