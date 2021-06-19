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
        'value1,value2,type1,type2',
        [
            pytest.param(
                1,
                2,
                ValueObjectA,
                ValueObjectA,
                id='different_values',
            ),
            pytest.param(
                1,
                1,
                ValueObjectA,
                ValueObjectB,
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
