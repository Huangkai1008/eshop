from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from module.catalog.application.contract import CatalogCreate, CatalogQuery
from module.catalog.application.contract.catalog import CatalogViewModel
from module.catalog.application.use_case import CatalogUseCase
from module.catalog.container import Container
from module.catalog.domain.model import Catalog
from seedwork.application import PaginatedItemsViewModel

router = APIRouter(prefix='/api/v1/catalog', tags=['Catalog'])


@router.get('/items/', response_model=PaginatedItemsViewModel[CatalogViewModel])
@inject
def get_catalogs(
    query: CatalogQuery = Depends(CatalogQuery),
    catalog_use_case: CatalogUseCase = Depends(Provide(Container.catalog_use_case)),
) -> Any:
    items, total = catalog_use_case.list(query.page, query.size)
    return dict(items=items, total=total)


@router.post('/items/', response_model=CatalogViewModel, status_code=201)
@inject
def create_catalog(
    model: CatalogCreate,
    catalog_use_case: CatalogUseCase = Depends(Provide(Container.catalog_use_case)),
) -> Catalog:
    return catalog_use_case.create(Catalog(**model.model_dump()))
