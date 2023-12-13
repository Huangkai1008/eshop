from typing import Any, Protocol

__all__ = ['CacheClient']


class CacheClient(Protocol):
    """Cache client interface."""

    def get(self, key: str) -> Any:
        ...

    def set(self, key: str, value: Any) -> Any:
        ...

    def delete(self, key: str) -> bool:
        ...
