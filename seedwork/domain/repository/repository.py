from typing import Protocol

from seedwork.domain.typings import T


class Repository(Protocol[T]):
    ...
