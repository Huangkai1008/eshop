from datetime import datetime, timedelta
from typing import Any, Callable

import pytest

from module.ordering.domain.model.order.address import Address
from module.ordering.domain.model.order.order import Order

order = dict(
    user_id='user_id',
    user_name='username',
    card_type_id=1,
    card_number='900x900',
    card_security_number='VISA',
    card_holder_name='ms',
    card_expiration=datetime.now() + timedelta(days=365),
    address=Address('street', 'city', 'state', 'country', 'zipcode'),
)


@pytest.fixture
def order_factory() -> Callable[..., Order]:
    def _order_factory(**kwargs: Any) -> Order:
        return Order(**order | kwargs)  # type: ignore

    return _order_factory
