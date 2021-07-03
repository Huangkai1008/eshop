from dataclasses import dataclass
from datetime import datetime

from eshop.seedwork.domain.event import Event

__all__ = ['OrderCreated']


@dataclass(frozen=True)
class OrderCreated(Event):
    user_id: str
    username: str
    card_type_id: int
    card_number: str
    card_security_number: str
    card_holder_name: str
    card_expiration: datetime
