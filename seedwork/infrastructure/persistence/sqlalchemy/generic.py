from typing import ClassVar, Optional, Type

from sqlalchemy.orm import Session

from seedwork.domain import Entity
from seedwork.domain.typings import T, ID
from seedwork.domain.repository.generic import GenericRepository

__all__ = ['SQLAlchemyGenericRepository']


class SQLAlchemyGenericRepository(GenericRepository[T, ID]):
    model: ClassVar[Type[Entity]]

    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def add(self, entity: T) -> T:
        self.session.add(entity)
        return entity

    def update(self, entity: T) -> T:
        self.session.add(entity)
        return entity

    def delete(self, entity_id: ID) -> None:
        entity = self.get(entity_id)
        if entity:
            self.session.delete(entity)

    def commit(self) -> None:
        self.session.commit()

    def get(self, entity_id: ID) -> Optional[T]:
        return self.session.get(self.model, entity_id)  # type: ignore
