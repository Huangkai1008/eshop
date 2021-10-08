from seedwork.application import BaseModel, QueryModel


class QueryCatalogType(QueryModel):
    ...


class CatalogTypeModel(BaseModel):
    name: str


class CatalogTypeViewModel(CatalogTypeModel):
    id: int


class CreateCatalogType(CatalogTypeModel):
    ...


class UpdateCatalogType(CatalogTypeModel):
    ...
