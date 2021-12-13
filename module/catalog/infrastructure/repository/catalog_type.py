from module.catalog.domain import CatalogType
from seedwork.infrastructure.persistence.sqlalchemy import SQLAlchemyGenericRepository

__all__ = ['CatalogTypeRepository']


class CatalogTypeRepository(SQLAlchemyGenericRepository[CatalogType, int]):
    model = CatalogType
