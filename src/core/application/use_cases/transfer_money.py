# src/core/application/use_cases/transfer_money.py

from asgiref.sync import sync_to_async
from django.db import transaction

from core.domain.services.transaction_service import TransactionService
from core.domain.services.ledger_service import LedgerService



class TransferMoneyUseCase:


    def __init__(
        self,
        account_repository,
        transaction_repository,
        ledger_repository
    ):

        self.account_repository = account_repository

        self.transaction_repository = transaction_repository

        self.transaction_service = TransactionService()

        self.ledger_service = LedgerService(
            ledger_repository
        )

    async def execute(
        self,
        from_account_id,
        to_account_id,
        amount,
        idempotency_key
    ):


        existing = await sync_to_async(
            self.transaction_repository
            .find_by_idempotency_key
        )(idempotency_key)


        if existing:

            return existing

        return await sync_to_async(
            self._execute_transaction,
            thread_sensitive=True
        )(
            from_account_id,
            to_account_id,
            amount,
            idempotency_key
        )

    def _execute_transaction(
        self,
        from_account_id,
        to_account_id,
        amount,
        idempotency_key
    ):

        with transaction.atomic():


            sender = (
                self.account_repository
                .get_for_update_sync(
                    from_account_id
                )
            )


            receiver = (
                self.account_repository
                .get_for_update_sync(
                    to_account_id
                )
            )


            tx = self.transaction_service.transfer(
                sender,
                receiver,
                amount,
                idempotency_key
            )


            sender.withdraw(amount)

            receiver.deposit(amount)



            self.account_repository.update_sync(
                sender
            )


            self.account_repository.update_sync(
                receiver
            )


            tx.mark_completed()


            self.transaction_repository.save_sync(
                tx
            )


            self.ledger_service.post_transaction_sync(
                tx
            )


            return tx