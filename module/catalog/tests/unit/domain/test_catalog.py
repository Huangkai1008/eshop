from typing import Callable

import pytest

from module.catalog.domain.catalog import Catalog
from module.catalog.domain.exception import CatalogDomainException


class TestCatalog:
    def test_create_catalog_succeeds(self) -> None:
        catalog = self._catalog_factory()

        assert catalog

    @pytest.mark.parametrize(
        'desired_quantity',
        [
            pytest.param(-1, id='negative'),
            pytest.param(0, id='zero'),
        ],
    )
    def test_remove_stock_failed_when_desired_quantity_is_invalid(
        self, desired_quantity: int
    ) -> None:
        catalog = self._catalog_factory()

        with pytest.raises(CatalogDomainException):
            catalog.remove_stock(desired_quantity)

    def test_remove_stock_failed_when_available_stock_is_zero(self) -> None:
        catalog = self._catalog_factory(available_stock=0)

        with pytest.raises(CatalogDomainException):
            catalog.remove_stock(1)

    @pytest.mark.parametrize(
        'available_stock,desired_quantity,removed_quantity,remaining_stock',
        [
            pytest.param(5, 5, 5, 0, id='available_stock_equals_desired_quantity'),
            pytest.param(
                5, 4, 4, 1, id='available_stock_greater_than_desired_quantity'
            ),
            pytest.param(5, 6, 5, 0, id='available_stock_less_than_desired_quantity'),
        ],
    )
    def test_remove_stock_get_expected_removed_quantity(
        self,
        available_stock: int,
        desired_quantity: int,
        removed_quantity: int,
        remaining_stock: int,
    ) -> None:
        catalog = self._catalog_factory(available_stock=available_stock)

        removed_quantity = catalog.remove_stock(5)

        assert removed_quantity == 5

    @pytest.fixture(autouse=True)
    def _register_factory(self, catalog_factory: Callable[..., Catalog]) -> None:
        self._catalog_factory = catalog_factory
