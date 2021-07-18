from dataclasses import dataclass

from seedwork.domain.entity import Entity

__all__ = ['CatalogBrand']


@dataclass
class CatalogBrand(Entity):
    brand: str
