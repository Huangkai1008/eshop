from sqlalchemy.orm import Mapped

from seedwork.infrastructure.persistence.sqlalchemy import DataEntity, str_field


class CatalogType(DataEntity):
    __tablename__ = 'catalog_type'

    name: Mapped[str_field]
