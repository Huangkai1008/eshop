from typing import Generic

from seedwork.domain.repository.crud import ID, CRUDRepository, T


class GenericUseCase(Generic[ID, T]):
    def __init__(self, repository: CRUDRepository) -> None:
        self._repo = repository

    def list(self, **kwargs) -> list[T]:
        return self._repo.list(**kwargs)

    def create(self, entity: T) -> T:
        entity = self._repo.add(entity)
        self._repo.commit()
        return entity

    def update(self, entity: T) -> T:
        entity = self._repo.update(entity)
        self._repo.commit()
        return entity

    def delete(self, entity_id: ID) -> None:
        self._repo.delete(entity_id)
        self._repo.commit()
