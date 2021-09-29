from sqlalchemy import DECIMAL, Boolean, Column, Integer, String, Table
from sqlalchemy.orm import registry

mapper_registry = registry()

catalog = Table(
    'catalog',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('description', String),
    Column('price', DECIMAL),
    Column('picture_file_name', String),
    Column('picture_uri', String),
    Column('catalog_type_id', Integer),
    Column('catalog_brand_id', Integer),
    Column('available_stock', Integer),
    Column('restock_threshold', Integer),
    Column('max_stock_threshold', Integer),
    Column('on_reorder', Boolean),
)
