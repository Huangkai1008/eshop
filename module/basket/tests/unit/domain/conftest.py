from decimal import Decimal
from typing import Any, Callable

import pytest

from module.basket.domain import Basket

basket = dict(
    buyer_id='1',
    items=[
        {
            'product_id': 1,
            'product_name': 'name1',
            'unit_price': Decimal('1.0'),
            'old_unit_price': Decimal('1.0'),
            'quantity': 2,
            'picture_url': 'url_1',
        },
        {
            'product_id': 2,
            'product_name': 'name2',
            'unit_price': Decimal('0.8'),
            'old_unit_price': Decimal('1.0'),
            'quantity': 1,
            'picture_url': 'url_2',
        }
    ]
)


@pytest.fixture
def basket_factory() -> Callable[..., Basket]:
    def _basket_factory(**kwargs: Any) -> Basket:
        return Basket(**basket | kwargs)  # type: ignore

    return _basket_factory
