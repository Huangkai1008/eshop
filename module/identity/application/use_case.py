from module.identity.domain.account import Account
from module.identity.infrastructure.repository.account import AccountRepository


class AccountUseCase:
    def __init__(self, account_repository: AccountRepository) -> None:
        self._repo = account_repository

    def register(self, account: Account) -> Account:
        return self._repo.add(account)
