from contextlib import nullcontext as does_not_raise
from decimal import Decimal
from typing import Any

import pytest

from module.ordering.domain.exception import OrderingDomainException
from module.ordering.domain.model.order import Order


class TestOrder:
    def test_create_new_order_raise_new_event(self, order: Order) -> None:
        expected = 1

        assert len(order.events) == expected

    def test_add_order_line_succeeds(self, order: Order) -> None:
        with does_not_raise():
            order.add_order_line(
                1,
                'phone',
                Decimal('1.0'),
                Decimal('1'),
                'picture',
                1,
            )

    @pytest.mark.parametrize(
        'product_id,product_name,unit_price,discount,picture_url,units,expectation',
        [
            pytest.param(
                1,
                'phone',
                Decimal('1.0'),
                Decimal('1.0'),
                'picture',
                -1,
                pytest.raises(OrderingDomainException),
                id='invalid units - negative',
            ),
            pytest.param(
                1,
                'phone',
                Decimal('1.0'),
                Decimal('1.0'),
                'picture',
                0,
                pytest.raises(OrderingDomainException),
                id='invalid units - zero',
            ),
            pytest.param(
                1,
                'phone',
                Decimal('-1.0'),
                Decimal('1.0'),
                'picture',
                1,
                pytest.raises(OrderingDomainException),
                id='invalid unit price - negative',
            ),
            pytest.param(
                1,
                'phone',
                Decimal('0.0'),
                Decimal('1.0'),
                'picture',
                1,
                pytest.raises(OrderingDomainException),
                id='invalid unit price - zero',
            ),
            pytest.param(
                1,
                'phone',
                Decimal('1.0'),
                Decimal('-1.0'),
                'picture',
                1,
                pytest.raises(OrderingDomainException),
                id='invalid discount - negative',
            ),
            pytest.param(
                1,
                'phone',
                Decimal('1.0'),
                Decimal('2.0'),
                'picture',
                1,
                pytest.raises(OrderingDomainException),
                id='invalid discount - greater than total',
            ),
        ],
    )
    def test_add_order_line_fails(
        self,
        order: Order,
        product_id: int,
        product_name: str,
        unit_price: Decimal,
        discount: Decimal,
        picture_url: str,
        units: int,
        expectation: Any,
    ) -> None:
        with expectation:
            order.add_order_line(
                product_id,
                product_name,
                unit_price,
                discount,
                picture_url,
                units,
            )
