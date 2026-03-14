# src/core/application/use_cases/create_account.py
from core.domain.entities.account import Account
from core.domain.value_objects.money import Money
from core.domain.repositories.account_repository import AccountRepository
import uuid

class CreateAccountUseCase:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    async def execute(self, owner: str, initial_balance: float = 0.0, currency: str = "USD") -> Account:
        account = Account(
            account_id=str(uuid.uuid4()),
            owner=owner,
            balance=Money(amount=initial_balance, currency=currency)
        )
        await self.account_repo.save(account)
        return account