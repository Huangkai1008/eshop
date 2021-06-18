import uuid
from dataclasses import dataclass, field
from typing import Any

__all__ = ['Entity']


@dataclass
class Entity:
    id: str = field(init=False)

    def __post_init__(self) -> None:
        self.id = self.next_id()

    @classmethod
    def next_id(cls) -> str:
        return str(uuid.uuid4())

    def __eq__(self, other: Any) -> bool:
        return other.__class__ is self.__class__ and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
