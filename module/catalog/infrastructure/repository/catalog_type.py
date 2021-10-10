from module.catalog.domain.catalog_type import CatalogType
from seedwork.infrastructure.persistence.sqlalchemy import SQLAlchemyGenericRepository

__all__ = ['CatalogTypeRepository']


class CatalogTypeRepository(SQLAlchemyGenericRepository[CatalogType, int]):
    model = CatalogType
