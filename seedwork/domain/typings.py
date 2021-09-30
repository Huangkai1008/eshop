from typing import TypeVar

from .entity import Entity, EntityId

T = TypeVar('T', bound=Entity)
ID = TypeVar('ID', bound=EntityId)
T_co = TypeVar('T_co', bound=Entity, covariant=True)
ID_co = TypeVar('ID_co', bound=EntityId, covariant=True)
