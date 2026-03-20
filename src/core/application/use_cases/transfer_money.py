# src/core/application/use_cases/transfer_money.py

from core.domain.services.transaction_service import TransactionService


class TransferMoneyUseCase:

    def __init__(self, account_repository, transaction_repository):
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository
        self.transaction_service = TransactionService()

    async def execute(self, from_account_id: str, to_account_id: str, amount):

        # Load accounts
        from_account = await self.account_repository.get_by_id(from_account_id)
        to_account = await self.account_repository.get_by_id(to_account_id)

        if not from_account or not to_account:
            raise ValueError("Account not found")

        # Domain logic
        transaction = self.transaction_service.transfer(
            from_account,
            to_account,
            amount
        )

        # Persist changes
        await self.account_repository.update(from_account)
        await self.account_repository.update(to_account)
        await self.transaction_repository.save(transaction)

        return transaction