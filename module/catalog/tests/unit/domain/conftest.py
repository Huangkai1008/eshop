from decimal import Decimal
from typing import Any, Callable

import pytest

from module.catalog.domain import Catalog

catalog = dict(
    name='name',
    description='description',
    price=Decimal('1.0'),
    picture_file_name='picture_file_name',
    picture_uri='picture_uri',
    restock_threshold=1,
    catalog_type_id=1,
    catalog_brand_id=1,
    catalog_type=dict(name='catalog_type'),
    catalog_brand=dict(name='catalog_brand'),
    available_stock=1,
    max_stock_threshold=1,
    on_reorder=False,
)


@pytest.fixture
def catalog_factory() -> Callable[..., Catalog]:
    def _catalog_factory(**kwargs: Any) -> Catalog:
        return Catalog(**catalog | kwargs)  # type: ignore

    return _catalog_factory
