from seedwork.application import BaseModel, QueryModel


class QueryCatalogBrand(QueryModel):
    ...


class CatalogBrandModel(BaseModel):
    name: str


class CatalogBrandViewModel(CatalogBrandModel):
    id: int


class CreateCatalogBrand(CatalogBrandModel):
    ...


class UpdateCatalogBrand(CatalogBrandModel):
    ...
