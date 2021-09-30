from dataclasses import dataclass

from seedwork.domain.entity import Entity


@dataclass
class CatalogBrand(Entity):
    brand: str
