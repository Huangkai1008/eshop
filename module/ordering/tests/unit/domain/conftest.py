from datetime import datetime, timedelta
from typing import Any, Callable

import pytest

from module.ordering.domain.model.order.address import Address
from module.ordering.domain.model.order.order import Order


@pytest.fixture
def order_factory() -> Callable[..., Order]:
    def _order_factory(**kwargs: Any) -> Order:
        return Order(
            'user_id',
            'username',
            1,
            '900x900',
            'VISA',
            'ms',
            datetime.now() + timedelta(days=365),
            Address('street', 'city', 'state', 'country', 'zipcode'),
            **kwargs,
        )

    return _order_factory
