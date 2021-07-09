from decimal import Decimal

from pydantic import BaseModel

__all__ = ['OrderLine']


class OrderLine(BaseModel):
    product_id: int
    product_name: str
    unit_price: Decimal
    discount: Decimal
    units: int
    picture_url: str
