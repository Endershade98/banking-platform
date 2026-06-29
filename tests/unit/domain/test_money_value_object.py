# tests/unit/domain/test_money_value_object.py

import pytest

from core.domain.value_objects.money import Money

from core.domain.exceptions.account_exceptions import (
    NegativeBalanceError
)


def test_money_addition():

    m1 = Money(100, "USD")
    m2 = Money(50, "USD")

    result = m1 + m2

    assert result.amount == 150
    assert result.currency == "USD"


def test_money_currency_mismatch():

    m1 = Money(100, "USD")
    m2 = Money(50, "EUR")

    with pytest.raises(
        ValueError,
        match="Cannot add different currencies"
    ):
        m1 + m2


def test_money_subtraction():

    m1 = Money(100, "USD")
    m2 = Money(40, "USD")

    result = m1 - m2

    assert result.amount == 60
    assert result.currency == "USD"


def test_money_negative_amount():

    with pytest.raises(
        NegativeBalanceError,
        match="Balance cannot be negative"
    ):
        Money(-10, "USD")


def test_money_repr():

    money = Money(100, "USD")

    assert repr(money) == "100 USD"