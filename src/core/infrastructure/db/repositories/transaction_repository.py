# src/core/infrastructure/db/repositories/transaction_repository.py

from asgiref.sync import sync_to_async
from core.domain.entities.transaction import Transaction
from core.domain.value_objects.money import Money
from apps.transactions.models import TransactionModel


class DjangoTransactionRepository:


    async def save(self, transaction):
        await sync_to_async(
            self.save_sync
        )(transaction)



    def save_sync(
        self,
        transaction
    ):

        TransactionModel.objects.create(

            id=transaction.transaction_id,

            idempotency_key=
            transaction.idempotency_key,

            from_account_id=
                transaction.from_account_id,

            to_account_id=
                transaction.to_account_id,

            amount=
                transaction.amount.amount,

            currency=
                transaction.amount.currency,

            status=
                transaction.status
        )
    
    def find_by_idempotency_key(
        self,
        key
    ):

        try:

            model = (
                TransactionModel.objects
                .get(
                    idempotency_key=key
                )
            )

        except TransactionModel.DoesNotExist:

            return None



        return Transaction(
            from_account_id=model.from_account_id,
            to_account_id=model.to_account_id,
            amount=Money(
                model.amount,
                model.currency
            ),
            idempotency_key=key
        )