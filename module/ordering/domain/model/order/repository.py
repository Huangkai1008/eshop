from abc import abstractmethod
from typing import Protocol

from module.ordering.domain.model.order import Order

__all__ = ['IOrderRepository']


class IOrderRepository(Protocol):
    @abstractmethod
    def add(self, order: Order) -> Order:
        ...

    @abstractmethod
    def update(self, order: Order) -> Order:
        ...
