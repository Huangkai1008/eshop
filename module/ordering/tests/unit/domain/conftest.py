from datetime import datetime, timedelta

import pytest

from module.ordering.domain.model.order.address import Address
from module.ordering.domain.model.order.order import Order


@pytest.fixture
def address() -> Address:
    return Address('street', 'city', 'state', 'country', 'zipcode')


@pytest.fixture
def order() -> Order:
    return Order(
        'user_id',
        'username',
        1,
        '900x900',
        'VISA',
        'ms',
        datetime.now() + timedelta(days=365),
        Address('street', 'city', 'state', 'country', 'zipcode'),
    )
