from typing import Protocol

from eshop.ordering.domain.model.order import Order

__all__ = ['IOrderRepository']


class IOrderRepository(Protocol):
    def add(self, order: Order) -> Order:
        ...

    def update(self, order: Order) -> Order:
        ...
