from datetime import datetime

from pydantic import Field, field_validator

from module.ordering.application.schema import OrderLine
from seedwork.application import Command

__all__ = ['CreateOrder']


class CreateOrder(Command):
    user_id: str
    user_name: str

    city: str
    street: str
    state: str
    zipcode: str
    country: str

    card_number: str = Field(min_length=12, max_length=19)
    card_holder_name: str
    card_expiration: datetime
    card_security_number: str
    card_type_id: int

    order_lines: list[OrderLine] = Field(min_length=1)

    @field_validator('card_expiration')
    def card_expiration_must_be_in_the_future(cls, v: datetime) -> datetime:
        if v < datetime.now():
            raise ValueError('card expiration must be in the future')
        return v
