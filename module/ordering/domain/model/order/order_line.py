from dataclasses import dataclass
from decimal import Decimal

from seedwork.domain import Entity

from module.ordering.domain.exception import OrderingDomainException

__all__ = ['OrderLine']


@dataclass
class OrderLine(Entity):
    product_id: int

    _product_name: str
    _picture_url: str
    _unit_price: Decimal
    _discount: Decimal
    _units: int = 1

    def __post_init__(self) -> None:
        # Maybe should use specification pattern or the `Parse, don't validate` pattern.
        # See also:
        # - https://stackoverflow.com/questions/33220394/how-to-share-validation-
        #   between-forms-and-value-objects-in-domain-driven-design?rq=4
        # - https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/

        self._units_should_greater_than_zero()
        self._unit_price_should_greater_than_zero()
        self._discount_should_greater_than_zero()
        self._total_should_greater_than_discount()

    @property
    def discount(self) -> Decimal:
        return self._discount

    @discount.setter
    def discount(self, value: Decimal) -> None:
        self._discount = value

    def add_units(self, units: int) -> None:
        if units <= 0:
            raise OrderingDomainException('Add units is not greater than 0')

        self._units += units

    @property
    def total(self) -> Decimal:
        return self._units * self._unit_price

    def _units_should_greater_than_zero(self) -> None:
        if self._units <= 0:
            raise OrderingDomainException('Invalid number of units')

    def _unit_price_should_greater_than_zero(self) -> None:
        if self._unit_price <= 0:
            raise OrderingDomainException('Invalid unit price')

    def _discount_should_greater_than_zero(self) -> None:
        if self._discount <= 0:
            raise OrderingDomainException('Invalid discount')

    def _total_should_greater_than_discount(self) -> None:
        if self.total < self._discount:
            raise OrderingDomainException(
                'The total of order item is lower than applied discount'
            )
