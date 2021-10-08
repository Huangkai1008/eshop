from decimal import Decimal
from typing import Optional

from seedwork.application import BaseModel, QueryModel

from .catalog_brand import CatalogBrandViewModel
from .catalog_type import CatalogTypeViewModel


class CatalogModel(BaseModel):
    name: str
    description: str
    price: Decimal
    picture_file_name: str
    picture_uri: str
    catalog_type: Optional[CatalogTypeViewModel]
    catalog_brand: Optional[CatalogBrandViewModel]
    available_stock: int
    restock_threshold: int
    max_stock_threshold: int
    on_reorder: bool


class CatalogViewModel(CatalogModel):
    id: int


class QueryCatalog(QueryModel):
    ...


class CreateCatalog(CatalogModel):
    ...


class UpdateCatalog(CatalogModel):
    ...
