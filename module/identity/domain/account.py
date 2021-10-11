from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from seedwork.infrastructure.persistence.sqlalchemy import DataEntity, str_field


class Account(DataEntity):
    __tablename__ = 'account'

    name: Mapped[str_field]
    password_hash: Mapped[str] = mapped_column(String(1024), nullable=False)
