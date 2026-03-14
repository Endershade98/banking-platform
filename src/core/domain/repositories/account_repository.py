# core/domain/repositories/account_repository.py

from abc import ABC, abstractmethod
from core.domain.entities.account import Account

class AccountRepository(ABC):
    @abstractmethod
    async def get_by_id(self, account_id: str) -> Account:
        pass

    @abstractmethod
    async def save(self, account: Account) -> None:
        pass

    @abstractmethod
    async def list_all(self) -> list[Account]:
        pass