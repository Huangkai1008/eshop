from module.catalog.domain.model import Catalog, CatalogBrand, CatalogType
from module.catalog.infrastructure.repository.catalog import CatalogRepository
from module.catalog.infrastructure.repository.catalog_brand import (
    CatalogBrandRepository,
)
from module.catalog.infrastructure.repository.catalog_type import CatalogTypeRepository
from seedwork.application import GenericUseCase


class CatalogUseCase(GenericUseCase[Catalog, int]):
    def __init__(self, repository: CatalogRepository) -> None:
        super().__init__(repository)


class CatalogBrandUseCase(GenericUseCase[CatalogBrand, int]):
    def __init__(self, repository: CatalogBrandRepository) -> None:
        super().__init__(repository)


class CatalogTypeUseCase(GenericUseCase[CatalogType, int]):
    def __init__(self, repository: CatalogTypeRepository) -> None:
        super().__init__(repository)
