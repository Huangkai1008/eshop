from typing import Protocol, TypeVar

from seedwork.domain import AggregateRoot

__all__ = ['Repository']

TAggregateRoot = TypeVar('TAggregateRoot', bound=AggregateRoot, covariant=True)


class Repository(Protocol[TAggregateRoot]):
    ...
