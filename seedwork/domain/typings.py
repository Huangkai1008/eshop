from typing import TypeVar

from .entity import Entity, EntityId

T = TypeVar('T', bound=Entity)
ID = TypeVar('ID', bound=EntityId)
