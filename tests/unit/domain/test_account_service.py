from core.domain.entities.account import Account
from core.domain.value_objects.money import Money
from core.domain.services.account_service import AccountService


def test_transfer_between_accounts():
    a1 = Account(owner="alice")
    a2 = Account(owner="bob")

    a1.deposit(Money(200))

    AccountService.transfer(a1, a2, Money(50))

    assert a1.balance.amount == 150
    assert a2.balance.amount == 50