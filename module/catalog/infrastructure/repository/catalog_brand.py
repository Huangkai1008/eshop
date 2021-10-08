from module.catalog.domain.model import CatalogBrand
from seedwork.infrastructure.persistence.sqlalchemy import SQLAlchemyGenericRepository


class CatalogBrandRepository(SQLAlchemyGenericRepository[CatalogBrand, int]):
    model = CatalogBrand
