from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from module.catalog.api.model import Message
from module.catalog.application.contract.catalog import (
    CatalogViewModel,
    CreateCatalog,
    QueryCatalog,
    UpdateCatalog,
)
from module.catalog.application.use_case import CatalogUseCase
from module.catalog.container import ApplicationContainer
from module.catalog.domain import Catalog
from seedwork.application import PaginatedItemsViewModel

router = APIRouter()


@router.get('/items/', response_model=PaginatedItemsViewModel[CatalogViewModel])
@inject
def get_catalogs(
    query: QueryCatalog = Depends(QueryCatalog),
    catalog_use_case: CatalogUseCase = Depends(
        Provide(ApplicationContainer.catalog_use_case)
    ),
) -> Any:
    items, total = catalog_use_case.list(query.page, query.size)
    return dict(items=items, total=total)


@router.post('/items/', response_model=CatalogViewModel, status_code=201)
@inject
def create_catalog(
    model: CreateCatalog,
    catalog_use_case: CatalogUseCase = Depends(
        Provide(ApplicationContainer.catalog_use_case)
    ),
) -> Any:
    return catalog_use_case.create(Catalog(**dict(model)))


@router.get(
    '/items/{item_id}/',
    response_model=CatalogViewModel,
    responses={404: {'model': Message}},
)
@inject
def get_catalog(
    item_id: int,
    catalog_use_case: CatalogUseCase = Depends(
        Provide(ApplicationContainer.catalog_use_case)
    ),
) -> Any:
    catalog = catalog_use_case.get(item_id)
    if not catalog:
        raise HTTPException(status_code=404)

    return catalog


@router.put(
    '/items/{item_id}/',
    response_model=CatalogViewModel,
    responses={404: {'model': Message}},
)
@inject
def update_catalog(
    item_id: int,
    model: UpdateCatalog,
    catalog_use_case: CatalogUseCase = Depends(
        Provide(ApplicationContainer.catalog_use_case)
    ),
) -> Any:
    catalog = catalog_use_case.update(item_id, Catalog(**dict(model)))
    if not catalog:
        raise HTTPException(status_code=404)

    return catalog


@router.delete('/items/{item_id}/', status_code=204, response_model=None)
@inject
def delete_catalog(
    item_id: int,
    catalog_use_case: CatalogUseCase = Depends(
        Provide(ApplicationContainer.catalog_use_case)
    ),
) -> Any:
    catalog_use_case.delete(item_id)
