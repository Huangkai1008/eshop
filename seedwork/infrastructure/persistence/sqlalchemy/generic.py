from typing import ClassVar, List, Optional, Type

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session

from seedwork.domain import Entity
from seedwork.domain.repository.generic import GenericRepository
from seedwork.domain.typings import ID, T

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

    def find_all(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        **filters: dict,
    ) -> List[T]:
        filter_expressions = self._get_filter_expressions(**filters)
        query = select(self.model).where(*filter_expressions)
        if page and size:
            query = self._and_pagination(query, page, size)

        entities = self.session.scalars(query).all()
        return entities  # type: ignore

    def get_count(self, **filters: dict) -> int:
        filter_expressions = self._get_filter_expressions(**filters)
        total = self.session.scalar(
            select(func.count()).select_from(self.model).where(*filter_expressions)
        )
        assert total is not None
        return total

    def _get_filter_expressions(self, **kwargs: dict) -> list:
        return [getattr(self.model, k) == v for k, v in kwargs.items()]

    @classmethod
    def _and_pagination(cls, query: Select, page: int, size: int) -> Select:
        offset = (page - 1) * size
        return query.offset(offset).limit(size)
