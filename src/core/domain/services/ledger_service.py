# src/core/domain/services/ledger_service.py

from core.domain.services.posting_engine import PostingEngine


class LedgerService:


    def __init__(
        self,
        ledger_repository
    ):
        self.repository = ledger_repository
        self.posting_engine = PostingEngine()



    def post_transaction_sync(
        self,
        transaction
    ):

        journal = self.posting_engine.create_journal(
            transaction
        )


        for entry in journal.entries:

            self.repository.save_sync(
                entry
            )


        return journal