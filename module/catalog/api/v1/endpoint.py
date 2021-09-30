from fastapi import APIRouter, Depends

from module.catalog.application.contract import (
    CatalogModel,
    CreateCatalog,
    QueryCatalog,
)
from seedwork.application import PaginatedItemsViewModel

router = APIRouter(prefix='/api/v1/catalog', tags=['Catalog'])


@router.get('/items/', response_model=PaginatedItemsViewModel[CatalogModel])
def get_catalogs(
    query: QueryCatalog = Depends(QueryCatalog),
):
    return {'items': [{'name': 'Foo'}, {'name': 'Bar'}]}


@router.post('/items/', response_model=CatalogModel, status_code=201)
def create_catalog(catalog: CreateCatalog):
    return catalog
