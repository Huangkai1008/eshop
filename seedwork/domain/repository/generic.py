from typing import Protocol

from seedwork.domain.typings import T, ID

from .crud import CRUDRepository
from .paginator import Paginator


class GenericRepository(CRUDRepository[T, ID], Paginator[T, ID], Protocol):
    ...
