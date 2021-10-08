from sqlalchemy.orm import Mapped

from seedwork.infrastructure.persistence.sqlalchemy import DataEntity, str_field


class CatalogBrand(DataEntity):
    __tablename__ = 'catalog_brand'

    brand: Mapped[str_field]
