# src/core/domain/entities/journal.py

from decimal import Decimal

from core.domain.entities.ledger_entry import LedgerEntry
from core.domain.exceptions.ledger_exceptions import (
    UnbalancedJournalError
)


class Journal:

    def __init__(
        self,
        transaction_id: str,
        entries: list[LedgerEntry]
    ):

        if not entries:
            raise ValueError(
                "Journal requires entries"
            )

        self.transaction_id = transaction_id
        self.entries = entries

        self.validate_balance()


    def validate_balance(self):

        debit_total = self._calculate_debit()

        credit_total = self._calculate_credit()


        if debit_total != credit_total:

            raise UnbalancedJournalError(
                f"Journal not balanced. "
                f"Debit={debit_total} "
                f"Credit={credit_total}"
            )


    def _calculate_debit(self) -> Decimal:

        return sum(
            (
                entry.amount
                for entry in self.entries
                if entry.entry_type == "debit"
            ),
            Decimal("0")
        )


    def _calculate_credit(self) -> Decimal:

        return sum(
            (
                entry.amount
                for entry in self.entries
                if entry.entry_type == "credit"
            ),
            Decimal("0")
        )


    def add_entry(
        self,
        entry: LedgerEntry
    ):

        if entry.transaction_id != self.transaction_id:
            raise ValueError(
                "Entry transaction mismatch"
            )


        self.entries.append(entry)

        self.validate_balance()