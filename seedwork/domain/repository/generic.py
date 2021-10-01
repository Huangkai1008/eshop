from abc import ABCMeta

from seedwork.domain.typings import ID, T

from .crud import CRUDRepository
from .supports_paginate import SupportsPaginate


class GenericRepository(CRUDRepository[T, ID], SupportsPaginate[T], metaclass=ABCMeta):
    ...
