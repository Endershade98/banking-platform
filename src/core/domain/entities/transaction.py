# src/core/domain/entities/transaction.py

from uuid import uuid4
from datetime import datetime, UTC
from core.domain.value_objects.money import Money
from core.domain.entities.ledger_entry import LedgerEntry  # nuova classe

class Transaction:
    
    def __init__(
        self,
        from_account_id,
        to_account_id,
        amount,
        idempotency_key=None
    ):

        self.transaction_id = str(uuid4())

        self.idempotency_key = idempotency_key

        self.from_account_id = from_account_id

        self.to_account_id = to_account_id

        self.amount = amount

        self.status = "PENDING"

        self.created_at=datetime.now(UTC)

        self.completed_at=None

        self.entries=[]

        self._validate()

    def _validate(self):
        if self.from_account_id == self.to_account_id:
            raise ValueError("Cannot transfer to the same account")
        if self.amount.amount <= 0:
            raise ValueError("Transaction amount must be positive")

    def mark_completed(self):
        self.status = "COMPLETED"
        self.completed_at = datetime.now(UTC)

    def mark_failed(self):
        self.status = "FAILED"
        self.completed_at = datetime.now(UTC)

    # -----------------------------
    # NUOVO: genera ledger entries
    # -----------------------------
    def generate_entries(self):

        if self.entries:
            return self.entries

        debit_entry = LedgerEntry(
            account_id=self.from_account_id,
            amount=self.amount.amount,
            currency=self.amount.currency,
            entry_type="debit",
            transaction_id=self.transaction_id,
        )


        credit_entry = LedgerEntry(
            account_id=self.to_account_id,
            amount=self.amount.amount,
            currency=self.amount.currency,
            entry_type="credit",
            transaction_id=self.transaction_id,
        )


        self.entries = [
            debit_entry,
            credit_entry
        ]

        return self.entries