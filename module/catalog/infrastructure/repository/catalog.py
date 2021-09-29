from module.catalog.domain.model.catalog import Catalog
from seedwork.infrastructure.persistence.sqlalchemy import SQLAlchemyGenericRepository

__all__ = ['CatalogRepository']


class CatalogRepository(SQLAlchemyGenericRepository[Catalog]):
    ...
