# tests/unit/domain/test_transaction_service.py

import pytest

from core.domain.services.transaction_service import TransactionService
from core.domain.entities.account import Account
from core.domain.value_objects.money import Money


def test_successful_transfer():

    service = TransactionService()

    account1 = Account(
        account_id="account1",
        balance=Money(1000, "USD")
    )

    account2 = Account(
        account_id="account2",
        balance=Money(500, "USD")
    )

    transaction = service.transfer(
        account1,
        account2,
        Money(200, "USD")
    )

    assert transaction.status == "PENDING"

    # TransactionService crea la transazione,
    # non movimenta direttamente i conti
    assert account1.balance.amount == 1000
    assert account2.balance.amount == 500

def test_transfer_creates_pending_transaction():

    service = TransactionService()


    account1 = Account(
        account_id="account1",
        balance=Money(1000,"USD")
    )

    account2 = Account(
        account_id="account2",
        balance=Money(500,"USD")
    )


    tx = service.transfer(
        account1,
        account2,
        Money(200,"USD")
    )


    assert tx.status == "PENDING"

    assert tx.from_account_id == "account1"
    assert tx.to_account_id == "account2"

    # nessuna modifica qui
    assert account1.balance.amount == 1000
    assert account2.balance.amount == 500

def test_same_account_transfer():

    service = TransactionService()


    account = Account(
        account_id="account1",
        balance=Money(1000,"USD")
    )


    with pytest.raises(
        ValueError,
        match="Cannot transfer to the same account"
    ):
        service.transfer(
            account,
            account,
            Money(100,"USD")
        )