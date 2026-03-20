# src/core/domain/repositories/transaction_repository.py

from abc import ABC, abstractmethod


class TransactionRepository(ABC):

    @abstractmethod
    async def save(self, transaction):
        pass