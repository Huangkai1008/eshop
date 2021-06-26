from dataclasses import FrozenInstanceError
from typing import Type, TypeVar, Union

import pytest

from tests.unit.seedwork.domain.conftest import ValueObjectA, ValueObjectB

VO = TypeVar('VO', bound=Union[ValueObjectA, ValueObjectB])


class TestValueObject:
    def test_value_objects_are_equal(self) -> None:
        vo1 = ValueObjectA(1)
        vo2 = ValueObjectA(1)

        equality: bool = vo1 == vo2

        assert equality is True

    @pytest.mark.parametrize(
        'type1,value1,type2,value2',
        [
            pytest.param(
                ValueObjectA,
                1,
                ValueObjectA,
                2,
                id='different_values',
            ),
            pytest.param(
                ValueObjectA,
                1,
                ValueObjectB,
                1,
                id='different_types',
            ),
        ],
    )
    def test_value_objects_are_not_equal(
        self,
        value1: int,
        value2: int,
        type1: Type[VO],
        type2: Type[VO],
    ) -> None:
        vo1 = type1(value1)
        vo2 = type2(value2)

        equality: bool = vo1 == vo2

        assert equality is False

    def test_value_objects_are_immutable(self) -> None:
        vo = ValueObjectA(1)

        with pytest.raises(FrozenInstanceError):
            vo.field = 2  # type: ignore  # noqa
