from dataclasses import dataclass

from eshop.seedwork.domain.value_object import ValueObject

__all__ = ['Address']


@dataclass(frozen=True)
class Address(ValueObject):
    street: str
    city: str
    state: str
    country: str
    zipcode: str
