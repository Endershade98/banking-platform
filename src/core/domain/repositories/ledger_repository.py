# src/core/domain/repositories/ledger_repository.py

from abc import ABC, abstractmethod


class LedgerRepository(ABC):

    @abstractmethod
    async def save(self, entry):
        pass


    @abstractmethod
    async def find_all(self):
        pass


    @abstractmethod
    async def find_by_account(
        self,
        account_id
    ):
        pass


    @abstractmethod
    async def find_by_transaction(
        self,
        transaction_id
    ):
        pass