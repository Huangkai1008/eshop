from enum import Enum, unique

__all__ = ['OrderStatus']


@unique
class OrderStatus(Enum):
    """Order status enumeration."""

    SUBMITTED = 'submitted'
