from typing import Protocol

from modules.ordering.domain.model.order import Order

__all__ = ['IOrderRepository']


class IOrderRepository(Protocol):
    def add(self, order: Order) -> Order:
        ...

    def update(self, order: Order) -> Order:
        ...
