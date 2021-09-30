from module.catalog.domain.model import Catalog
from seedwork.application import QueryModel


class CatalogModel(Catalog):
    ...


class QueryCatalog(QueryModel):
    ...


class CreateCatalog(CatalogModel):
    ...
