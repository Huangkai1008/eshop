from sqlalchemy import DECIMAL, Boolean, Column, Integer, String, Table
from sqlalchemy.orm import registry

from module.catalog.domain.model import Catalog

mapper_registry = registry()
metadata = mapper_registry.metadata

catalog = Table(
    'catalog',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('description', String(255)),
    Column('price', DECIMAL),
    Column('picture_file_name', String(255)),
    Column('picture_uri', String(255)),
    Column('catalog_type_id', Integer),
    Column('catalog_brand_id', Integer),
    Column('available_stock', Integer),
    Column('restock_threshold', Integer),
    Column('max_stock_threshold', Integer),
    Column('on_reorder', Boolean),
)


def start_mappers() -> None:
    mapper_registry.map_imperatively(Catalog, catalog)
