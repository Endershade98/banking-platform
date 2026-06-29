# tests/unit/domain/test_accounting_rules.py

import pytest

from core.domain.entities.account import Account
from core.domain.value_objects.money import Money
from core.domain.rules.accounting_rules import AccountingRules



def test_self_transfer():

    account=Account(
        account_id="1",
        balance=Money(100)
    )


    with pytest.raises(Exception):

        AccountingRules.validate_transfer(
            account,
            account,
            Money(10)
        )



def test_currency_mismatch():

    a=Account(
        balance=Money(100,"EUR")
    )

    b=Account(
        balance=Money(100,"EUR")
    )


    with pytest.raises(Exception):

        AccountingRules.validate_transfer(
            a,
            b,
            Money(10,"USD")
        )