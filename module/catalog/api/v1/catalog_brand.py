from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from module.catalog.application.contract.catalog_brand import QueryCatalogBrand
from module.catalog.application.use_case import CatalogBrandUseCase
from module.catalog.container import ApplicationContainer
from module.catalog.domain import CatalogBrand
from seedwork.application import PaginatedItemsViewModel

router = APIRouter()


@router.get('/catalog-brands/', response_model=PaginatedItemsViewModel[CatalogBrand])
@inject
def get_catalog_brands(
    query: QueryCatalogBrand = Depends(QueryCatalogBrand),
    catalog_brand_use_case: CatalogBrandUseCase = Depends(
        Provide(ApplicationContainer.catalog_brand_use_case)
    ),
) -> Any:
    items, total = catalog_brand_use_case.list(query.page, query.size)
    return dict(items=items, total=total)


@router.post('/catalog-brands/', response_model=CatalogBrand, status_code=201)
@inject
def create_catalog_brand(
    model: CatalogBrand,
    catalog_brand_use_case: CatalogBrandUseCase = Depends(
        Provide(ApplicationContainer.catalog_brand_use_case)
    ),
) -> Any:
    return catalog_brand_use_case.create(model)
