# src/core/domain/services/transaction_service.py

from core.domain.entities.transaction import Transaction
from core.domain.value_objects.money import Money


class TransactionService:

    def transfer(self, from_account, to_account, amount: Money) -> Transaction:

        # Business rules
        if from_account.is_frozen:
            raise ValueError("Source account is frozen")

        if to_account.is_frozen:
            raise ValueError("Destination account is frozen")

        if from_account.balance.currency != amount.currency:
            raise ValueError("Currency mismatch")

        if from_account.balance.amount < amount.amount:
            raise ValueError("Insufficient funds")

        # Apply transfer
        from_account.withdraw(amount)
        to_account.deposit(amount)

        # Create transaction
        transaction = Transaction(
            from_account_id=from_account.account_id,
            to_account_id=to_account.account_id,
            amount=amount,
        )

        transaction.mark_completed()

        return transaction