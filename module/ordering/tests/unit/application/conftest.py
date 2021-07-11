from datetime import datetime, timedelta
from decimal import Decimal

import pytest

order_line_input = dict(
    product_id=1,
    product_name='phone',
    unit_price=Decimal('1.0'),
    discount=Decimal('1.0'),
    picture_url='picture',
    units=1,
)

create_order_command_input = dict(
    user_id='id',
    user_name='name',
    card_type_id=1,
    card_number='123456561212',
    card_security_number='security',
    card_holder_name='holder',
    card_expiration=datetime.now() + timedelta(days=365),
    street='street',
    city='city',
    country='country',
    zipcode='zipcode',
    state='state',
    order_lines=[
        order_line_input,
    ],
)


@pytest.fixture
def create_order_input() -> dict:
    return create_order_command_input


@pytest.fixture
def create_order_input_with_card_expiration_in_past() -> dict:
    return create_order_command_input | dict(
        card_expiration=datetime.now() - timedelta(days=365),
    )


@pytest.fixture
def create_order_input_with_no_order_lines() -> dict:
    return create_order_command_input | dict(
        order_lines=[],
    )
