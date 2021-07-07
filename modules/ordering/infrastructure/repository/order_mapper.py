from sqlalchemy import (
    DECIMAL,
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import foreign, registry, relationship

from modules.ordering.domain.model.order import Address, Order, OrderLine

mapper_registry = registry()

order = Table(
    'order',
    mapper_registry.metadata,
    Column('id', String(255), primary_key=True),
    Column('order_status', String(255)),
    Column('description', String(255)),
    Column('buyer_id', String(255)),
    Column('payment_method_id', Integer),
    Column('order_date', DateTime),
    Column('is_draft', Boolean),
)

order_line = Table(
    'order_line',
    mapper_registry.metadata,
    Column('id', String(255), primary_key=True),
    Column('product_id', Integer),
    Column('product_name', String(255)),
    Column('picture_url', String(255)),
    Column('unit_price', DECIMAL),
    Column('discount', DECIMAL),
    Column('units', Integer),
    Column('order_id', String(255), index=True),
)

address = Table(
    'address',
    mapper_registry.metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('street', String(255)),
    Column('city', String(255)),
    Column('state', String(255)),
    Column('country', String(255)),
    Column('zip_code', String(255)),
    Column('order_id', String(255), index=True),
)


def start_mappers() -> None:
    mapper_registry.map_imperatively(OrderLine, order_line)
    mapper_registry.map_imperatively(Address, address)
    mapper_registry.map_imperatively(
        Order,
        order,
        properties={
            '_order_lines': relationship(
                OrderLine,
                primaryjoin=foreign(order.c.id) == foreign(order_line.c.order_id),
            ),
            '_address': relationship(
                Address,
                primaryjoin=foreign(order.c.id) == foreign(address.c.order_id),
                uselist=False,
            ),
        },
    )
