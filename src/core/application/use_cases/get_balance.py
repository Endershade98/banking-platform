# src/core/application/use_cases/get_balance.py
from core.domain.repositories.account_repository import AccountRepository
from core.domain.value_objects.money import Money

class GetBalanceUseCase:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    async def execute(self, account_id: str) -> Money:
        account = await self.account_repo.get_by_id(account_id)
        return account.balance