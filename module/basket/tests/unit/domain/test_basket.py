from typing import Callable

import pytest

from module.basket.domain import Basket


class TestBasket:
    def test_create_basket_succeeds(self) -> None:
        basket = self._basket_factory()

        assert basket

    @pytest.fixture(autouse=True)
    def _register_factory(self, basket_factory: Callable[..., Basket]) -> None:
        self._basket_factory = basket_factory
