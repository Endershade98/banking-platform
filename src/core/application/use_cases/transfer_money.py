# src/core/application/use_cases/transfer_money.py

from core.domain.services.transaction_service import TransactionService
from core.domain.value_objects.money import Money
from core.domain.services.ledger_service import LedgerService


class TransferMoneyUseCase:


    def __init__(
        self,
        account_repository,
        transaction_repository,
        ledger_repository=None
    ):

        self.account_repository = account_repository
        self.transaction_repository = transaction_repository

        self.transaction_service = TransactionService()


        self.ledger_service = (
            LedgerService(ledger_repository)
            if ledger_repository
            else None
        )



    async def execute(
        self,
        from_account_id,
        to_account_id,
        amount: Money
    ):


        from_account = await self.account_repository.get_by_id(
            from_account_id
        )

        to_account = await self.account_repository.get_by_id(
            to_account_id
        )


        if not from_account or not to_account:
            raise ValueError(
                "Account not found"
            )


        transaction = self.transaction_service.transfer(
            from_account,
            to_account,
            amount
        )


        await self.account_repository.update(
            from_account
        )

        await self.account_repository.update(
            to_account
        )


        await self.transaction_repository.save(
            transaction
        )


        if self.ledger_service:

            await self.ledger_service.post_transaction(
                transaction
            )


        return transaction