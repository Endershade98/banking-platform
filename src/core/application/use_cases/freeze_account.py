# src/core/application/use_cases/freeze_account.py
from core.domain.repositories.account_repository import AccountRepository

class FreezeAccountUseCase:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    async def execute(self, account_id: str) -> None:
        account = await self.account_repo.get_by_id(account_id)
        account.freeze()  # Supponendo che Account abbia un metodo freeze()
        await self.account_repo.save(account)