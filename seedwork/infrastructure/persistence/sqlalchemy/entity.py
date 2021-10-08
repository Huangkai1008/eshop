from typing import Annotated, Any

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column

int_pk = Annotated[int, mapped_column(primary_key=True)]
str_field = Annotated[str, mapped_column(String(255))]


class Base(DeclarativeBase):
    ...


class DataEntity(MappedAsDataclass, Base):
    """Base class for data entities.

    Notes:
        DataEntity only used in Supporting Domain Model with a Data Mapper pattern.
        For a complex domain model, you should use AggregateRoot.

        For fastapi application, you can use SqlModel library to generate pydantic,
        it's simpler.

    """

    __abstract__ = True

    id: Mapped[int_pk] = mapped_column(init=False)

    def __eq__(self, other: Any) -> bool:
        return other.__class__ is self.__class__ and self.id == other.id
