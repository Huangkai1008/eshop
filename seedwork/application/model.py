from dataclasses import asdict
from typing import Annotated, Generic, TypeVar, Union

from pydantic import BaseModel as _BaseModel
from pydantic import PositiveInt
from typing_extensions import Self

from seedwork.domain import Entity

ItemT = TypeVar('ItemT')


class BaseModel(_BaseModel):
    @classmethod
    def from_entity(cls, entity: Entity) -> Self:
        return cls(**asdict(entity))


class QueryModel(BaseModel):
    page: Annotated[Union[PositiveInt, None], 'page number'] = 1
    size: Annotated[Union[PositiveInt, None], 'page size'] = 10


class PaginatedItemsViewModel(BaseModel, Generic[ItemT]):
    total: int
    items: list[ItemT]
