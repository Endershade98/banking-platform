from core.domain.entities.account import Account
from core.domain.value_objects.money import Money


def test_account_deposit():
    account = Account(owner="alice")

    account.deposit(Money(100))

    assert account.balance.amount == 100


def test_account_withdraw():
    account = Account(owner="alice")

    account.deposit(Money(200))
    account.withdraw(Money(50))

    assert account.balance.amount == 150