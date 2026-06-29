# tests/unit/domain/test_transaction_entity.py

import pytest
from decimal import Decimal

from core.domain.entities.transaction import Transaction
from core.domain.value_objects.money import Money

from core.domain.exceptions.account_exceptions import (
    NegativeBalanceError
)


def test_transaction_negative_amount():

    with pytest.raises(NegativeBalanceError):

        Transaction(
            from_account_id="account1",
            to_account_id="account2",
            amount=Money(-50, "USD"),
        )


def test_transaction_completed_at_only_after_completion():

    transaction = Transaction(
        from_account_id="account1",
        to_account_id="account2",
        amount=Money(100,"USD"),
    )

    assert transaction.completed_at is None

    transaction.mark_completed()

    assert transaction.completed_at is not None

def test_transaction_creation():
    transaction = Transaction(
        from_account_id="account1",
        to_account_id="account2",
        amount=Money(100, "USD"),
    )

    assert transaction.from_account_id == "account1"
    assert transaction.to_account_id == "account2"
    assert transaction.amount.amount == 100
    assert transaction.amount.currency == "USD"
    assert transaction.status == "PENDING"
    assert transaction.created_at is not None
    assert transaction.completed_at is None

def test_transaction_same_account():
    try:
        Transaction(
            from_account_id="account1",
            to_account_id="account1",
            amount=Money(100, "USD"),
        )
    except ValueError as e:
        assert str(e) == "Cannot transfer to the same account"


def test_transaction_id_uniqueness():
    transaction1 = Transaction(
        from_account_id="account1",
        to_account_id="account2",
        amount=Money(100, "USD"),
    )
    transaction2 = Transaction(
        from_account_id="account3",
        to_account_id="account4",
        amount=Money(200, "USD"),
    )

    assert transaction1.transaction_id != transaction2.transaction_id

def test_transaction_timestamp():
    transaction = Transaction(
        from_account_id="account1",
        to_account_id="account2",
        amount=Money(100, "USD"),
    )

    assert transaction.created_at is not None
    assert transaction.created_at.tzinfo is not None  # Ensure it's timezone-aware

def test_transaction_status_transitions():
    transaction = Transaction(
        from_account_id="account1",
        to_account_id="account2",
        amount=Money(100, "USD"),
    )

    assert transaction.status == "PENDING"

    transaction.mark_completed()
    assert transaction.status == "COMPLETED"

    # Reset for failed test
    transaction = Transaction(
        from_account_id="account1",
        to_account_id="account2",
        amount=Money(100, "USD"),
    )

    transaction.mark_failed()
    assert transaction.status == "FAILED"


@pytest.mark.unit
def test_transaction_generate_entries():
    # Setup: creiamo una transaction
    from_account = "acc_1"
    to_account = "acc_2"
    amount = Money(amount=Decimal("100.00"), currency="USD")

    tx = Transaction(
        from_account_id=from_account,
        to_account_id=to_account,
        amount=amount
    )

    # Non ci sono entries prima di generarle
    assert tx.entries == []

    # Generiamo ledger entries
    entries = tx.generate_entries()

    # Verifica che siano due
    assert len(entries) == 2

    debit, credit = entries

    # Controlliamo i valori
    assert debit.account_id == from_account
    assert debit.amount == Decimal("100.00")
    assert debit.currency == "USD"
    assert debit.entry_type == "debit"
    assert debit.transaction_id == tx.transaction_id

    assert credit.account_id == to_account
    assert credit.amount == Decimal("100.00")
    assert credit.currency == "USD"
    assert credit.entry_type == "credit"
    assert credit.transaction_id == tx.transaction_id

    # Chiamando generate_entries di nuovo non duplica le entries
    entries2 = tx.generate_entries()
    assert entries2 is entries  # stesso oggetto