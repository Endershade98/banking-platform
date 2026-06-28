# core/domain/entities/ledger_entry.py

from datetime import datetime, UTC
from decimal import Decimal
import uuid


class LedgerEntry:
    def __init__(
        self,
        account_id: str,
        amount: Decimal,
        currency: str,
        entry_type: str,  # "debit" | "credit"
        transaction_id: str,
        created_at: datetime | None = None,
    ):
        if entry_type not in ("debit", "credit"):
            raise ValueError("Invalid entry type")

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.entry_id = str(uuid.uuid4())
        self.account_id = account_id
        self.amount = amount
        self.currency = currency
        self.entry_type = entry_type
        self.transaction_id = transaction_id
        self.created_at = created_at or datetime.now(UTC)