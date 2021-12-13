from decimal import Decimal
from typing import Optional

from sqlmodel import Field, Relationship

from module.catalog.domain.exception import CatalogDomainException
from seedwork.infrastructure.persistence.sqlmodel import (
    SQLModelEntity,
    id_field,
    str_field,
)


class _CatalogBrand(SQLModelEntity):
    name: str = str_field


class CatalogBrand(_CatalogBrand, table=True):
    id: Optional[int] = id_field


class CreateCatalogBrand(_CatalogBrand):
    ...


class _CatalogType(SQLModelEntity):
    name: str = str_field


class CreateCatalogType(_CatalogType):
    ...


class CatalogType(_CatalogType, table=True):
    id: Optional[int] = id_field


class _Catalog(SQLModelEntity):
    description: str = str_field
    price: Decimal
    picture_file_name: str = str_field
    picture_uri: Optional[str] = str_field
    available_stock: int
    restock_threshold: int
    max_stock_threshold: int
    on_reorder: int

    catalog_type_id: int
    catalog_brand_id: int


class Catalog(_Catalog, table=True):
    id: Optional[int] = id_field
    name: str = str_field

    catalog_type_id: int = Field(foreign_key='catalog_type.id')
    catalog_brand_id: int = Field(foreign_key='catalog_brand.id')
    catalog_type: Optional[CatalogType] = Relationship()
    catalog_brand: Optional[CatalogBrand] = Relationship()

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


class CreateCatalog(_Catalog):
    name: str = str_field


class UpdateCatalog(_Catalog):
    ...


class CatalogViewModel(_Catalog):
    id: int
    catalog_type: CatalogType
    catalog_brand: CatalogBrand
