from sqlalchemy.orm import Session

from modules.ordering.domain.model.order import IOrderRepository, Order

__all__ = ['OrderRepository']


class OrderRepository(IOrderRepository):
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def add(self, order: Order) -> Order:
        self.session.add(order)
        return order

    def update(self, order: Order) -> Order:
        self.session.add(order)
        return order
