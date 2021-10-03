from typing import Generic, List, Optional, Tuple

from seedwork.domain.repository.generic import GenericRepository
from seedwork.domain.typings import ID, T


class GenericUseCase(Generic[T, ID]):
    def __init__(self, repository: GenericRepository) -> None:
        self._repo = repository

    def list(
        self, page: Optional[int] = None, size: Optional[int] = None, **kwargs: dict
    ) -> Tuple[List[T], int]:
        entities = self._repo.find_all(page=page, size=size, **kwargs)
        total = self._repo.get_count(**kwargs)
        return entities, total

    def create(self, entity: T) -> T:
        entity = self._repo.add(entity)
        return entity

    def update(self, entity: T) -> T:
        entity = self._repo.update(entity)
        return entity

    def delete(self, entity_id: ID) -> None:
        self._repo.delete(entity_id)
