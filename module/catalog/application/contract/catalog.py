from decimal import Decimal

from seedwork.application import BaseModel, QueryModel


class CatalogModel(BaseModel):
    name: str
    description: str
    price: Decimal
    picture_file_name: str
    picture_uri: str
    catalog_type_id: int
    catalog_brand_id: int
    available_stock: int
    restock_threshold: int
    max_stock_threshold: int
    on_reorder: bool


class CatalogViewModel(CatalogModel):
    id: int


class CatalogQuery(QueryModel):
    ...


class CatalogCreate(CatalogModel):
    ...
