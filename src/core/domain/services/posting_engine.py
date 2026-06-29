# src/core/domain/services/posting_engine.py

from core.domain.entities.journal import Journal
from core.domain.services.ledger_validator import LedgerValidator



class PostingEngine:


    def create_journal(
        self,
        transaction
    ):


        entries = (
            transaction.generate_entries()
        )


        LedgerValidator.validate(
            entries
        )


        return Journal(
            transaction.transaction_id,
            entries
        )