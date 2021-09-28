from dataclasses import dataclass
from decimal import Decimal

from module.catalog.domain.exception import CatalogDomainException
from seedwork.domain import Entity

__all__ = ['Catalog']


@dataclass
class Catalog(Entity):
    name: str
    description: str
    price: Decimal
    picture_file_name: str
    picture_uri: str
    catalog_type_id: int
    catalog_brand_id: int
    available_stock: int
    restock_threshold: int
    max_stock_threshold: int
    on_reorder: bool

    def remove_stock(self, desired_quantity: int) -> int:
        """Remove stock from the catalog.

        Args:
            desired_quantity: Desired quantity to remove.
        Returns:
            The number actually removed from stock.

        """

        if self.available_stock == 0:
            raise CatalogDomainException(
                f'Empty stock, product item {self.name} is sold out'
            )

        if desired_quantity <= 0:
            raise CatalogDomainException(
                'Catalog units desired should be greater than zero'
            )

        # If the available stock is enough to cover the desired quantity,
        # then remove the desired quantity from the available stock.
        # Otherwise, remove the available stock.
        removed_quantity = min(desired_quantity, self.available_stock)

        self.available_stock -= removed_quantity
        return removed_quantity
