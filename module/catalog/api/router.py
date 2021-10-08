from fastapi import APIRouter

from .v1.catalog import router as catalog_router
from .v1.catalog_brand import router as catalog_brand_router
from .v1.catalog_type import router as catalog_type_router

v1_router = APIRouter(prefix='/api/v1/catalog', tags=['Catalog'])

v1_router.include_router(catalog_router)
v1_router.include_router(catalog_brand_router)
v1_router.include_router(catalog_type_router)
