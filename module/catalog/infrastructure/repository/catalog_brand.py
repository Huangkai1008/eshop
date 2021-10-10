from module.catalog.domain import CatalogBrand
from seedwork.infrastructure.persistence.sqlalchemy import SQLAlchemyGenericRepository


class CatalogBrandRepository(SQLAlchemyGenericRepository[CatalogBrand, int]):
    model = CatalogBrand
