from sqlalchemy.orm import declared_attr
from sqlmodel import Field, SQLModel

id_field = Field(default=None, primary_key=True)
str_field = Field(max_length=255)


class SQLModelEntity(SQLModel):
    __abstract__ = True

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return ''.join(
            ['_' + i.lower() if i.isupper() else i for i in cls.__name__]
        ).lstrip('_')
