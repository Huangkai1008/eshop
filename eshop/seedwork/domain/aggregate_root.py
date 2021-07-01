from dataclasses import dataclass

from eshop.seedwork.domain.entity import Entity


@dataclass
class AggregateRoot(Entity):
    ...
