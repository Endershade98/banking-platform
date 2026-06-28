# src/core/domain/services/posting_engine.py

from core.domain.entities.journal import Journal


class PostingEngine:


    def create_journal(
        self,
        transaction
    ) -> Journal:


        entries = (
            transaction.generate_entries()
        )


        return Journal(
            transaction_id=
                transaction.transaction_id,

            entries=entries
        )