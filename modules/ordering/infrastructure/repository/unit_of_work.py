from sqlalchemy.orm import Session
from typing_extensions import Self

from modules.ordering.infrastructure.repository.order import OrderRepository
from seedwork.infrastructure.persistence.sqlalchemy import SQLAlchemyUnitOfWork

__all__ = ['UnitOfWork']


class UnitOfWork(SQLAlchemyUnitOfWork):
    def __enter__(self) -> Self:
        self.session: Session = self.session_factory()
        self.orders = OrderRepository(self.session)
        return super().__enter__()
