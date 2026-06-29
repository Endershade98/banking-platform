# src/core/domain/services/transaction_service.py

from core.domain.entities.transaction import Transaction


class TransactionService:


    def transfer(
        self,
        from_account,
        to_account,
        amount,
        idempotency_key=None
    ):


        transaction = Transaction(
            from_account_id=
                from_account.account_id,

            to_account_id=
                to_account.account_id,

            amount=amount,

            idempotency_key=
                idempotency_key
        )


        return transaction