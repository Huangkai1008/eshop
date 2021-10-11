from module.identity.domain.account import Account
from seedwork.infrastructure.persistence.sqlalchemy import SQLAlchemyGenericRepository


class AccountRepository(SQLAlchemyGenericRepository[Account, int]):
    model = Account
