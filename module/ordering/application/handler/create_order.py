from dataclasses import dataclass

from seedwork.infrastructure.logging import Logger

from module.ordering.application.command.create_order import CreateOrder
from module.ordering.domain.model.order import Address, Order
from module.ordering.infrastructure.repository.unit_of_work import UnitOfWork

__all__ = ['CreateOrderHandler']


@dataclass
class CreateOrderHandler:
    _uow: UnitOfWork
    _logger: Logger

    def __call__(self, command: CreateOrder) -> Order:
        address = Address(
            street=command.street,
            city=command.city,
            country=command.country,
            zipcode=command.zipcode,
            state=command.state,
        )
        order = Order(
            user_id=command.user_id,
            user_name=command.user_name,
            card_type_id=command.card_type_id,
            card_number=command.card_number,
            card_security_number=command.card_security_number,
            card_holder_name=command.card_holder_name,
            card_expiration=command.card_expiration,
            address=address,
        )
        for order_line in command.order_lines:
            order.add_order_line(
                product_id=order_line.product_id,
                product_name=order_line.product_name,
                unit_price=order_line.unit_price,
                discount=order_line.discount,
                picture_url=order_line.picture_url,
                units=order_line.units,
            )

        self._logger.log('Creating Order - Order: {order}', order=order)

        with self._uow as uow:
            uow.orders.add(order)
            uow.commit()
        return order
