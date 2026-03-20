import logging

import pytest
from core.domain.entities.transaction import Transaction
from core.domain.value_objects.money import Money

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

def test_transaction_negative_amount():
    try:
        transaction = Transaction(
            from_account_id="account1",
            to_account_id="account2",
            amount=Money(-50, "USD"),
        )
    except ValueError as e:        
        assert str(e) == "Money amount cannot be negative"

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

def test_transaction_completed_at():
    with pytest.raises(ValueError):
        transaction = Transaction(
            from_account_id="account1",
            to_account_id="account2",
            amount=Money(-100, "USD"),
        )