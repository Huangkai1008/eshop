from module.catalog.domain.model import Catalog
from seedwork.application import GenericUseCase


class CatalogUseCase(GenericUseCase[int, Catalog]):
    ...
