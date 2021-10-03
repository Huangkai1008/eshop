from module.catalog.domain.model import Catalog
from module.catalog.domain.model.repository import ICatalogRepository
from seedwork.application import GenericUseCase


class CatalogUseCase(GenericUseCase[Catalog, int]):
    def __init__(self, repository: ICatalogRepository) -> None:
        super().__init__(repository)
