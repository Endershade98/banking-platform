import logging

from core.domain.services.transaction_service import TransactionService
from core.domain.value_objects.money import Money
from core.domain.entities.account import Account

def test_successful_transfer():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1000, "USD"))
    account2 = Account(account_id="account2", balance=Money(500, "USD"))

    transaction = service.transfer(account1, account2, Money(200, "USD"))

    assert transaction.status == "COMPLETED"
    assert account1.balance.amount == 800
    assert account2.balance.amount == 700


def test_insufficient_funds():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(100, "USD"))
    account2 = Account(account_id="account2", balance=Money(500, "USD"))

    try:
        service.transfer(account1, account2, Money(200, "USD"))
    except ValueError as e:
        assert str(e) == "Insufficient funds"
        assert account1.balance.amount == 100
        assert account2.balance.amount == 500

def test_frozen_account():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1000, "USD"), is_frozen=True)
    account2 = Account(account_id="account2", balance=Money(500, "USD"))

    try:
        service.transfer(account1, account2, Money(200, "USD"))
    except ValueError as e:
        assert str(e) == "Source account is frozen"
        assert account1.balance.amount == 1000
        assert account2.balance.amount == 500

def test_currency_mismatch():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1000, "USD"))
    account2 = Account(account_id="account2", balance=Money(500, "EUR"))

    try:
        service.transfer(account1, account2, Money(200, "USD"))
    except ValueError as e:
        assert str(e) == "Cannot add different currencies"

def test_negative_amount():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1000, "USD"))
    account2 = Account(account_id="account2", balance=Money(500, "USD"))

    try:
        service.transfer(account1, account2, Money(-50, "USD"))
    except ValueError as e:
        assert str(e) == "Money amount cannot be negative"

def test_zero_amount():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1000, "USD"))
    account2 = Account(account_id="account2", balance=Money(500, "USD"))

    try:
        service.transfer(account1, account2, Money(0, "USD"))
    except ValueError as e:
        assert str(e) == "Withdrawal amount must be positive"

def test_same_account_transfer():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1000, "USD"))

    try:
        service.transfer(account1, account1, Money(100, "USD"))
    except ValueError as e:
        assert str(e) == "Cannot transfer to the same account"

def test_large_transfer():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1_000_000, "USD"))
    account2 = Account(account_id="account2", balance=Money(500, "USD"))

    transaction = service.transfer(account1, account2, Money(500_000, "USD"))

    assert transaction.status == "COMPLETED"
    assert account1.balance.amount == 500_000
    assert account2.balance.amount == 500_500

def test_transaction_creation():
    service = TransactionService()

    account1 = Account(account_id="account1", balance=Money(1000, "USD"))
    account2 = Account(account_id="account2", balance=Money(500, "USD"))

    transaction = service.transfer(account1, account2, Money(200, "USD"))

    assert transaction.from_account_id == "account1"
    assert transaction.to_account_id == "account2"
    assert transaction.amount.amount == 200
    assert transaction.amount.currency == "USD"
    assert transaction.status == "COMPLETED"
    assert transaction.created_at is not None
    assert transaction.completed_at is not None