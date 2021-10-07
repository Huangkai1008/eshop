from typing import Any, Protocol, TypeVar

from .entity import EntityId


class EntityType(Protocol):
    id: Any


T = TypeVar('T', bound=EntityType)
ID = TypeVar('ID', bound=EntityId)
T_co = TypeVar('T_co', bound=EntityType, covariant=True)
ID_co = TypeVar('ID_co', bound=EntityId, covariant=True)
