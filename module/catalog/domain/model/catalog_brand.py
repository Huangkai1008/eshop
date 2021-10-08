from sqlalchemy.orm import Mapped

from seedwork.infrastructure.persistence.sqlalchemy import DataEntity, str_field


class CatalogBrand(DataEntity):
    __tablename__ = 'catalog_brand'

    name: Mapped[str_field]
