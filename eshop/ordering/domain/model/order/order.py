from dataclasses import InitVar, dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Literal, Optional, Union

from .address import Address
from .order_line import OrderLine
from .order_status import OrderStatus

__all__ = ['Order']


@dataclass
class Order:
    user_id: InitVar[str]
    user_name: InitVar[str]

    card_type_id: InitVar[int]
    card_number: InitVar[str]
    card_security_number: InitVar[str]
    card_holder_name: InitVar[str]
    card_expiration: InitVar[datetime]

    address: Address

    order_status: OrderStatus = field(default=OrderStatus.SUBMITTED)
    description: str = field(init=False)

    _order_lines: list[OrderLine] = field(default_factory=list)
    _buyer_id: Optional[str] = field(default=None)
    _payment_method_id: Optional[int] = field(default=None)
    _order_date: datetime = field(default_factory=datetime.now)
    _is_draft: bool = False

    def __post_init__(
        self,
        user_id: str,
        user_name: str,
        card_type_id: int,
        card_number: str,
        card_security_number: str,
        card_holder_name: str,
        card_expiration: datetime,
    ) -> None:
        ...

    def add_order_line(
        self,
        product_id: int,
        product_name: str,
        unit_price: Decimal,
        discount: Decimal,
        picture_url: str,
        units: int = 1,
    ) -> None:
        existing_order_for_product: Optional[OrderLine] = next(
            (o for o in self._order_lines if o.product_id == product_id), None
        )
        if existing_order_for_product:
            existing_order_for_product.discount = max(
                discount, existing_order_for_product.discount
            )
            existing_order_for_product.add_units(units)
        else:
            order_line = OrderLine(
                product_id, product_name, picture_url, unit_price, discount, units
            )
            self._order_lines.append(order_line)

    @property
    def buyer_id(self) -> str:
        return self.buyer_id

    @property
    def total(self) -> Union[Decimal, Literal[0]]:
        return sum(order_line.total for order_line in self._order_lines)
