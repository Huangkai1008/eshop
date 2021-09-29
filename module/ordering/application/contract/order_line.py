from decimal import Decimal

from seedwork.application import BaseModel

__all__ = ['OrderLineModel']


class OrderLineModel(BaseModel):
    product_id: int
    product_name: str
    unit_price: Decimal
    discount: Decimal
    units: int
    picture_url: str
