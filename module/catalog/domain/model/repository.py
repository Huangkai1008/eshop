from abc import ABCMeta

from seedwork.domain.repository.generic import GenericRepository


class ICatalogRepository(GenericRepository, metaclass=ABCMeta):
    ...
