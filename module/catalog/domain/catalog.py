from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from module.catalog.domain.exception import CatalogDomainException
from seedwork.infrastructure.persistence.sqlalchemy import DataEntity, str_field

from .catalog_brand import CatalogBrand
from .catalog_type import CatalogType


class Catalog(DataEntity):
    __tablename__ = 'catalog'

    name: Mapped[str_field]
    description: Mapped[str_field]
    price: Mapped[Decimal]
    picture_file_name: Mapped[str_field]
    picture_uri: Mapped[str_field]
    catalog_type_id: Mapped[int] = mapped_column(ForeignKey('catalog_type.id'))
    catalog_brand_id: Mapped[int] = mapped_column(ForeignKey('catalog_brand.id'))
    catalog_type: Mapped[CatalogType] = relationship(CatalogType, uselist=False)
    catalog_brand: Mapped[CatalogBrand] = relationship(CatalogBrand, uselist=False)
    available_stock: Mapped[int]
    restock_threshold: Mapped[int]
    max_stock_threshold: Mapped[int]
    on_reorder: Mapped[int]

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
