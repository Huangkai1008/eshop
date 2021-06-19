from dataclasses import dataclass

from eshop.seedwork.domain.value_object import ValueObject


@dataclass(frozen=True)
class ValueObjectA(ValueObject):
    field: int


@dataclass(frozen=True)
class ValueObjectB(ValueObject):
    field: int
