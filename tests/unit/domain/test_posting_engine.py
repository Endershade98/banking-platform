# tests/unit/domain/test_posting_engine.py

from core.domain.entities.transaction import Transaction
from core.domain.value_objects.money import Money
from core.domain.services.posting_engine import PostingEngine


def test_transaction_creates_balanced_journal():

    transaction = Transaction(
        from_account_id="A",
        to_account_id="B",
        amount=Money(100, "USD")
    )


    engine = PostingEngine()

    journal = engine.create_journal(
        transaction
    )


    assert journal.transaction_id == transaction.transaction_id

    assert len(journal.entries) == 2


    debit = journal.entries[0]
    credit = journal.entries[1]


    assert debit.entry_type == "debit"
    assert credit.entry_type == "credit"


    assert debit.amount == 100
    assert credit.amount == 100