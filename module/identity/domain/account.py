from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from seedwork.infrastructure.persistence.sqlalchemy import DataEntity, str_field


class Account(DataEntity):
    __tablename__ = 'account'

    name: Mapped[str_field]
    password: Mapped[str] = mapped_column(String(1024), nullable=False)

    card_number: Mapped[str_field] = mapped_column(nullable=False)
    security_number: Mapped[str_field] = mapped_column(nullable=False)
    expiration: Mapped[str_field] = mapped_column(nullable=False)
