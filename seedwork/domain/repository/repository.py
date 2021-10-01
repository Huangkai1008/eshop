from typing import Protocol, runtime_checkable

from seedwork.domain.typings import T_co


@runtime_checkable
class Repository(Protocol[T_co]):
    ...
