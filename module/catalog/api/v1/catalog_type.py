from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from module.catalog.application.contract.catalog_type import (
    CreateCatalogType,
    QueryCatalogType,
)
from module.catalog.application.use_case import CatalogTypeUseCase
from module.catalog.container import ApplicationContainer
from module.catalog.domain.model import CatalogType
from seedwork.application import PaginatedItemsViewModel

router = APIRouter()


@router.get('/catalog-types/', response_model=PaginatedItemsViewModel[CatalogType])
@inject
def get_catalog_types(
    query: QueryCatalogType = Depends(QueryCatalogType),
    catalog_type_use_case: CatalogTypeUseCase = Depends(
        Provide(ApplicationContainer.catalog_type_use_case)
    ),
) -> Any:
    items, total = catalog_type_use_case.list(query.page, query.size)
    return dict(items=items, total=total)


@router.post('/catalog-types/', response_model=CatalogType, status_code=201)
@inject
def create_catalog_type(
    model: CreateCatalogType,
    catalog_type_use_case: CatalogTypeUseCase = Depends(
        Provide(ApplicationContainer.catalog_type_use_case)
    ),
) -> Any:
    return catalog_type_use_case.create(CatalogType(**dict(model)))
